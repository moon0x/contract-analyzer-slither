import csv
import subprocess
import sys

import Constants

def analyzeContract(address, filePath):
    print(f'Started analyzing on {address}')
    try:
        with open(filePath, 'w+') as output:
            result = str(subprocess.check_output(['python', Constants.SLITHER_WRAPPER, address]), 'utf-8')
            output.write(result)
    except:
        print("slither print error")

    print(f'Finished analyzing on {address}')

with open(Constants.OUTPUT_FILE_NAME, mode='w') as result_file:
    fieldnames = Constants.OUTPUT_FIELD_NAMES
    writer = csv.DictWriter(result_file, fieldnames=fieldnames)
    writer.writeheader()

    with open(Constants.INPUT_FILE_NAME) as contract_file:
        csv_reader = csv.reader(contract_file, delimiter=',')
        line_count = 0
        skipped_count = 0
        for row in csv_reader:
            if Constants.SKIP_LINE > skipped_count:
                skipped_count += 1
                continue
            
            if row[1]:
                address = row[1]
                name = row[2]
                path = f'{Constants.OUTPUT_FOLDER}/{address}-{name}.txt'

                analyzeContract(address, path)
                
                line_count += 1
                writer.writerow({
                    'No': line_count,
                    'Address': address,
                    'Name': name,
                    'FilePath': path
                })

            if line_count >= 10:
                break

        print(f'Processed {line_count} contracts.')
