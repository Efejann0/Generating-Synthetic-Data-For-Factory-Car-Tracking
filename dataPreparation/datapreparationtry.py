# %%
import pandas as pd
import numpy as np
df = pd.DataFrame()

column_name = 'passingtime'

min_deger = 1
max_deger = 5
df[column_name] = np.random.randint(min_deger, max_deger + 1, size=len(df))

# %%
import pandas as pd
import numpy as np
Yabby_numbers = 25
column_names = ['Yabby{}'.format(i) for i in range(1,Yabby_numbers+1)]
zero_array = np.zeros((1, Yabby_numbers))
Yabbys = pd.DataFrame(zero_array, columns=column_names)
Yabbys = Yabbys.T
print(Yabbys)
# %%
import random
from enum import Enum

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

for _ in range(10):  # Specify the number of iterations as needed
    random_route = random.choice(list(RouteOfFabric))
    print(random_route)
    print(random_route.value)

# %%
import pandas as pd
fabrics_in_the_factory = pd.DataFrame()
fabric_types = pd.read_csv('fabric_types.csv')
fabric_types = fabric_types.reset_index(drop=True)
random_row = fabric_types.sample()
print("Rasgele Seçilen Satır:")
print(str(random_row["KUMAS"].values[0]))
# %%
import pandas as pd

data = {'Yabby': ['Yabby{}'.format(i+1) for i in range(25)],
        'Using': [0.0] * 25}

Yabbys = pd.DataFrame(data)

print(Yabbys)
# %%
import pandas as pd
import numpy as np

data = {'Yabby': ['Yabby{}'.format(i+1) for i in range(25)],
        'Using': [0.0] * 25}

Yabbys = pd.DataFrame(data)
filtered_index = Yabbys[Yabbys['Using'].astype(str).str.startswith('0')].index
random_yabby = np.random.choice(filtered_index)
Yabbys.at[random_yabby - 1, 'Using'] = 1.0
using_yabby_device = Yabbys.iloc[random_yabby - 1]['Yabby']
print(Yabbys.iloc[random_yabby - 1]['Yabby'], using_yabby_device)
# %%
import pandas as pd

zone_2 =[]
zone_3 =[]
zone_4 =[]
bekleme_alani =[]

random_create_fabric_info = pd.read_csv('fabrics_in_the_factory.csv')
random_create_fabric_info["Datalogged"] = pd.to_datetime(random_create_fabric_info["Datalogged"])
random_create_fabric_info  = random_create_fabric_info.sort_values("Datalogged")

if len(zone_2) < 1:
    random_create_fabric_info['Route']
    for index, row in random_create_fabric_info.iterrows():
        route_data = row["Route"]
        zone_check = (route_data.split(',')).pop()
        print(zone_check)
        if zone_check == 2:
            zone_2.append(row["Route"])
            random_create_fabric_info.loc[index, 'Route'] = str(route_data)
            break
            
        route_list = eval(route_data)
print(random_create_fabric_info)
# %%
# Route_1 = [2, 3, 4]
# Route_2 = [2, 4, 3]
# Route_3 = [3, 4, 2]
# Route_4 = [3, 2, 4]
# Route_5 = [4, 3, 2]
# Route_6 = [4, 2, 3]
# Route_7 = [4, 3]
# Route_8 = [4, 2]
# Route_9 = [2, 3]
# Route_10 = [2, 4]
# Route_11 = [3, 2]
# Route_12 = [3, 4]
# Route_13 = [2]
# Route_14 = [3]
# Route_15 = [4]

# # routes_array = [Route_1, Route_2, Route_3, Route_4, Route_5,
# #                          Route_6, Route_7, Route_8, Route_9, Route_10,
# #                          Route_11, Route_12, Route_13, Route_14, Route_15]
# routes_array =[Route_13, Route_14, Route_15]
