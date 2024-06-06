import pytest

@pytest.fixture()
def test_login():
    print('login')


def pytest_configure(config):
    marker_list= ['search',"login"]
    for markers in marker_list:
        config.addinivalue_line(
            'markers',markers
        )
