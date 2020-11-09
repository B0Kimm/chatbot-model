import os
import sys
import json
import nltk
import pandas as pd
from pandas import DataFrame
import csv
import itertools
from konlpy.tag import Okt
import re

filename = './data/dialog.json'
filename2 = 'testjson.csv'
# Chatbot().json_to_csv('dialog.json', '카페')
review_column = ['question', 'answer', 'intent']

result = []
question_only=[]
answer_only=[]
with open(filename, 'rb') as json_file:
    data = json.load(json_file)
    for idx in range(0, 10):
        if data['DATA'][idx]['DOMAIN'] == '관광/여가/오락':
            for n in range(0,2):
                for a in range(0,63):
                    # intent = data['DATA'][idx]['CATEGORY'][n]['INTENT'][a]['MAIN_INTENT']
                    for item in data['DATA'][idx]['CATEGORY'][n]['INTENT'][a]['INTENT']:
                        try: 
                            answer = item['answer']
                            question = item['question']
                            imsi = [ question, answer, intent]
                            result.append(imsi)
                            print(imsi)
                        except :
                            print('error')
    # for idx in range(0, 10):
    #     if data['DATA'][idx]['DOMAIN'] == '일반음식점':
    #         for n in range(0,1):
    #             if data['DATA'][idx]['CATEGORY'][n]['category'] == '배달음식점':
    #                         # intent = data['DATA'][idx]['CATEGORY'][n]['INTENT']
    #                 for a in range(0, 132):  #len으로 바꾸기 / 114 /132
    #                     sub_intent = data['DATA'][idx]['CATEGORY'][n]['INTENT'][a]['SUB_INTENT']
    #                     for b in range(0, 10):
    #                         for item in sub_intent[b]['INTENT']:
    #                             try: 
    #                                 sub_intent = sub_intent[b]['SUB_INTENT']
    #                                 answer = item['answer']
    #                                 question = item['question']
    #                                 imsi = [ question, answer, sub_intent]
    #                                 result.append(imsi)
    #                             except :
    #                                 print('error')

result = pd.DataFrame(result, columns=review_column)
outputname = 'total.csv'
result.to_csv(outputname, mode='w', encoding='utf-8', index=False)

print('------------ finished --------')

# with open(filename, 'r', encoding='utf-8') as f1, open('test.txt', 'w', encoding='utf-8') as file:
#     for row in f1.iter_rows():
#         file.write(row['question'].value + '\t' + row['answer'].value + '\t')
#         file.close()

# print('------------ finished --------')



df = pd.read_csv('testjson.csv', sep = ',', encoding= 'utf-8')
        
okt = Okt()
result = []
stopword = []
# stopword 리스트 만들기
with open('stopword.txt', 'r', encoding='utf-8') as file:
    for text in file:
        w = text.strip('\n')
        stopword.append(w)

question = []
        # mecab = Mecab(dicpath='C:/mecab/mecab-ko-dic')
for index, row in df.iterrows():
    temp_q = []
    # temp_q = mecab.morphs(sentence)
    sentence = row['question']
    temp_q = okt.morphs(sentence)
            
    q_temp = []
    for token in temp_q:
        if token not in stopword:
            q_temp.append(token)
    toeknized_sent = ' '.join(q_temp)
    question.append(toeknized_sent)

answer = []
for index,row in df.iterrows():
    temp_a = []
    # temp_a = mecab.morphs(sentence)
    temp_a = okt.morphs(row['answer'])
            
    a_temp = []
    for token in temp_a:
        if token not in stopword:
            a_temp.append(token)
    toeknized_sent_a = ' '.join(a_temp)
    answer.append(toeknized_sent_a)

question = pd.DataFrame(question, columns=['question'])
answer = pd.DataFrame(answer, columns=['answer'])

data = pd.concat([question, answer], axis=1)
print(data.head())

with open('corpus.txt', 'w', encoding='utf-8') as file:
    for index, row in data.iterrows():
        file.write(str(row['question']) + '\t' + str(row['answer']) + '\n')
    file.close()

print('------------ finished --------')

# text1 ='010-4928'
# text2 ='010-5930-3928'
# text3 ='1993-5929'

# pattern = r'\d{2,3}-\d{3,4}-\d{4}'
# text1 =re.sub(pattern, 'phone', text1)
# # pattern = r'^[0-9]+-[0-9]+-[0-9]+'
# text1 =re.sub(pattern, 'phone', text1)
# print(text1)
# text2 =re.sub(pattern, 'phone', text2)
# print(text2)
# text3 =re.sub(pattern, 'phone', text3)
# print(text3)

# print('====test=======')

# re_pattern = r'\d{2,3}[-\.\s]*\d{3,4}[-\.\s]*\d{4}(?!\d)'
# text12 = re.sub(re_pattern, 'tel', text1)
# print(text12)
# re_pattern = r'\(\d{3}\)\s*\d{4}[-\.\s]??\d{4}'
# text22 = re.sub(re_pattern, 'tel', text1)
# print(text22)

# re_pattern = r'\d{2,3}[-\.\s]*\d{3,4}[-\.\s]*\d{4}(?!\d)'
# print(text2 = re.sub(re_pattern, 'tel', text2))
# re_pattern = r'\(\d{3}\)\s*\d{4}[-\.\s]??\d{4}'
# print(text2 = re.sub(re_pattern, 'tel', text2))

# re_pattern = r'\d{2,3}[-\.\s]*\d{3,4}[-\.\s]*\d{4}(?!\d)'
# print(text3 = re.sub(re_pattern, 'tel', text3))
# re_pattern = r'\(\d{3}\)\s*\d{4}[-\.\s]??\d{4}'
# print(text3 = re.sub(re_pattern, 'tel', text3))





