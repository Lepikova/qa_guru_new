import pytest


@pytest.mark.first
def test_first():
    assert "hello" in "hello word"


@pytest.mark.second
def test_second():
    assert len("hello") == 5
