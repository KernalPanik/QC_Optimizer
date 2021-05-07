import sys
import csv
from Learner.qmodel import init_test_procedure, init_training_procedure, predict
'''
This module is responsible for invocation of ml model, evaluating given circuit data,
providing predicted optimizations
'''

def extract_subdags_from_csv(filename):
    subdag_list = list()
    with open(filename, newline='') as entry:
        reader = csv.reader(entry)

        for row in reader:
            floats = [float(item) for item in row]
            subdag_list.append(floats)
    
    return subdag_list

def save_predictions_to_csv(filename, predictions):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        pred_set = set(predictions)
        writer.writerow(pred_set)

print("Invoking Training Procedure...")

model = init_training_procedure("Learner/training_data.csv", 32)

print("Invoking Testing Procedure...")

init_test_procedure(model, "Learner/test_data.csv", 32)

print("Predicting...")

subdags = extract_subdags_from_csv("temp_eval_hashed.csv")
pred_names = predict(model, subdags)

print("Saving Prediction Results...")
save_predictions_to_csv("temp_pred.csv", pred_names)
print("Saved")

sys.exit(0)