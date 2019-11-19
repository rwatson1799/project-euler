import numpy as np

nums = np.array(range(1,101))

diff = (sum(nums) ** 2) - sum(nums ** 2)

print(diff)