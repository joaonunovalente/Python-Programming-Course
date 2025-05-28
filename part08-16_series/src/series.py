class Series:
    def __init__(self, title: str, seasons: int, genre_list: list):
        self.title: str = title
        self.seasons: int = seasons
        self.genre_list: list = genre_list
        self.rating_list: list = []

    def rate(self, rating: int):
        self.rating_list.append(rating)
    
    def get_average(self):
        return sum(self.rating_list)/len(self.rating_list)
    
    def __str__(self):
        message1 = f"{self.title} ({self.seasons} seasons)\n"
        message2 = "genres: " + ", ".join(self.genre_list) + "\n"
        if len(self.rating_list) == 0:
            message3 = "no ratings"
        else:
            message3 = f"{len(self.rating_list)} ratings, average {self.get_average():.1f} points" 

        return message1 + message2 + message3

def minimum_grade(rating: float, series_list: list) -> list:
    output_list: list = []
    for serie in series_list:
        if serie.get_average() >= rating:
            output_list.append(serie) 

    return output_list

def includes_genre(genre: str, series_list: list) -> list:
    output_list: list = []
    for serie in series_list:
        if genre in serie.genre_list:
            output_list.append(serie)
            
    return output_list

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)