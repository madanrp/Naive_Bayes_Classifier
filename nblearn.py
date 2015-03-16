from nb import NBClassifier
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print('nblearn.py TRANINGFILE MODELFILE')
        sys.exit(2)

    traning_file = args[1]
    model_file = args[2]

    nb_classifier = NBClassifier()

    nb_classifier.read_training_file(traning_file)

    nb_classifier.write_data_learned(model_file)
