color_coefficients = {
    "white": 1,
    "blue": 1,
    "yellow": 1.1,
    "red": 1,
    "pearl white": 1.2,
    "metallic gray": 1.3
}

part_coefficients = {
    "hood": 1,
    "front door": 1.2,
    "rear door": 1.1,
    "front bumper": 1,
    "rear bumper": 1,
    "roof": 1.1
}

# Base cost per car part
base_cost = 12000

# Get user input
part = input("Enter the car part to be painted (hood, front door, rear door, front bumper, rear bumper, roof): ").strip().lower()
color = input("Enter the paint color (white, blue, yellow, red, pearl white, metallic gray): ").strip().lower()

# Check if the input is valid
if part in part_coefficients and color in color_coefficients:

    total_cost = base_cost * part_coefficients[part] * color_coefficients[color]

    print(f"The cost to paint the {part} with {color} color: {total_cost} RUB")
else:
    print("Invalid car part or color. Please try again.")
print("Thank you! See you again!")