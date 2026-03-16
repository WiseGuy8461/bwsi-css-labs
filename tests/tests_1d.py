
import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([3,2,7,30,4], 9) == [1,2]
    assert two_sum([0,0,0,3,-2], 1) == [3,4]

if __name__ == "__main__":
    pytest.main()