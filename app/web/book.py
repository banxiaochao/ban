from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchFrom

from . import web


@web.route('/book/search/')
def search():
    """
        q :普通关键字 isbn
        page
    :return:
    """
    q = request.args['q']
    # 至少要有一个字符，长度限制
    page = request.args['page']
    # 正整数，最大值限制

    #验证层
    form = SearchFrom(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
        # dict序列化
        # API
        return jsonify(result)
    #return json.dumps(result),200,{'content-type':'application/json'}
    else:
        return jsonify({'msg':'参数错误'})