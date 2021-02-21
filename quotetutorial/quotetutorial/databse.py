import sqlite3

conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

curr.execute("""create table quotes_tb(
title text
)""")
