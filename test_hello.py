import pytest

from hello import hw

class TestHello(object):
    """
    Test suite for hw
    """
    def test_hw(self):
        assert "hello world" == hw()
