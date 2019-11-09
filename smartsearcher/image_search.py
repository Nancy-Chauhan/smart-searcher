import psycopg2 as pg
from psycopg2.extras import RealDictCursor
from . import db
from . import embeddings

import itertools
import sys

from sklearn.metrics.pairwise import cosine_similarity


def find_matching_images(query_image, category, limit=30):
    images = __find_images_by_category(category)

    matches = itertools.islice(
        __rank_images_by_similarity(query_image, images), limit)

    return [{'image': match[0], 'similarity': float(match[1])} for match in matches]


def __find_images_by_category(category):
    with db.get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                'SELECT * FROM products WHERE articleType = %s', (category,))

            return cur.fetchall()


def __file_path(img_id):
    return f'data/images/{img_id}.jpg'


def __rank_images_by_similarity(query_image, images):
    query_vector = embeddings.get_embedding(query_image, cached=False)
    image_vectors = [embeddings.get_embedding(__file_path(img['id'])) for img in images]

    similarity = cosine_similarity([query_vector], image_vectors)

    return reversed(sorted(zip(images, similarity[0]), key=lambda x: x[1]))


if __name__ == "__main__":
    img = sys.argv[2]
    cat = sys.argv[1]

    print(find_matching_images(img, cat))
