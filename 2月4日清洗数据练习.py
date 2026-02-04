raw_info = "  Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X  "

info = raw_info.strip()
parts = info.split("; ")

mission_id = parts[3][8:]
coords = (40, 74)

items_string = parts[2][6:]
items_list = items_string.split(",")
unique_items = set(items_list)

agent_file = {
    "Agent": "007_Bond",
    "Mission_ID": mission_id,
    "Location": coords,
    "Equipment": list(unique_items)}

print(agent_file)
