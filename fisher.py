from flask import Flask
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search/<q>/<page>')
def search(q,page):
    """
        q :普通关键字 isbn
        page
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    pass



def helloq():
    return 'hello,xiaoban'

#app.add_url_rule('/hello',view_func=hello)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=81)