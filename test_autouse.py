import pytest

# 每个方法前执行
@pytest.fixture(autouse=True)
def open():
    print('打开浏览器')



def test_search1(open):
    print('test_search1')
    raise NameError
    pass

def test_search2(open):
    print('test_search2')


if __name__ == '__main__':
    pytest.main()