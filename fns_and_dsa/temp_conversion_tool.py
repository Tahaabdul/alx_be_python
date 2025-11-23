FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
  """Converts a temperature from Fahrenheit to Celsius."""
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """Converts a temperature from Celsius to Fahrenheit."""
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  """Prompts the user for temperature conversion and displays the result."""
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        unit_label = "°C"
        result_unit = "°F"
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        unit_label = "°F"
        result_unit = "°C"
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

      print(f"{temperature:.1f}{unit_label} is {converted_temp:.2f}{result_unit}")
      break
    except ValueError as e:
      # Handle the case where the user enters a non-numeric value
      if "could not convert string to float" in str(e):  # Check for specific error message
        print("Invalid temperature. Please enter a numeric value.")
      else:
        print(f"Error: {e}")  # Print the original error message for other cases




if __name__ == "__main__":
  main()