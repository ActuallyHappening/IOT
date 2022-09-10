# Original Source: https://docs.circuitpython.org/projects/mlx90640/en/latest/

try:
  import board
except NotImplementedError as exc:
  print(f"Note: This machine is not compatible with MLX90640")
  raise NotImplementedError from exc
else:
  import busio
  import adafruit_mlx90640

  while True:
    i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
    try:
      mlx = adafruit_mlx90640.MLX90640(i2c)
    except ValueError as exc:
      print(f"No MLX90640 detected :( - {exc}")
    else:
      break
  
  print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

  # if using higher refresh rates yields a 'too many retries' exception,
  # try decreasing this value to work with certain pi/camera combinations
  mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

def main():
  try:
    import Process_raw as process
  except ImportError as exc:
    print("Error: Could not import Process_raw, not started main loop")
  while True:
    print(get_frame())

def get_frame():
  frame = [0] * (24*32)
  while frame[0] == 0:
    try:
        mlx.getFrame(frame)
    except ValueError as exc:
        # these happen, no biggie - retry
        print("(Error) ValueError: {exc}")
    return frame

if __name__ == "__main__":
  main()