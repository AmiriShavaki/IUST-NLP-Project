:: You can uncomment two below lines and replace your desired virtual environment
:: call C:/ProgramData/Anaconda3/Scripts/activate
:: call conda activate cs224n
python -m src.collect_raw_data
python -m src.clean_collected_raw_data
python -m src.wordbreak_and_sentencebreak_cleaned_data
python -m src.total_data_size_before_after_cleaning
PAUSE