import pandas as pd
from pandas import DataFrame
import re


df = pd.read_csv('crazy.csv', sep=',', encoding='utf-8')

for index, row in df.iterrows():
    if row['intent'] == '카카오페이삼성페이결제':
        row['intent'] = '88'
    elif row['intent'] == '클로징시간문의':
        row['intent'] = '89'
    elif row['intent'] == '클로징주문시간문의':
        row['intent'] = '90'
    elif row['intent'] == '토핑문의':
        row['intent'] = '91'
    elif row['intent'] == '특정재료첨삭요구':
        row['intent'] = '92'
    elif row['intent'] == '포장가격문의':
        row['intent'] = '93'
    elif row['intent'] == '포장시할인문의':
        row['intent'] = '94'
    elif row['intent'] == '할인방법문의':
        row['intent'] = '95'
    elif row['intent'] == '할인정보문의':
        row['intent'] = '96'
    elif row['intent'] == '할인쿠폰사용':
        row['intent'] = '97'
    elif row['intent'] == '할인쿠폰적립카드문의':
        row['intent'] = '98'
    elif row['intent'] == '할인행사기간문의':
        row['intent'] = '99'
    elif row['intent'] == '현금영수증발행요청':
        row['intent'] = '100'
    elif row['intent'] == '현금할인문의':
        row['intent'] = '101'
    elif row['intent'] == '홀가격과배달가격차이문의':
        row['intent'] = '102'
    elif row['intent'] == '홀식사문의':
        row['intent'] = '103'
    elif row['intent'] == '휴일문의':
        row['intent'] = '104'
    elif row['intent'] == '1인1잔문의':
        row['intent'] = '105'
    elif row['intent'] == 'MD제품문의':
        row['intent'] = '106'
    elif row['intent'] == '결제문의':
        row['intent'] = '107'
    elif row['intent'] == '결제요청':
        row['intent'] = '108'
    elif row['intent'] == '계열사문의':
        row['intent'] = '109'
    elif row['intent'] == '계절메뉴주문문의':
        row['intent'] = '110'
    # elif row['intent'] == '예약배달문의':
    #     row['intent'] = '65'
    # elif row['intent'] == '영업시간문의':
    #     row['intent'] = '64'
    # elif row['intent'] == '엘지멤버십할인문의':
    #     row['intent'] = '63'
    # elif row['intent'] == '양에대한질문':
    #     row['intent'] = '62'
    # elif row['intent'] == '양념소스요구':
    #     row['intent'] = '61'
    # elif row['intent'] == '양념소스별도구매문의':
    #     row['intent'] = '60'
    # elif row['intent'] == '앱주문할인문의':
    #     row['intent'] = '59'
    # elif row['intent'] == '앱문의':
    #     row['intent'] = '58'
    # elif row['intent'] == '신메뉴문의':
    #     row['intent'] = '57'
    # elif row['intent'] == '식재료문의':
    #     row['intent'] = '56'
    # elif row['intent'] == '식사배달요청':
    #     row['intent'] = '55'
    # elif row['intent'] == '술배달문의요청':
    #     row['intent'] = '54'
    # elif row['intent'] == '수저요구':
    #     row['intent'] = '53'
    # elif row['intent'] == '소스정보문의':
    #     row['intent'] = '52'
    # elif row['intent'] == '세트메뉴할인문의':
    #     row['intent'] = '51'
    # elif row['intent'] == '세트메뉴중메뉴교환문의요청':
    #     row['intent'] = '50'
    # elif row['intent'] == '세트메뉴주문':
    #     row['intent'] = '49'
    # elif row['intent'] == '세트메뉴종류문의':
    #     row['intent'] = '48'
    # elif row['intent'] == '세트메뉴서비스문의':
    #     row['intent'] = '47'
    # elif row['intent'] == '세트메뉴구성문의':
    #     row['intent'] = '46'
    # elif row['intent'] == '선결제문의':
    #     row['intent'] = '45'
    # elif row['intent'] == '서비스변경주문문의':
    #     row['intent'] = '44'
    # elif row['intent'] == '서비스문의':
    #     row['intent'] = '43'
    # elif row['intent'] == '상품권결제':
    #     row['intent'] = '42'
    # elif row['intent'] == '사이즈-업문의요청':
    #     row['intent'] = '41'
    # elif row['intent'] == '사이드메뉴정보문의':
    #     row['intent'] = '40'
    # elif row['intent'] == '빨리되는메뉴문의':
    #     row['intent'] = '39'
    # elif row['intent'] == '베스트메뉴문의추천요청':
    #     row['intent'] = '38'
    # elif row['intent'] == '배달출발도착알림요청':
    #     row['intent'] = '37'
    # elif row['intent'] == '배달장소범위문의':
    #     row['intent'] = '36'
    # elif row['intent'] == '배달용기변경요청':
    #     row['intent'] = '35'
    # elif row['intent'] == '배달용기문의':
    #     row['intent'] = '34'


df.to_csv('crazy.csv', mode='w', encoding='utf-8', index=False)




print(df.head(20))
