import numpy as np
import matplotlib.pyplot as plt

def avg(x):
    return sum(x) / len(x)

def plot_file(results_name, his):

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

    HIS.append(his)
    AC.append(avg(accuracy))
    LAB.append(results_name[:-3])

    #print("accuracy: ", accuracy)
    #print("true positive: ", true_positive)
    #print("false negative: ", false_negative)
    #print("true negative: ", true_negative)
    #print("false positive: ", false_positive)
    #print("Sanity check: ", true_positive + false_negative)
    #print("Sanity check: ", true_negative + false_positive)

HIS = []
AC = []
LAB = []

plot_file("10x|e5st|32_64f|5_5_5_5si|256d|2l.txt", 10)
plot_file("20x|5e4st|32f|5_5si|256d|2l.txt", 20)
plot_file("20x|5e4st|64f|5_5si|256d|2l.txt", 20)
plot_file("20x|e5st|32f|5_5si|256d|2l.txt", 20)
plot_file("20x|e5st|64f|5_5si|256d|2l.txt", 20)
plot_file("2x|5e4st|32f|5_5si|256d|2l.txt", 2)
plot_file("2x|5e4st|64f|5_5si|256d|2l.txt", 2)
plot_file("5x|e5st|32_64f|5_5_5_5si|256d|2l.txt", 5)

fig, ax = plt.subplots()
ax.scatter(HIS, AC)
for i, lab in enumerate(LAB):
    ax.annotate(lab, (HIS[i], AC[i]))

plt.show()
