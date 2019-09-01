# -*- coding:utf-8 -*-
import requests

apikey = "9f555f45abe1f9e3cb73de13038369"

def api_entities_identify(query):
    params = {"q": query, "apikey": apikey}
    url = "http://shuyantech.com/api/entitylinking/cutsegment"
    with requests.get(url, params=params) as r:
        json = r.json()
        cuts, entities = json["cuts"], json["entities"]
        return cuts, [entity for status, entity in entities]


def api_ment2ent(query):
    url = "http://shuyantech.com/api/cndbpedia/ment2ent"
    params = {"q": query, "apikey": apikey}
    with requests.get(url, params=params) as r:
        json = r.json()
        if json["status"] == "ok":
            return json["ret"]
    return list()


def api_avpair(query):
    url = "http://shuyantech.com/api/cndbpedia/avpair"
    params = {"q": query, "apikey": apikey}
    with requests.get(url, params=params) as r:
        json = r.json()
        if json["status"] == "ok":
            return [(i,j) for (i,j) in json["ret"]]
    return list()


def api_value(ent, rela):
    url = "http://shuyantech.com/api/cndbpedia/value"
    params = {"q": ent, "attr":rela, "apikey": apikey}
    with requests.get(url, params=params) as r:
        json = r.json()
        if json["status"] == "ok":
            return json["ret"]
    return list()


# tests

def test_api_entities_identify():
    while True:
        query = input(">")
        cuts, entities = api_entities_identify(query)
        for cut in cuts:
            print(cut, end=' ')
        print(end='\n\n')
        for entity in entities:
            print(entity, end=' ')
        print()


def test_api_ment2ment():
    while True:
        query = input(">")
        entities = api_ment2ent(query)
        for entity in entities:
            print(entity, end=' ')
        print()


def test_api_avpair():
    while True:
        query = input(">")
        properties = api_avpair(query)
        for key, val in properties:
            print('\t', val, key, sep='-@-')
        print()


def test_api_value():
    while True:
        ent = input("entity >")
        rela = input("relation >")
        values = api_value(ent, rela)
        for val in values:
            print(val, end=' ')
        print()


if __name__ == "__main__":
    test_api_entities_identify()
    #test_api_ment2ment()
    #test_api_avpair()
