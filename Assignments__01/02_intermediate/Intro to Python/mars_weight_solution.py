def calculate_weight_on_planet(earth_weight,planet):
  gravity_constants = {
      "Mercury": 0.376,
      "Venus": 0.889,
      "Mars": 0.378,
      "Jupiter": 2.360,
      "Saturn": 1.081,
      "Uranus": 0.815,
      "Neptune": 1.140,
  }

  if planet in gravity_constants:
    weight_on_planet = earth_weight * gravity_constants[planet]
    return f"Your weight on {planet} is: {weight_on_planet: .2f}"

  else:
    return "Invalid planet name"

earth_weight = float(input("Enter your weight on Earth: "))
planet = input("Enter the name of a planet in our solar system: ")

result = calculate_weight_on_planet(earth_weight, planet)
print(result)