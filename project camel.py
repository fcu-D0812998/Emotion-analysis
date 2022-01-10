from snownlp import SnowNLP
import jieba as jb
import pandas as pd
import requests
import re
from opencc import OpenCC

book = ""
while 1:
    choose = int(input('請輸入功能選項:1.DC/2.自行輸入文章:'))
    if choose == 1:


        def remove_urls (vTEXT):
            vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
            return(vTEXT)


        num = input('輸入DC文章號碼:')  #233873376 ,233871075 ,233873853,233871104 ,
                                        #233831114 ,233842329 , 233829823 , 233822339 , 233819007
                                        # 233837829 ,
        url = 'http://www.dcard.tw/_api/posts/' + num
        rget = requests.get(url)
        rgetjs = rget.json()

        content = rgetjs['content']
        rcontent = remove_urls(content)
        rcontent = rcontent.replace('\n','').replace('\r','').replace(' ','').replace(u'\xa0','')
        print(rcontent)

        with open('emotion analyse.txt', 'w', encoding="utf-8") as f:
            f.write(rcontent)

        cc = OpenCC('t2s')


        txt = open('emotion analyse.txt', 'r', encoding='utf-8')
        text = txt.read()
        txt.close()


        text = cc.convert(text)
        sentences = []
        senti_score = []
        sum = 0
        count = 0
        s = SnowNLP(text)
        print('計算句子情感值')
        words = jb.cut(text, cut_all=False)
        for i in words:
            a1 = SnowNLP(i)
            a1_tag = a1.tags
            for cot in a1_tag:
                if cot[1] == 'a':
                    a2 = a1.sentiments
                    sentences.append(i)
                    senti_score.append(a2)
                    sum += a1.sentiments
                    count += 1
        print(sentences,senti_score)

        sum /= count

    elif choose == 2:
        book = ''
        print('請輸入你的文章:')
        while True:
            newstr = input()
            if newstr == '0':
                break
            book = book + newstr

        with open('emotion analyse.txt', 'w', encoding="utf-8") as f:
            f.write(book)
        cc = OpenCC('t2s')

        txt = open('emotion analyse.txt', 'r', encoding='utf-8')
        text = txt.read()
        txt.close()

        text = cc.convert(text)
        sentences = []
        senti_score = []
        sum = 0
        count = 0
        s = SnowNLP(text)
        print('計算句子情感值')
        words = jb.cut(text, cut_all=False)
        for i in words:
            a1 = SnowNLP(i)
            a1_tag = a1.tags
            for cot in a1_tag:
                if cot[1] == 'a':
                    a2 = a1.sentiments
                    sentences.append(i)
                    senti_score.append(a2)
                    sum += a1.sentiments
                    count += 1
        print(sentences, senti_score)

        sum /= count

    if sum <= 0.43:
         print(sum)
         print('這是一個負面評價')
    elif sum >= 0.57:
        print(sum)
        print('這是一個正面評價')
    else:
        print(sum)
        print('這是一個中性評價')