from dataclasses import asdict, dataclass
from typing import List


@dataclass
class Person:
    name: str

    def __iter__(self):
        return iter(asdict(self).values())


@dataclass
class House:
    name: str
    seat: str
    sigil: str
    words: str
    people: List[Person]

    @property
    def is_valid(self) -> bool:
        return True if self.people and len(self.people) > 1 else False

    def list_members(self) -> None:
        for i in self.people:
            print(f" - {i.name}")
        return None

    def summary(self) -> None:
        summary_text = f"House {self.name} of {self.seat} with {self.sigil} sigil and '{self.words}' words has {len(self.people)} members."
        print(summary_text)
        return None
