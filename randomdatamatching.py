from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
import random

number_of_fabrics_in_the_factory = 1

now_date = datetime.now()
time = now_date - relativedelta(months=5)

sipno = 0

def random_route(rand_fabric):
#     "2,3,4"
# "2,4,3"
# "3,4,2"
# "3,2,4"
# "4,3,2"
# "4,2,3"
    if rand_fabric.find("SÜPREM") != -1:
        random_route = [2,3,4]
    elif rand_fabric.find("SüPREM") != -1:
        random_route = [2,3,4]
    elif rand_fabric.find("SUPREM") != -1:
        random_route = [2,3,4]
    elif rand_fabric.find("RİBANA") != -1:
        random_route = [2,4,3]
    elif rand_fabric.find("KAŞKORSE") != -1:
        random_route = [3,4,2]
    elif rand_fabric.find("FUTTER") != -1:
        random_route = [3,2,4]
    elif rand_fabric.find("İNTERLOK") != -1:
        random_route = [4,3,2]
    elif rand_fabric.find("SELANIK") != -1:
        random_route = [4,2,3]
    elif rand_fabric.find("SELANİK") != -1:
        random_route = [4,2,3]
    else:
        #rota csvsini okuyoruz seciyoruz
        random_route_type = pd.read_csv('dataPreparation\\route.csv')
        random_route_type = random_route_type.reset_index(drop=True)
        # rastgele bir rota seciyoruz
        random_row = random_route_type.sample()
        random_route = str(random_row["route"].values[0]).split(',')
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

def create_new_fabric(yabby,last_time,yabbys,max_sipno):
    last_time = circle_increase_time(last_time)
    rand_fabric = random_fabric()
    route_fabric = list(random_route(rand_fabric))
    latitude = -999
    longitude =-999
    zone = -1
    index = yabbys.loc[yabbys['Yabby'] == yabby].index[0]
    yabbys.at[index, 'Using'] = 0
    filtered_index = yabbys[yabbys['Using']==0].index
    random_yabby = np.random.choice(filtered_index)
    yabbys.at[random_yabby, 'Using'] = 1
    max_sipno = max_sipno + 1
    using_yabby_device = yabbys.iloc[random_yabby]['Yabby']
    new_data={'Kumas':rand_fabric ,'Route':route_fabric ,'Yabby':using_yabby_device,'Datalogged':last_time,'sipno':max_sipno,'latitude':latitude,'longitude':longitude,'zone':zone}
    return new_data

def generate_random_location(zone):
    # Generate random latitude and longitude within the bounding box
    if zone == 2:
        area_min_latitude = 38.618265  # Example minimum latitude of the area
        area_max_latitude = 38.618855  # Example maximum latitude of the area
        area_min_longitude = 27.365185  # Example minimum longitude of the area
        area_max_longitude = 27.365780 # Example maximum longitude of the area
    elif zone == 3:
        area_min_latitude = 38.618378  
        area_max_latitude = 38.618777  
        area_min_longitude = 27.364951  
        area_max_longitude = 27.365300 
    elif zone == 4:
        area_min_latitude = 38.617913  
        area_max_latitude = 38.618379  
        area_min_longitude = 27.365317  
        area_max_longitude = 27.365854 
    else:
        area_min_latitude = 38.618326  
        area_max_latitude = 38.618818  
        area_min_longitude = 27.365625  
        area_max_longitude = 27.365992 
        
    random_latitude = random.uniform(area_min_latitude, area_max_latitude)
    random_longitude = random.uniform(area_min_longitude, area_max_longitude)

    return random_latitude, random_longitude

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
    global number_of_fabrics_in_the_factory , time, sipno
    fabrics_in_the_factory = pd.DataFrame()
    yabbys = create_yabbys_devices()
    for _ in range(number_of_fabrics_in_the_factory):
        # rastgele bir kumas seciyoruz
        rand_fabric = random_fabric()

        # enum classtan rota seciyoruz
        route_fabric = random_route(rand_fabric)

        #Atanicak yabby' belirliyoruz
        filtered_index = yabbys[yabbys['Using']==0].index
        random_yabby = np.random.choice(filtered_index)
        yabbys.at[random_yabby, 'Using'] = 1
        using_yabby_device = yabbys.iloc[random_yabby]['Yabby']

        # Tarihini belirtiyoruz
        time = increase_time(time)

        #siparis numarasi ekliyoruz
        sipno = sipno + 1

        #baslangic icin sabit deger atiyoruz
        latitude = -999
        longitude =-999
        zone = -1

        # olusturdugumuz veri setini kayit edip dataframe'e ekliyoruz
        new_data={'Kumas':rand_fabric ,'Route':[route_fabric] ,'Yabby':using_yabby_device,'Datalogged':time,'sipno':sipno,'latitude':latitude,'longitude':longitude,'zone':zone }
        fabrics_in_the_factory = pd.concat([fabrics_in_the_factory, pd.DataFrame(new_data)], ignore_index=True)

    # kolon isim verini verip kontrol icin csvye cevirip kayit ediyoruz    
    mapping = {fabrics_in_the_factory.columns[0]: 'Kumas', fabrics_in_the_factory.columns[1]: 'Route',
                fabrics_in_the_factory.columns[2]: 'Yabby', fabrics_in_the_factory.columns[3]: 'Datalogged',
                fabrics_in_the_factory.columns[4]: 'sipno'}
    fabrics_in_the_factory = fabrics_in_the_factory.rename(columns=mapping)
    fabrics_in_the_factory.to_csv('dataPreparation\\fabrics_in_the_factory.csv', index=True)
    # print(fabrics_in_the_factory)
    return fabrics_in_the_factory, yabbys