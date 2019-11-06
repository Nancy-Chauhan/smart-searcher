from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

from . import imagenet
from . import bootstrap

import os
import logging

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.html')


@app.route('/classify', methods=['POST'])
def success():
    f = request.files['file']
    tmp_path = os.path.join('tmp', secure_filename(f.filename))
    f.save(tmp_path)

    return jsonify({
        'imagenet': imagenet.predict(tmp_path)
    })


if __name__ == '__main__':
    logging.basicConfig()
    bootstrap.bootstrap()
    app.run(debug=True)
