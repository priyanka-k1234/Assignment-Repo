# main.py
from carbon_calculators import calculate_energy_footprint, calculate_travel_footprint, calculate_waste_footprint
from report_generator import generate_report

def main():
    print("Welcome to the Carbon Footprint Monitoring Tool!")
    
    # Collect data from the user
    energy_kWh = float(input("Enter your energy consumption in kWh: "))
    miles_travelled = float(input("Enter the total miles traveled in a year: "))
    vehicle_type = input("Enter your vehicle type (car, electric_car, bus): ").lower()
    waste_weight = float(input("Enter the total waste generated in kg: "))

    # Calculate carbon footprint for each category
    energy_footprint = calculate_energy_footprint(energy_kWh)
    travel_footprint = calculate_travel_footprint(miles_travelled, vehicle_type)
    waste_footprint = calculate_waste_footprint(waste_weight)

    # Generate and print the report
    report = generate_report(energy_footprint, travel_footprint, waste_footprint)
    print("\nCarbon Footprint Report:\n")
    print(report)

if __name__ == "__main__":
    main()