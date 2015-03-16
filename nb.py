#!/usr/bin/python3

import os
import sys
import traceback
import pdb
from functools import reduce
import operator
import math

class NBClass:
    def __init__(self, class_name):
        self.class_name = class_name
        self.words = {}
        self.total_words = 0

    def add_word(self, word, count = 1):
        self.words[word] = self.words.get(word, 0) + count
        self.total_words += count

    def add_document(self, document):
        for word in document:
            self.add_word(word)

    def does_exists(self, word):
        return word in self.words

    def get_document_prob(self, document, vocab_length):
        add_one_smoothing = False
        for word in document:
            if word not in self.words:
                add_one_smoothing = True
                break

        result = 0.0
        for word in document:
            tmp = self.get_word_prob(word, vocab_length, add_one_smoothing)     
            result += math.log(tmp)

        return result
        

    def get_word_prob(self, word, vocab_length, add_one_smoothing = False):
        result = 0
        if add_one_smoothing:
            result = self.words.get(word, 1)/(self.total_words + vocab_length)
        else:
            result = self.words.get(word, 0)/(self.total_words)

        return result

    def get_detail_str(self):
        result = 'class=%s\n'%(self.class_name)
        for word in self.words:
            result += '%s %d ' % (word, self.words[word])
        return result[:-1]
            
class NBClassifier:
    def __init__(self):
        self.class_count = {}
        self.vocabulary = set()
        self.class_struct = {}

    def add_class(self, class_name):
        if class_name not in self.class_struct:
            nb_class = NBClass(class_name)
            self.class_struct[class_name] = nb_class

    def get_class_prob(self, class_name):
        return math.log(self.class_count.get(class_name, 0) / sum(self.class_count.values()))

    def add_learned_data(self, class_name, document):
        for word in document.keys():
            self.vocabulary.add(word)

        if class_name not in self.class_struct:
            self.add_class(class_name)

        nbclass = self.class_struct[class_name]

        for word in document.keys():
            nbclass.add_word(word, document[word])

    def add_document(self, class_name, document):
        for word in document:
            self.vocabulary.add(word)
        
        if class_name not in self.class_struct:
            self.add_class(class_name)
            
        nbclass = self.class_struct[class_name]
        nbclass.add_document(document)     

        self.class_count[class_name] = self.class_count.get(class_name, 0) + 1

    def read_training_file(self, file_path):
        with open(file_path, encoding = "ISO-8859-1") as f:
            examples = f.readlines()
            for example in examples:
                example = example.strip()
                result = example.split()
                class_name = result[0]
                document = result[1:]
                self.add_document(class_name, document)

    def get_class_count_str(self):
        result = 'class_count\n'

        for class_name in self.class_count.keys():
            result += '%s=%d\n' % (class_name, self.class_count[class_name])

        result += 'end_class_count'
        return result

    def get_class_struct_str(self):
        result = 'class_struct\n'

        for class_name in self.class_struct:
            result += self.class_struct[class_name].get_detail_str()
            result += '\n'

        result += 'end_class_struct'
        return result

    def write_data_learned(self, file_name):
        with open(file_name, "w", encoding = "ISO-8859-1") as f:
            class_count_str = self.get_class_count_str()
            f.write(class_count_str)
            f.write("\n")

            class_struct_str = self.get_class_struct_str()
            f.write(class_struct_str)

    def read_data_learned(self, file_name):
        with open(file_name, encoding = "ISO-8859-1") as f:
            lines = [line.strip() for line in f.readlines()]
            
            line_count = 1
            while lines[line_count] != 'end_class_count':
                class_name, count = lines[line_count].split('=')
                self.class_count[class_name] = int(count)
                line_count += 1

            line_count += 1
            if lines[line_count] == 'class_struct':
                line_count += 1
                while lines[line_count] != 'end_class_struct':
                    class_name = lines[line_count].split('=')[1]
                    line_count += 1
                    word_count_list = lines[line_count].split(' ')

                    line_count += 1
                    index = 0
                    document = {}
                    while index < len(word_count_list):
                        word = word_count_list[index]
                        index += 1
                        count = int(word_count_list[index])
                        document[word] = count
                        index += 1

            
                    self.add_learned_data(class_name, document)



    def classify_document(self, document):
        final_class_name = None
        class_prob = {}
        for class_name in self.class_struct:
            nbclass = self.class_struct[class_name]
            nbclass_prob = self.get_class_prob(class_name)
            prob_doc_class = nbclass.get_document_prob(document, len(self.vocabulary))
            result = nbclass_prob + prob_doc_class
            class_prob[result] = class_name

        return class_prob[max(class_prob.keys())]
