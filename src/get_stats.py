import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce
from bidi.algorithm import get_display
from arabic_reshaper import reshape
from persiantools import digits
from matplotlib.ticker import FuncFormatter

## Number of Comments

# Plot
com_cnt = [len(open(f'../data/raw/{i}star.csv', encoding="utf-8").readlines()) - 1 for i in range(1, 5+1)]
labels = tuple(f'{i} ستاره' for i in range(1, 5+1))
fig, ax = plt.subplots()
ax.pie(
    com_cnt,
    labels=list(map(lambda x:get_display(reshape(digits.en_to_fa(x))), labels)),
    autopct=lambda x: digits.en_to_fa('%1.1f%%' % x).replace(".", ','),
    pctdistance=1.25,
    labeldistance=.6
)
fig.savefig("../stats/com_cnt.png", dpi=200)
fig.savefig("../latex_report/Images/com_cnt.png", dpi=200)

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
labels = tuple(f'{i} ستاره' for i in range(1, 5+1))
fig, ax = plt.subplots()
ax.pie(
    sen_cnt,
    labels=list(map(lambda x:get_display(reshape(digits.en_to_fa(x))), labels)),
    autopct=lambda x: digits.en_to_fa('%1.1f%%' % x).replace(".", ','),
    pctdistance=1.25,
    labeldistance=.6
)
fig.savefig("../stats/sen_cnt.png", dpi=200)
fig.savefig("../latex_report/Images/sen_cnt.png", dpi=200)

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
labels = tuple(f'{i} ستاره' for i in range(1, 5+1))
fig, ax = plt.subplots()
ax.pie(
    word_cnt,
    labels=list(map(lambda x:get_display(reshape(digits.en_to_fa(x))), labels)),
    autopct=lambda x: digits.en_to_fa('%1.1f%%' % x).replace(".", ','),
    pctdistance=1.25,
    labeldistance=.6
)
fig.savefig("../stats/word_cnt.png", dpi=200)
fig.savefig("../latex_report/Images/word_cnt.png", dpi=200)

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


## Number of unique words

# Plot
dfs = [pd.read_csv(f'../data/clean/{i}star.csv') for i in range(1, 5+1)]
word_sets = [dfs[i]['0'].apply(lambda x:set(x.split())) for i in range(5)]
unq_word_cnt = [len(reduce(set.union, word_sets[i].tolist())) for i in range(5)]
labels = tuple(f'{i} ستاره' for i in range(1, 5+1))
fig, ax = plt.subplots()
ax.pie(
    unq_word_cnt,
    labels=list(map(lambda x:get_display(reshape(digits.en_to_fa(x))), labels)),
    autopct=lambda x: digits.en_to_fa('%1.1f%%' % x).replace(".", ','),
    pctdistance=1.25,
    labeldistance=.6
)
fig.savefig("../stats/unq_word_cnt.png", dpi=200)
fig.savefig("../latex_report/Images/unq_word_cnt.png", dpi=200)

# Table
output_file = open("../latex_report/tables/unq_word_cnt.csv", "w", encoding="utf-8")
output_file2 = open("../stats/unq_word_cnt.csv", "w", encoding="utf-8")
output_file.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره",
    "تعداد کلمات منحصر به فرد, {},{},{},{},{}".format(*unq_word_cnt)
)))
output_file2.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره",
    "تعداد کلمات منحصر به فرد, {},{},{},{},{}".format(*unq_word_cnt)
)))
output_file.close()
output_file2.close()


## Number of common unique words among each pairs of labels

# Table
unq_words = [reduce(set.union, word_sets[i].tolist()) for i in range(5)]
com_words_cnt = dict()
uncom_words_cnt = dict()
for i in range(1, 5+1): # Label1: i star
    for j in range(i+1, 5+1): # Label2: j star
        com_words_cnt[(i, j)] = len(unq_words[i - 1].intersection(unq_words[j - 1]))
        uncom_words_cnt[(i, j)] = len(unq_words[i - 1]) + len(unq_words[j - 1]) - 2 * com_words_cnt[(i, j)]

pairs = []
pairs_val = []

first_row = [""] * 11
second_row = [""] * 11
second_row[0] = "کلمات منحصربفرد مشترک"
for i, key in enumerate(com_words_cnt, start=1):
    first_row[i] = "{}ستاره و {}ستاره".format(*key)
    second_row[i] = str(com_words_cnt[key])

    pairs.append(first_row[i])
    pairs_val.append(com_words_cnt[key])

csv_content = ",".join(first_row) + '\n' + ",".join(second_row)
output_file = open("../latex_report/tables/com_words_cnt.csv", "w", encoding="utf-8")
output_file2 = open("../stats/com_words_cnt.csv", "w", encoding="utf-8")
output_file.write(csv_content)
output_file2.write(csv_content)
output_file.close()
output_file2.close()

# Plot
pairs_val, pairs = zip(*sorted(zip(pairs_val, pairs)))
pairs = [digits.en_to_fa(get_display(reshape(label))) for label in pairs]

fig, ax = plt.subplots(figsize=(16, 9))
ax.barh(pairs, pairs_val)
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)
# ax.xaxis.set_major_formatter(FuncFormatter(lambda x_val, tick_pos:digits.en_to_fa(str(x_val))))
ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)
ax.invert_yaxis()
for i in ax.patches:
    plt.text(
        i.get_width() + 0.2,
        i.get_y() + 0.5,
        # digits.en_to_fa(str(round((i.get_width()), 2))),
        str(round((i.get_width()), 2)),
        fontsize=10,
        fontweight='bold',
        color='grey'
    )
fig.savefig("../stats/com_words_cnt.png", dpi=200)
fig.savefig("../latex_report/Images/com_words_cnt.png", dpi=200)


## Number of uncommon unique words among each pairs of labels

# Table
pairs = []
pairs_val = []

first_row = [""] * 11
second_row = [""] * 11
second_row[0] = "کلمات منحصربفرد غیرمشترک"
for i, key in enumerate(uncom_words_cnt, start=1):
    first_row[i] = "{}ستاره و {}ستاره".format(*key)
    second_row[i] = str(uncom_words_cnt[key])

    pairs.append(first_row[i])
    pairs_val.append(uncom_words_cnt[key])

csv_content = ",".join(first_row) + '\n' + ",".join(second_row)
output_file = open("../latex_report/tables/uncom_words_cnt.csv", "w", encoding="utf-8")
output_file2 = open("../stats/uncom_words_cnt.csv", "w", encoding="utf-8")
output_file.write(csv_content)
output_file2.write(csv_content)
output_file.close()
output_file2.close()

# Plot
pairs_val, pairs = zip(*sorted(zip(pairs_val, pairs)))
pairs = [digits.en_to_fa(get_display(reshape(label))) for label in pairs]

fig, ax = plt.subplots(figsize=(16, 9))
ax.barh(pairs, pairs_val)
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)
# ax.xaxis.set_major_formatter(FuncFormatter(lambda x_val, tick_pos:digits.en_to_fa(str(x_val))))
ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)
ax.invert_yaxis()
for i in ax.patches:
    plt.text(
        i.get_width() + 0.2,
        i.get_y() + 0.5,
        # digits.en_to_fa(str(round((i.get_width()), 2))),
        str(round((i.get_width()), 2)),
        fontsize=10,
        fontweight='bold',
        color='grey'
    )
fig.savefig("../stats/uncom_words_cnt.png", dpi=200)
fig.savefig("../latex_report/Images/uncom_words_cnt.png", dpi=200)