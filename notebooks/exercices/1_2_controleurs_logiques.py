if unit == "Celsius" or unit == "C":
    new_temperature = (9 * temperature) / 5 + 32
    print(str(temperature) + " Celsius correspond à " + str(new_temperature) + " Fahrenheit.")
elif unit == "Fahrenheit" or unit == "F":
    new_temperature = (temperature - 32) * 5 / 9
    print(str(temperature) + " Fahrenheit correspond à " + str(new_temperature) + " Celsius.")