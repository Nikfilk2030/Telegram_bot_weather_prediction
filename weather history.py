from wwo_hist import retrieve_hist_data
import typing as tp

def get_cities_list(file: str) -> tp.List[str]:
    with open(file) as f:
        l = [row.strip() for row in f.readlines()]
    return l


frequency = 3
start_date = '18-OCT-2020'
end_date = '18-OCT-2021'
api_key = 'eb17522691384ca08f4205244212010'
location_list = get_cities_list('cities.txt')
retrieve_hist_data(api_key,
                        location_list,
                        start_date,
                        end_date,
                        frequency,
                        location_label=False,
                        export_csv=True,
                        store_df=True)