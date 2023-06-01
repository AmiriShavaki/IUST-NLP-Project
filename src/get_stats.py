import matplotlib.pyplot as plt
import pandas as pd

## Number of Comments

# Plot
com_cnt = [len(open(f'../data/raw/{i}star.csv', encoding="utf-8").readlines()) - 1 for i in range(1, 5+1)]
labels = tuple(f'{i} star' for i in range(1, 5+1))
fig, ax = plt.subplots()
ax.pie(com_cnt, labels=labels, autopct='%1.1f%%', pctdistance=1.25, labeldistance=.6)
fig.savefig("../stats/com_cnt.png")
fig.savefig("../latex_report/Images/com_cnt.png")

# Table
output_file = open("../latex_report/tables/com_cnt.csv", "w", encoding="utf-8")
output_file2 = open("../stats/com_cnt.csv", "w", encoding="utf-8")
output_file.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد کامنت جمع‌آوری‌شده, {},{},{},{},{},{}".format(*com_cnt, sum(com_cnt))
)))
output_file2.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد کامنت جمع‌آوری‌شده, {},{},{},{},{},{}".format(*com_cnt, sum(com_cnt))
)))
output_file.close()
output_file2.close()


## Number of sentences

# Plot
dfs = [pd.read_csv(f'../data/sentencebroken/{i}star.csv') for i in range(1, 5+1)]
sen_cnt = [sum(df.apply(lambda x: x.notnull().sum(), axis='columns')) for df in dfs]
labels = tuple(f'{i} star' for i in range(1, 5+1))
fig, ax = plt.subplots()
ax.pie(sen_cnt, labels=labels, autopct='%1.1f%%', pctdistance=1.25, labeldistance=.6)
fig.savefig("../stats/sen_cnt.png")
fig.savefig("../latex_report/Images/sen_cnt.png")

# Table
output_file = open("../latex_report/tables/sen_cnt.csv", "w", encoding="utf-8")
output_file2 = open("../stats/sen_cnt.csv", "w", encoding="utf-8")
output_file.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد جملات, {},{},{},{},{},{}".format(*sen_cnt, sum(sen_cnt))
)))
output_file2.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد جملات, {},{},{},{},{},{}".format(*sen_cnt, sum(sen_cnt))
)))
output_file.close()
output_file2.close()


## Number of words

# Plot
dfs = [pd.read_csv(f'../data/clean/{i}star.csv') for i in range(1, 5+1)]
word_cnt = [sum(dfs[i]['0'].apply(lambda x:len(x.split()))) for i in range(5)]
labels = tuple(f'{i} star' for i in range(1, 5+1))
fig, ax = plt.subplots()
ax.pie(word_cnt, labels=labels, autopct='%1.1f%%', pctdistance=1.25, labeldistance=.6)
fig.savefig("../stats/word_cnt.png")
fig.savefig("../latex_report/Images/word_cnt.png")

# Table
output_file = open("../latex_report/tables/word_cnt.csv", "w", encoding="utf-8")
output_file2 = open("../stats/word_cnt.csv", "w", encoding="utf-8")
output_file.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد کلمات, {},{},{},{},{},{}".format(*word_cnt, sum(word_cnt))
)))
output_file2.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد کلمات, {},{},{},{},{},{}".format(*word_cnt, sum(word_cnt))
)))
output_file.close()
output_file2.close()