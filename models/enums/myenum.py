try:
    from enum import StrEnum
except ImportError:
    from enum import Enum
    class StrEnum(str, Enum):
        ...


class ItemTypes(str, Enum):
    entry1 = 'entry1'
    entry2 = 'entry2'
    entry3 = 'entry3'
