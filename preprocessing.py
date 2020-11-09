import os
import sys
import json
import nltk
import pandas as pd
from pandas import DataFrame
import csv
import re
# from konlpy.tag import Mecab
from konlpy.tag import Okt
# from chatspace import ChatSpace
from tqdm import tqdm_pandas
# from pykospacing import spacing #spacing
# import torch

clfc_column = ['question', 'answer', 'intent']


class Chatbot:
    def __init__(self):
        ...

    def hook(self):
        ...

    def extracting(self, filename, domain, category) :
        result = []
        with open(filename+'.json', 'rb') as json_file:
                    data = json.load(json_file)
                    for idx in range(0, 10):
                        if data['DATA'][idx]['DOMAIN'] == f'{domain}':
                            for n in range(0,1):
                                if data['DATA'][idx]['CATEGORY'][n]['category'] == f'{category}':
                                    for a in range(0, 132):  #len으로 바꾸기 / 114 /132
                                        intent = data['DATA'][idx]['CATEGORY'][n]['INTENT'][a]['MAIN_INTENT']
                                        for item in data['DATA'][idx]['CATEGORY'][n]['INTENT'][a]['INTENT']:
                                            try: 
                                                answer = item['answer']
                                                question = item['question']
                                                imsi = [ question, answer, intent]
                                                result.append(imsi)
                                            except :
                                                print('error')

        result = pd.DataFrame(result, columns=clfc_column)
        outputname = f'{filename}.csv'
        result.to_csv(outputname, mode='w', encoding='utf-8', index=False)
    
    #데이터 전처리
    def cleansing(self, text):
        only_BMP_pattern = re.compile("["
        u"\U00010000-\U0010FFFF" 
                           "]+", flags=re.UNICODE)
        new_text = only_BMP_pattern.sub(r' ', str(text))
        new_text = re.sub('[❤️★♥️✨⭐♡♥☆⚽️⚾️❄❣️❤]+', ' ', new_text) 
        pattern = '([ㄱ-ㅎㅏ-ㅣ]+)' #한글 자음 모음 제거 ㅋㅋㅋㅋ
        new_text = re.sub(pattern=pattern, repl='', string=new_text)
        new_text = re.sub('[-=+,#/\:^$@*\"※~&%ㆍ!』\\‘;|\(\)\[\]\<\>`\'…》]', ' ', new_text) #특수기호
        new_text = re.sub(' +', ' ', new_text) #띄어쓰기가 2번이상 들어가면 -> 1번
        return new_text

    #가격 정보 전처리 
    def number_filter(self, text):
        pattern = r'\d{1,3}[,\.]\d{1,3}[만\천]?\s?[원]|\d{1,5}[만\천]?\s?[원]'
        text = re.sub(pattern, 'money', text)
        pattern = r'[일/이/삼/사/오/육/칠/팔/구/십/백][만\천]\s?[원]'
        text = re.sub(pattern, 'money', text)
        pattern = r'(?!-)\d{2,4}[0]{2,4}(?!년)(?!.)|\d{1,3}[,/.]\d{3}'
        text = re.sub(pattern, 'money', text)

    def phone_number_filter(text):
        re_pattern = r'\d{2,3}[-\.\s]*\d{3,4}[-\.\s]*\d{4}(?!\d)'
        new_text = re.sub(re_pattern, 'tel', text)
        re_pattern = r'\(\d{3}\)\s*\d{4}[-\.\s]??\d{4}'
        new_text = re.sub(re_pattern, 'tel', new_text)
        return new_text

    # 사람 정보 (3인분, 3인, 3명)
    def person_filter(self, text):
        ...

    # 몇 동 몇 호 1잔이
    def address_filter(self, text):
        ...

    # 전화번호
    def number_filter(self, text):
        pattern = r'^[0-9]+-[0-9]+'
        text =re.sub(pattern, 'phone', text)
    
    # 용량
    def quantity_filter(self, text):
        ...

    def stopword(self, filename, index):
        df = pd.read_csv(f'{filename}.csv', sep = ',', encoding= 'utf-8')
        
        mecab = Mecab(dicpath='C:/mecab/mecab-ko-dic')
        result = []
        stopword = []
        # stopword 리스트 만들기
        with open('stopword.txt', 'r', encoding='utf-8') as file:
            for text in file:
                w = text.strip('\n')
                stopword.append(w)

        outcome = []
                
        for index, row in df.iterrows():
            temp_q = []
            # temp_q = mecab.morphs(sentence)
            sentence = row[f'{index}']
            temp_q = mecab.morphs(sentence)
                    
            q_temp = []
            for token in temp_q:
                if token not in stopword:
                    q_temp.append(token)
            toeknized_sent = ' '.join(q_temp)
            outcome.append(toeknized_sent)

        outcome = pd.DataFrame(outcome, columns=['question']) 


    def tokenizer(self, filename, saving_name):
        df = pd.read_csv(f'{filename}.csv', sep = ',', encoding= 'utf-8')
        with open(saving_name, 'w', encoding='utf-8') as file:
            for index, row in data.iterrows():
                file.write(str(row['question']) + '\t' + str(row['answer']) + '\n')
            file.close()         

        

    
if __name__ == '__main__':
    # Chatbot().extracting('dialog.json', '카페', '카페')
    chatbot = Chatbot()
    chatbot.stopword('testjson')
    
