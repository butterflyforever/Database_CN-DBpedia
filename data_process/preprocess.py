# -*- coding: utf-8 -*-
import json

PATH = "/home/liyang/project/database/"
OUTPUT_DIR = PATH + "record.txt"
OUTPUT_FILENAME = PATH + "baike_json.json"
SRC_FILENAME = PATH + "data/baike_triples.txt"

def count(SRC_FILENAME):
    rel_dic = dict()
    with open(SRC_FILENAME, "r", encoding = 'utf-8') as f:
        for line in f:
            split = line.split('\t')
            rel = split[1]
            if rel in rel_dic:
                rel_dic[rel] += 1
            else:
                rel_dic[rel] = 1
    print(f"############")
    


def tuple2json(triples_filename):
    def __tuple2pair(line):
        split = line.split('\t')
        return [split[0], split[1:]]

    js = dict()
    with open(triples_filename, "r", encoding='utf-8') as f:
        with open(OUTPUT_DIR, "w", encoding="utf-8") as output:
            for ind, (key, entity) in enumerate(map(__tuple2pair, f)):
                if key in js:
                    js[key].append(entity)
                else:
                    print(key, file=output)
                    js[key] = [entity]
                if ind % 1000000 == 0:
                    print('>>>',ind)
    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(js, f)


def test_tuple2json():
    tuple2json(SRC_FILENAME)


def verify():
    with json.load(OUTPUT_FILENAME) as js:
        for ind, key in enumerate(js):
            print(key, js[key])
            if ind > 100:
                break
            

if __name__ == "__main__":
    test_tuple2json()
    # verify()
