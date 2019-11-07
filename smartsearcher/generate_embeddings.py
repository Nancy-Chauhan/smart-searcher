import os
import sys
import logging

from .embeddings import get_embedding
from tqdm import tqdm

logger = logging.getLogger('generate_embeddings')

__SUPPORTED_EXTS = set(['.jpg', '.gif', '.png', '.jpeg'])


def __file_supported(f):
    _, ext = os.path.splitext(f)
    return ext.lower() in __SUPPORTED_EXTS


def __preprocess_directory(directory):
    for root, _, files in os.walk(directory):
        logger.info('Processing directory: %s', root)
        for f in tqdm(files):
            if not __file_supported(f):
                continue

            file = os.path.join(root, f)

            get_embedding(file)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        __preprocess_directory(sys.argv[1])
    except KeyboardInterrupt:
        logger.info("Received Ctrl + C. Exiting...")
