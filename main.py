from lib import calculate_travel_time, calculate_fuel_needed, calculate_trip_cost

def main():
    """Головна функція для розрахунку поїздки."""
    distance = 540
    speed = 90
    consumption = 8
    price = 55

    travel_time = calculate_travel_time(distance, speed)
    fuel = calculate_fuel_needed(distance, consumption)
    cost = calculate_trip_cost(fuel, price)

    print("--- Розрахунок поїздки ---")
    print(f"Відстань: {distance} км")
    print(f"Час у дорозі: {travel_time} год")
    print(f"Потрібно пального: {fuel} л")
    print(f"Загальна вартість: {cost} грн")

if __name__ == '__main__':
    main()