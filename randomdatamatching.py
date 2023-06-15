import pandas as pd
from enum import Enum
import random
import numpy as np

class RouteOfFabric(Enum):
        Route_1 = [2,3,4]
        Route_2 = [2,4,3]
        Route_3 = [3,4,2]
        Route_4 = [3,2,4]
        Route_5 = [4,3,2]
        Route_6 = [4,2,3]
        Route_7 = [4,3]
        Route_8 = [4,2]
        Route_9 = [2,3]
        Route_10 = [2,4]
        Route_11 = [3,2]
        Route_12 = [3,4]
        Route_13 = [2]
        Route_14 = [3]
        Route_15 = [4]

def random_route():
    # enum classtan rota seciyoruz
    random_route = random.choice(list(RouteOfFabric))
    route = random_route.value
    return route

def random_fabric():
    fabric_types = pd.read_csv('dataPreparation\\fabric_types.csv')
    fabric_types = fabric_types.reset_index(drop=True)
    # rastgele bir kumas seciyoruz
    random_row = fabric_types.sample()
    fabric = str(random_row["KUMAS"].values[0])
    return fabric

def create_yabbys():
    yabby_numbers = 25
    data = {'Yabby': ['Yabby{}'.format(i) for i in range(yabby_numbers)],
            'Using': [0.0] * yabby_numbers}
    yabbys = pd.DataFrame(data)
    return yabbys

def t_zero_monent():
    fabrics_in_the_factory = pd.DataFrame()
    yabbys = create_yabbys()
    for _ in range(18):
        # enum classtan rota seciyoruz
        route_fabric = random_route()

        # rastgele bir kumas seciyoruz
        rand_fabric = random_fabric()

        #Atanicak yabby' belirliyoruz
        filtered_index = yabbys[yabbys['Using']==0].index
        random_yabby = np.random.choice(filtered_index)
        yabbys.at[random_yabby, 'Using'] = 1
        using_yabby_device = yabbys.iloc[random_yabby]['Yabby']

        # olusturdugumuz veri setini kayit edip dataframe'e ekliyoruz
        new_data={'Kumas':rand_fabric ,'Route':[route_fabric] ,'Yabby':using_yabby_device }
        fabrics_in_the_factory = pd.concat([fabrics_in_the_factory, pd.DataFrame(new_data)], ignore_index=True)

    # kolon isim verini verip kontrol icin csvye cevirip kayit ediyoruz    
    mapping = {fabrics_in_the_factory.columns[0]: 'Kumas', fabrics_in_the_factory.columns[1]: 'Route', fabrics_in_the_factory.columns[2]: 'Yabby'}
    fabrics_in_the_factory = fabrics_in_the_factory.rename(columns=mapping)
    fabrics_in_the_factory.to_csv('fabrics_in_the_factory.csv', index=True)
    return fabrics_in_the_factory, yabbys