# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2023/8/19
@mail: axingfly@gmail.com

Less is more.
"""
from lark import Lark
from lark import Transformer

from jsonparser.grammar import GRAMMAR


class JsonUnmarshal(Transformer):
    def __init__(self):
        super().__init__()
        self.parser = Lark(grammar=GRAMMAR, start="start", parser='lalr', debug=True)

    def start(self, items):
        return items[0]

    def value(self, items):
        return items[0]

    def object(self, items):
        return dict(items)

    def array(self, items):
        return list(items)

    def pair(self, items):
        k, v = items
        return k, v

    def null(self, _):
        return None

    def true(self, _):
        return True

    def false(self, _):
        return False

    def SIGNED_NUMBER(self, item):
        return float(item)

    def ESCAPED_STRING(self, item):
        return item[1:-1]


if __name__ == '__main__':
    j = JsonUnmarshal()
    tree = j.parser.parse("""{"hello": "world", "name": ["a", "b", -12]}""")
    tran = j.transform(tree)
    print(tran)
    print(tran['hello'])
    print(tran['name'][0])
