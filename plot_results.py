import numpy as np

results_name = "results.txt"
results_file = open(results_name, "r")
results_list = []

for word in results_file.read().split():
    word = word.replace(",", "").replace("[", "").replace("\'", "")
    word = word.replace("]", "").replace("{", "").replace("}", "")
    word = word.replace(":", "").replace("-", "")
    if not word == "":
        results_list.append(word)

indices = range(len(results_list))
accuracy = []
true_positive = []
false_negative = []
true_negative = []
false_positive = []
for i in indices:
    if results_list[i] == "accuracy":
        i += 1
        accuracy.append(float(results_list[i]))
    elif results_list[i] == "true":
        i += 1
        if results_list[i] == "positives":
            i += 1
            true_positive.append(int(float(results_list[i])))
        elif results_list[i] == "negatives":
            i += 1
            true_negative.append(int(float(results_list[i])))
    elif results_list[i] == "false":
        i += 1
        if results_list[i] == "positives":
            i += 1
            false_positive.append(int(float(results_list[i])))
        elif results_list[i] == "negatives":
            i += 1
            false_negative.append(int(float(results_list[i])))

accuracy = np.array(accuracy)
true_positive = np.array(true_positive)
false_negative = np.array(false_negative)
true_negative = np.array(true_negative)
false_positive = np.array(false_positive)

print(accuracy)
print(true_positive)
print(false_negative)
print(true_negative)
print(false_positive)
print(true_positive + false_negative)
print(true_negative + false_positive)
