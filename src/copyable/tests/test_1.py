from __future__ import annotations

import unittest
from typing import Any, Self

from copyable.core import Copyable

__all__ = ["TestCopyable1"]


class TestCopyable1(unittest.TestCase):
    def _test_init_raises(self: Self, cls: Any) -> None:
        with self.assertRaises(TypeError):
            cls()  # abstract

    def test_copyable_cannot_be_instantiated(self: Self) -> None:
        self._test_init_raises(Copyable)

    def test_subclass_without_copy_is_abstract(self: Self) -> None:
        class Bad(Copyable):
            pass

        self._test_init_raises(Bad)

    def test_subclass_must_implement_copy(self: Self) -> None:

        class Good(Copyable):
            def copy(self: Self) -> Self:
                return self

        g: Good
        g = Good()
        self.assertIs(g.copy(), g)

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
