"""Unit tests for timer"""
import pytest

from data_task_accelerator.timer import pls_wait, get_time_now

def test_pls_wait_seconds_input():
    """Input seconds value is invalid"""
    assert pls_wait(1) == None

def test_if_input_is_str():
    """Input date/time value is invalid"""
    assert type(get_time_now("%D")) == str
