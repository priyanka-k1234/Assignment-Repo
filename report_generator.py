# report_generator.py

def generate_report(energy_footprint, travel_footprint, waste_footprint):
    total_footprint = energy_footprint + travel_footprint + waste_footprint
    suggestions = []

    if energy_footprint > 1000:
        suggestions.append("Consider using energy-efficient appliances or renewable energy sources.")
    if travel_footprint > 500:
        suggestions.append("Try using public transport or switching to an electric vehicle.")
    if waste_footprint > 100:
        suggestions.append("Increase recycling efforts and reduce waste generation.")

    report = f"Total Carbon Footprint: {total_footprint} kg CO2\n\nSuggestions to reduce:\n"
    for suggestion in suggestions:
        report += f"- {suggestion}\n"
    return report
