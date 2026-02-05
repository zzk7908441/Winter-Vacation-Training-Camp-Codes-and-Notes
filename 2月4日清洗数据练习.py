raw_info = " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; \nMission:2025-RESCUE-X "
clean_str = raw_info.strip().replace('\n', '')
parts = [item.strip().split(':') for item in clean_str.split(';') if item.strip()]
temp_map = {k.strip(): v.strip() for k, v in parts}
items_set = set(temp_map['Items'].split(','))
coords_tuple = tuple(map(int, temp_map['Coords'].replace('(', '').replace(')', '').split(',')))
mission_code = temp_map['Mission'][5:]
agent_file = {
    'agent_id': temp_map['Agent'],
    'coords': coords_tuple,
    'unique_items': items_set,
    'mission_code': mission_code
}

print(agent_file)
