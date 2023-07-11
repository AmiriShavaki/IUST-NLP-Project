## How do I prepare an environment to run the project?
Simply using conda you can run `conda create --name <envname> --file requirements.txt` in the root directory of the project and then every dependency needed to run this project will be installed and ready for you!

## How do I get the report?
The report is written in Persian and prepared using $\LaTeX$. If you run the above process and get new data and new stats then it will auto updated on the report once you run the `generate_phase1_report_pdf.bat` and `generate_phase2_report_pdf.bat` scripts.

# Phase 2

### Train word2vec model on a specific class or the whole dataset
```
cp data\sentencebroken\Xstar.csv src\word2vec\utils\datasets\Xstar.csv
python -m src.word2vec.run --file Xstar
```
or
```
cp data\sentencebroken\1star.csv src\word2vec\utils\datasets\1star.csv
cp data\sentencebroken\2star.csv src\word2vec\utils\datasets\2star.csv
cp data\sentencebroken\3star.csv src\word2vec\utils\datasets\3star.csv
cp data\sentencebroken\4star.csv src\word2vec\utils\datasets\4star.csv
cp data\sentencebroken\5star.csv src\word2vec\utils\datasets\5star.csv
python -m src.word2vec.run --file all
```
Then the result model will be saved in `models/Xstar.word2vec.npy` or `models/all.word2vec.npy`

### Generate report tables of word2vec results
```
python -m src.word2vec_load_query
```
Then the result tables will be saved in `\latex_phase2_report\tables`

### Spliting dataset into 5 parts (Each part is the whole dataset except for a specific class)
```
python -m src.tokenization.split_into_parts
```

### Train Tokenizer model on each part and store result models separately then move them to experiments folder
```
python -m src.tokenization.tokenize
set TOKENSIZE=50 800 5000 15000
set PART=1 2 3 4 5
FOR %%t in (%TOKENSIZE%) DO (
  FOR %%p in (%PART%) DO (
    move %%t_%%p.model experiments\tokenization\%%t_%%p.model
    move %%t_%%p.vocab experiments\tokenization\%%t_%%p.vocab
  )
)
```

### Evaluating models based on UNK percentage and then store statistics in csv tables in `\latex_phase2_report\Tables`
```
FOR %%p in (%PART%) DO (
  python -m src.tokenization.count_UNK --part %%p
)
```

### Move best trained model to the `models` directory
```
move experiments\tokenization\50_3.model models\Tokenizer.model
```

You can also use `run_phase2.bat` to run the whole of the above process

# Phase 1
[Link to the collected dataset on huggingface](https://huggingface.co/datasets/Amiri/Google-Play-Reviews-for-Sentiment-Analysis/tree/main)

### Collecting raw data from google play
```
python -m src.collect_raw_data.py
```

### Cleaning the collected data
```
python -m src.clean_collected_raw_data.py
```

### Breaking the cleaned data into sentences and words
```
python -m src.wordbreak_and_sentencebreak_cleaned_data.py
```

### Getting the total size of data before and after cleaning
```
python -m src.total_data_size_before_after_cleaning.py
```

### Getting other statistics tables and plots
```
python -m src.get_stats.py
```

You can also use `run_phase1.bat` to run the whole of the above process
