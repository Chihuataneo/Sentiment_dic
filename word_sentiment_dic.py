# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:58:23 2017
@author: YoungHao
"""

import jieba

positive_emotion_word = []
negative_emotion_word = []
not_word = []
most_word = []
very_word = []
more_word = []
ish_word = []
insufficiently_word = []
over_word = []
    
    # coding: utf-8 

#���÷־�ı�־���ţ����Ը���ʵ����Ҫ�����޸�
cutlist ="������;"

#���ĳ�ַ��Ƿ�־��־���ŵĺ���������ǣ�����True�����򷵻�False
def FindToken(cutlist, char):
    if char in cutlist:
        return True
    else:
        return False
 
#���з־�ĺ��ĺ���    
def Cut(cutlist,lines):          #����1�����÷־��־��������2�����־���ı���Ϊһ�������ַ�
    l = []         #�����б����ڴ洢�����־�ɹ�����������ݣ�Ϊ�����ķ���ֵ
    line = []    #��ʱ�б����ڴ洢���񵽷־��־��֮ǰ��ÿ���ַ���һ�����ַ־���ź󣬾ͻὫ������ȫ������l��Ȼ��ͻᱻ���
        
    for i in lines:         #�Ժ�������2�е�ÿһ�ַ�������м�� ���������У������if��else�Ի�һ��λ�ã�����ö���
        if FindToken(cutlist,i):       #�����ǰ�ַ��Ƿ־����
            line.append(i)          #�����ַ�������ʱ�б���
            l.append(''.join(line))   #���ѵ�ǰ��ʱ�б�����ݼ��뵽�����б���
            line = []  #�������б���գ��Ա��´η־�ʹ��
        else:         #�����ǰ�ַ����Ƿ־���ţ��򽫸��ַ�ֱ�ӷ�����ʱ�б���
            line.append(i)     
    return l
    
def ReadDic():           #��ȡ��дʵ�
    positive_emotion = []
#    positive_evaluation = []
    negative_emotion = []
#    negative_evaluation = []
    notWord = []
    mostWord = []
    veryWord = []
    moreWord = []
    ishWord = []
    insufficientlyWord = []
    overWord = []
    for lines in open("������д�����ģ�.txt"):
        positive_emotion.append(lines)
    for lines in open("������д�����ģ�.txt"):
        negative_emotion.append(lines)
#    for lines in open("�������۴�����ģ�.txt"):
#        negative_evaluation.append(lines)
#    for lines in open("�������۴�����ģ�.txt"):
#        positive_evaluation.append(lines)
    for lines in open("notDictionary.txt"):
        notWord.append(lines)
    for lines in open("most.txt"):
        mostWord.append(lines)
    for lines in open("very.txt"):
        veryWord.append(lines)        
    for lines in open("more.txt"):
        moreWord.append(lines)
    for lines in open("ish.txt"):
        ishWord.append(lines)
    for lines in open("insufficiently.txt"):
        insufficientlyWord.append(lines)
    for lines in open("over.txt"):
        overWord.append(lines)
    for i in positive_emotion:
        positive_emotion_word.append(i.strip())
    for i in negative_emotion:
        negative_emotion_word.append(i.strip())
    for i in notWord:
        not_word.append(i.strip())
    for i in mostWord:
        most_word.append(i.strip())        
    for i in veryWord:
        very_word.append(i.strip())
    for i in moreWord:
        more_word.append(i.strip())
    for i in ishWord:
        ish_word.append(i.strip())        
    for i in insufficientlyWord:
        insufficiently_word.append(i.strip())        
    for i in overWord:
        over_word.append(i.strip())        
        
        
#����Ϊ������������ʵ�ִ��ı��ļ��ж�ȡ���ݲ����з־䡣
def ReadBook():
    split_sentence = []
    split_group = []
    for lines in open("t.txt"):    
        line_dot = lines + '��'
        split_sentence = []
        split_group = []
        l = Cut(list(cutlist),list(line_dot))     
        for line in l:  
           if line.strip() !="":      
                li = line.strip().split()   
                for sentence in li:
                    split_sentence.append(sentence)
                    g = sentence.split("��")
                    for group in g:
                        split_group.append(group)
    ReadDic()
    sumValue = CalNegativeEmotionValue(split_group) + CalPositiveEmotionValue(split_group)
    print(sumValue)

def CalPositiveEmotionValue(split_group):
    posiValue = 0
    for i in split_group:      #�ִʲ���д���
        seg_list = jieba.cut(i)
        t = "/".join(seg_list)
        text = t.split("/")
        j = 0    #�������λ�ü���
        positive_group = []
        not_group_word = []
        degree_word = []

        lastEmotionWordPosition = -1   #��Ϊrange��ԭ������Ϊ-1
        for k in text:
            positive_group_word = []
            if k in positive_emotion_word:
                print("positive:"+ i + ":" + k)
                positive_group_word.append((j, 1, 5))   #��дʣ�����λ�ã�����������ǿ�ȣ�
                for position in range(j, lastEmotionWordPosition, -1):
                    if text[position][0] in not_word:
                        not_group_word.append((position, -1))
                    if text[position][0] in most_word:
                        degree_word.append((position, 2))
                    if text[position][0] in more_word:
                        degree_word.append((position, 1.2))
                    if text[position][0] in very_word:
                        degree_word.append((position, 1.25))                        
                    if text[position][0] in ish_word:
                        degree_word.append((position, 0.8))                        
                    if text[position][0] in insufficiently_word:
                        degree_word.append((position, 0.5))
                    if text[position][0] in over_word:
                        degree_word.append((position, 1.5))
                lastEmotionWordPosition = j
                

                if (len(not_group_word) % 2) != 0:
                    w = -1
                else:
                    w = 1
                if (len(degree_word) >= 1) & (len(not_group_word) >= 1):
                    if degree_word[0][0] > not_group_word[0][0]:
                        w = 0.5
                if (len(degree_word) >= 1):
                    posi = w * degree_word[0][1] * positive_group_word[0][2]
                    print(posi)
                else:
                    posi = w*positive_group_word[0][2]
                    print(posi)
                posiValue = posiValue + posi
                positive_group.append(positive_group_word)
                positive_group.append(not_group_word)
                positive_group.append(degree_word)
                print(positive_group)
                print(posiValue)
            j = j + 1
    return posiValue
       # print(positive_group, not_group_word, most_group_word, very_group_word, more_group_word, insufficient_group_word, ish_group_word, over_group_word)
        
   #     if len(positive_len) == 1:
   #         if not_group_word 
            
def CalNegativeEmotionValue(split_group):
    negaValue = 0
    for i in split_group:      #�ִʲ���д���
        seg_list = jieba.cut(i)
        t = "/".join(seg_list)
        text = t.split("/")
        j = 0    #�������λ�ü���
        negative_group = []
        not_group_word = []
        degree_word = []

        lastEmotionWordPosition = -1
        for k in text:
            negative_group_word = []
            if k in negative_emotion_word:
                print("negative:"+ i + ":" + k)
                negative_group_word.append((j, -1, -5))   #��дʣ�����λ�ã�����������ǿ�ȣ�
                for position in range(j, lastEmotionWordPosition, -1):
                    if text[position][0] in not_word:
                        not_group_word.append((position, -1))
                    if text[position][0] in most_word:
                        degree_word.append((position, 2))
                    if text[position][0] in more_word:
                        degree_word.append((position, 1.2))
                    if text[position][0] in very_word:
                        degree_word.append((position, 1.25))                        
                    if text[position][0] in ish_word:
                        degree_word.append((position, 0.8))                        
                    if text[position][0] in insufficiently_word:
                        degree_word.append((position, 0.5))
                    if text[position][0] in over_word:
                        degree_word.append((position, 1.5))
                lastEmotionWordPosition = j
                

                if (len(not_group_word) % 2) != 0:
                    w = -1
                else:
                    w = 1
                if (len(degree_word) >= 1) & (len(not_group_word) >= 1):
                    if degree_word[0][0] > not_group_word[0][0]:
                        w = 0.5
                if (len(degree_word) >= 1):
                    nega = w * degree_word[0][1] * negative_group_word[0][2]
                    print(nega)
                else:
                    nega = w * negative_group_word[0][2]
                    print(nega)
                negaValue = negaValue + nega 
                negative_group.append(negative_group_word)
                negative_group.append(not_group_word)
                negative_group.append(degree_word)
                print(negative_group)
                print(negaValue)
            j = j + 1
    return negaValue

def CalSumValue():
    ReadDic()
    sumValue = CalNegativeEmotionValue() + CalPositiveEmotionValue()
    print(sumValue)
    