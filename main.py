from src.populate_data import get_starks


def main():
    house_stark = get_starks()
    if house_stark.is_valid:
        house_stark.summary()
        house_stark.list_members()


if __name__ == "__main__":
    main()
