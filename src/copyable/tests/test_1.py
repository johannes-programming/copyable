from __future__ import annotations

import unittest
from typing import *

from copyable.core import Copyable


class TestCopyable(unittest.TestCase):
    def test_copyable_cannot_be_instantiated(self: Self) -> None:
        with self.assertRaises(TypeError):
            Copyable()  # abstract

    def test_subclass_without_copy_is_abstract(self: Self) -> None:
        class Bad(Copyable):
            pass

        with self.assertRaises(TypeError):
            Bad()

    def test_copy_returns_same_type_and_new_instance(self: Self) -> None:
        class Point(Copyable):
            __slots__ = ("x", "y")

            def __init__(self: Self, x: int, y: int) -> None:
                self.x = x
                self.y = y

            def copy(self: Self) -> Self:
                return type(self)(self.x, self.y)

        p: Point
        c: Point
        p = Point(1, 2)
        c = p.copy()

        self.assertIsInstance(c, Point)
        self.assertIsNot(c, p)
        self.assertEqual((c.x, c.y), (p.x, p.y))


if __name__ == "__main__":
    unittest.main()
