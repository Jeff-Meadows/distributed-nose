
import unittest


class TC1(unittest.TestCase):
    def test_method1(self):
        assert True

    def test_method2(self):
        assert True

    def test_method3(self):
        assert True

    def test_method4(self):
        assert True


class TC2(TC1):
    pass


class TC3(unittest.TestCase):
    _distributed_can_split_ = False

    def test_method1(self):
        assert True

    def test_method2(self):
        assert True

    def test_method3(self):
        assert True

    def test_method4(self):
        assert True


def test_func1():
    assert True


def test_func2():
    assert True
