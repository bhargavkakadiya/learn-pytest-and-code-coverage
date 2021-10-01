import mul_div


class Test_mul_div:

    @staticmethod
    def test_mul():
        assert mul_div.multiplication(3, 2) == 6

    @staticmethod
    def test_div():
        assert mul_div.division(4, 2) == 2