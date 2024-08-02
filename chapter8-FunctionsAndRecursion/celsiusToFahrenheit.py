
def convert(value):
  return (value * 9/5) + 32


n=int(input("Enter the temperature in Celsius : "))
fahren=convert(n)
print(f"the celsius   {n} in fahrenheit is {fahren}")