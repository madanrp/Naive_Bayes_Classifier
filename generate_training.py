import sys
import getopt
from os import listdir
from os.path import isfile, join
import traceback

def get_options(argv):
    directory = ''
    class_type = ''
    #if 0 train data, 1 test data
    train_test = 0
    try:
        opts, args = getopt.getopt(argv, "hd:t:s:", ["directory=", "type=", "subtype="])
    except getopt.GetoptError as e:
        print(e)
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print('generate_training.py -d directory -t class_type')
            sys.exit()
        elif opt in ("-d", "--directory"):
            directory = arg
        elif opt in ("-t", "--type"):
            class_type = arg
        elif opt in ("-s", "--subtype"):
            train_test = int(arg)

    return [directory, class_type, train_test]

def list_files(directory):
    files = [ f for f in listdir(directory) if isfile(join(directory,f)) ]
    files = sorted(files)
    return files

def extract_file_class(file_name):
    file_class = file_name.split('.')[0]
    return file_class

def extract_words(file_path):
    with open(file_path, "r", encoding = "ISO-8859-1") as f:
        try:
            data = f.read()
        except:
            print(file_path)
            traceback.print_exc(file=sys.stdout)
            return []
        words = data.split()
        return words

def process_files(directory, class_type, train_test):
    file_list = list_files(directory)
    output_file_name = "%s_training.txt" % class_type
    class_name = []
    with open(output_file_name, "w") as f:
        for each_file in file_list:
            file_class = extract_file_class(each_file)
            file_path = directory + "/" + each_file
            words = extract_words(file_path)
            output_list = [file_class]
            if train_test == 1:
                output_list = []
            class_name.append(file_class)
            #output_list = []
            output_list.extend(words)
            output = ' '.join(output_list)
            f.write(output)
            f.write("\n")
    return class_name

if __name__ == "__main__":
    directory, class_type, train_test = get_options(sys.argv[1:])
    class_name = process_files(directory, class_type, train_test)
    if train_test == 1:
        with open("%s_class_name"%class_type, "w") as f:
            for name in class_name:
                f.write(name + "\n")
