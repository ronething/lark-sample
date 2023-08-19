# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2023/8/19
@mail: axingfly@gmail.com

Less is more.
"""

GRAMMAR = """
start: sum

?sum: product
    | sum "+" product   -> add
    | sum "-" product   -> sub

?product: item
    | product "*" item  -> mul
    | product "/" item  -> div

?item: NUMBER           -> number
     | "-" item         -> neg
     | "(" sum ")"

%import common.NUMBER
%ignore " "
"""