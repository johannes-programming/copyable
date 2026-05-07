from abc import ABC, abstractmethod
from typing import *

import setdoc

__all__ = ["Copyable"]


class Copyable(ABC):
    __slots__ = ()

    @setdoc.basic
    def __copy__(self: Self) -> Self:
        return self.copy()

    __hash__: Any
    __hash__ = None

    @abstractmethod
    @setdoc.basic
    def copy(self: Self) -> Self: ...
