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