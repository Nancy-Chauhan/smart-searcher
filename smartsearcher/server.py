from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

from . import classifier
from . import bootstrap
from . import category_matcher

import os
import logging

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.html')


@app.route('/search', methods=['POST'])
def success():
    f = request.files['file']
    tmp_path = os.path.join('tmp', secure_filename(f.filename))
    f.save(tmp_path)

    predictions = classifier.predict(tmp_path)
    match = category_matcher.find_category(predictions)

    return jsonify({
        'categories': predictions,
        'bestMatch': match
    })


@app.route('/search', methods=['POST'])
def search():
    return jsonify([])


if __name__ == '__main__':
    logging.basicConfig()
    bootstrap.bootstrap()
    app.run(debug=True)
