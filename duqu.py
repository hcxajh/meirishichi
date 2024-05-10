import sqlite3
import opencc
converter = opencc.OpenCC('t2s')

def paginate_poems(page_number, page_size):
    # 计算从哪一条记录开始
    offset = (page_number - 1) * page_size

    # 连接到数据库
    conn = sqlite3.connect('poetry.db')
    cursor = conn.cursor()

    # 执行带分页的查询
    cursor.execute('SELECT author, title FROM poems LIMIT ? OFFSET ?', (page_size, offset))

    # 获取查询结果
    rows = cursor.fetchall()
    for row in rows:
        formatted_str = f"Author: {row[0]}, Title: {row[1]}"
        converted_str = converter.convert(formatted_str)

        print(converted_str)

        # 关闭 Cursor 和连接
    cursor.close()
    conn.close()


# 测试函数，获取第1页的数据，每页10条
paginate_poems(1, 10)