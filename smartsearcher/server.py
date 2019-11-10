from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from . import classifier
from . import bootstrap
from . import category_matcher
from . import image_search
from . import repository

import os
import logging
import uuid

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('server')

app = Flask(__name__)
CORS(app)

@app.route('/')
def upload():
    return render_template('upload.html')


@app.route('/search', methods=['POST'])
def search():
    req_id = str(uuid.uuid4())
    f = request.files['file']
    img_upload_path = os.path.join('tmp', secure_filename(f.filename))
    f.save(img_upload_path)

    log.info('%s: Received search request', req_id)

    log.info('%s: Running classifier', req_id)
    predictions = classifier.predict(img_upload_path)

    log.info('%s: Finding matching images', req_id)
    match = category_matcher.find_category(predictions)

    category = match['category']

    return jsonify({
        'category': match,
        'matches': image_search.find_matching_images(img_upload_path, category, req_id)
    })

@app.route('/discover')
def discover():
    return jsonify(repository.find_random_products(30))


if __name__ == '__main__':
    bootstrap.bootstrap()
    app.run(debug=True, host='0.0.0.0')
