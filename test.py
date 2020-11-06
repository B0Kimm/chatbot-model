import json
import pandas as pd
from pandas import DataFrame
import re


df = pd.read_excel('testjson.xlsx')
delivery = []
for index, row in df.iterrows():
    imsi = [row['intent'], row['question'], row['answer']]
    delivery.append(imsi)



df2 = pd.read_excel('testjson1.xlsx')
cafe = []
for index, row in df2.iterrows():
    imsi = [row['answer'],row['intent'], row['question']]
    cafe.append(imsi)

delivery = pd.DataFrame(delivery, columns = ['intent', 'q', 'a'])
cafe = pd.DataFrame(cafe, columns = ['intent', 'q', 'a'])
temp = pd.concat([delivery, cafe], axis=0)
# print(temp.groupby(['intent']).count())

temp.to_csv('data.csv', mode='w', encoding='utf-8', index=False)

category = []
count = 0
for index, row in temp.iterrows():
    if row['intent'] not in category:
        category.append(row['intent'])
    else:
        continue

category = pd.DataFrame(category)
category.to_csv('fuckit.csv', encoding='utf-8')
print(category.head(20))




# data = []
# for index, row in temp.iterrows():
#     re_pattern = r'\d{2,3}[-\.\s]*\d{3,4}[-\.\s]*\d{4}(?!\d)'
#     row[0] = re.sub(re_pattern, 'tel', str(row[0]))
#     row[1] = re.sub(re_pattern, 'tel', str(row[1]))
#     re_pattern = r'\(\d{3}\)\s*\d{4}[-\.\s]??\d{4}'
#     row[0] = re.sub(re_pattern, 'tel', str(row[0]))
#     row[1] = re.sub(re_pattern, 'tel', str(row[1]))
#     re_pattern = r'\d{1,3}[,\.]\d{1,3}[만\천]?\s?[원]|\d{1,5}[만\천]?\s?[원]'
#     row[0] = re.sub(re_pattern, 'money', str(row[0]))
#     row[1] = re.sub(re_pattern, 'money', str(row[1]))
#     re_pattern = r'[일/이/삼/사/오/육/칠/팔/구/십/백][만\천]\s?[원]'
#     row[0] = re.sub(re_pattern, 'money', str(row[0]))
#     row[1] = re.sub(re_pattern, 'money', str(row[1]))
#     re_pattern = r'(?!-)\d{2,4}[0]{2,4}(?!년)(?!.)|\d{1,3}[,/.]\d{3}'
#     row[0] = re.sub(re_pattern, 'money', str(row[0]))
#     row[1] = re.sub(re_pattern, 'money', str(row[1]))

# data = pd.DataFrame(data)


# with open('data.csv', 'wt', encoding='utf-8') as file1:
#     for index, row in temp.iterrows():
#         # file1.writelines(f'[CLS] {row[0]} [SEP] {row[1]} [SEP] \n')
#         file1.writelines(f'{row[0]}\t{row[1]}\t{row[2]}\n')
#     file1.close()
