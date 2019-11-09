import psycopg2 as pg

__connection = None

def get_connection():
    global __connection
    if not __connection:
        __connection = pg.connect('')

    return __connection



