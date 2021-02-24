# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import sqlite3
from random import seed
from random import randint
from time import time



class RaidforumsPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def ceate_connection(self):
        self.conn = sqlite3.connect("raidforums_database.db")
        self.conn.execute("""PRAGMA foreign_keys = 1""")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists post_table""")
        self.curr.execute("""drop table if exists details_post""")
        self.curr.execute("""drop table if exists user_table""")
        self.curr.execute("""create table if exists details_tb(
                                            id text primary key ,
                                            link_to_post text,
                                            actual_post text
                                            )""")
        self.curr.execute("""create table if exists user_table(
                                            id text primary key,
                                            user_status text,
                                            user_posts smallint,
                                            user_threads smallint,
                                            user_joined text,
                                            user_reputation text,
                                            user_service text
                                            )""")
        self.curr.execute("""create table if not exists post_table(
                                            id text primary key,
                                            post_name text,
                                            post_by text,
                                            post_date text,
                                            post_views_no smallint,
                                            post_replies_no smallint,
                                            link_to_post text
                                            )""")

    def process_item(self, item, spider):
        # self.store_db(item)
        # self.close_db()
        return item

    def store_db(self,item):          #modifications required about foreign_keys and id generation
        self.curr.execute("""insert into details_tb values(?,?,?)""", (
            id,
            item['post_link'],
            item['actual_post']
        ))
        self.curr.execute("""insert into details_tb values(?,?,?,?,?,?,?)""", (
            id,
            item['user_status'],
            item['user_posts'],
            item['user_threads'],
            item['user_joined'],
            item['user_reputation'],
            item['user_service']
        ))
        self.curr.execute("""insert into post_table values(?,?,?,?,?,?,?)""",(
            id,
            item['post_name'],
            item['post_by'],
            item['post_date'],
            item['post_views_no'],
            item['post_replies_no'],
            item['link_to_post']
        ))
        self.conn.commit()


    def close_db(self):
        self.cur.close()
        self.con.close()
