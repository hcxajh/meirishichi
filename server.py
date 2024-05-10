import sqlite3
import random
from jinja2 import Environment, FileSystemLoader


def get_poems(page, page_size):
    offset = (page - 1) * page_size
    conn = sqlite3.connect('poetry.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT author, title, paragraphs FROM poems LIMIT ? OFFSET ?", (page_size, offset))
    poems = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return poems


random_page = random.randint(1, 10)


def generate_html_files():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('muban.htm')
    # 模拟的页面渲染过程
    for page in range(1, 11):
        poems = get_poems(page, 1)  # 假设每页10首诗
        rendered = template.render(page_number=page, poems=poems, total_pages=10, random_page=random_page)
        with open(f'{page}.html', 'w', encoding='utf-8') as file:
            file.write(rendered)


generate_html_files()
