import os
import math

# Dictionary with subfolders for each .rwy file
icao_dict = {
    "ANDES.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\ANDES\OTHER\ANDES.rwy",},
    "BAQ.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\BAQ\OTHER\BAQ.rwy",},
    "BGA.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\BGA\OTHER\BGA.rwy",},
    "BOG.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\BOG\OTHER\BOG.rwy",},
    "CLO.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\CLO\OTHER\CLO.rwy",},
    "CUC.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\CUC\OTHER\CUC.rwy",},
    "EYP.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\EYP\OTHER\EYP.rwy",},
    "LET.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\LET\OTHER\LET.rwy",}, 
    "MDE.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\MDE\OTHER\MDE.rwy",},
    "MIL.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\FIR\MIL\OTHER\MIL.rwy",},
    "NVA.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\NVA\OTHER\NVA.rwy",},
    "PEI.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\PEI\OTHER\PEI.rwy",},
    "SPP.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\SPP\OTHER\SPP.rwy",},
    "VVC.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\TMA\VVC\OTHER\VVC.rwy",},
    "SKEC.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\FIR\SKEC\OTHER\SKEC.rwy",},
    "SKED.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\FIR\SKED\OTHER\SKED.rwy",},
    "BND_SKED_SKEC_AD.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\Common\AIRPORTS\BND_SKED_SKEC_AD.rwy",},
    "BND_SKED_SKEC.rwy": {"subfolder": r"\Aurora\SectorFiles\Include\COnew\Common\AIRPORTS\BND_SKED_SKEC_AD.rwy",},
	"MIL.rwy": {"subfolder" : r"\Aurora\SectorFiles\Include\COnew\FIR\MIL\OTHER\MIL.rwy",},
	"NBY_RWY.rwy": {"subfolder" : r"\Aurora\SectorFiles\Include\COnew\Common\AIRPORTS\NBY_RWY.rwy",},
}

# Function to convert DEG.MIN.SEC.DECIMAL_SECS to Decimal Degrees
def dms_to_decimal(deg_min_sec):
    direction = deg_min_sec[0]
    dms_split = deg_min_sec[1:].split('.')
    degrees = int(dms_split[0])
    minutes = int(dms_split[1])
    seconds = int(dms_split[2])
    decimal_seconds = float(dms_split[3])
    decimal_degrees = degrees + minutes / 60 + (seconds + decimal_seconds / 1000) / 3600
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

# Function to calculate the true heading (bearing) from two points
def calculate_bearing(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    d_lon = lon2 - lon1
    x = math.sin(d_lon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(d_lon))
    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    bearing = (initial_bearing + 360) % 360
    return bearing

# Function to update the .rwy file with calculated true headings
def update_rwy_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        # Parsing the original file format
        data = line.strip().split(';')
        if len(data) < 10:
            continue  # Skip invalid lines

        icao, rwy_number, opposite_rwy, _, _, _, _, lat1, lon1, lat2, lon2 = data[:11]

        # Convert DMS to Decimal Degrees
        lat1_dec = dms_to_decimal(lat1)
        lon1_dec = dms_to_decimal(lon1)
        lat2_dec = dms_to_decimal(lat2)
        lon2_dec = dms_to_decimal(lon2)

        # Calculate true headings
        true_heading_1 = calculate_bearing(lat1_dec, lon1_dec, lat2_dec, lon2_dec)
        true_heading_2 = (true_heading_1 + 180) % 360  # Opposite direction

        # Modify the line with the new true headings
        new_line = f"{icao};{rwy_number};{opposite_rwy};{data[3]};{data[4]};{round(true_heading_1)};{round(true_heading_2)};{lat1};{lon1};{lat2};{lon2};"
        new_lines.append(new_line)

    # Overwrite the file with the updated data
    with open(file_path, 'w') as file:
        for line in new_lines:
            file.write(line + '\n')

# Main loop to go through each file in the icao_dict and update the true headings
for filename, info in icao_dict.items():
    file_path = os.path.join(info['subfolder'])
    if os.path.exists(file_path):
        print(f"Updating {filename} at {file_path}")
        update_rwy_file(file_path)
    else:
        print(f"File {filename} not found at {file_path}")
