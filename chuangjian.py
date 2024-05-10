import sqlite3

def create_database(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # 创建表
    c.execute('''
        CREATE TABLE IF NOT EXISTS poems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            title TEXT,
            paragraphs TEXT,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 调用函数创建数据库和表
create_database('poetry.db')
