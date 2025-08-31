# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds: int = 0
        self.minutes: int = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.minutes = 0
            self.seconds = 0

    def __str__(self):
        if int(self.minutes) < 10 and int(self.seconds) < 10:
            return f"{"0" + str(self.minutes)}:{"0" + str(self.seconds)}"
        if int(self.minutes) < 10:
            return f"{"0" + str(self.minutes)}:{self.seconds}"
        if int(self.seconds) < 10:
            return f"{self.minutes}:{"0" + str(self.seconds)}"
        return f"{self.minutes}:{self.seconds}"
    

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3601):
        print(watch)
        watch.tick()