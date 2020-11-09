


def whitespace_tokenize(data):
    data = data.strip()    # 문자열의 맨앞, 맨끝 공백 지움
    if not data:
        return []
    tokens = data.split()  # 문자열을 스페이스,탭,엔터 단위로 분리하여 배열에 집어넣음
    return tokens


txt_file = open("./dic/corpus.txt", 'r', encoding='utf-8')
korquad_data = txt_file.read()
txt_file.close()

for wst in whitespace_tokenize(korquad_data):   # wst : 공백,탭,엔터 기준 문자열 하나
    print(wst)
    break


