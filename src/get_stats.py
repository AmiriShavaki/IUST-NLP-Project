import matplotlib.pyplot as plt

# Number of Comments
com_cnt = [len(open(f'../data/raw/{i}star.csv', encoding="utf-8").readlines()) - 1 for i in range(1, 5+1)]
labels = tuple(f'{i} star' for i in range(1, 5+1))
fig, ax = plt.subplots()
ax.pie(com_cnt, labels=labels, autopct='%1.1f%%', pctdistance=1.25, labeldistance=.6)
fig.savefig("../stats/com_cnt.png")