import folium
import webbrowser
import os

def dms_to_decimal(dms, direction):
    seconds = int(dms[-2:])
    minutes = int(dms[-4:-2])
    degrees = int(dms[:-4])

    decimal = degrees + (minutes / 60) + (seconds / 3600)

    return decimal * direction

def create_alphabet_to_number(max_values, previous_value, current_char_index, mapping, chars, previous_char):
    if current_char_index == len(chars):
        # TODO: strict oplopend? Zou kunnen betekenen: altijd eindigen op 9, en elke waarde moet voorkomen?
        if False or ord('Z') - ord(previous_char) < 9 - previous_value: # no room for last numbers
            pass
        else:
            yield mapping
    else:
        # TODO: strict oplopend?
        #  Zou kunnen betekenen: altijd eindigen op 9, en elke waarde moet voorkomen?
        for i in range(previous_value, max_values[chars[current_char_index]] + 1):
            if i - ord(previous_char) < i - previous_value:  # no room for missing numbers
                pass

            mapping[chars[current_char_index]] = str(i)
            yield from create_alphabet_to_number(max_values, i, current_char_index + 1, mapping, chars, chars[current_char_index])

# Define a GPS position (latitude, longitude)
gps_positions = set()  # Example: London, UK

# Create a map centered at the GPS position
mymap = folium.Map(location=(0, 0), zoom_start=2)

# set max values for each char
max_values = {}

for i in range(26):
    max_values[chr(i + ord('A'))] = 9

direction_lat = 1
direction_lon = 1
latitude = "VETARM"
longitude = "ROKJE"

# latitude = "SHANDY"
# longitude = "-WITJE"

if latitude[0] == "-":
    direction_lat = -1
    latitude = latitude[1:]

if longitude[0] == "-":
    direction_lon = -1
    longitude = longitude[1:]


max_values[latitude[-2]] = 5
max_values[latitude[-4]] = 5
max_values[longitude[-2]] = 5
max_values[longitude[-4]] = 5


for mapping in create_alphabet_to_number(max_values, 0, 0, {}, sorted(set(list(latitude + longitude))), 'A'):
    latitude_dms = "".join([mapping[c] for c in list(latitude)])
    longitude_dms = "".join([mapping[c] for c in list(longitude)])

    print(mapping, latitude_dms)

    gps_positions.add((dms_to_decimal(latitude_dms, direction_lat), dms_to_decimal(longitude_dms, direction_lon)))


for gps_position in gps_positions:
    folium.Circle(
        location=gps_position,
        radius=500,  # radius in meters
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.4
    ).add_to(mymap)


# Save the map to an HTML file temporarily
map_filename = "temp_map.html"
mymap.save(map_filename)

# Open the map in the default web browser, simulating a popup
webbrowser.open('file://' + os.path.realpath(map_filename))