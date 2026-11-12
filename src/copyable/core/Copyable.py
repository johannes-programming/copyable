from __future__ import annotations

__all__: list[str] = ["Copyable"]

from abc import ABC, abstractmethod
from typing import Any, Self

import setdoc


class Copyable(ABC):
    __slots__ = ()

    __hash__: Any
    __hash__ = None

    @abstractmethod
    @setdoc.basic
    def copy(self: Self) -> Self: ...
