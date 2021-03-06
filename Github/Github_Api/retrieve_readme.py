import requests
import csv
import json
import base64
import nltk
from nltk.tokenize import word_tokenize

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
total_words = 0
def words_list(userName):

    repo_name = ''
    with open('../../Github_repos.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for raw in csv_reader:
            if raw[2] == userName:
                repo_name = raw[3]
                print(repo_name)
                break
    word_tokens = ''
    try:
        response = requests.get('https://api.github.com/repos/'+userName+'/'+repo_name+'/readme?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34')
        data = json.loads(response.content)
        decoded_content = base64.b64decode(data["content"])
        words = decoded_content.decode('utf-8')
        word_tokens = word_tokenize(words)
    except Exception as ex:
        print('Error occurred: '+str(ex))
        return [], 0


    filtered_sentence = []
    for w in word_tokens:
        if w != '``':
            filtered_word = remove_punctuations(w)
            if filtered_word:
                filtered_sentence.append(filtered_word)

    total_words = len(filtered_sentence)
    return filtered_sentence, total_words


def remove_punctuations(str):
    no_punct = ""
    for char in str:
        if char not in punctuations:
            no_punct = no_punct + char

    return no_punct

# words_list('ThisaruGuruge')