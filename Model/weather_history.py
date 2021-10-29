from wwo_hist import retrieve_hist_data
import typing as tp
import os


def get_cities_list(file: str) -> tp.List[str]:
    with open(file) as f:
        l = [row.strip() for row in f.readlines()]
    return l


def get_history_data(frequency: int, start_date: str, end_date: str, api_key: str, cities_list_filename: str,
                     dir: str) -> tp.NoReturn:
    cities_list = get_cities_list(cities_list_filename)
    os.chdir(dir + '\\')
    retrieve_hist_data(api_key,
                       cities_list,
                       start_date,
                       end_date,
                       frequency,
                       location_label=False,
                       export_csv=True,
                       store_df=True)
    os.chdir('..')
