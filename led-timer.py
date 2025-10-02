import time

led_path = '/sys/class/leds/ACT/brightness'

def write_led(value):
  with open(led_path, 'w') as file:
    file.write(str(value))

print('Blinking ACT LED... Press CTRL + C to stop')

try:
  while 1:
    write_led(1)
    time.sleep(0.5)
    write_led(0)
    time.sleep(0.5)
except KeyboardInterrupt:
  write_led(1)
  print('Stopped')