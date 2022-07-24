from typing import Dict
from gpiozero import LED

_pin_numbers: Dict[str, int] = {
  "dp": 2,
  "a": 3,
  "b": 4,
  "c": 7,
  "d": 8,
  "e": 9,
  "f": 10,
  "g": 11,
}
pin_numbers = {}
for key, value in _pin_numbers.items():
  # print(f"initializing LED on pin {value=}")
  pin_numbers[key] = {"num": value, "LED": LED(value)}
pin_numbers["nonDp"] = {k: v for k, v in pin_numbers.items() if k != "dp"}

# Digits to display map
digit_mappings = {
# A	B	C	D	E	F	G
  "__meta__": ["a", "b", "c", "d", "e", "f", "g"],
  "0": "1111110",
  "1": "0110000",
  "2": "1101101",
  "3": "1111001",
  "4": "0110011",
  "5": "1011011",
  "6": "1011111",
  "7": "1110000",
  "8": "1111111",
  "9": "1111011",
  "A": "1110111",
  "b": "0011111",
  "C": "1001110",
  "d": "0111101",
  "E": "1001111",
  "F": "1000111",
  "Empty": "0000000",
  "Full": "1111111",
}

def display_char(digit: str="Full", pin_numbers=pin_numbers):
  for i, pin in enumerate(digit_mappings[digit]):
    led = pin_numbers[digit_mappings["__meta__"][i]]["LED"]
    state = True if pin == "1" else False
    # print(f"Changing led (num {i=}, {led=}) to {state=}")
    led.on() if state else led.off()

if __name__ == "__main__":
  display_char("0")