def calculate_travel_time(distance, speed):
    """"Розрахунок тривалості дороги."""
    return distance / speed


def calculate_fuel_needed(distance, consumption):
    """Обчислює необхідну кількість пального в літрах."""
    return (distance / 100) * consumption


def calculate_trip_cost(fuel_needed, fuel_price):
    """Обчислює вартість пального для поїздки."""
    return fuel_needed * fuel_price