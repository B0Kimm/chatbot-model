import os
import sys
import json
import nltk
import konlpy.tag import Mecab
from chatspace import ChatSpace
from tqdm import tqdm_pandas
from pykospacing import spacing #spacing
import torch



class ChatbotClassification:
    def __init__(self):
        ...

    
    #데이터 전처리
    def cleansing(self, text):
        only_BMP_pattern = re.compile("["
        u"\U00010000-\U0010FFFF" 
                           "]+", flags=re.UNICODE)
        new_text = only_BMP_pattern.sub(r' ', str(text))
        new_text = emoji_pattern.sub(r' ', new_text)
        new_text = re.sub('[❤️★♥️✨⭐♡♥☆⚽️⚾️❄❣️❤]', ' ', new_text) 
        pattern = '([ㄱ-ㅎㅏ-ㅣ]+)' #한글 자음 모음 제거 ㅋㅋㅋㅋ
        new_text = re.sub(pattern=pattern, repl='', string=new_text)
        new_text = re.sub('[-=+,#/\:^$@*\"※~&%ㆍ!』\\‘;|\(\)\[\]\<\>`\'…》]', ' ', new_text) #특수기호
        new_text = re.sub('  ', ' ', new_text) #띄어쓰기가 2번이상 들어가면 -> 1번
        return new_text

    #가격 정보 전처리 (3인분, 3인, 3명)
    def number_filter(self, text):
        pattern = r'\d{1,3}[,\.]\d{1,3}[만\천]?\s?[원]|\d{1,5}[만\천]?\s?[원]'
        text = re.sub(pattern, 'money', text)
        pattern = r'[일/이/삼/사/오/육/칠/팔/구/십/백][만\천]\s?[원]'
        text = re.sub(pattern, 'money', text)
        pattern = r'(?!-)\d{2,4}[0]{2,4}(?!년)(?!.)|\d{1,3}[,/.]\d{3}'
        text = re.sub(pattern, 'money', text)
        

    def tokenizer(self, corpus, save_name, space=False):
        toeknizer = Mecab(dicpath='C:/mecab/mecab-ko-dic')
        total_lines = sum(1 for line in open(corpus, 'r', encoding='utf-8'))
        # tqdm에 입력할 total값을 구하기 위해 사용

        with open(corpus, 'r', encoding='utf-8') as f1, open(save_name, 'w', encoding='utf-8') as f2:
            for _, line in tqdm(enumerate(f1), total=total_lines):
                sentence = line.replace('\n','').strip()
                if space: 
                    sentence = spacing(line.replace('\n', '').strip())
                toeknized_sent = ' '.join(tokenizer.morphs(sentence))
                f2.writelines(toeknized_sent+'\n')

    def shaper(self, text)
        

    

