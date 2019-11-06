import os
import wget
import logging

def __ensure_directories():
    logging.info('Creating data directories')
    os.makedirs('data', exist_ok=True)
    os.makedirs('tmp', exist_ok=True)

def __download_data():
    if not os.path.exists('data/wordnet.is_a.txt'):
        logging.info('Downloading ImageNet relationships mapping...')
        wget.download('http://www.image-net.org/archive/wordnet.is_a.txt', 'data')

    if not os.path.exists('data/words.txt'):
        logging.info('Downloading ImageNet words mapping...')
        wget.download('http://www.image-net.org/archive/words.txt', 'data')


def bootstrap():
    __ensure_directories()
    __download_data()
