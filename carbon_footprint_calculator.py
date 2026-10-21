car_km = float(input("Car travel per week (km): "))
electricity = float(input("Electricity usage per week (kWh): "))

car_emissions = car_km * 0.2
power_emissions = electricity * 0.7
total = car_emissions + power_emissions

print("Car Emissions:", round(car_emissions, 2), "kg CO2")
print("Electricity Emissions:", round(power_emissions, 2), "kg CO2")
print("Weekly Carbon Footprint:", round(total, 2), "kg CO2")
