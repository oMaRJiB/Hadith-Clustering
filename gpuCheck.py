import tensorflow as tf

# 1. Check if the Metal GPU is visible to TensorFlow
gpus = tf.config.list_physical_devices('GPU')
print(f"Num GPUs Available: {len(gpus)}")
print(f"GPU Details: {gpus}")

# 2. (Optional) Log device placement to verify operations run on the GPU
tf.debugging.set_log_device_placement(True)

# Run a quick computation to trigger the Metal device printout
a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
b = tf.constant([[1.0, 1.0], [1.0, 1.0]])
c = tf.matmul(a, b)