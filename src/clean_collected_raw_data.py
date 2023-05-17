from src import CLS_CNT
import pandas as pd
import os.path
import contractions
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from tqdm import tqdm
import emoji
import re

fix_contractions = lambda x: contractions.fix(x)
remove_digits = lambda x: "".join([i for i in x if not i.isdigit()])
remove_extra_spaces = lambda x: " ".join(x.split())
remove_punctuations = lambda x: re.sub("[^0-9A-Za-z .]", "", x)
remove_stopwords = lambda x: " ".join([i for i in x.split() if i not in stopwords.words("english")])
def replace_emojis(x):
    return emoji.replace_emoji(x, replace=lambda chars, data_dict: ' '.join(data_dict['en'].split('_')).strip(':'))

def cleaner(x):
    return remove_extra_spaces(remove_punctuations(remove_digits(fix_contractions(remove_stopwords(replace_emojis(x))))))

raw_data = [pd.read_csv(os.path.dirname(__file__) + f'/../data/raw/{i}star.csv') for i in range(1, 1 + CLS_CNT)]

cleaned_data = [df.applymap(cleaner) for df in tqdm(raw_data)]
for i in range(CLS_CNT):
    cleaned_data[i].to_csv(os.path.dirname(__file__) + f'/../data/clean/{i + 1}star.csv', index=False)