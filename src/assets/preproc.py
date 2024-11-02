import json

# Function to process the text file and convert it to JSON format
def txt_to_json(input_file, output_file):
    # Dictionary to store the data in JSON format
    json_data = {}
    
    # Open and read the text file
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Split each line by '=' to separate the key and value
            if '=' in line:
                idx = line.find("=")
                code = line[0:idx]
                character = line[idx+1:-1]
                if character == "\\n": character = "\n"
                # Add the entry to the dictionary
                json_data[character] = code
    
    # Write the dictionary to a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

# Example usage
txt_to_json('./dict.txt', './dict.json')
