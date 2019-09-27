import sqlite3

db = sqlite3.connect('db.sqlite3')

c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS `users` ('
          'username varchar(32) NOT NULL UNIQUE, '
          'passhash varchar(64) NOT NULL, '
          'status char(1) NOT NULL, '
          'isactive BOOLEAN NOT NULL'
          ')'
          )  # statuses: {'g': 'guardian', 'a': 'admin', 'u': 'user'}

c.execute('INSERT INTO users (username, passhash, status, isactive) '
          'VALUES ("admin", "kek", "a", 1),'
          '("guardian", "kek", "g", 1)')

db.commit()
