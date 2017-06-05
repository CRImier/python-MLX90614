from mlx90614 import *

thermometer = MLX90614(0x5a)

print thermometer.get_amb_temp()
print thermometer.get_obj_temp()