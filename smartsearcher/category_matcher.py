import pandas as pd

__REPLACE_MAP = {
    'Tshirts': 'tshirt',
    'Shirts': 'shirt',
    'Casual Shoes': 'shoes',
    'Watches': 'watch',
    'Sports Shoes': 'shoe',
    'Kurtas': 'shirt',
    'Tops': 'top',
    'Handbags': 'handbag',
    'Heels': 'shoes',
    'Sunglasses': 'sunglass',
    'Wallets': 'wallet',
    'Flip Flops': 'shoe',
    'Sandals': 'sandal',
    'Briefs': 'briefs',
    'Belts': 'belt',
    'Backpacks': 'backpack',
    'Socks': 'socks',
    'Formal Shoes': 'shoe',
    'Perfume and Body Mist': 'perfume',
    'Jeans': 'jean',
    'Shorts': 'shorts',
    'Trousers': 'trouser',
    'Flats': 'shoe',
    'Bra': 'bra',
    'Dresses': 'dress',
    'Sarees': 'saree',
    'Earrings': 'earring',
    'Deodorant': 'perfume',
    'Nail Polish': 'nail polish',
    'Lipstick': 'lipstick',
    'Track Pants': 'pant',
    'Clutches': 'purse',
    'Sweatshirts': 'sweatshirt',
    'Caps': 'cap',
    'Sweaters': 'sweater',
    'Ties': 'tie',
    'Jackets': 'jacket',
    'Innerwear Vests': 'vest',
    'Kurtis': 'shirt',
    'Tunics': 'tunic',
    'Nightdress': 'nightdress',
    'Leggings': 'legging',
    'Pendant': 'pendant',
    'Capris': 'capri',
    'Necklace and Chains': 'necklace',
    'Lip Gloss': 'lipstick',
    'Night suits': 'dress',
    'Trunk': 'trunks',
    'Skirts': 'skirt',
    'Scarves': 'scarf',
    'Ring': 'ring',
    'Dupatta': 'scarf',
    'Accessory Gift Set': 'gift',
    'Cufflinks': 'cufflink',
    'Kajal and Eyeliner': 'eyeliner'
}

__CATEGORIES = set(__REPLACE_MAP.values())


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
