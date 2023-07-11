import argparse
import sentencepiece as spm

def UNK_percentage(part, vocabsize):
    sp = spm.SentencePieceProcessor()
    sp.load(f'experiments/tokenization/{vocabsize}_{part}.model')
    total = unk = 0
    test_data = open(f"data/sentencebroken/{part}star.csv")
    for line in test_data.readlines()[1:]:
        sentences = line.split(',')
        for sentence in sentences:
            if len(sentence) > 1:
                ids = sp.EncodeAsIds(sentence)
                total += len(ids)
                unk += sum(id == 0 for id in ids)
    return unk / total * 100

parser = argparse.ArgumentParser()
parser.add_argument("--part")
args = parser.parse_args()

VOCAB_SIZES = (50, 800, 5000, 15000)

first_row = [""] * 5
second_row = [""] * 5
second_row[0] = "UNK percentage"
for i, key in enumerate(VOCAB_SIZES, start=1):
    first_row[i] = "vocabsize={}".format(key)
    second_row[i] = "\\lr{{{:.2f}}}".format(UNK_percentage(args.part, key))
csv_content = "\n".join((",".join(first_row), ",".join(second_row)))
output_file = open(f"latex_phase2_report/tables/count_UNK{args.part}.csv".format(), "w", encoding="utf-8")
output_file.write(csv_content)
output_file.close()