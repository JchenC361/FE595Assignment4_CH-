import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from operator import itemgetter
from collections import defaultdict

# Extract the name of files and save the file names of male data and female data in two separate lists.
HeFileNamesList = os.listdir("D:\He")
SheFileNamesList = os.listdir("D:\She")

# Initialize analyzer.
analyzer = SentimentIntensityAnalyzer()

# Create a male dictionary combining sentences with their neg, pos, and compound values.
HeFileList = []
HeFileValueList = []
for e in HeFileNamesList:
    HePath = "/He/"+e
    file_he = open(HePath, "r")
    txt = file_he.read()
    txt_array = txt.split("He")
    txt_array.pop(0)
    for e_txt in txt_array:
        WhatHeDoes = "He"+e_txt
        HeFileList.append(WhatHeDoes)
        sentence_value_dict_element = analyzer.polarity_scores(WhatHeDoes)
        sentence_value_dict_element['What is he like?'] = WhatHeDoes
        HeFileValueList.append(sentence_value_dict_element)

# Save the merged male information in a txt file.
with open('/He.txt', mode='wt', encoding='utf-8') as file:
    file.write(''.join(HeFileList))
# Sort male sentences with respect to compound value.
HeFileListSortedByCompound = sorted(HeFileValueList, key=itemgetter('compound'))

# Correct interpunction error from sentences.
WhatIsMaleLike = []
MaleCleanData = []
for i in range(0, len(HeFileListSortedByCompound)):
    WhatIsMaleLike.append(HeFileListSortedByCompound[i]['What is he like?'])
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace(". \n", ".")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace("! \n", "!")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace(".\n", ".")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace("!\n", "!")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace("\n", ".")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace("..", ".")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace(".'.", "'.")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace(".' .", "'.")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace(".' ", ".")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace("  .", ".")
    WhatIsMaleLike[i] = WhatIsMaleLike[i].replace(" .", ".")
    MaleCleanData.append(WhatIsMaleLike[i] + "\n")

# Save the male information with clean data.
with open('/He_CleanData.txt', mode='wt', encoding='utf-8') as file:
    file.write(''.join(MaleCleanData))

# Create a female dictionary combining sentences with their neg, pos, and compound values.
SheFileList = []
SheFileValueList = []
for e in SheFileNamesList:
    ShePath = "/She/"+e
    file_she = open(ShePath, "r")
    txt = file_she.read()
    txt_array = txt.split("She")
    txt_array.pop(0)
    for e_txt in txt_array:
        WhatSheDoes = "She"+e_txt
        SheFileList.append(WhatSheDoes)
        sentence_value_dict_element = analyzer.polarity_scores(WhatSheDoes)
        sentence_value_dict_element['What is she like?'] = WhatSheDoes
        SheFileValueList.append(sentence_value_dict_element)

# Save the merged female information in a txt file.
with open('/She.txt', mode='wt', encoding='utf-8') as file:
    file.write(''.join(SheFileList))
# Sort female sentences with respect to compound value.
SheFileListSortedByCompound = sorted(SheFileValueList, key=itemgetter('compound'))


# Correct interpunction error from sentences.
WhatIsFemaleLike = []
FemaleCleanData = []
for i in range(0, len(SheFileListSortedByCompound)):
    WhatIsFemaleLike.append(SheFileListSortedByCompound[i]['What is she like?'])
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace(". \n", ".")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace("! \n", "!")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace(".\n", ".")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace("!\n", "!")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace("\n", ".")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace("..", ".")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace(".'.", "'.")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace(".' .", "'.")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace(".' ", ".")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace("  .", ".")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace(" .", ".")
    WhatIsFemaleLike[i] = WhatIsFemaleLike[i].replace(". ", ".")
    FemaleCleanData.append(WhatIsFemaleLike[i]+"\n")

# Save the male information with clean data.
with open('/She_CleanData.txt', mode='wt', encoding='utf-8') as file:
    file.write(''.join(FemaleCleanData))

# Pick up the first element, the record with the worst character of male, from sorted male list.
WhatIsTheWorstMaleLike = WhatIsMaleLike[0]
# Pick up the first element, the record with the worst character of female, from sorted female list.
WhatIsTheWorstFemaleLike = WhatIsFemaleLike[0]
# Combine last two sentences and "They fight crime!"
TheWorstGroup = WhatIsTheWorstMaleLike + " " + WhatIsTheWorstFemaleLike + " "
TheWorstGroup = TheWorstGroup + "They fight crime!"

# Pick up the last element, the record with the best character of male, from sorted male list.
WhatIsTheBestMaleLike = WhatIsMaleLike[len(WhatIsMaleLike)-1]
# Pick up the last element, the record with the best character of female, from sorted female list.
WhatIsTheBestFemaleLike = WhatIsFemaleLike[len(WhatIsFemaleLike)-1]
# Combine last two sentences and "They fight crime!"
TheBestGroup = WhatIsTheBestMaleLike + " " + WhatIsTheBestFemaleLike + " "
TheBestGroup = TheBestGroup + "They fight crime!"

# Use defaultdict package in python to calculate how many times each sentences appear.
d_Male = defaultdict(int)
d_Female = defaultdict(int)
for line in WhatIsMaleLike:
    d_Male[line] += 1
for line in WhatIsFemaleLike:
    d_Female[line] += 1

# Create a list to save the most common male sentences.
# Since no sentence appear more than twice, we can take number two as condition to grasp the most common descriptions.
MaleCommonSentencesList = []
for line in d_Male:
    if d_Male[line] == 2:
        MaleCommonSentencesList.append(line+"\n")
with open('/He_mostCommonSentences.txt', mode='wt', encoding='utf-8') as file:
    file.write(''.join(MaleCommonSentencesList))

# Create a list to save the most common female sentences.
# Since no sentence appear more than twice, we can take number two as condition to grasp the most common descriptions.
FemaleCommonSentencesList = []
for line in d_Female:
    if d_Female[line] == 2:
        FemaleCommonSentencesList.append(line+"\n")
with open('/She_mostCommonSentences.txt', mode='wt', encoding='utf-8') as file:
    file.write(''.join(FemaleCommonSentencesList))

