cars = [
    {"company": "Tata", "model": "Nano", "mileage": 30000, "fuel_consumed": 400},
    {"company": "BMW", "model": "X5", "mileage": 15000, "fuel_consumed": 350},
    {"company": "Hyundai", "model": "Verna", "mileage": 22000, "fuel_consumed": 390}]


def calculate_mpl(car_calc):
    mpl = car_calc["mileage"]/car_calc["fuel_consumed"]
    return mpl


def car_name(cname):
    cname = f"{cname['company']} {cname['mileage']}"
    return cname


def car_info(car):
    name= car_name(car)
    mpl= calculate_mpl(car)
    print(f"{name} does {mpl} miles per litre")
    #return None

for car in cars:
    car_info(car)
