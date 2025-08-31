from datetime import datetime


def is_it_valid(pic: str) -> bool:
    """Validates the Finnish Personal Identity Codes (PIC)."""
    string_constante = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    # Variables
    date = pic[0:6]
    day = pic[0:2]
    mouth = pic[2:4]
    year = pic[4:6]
    century = pic[6]
    personal_identifier = pic[7:10]
    control_character = pic[10]
    

    number = int(date + personal_identifier)
    remainder = number % 31
    if string_constante[remainder] == control_character:
        pass
    else:
        return False
    

    if len(pic) != 11:
        return False
    
    try:
        if century == "-":
            year = "18" + year
        elif century == "+":
            year = "19" + year
        elif century == "A":
            year = "20" + year 
        date = datetime(int(year), int(mouth), int(day))
    except ValueError:
        return False


    return True

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
    print(is_it_valid("290200-1239"))
