import unittest
from dog import Dog

class TestDog(unittest.TestCase):
    """Dogクラスの振る舞いを検証するユニットテスト。"""

    def setUp(self):
        """各テストの前に新しいDogインスタンスを用意する。"""
        self.dog = Dog("ポチ")

    def test_initial_state(self):
        """初期状態で名前と元気度が正しく設定されていること。"""
        self.assertEqual(self.dog.name, "ポチ")
        self.assertEqual(self.dog.genki, 3)

    def test_genki_is_read_only(self):
        """genkiプロパティを外部から直接変更しようとするとエラーになること。"""
        with self.assertRaises(AttributeError):
            self.dog.genki = 10

    def test_bark_decreases_genki_and_returns_message(self):
        """元気度があるときに吠えると元気度が1減り、鳴き声を返すこと。"""
        message = self.dog.bark()
        self.assertEqual(message, "ポチ:[ワン]")
        self.assertEqual(self.dog.genki, 2)

    def test_bark_until_tired(self):
        """元気度が0になると疲れたメッセージを返し、0未満にならないこと。"""
        for _ in range(3):
            self.dog.bark()

        tired_message = self.dog.bark()
        self.assertEqual(tired_message, "ポチは疲れたようです")
        self.assertEqual(self.dog.genki, 0)

    def test_eat_increases_genki_and_allows_barking_again(self):
        """餌を食べると元気度が1増え、疲れたあとも再び吠えられること。"""
        for _ in range(4):
            self.dog.bark()

        eat_message = self.dog.eat()
        self.assertEqual(eat_message, "ポチは餌を食べて少し元気になったみたいです")
        self.assertEqual(self.dog.genki, 1)

        bark_message = self.dog.bark()
        self.assertEqual(bark_message, "ポチ:[ワン]")
        self.assertEqual(self.dog.genki, 0)


if __name__ == "__main__":
    unittest.main()
