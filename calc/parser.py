# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2023/8/19
@mail: axingfly@gmail.com

Less is more.
"""

from lark import Lark
from lark import Transformer

from calc.grammer import GRAMMAR


class Calc(Transformer):
    def __init__(self):
        super().__init__()
        self.parser = Lark(grammar=GRAMMAR, start="start", parser='lalr', debug=True)

    def start(self, items):
        return items[0]

    def add(self, items):
        return items[0] + items[1]

    def sub(self, items):
        return items[0] - items[1]

    def mul(self, items):
        return items[0] * items[1]

    def div(self, items):
        return items[0] / items[1]

    def number(self, items):
        return float(items[0])

    def neg(self, items):
        return -items[0]


if __name__ == '__main__':
    c = Calc()
    tree = c.parser.parse("3 + 5 * (2 - 8)")
    result = c.transform(tree)
    print(result, type(result))
