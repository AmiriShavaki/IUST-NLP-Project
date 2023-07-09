import pandas as pd
from functools import reduce
import numpy as np
from .word2vec.utils.treebank import StanfordSentiment

cos_sim = lambda x, y: np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

logfile = open("logs/word2vec_load_query.log", 'a')
logfile.write("Generating tables of word2vec\n")

dfs = [pd.read_csv(f'data/clean/{i}star.csv') for i in range(1, 5+1)]
word_sets = [dfs[i]['0'].apply(lambda x:set(x.split())) for i in range(5)]
unq_words = [reduce(set.union, word_sets[i].tolist()) for i in range(5)]

com_words = dict()
sim_vecs = dict()
for i in range(1, 5+1): # Label1: i star
    class1 = f"{i}star"
    model1 = np.load(f"models/{class1}.word2vec.npy")
    dataset1 = StanfordSentiment()
    tokens1 = dataset1.tokens(f"{i}star")
    for j in range(i+1, 5+1): # Label2: j star
        class2 = f"{j}star"
        model2 = np.load(f"models/{class2}.word2vec.npy")
        dataset2 = StanfordSentiment()
        tokens2 = dataset2.tokens(f"{j}star")

        com_words[(i, j)] = unq_words[i - 1].intersection(unq_words[j - 1])
        sim_vecs[(i, j)] = dict()
        for word in com_words[(i, j)]:
            word = word.lower().replace('.', '')
            if word == '':
                continue
            word_ind1 = tokens1[word]
            word_ind2 = tokens2[word]
            sim_vecs[(i, j)][word] = cos_sim(model1[word_ind1], model2[word_ind2])

# sort based on cosine similarity and find max/min similarity of the pairs
max_sim_vecs = dict()
min_sim_vecs = dict()
for i in range(1, 5 + 1):
    for j in range(i + 1, 5 + 1):
        max_sim_vecs[(i, j)] = max(sim_vecs[(i, j)].items(), key=lambda x:x[1])
        min_sim_vecs[(i, j)] = min(sim_vecs[(i, j)].items(), key=lambda x:x[1])
        logfile.write(f"Highest value of pair ({i}, {j}): {max_sim_vecs[(i, j)]}\n")
        logfile.write(f"Lowest value of pair ({i}, {j}): {min_sim_vecs[(i, j)]}\n")

# Max Similarity File
first_row = [""] * 11
second_row = [""] * 11
third_row = [""] * 11
second_row[0] = "کلمه"
third_row[0] = "شباهت"
for i, key in enumerate(max_sim_vecs, start=1):
    first_row[i] = "{}ستاره و {}ستاره".format(*key)
    second_row[i] = str(max_sim_vecs[key][0])
    third_row[i] = str("{:.2f}".format(max_sim_vecs[key][1]))
csv_content = "\n".join((",".join(first_row), ",".join(second_row), ",".join(third_row)))
output_file = open("latex_phase2_report/tables/word2vec_max_com_sim.csv", "w", encoding="utf-8")
output_file.write(csv_content)
output_file.close()

# Min Similarity File
first_row = [""] * 11
second_row = [""] * 11
third_row = [""] * 11
second_row[0] = "کلمه"
third_row[0] = "شباهت"
for i, key in enumerate(min_sim_vecs, start=1):
    first_row[i] = "{}ستاره و {}ستاره".format(*key)
    second_row[i] = str(min_sim_vecs[key][0])
    third_row[i] = str("{:.2f}".format(min_sim_vecs[key][1]))
csv_content = "\n".join((",".join(first_row), ",".join(second_row), ",".join(third_row)))
output_file = open("latex_phase2_report/tables/word2vec_min_com_sim.csv", "w", encoding="utf-8")
output_file.write(csv_content)
output_file.close()

logfile.close()