for omit_ind in range(1, 5+1):
    res_file = open(f"src/tokenization/data{omit_ind}.txt", 'w')
    for i in range(1, 5+1):
        if i == omit_ind:
            continue
        class_file = open(f"data/sentencebroken/{i}star.csv")
        first = True
        for line in class_file.readlines():
            if first:
                first = False
                continue
            sentences = line.split(',')
            for sentence in sentences:
                if len(sentence) > 1:
                    res_file.write(sentence)
                    res_file.write('\n')
    res_file.close()