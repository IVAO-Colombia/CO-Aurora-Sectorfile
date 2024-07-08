# List of codes to retain
codes_to_retain = ["SEMDO","KONSO","AKNIL","UKTIV","URIBI","REBIM","GILGA","AMBAS","SELAN","OROSA","EDROD","TOMEK","BOBKA","NEVPA","SINID","KILER","SUSDA","ROPOL","ROKIN","ALPON","BITIX","ISIMO","BOGAL","ESEDA","KAKOL","KAKUD","MORGI","EDRES","TIGRO","DAGMI","UMPUR","EDVAR","MUDIN","ARMOL","GAXAL","LUVTO","KOGPI","UGSAT","TOTAD","SUBLO","VOVLU","DOSPU","VUKRA","GEKIM","AKPAM","IRAXU","DAGLU","EGISA","ISLUN","DIMOL","UGALU","GERNA","SERVO","BUTAL","RAXOG","AKPEK"]  # Add more codes as needed

# Input and output file names
input_filename = "FIX_ALL.fix"
output_filename = "filtered_fixes.txt"

# Read the input file and filter the lines based on codes_to_retain
with open(input_filename, "r") as input_file:
    lines = input_file.readlines()

# Create a list to hold the filtered lines
filtered_lines = []

# Iterate over each line in the input file
for line in lines:
    # Check if any of the codes in the list is in the line
    if any(code in line for code in codes_to_retain):
        filtered_lines.append(line)

# Write the filtered lines to the output file
with open(output_filename, "w") as output_file:
    output_file.writelines(filtered_lines)

print(f"Filtered {len(filtered_lines)} lines and wrote to '{output_filename}'.")
