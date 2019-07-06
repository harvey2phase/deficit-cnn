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
        accuracy.append(results_list[i])
    # TODO: NOT DONE YET, CHECK VARIABLE NAMES
    elif results_list[i] == "true":
        i += 1
        if results_list[i] == "positive":
            i += 1
            true_positive.append(results_list[i])
        elif results_list[i] == "negative":
            i += 1
            true_positive.append(results_list[i])
    elif results_list[i] == "false":
        i += 1
        if results_list[i] == "positive":
            i += 1
            true_positive.append(results_list[i])
        elif results_list[i] == "negative":
            i += 1
            true_positive.append(results_list[i])
