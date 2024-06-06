import pytest
import allure

@allure.feature('denglu')
class TestLogin():
    @allure.story('登录成功')
    def test_login_success(self):
        print('测试用例登录成功')
        pass

    @allure.story('登录失败')
    def test_login_fail(self):
        print('测试用例登录失败')
        pass

    @allure.story('用户名缺失')
    def test_name_less(self):
        print('测试用例缺少用户名')
        pass

    @allure.story('密码缺失')
    def test_password_less(self):
        with allure.step('点击用户名'):
            print('请输入用户名')
        with allure.step('点击密码'):
            print('请输入密码')
        print('点击登录')
        with allure.step('点击登录后登录失败'):
            assert '1'==1
            print('登录失败')

        pass

    @allure.story('登录失败')
    def test_password_fail(self):
        print('用例登录失败')
        pass


if __name__ == '__main__':
    pytest.main()