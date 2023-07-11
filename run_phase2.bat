@echo off
SetLocal

Echo Starting run script of phase 2>run.log

:: You can uncomment two below lines and replace your desired virtual environment
call C:/ProgramData/Anaconda3/Scripts/activate
call conda activate cs224n
Echo Virtual environment activated successfully>>run.log

:: Word2Vec
cp data\sentencebroken\1star.csv src\word2vec\utils\datasets\1star.csv
cp data\sentencebroken\2star.csv src\word2vec\utils\datasets\2star.csv
cp data\sentencebroken\3star.csv src\word2vec\utils\datasets\3star.csv
cp data\sentencebroken\4star.csv src\word2vec\utils\datasets\4star.csv
cp data\sentencebroken\5star.csv src\word2vec\utils\datasets\5star.csv
Echo Dataset files copied into working directory of the word2vec>>run.log
Echo Starting to process 1star.csv>>run.log
python -m src.word2vec.run --file 1star
Echo Done!>>run.log
Echo Starting to process 2star.csv>>run.log
python -m src.word2vec.run --file 2star
Echo Done!>>run.log
Echo Starting to process 3star.csv>>run.log
python -m src.word2vec.run --file 3star
Echo Done!>>run.log
Echo Starting to process 4star.csv>>run.log
python -m src.word2vec.run --file 4star
Echo Done!>>run.log
Echo Starting to process 5star.csv>>run.log
python -m src.word2vec.run --file 5star
Echo Done!>>run.log
Echo Starting to process all of the data at once>>run.log
python -m src.word2vec.run --file all
Echo Done!>>run.log
Echo Generating tables of word2vec>>run.log
python -m src.word2vec_load_query
Echo Saved in /latex_phase2_report/tables>>run.log

:: Tokenization
Echo Spliting Dataset into five parts>>run.log
python -m src.tokenization.split_into_parts
Echo Tokenizing each part five times with different voab sizes>>run.log
python -m src.tokenization.tokenize
Echo Moving generated files to experiments directory>>run.log
set TOKENSIZE=50 800 5000 15000
set PART=1 2 3 4 5
set I=1 2 3 4 5
FOR %%t in (%TOKENSIZE%) DO (
  FOR %%p in (%PART%) DO (
    FOR %%i in (%I%) DO (
      move %%t_%%p_%%i.model experiments\tokenization\%%t_%%p_%%i.model
      move %%t_%%p_%%i.vocab experiments\tokenization\%%t_%%p_%%i.vocab
    )
  )
)

PAUSE