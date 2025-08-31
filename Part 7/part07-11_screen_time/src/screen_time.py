from datetime import datetime, timedelta


def input_info() -> dict:
    """
    Collects input from the user for filename, starting date, and number of days.
    It also collects the screen time for each day.
    Returns a dictionary with all this information.
    """
    # Ask for user input 
    filename: str = input("Filename: ")
    starting_date: str = input("Starting date (dd.mm.yyyy): ")
    number_days: int = int(input("How many days: "))

    # Define datetime object
    day: int = int(starting_date.split(".")[0])
    month: int = int(starting_date.split(".")[1])
    year: int = int(starting_date.split(".")[2])
    first_day: datetime = datetime(year, month, day)

    # Define timedelta object: 1 day
    one_day: timedelta = timedelta(days=1)

    last_day = first_day + (one_day * (number_days - 1))

    # Create dictionary to store the screen time values
    my_dictionary: dict = {}
    my_dictionary["filename"] = filename
    my_dictionary["first_date"] = first_day.strftime("%d.%m.%Y")
    my_dictionary["last_date"] = last_day.strftime("%d.%m.%Y")
    my_dictionary["number_days"] = number_days

    # Loops for {number_days} asking for the screen time.
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    total_number_minutes: int = 0
    for i in range(number_days):
        current_day: datetime = first_day + (one_day * i)
        screen_time: str = input(f"Screen time {current_day.strftime('%d.%m.%Y')}: ")

        number_minutes: int = sum(map(int, screen_time.split(" ")))
        total_number_minutes += number_minutes

        my_dictionary[f"day_{i + 1}"] = [current_day.strftime("%d.%m.%Y"), screen_time, number_minutes]

    average: float = total_number_minutes / number_days
    my_dictionary["total number minutes"] = total_number_minutes
    my_dictionary["average"] = average
    
    return my_dictionary

def save_data(my_dictionary: dict):
    """Saves data in text file."""

    with open(my_dictionary["filename"], "w") as f:
        f.write(f"Time period: {my_dictionary['first_date']}-{my_dictionary['last_date']}\n")
        f.write(f"Total minutes: {my_dictionary['total number minutes']}\n")
        f.write(f"Average minutes: {my_dictionary['average']}\n")

        for i in range(1, my_dictionary["number_days"] + 1):
            parts = my_dictionary[f"day_{i}"][1].replace(" ", "/")
            f.write(f"{my_dictionary[f'day_{i}'][0]}: {parts}\n")


def main():
    """Main function that calls every function in the script."""
    my_dictionary = input_info()
    save_data(my_dictionary)

main()
