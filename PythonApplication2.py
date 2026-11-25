from models import Antibiotic, Medicine, Vaccine, Vitamin


def print_medicines_info(medicines: list[Medicine]) -> None:
    for item in medicines:
        print(item.info())


def main() -> None:
    medicines: list[Medicine] = [
        Antibiotic("Амоксиклав", 2, 185.0),
        Vitamin("Вітамін D3", 1, 240.5),
        Vaccine("Вакцина проти грипу", 5, 420.0),
    ]
    print_medicines_info(medicines)


if __name__ == "__main__":
    main()
