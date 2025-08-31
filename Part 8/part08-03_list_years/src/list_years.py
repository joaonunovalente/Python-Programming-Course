# Write your solution here
# Remember the import statement
from datetime import date

def list_years(dates: list) -> list:
    list_years_ordered: list = []
    for date in dates:
        list_years_ordered.append(date.year)
    list_years_ordered.sort()

    return list_years_ordered


if __name__ == "__main__":
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)
