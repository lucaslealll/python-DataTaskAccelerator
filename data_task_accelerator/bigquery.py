"""
dta.bigquery
~~~~~~~~~~~~
"""
import numpy as np
import pandas as pd
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account


def sync_data_types_bq(df, db_project_id, table, auth_file, debug=False):
    """Synchronizes the data types of each column of the current dataframe with the respective types of the columns of the sending database and returns the typed dataframe.

    Parameters
    ----------
    `auth_file` : credentials to authorize project access on the google platform
    `db_project_id`: Google Cloud Compute project identification number
    `df`: the dataframe "object" so the function can transfer sync
    `table`: the "table" of the database so that the function can identify the data type

    By default:
        - debug : False
        - datetime format : Y-m-d H:M:S [2023-02-15 11:32:15]

    Examples
    --------
    Synchronize the data types of the dataframe "purchases" with the respective table

    >>> purchases = sync_data_types(purchases, "purchases-341256", "purchases-341256.month_shopping", f"{SRC_PATH}auth_file.json")
    """
    auth = service_account.Credentials.from_service_account_file(auth_file)

    pandas_gbq.context.project = db_project_id
    client = bigquery.Client(credentials=auth, project=db_project_id)

    table = client.get_table(table)

    generated_schema = [{"name": i.name, "type": i.field_type} for i in table.schema]

    dict = {
        "STRING": str,
        "INTEGER": np.int64,
        "FLOAT": float,
    }

    for dtype in generated_schema:
        if debug == True:
            print(dtype)
        else:
            pass
        if dtype["type"] == "DATE":
            df[dtype["name"]] = pd.to_datetime(
                df[dtype["name"]], format="%Y-%m-%d", errors="coerce"
            )
        elif "_id" in dtype["name"]:
            df[dtype["name"]] = df[dtype["name"]].astype(str)
        elif dtype["name"] == "cost_per_thruplay":
            df[dtype["name"]] = df[dtype["name"]].astype(float)
        elif dtype["type"] == "TIMESTAMP":
            df[dtype["name"]] = pd.to_datetime(
                df[dtype["name"]], format="%Y-%m-%d %H:%M:%S", errors="ignore"
            )
        else:
            df[dtype["name"]] = df[dtype["name"]].astype(dict[dtype["type"]])

    return df
