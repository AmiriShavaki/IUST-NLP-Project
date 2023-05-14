import os.path
f = open(os.path.dirname(__file__) + '/../data/raw/test.txt', 'w')
f.write("Just for the sake of testing")
f.close()