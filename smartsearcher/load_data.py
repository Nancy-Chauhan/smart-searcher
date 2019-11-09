import pandas as pd
import sys
import io
from . import db

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


def __import_file(file):

    data = pd.read_csv(file)
    data.articleType.replace(__REPLACE_MAP, inplace=True)

    data = data[data.articleType.isin(__REPLACE_MAP.values())][:]
    data.drop(columns=['year'], inplace=True)

    data['description'] = data.baseColour + ' ' + \
        data.usage + ' ' + data.productDisplayName

    with db.get_connection() as conn:
        with conn.cursor() as cur:
            output = io.StringIO()
            data.to_csv(output, sep='\t', header=False, index=False)
            output.seek(0)
            contents = output.getvalue()
            cur.copy_from(output, 'products',  null="")  # null values become ''
            conn.commit()


def __migrate():
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                '''
                DROP TABLE IF EXISTS products;
                CREATE TABLE products (
                    id bigint,
                    gender varchar(32),
                    masterCategory varchar(255),
                    subCategory varchar(255),
                    articleType	varchar(255),
                    baseColour varchar(255),
                    season varchar(16),
                    usage varchar(32),
                    productDisplayName varchar(255),
                    searchDescription varchar(255)
                    );
                '''
            )
            cur.execute('CREATE EXTENSION IF NOT EXISTS tsm_system_rows;')


if __name__ == "__main__":
    __migrate()
    __import_file(sys.argv[1])
