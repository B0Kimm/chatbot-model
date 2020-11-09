import json
import pandas as pd
from pandas import DataFrame
import re


df = pd.read_csv('data.txt', sep=',', header=None)

result = []
# for index, row in df.iterrows():
#     result.append(row)
for index, row in df.iterrows():
    re_pattern1 = r'\d{2,3}[-\.\s]*\d{3,4}[-\.\s]*\d{4}(?!\d)'
    text = re.sub(re_pattern1, 'tel', str(row[0]))
    # re_pattern = r'\d{1,3}[,\.]\d{1,3}[만\천]?\s?[원]|\d{1,5}[만\천]?\s?[원]'
    # text = re.sub(re_pattern, 'money', text)
    # re_pattern = r'[일/이/삼/사/오/육/칠/팔/구/십/백][만\천]\s?[원]'
    # text = re.sub(re_pattern, 'money', text)
    # re_pattern = r'(?!-)\d{2,4}[0]{2,4}(?!년)(?!.)|\d{1,3}[,/.]\d{3}'
    # text = re.sub(re_pattern, 'money', text)

    re_pattern1 = r'\d{2,3}[-\.\s]*\d{3,4}[-\.\s]*\d{4}(?!\d)'
    text2 = re.sub(re_pattern1, 'tel', str(row[1]))
    # re_pattern = r'\d{1,3}[,\.]\d{1,3}[만\천]?\s?[원]|\d{1,5}[만\천]?\s?[원]'
    # text2 = re.sub(re_pattern, 'money', text2)
    # re_pattern = r'[일/이/삼/사/오/육/칠/팔/구/십/백][만\천]\s?[원]'
    # text2 = re.sub(re_pattern, 'money', text2)
    # re_pattern = r'(?!-)\d{2,4}[0]{2,4}(?!년)(?!.)|\d{1,3}[,/.]\d{3}'
    # text2 = re.sub(re_pattern, 'money', text2)

    imsi = [row[2], text , text2]
    result.append(imsi)
result = pd.DataFrame(result)

with open('./data/train.txt', 'wt', encoding='utf-8') as file1:
    for index, row in result.iterrows():
        # file1.writelines(f'[CLS] {row[0]} [SEP] {row[1]} [SEP] \n')
        file1.writelines(f'{row[0]} $ {row[1]} $ {row[2]} \n')
    file1.close()
