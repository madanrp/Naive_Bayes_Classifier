from nb import NBClassifier
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print('nblearn.py MODELFILE TESTFILE')
        sys.exit(2)

    model_file = args[1]
    test_file = args[2]

    nb_classifier = NBClassifier()
    nb_classifier.read_data_learned(model_file) 

    with open(test_file, encoding = "ISO-8859-1") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            document = line.split()
            class_name = nb_classifier.classify_document(document) 
            print(class_name)
