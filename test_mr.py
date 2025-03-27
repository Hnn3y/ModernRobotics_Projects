import modern_robotics as mr
import numpy as np

# Define an SE(3) matrix
se3mat = np.array([
    [0, 0, 0, 0], 
    [0, 0, -1.5708, 2.3562], 
    [0, 1.5708, 0, 2.3562], 
    [0, 0, 0, 0]
])

# Compute the matrix exponential
T = mr.MatrixExp6(se3mat)

# Print the result
print("Resulting Transformation Matrix:")
print(T)
