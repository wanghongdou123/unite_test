import pytest
import allure


def test_success():
    assert True


def test_failure():
    assert False


def test_skip():
    pytest.skip('for a reason')



def test_broken():
    raise Exception('oops')