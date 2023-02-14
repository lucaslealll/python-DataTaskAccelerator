"""timer.py"""

from datetime import datetime
from time import sleep


class Timer:
    """Timer class"""

    # pylint: disable=too-many-instance-attributes

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
        """Shows a progress bar while waiting x seconds

        By default:
            - sec = 1

        >>> waiting(5)
        |██████____|100% 6/10s [08 Feb,2023 10:19:49<10:19:59]
        """

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
