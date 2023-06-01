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

## How do I get the report?
The report is written in Persian and prepared using $\LaTeX$. If you run the above process and get new data and new stats then it will auto updated on the report once you run the `generate_report_pdf.bat` script
