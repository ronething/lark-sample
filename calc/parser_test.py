import unittest

from calc.parser import Calc


class MyTestCase(unittest.TestCase):
    def test_parse(self):
        c = Calc()
        tree = c.parser.parse("3 + 5 * (2 - 8)")
        pretty_tree = """start
  add
    number	3
    mul
      number	5
      sub
        number	2
        number	8
"""
        # print(tree.pretty())
        self.assertEqual(pretty_tree, tree.pretty())  # add assertion here


if __name__ == '__main__':
    unittest.main()
