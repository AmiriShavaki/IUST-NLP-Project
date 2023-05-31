import os
import pandas as pd

file_sizes_before = [
    "\\lr{{{:.2f}MB}}".format(os.path.getsize(f'../data/raw/{i}star.csv') / 1048576) for i in range(1, 5+1)
]
file_sizes_before.append("\\lr{{{:.2f}MB}}".format(sum(
    os.path.getsize(f'../data/raw/{i}star.csv') / 1048576 for i in range(1, 5+1)
)))
file_sizes_after = [
    "\\lr{{{:.2f}MB}}".format(os.path.getsize(f'../data/clean/{i}star.csv') / 1048576) for i in range(1, 5+1)
]
file_sizes_after.append("\\lr{{{:.2f}MB}}".format(sum(
    os.path.getsize(f'../data/clean/{i}star.csv') / 1048576 for i in range(1, 5+1)
)))

dfs = [pd.read_csv(f'../data/raw/{i}star.csv') for i in range(1, 5+1)]
word_cnt_before = [sum(dfs[i]['0'].apply(lambda x:len(x.split()))) for i in range(5)]
word_cnt_before.append(sum(word_cnt_before))

dfs = [pd.read_csv(f'../data/clean/{i}star.csv') for i in range(1, 5+1)]
word_cnt_after = [sum(dfs[i]['0'].apply(lambda x:len(x.split()))) for i in range(5)]
word_cnt_after.append(sum(word_cnt_after))

output_file = open("../latex_report/tables/sizes_before_cleaning.csv", "w", encoding="utf-8")
output_file2 = open("../stats/sizes_before_cleaning.csv", "w", encoding="utf-8")
output_file.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد کلمات,{},{},{},{},{},{}".format(*word_cnt_before),
    "حجم فایل, {},{},{},{},{},{}".format(*file_sizes_before)
)))
output_file2.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد کلمات,{},{},{},{},{},{}".format(*word_cnt_before),
    "حجم فایل, {},{},{},{},{},{}".format(*file_sizes_before)
)))
output_file.close()
output_file2.close()

output_file = open("../latex_report/tables/sizes_after_cleaning.csv", "w", encoding="utf-8")
output_file2 = open("../stats/sizes_after_cleaning.csv", "w", encoding="utf-8")
output_file.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد کلمات,{},{},{},{},{},{}".format(*word_cnt_after),
    "حجم فایل, {},{},{},{},{},{}".format(*file_sizes_after)
)))
output_file2.write('\n'.join((
    ",۱ ستاره,۲ ستاره,۳ ستاره, ۴ ستاره, ۵ ستاره, همه‌ برچسب‌ها",
    "تعداد کلمات,{},{},{},{},{},{}".format(*word_cnt_after),
    "حجم فایل, {},{},{},{},{},{}".format(*file_sizes_after)
)))
output_file.close()
output_file2.close()