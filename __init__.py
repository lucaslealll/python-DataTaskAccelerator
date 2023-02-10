# flake8: noqa

"""
dta
~~~
"""


__version__ = "1.0.0"
__author__ = "Lucas Omar Andrade Leal"

from .bigquery import sync_data_types_bq
from .examples.exceptions import (
    CellNotFound,
    GSpreadException,
    IncorrectCellLabel,
    NoValidUrlKeyFound,
    SpreadsheetNotFound,
    WorksheetNotFound,
)
from .gsheets import (
    connect_gsheets,
    get_cell_data,
    get_worksheet,
    get_worksheet_dedup,
    get_worksheet_df,
    get_worksheet_next_avaible_row,
    get_worksheet_sort_jobdt_and_dedup,
    gsheets_dedup_ids_and_update,
    gsheets_worksheet_update,
)
from .messenger import send_alert_email, send_email
from .selenium import import_cookies
from .timer import pls_wait
from .utils import check_file_exists, delete_file, get_config_dir, rename_file
