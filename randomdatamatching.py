import pandas as pd
from enum import Enum
import random
import numpy as np

Yabby_numbers = 25
data = {'Yabby': ['Yabby{}'.format(i) for i in range(Yabby_numbers)],
        'Using': [0.0] * Yabby_numbers}
Yabbys = pd.DataFrame(data)

fabrics_in_the_factory = pd.DataFrame()
fabric_types = pd.read_csv('dataPreparation\\fabric_types.csv')
fabric_types = fabric_types.reset_index(drop=True)
random_row = fabric_types.sample()

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

random_route = random.choice(list(RouteOfFabric))

for _ in range(18):
    random_route = random.choice(list(RouteOfFabric))
    random_row = fabric_types.sample()
    kumas = str(random_row["KUMAS"].values[0])
    route = random_route.value
    filtered_index = Yabbys[Yabbys['Using']==0].index
    
    random_yabby = np.random.choice(filtered_index)
    Yabbys.at[random_yabby, 'Using'] = 1
    
    using_yabby_device = Yabbys.iloc[random_yabby]['Yabby']
    # print(Yabbys)
    print(filtered_index,using_yabby_device)
    # print(kumas, route, using_yabby_device)
    new_data={'Kumas':kumas ,'Route':[route] ,'Yabby':using_yabby_device }
    fabrics_in_the_factory = pd.concat([fabrics_in_the_factory, pd.DataFrame(new_data)], ignore_index=True)
    
mapping = {fabrics_in_the_factory.columns[0]: 'Kumas', fabrics_in_the_factory.columns[1]: 'Route', fabrics_in_the_factory.columns[2]: 'Yabby'}
fabrics_in_the_factory = fabrics_in_the_factory.rename(columns=mapping)
fabrics_in_the_factory.to_csv('fabrics_in_the_factory.csv', index=True)