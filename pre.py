import json
import pandas as pd
from pandas import DataFrame
'''extraction

# filename = 'dialog.json'
# columns = ['question', 'answer', 'intent']

# result = []
# with open(filename, encoding='utf-8') as file:
#     data = json.load(file)
#     for a in range(0, 10):
#         if data['DATA'][a]['DOMAIN'] == '숙박':
#             for b in range(len(data['DATA'][a]['CATEGORY'])):
#                 for c in range(len(data['DATA'][a]['CATEGORY'][b]['INTENT'])):
#                     intent = data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['MAIN_INTENT']
#                     for d in range(len(data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['INTENT'])):
#                         try :
#                             question = data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['INTENT'][d]['question']
#                             answer = data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['INTENT'][d]['answer']
#                             imsi = [question, answer, intent]
#                             result.append(imsi)
#                         except:
#                             print('error')

# result = pd.DataFrame(result, columns = columns)
# print(result.head(10))

# result2 = []
# with open(filename, encoding='utf-8') as file:
#     data = json.load(file)
#     for a in range(0, 10):
#         if data['DATA'][a]['DOMAIN'] == '의복/의류점':
#             for b in range(len(data['DATA'][a]['CATEGORY'])):
#                 for c in range(len(data['DATA'][a]['CATEGORY'][b]['INTENT'])):
#                     intent = data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['MAIN_INTENT']
#                     for d in range(len(data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['INTENT'])):
#                         try :
#                             question = data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['INTENT'][d]['question']
#                             answer = data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['INTENT'][d]['answer']
#                             imsi = [question, answer, intent]
#                             result2.append(imsi)
#                         except:
#                             print('error')


# # cafe = []
# # with open(filename, encoding='utf-8') as file:
# #     data = json.load(file)
# #     for a in range(0, 10):
# #         if data['DATA'][a]['DOMAIN'] == '일반음식점':
# #             for b in range(len(data['DATA'][a]['CATEGORY'])):
# #                 if data['DATA'][a]['CATEGORY'][b]['category'] != '배달음식점':
# #                     for c in range(len(data['DATA'][a]['CATEGORY'][b]['INTENT'])):
# #                         intent = data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['MAIN_INTENT']
# #                         for d in range(len(data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['INTENT'])):
# #                             try :
# #                                 question = data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['INTENT'][d]['question']
# #                                 answer = data['DATA'][a]['CATEGORY'][b]['INTENT'][c]['INTENT'][d]['answer']
# #                                 imsi = [question, answer, intent]
# #                                 result2.append(imsi)
# #                             except:
# #                                 print('error')

# # cafe = pd.DataFrame(cafe, columns = columns)
# # print(cafe.head(10))

# result2 = pd.DataFrame(result2, columns = columns)
# print(result2.head(10))

# data = pd.concat([result, result2], axis=0)
# print(data.head(10))

# result2.to_csv('4.csv', sep=',',index= False, encoding='utf-8')

'''

# import re


# df = pd.read_csv('1.csv', sep=',', encoding='utf-8')
# delivery = []
# for index, row in df.iterrows():
#     imsi = [row['question'], row['answer']]
#     delivery.append(imsi)



# df2 = pd.read_csv('2.csv', sep=',', encoding='utf-8')
# cafe = []
# for index, row in df2.iterrows():
#     imsi = [row['question'], row['answer']]
#     cafe.append(imsi)


# df3 = pd.read_csv('3.csv', sep=',', encoding='utf-8')
# f3 = []
# for index, row in df.iterrows():
#     imsi = [row['question'], row['answer']]
#     f3.append(imsi)



# df4 = pd.read_csv('4.csv', sep=',', encoding='utf-8')
# f4 = []
# for index, row in df2.iterrows():
#     imsi = [row['question'], row['answer']]
#     f4.append(imsi)

# delivery = pd.DataFrame(delivery)
# cafe = pd.DataFrame(cafe)
# f3 = pd.DataFrame(f3)
# f4 = pd.DataFrame(f4)
# temp = pd.concat([delivery, cafe], axis=0)
# temp2 = pd.concat([f3, f4], axis=0)
# data = pd.concat([temp, temp2], axis=0)

# data.to_csv('total.csv', mode='w', encoding='utf-8', index=False)




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

df6 = pd.read_csv('most_updated.csv', sep=',', encoding='utf-8')
t = []
for index, row in df6.iterrows():
    t.append(row)
t = pd.DataFrame(t)
# t.to_csv('kogpt2.txt', mode='w', encoding='utf-8', index=False)

with open('bert_most_updated.txt', 'wt', encoding='utf-8') as file1:
    for index, row in t.iterrows():
        file1.writelines(f'{row[0]}\t{row[1]}\n')
        # file1.writelines(f'[CLS] {row[0]} [SEP] {row[1]} [SEP] \n')
    file1.close()
