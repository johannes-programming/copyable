from abc import ABC, abstractmethod
from typing import *

import setdoc

__all__ = ["Copyable"]


class Copyable(ABC):
    __slots__ = ()

    __hash__ = None

    @abstractmethod
    @setdoc.basic
    def copy(self: Self) -> Self: ...
