# carbon_calculators.py

def calculate_energy_footprint(kWh):
    # Average carbon footprint for 1 kWh of energy (this will vary by location)
    carbon_per_kWh = 0.92  # in kg CO2 per kWh (example value)
    return kWh * carbon_per_kWh

def calculate_travel_footprint(miles, vehicle_type):
    # Average CO2 emissions for various vehicle types (kg CO2 per mile)
    emissions_per_mile = {
        'car': 0.411,  # Example: gas car
        'electric_car': 0.0,  # Zero emissions for electric car
        'bus': 0.089,  # Average for a bus per mile
    }
    return miles * emissions_per_mile.get(vehicle_type, 0)

def calculate_waste_footprint(weight):
    # Approximate carbon footprint of waste (kg CO2 per kg of waste)
    carbon_per_kg = 0.4
    return weight * carbon_per_kg
