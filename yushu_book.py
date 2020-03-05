from http import HTTP

class YuShuBook:
    isbn_url = 'http://127.0.0.1/book/isbn/{}'
    keyword_url = 'http://127.0.0.1/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    def search_by_keyword(cls,keyword,count=15,start=0):
        url = cls.keyword_url.format(keyword,count,start)
        result = HTTP.get(keyword)
        return result