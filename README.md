## How do I prepare an environment to run the project?
Simply using conda you can run `conda create --name <envname> --file requirements.txt` in the root directory of the project and then every dependency needed to run this project will be installed and ready for you!

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

### Generate report table of word2vec results
```
python -m srcword2vec_load_query
```
Then the result tables will be saved in `\latex_phase2_report\tables`

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

You can also use `run.bat` to run the whole of the above process

## How do I get the report of phase 1?
The report is written in Persian and prepared using $\LaTeX$. If you run the above process and get new data and new stats then it will auto updated on the report once you run the `generate_phase1_report_pdf.bat` script
