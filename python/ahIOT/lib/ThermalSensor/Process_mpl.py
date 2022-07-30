from .Process_raw import defaultDimensions
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot(frame, dimensions=defaultDimensions):
  # using matplot lib plot the frame
  ...

def main():
  print("Beginning ...")
  x = np.linspace(0, 2 * np.pi, 200)
  y = np.sin(x)

  fig, ax = plt.subplots()
  ax.plot(x, y)
  plt.show()

if __name__ == '__main__':
    main()
    