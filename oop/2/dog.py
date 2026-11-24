class Dog:
    """元気度（_genki）を持ち、吠えたり餌を食べたりできる犬を表すクラス。"""

    def __init__(self, name: str):
        """犬の名前と初期の元気度を設定する。

        Args:
            name: 犬の名前。
        """
        self.name = name
        self._genki = 3

    def bark(self) -> str:
        """元気度があれば吠え、なければ疲れたメッセージを返す。

        元気度が1以上ある場合は1消費して鳴き声を返し、
        0以下の場合は疲れた旨の文字列を返す。

        Returns:
            鳴き声または疲れたことを示すメッセージ。
        """
        if self._genki > 0:
            self._genki -= 1
            return self.name + ":[ワン]"
        return self.name + "は疲れたようです"

    def eat(self) -> str:
        """餌を食べて元気度を1増やし、メッセージを返す。

        Returns:
            餌を食べたことを示すメッセージ。
        """
        self._genki += 1
        return self.name + "は餌を食べて少し元気になったみたいです"

if __name__ == "__main__":
    print("ポチは疲れるまで吠え続けます")
    pochi = Dog("ポチ")
    for _ in range(4):
        print(pochi.bark())

    print(pochi.eat())
    print(pochi.bark())

