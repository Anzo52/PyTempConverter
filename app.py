# API for converting between Fahrenheit and Celsius

from converter import converts
from flask import Flask
from flask import jsonify
from flask import request
from flask_autodoc.autodoc import Autodoc

app = Flask(__name__)
auto = Autodoc(app)

@app.route('/', methods=['GET'])
def index():
    return '''<h1>API for converting between Fahrenheit and Celsius</h1>
<p>/api/v1.0/convert?f=<i>fahrenheit</i>&c=<i>celsius</i></p>
<p>/api/v1.0/convert?c=<i>celsius</i>&f=<i>fahrenheit</i></p>'''


@app.route('/api/v1.0/convert', methods=['GET'])
@auto.doc()
def convert():
    if 'f' in request.args:
        f = float(request.args['f'])
        c = converts.f2c(f)
        return jsonify({'f': f, 'c': c})
    elif 'c' in request.args:
        c = float(request.args['c'])
        f = converts.c2f(c)
        return jsonify({'c': c, 'f': f})
    else:
        return jsonify({'error': 'Missing parameter'})

@app.route('/documentation')
def documentation():
  return auto.html()


if __name__ == '__main__':
    app.run(debug=True)


# curl -i http://localhost:5000/api/v1.0/convert?f=32
# curl -i http://localhost:5000/api/v1.0/convert?c=0
