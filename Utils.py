import csv
from Scheduler.DagHandler import hash_adj_list

def put_subdags_into_csv(csv_path: str, subdags: list):
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for subdag in subdags:
            writer.writerow(subdag)

def hash_training_data(training_data_path: str, hashed_data_path: str, col_count = 4) -> str:
    with open(training_data_path, newline='') as entry:
        with open(hashed_data_path, 'w', newline='') as output:
            writer = csv.writer(output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            reader = csv.reader(entry)

            for row in reader:
                hashed_row = hash_adj_list(row[0:3])
                hashed_row.append(row[-1])
                writer.writerow(hashed_row)
