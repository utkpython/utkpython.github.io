#describe = { "cat": "cute", "dog": "friendly", "fish": "smelly", "dragon": "mythical", "python": "fun" }

#describe["cat"]
#describe["python"]

#adjectives = { "cat": ["cute","fluffy"], 
#                "dog": ["friendly","loyal", "happy"], 
#                "fish": ["smelly","swimmy"], 
#                "dragon": ["mythical","fire-breathing"], 
#                "python": ["fun", "badass"] }

#for noun in adjectives:
#  print "a", ', '.join(adjectives[noun]), noun
  
  
  
#tetrisScores = { "Kim Kardashian": 100000,
#                "Kanye West": 80000,
#                "Taylor Swift": 130000,
#                "Bill Gates": 97000,
#                "Ash Ketchum": 900000,
#                "Barack Obama": 102000,
#                "Marissa Mayer": 1000000}

#for player in tetrisScores:
#  print tetrisScores[player]

#### a more complicated example
#### didn't know that bill gates' birthday was actually 10/28 --- the day of the seminar
#tetrisDB = { "Kim Kardashian":   {"high score":300000, "age": 34},
#                "Kanye West":    {"high score": 200000, "age": 37},
#                "Taylor Swift":  {"high score": 430000, "age": 24},
#                "Bill Gates":    {"high score": 97000, "age": 60},
#                "Ash Ketchum":   {"high score": 800000, "age": 10},
#                "Barack Obama":  {"high score": 102000, "age": 53},
#                "Marissa Mayer": {"high score": 1000000, "age": 39}}

#names = []
#scores = []
#ages = []                               
#for player in tetrisDB:
#    names.append(player)
#    scores.append(tetrisDB[player]["high score"])
#    ages.append(tetrisDB[player]["age"])

#from pylab import *

#scatter(ages,scores)
#show(plot)
