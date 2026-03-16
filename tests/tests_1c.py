
import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([-5,5,-5,5,-5,2,2,-1,3]) == 6

if __name__ == "__main__":
    pytest.main()