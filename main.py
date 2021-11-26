import json
from sys import path
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def main(path):
    data = json.load(open(path, encoding='utf-8'))
    notification = data['posted']
    notification_len = len(notification)
    notification_id =[]
    notification_polarity = []
    notification_subjectivity = []


    for i in range(notification_len):
        text = notification[i]['text']
        nid = notification[i]['nid']
        notification_id.append(nid)

        sia = SentimentIntensityAnalyzer()
        ss = sia.polarity_scores(text)
        cmpd = ss['compound']
        notification_polarity.append(cmpd)
        if ss['compound'] < 0:
            polarity = 'negative'
        elif ss['compound'] > 0:
            polarity = 'positive'
        else:
            polarity = 'neutral'    
        notification_subjectivity.append(polarity)
    
    return notification_id, notification_polarity, notification_subjectivity



'''
Documentation:-
path :- 
path of the json file passed in as an argument to the function 

return:-
polarity :-
polarity of the notification POSITIVE, NEGATIVE, NEUTRAL
nid :-
nid of the notification
may be same or different for different notifications
cmpd :-
compound score of the notification

notification_id, notification_polarity, notification_subjectivity = main()
notification_id = list of notification id
notification_polarity = list of notification polarity
notification_subjectivity = list of notification subjectivity


puriyala naa kaelu !!
'''

