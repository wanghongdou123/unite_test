import pytest
import sys


@pytest.mark.parametrize("test_input,expected",[('3+5',8),('2+3',5)])
def test_eval(test_input,expected):

    # eval是将字符串str当成有效的表达式来求值，并返回结果
    print(eval(test_input))
    assert eval(test_input) == expected



# 参数组合
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,9,10])
def test_foo(x,y):
    print(f"测试数据组合x{x},y{y}")



# 方法名作为参数
test_user_data = ["tom","jerry"]
@pytest.fixture(scope='module')
def login_r(request):
    # 这是接收并传入的参数
    user = request.param
    print(f'\n 打开首页准备登录，登录用户{user}')
    return user


# @pytest.mark.xfail
# @pytest.mark.skip('此次测试不执行')
@pytest.mark.skipif(sys.platform == 'darwin',reason='不在mac上执行')
# indirect=True可以把传过来的参数当函数执行
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f'测试用例中login返回的值是:{a}')
    assert a != ''



if __name__ == '__main__':
    pytest.main()
