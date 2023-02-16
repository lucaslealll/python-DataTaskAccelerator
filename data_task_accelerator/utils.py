"""
dta.utils
~~~~~~~~~
"""

import datetime
import glob
import os
import subprocess
from datetime import datetime
from time import sleep

from cairo import Path

E_STR_PREFIX = ("EXTRACT").ljust(11)
RM_STR_PREFIX = ("REMOVE").ljust(11)
RNM_STR_PREFIX = ("RENAME").ljust(11)
T_STR_PREFIX = ("TRANSFORM").ljust(11)


def get_config_dir(config_dir_name="dta", os_is_windows=os.name == "nt"):
    """Construct a config dir path.

    By default:
        - `%APPDATA%\dta` on Windows
        - `~/.config/dta` everywhere else
    """
    if os_is_windows:
        return Path(os.environ["APPDATA"], config_dir_name)
    else:
        return Path(Path.home(), ".config", config_dir_name)


DEFAULT_CONFIG_DIR = get_config_dir()

DEFAULT_FILE_DIR_PATH = DEFAULT_CONFIG_DIR
DEFAULT_FILENAME = DEFAULT_CONFIG_DIR / "filename.txt"
DEFAULT_NEW_FILENAME = DEFAULT_CONFIG_DIR / "new_filename.txt"


def rename_file(
    path=DEFAULT_FILE_DIR_PATH,
    filename=DEFAULT_FILENAME,
    new_filename=DEFAULT_NEW_FILENAME,
) -> None:
    """Rename a file.

    Parameters
    ----------
    `path` : Full file path.
    `filename` : Full filename or its prefix.
    `new_filename` : The new name to assign to this file

    Examples
    --------
    Rename a file called test.csv to newname.csv

    >>> rename_file("/home/computer/Desktop/finalFolder", "test.csv", "newname.csv")
    """
    for file in glob.glob(f"{path}{filename}*"):
        name = file
    os.rename(f"{name}", f"{path}{new_filename}")
    return None


def delete_file(path=DEFAULT_FILE_DIR_PATH, filename=DEFAULT_FILENAME) -> None:
    """Delete a file.

    Parameters
    ----------
    `path` : Full file path.
    `filename` : Full filename or its prefix.

    Examples
    --------
    Delete a file called test.csv

    >>> delete_file("/home/computer/Desktop/finalFolder", "test.csv")
    """
    subprocess.getoutput(f"rm {path}{filename}")
    return None


def check_file_exists(
    path=DEFAULT_FILE_DIR_PATH,
    filename=DEFAULT_FILENAME,
    min_file_size=1,
    timeout=15,
) -> bool:
    """Checks the existence of a file, returning True or False.

    Parameters
    ----------
    `path` : Full file path.
    `filename` : Full filename or is prefix.
    `min_file_size` : The minimum size of a file to be able to use it
    `timeout` : Maximum waiting time to find the file

    By default:
        - `min_file_size` : is considered 1
            - must be informed in bytes
        - `timeout` : wait 15 seconds

    Examples
    --------
    Looking for a file that actually exists, called "teste.txt", with a minimum of 100 Bytes and waiting a maximum of 10 seconds

    >>> file_exists("/home/computer/Desktop/finalFolder", "test", 100, 10)
    >>> True
    """

    fully_downloaded_file = False
    start_time = int((datetime.now()).strftime("%H%M%S"))
    current_time = start_time
    stop_time = start_time + timeout

    while fully_downloaded_file == False:
        try:
            for file in glob.glob(f"{path}{filename}*"):
                pwd_file = str(file)

            file_exists = os.path.isfile(f"{pwd_file}")

            if file_exists == True:
                file_size_bytes = int(os.stat(f"{pwd_file}").st_size)

                if file_size_bytes < min_file_size:
                    sleep(1)
                elif file_size_bytes >= min_file_size:
                    fully_downloaded_file = True
                    return fully_downloaded_file
        except:
            current_time = int((datetime.now()).strftime("%H%M%S"))
            if fully_downloaded_file == False and current_time >= stop_time:
                return fully_downloaded_file


def get_current_script_name() -> str:
    return str(os.path.basename(__file__))


"""
lista_de_listas = [
    list_comments_content,
    list_likes_content,
    list_reach,
    list_shares,
    list_views,
]

for lista in lista_de_listas:
    lista = lista
    print(f"{lista}")
i = 0
for lista in lista_de_listas:
    lista_final = lista

    item_da_aux_list = []
    final_metrics_list = []

    for valor in lista:
        valor = valor.replace(",", "")
        valor = valor.replace("--", "0")
        valor = valor.split(" ")[0]

        if "K" in valor:
            valor = valor.replace("K", "")
            valor = float(valor) * 1000
        else:
            if "M" in valor:
                valor = valor.replace("M", "")
                valor = float(valor) * 1000000

        item_da_aux_list.append(float(valor))
        lista_final = item_da_aux_list

    lista_de_listas[i] = lista_final

i = i + 1
for i in lista_de_listas:
    a = i
    print(a)
"""
