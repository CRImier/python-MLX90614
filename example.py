from mlx90614 import MLX90614

thermometer_address = 0x5a

thermometer = MLX90614(thermometer_address)

print thermometer.get_amb_temp()
print thermometer.get_obj_temp() 
