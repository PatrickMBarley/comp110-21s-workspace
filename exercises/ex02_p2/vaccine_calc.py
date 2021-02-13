"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730163234"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days: int = days_to_target(population, doses, doses_per_day, target)
    vaccine_date: datetime = future_date(days)
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + vaccine_date.strftime("%B %d, %Y"))


def days_to_target(pop: int, doses: int, per_day: int, target: int) -> int:
    days: int = int(round((((target * pop * 2) / 100) - doses) / per_day))
    return days

def future_date(days: int) -> datetime:
    today: datetime = datetime.today()
    future: timedelta = timedelta(days)
    vaccinedate: datetime = today + future
    return vaccinedate

if __name__ == "__main__":
    main()
