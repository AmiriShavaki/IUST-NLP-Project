import sentencepiece as spm

VOCAB_SIZES = (50, 800, 5000, 15000)

for vocab_size in VOCAB_SIZES:
    for part in range(1, 5+1):
        for i in range(1, 5+1):
            spm.SentencePieceTrainer.Train(
                input=f"src/tokenization/data{part}.txt",
                model_prefix=f"{vocab_size}_{part}_{i}",
                vocab_size=vocab_size,
                character_coverage=0.98
            )