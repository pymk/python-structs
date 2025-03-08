from src.data_model import House, Person


def get_starks() -> House:
    stark_people = [
        Person("Eddard Stark"),
        Person("Catelyn Tully"),
        Person("Robb Stark"),
        Person("Sansa Stark"),
        Person("Arya Stark"),
        Person("Bran Stark"),
        Person("Rickon Stark"),
        Person("Jon Snow"),
    ]
    stark = House(
        name="Stark",
        seat="Winterfell",
        sigil="direwolf",
        words="Winter is coming",
        people=stark_people,
    )

    return stark
