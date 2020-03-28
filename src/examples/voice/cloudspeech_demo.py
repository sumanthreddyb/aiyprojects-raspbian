
#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import process_text.py as processText
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random

#variables initalization
phase="Intro"
Family=0
Friends=0
Academics=0
Others=0
intro_text="Hi there May i know your good name please"
greet_text="Hello [*****] My name is Dimple, I am your counsellor friend.I shall ask you questions about you and you can feel free to converse with me.You will be rewarded at the end of conversation"
questions=[{'ques':'Do Your  parents encourge you to make your own decisions ?','intent':'Family'},
           {'ques':'Do You think that your  parents try to control everything you do ?','intent':'Family'},
           {'ques':'Do you feel that my talents are not recognized well enough in your class?','intent':'Friends'},
           {'ques':'What do you do when somone corrects your mistakes?','intent':'Others'},
           {'ques':'Do you make friends Easily','intent':'Friends'},
           {'ques':'Who are your best friends','intent':'Friends'},
           {'ques':'Do you have any Enemies','intent':'Others'},
           {'ques':'Do you enjoy doing your homeworks ?','intent':'Academics'},
           {'ques':'Do you fear exams or tests ?','intent':'Academics'}]
total_questions=len(questions)
sid = SentimentIntensityAnalyzer()
sentimentScore={}


#Functions declaration
def summarize():
    print("You seem to be interesting than all others I have seen Get Lost !!!")
    
def getReply(ques):
    return(input(ques))

def getRandomQuestion():
    globals()['total_questions']=len(questions)
    if total_questions>0:
        rand_index=random.randint(0,total_questions-1)
        rand_question=questions[rand_index]
        del questions[rand_index]
        return(rand_question)
    else:
        summarize()
        
def processReply(reply,intent):
    sentimentScore = sid.polarity_scores(reply)
    if sentimentScore['compound']>0:
        globals()[intent]+=sentimentScore['pos']
        print('pos:',sentimentScore['pos'])
    else:
        globals()[intent]-=sentimentScore['neg']
        print('neg:',sentimentScore['neg'])
        
    

print(greet_text)
question={}
while(True):
    question=getRandomQuestion()
    if(question):
        reply=getReply(question['ques'])
        processReply(reply, question['intent'])
    else:
        break
print('Your Scoring is: \n Family: ',Family,'\n Friends: ',Friends,'\n Academics: ',Academics,'\n Others: ',Others,"\n ******************")
