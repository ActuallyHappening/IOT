# Original Source: https://docs.circuitpython.org/projects/mlx90640/en/latest/
import busio
try:
  from . import adafruit_mlx90640 as adafruit_mlx90640
except ImportError as exc:
  raise exc
  from .. .. import adafruit_mlx90640 as adafruit_mlx90640

try:
  import board
except NotImplementedError as exc:
  print(f"Note: This machine is not compatible with MLX90640")
  raise NotImplementedError from exc
else:
  
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
  mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ

def main():
  try:
    import Process_raw as process
  except ImportError as exc:
    print("Error: Could not import Process_raw, not started main loop")
  while True:
    print(get_frame())

def get_frame():
  frame = [0] * (24*32)
  _err_count = 0
  while True:
    try:
        mlx.getFrame(frame)
    except ValueError as exc:
        # these happen, no biggie - retry
        print(f"(Error) ValueError: {exc}")
        _err_count += 1
        if _err_count > 3:
          print(f"(Warning: Changing mls_refresh_rate to 2Hz)")
          mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
        if _err_count > 6:
          print(f"(Warning: Changing mls_refresh_rate to 1Hz)")
          mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_1_HZ
        if _err_count > 9:
          print(f"(ERROR: Too many retries, exiting, at refresh rate of 1Hz)")
    if _err_count == 0:
        print(f"(Info: Changing/Keeping mlx_refresh_rate to 4Hz)")
        mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ
    return frame

if __name__ == "__main__":
  main()