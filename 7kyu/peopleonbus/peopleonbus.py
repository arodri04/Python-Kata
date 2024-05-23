def number(bus_stops):
    print(bus_stops)
    num = 0
    for stop in bus_stops:
        num += stop[0]
        num -= stop[1]
    return num