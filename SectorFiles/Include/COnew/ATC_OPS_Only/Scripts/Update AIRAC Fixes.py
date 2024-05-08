import os

# Define the common subfolder where all output files will be stored
output_subfolder = "OUTPUT_FIX"

# Create a dictionary with the list of ICAOs for each output file
icao_dict = {
    "ANDES_TERM.fix": {"SETU","SKIP"},
    "BAQ_TERM.fix": {"SKBQ","SKBR","SKCB","SKCG","SKCV","SKCZ","SKFU","SKMG","SKMR","SKSM","SKSR","SKTL"},
    "BGA_TERM.fix": {"SKBG","SKCM","SKEJ","SKLA","SKOC","SKPA","SKSG","SKSO","SKTJ"},
    "BOG_TERM.fix": {"SKBO","SKTI","SKQU","SKIB","SKGY","SKGI","SKMA","SKME"},
    "CLO_TERM.fix": {"SKBU","SKCL","SKGO","SKHA","SKPP","SKUL","SKGB"},
    "CUC_TERM.fix": {"SKCC","SKCN","SKSA","SKTM","SKUC","SVSA"},
    "EYP_TERM.fix": {"SKHC","SKMN","SKPZ","SKTD","SKYP","SQUJ"},
    "LET_TERM.fix": {"SBTT","SKLT","SPBC","SWII"},
    "MDE_TERM.fix": {"SKAM","SKMD","SKOT","SKRG","SKSF","SKUR"},
    "MIL_TERM.fix": {"SKCV","SKPQ","SKTI","SKME","SKJC","SKGB","SKNA","SKTQ","SKUA","SKAP","SKMA"},
    "NVA_TERM.fix": {"SKGZ","SKNV"},
    "PEI_TERM.fix": {"SKAR", "SKGO", "SKMZ","SKPE"},
    "SPP_TERM.fix": {"SKSP", "SKPV"},
    "VVC_TERM.fix": {"SKVV", "SKAP", "SKPG"},
    "SKEC_TERM.fix": {"SKBC","SKVP","SKPB","SKMP","SKBC","SKRH","SKLM","SKMJ"},
    "SKED_TERM.fix": {"SKBS","SKNQ","SKUI","SKCD","SKJC","SKGP","SKCO","SKPS","SKAC","SKMU","SKLP","SKPI","SKVG","SKAS","SKFL","SKTQ","SKLG","SKSV","SKNA","SKSJ","SKMF","SKCR","SKPD","SKUA","SKPC","SKOE"},
    "BND_SKED_SKEC_AD_TERM.fix": {"SKNC","SKOC","SKAG","SKTB"},
    "BND_SKED_SKEC_TERM.fix": {"SKML","SKCU","SKEB","SKAD","SKTU","SKLC"},
    # Add more output files and corresponding ICAOs here
}

# Read the input file
input_file = "FIX_ALL.fix"
output_files = {key: [] for key in icao_dict}

with open(input_file, "r") as file:
    for line in file:
        # Ensure the line has enough parts
        parts = line.split(";")
        if len(parts) < 5:  # Check if there are at least 5 elements (minimum expected)
            continue  # Skip lines that don't have enough elements

        parameter_str = parts[3].strip()  # 4th variable
        parameter = int(parameter_str.replace("(", "").replace(")", ""))  # Remove parentheses and convert to integer
        notes = parts[-1].strip()

        # Check if the parameter is 1
        if parameter == 1:
            # Check if there's an ICAO code in the notes and match it to output files
            if "//" in notes:
                icao_code = notes.split("//")[-1].strip()  # Get ICAO code
                for output_file, icao_set in icao_dict.items():
                    if icao_code in icao_set:
                        output_files[output_file].append(line.strip())  # Add to the correct output file

# Ensure the common output subfolder exists
os.makedirs(output_subfolder, exist_ok=True)

# Write to output files in the common subfolder
for filename, lines in output_files.items():
    full_path = os.path.join(output_subfolder, filename)

    with open(full_path, "w") as file:
        for line in lines:
            file.write(f"{line}\n")

print("Output files have been created in the 'OUTPUT_FIX' subfolder.")
