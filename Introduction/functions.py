cars = [
    {"company": "Tata", "model": "Nano", "mileage": 30000, "fuel_consumed": 400},
    {"company": "BMW", "model": "X5", "mileage": 15000, "fuel_consumed": 350},
    {"company": "Hyundai", "model": "Verna", "mileage": 22000, "fuel_consumed": 390}]


def calculate_mpl(car_calc, intro):
    print(intro)
    mpl = car_calc["mileage"]/car_calc["fuel_consumed"]
    name = f"{car_calc['company']} {car_calc['mileage']}"
    print(f"{name} does {mpl} miles per litre")


for car in cars:
    calculate_mpl(car, "This car")
