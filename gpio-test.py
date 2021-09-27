import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

print("Probing all GPIOs. 0 = 0V, 1 = 3.3V")

for i in range(26):
	gpio.setup(i + 1, gpio.IN)
	print("GPIO " + str(i + 1) + ": " + str(gpio.input(i + 1)))
