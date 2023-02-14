"""
dta.gsheets
~~~~~~~~~~~

This module contains common gsheets' models.

"""
import gspread
import pandas as pd


def connect_gsheets(auth):
    gsheets = gspread.authorize(auth)
    return gsheets


def get_worksheet(auth, worksheet_name, sheet_name, head_row=1):
    """Import a worksheet object from gsheets.

    Parameters
    ----------
    `auth` : Credentials to authorize project access on the google platform
    `worksheet_name` : name of the worksheet you want to get information about
    `sheet_name` : sheet page name you want to get data from
    `head_row` : row where data header starts

    By default:
        - `head_row` : is considered 1

    Examples
    --------
    Get the Google Sheets worksheet object

    >>> worksheet = get_gsheets_worksheet(GSHEETS_CREDENTIAL, "worksheet name", "data page name", 6)
    """
    gsheets = connect_gsheets(auth)
    wks = (
        gsheets.open(worksheet_name)
        .worksheet(sheet_name)
        .get_all_records(head=head_row)
    )
    return wks


def get_worksheet_df(auth, worksheet_name, sheet_name, head_row=1):
    """Import a worksheet object from gsheets as a pandas dataframe.

    Parameters
    ----------
    `auth` : Credentials to authorize project access on the google platform
    `worksheet_name` : name of the worksheet you want to get information about
    `sheet_name` : sheet page name you want to get data from
    `head_row` : row where data header starts

    By default:
        - `head_row` : is considered 1

    Examples
    --------
    Get the Google Sheets worksheet object

    >>> worksheet = get_gsheets_worksheet_dataframe(GSHEETS_CREDENTIAL, "worksheet name", "data page name", 6)
    """
    wks = get_worksheet(auth, worksheet_name, sheet_name, head_row)
    df = pd.DataFrame(wks.get_all_records(head=head_row))
    return df


def get_cell_data(
    auth,
    worksheet_name,
    sheet_name,
    sheet_id_col,
    sheet_col,
    id,
):
    """Retrieve a specific cell data.

    Parameters
    ----------
    `auth` : Credentials to authorize project access on the google platform
    `worksheet_name` : name of the worksheet you want information about
    `sheet_name` : sheet page name you want to get data from
    `sheet_id_col`: name of the column where the cell identifier is
    `sheet_col`: name of the column where the content is
    `id`: identifier the cell which you want to be required

    Examples
    --------
    Retrieve cell data content

    >>> data = get_cell_data(auth, "spreadsheet", "spreadsheet page", "ID", "Tokens", "TokenWebsite")
    >>> mndhd6105mfyd62lf~f-=h023u3rnggsds72y23nfgm,gfpsiqy2mt
    """
    sheet = get_worksheet_df(auth, worksheet_name, sheet_name)
    content = str(sheet[sheet[sheet_id_col] == id][sheet_col].item())
    return content


def get_worksheet_dedup(
    auth,
    col_subset,
    worksheet_name,
    sheet_name,
    keep_option="first",
    first_cell="A1",
    last_cell="ZZ",
):
    """Returns dataframe where the column passed as parameter is considered the core set for duplicate data row remover.

    Parameters
    ----------
    `auth` : Credentials to authorize project access on the google platform
    `col_subset`: column(s) to consider to check for duplicate data in it
    `worksheet_name` : name of the worksheet you want information about
    `sheet_name` : sheet page name you want to get data from

    By default:
        - `keep_option` : Line 1 as data to be kept
        - `first_cell` : Cell "A1" as the starting point for dataframe cleaning and reordering
        - `last_cell` : The cell "ZZ" as the endpoint for dataframe cleaning and reordering

    Examples
    --------
    Get the Google Sheets worksheet object

    >>> dedup_dataframe = gsheets_dedup(GSHEETS_CREDENTIAL, "post_title", "facebook_posts", "all_posts", "last", "A5")
    """
    wks = get_worksheet(auth, worksheet_name, sheet_name)
    df = get_worksheet_df(auth, worksheet_name, sheet_name)
    df = df.astype(str).drop_duplicates(subset=col_subset, keep=keep_option)
    df.batch_clear([f"{first_cell}:{last_cell}"])
    wks.update(
        f"{first_cell}",
        df.values.tolist(),
        value_input_option="USER_ENTERED",
    )
    return df


