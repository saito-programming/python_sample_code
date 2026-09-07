import redis
import evdev
from evdev import InputDevice, ecodes

# Redis接続設定
r = redis.Redis(host='localhost', port=6379, db=0)

def find_mouse_device():
    """システムに接続されているマウスデバイスを検索"""
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        # デバイスの機能をチェック（EV_KEY capabilities）
        capabilities = device.capabilities()
        if ecodes.EV_KEY in capabilities:
            # 左クリック(BTN_LEFT)をサポートしているデバイスを選択
            if ecodes.BTN_LEFT in capabilities[ecodes.EV_KEY]:
                return device
    return None

def main():
    try:
        r.ping()
        print("Redisへの接続成功")
    except Exception as e:
        print(f"Redis接続エラー: {e}")
        return

    device = find_mouse_device()
    if not device:
        print("マウスデバイスが見つかりませんでした。")
        print("/dev/input/event* へのアクセス権限を確認してください。")
        return

    print(f"使用デバイス: {device.name} ({device.path})")
    print("監視を開始しました (Ctrl+C で終了)")

    try:
        # デバイスの入力イベントをループ監視
        for event in device.read_loop():
            # キー/ボタンイベントかつ、ボタンが押された瞬間(value == 1)を検知
            if event.type == ecodes.EV_KEY and event.value == 1:
                # 左クリック・右クリック・中クリックのどれか
                if event.code in (ecodes.BTN_LEFT, ecodes.BTN_RIGHT, ecodes.BTN_MIDDLE):
                    new_count = r.incr('mouse_clicks')
                    print(f"Total Clicks: {new_count}")

    except KeyboardInterrupt:
        print("\n監視を停止しました。")
    except PermissionError:
        print(f"\nエラー: {device.path} の読み取り権限がありません。")
        print("`sudo usermod -aG input $USER` を実行して再ログインするか、sudoで実行してください。")

if __name__ == "__main__":
    main()
