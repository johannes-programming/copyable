import inspect
import unittest
from abc import ABCMeta
from typing import *

from copyable.core import Copyable


class TestCopyable(unittest.TestCase):
    def test_is_abstract(self: Self) -> None:
        # Copyable must be an abstract base class and not directly instantiable.
        self.assertIsInstance(Copyable, ABCMeta)
        with self.assertRaises(TypeError):
            Copyable()  # type: ignore[abstract]

    def test_slots_hash_and_abstractmethod(self: Self) -> None:
        copy_attr: Any
        # __slots__ is explicitly empty and __hash__ disabled.
        self.assertTrue(hasattr(Copyable, "__slots__"))
        self.assertEqual(getattr(Copyable, "__slots__"), ())
        self.assertIsNone(getattr(Copyable, "__hash__"))

        # "copy" exists and is marked abstract.
        self.assertTrue(hasattr(Copyable, "copy"))
        copy_attr = getattr(Copyable, "copy")
        self.assertTrue(getattr(copy_attr, "__isabstractmethod__", False))

    def test_copy_signature_and_annotations(self: Self) -> None:
        # Ensure there's a "copy" method and it has type hints present.
        # Note: runtime "Self" may or may not resolve depending on Python version;
        # we just verify annotations are present and consistent.
        hints: dict[str, Any]
        sig: inspect.Signature
        params: list[inspect.Parameter]
        self.assertTrue(callable(getattr(Copyable, "copy")))
        hints = get_type_hints(Copyable.copy, include_extras=True)
        self.assertIn("return", hints)

        sig = inspect.signature(Copyable.copy)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0].name, "self")

    def test_subclass_must_implement_copy(self: Self) -> None:
        class Bad(Copyable):
            pass

        class Good(Copyable):
            def copy(self: Self) -> Self:
                return self

        g: Good
        with self.assertRaises(TypeError):
            Bad()  # still abstract
        g = Good()
        self.assertIs(g.copy(), g)


if __name__ == "__main__":
    unittest.main()
