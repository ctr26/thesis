import git
repo = git.Repo()
path = "count.txt"

g = git.Git()
hexshas = g.log('--pretty=%H','--follow','--',path).split('\n')

loginfo = g.log(path,p=True)
# print(loginfo)

import re

dates = re.findall('(?<=Date:)(.*)(?=\n)', loginfo)
words = re.findall('(?<=\+Words in text:)(.*)(?=\n)', loginfo)

from dateutil import parser

parsed_dates =[]
for i,date in enumerate(dates):
    parsed_dates.append(parser.parse(date))

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4))
# fig.autofmt_xdate(rotation=45)
plt.plot_date(parsed_dates[0:92],words[0:92])
plt.draw()
fig.savefig('tessstttyyy.png', dpi=100)
plt.savefig('temp.pdf')
