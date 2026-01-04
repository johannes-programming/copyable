from abc import ABC, abstractmethod
from typing import *

import setdoc

__all__ = ["Copyable"]


class Copyable(ABC):
    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def copy(self: Self) -> Self: ...
