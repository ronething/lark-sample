# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2023/8/19
@mail: axingfly@gmail.com

Less is more.
"""

GRAMMAR = """
start: value

object: "{" [pair ("," pair)*] "}"
pair: ESCAPED_STRING ":" value

array: "[" [value ("," value)*] "]"

value: ESCAPED_STRING
     | SIGNED_NUMBER
     | object
     | array
     | "true"       -> true
     | "false"      -> false
     | "null"       -> null

%import common.ESCAPED_STRING
%import common.SIGNED_NUMBER
%import common.WS
%ignore WS

"""
