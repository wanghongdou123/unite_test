import pytest

def test_one(test_login):
    print('test_one要登录')
    a = 'hello'
    assert 'e' in a

def test_two():
    print('test_two不需要登录')
    a = 'hello'
    assert 'l' in a

def test_three(test_login):
    print('test_three要登录')
    a = 'hello'
    assert 'o' in a


if __name__ == '__main__':
    pytest.main()