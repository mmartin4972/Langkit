import sqlite3
from string import punctuation

create_users_table = """CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username text NOT NULL, 
    password text NOT NULL
);"""

create_topics_table = """CREATE TABLE topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name text NOT NULL, 
    sourceLang text NOT NULL, 
    targetLang text NOT NULL, 
    user_id integer NOT NULL, 
    FOREIGN KEY (user_id) REFERENCES users (id)
);"""

create_pairs_table ="""CREATE TABLE pairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    source text NOT NULL, 
    translation text NOT NULL,
    topic_id integer NOT NULL,
    FOREIGN KEY (topic_id) REFERENCES topics (id)
);"""

insert_user = """INSERT INTO users (username, password) VALUES ('%s', '%s');"""

insert_topic = """INSERT INTO topics (name, sourceLang, targetLang, user_id) VALUES
    ('%s', '%s', '%s', (SELECT id FROM users WHERE username = '%s'));"""

delete_topic = """DELETE FROM topics WHERE name = '%s_%s';"""

insert_pair = """INSERT INTO pairs (source, translation, topic_id) VALUES
    ('%s', '%s', (SELECT id FROM topics WHERE name = '%s'));"""

select_topics = """SELECT name FROM topics WHERE 
    user_id = (SELECT id FROM users WHERE username = '%s');"""

select_topic = """SELECT * FROM pairs WHERE 
    topic_id = (SELECT id FROM topics WHERE name = '%s_%s');"""


class handler:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)

        self.cur = self.con.cursor()
        self.cur.execute("DROP TABLE IF EXISTS users")
        self.cur.execute("DROP TABLE IF EXISTS topics")
        self.cur.execute("DROP TABLE IF EXISTS pairs")
        self.cur.execute(create_users_table)
        self.cur.execute(create_topics_table)
        self.cur.execute(create_pairs_table)


    def add_user(self, username: str, password: str):
        self.cur.execute(insert_user % (username, password))
        print("Added user: %s with password: %s" % (username, password))

    
    def add_topic_to_user(self, username: str, topic_name: str, lang: tuple):
        self.cur.execute(insert_topic % (username + "_" + topic_name, lang[0], lang[1], username))
        print("Added topic: %s" % topic_name)


    def remove_topic_from_user(self, username: str, topic_name: str):
        self.cur.execute(delete_topic % (username, topic_name))
        print("Deleted Topic")


    def add_pair_to_topic(self, username: str, topic_name: str, pair: tuple):
        self.cur.execute(insert_pair % (pair[0], pair[1], username + "_" + topic_name))
        print("Added pair: ", pair)

    
    def get_topics(self, username: str):
        ret = self.cur.execute(select_topics % username)
        l = []
        for i in ret:
            l.append([t.strip(punctuation) for t in str(i).split('_')][1])
        return l


    def get_topic (self, username: str, topic_name: str):
        ret = self.cur.execute(select_topic % (username, topic_name))
        l = []
        for r in ret:
            l.append((r[1], r[2]))
        return l
