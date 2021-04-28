from playsound import playsound
import time
import datetime
import json
from pathlib import Path
from random import randint


# credit to: https://github.com/chinese-poetry/chinese-poetry
poetry_path = Path('poet_tang')
poetry_files = list()
for file in poetry_path.iterdir():
    if file.is_file():
        poetry_files.append(file)
# print(poetry_files)


def random_poetry_line():
    rand_poetry_file = poetry_files[randint(0, len(poetry_files)-1)]
    #print(rand_poetry_file)

    with open(rand_poetry_file, 'r') as f:
        poetry_data = json.load(f)

    # print(poetry_data)

    random_poetry = poetry_data[randint(0, len(poetry_data)-1)]
    random_paragraphs = random_poetry['paragraphs']
    random_line = random_paragraphs[randint(0, len(random_paragraphs)-1)]
    print(random_line)
    print(random_poetry['author'], '-', random_poetry['title'])


wav_file = 'poop.wav'
while True:
    playsound(wav_file)
    print('\n', datetime.datetime.now())
    random_poetry_line()
    print('\n')
    time.sleep(239)
