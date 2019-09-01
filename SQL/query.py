# -*- coding: utf-8 -*-
from contextlib import closing
import mysql.connector as connector
from apis import api_ment2ent, api_avpair, api_value

config = {
    "user":"liyang",
    "password": "1239233008",
    "database": "db_project",
    "host":'localhost',
    "auth_plugin":'mysql_native_password',
    "raise_on_warnings": True
}

cnx = connector.connect(**config)


def query_ment2ent(mention):
    query = (
        """SELECT entity FROM m2e WHERE mention=%s"""
    )
    with closing(cnx.cursor()) as cur:
        cur.execute(query, (mention,))
        res = [entity for (entity,) in cur]

    if len(res) > 0:
        return re
    # if result is empty, use the api for update
    try:
        entities=api_ment2ent(mention)
    except Exception as e:
        return list()
    return entities


def query_ent2relation_entity2(entity):
    query = (
        """SELECT relation, entity2 FROM baike WHERE entity1 = %s"""
    )
    with closing(cnx.cursor()) as cur:
        cur.execute(query, (entity,))
        res = [(relation,entity2) for (relation, entity2) in cur]
    if len(res) > 0:
        return res
    # if the result is empty, use the api for update
    try:
        res = api_avpair(entity)
    except Exception as e:
        return list()
    return res


def query_ent_rela2entity(entity, relation):
    query = (
        """SELECT entity2 FROM baike WHERE entity1=%s AND relation=%s"""
    )
    with closing(cnx.cursor()) as cur:
        cur.execute(query, (entity, relation))
        res = [ent for ent in cur]
    if len(res) > 0:
        return res

    try:
        res = api_value(entity, relation)
    except Exception as e:
        return list()
    return res


def query_api_ent_ent2rela(ent1, ent2):
    query = (
        """
            with men1ent(entity) as (
                select entity from m2e where mention=%s
            ), men2ent(entity) as (
                select entity from m2e where mention=%s
            ) select relation from baike where entity1 in men1ent and entity2 in men2ent or entity1 in men2ent and entity2 in men1ent
        """
    )
    with closing(cnx.cursor()) as cur:
        cur.execute(query, (ent1, ent2))
        res = [rela for rela in cur]
    return res


if __name__ == "__main__":
    result = query_relation_entity2("中华人民共和国")