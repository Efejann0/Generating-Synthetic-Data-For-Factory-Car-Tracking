import pandas as pd
import numpy as np
import randomdatamatching as RandomDataMatching
import random
zone_2_siniri = 1
zone_2 =[]
zone_3 =[]
zone_4 =[]

def simulation_function(random_create_fabric_info, yabbys):
    random_create_fabric_info["Datalogged"] = pd.to_datetime(random_create_fabric_info["Datalogged"])
    random_create_fabric_info  = random_create_fabric_info.sort_values("Datalogged")

    if len(zone_2) < zone_2_siniri:
        for index, row in random_create_fabric_info.iterrows():
            route_data = row["Route"]
            print('buyukifegirdim')
            # route_data = random_create_fabric_info.loc[index, 'Route']
            zone_check = route_data.pop()
            print(zone_check)
            if int(zone_check) == 2:
                zone_2.append(row["Yabby"])
                if len(route_data) == 0:
                    print('ife girdim')
                    new_fabric = RandomDataMatching.create_new_fabric(row["Yabby"],row["Datalogged"],yabbys)
                    random_create_fabric_info.loc[index] = new_fabric
                    break
                else:
                    print('else girdim')
                    print(index, route_data)
                    update_time = RandomDataMatching.circle_increase_time(row["Datalogged"])
                    random_create_fabric_info.at[index, 'Route'] = route_data
                    random_create_fabric_info.at[index, 'Datalogged'] = update_time
                    break
            else:
                route_data.append(zone_check)
                
    print(random_create_fabric_info)