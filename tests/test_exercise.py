import pytest
from src.exercise import greatest

def test_exercise():
    assert greatest(3,2,6) == 6
    assert greatest(2,7,4) == 7
