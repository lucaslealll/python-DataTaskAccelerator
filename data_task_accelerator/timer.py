"""timer.py"""

from datetime import datetime
from time import sleep


def get_time_now(format="%d %b,%Y %H:%M:%S") -> str:
    """Return the day, month, year, hour, minute and seconds.

    By default:
        - strftime : %d %b,%Y %H:%M:%Su

    >>> date = get_time_now()
    '15 Feb,2023 15:28:48'

    >>> date = get_time_now("%D")
    '02/15/23'

    >>> date = get_time_now("%H:%M")
    '15:35'
    """
    if not isinstance(format, str):
        raise TypeError("Value is invalid. Use string to specify the output format")

    return datetime.now().strftime(format)


def pls_wait(sec=1) -> None:
    """Shows a progress bar while waiting x seconds.

    By default:
        - sec : 1

    >>> waiting(5)
    |██████____|100% 6/10s [08 Feb,2023 10:19:49<10:19:59]
    """
    # Validate time value
    if not isinstance(sec, int):
        raise TypeError("Time value is invalid. Use integer value to specify seconds")

    start_datetime = get_time_now()

    for i in range(sec + 1):
        percent = int((i * 100) / sec)
        current_datetime = get_time_now()
        print(
            f"|{'█' * i}{'_' * (sec-i)}|{percent}% {i}/{sec}s [{start_datetime}<{current_datetime}]",
            end="\r",
            flush=True,
        )
        sleep(1)
    print(flush=True)

    return None


"""
class Timer:
    \"""Timer class\"""

    def __init__(self, seconds: int) -> None:
        super().__init__()

        # Validate time value
        value = isinstance(seconds, int)
        if type(value) != seconds:
            raise ValueError(
                "Time value is invalid. Use integer value to specify seconds"
            )

        # Map class arguments to private variables
        self._seconds = seconds

        # Statistical variables
        self.start_time = None

    # Public functions
    def pls_wait(self, sec=1):
        \"""Shows a progress bar while waiting x seconds

        By default:
            - sec = 1

        >>> waiting(5)
        |██████____|100% 6/10s [08 Feb,2023 10:19:49<10:19:59]
        \"""

        def get_time_now():
            return datetime.now().strftime("%d %b,%Y %H:%M:%S")

        start_datetime = get_time_now()

        for i in range(sec + 1):
            percent = int((i * 100) / sec)
            current_datetime = get_time_now()
            print(
                f"|{'█' * i}{'_' * (sec-1)}|{percent}% {i}/{sec}s [{start_datetime}<{current_datetime}]",
                end="\r",
                flush=True,
            )
            sleep(1)
"""
