import csv

print('Важно! На этот вопрос следует ответить с большой буквы, используя латиницу!\n'
      'Какой жанр Вы предпочитаете?'
      '(если предпочтений нет, то жмите "Enter"):')
genre = str(input())
genre = genre.split(',')
print('Важно! На этот вопрос следует ответить с большой буквы!\n'
      'Вы больше предпочитаете многосерийное или полнометражное аниме?'
      '(если предпочтений нет, то жмите "Enter"):')
seriesnumber = str(input())
print('Важно! На этот вопрос следует ответить только цифрой!\n'
      'Сколько времени в минутах Вы готовы потратить на просмотр аниме?'
      '(если без разницы, то жмите "Enter"):')
anime_duration = str(input())
print('Важно! На этот вопрос следует ответить с большой буквы, используя латиницу!\n'
      'Какую студию Вы предпочитаете?'
      '(если без разницы, то жмите "Enter"):')
anime_studio = str(input())
anime_studio = anime_studio.split(',')
print('Важно! На этот вопрос следует ответить только цифрой!\n'
      'Какая минмальная оценка аниме Вас устраивает?'
      '(если без разницы, то жмите "Enter"):')
minGrade = str(input())
print('Важно! На этот вопрос следует ответить только цифрой!\n'
      'Какая максимальная оценка аниме Вас устраивает?'
      '(если без разницы, то жмите "Enter"):')
maxGrade = str(input())


def tags(genre):
    for k in range(len(genre)):
        if column[5] == 'Unknown' or column[5] == 'Tags':
            return 0
        elif column[5] == 'Unknown'and genre == '':
            return 1
        elif genre == '':
            return 1
        elif str(genre[k]) not in column[5]:
            return 0
        else:
            return 1


def episodes(seriesnumber):
    if column[8] == 'Unknown' or column[8] == 'Episodes':
        return 0
    elif column[8] == 'Unknown' and seriesnumber == '':
        return 1
    elif seriesnumber == '':
        return 1
    elif seriesnumber == 'Многосерийное':
        if int(column[8]) > 1:
            return 1
        else:
            return 0
    elif seriesnumber == 'Полнометражное':
        if int(column[8]) == 1:
            return 1
        else:
            return 0


def duration(anime_duration):
    if column[10] == 'Unknown' or column[10] == 'Duration':
        return 0
    elif column[10] == 'Unknown' and anime_duration == '':
        return 1
    elif anime_duration == '':
        return 1
    elif int(anime_duration) == int(column[10]):
        return 1
    elif int(anime_duration) < int(column[10]):
        return 0
    elif int(anime_duration) >= int(column[10]):
        return 1


def studio(anime_studio):
    for k in range(len(anime_studio)):
        if column[14] == 'Unknown' or column[14] == 'Studios':
            return 0
        elif column[14] == 'Unknown'and anime_studio == '':
            return 1
        elif anime_studio == '':
            return 1
        elif str(anime_studio[k]) not in column[14]:
            return 0
        else:
            return 1


def grade(minGrade, maxGrade):
    if column[3] == 'Unknown' or column[3] == 'Rating Score':
        return 0
    elif column[3] == 'Unknown' and minGrade == '' and maxGrade == '':
        return 1
    elif minGrade == '' and maxGrade == '':
        return 1
    elif maxGrade == '' and float(minGrade) >= float(column[3]):
        return 1
    elif minGrade == '' and float(maxGrade) <= float(column[3]):
        return 1
    elif float(minGrade) <= float(column[3]) <= float(maxGrade):
        return 1
    else:
        return 0


recomendation = open('recomendation.txt', 'w', encoding='utf-8')
with open('anime.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    for column in reader:
        if tags(genre) == 1 and episodes(seriesnumber) == 1 and duration(anime_duration) == 1 \
        and studio(anime_studio) == 1 and grade(minGrade, maxGrade) == 1:
            recomendation.write(column[1] + '\n')








