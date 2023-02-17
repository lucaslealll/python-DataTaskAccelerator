"""Unit tests for timer"""
from data_task_accelerator.messenger import send_email


def test_sendmail_function():
    """Input seconds value is invalid"""
    assert (
        send_email(
            from_addr="jack_saur@gmail.com",
            from_psswd="dshrnliru83no10d",
            to_addr="daniels_raptor@gmail.com",
            msg_subject="Lorem",
            msg_body="Lorem ipsum dolor sit amet...",
        )
        == None
    )
