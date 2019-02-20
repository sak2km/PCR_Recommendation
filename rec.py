
# coding: utf-8

import urllib
import webbrowser
import pdb


def recommend_suid(speaker_id, mood_id, scream, cry):
    # using outputs form acoustics, return appropriate recommendation (survey)

    # basic dictionary for temporary testing {mood_id : recommended survey_id}
    mood_2_rec = {
        'H' : 1, # "HAPPY! Listen to some music you like.",
        'A' : 2, # "ANGRY! Relax and grab a cup of tea :)",
        'N' : 3, # "NEUTRAL! Do some yoga",
        'S' : 4, # "SAD! Talk to your friend.",
        # 'Sc' : 4, # "SCREAM! Calm down.",
        # 'Cr' : 5  # "CRY! Stop crying and walk around."
    }
    survey_id = mood_2_rec[mood_id]
    # For now, if screamed, add 5, and add 10 if cried
    if scream:
        survey_id += 5
    if cry:
        survey_id += 10
    return survey_id


def send_rec(phone_url, speaker_id, survey_id, server_url, androidid, empathid, alarm):
    print("survey_id: %s"%survey_id)
    # example url:
    # http://191.168.0.106:2226/?q={"id":"2","c":"startsurvey","suid":16,"server":"http://191.168.0.107/ema/ema.php","androidid":"db7d3cdb88e1a62a","empathid":"999|1550004755","alarm":"true"}
    # http://191.168.0.106:2226/?q={"id":"2","c":"startsurvey","suid":16,"server":"http://191.168.0.107/ema/ema.php","androidid":"db7d3cdb88e1a62a","empathid":"999|1550004755","alarm":"True"}
    # pdb.set_trace()
    url = phone_url + "/?q={\"id\":\""+speaker_id+"\",\"c\":\"startsurvey\",\"suid\":"+ survey_id + ",\"server\":\""+server_url+"\",\"androidid\":\""+androidid+"\",\"empathid\":\""+empathid+"\",\"alarm\":\""+str(alarm).lower()+"\"}"
    print("url: %s"%url)
    # urllib.urlopen(url)
    webbrowser.open(url) # to open on browser
    # return
    


if __name__ == '__main__':
    # input to be changed: (phone_url, mood_id, speaker_id, server_url, androidid, empathid, alarm)
    # get recommended survey_id based on speaker_id and classified mood_id
    survey_id = recommend_suid(speaker_id='123',mood_id='H', scream=1, cry=1)

    # based on recommended survey_id, form url to trigger phone buzz, using other parameters
    send_rec(phone_url='http://191.168.0.106:2226', speaker_id='2', survey_id=str(survey_id), server_url='http://191.168.0.107/ema/ema.php', androidid='db7d3cdb88e1a62a', empathid='999|1550004755', alarm=True) 

# Outputs from acoustic pipeline 
# line 1: speaker ID. possible value: 0, 1, 2. 0 denotes speaker #1, 1 denotes speaker #2, 2 denotes un-identifiable speaker.
# line 2: mood from the audio clip. possible value: H, A, N, S, standing for happy, angry, neutral, sad respectively.
# line 3: scream. possible value: 0, 1. 0 represents that screaming is not detected. 1 represents screaming is detected.
# line 4: cry. possible value: 0, 1. 0 represents that crying is not detected. 1 represents crying is detected.