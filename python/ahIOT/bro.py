from firebase import send_firebase
from lib.ThermalSensor.Extract_raw import get_frame

# i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

# mlx = adafruit_mlx90640.MLX90640(i2c)
# print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

# # if using higher refresh rates yields a 'too many retries' exception,
# # try decreasing this value to work with certain pi/camera combinations
# mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

while True:
  send_firebase(get_frame())
    