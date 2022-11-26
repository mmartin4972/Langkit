import sqlite3
from string import punctuation


create_topics_table = """CREATE TABLE topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name text NOT NULL, 
    sourceLang text NOT NULL, 
    targetLang text NOT NULL
);"""

create_pairs_table ="""CREATE TABLE pairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    source text NOT NULL, 
    translation text NOT NULL,
    topic_id integer NOT NULL,
    FOREIGN KEY (topic_id) REFERENCES topics (id)
);"""

insert_topic = """INSERT INTO topics (name, sourceLang, targetLang) VALUES
    ('%s', '%s', '%s'));"""

delete_topic = """DELETE FROM topics WHERE name = '%s';"""

insert_pair = """INSERT INTO pairs (source, translation, topic_id) VALUES
    ('%s', '%s', (SELECT id FROM topics WHERE name = '%s'));"""

delete_pair = """DELETE FROM pairs WHERE topic_id = (SELECT if from topics WHERE name = '%s') AND source = '%s'"""

select_topics = """SELECT * FROM topics;"""

select_topic = """SELECT * FROM pairs WHERE 
    topic_id = (SELECT id FROM topics WHERE name = '%s');"""


class handler:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)

        self.cur = self.con.cursor()
        self.cur.execute("DROP TABLE IF EXISTS topics")
        self.cur.execute("DROP TABLE IF EXISTS pairs")
        self.cur.execute(create_topics_table)
        self.cur.execute(create_pairs_table)

    
    def add_topic(self, topic_name: str, lang: tuple):
        self.cur.execute(insert_topic % (topic_name, lang[0], lang[1]))


    def remove_topic(self, topic_name: str):
        self.cur.execute(delete_topic % (topic_name))


    def add_pair_to_topic(self, topic_name: str, pair: tuple):
        self.cur.execute(insert_pair % (pair[0], pair[1], topic_name))

    
    def remove_pair_from_topic(self, topic_name: str, pair: tuple):
        self.cur.execute(delete_pair % (topic_name, pair[0]))


    def get_topics(self):
        ret = self.cur.execute(select_topics)
        l = []
        for r in ret:
            l.append((r[0], r[1], r[2], r[3])), 
        return l


    def get_topic (self, topic_name: str):
        ret = self.cur.execute(select_topic % (topic_name))
        l = []
        for r in ret:
            l.append((r[0], r[1], r[2]))
        return l
