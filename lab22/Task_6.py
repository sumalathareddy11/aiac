# ============================================
# Task 6 – Environmental and Societal Impact
# AI Energy Consumption Awareness Simulator
# ============================================

def calculate_energy_consumption(model_type, usage_hours):
    """
    Simulate energy consumption (kWh) for different AI models.
    These are just approximate demo values for understanding.
    """
    # Approximate power usage per hour (in kWh)
    power_usage = {
        "small_model": 0.5,     # like a chatbot or small ML model
        "medium_model": 2.0,    # image generation or NLP model
        "large_model": 10.0     # large-scale AI model like GPT training
    }
    
    energy_used = power_usage.get(model_type, 0) * usage_hours
    carbon_emission = energy_used * 0.45  # 0.45 kg CO2 per kWh (approximate)
    return energy_used, carbon_emission


def main():
    print("=====================================")
    print(" 🌍 AI ENERGY IMPACT SIMULATOR ")
    print("=====================================\n")
    print("Learn how AI computing affects energy and the environment.\n")

    print("Select AI model type:")
    print("1. Small model (chatbot, small ML tasks)")
    print("2. Medium model (image generation, NLP)")
    print("3. Large model (AI training on GPUs)")
    
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        model_type = "small_model"
    elif choice == "2":
        model_type = "medium_model"
    elif choice == "3":
        model_type = "large_model"
    else:
        print("Invalid choice! Defaulting to small model.")
        model_type = "small_model"

    usage_hours = float(input("\nEnter estimated usage hours: "))

    energy_used, carbon_emission = calculate_energy_consumption(model_type, usage_hours)

    print("\n=====================================")
    print("        AI ENERGY REPORT")
    print("=====================================")
    print(f"Model Type        : {model_type.replace('_', ' ').title()}")
    print(f"Usage Duration    : {usage_hours} hour(s)")
    print(f"Energy Consumed   : {energy_used:.2f} kWh")
    print(f"CO₂ Emitted       : {carbon_emission:.2f} kg")
    print("-------------------------------------")
    print("🌱 Environmental Tip:")
    print("- Optimize code to use less GPU power.")
    print("- Use energy-efficient cloud servers.")
    print("- Schedule heavy AI tasks during renewable energy hours.")
    print("-------------------------------------")
    print("💬 Societal Impact Discussion:")
    print("AI systems depend on large data centers that consume massive energy.")
    print("Students and developers must balance innovation with sustainability.")
    print("=====================================\n")


if __name__== "__main__":
    main()