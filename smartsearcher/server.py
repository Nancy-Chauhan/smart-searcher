from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

from . import classifier
from . import bootstrap
from . import category_matcher
from . import image_search
from . import repository

import os
import logging

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.html')


@app.route('/search', methods=['POST'])
def search():
    f = request.files['file']
    img_upload_path = os.path.join('tmp', secure_filename(f.filename))
    f.save(img_upload_path)

    predictions = classifier.predict(img_upload_path)
    match = category_matcher.find_category(predictions)

    category = match['category']

    return jsonify({
        'category': match,
        'matches': image_search.find_matching_images(img_upload_path, category)
    })

@app.route('/discover')
def discover():
    return jsonify(repository.find_random_products(30))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    bootstrap.bootstrap()
    app.run(debug=True)
