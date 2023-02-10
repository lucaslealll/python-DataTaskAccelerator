"""
dta.timer
~~~~~~~~~

Simple time management.

"""

from datetime import datetime
from time import sleep


def pls_wait(sec=1):
    """Shows a progress bar while waiting x seconds

    By default:
        - sec = 1

    >>> waiting(5)
    |██████____|100% 6/10s [08 Feb,2023 10:19:49<10:19:59]
    """
    start_datetime = datetime.now().strftime("%d %b,%Y %H:%M:%S")

    for i in range(sec + 1):
        fill_bar = i
        fill_points = sec - i

        percent = int((i * 100) / sec)
        current_datetime = datetime.now().strftime("%H:%M:%S")
        print(
            f"|{'█' * fill_bar}{'_' * fill_points}|{percent}% {i}/{sec}s [{start_datetime}<{current_datetime}]",
            end="\r",
            flush=True,
        )
        sleep(1)

    return None
