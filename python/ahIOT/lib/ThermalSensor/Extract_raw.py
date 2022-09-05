# Original Source: https://docs.circuitpython.org/projects/mlx90640/en/latest/

try:
  import board
except NotImplementedError as exc:
  print(f"Note: This machine is not compatible with MLX90640")
  raise NotImplementedError from exc
else:
  import busio
  import adafruit_mlx90640

  i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

  mlx = adafruit_mlx90640.MLX90640(i2c)
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
    process.iterate(process.print_frame_value)

def get_frame():
  frame = [0] * (24*32)
  try:
      mlx.getFrame(frame)
  except ValueError:
      # these happen, no biggie - retry
      print("(Error)")
      return None
  return frame

if __name__ == "__main__":
  main()