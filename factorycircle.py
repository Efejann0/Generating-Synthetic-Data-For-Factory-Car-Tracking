import pandas as pd
import randomdatamatching as RandomDataMatching

zone_2_siniri = 4
zone_3_siniri = 1
zone_4_siniri = 1

zone_2 = []
zone_3 = []
zone_4 = []
islem_goren_kumaslar = []


def simulation_function(random_create_fabric_info, yabbys):
    random_create_fabric_info["Datalogged"] = pd.to_datetime(random_create_fabric_info["Datalogged"])
    random_create_fabric_info  = random_create_fabric_info.sort_values("Datalogged", ascending = False)

    if len(zone_2) < zone_2_siniri:
        count_zone_2 = 0
        for index, row in random_create_fabric_info.iterrows():
            route_data = row["Route"]
            # route_data = random_create_fabric_info.loc[index, 'Route']
            zone_check = route_data.pop()
            if int(zone_check) == 2:
                latitude, longitude = RandomDataMatching.generate_random_location(int(zone_check))
                zone_2.append(row["Yabby"])
                if len(route_data) == 0:
                    count_zone_2 = count_zone_2 + 1
                    max_sipno = random_create_fabric_info['sipno'].max()
                    new_fabric = RandomDataMatching.create_new_fabric(row["Yabby"],row["Datalogged"],yabbys,max_sipno)
                    random_create_fabric_info.loc[index] = new_fabric
                    if count_zone_2 == zone_2_siniri:
                        break
                else:
                    count_zone_2 = count_zone_2 + 1
                    update_time = RandomDataMatching.circle_increase_time(row["Datalogged"])
                    random_create_fabric_info.at[index, 'Route'] = route_data
                    random_create_fabric_info.at[index, 'Datalogged'] = update_time
                    random_create_fabric_info.at[index, 'latitude'] = latitude
                    random_create_fabric_info.at[index, 'longitude'] = longitude
                    random_create_fabric_info.at[index, 'zone'] = 2
                    if count_zone_2 == zone_2_siniri:
                        break
            else:
                route_data.append(zone_check) 
                break

    islem_goren_kumaslar.extend(zone_2)
    
    if len(zone_4) < zone_4_siniri:
        count_zone_4 = 0
        for index, row in random_create_fabric_info.iterrows():
            route_data = row["Route"]
            used_yabby = row["Yabby"]
            # route_data = random_create_fabric_info.loc[index, 'Route']
            zone_check = route_data.pop()
            if used_yabby not in islem_goren_kumaslar:
                if int(zone_check) == 4:
                    latitude, longitude = RandomDataMatching.generate_random_location(int(zone_check))
                    zone_4.append(row["Yabby"])
                    if len(route_data) == 0:
                        count_zone_4 = count_zone_4 + 1
                        max_sipno = random_create_fabric_info['sipno'].max()
                        new_fabric = RandomDataMatching.create_new_fabric(row["Yabby"],row["Datalogged"],yabbys,max_sipno)
                        random_create_fabric_info.loc[index] = new_fabric
                        if count_zone_4 == zone_4_siniri:
                            break
                    else:
                        count_zone_4 = count_zone_4 + 1
                        update_time = RandomDataMatching.circle_increase_time(row["Datalogged"])
                        random_create_fabric_info.at[index, 'Route'] = route_data
                        random_create_fabric_info.at[index, 'Datalogged'] = update_time
                        random_create_fabric_info.at[index, 'latitude'] = latitude
                        random_create_fabric_info.at[index, 'longitude'] = longitude
                        random_create_fabric_info.at[index, 'zone'] = 4
                        if count_zone_4 == zone_4_siniri:
                            break   
                else:
                    route_data.append(zone_check)   
                    break     
            else:
                route_data.append(zone_check)

    islem_goren_kumaslar.extend(zone_4)

    if len(zone_3) < zone_3_siniri:
        count_zone_3 = 0
        for index, row in random_create_fabric_info.iterrows():
            route_data = row["Route"]
            used_yabby = row["Yabby"]
            # route_data = random_create_fabric_info.loc[index, 'Route']
            zone_check = route_data.pop()
            if used_yabby not in islem_goren_kumaslar:
                if int(zone_check) == 3:
                    latitude, longitude = RandomDataMatching.generate_random_location(int(zone_check))
                    zone_3.append(row["Yabby"])
                    if len(route_data) == 0:
                        count_zone_3 = count_zone_3 + 1
                        max_sipno = random_create_fabric_info['sipno'].max()
                        new_fabric = RandomDataMatching.create_new_fabric(row["Yabby"],row["Datalogged"],yabbys,max_sipno)
                        random_create_fabric_info.loc[index] = new_fabric
                        if count_zone_3 == zone_3_siniri:
                            break
                    else:
                        count_zone_3 = count_zone_3 + 1
                        update_time = RandomDataMatching.circle_increase_time(row["Datalogged"])
                        random_create_fabric_info.at[index, 'Route'] = route_data
                        random_create_fabric_info.at[index, 'Datalogged'] = update_time
                        random_create_fabric_info.at[index, 'latitude'] = latitude
                        random_create_fabric_info.at[index, 'longitude'] = longitude
                        random_create_fabric_info.at[index, 'zone'] = 3
                        print('girdim gor beni')
                        if count_zone_3 == zone_3_siniri:
                            break
                else:
                    route_data.append(zone_check)    
                    break    
            else:
                route_data.append(zone_check)
    
    islem_goren_kumaslar.extend(zone_3)

    for i, row in random_create_fabric_info.iterrows():
        value = row['Yabby']
        if value not in islem_goren_kumaslar:
            # Değer dizide bulunmadığında zamanı değiştir
            update_time = RandomDataMatching.circle_increase_time(row["Datalogged"])
            latitude, longitude = RandomDataMatching.generate_random_location(1)
            random_create_fabric_info.at[i, 'Datalogged'] = update_time
            random_create_fabric_info.at[i, 'latitude'] = latitude
            random_create_fabric_info.at[i, 'longitude'] = longitude
            random_create_fabric_info.at[i, 'zone'] = 1

    zone_2.clear()
    zone_3.clear()
    zone_4.clear()
    print('kullanilan yabbyler: ',islem_goren_kumaslar)
    print('kalan liste: ',random_create_fabric_info)
    islem_goren_kumaslar.clear()
    return random_create_fabric_info,yabbys