def get_worksheet_sort_jobdt_and_dedup(
    auth,
    col_subset,
    worksheet_name,
    sheet_name,
    first_cell="A1",
    jobdate_col="jobdate",
):
    """Returns dataframe where the column passed as parameter is considered the core set for duplicate data row remover. After, sor considering "jobdate" column

    Parameters
    ----------
    `auth` : Credentials to authorize project access on the google platform
    `col_subset`: column(s) to consider to check for duplicate data in it
    `worksheet_name` : name of the worksheet you want information about
    `sheet_name` : sheet page name you want to get data from

    By default:
        - `jobdate_col_name` : "jobdate"
        - `keep_option` : Line 1 as data to be kept
        - `first_cell` : Cell "A1" as the starting point for dataframe cleaning and reordering
        - `last_cell` : The cell "ZZ" as the endpoint for dataframe cleaning and reordering

    Examples
    --------
    Get the Google Sheets worksheet object

    >>> dedup_dataframe = gsheets_sort_jobdate_and_dedup(GSHEETS_CREDENTIAL, "post_title", "facebook_posts", "all_posts", "last", "A5", "jobdate")
    """
    wks = get_worksheet(auth, worksheet_name, sheet_name)
    df = pd.DataFrame(worksheet_name.get_all_records(head=1))
    df[jobdate_col] = df[jobdate_col].astype("datetime64[ns]")
    df = (
        df.sort_values(by=[jobdate_col], ascending=False)
        .astype(str)
        .drop_duplicates(subset=col_subset, keep="first")
    )
    wks.batch_clear([f"{first_cell}:ZZ"])
    wks.update(
        f"{first_cell}",
        df.values.tolist(),
        value_input_option="USER_ENTERED",
    )
    return None


def get_worksheet_next_avaible_row(worksheet, col):
    """
    Return the ID of the next cell into which data can be entered

    Parameters
    ----------
    `worksheet` : the worksheet "object" so that the function can identify the data
    `col` : column which function should be considered to check cell continuity

    Examples
    --------
    Get, from the facebook posts spreadsheet, in the column where the comments of all the posts are, the next line where the new data can be inserted

    >>> dataframe = gsheets_worksheet_next_avaible_row(worksheet, "A")
    >>> A237
    """
    string_list = list(filter(None, worksheet.col_values(2)))
    last_row_plus_one = str(len(string_list) + 1)
    return str(col + last_row_plus_one)


def gsheets_worksheet_update(worksheet, current_dataframe, pivot_col):
    """
    Update a Google Sheets spreadsheet from a reference column

    Parameters
    ----------
    `worksheet`: the "object" of the worksheet so that the function can identify the data
    `current_dataframe`: the dataframe "object" so the function can transfer to the worksheet
    `pivot_col`: column which the function must be considered to establish the upload

    Examples
    --------
    Upload the face dataframe data, in the facebook statistics worksheet, considering the pivot column "A3"

    >>> gsheets_worksheet_update(worksheet, facebook_metrics_dataframe, "A3")
    """
    current_dataframe = current_dataframe.astype(str)

    worksheet.update(
        f"{pivot_col}",
        current_dataframe.values.tolist(),
        value_input_option="USER_ENTERED",
    )
    return None


def gsheets_dedup_ids_and_update(worksheet, sheet, dataframe, auth):
    """Updates the Google Sheets spreadsheet where the column "id" is core set for row removal of duplicate data.

    Parameters
    ----------
    `worksheet`: name of the worksheet you want information about
    `sheet`: sheet page name you want to get data from
    `dataframe`: the dataframe "object" so the function can transfer to the worksheet
    `auth` : Credentials to authorize project access on the google platform

    Examples
    --------
    Deduplicates data from the "main" worksheet

    >>> gsheets_dedup_ids_and_update("brandwatch_data", "main", dataframe_main, auth)
    """

    wks = get_worksheet(auth, worksheet, sheet)
    df = pd.DataFrame(wks.get_all_records(head=1))
    df = df.astype(str)

    dataframe = dataframe.astype(str)

    ids = df["id"].unique()
    ids = list(filter(None, ids))

    final_ids = dataframe["id"].unique()
    final_ids = list(filter(None, final_ids))
    final_ids = [x for x in final_ids if x not in ids]

    dataframe = dataframe[dataframe["id"].isin(final_ids)]

    next_row = get_worksheet_next_avaible_row(wks, "A")

    wks.update(
        f"{next_row}",
        dataframe.values.tolist(),
        value_input_option="USER_ENTERED",
    )
    return None
