import psycopg2 as pg
from . import db


def __map_to_dict(row):
    return {
        'id': row[0],
        'gender':  row[1],
        'masterCategory':  row[2],
        'subCategory':  row[3],
        'articleType':  row[4],
        'baseColour':  row[5],
        'season':  row[6],
        'usage':  row[7],
        'displayName':  row[8],
    }


def __map_result_to_dicts(rows):
    return [__map_to_dict(row) for row in rows]


def find_images_by_category(category):
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                'SELECT * FROM products WHERE articleType = %s LIMIT 2000', (category,))

            return __map_result_to_dicts(cur.fetchall())


def find_random_products(limit=30):
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                'SELECT * FROM products TABLESAMPLE SYSTEM_ROWS(%s);', (limit,))

            return __map_result_to_dicts(cur.fetchall())
