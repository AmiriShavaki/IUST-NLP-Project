import nltk.data
from wordsegment import load, segment
from src import CLS_CNT
import os.path
import pandas as pd
from tqdm import tqdm

sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
load() # Word Tokenizer

for i in tqdm(range(1, CLS_CNT+1)):
    cleaned_df = pd.read_csv(os.path.dirname(__file__) + f'/../data/clean/{i}star.csv')

    sentence_broken_res = []
    word_broken_res = []
    for ind, row in cleaned_df.iterrows():
        sentence_broken_row = sentence_tokenizer.tokenize(row[0])
        word_broken_row = segment(row[0])

        sentence_broken_res.append(sentence_broken_row)
        word_broken_res.append(word_broken_row)

    sentence_broken_df = pd.DataFrame(sentence_broken_res)
    word_broken_df = pd.DataFrame(word_broken_res)

    sentence_broken_df.to_csv(os.path.dirname(__file__) + f'/../data/sentencebroken/{i}star.csv', index=False)
    word_broken_df.to_csv(os.path.dirname(__file__) + f'/../data/wordbroken/{i}star.csv', index=False)