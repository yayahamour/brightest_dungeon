import pytest
import mock
import main

@pytest.mark.parametrize("result")
def fire_scroll_test():
    pass


def test_main():
    with mock.patch.object(__builtins__, 'input', lambda : 'sdfsd'):          
        assert main() == ValueError
        
    with mock.patch.object(__builtins__, 'input', lambda : '2545'):
        assert main() == 'Wrong number'


