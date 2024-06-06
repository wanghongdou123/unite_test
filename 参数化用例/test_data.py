import pytest
import yaml

class TestData:

    @pytest.mark.parametrize("a,b",yaml.safe_load(open("./test.yaml")))
    def test_data(self,a,b):
        sum = a + b
        print(sum)
