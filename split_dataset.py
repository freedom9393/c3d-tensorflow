from random import shuffle

read_from = "train1.list"
train_file = "train.list"
test_file = "test.list"
num_of_classes = 7
threshold = .9

txt_lines = []
with open(read_from, 'r') as lines:
    for line in lines:
        txt_lines.append(line.strip().split(" "))

data = []
for i in range(num_of_classes):
    data.append([])

for j in range(len(txt_lines)):
    data[int(txt_lines[j][1])].append(txt_lines[j])

train, test = [], []
for i in range(num_of_classes):
    shuffle(data[i])
    train.extend(data[i][:round(len(data[i])*threshold)])
    test.extend(data[i][round(len(data[i])*threshold):])

with open(train_file, 'w+') as line:
    for item in train:
        item = " ".join(str(x) for x in item)
        print(item)
        line.write("%s\n" % item)

with open(test_file, 'w+') as line:
    for item in test:
        item = " ".join(str(x) for x in item)
        print(item)
        line.write("%s\n" % item)