import json
import os
import sqlite3


def load_json_to_sqlite(json_path, db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # 读取 JSON 文件
    with open(json_path, 'r', encoding='utf-8') as file:
        poems = json.load(file)
        for poem in poems:
            # 提取数据，处理多段落文本
            paragraphs = '\n'.join(poem['paragraphs'])
            notes = '\n'.join(poem.get('note', []))  # 处理不存在的情况
            # 插入数据
            c.execute('''
                INSERT INTO poems (author, title, paragraphs, notes)
                VALUES (?, ?, ?, ?)
            ''', (poem['author'], poem['title'], paragraphs, notes))
    conn.commit()
    conn.close()

# 加载 JSON 数据到 SQLite
def load_all_jsons(directory, db_path):
    for filename in os.listdir(directory):
        if filename.startswith('poet.tang.') or filename.startswith('poet.song.'):
            json_path = os.path.join(directory, filename)
            load_json_to_sqlite(json_path, db_path)

# 调用函数处理整个目录
load_all_jsons('../全唐诗/', 'poetry.db')
