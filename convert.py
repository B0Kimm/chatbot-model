import docx2txt
import pandas as pd
from pandas import DataFrame

# # my_text = docx2txt.process("data.docx")


# with open('data.txt', 'wt', encoding='utf-8') as file:
#     # for line in my_text:
#     #     line.rstrip()

#     file.write(my_text)
#     file.close()




# import sys
# import re

# text = 'data.txt'
# file2 = open(text, 'r', encoding='utf-8')
# a = file2.read()

# print(a)

# for line in a:
#     string += line #.replace('\n', '\t')
# file2.close()

# file3 = open(text, 'wt', encoding='utf-8')
# file3.write(string)
# file3.close()


# df6 = pd.read_csv('category.csv', sep=',', encoding='utf-8')
# t = []
# for index, row in df6.iterrows():
#     imsi = [row['intent'], row['a']]
#     t.append(imsi)
# t = pd.DataFrame(t)
# t.to_csv('kogpt2.txt', mode='w', encoding='utf-8', index=False)
task = []
with open('category.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lines = line.split(',')
        task.append(lines)
    file.close()


task = pd.DataFrame(task)
t = []
for index, row in task.iterrows():
    no = row[1].strip('\n')
    imsi = [no, row[0]]
    t.append(imsi)
t = pd.DataFrame(t)
# t.to_csv('kogpt2.txt', mode='w', encoding='utf-8', index=False)

with open('bert_c.txt', 'wt', encoding='utf-8') as file1:
    for index, row in t.iterrows():
        file1.writelines(f'{row[0]}\t{row[1]}\n')
        # file1.writelines(f'[CLS] {row[0]} [SEP] {row[1]} [SEP] \n')
    file1.close()


for i in range(0, 10, 2):    # 0부터 8까지 2씩 증가
    print('Hello, world!', i)
