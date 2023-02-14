"""Unit tests for timer"""
import pytest

from data_task_accelerator.timer import Timer


def test_value_input_valid():
    """Input seconds value is invalid"""
    with pytest.raises(ValueError) as execinfo:
        print(type(Timer.pls_wait(5)))
        assert type(Timer.pls_wait(5)) == "function"
    assert str(execinfo.value) == "Input seconds value is invalid. Try integer values."
