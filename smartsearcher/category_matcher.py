import pandas as pd

__CATEGORIES = set([
    'tshirt', 'shirt', 'shoes', 'watch', 'top', 'handbag', 'sunglass',
    'wallet', 'sandal', 'briefs', 'belt', 'backpack', 'socks', 'perfume', 'jean',
    'shorts', 'trouser', 'bra', 'dress', 'saree', 'earring', 'perfume', 'nail polish',
    'lipstick', 'pant', 'purse', 'sweatshirt', 'cap', 'sweater', 'tie', 'jacket',
    'vest', 'tunic', 'nightdress', 'legging', 'pendant', 'capri', 'necklace',
    'lipstick', 'dress', 'trunks', 'skirt', 'scarf', 'ring', 'scarf', 'gift',
    'cufflink', 'eyeliner'
])


def find_category(predictions):
    category_1, score_1 = __match_score(predictions[0]['categories'])
    category_2, score_2 = __match_score(predictions[1]['categories'])

    return {
        'category': category_1,
        'name': predictions[0]['name'].replace('_', ' ')
    } if score_1 < score_2 else {
        'category': category_2,
        'name': predictions[1]['name'].replace('_', ' ')}


def __match_score(synonym_set):
    for i, words in enumerate(synonym_set):
        for word in words:
            if word in __CATEGORIES:
                return word, i

    return None, 99999
