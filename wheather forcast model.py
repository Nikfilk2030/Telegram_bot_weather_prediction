from wwo_hist import retrieve_hist_data
import pandas as pd
import typing as tp
from sklearn.model_selection import train_test_split

def get_the_weather_history(*args: tp.List) -> tp.NoReturn:
    hist_weather_data = retrieve_hist_data(a)

'''frequency = 3
start_date = '18-OCT-2016'
end_date = '18-OCT-2021'
api_key = 'eb17522691384ca08f4205244212010'
location_list = ['moscow']
get_the_weather_history(api_key,
                        location_list,
                        start_date,
                        end_date,
                        frequency,
                        location_label=False,
                        export_csv=True,
                        store_df=True)'''


weather_data = pd.read_csv('moscow.csv', usecols=[0, 13, 16, 17, 19, 20, 21, 23])
x = weather_data.drop(['tempC'], axis=1)
y = weather_data['tempC']
for i in x:
    print(type(i[0]))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)