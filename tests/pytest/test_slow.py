import pytest
import time


@pytest.mark.parametrize('_', range(5))
def test_slow(_):
    time.sleep(1)
