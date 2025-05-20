# 12. Static Methods
# Assignment: 12 Static Methods
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

# Solve:

class TempratureConverter:


    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


if __name__ == "__main__":
    print("Fahrenheit:", TempratureConverter.celsius_to_fahrenheit(25))
    print("Fahrenheit:", TempratureConverter.celsius_to_fahrenheit(200))