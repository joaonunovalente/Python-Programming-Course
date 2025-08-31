class LotteryNumbers:
    def __init__(self, week: int, numbers: int):
        self.week = week
        self.correct_numbers = numbers
    
    def number_of_hits(self, hit_numbers: int):
        return len([number for number in self.correct_numbers if number in hit_numbers])
    
    def hits_in_place(self, hit_numbers):
        return [number if number in self.correct_numbers else -1 for number in hit_numbers]

if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))