import re

def valid_num (nums, maximum):
  for num in nums:
    if num[-1:] == "%":
      num = (float(num[:-1])* maximum )/ 100.0
    if float(num) < 0.0 or float(num) > maximum:
      return False
  return True

def valid_color (color):
  nums = re.findall(r"(-?\.?\d+(?:\.\d+)?%?)", color)
  if color[:5] == "rgba(":
    if len(nums) == 4:
      return valid_num(nums[:3], 255) and valid_num(nums[-1:], 1) 
    return False
  if color[:4] == "rgb(":
    if len(nums) == 3:
    	return valid_num(nums, 255)
    return False
  return False
