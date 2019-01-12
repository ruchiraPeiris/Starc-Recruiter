from Github.Commit_sentiment.Sentiment import calEmotionalLevel
from Github.Github_Api.Retrieve_commits import commitList
import csv



with open('../../Github_repos.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for user2 in csv_reader:
        list2 = []
        list2 = commitList(user2[0], user2[1], user2[2])
        statement = ''
        score = 0
        for commit2 in list2:
            statement += commit2
        if len(list2) >= 5:
            score = calEmotionalLevel(statement)
        print 'Value of ' + user2[1] + ' : ' + str(score)