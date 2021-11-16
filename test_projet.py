
import builtins
import pytest
import mock
from main import *
from src import *

def test_main():
    with mock.patch.object(builtins, 'input', lambda _: 'nineteen'):
        with pytest.raises(TypeError):
            prog()

    with mock.patch.object(builtins, 'input', lambda _: '8'):
        with pytest.raises(ValueError):
            prog()
                

