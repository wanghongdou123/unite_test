import pytest

@pytest.fixture()
def test_login():
    print('login')

class TestDemo():
    def setup_module(self):
        print('这是setup_module方法')


    def teardown_module(self):
        print("这是teardown_module方法")


    def setup_function(self):
        print("setup_function")


    def teardown_module(self):
        print("teardown_module")


    def setup_class(self):
        print("setup_class")


    def teardown_class(self):
        print("teardown_class")


    def setup_method(self):
        print("setup_method")


    def teardown_method(self):
        print("teardown_method")


    def setup(self):
        print("setup")


    def teardown(self):
        print("teardown")


    def test_one(self):
        print('test_one要登录')
        a = 'hello'
        assert 'e' in a

    def test_two(self):
        print('test_two不需要登录')
        a = 'hello'
        assert 'l' in a

    def test_three(self):
        print('test_three')
        a = 'hello'
        assert 'o' in a


if __name__ == '__main__':
    pytest.main(['-vs'])
