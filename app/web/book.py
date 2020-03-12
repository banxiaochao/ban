from flask import jsonify, request,render_template,flash
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchFrom
from app.view_models.book import BookViewModel, BookCollection
import json

from . import web


@web.route('/book/search/')
def search():
    """
        q :普通关键字 isbn
        page
    :return:
    """
   # q = request.args['q']
    # 至少要有一个字符，长度限制
   # page = request.args['page']
    # 正整数，最大值限制

    #验证层
    form = SearchFrom(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        # yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book = YuShuBook()
            yushu_book.search_by_isbn(q)
        else:
            yushu_book = YuShuBook()
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
       # return json.dumps(books,default=lambda o: o.__dict__)
       # return jsonify(books.__dict__)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
       # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass


@web.route('/test')
def test():
    r = {
        'name': 'None',
        'age': 18
    }
    flash('hello,banxiaochao')
    flash('hello,3yue')

    #模板 html
    return render_template('test.html', data=r)