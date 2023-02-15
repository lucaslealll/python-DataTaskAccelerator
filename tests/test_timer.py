"""Unit tests for timer"""
import pytest

from data_task_accelerator.timer import pls_wait, get_time_now


def test_if_input_is_int():
    """Input seconds value is invalid"""
    with pytest.raises(ValueError) as execinfo:
        assert pls_wait(5)
    assert str(execinfo.value) == "Input seconds value is invalid. Try integer values."


def test_if_input_is_str():
    """Input date/time value is invalid"""
    with pytest.raises(ValueError) as execinfo:
        assert get_time_now("%D")
    assert str(execinfo.value) == "Input seconds value is invalid. Try string values."
