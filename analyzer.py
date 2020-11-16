# Analyzer of contracts on Etherscan using slither
import csv
import subprocess
import sys
import os

import Constants

def file_reader(filename):
    with open(Constants.INPUT_FILE_NAME) as file:
        readData = [row for row in csv.reader(file, delimiter=',')]
        return readData
    return None

def file_writer_header(filename, fieldnames):
    with open(filename, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def file_writer(filename, writedata):
    with open(filename, mode='w+') as file:
        fieldnames = Constants.OUTPUT_FIELD_NAMES
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(writedata)
        return writer
    return None

def analyzeContract(address, filePath):
    print(f'Started analyzing on {address}')
    try:
        with open(filePath, 'w+') as output:
            result = str(subprocess.check_output(['python', Constants.SLITHER_WRAPPER, address]), 'utf-8')
            output.write(result)
    except:
        print("slither print error", e)

    print(f'Finished analyzing on {address}')

def analyzeAll():
    contracts = file_reader(Constants.INPUT_FILE_NAME)
    if contracts == None:
        print("input file error")
        exit()

    line_count = 0
    skipped_count = 0
    for row in contracts:
        if Constants.SKIP_LINE > skipped_count:
            skipped_count += 1
            continue
        
        if row[1]:
            address = row[1]
            name = row[2]
            path = f'{Constants.OUTPUT_FOLDER}/{address}-{name}.txt'

            analyzeContract(address, path)
            
            line_count += 1
            file_writer(Constants.OUTPUT_FILE_NAME, {
                'No': line_count,
                'Address': address,
                'Name': name,
                'FilePath': path
            })


    print(f'Processed {line_count} contracts.')

def main():
    if not os.path.exists(Constants.OUTPUT_FOLDER):
        os.makedirs(Constants.OUTPUT_FOLDER)

    file_writer_header(Constants.OUTPUT_FILE_NAME, Constants.OUTPUT_FIELD_NAMES)

    analyzeAll()

if __name__ == "__main__":
    main()
