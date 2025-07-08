class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __eq__(self, another):
        if self.day + self.month + self.year == another.day + another.month + another.year:
            return True
        else:
            return False
        
    def __gt__(self, another):
        date1 = str(self.year) + str(format(self.month,'02')) + str(format(self.day,'02')) 
        date2 = str(another.year) + str(format(another.month,'02')) + str(format(another.day,'02'))
        if date1 > date2:
            return True
        else:
            return False
        
    def __add__(self, days: int):
        total_days = (self.year * 360) + ((self.month - 1) * 30) + (self.day - 1)
        total_days += days

        new_year = total_days // 360
        leftover_days = total_days % 360

        new_month = (leftover_days // 30) + 1
        new_day = (leftover_days % 30) + 1

        return SimpleDate(new_day, new_month, new_year)
    
    def __sub__(self, another):
        total_days_self = (self.year * 360) + ((self.month - 1) * 30) + (self.day - 1)
        total_days_another = (another.year * 360) + ((another.month - 1) * 30) + (another.day - 1)
        return abs(total_days_self - total_days_another)

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)