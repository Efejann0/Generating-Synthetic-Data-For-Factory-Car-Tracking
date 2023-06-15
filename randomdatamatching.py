from enum import Enum
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
import random

number_of_fabrics_in_the_factory = 18

now_date = datetime.now()
time = now_date - relativedelta(months=4)

Route_1 = [2, 3, 4]
Route_2 = [2, 4, 3]
Route_3 = [3, 4, 2]
Route_4 = [3, 2, 4]
Route_5 = [4, 3, 2]
Route_6 = [4, 2, 3]
Route_7 = [4, 3]
Route_8 = [4, 2]
Route_9 = [2, 3]
Route_10 = [2, 4]
Route_11 = [3, 2]
Route_12 = [3, 4]
Route_13 = [2]
Route_14 = [3]
Route_15 = [4]

# routes_array = [Route_1, Route_2, Route_3, Route_4, Route_5,
#                          Route_6, Route_7, Route_8, Route_9, Route_10,
#                          Route_11, Route_12, Route_13, Route_14, Route_15]
routes_array =[Route_13, Route_14, Route_15]

def random_route():
    #rota seciyoruz
    random_route = random.choice(routes_array)
    return random_route

def random_fabric():
    fabric_types = pd.read_csv('dataPreparation\\fabric_types.csv')
    fabric_types = fabric_types.reset_index(drop=True)
    # rastgele bir kumas seciyoruz
    random_row = fabric_types.sample()
    fabric = str(random_row["KUMAS"].values[0]).strip()
    return fabric

def create_yabbys_devices():
    #ToDo yabbyleri birden baslatinca sorun cikiyor nedenini anla duzelt
    # kac yabbymiz olsun onu belirliyoruz
    yabby_numbers = 25
    data = {'Yabby': ['Yabby{}'.format(i) for i in range(yabby_numbers)],
            'Using': [0.0] * yabby_numbers}
    yabbys = pd.DataFrame(data)
    return yabbys

def create_new_fabric(yabby,last_time,yabbys):
    last_time = circle_increase_time(last_time)
    route_fabric = random_route()
    rand_fabric = random_fabric()
    index = yabbys.loc[yabbys['Yabby'] == yabby].index[0]
    yabbys.at[index, 'Using'] = 0
    filtered_index = yabbys[yabbys['Using']==0].index
    random_yabby = np.random.choice(filtered_index)
    yabbys.at[random_yabby, 'Using'] = 1
    using_yabby_device = yabbys.iloc[random_yabby]['Yabby']
    new_data={'Kumas':rand_fabric ,'Route':[route_fabric] ,'Yabby':using_yabby_device,'Datalogged':time}
    return new_data

def circle_increase_time(time):
     #ToDo son kisimlari surenin ayni geliyor neden anlamadim bakilsin olmazsa without_milliseconds devam ederiz
     random_hours = random.randint(1, 2)
     random_minutes = random.randint(1, 30)
     random_seconds = random.randint(1, 60)
     random_milliseconds = random.randint(1, 999)
     random_microseconds = random_milliseconds * 1000
     time_delta = timedelta(hours=random_hours) + timedelta(minutes=random_minutes) + timedelta(seconds=random_seconds) + timedelta(microseconds=random_microseconds)
     time = time + time_delta
     return time

def increase_time(time):
     #ToDo son kisimlari surenin ayni geliyor neden anlamadim bakilsin olmazsa without_milliseconds devam ederiz
     random_minutes = random.randint(1, 3)
     random_seconds = random.randint(1, 60)
     random_milliseconds = random.randint(1, 999)
     random_microseconds = random_milliseconds * 1000
     time_delta = timedelta(minutes=random_minutes) + timedelta(seconds=random_seconds) + timedelta(microseconds=random_microseconds)
     time = time + time_delta
     return time

def t_zero_monent():
    global number_of_fabrics_in_the_factory , time
    fabrics_in_the_factory = pd.DataFrame()
    yabbys = create_yabbys_devices()
    for _ in range(number_of_fabrics_in_the_factory):
        # enum classtan rota seciyoruz
        route_fabric = random_route()

        # rastgele bir kumas seciyoruz
        rand_fabric = random_fabric()

        #Atanicak yabby' belirliyoruz
        filtered_index = yabbys[yabbys['Using']==0].index
        random_yabby = np.random.choice(filtered_index)
        yabbys.at[random_yabby, 'Using'] = 1
        using_yabby_device = yabbys.iloc[random_yabby]['Yabby']

        # Tarihini belirtiyoruz
        time = increase_time(time)

        # olusturdugumuz veri setini kayit edip dataframe'e ekliyoruz
        new_data={'Kumas':rand_fabric ,'Route':[route_fabric] ,'Yabby':using_yabby_device,'Datalogged':time}
        fabrics_in_the_factory = pd.concat([fabrics_in_the_factory, pd.DataFrame(new_data)], ignore_index=True)

    # kolon isim verini verip kontrol icin csvye cevirip kayit ediyoruz    
    mapping = {fabrics_in_the_factory.columns[0]: 'Kumas', fabrics_in_the_factory.columns[1]: 'Route',
                fabrics_in_the_factory.columns[2]: 'Yabby', fabrics_in_the_factory.columns[3]: 'Datalogged'}
    fabrics_in_the_factory = fabrics_in_the_factory.rename(columns=mapping)
    fabrics_in_the_factory.to_csv('dataPreparation\\fabrics_in_the_factory.csv', index=True)
    print(fabrics_in_the_factory)
    return fabrics_in_the_factory, yabbys