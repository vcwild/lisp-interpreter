from collections.abc import MutableMapping
from typing import TypeAlias

Symbol: TypeAlias = str
Number: TypeAlias = int | float
Atom: TypeAlias = int | float | Symbol
Expression: TypeAlias = Atom | list
Environment: TypeAlias = MutableMapping[Symbol, object]
