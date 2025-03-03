import math


def get_station_data(filename: str) -> dict:
    stations: dict = {}

    with open(filename) as file:
        it = iter(file)
        next(it, None)
        for line in file:
            line = line.strip()
            parts = line.split(';')

            longitude = float(parts[0])
            latitude = float(parts[1])
            station_name = parts[3]

            # Add to dictionary
            stations[station_name] = (longitude, latitude)

    return stations


def distance(stations: dict, station1: str, station2: str) -> float:
    for key, value in stations.items():
        if key == station1:
            longitude1 = value[0]
            latitude1 = value[1]
        elif key == station2:
            longitude2 = value[0]
            latitude2 = value[1]

        if station1 == station2:
            longitude1 = 0
            longitude2 = 0
            latitude1 = 0
            latitude2 = 0

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict) -> tuple[str, str, float]:
    result = tuple()
    d_maximum = 0
    for station1 in stations:
        for station2 in stations:
            d = distance(stations, station1, station2)
            if d > d_maximum:
                result = tuple()
                result = (station1, station2, d)
                d_maximum = d
    
    return result


if __name__ == "__main__":
    filename = 'stations1.csv'
    stations = get_station_data(filename)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)