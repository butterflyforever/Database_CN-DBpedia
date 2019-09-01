#coding=utf-8

import sys 
PATH = "/Users/liyang/Desktop/Course/Database/Project/code/SQL/"
sys.path.append(PATH)
import mysql.connector as connector

from query import *
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost', port=9876, lang = 'zh')


#sentence = f"中国的首都在哪里?"

def analysis(sentence):
	
	#print(nlp.word_tokenize(sentence))
	tag = nlp.pos_tag(sentence)
	print(tag)

	ner = nlp.ner(sentence)
	print(ner)

	# find all NN/NR which is not Entity
	tag_nn_nr = []
	for index, word in enumerate(tag):
		if word[1] == 'NN' or word[1] == 'NR':
			if ner[index][1] == 'O':
				tag_nn_nr.append(word)

	print(tag_nn_nr)
	# find all entity
	entities = []
	entity = ''
	attribute = ''
	for index, word in enumerate(ner):
		if word[1] == 'O':
			if entity != '':
				entities.append((entity,attribute))
			entity = ''
			attribute = ''
		else:
			entity = entity + word[0]
			attribute = word[1]

	print(entities)
	#return [tag_nn_nr,entities]

	if len(entities) + len(tag_nn_nr) <= 2:
		result = []
		result_tmp = entities + tag_nn_nr
		for word in result_tmp:
			result.append(word[0])
		return result
	
	result = []
	result_str = []
	# >= 2 entities
	if len(entities) >= 2:
		result = entities[0:2]

	# 1 entity + 1 NN/NR
	elif len(entities) == 1:
		tmp = tag_nn_nr[0]
		for word in tag_nn_nr:
			if word[1] == "NR":
				tmp = word
			break
		result = [entities[0],tmp]

	# 2 NN/NR
	else:
		#first loop: add NR untill len(result)>=2
		for word in tag_nn_nr:
			if len(result) == 2:
				break
			if word[1] == "NR":
				result.append(word)

		#second loop: add NN to make result have at least 1 noun
		for word in tag_nn_nr:
			if len(result) != 0:
				break
			if word[1] == "NN":
				result.append(word)

	for word in result:
		result_str.append(word[0])
	#return result_str
	print("#####")

	#print(query_api_ent_ent2rela(result_str[0],result_str[1]))

	return result_str

	#print(nlp.parse(sentence))
	#print(nlp.dependency_parse(sentence))

if __name__ == '__main__':
	
	print("parsing:")

	sentence = ''
	while True:
		sentence = input("input:").strip()
		if sentence == '':
			break
		analysis(sentence)
	
	print("end")

