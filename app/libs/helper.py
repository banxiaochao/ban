def is_isbn_or_key(word):
    """
    # isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些‘-’
    #判断传进来的是否为isbn
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-','')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key