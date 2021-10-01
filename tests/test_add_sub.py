import add_sub


class Test_add_sub:

    @staticmethod
    def test_add():
        assert add_sub.addition(3, 2) == 5

    @staticmethod
    def test_sub():
        assert add_sub.subtraction(3, 2) == 1