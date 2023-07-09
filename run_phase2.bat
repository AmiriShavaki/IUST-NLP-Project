@REM Echo Starting run script of phase 2>run.log

:: You can uncomment two below lines and replace your desired virtual environment
call C:/ProgramData/Anaconda3/Scripts/activate
call conda activate cs224n
@REM Echo Virtual environment activated successfully>>run.log

:: Word2Vec
@REM cp data\sentencebroken\1star.csv src\word2vec\utils\datasets\1star.csv
@REM cp data\sentencebroken\2star.csv src\word2vec\utils\datasets\2star.csv
@REM cp data\sentencebroken\3star.csv src\word2vec\utils\datasets\3star.csv
@REM cp data\sentencebroken\4star.csv src\word2vec\utils\datasets\4star.csv
@REM cp data\sentencebroken\5star.csv src\word2vec\utils\datasets\5star.csv
@REM Echo Dataset files copied into working directory of the word2vec>>run.log
@REM Echo Starting to process 1star.csv>>run.log
@REM python -m src.word2vec.run --file 1star
@REM Echo Done!>>run.log
@REM Echo Starting to process 2star.csv>>run.log
@REM python -m src.word2vec.run --file 2star
@REM Echo Done!>>run.log
@REM Echo Starting to process 3star.csv>>run.log
@REM python -m src.word2vec.run --file 3star
@REM Echo Done!>>run.log
@REM Echo Starting to process 4star.csv>>run.log
@REM python -m src.word2vec.run --file 4star
@REM Echo Done!>>run.log
@REM Echo Starting to process 5star.csv>>run.log
@REM python -m src.word2vec.run --file 5star
@REM Echo Done!>>run.log
@REM Echo Starting to process all of the data at once>>run.log
@REM python -m src.word2vec.run --file all
@REM Echo Done!>>run.log
Echo Generating tables of word2vec>>run.log
python -m src.word2vec_load_query
Echo Saved in /latex_phase2_report/tables>>run.log

PAUSE