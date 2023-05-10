# format_data.py

import csv

# read csv file: takes a csv file as input and outputs data in a matrix
def readCSV(input_file):
    data = []
    with open(input_file, mode="r", newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            data.append(row)
    return data

# write csv file: takes data matrix as input and outputs a csv file 
def writeCSV(output_file, data):
    with open(output_file, mode="w", newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            writer.writerow(row)

# get seconds from minutes
def getSeconds(minutes):
    seconds = -999
    split = minutes.split(":")
    if len(split) == 1:
        seconds = float(split[0])
    elif len(split) == 2:
        seconds = 60 * float(split[0]) + float(split[1])
    seconds = round(seconds, 2)
    return seconds

# Get data map in minutes
def getDataMinutes(data):
    data_map = {}
    for row in data:
        key     = int(row[0])
        value   = row[1]
        data_map[key] = value
    return data_map

# Get data map in seconds
def getDataSeconds(data):
    data_map = {}
    for row in data:
        key     = int(row[0])
        value   = getSeconds(row[1])
        data_map[key] = value
    return data_map

def format(input_file, output_file):
    print("Formatting")
    data = readCSV(input_file)
    data_map = getDataSeconds(data)
    
    # Sort dictionary based on keys
    sorted_map = dict(sorted(data_map.items()))
    
    # Create output data matrix
    output_data = [[key, value] for key, value in sorted_map.items()] 
    
    for key in sorted_map:
        value = sorted_map[key]
        print("{0}: {1:.2f}".format(key, value))
    
    writeCSV(output_file, output_data)

def main():
    #input_file  = "data/2023_05_08_set_1_min.csv"
    #output_file = "data/2023_05_08_set_1_sec.csv"
    input_file  = "data/2023_05_10_set_1_min.csv"
    output_file = "data/2023_05_10_set_1_sec.csv"
    format(input_file, output_file)

if __name__ == "__main__":
    main()

