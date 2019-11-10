from . import embeddings
from . import repository

import itertools
import sys

from sklearn.metrics.pairwise import cosine_similarity

import logging
import uuid

log = logging.getLogger(__name__)

def find_matching_images(query_image, category, req_id=str(uuid.uuid4()), limit=30):
    images = repository.find_images_by_category(category)

    matches = itertools.islice(
        __rank_images_by_similarity(query_image, images, req_id), limit)

    return [{'image': match[0], 'similarity': float(match[1])} for match in matches]


def __file_path(img_id):
    return f'data/images/{img_id}.jpg'


def __rank_images_by_similarity(query_image, images, req_id=str(uuid.uuid4())):

    if len(images) == 0:
        return []

    log.debug('%s Generating embeddings', req_id)
    query_vector = embeddings.get_embedding(query_image, cached=False)

    log.debug("%s Matching against %d", req_id, len(images))
    image_vectors = [embeddings.get_embedding(__file_path(img['id'])) for img in images]

    log.debug('%s Finding similar images', req_id)
    similarity = 1 - cosine_similarity([query_vector], image_vectors)

    return sorted(zip(images, similarity[0]), key=lambda x: x[1])


if __name__ == "__main__":
    img = sys.argv[2]
    cat = sys.argv[1]

    print(find_matching_images(img, cat))
