class WeatherStation:
    def __init__(self, station: str):
        self.__station: str = station
        self.__observations: list = []
    
    def add_observation(self, observation: str):
        self.__observations.append(observation)
    
    def latest_observation(self):
        if not self.__observations:
            return ""
        return self.__observations[-1]
    
    def number_of_observations(self):
        return len(self.__observations)
    
    def __str__(self):
        return f"{self.__station}, {self.number_of_observations()} observations"


if __name__ == "__main__":
    a=WeatherStation("Kumpula")
    m=a.latest_observation()