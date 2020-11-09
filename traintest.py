import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split

task = []
with open('bert_most_updated.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lines = line.split('\t')
        task.append(lines)
    file.close()


task = pd.DataFrame(task)

train, test = train_test_split(task, test_size =0.2)


t = []
for index, row in task.iterrows():
    no = row[1].strip('\n')
    imsi = [no, row[0]]
    t.append(imsi)
t = pd.DataFrame(t)
# t.to_csv('kogpt2.txt', mode='w', encoding='utf-8', index=False)

with open('bert_most_update_train.txt', 'wt', encoding='utf-8') as file1:
    for index, row in train.iterrows():
        file1.writelines(f'{row[0]}\t{row[1]}')
        # file1.writelines(f'[CLS] {row[0]} [SEP] {row[1]} [SEP] \n')
    file1.close()

with open('bert_most_update_test.txt', 'wt', encoding='utf-8') as file1:
    for index, row in test.iterrows():
        file1.writelines(f'{row[0]}\t{row[1]}')
        # file1.writelines(f'[CLS] {row[0]} [SEP] {row[1]} [SEP] \n')
    file1.close()


for i in range(0, 10, 2):    # 0부터 8까지 2씩 증가
    print('Hello, world!', i)
