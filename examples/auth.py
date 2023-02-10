"""
dta.auth
~~~~~~~~
"""

import gspread
import sqlalchemy

L_TASK = ("LOAD").ljust(11)


class SqlServerConnection:
    def __init__(
        self,
        client_name,
        db_name,
        jbdt,
        password,
        project_id,
        script_filename,
        server_name,
        username,
    ):
        self.client = client_name
        self.database = db_name
        self.jobdate = jbdt
        self.password = password
        self.project_id = project_id
        self.script = script_filename
        self.server = server_name
        self.user = username

    def connect_sqlserver(self):
        global ENGINE
        ENGINE = sqlalchemy.create_engine(
            f"""mssql+pyodbc:///?odbc_connect=DRIVER={{ODBC Driver 17 for SQL Server}}; Server={self.server}; Database={self.database}; Uid={self.user}; Pwd={self.password};""",
            fast_executemany=True,
        )
        return ENGINE

    def disconnect_sqlserver(self):
        ENGINE.connect().close()
        ENGINE.connect().invalidate()
        ENGINE.dispose()


class GsheetsConnection:
    def __init__(self, gsheets_credentials):
        self.credentials = gsheets_credentials

    def connect_gsheets(self):
        google_sheets = gspread.authorize(self.credentials)
        return google_sheets
