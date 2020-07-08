def pyramidal_string(string, _type):
  # special cases
  if string == '':
    return []
  if len(string) == 1:
    return [string]

  pyramid_lines = calculate_pyramid_lines(string)
  if pyramid_lines == -1:
    return 'Error!'

  if _type == 'REV':
    return pyramidal_string_reverse(string, pyramid_lines)
  else:
    return pyramidal_string_regular(string)
  
def pyramidal_string_regular(string):
  str_len = len(string)
  result = []
  i = 0
  j = 1
  while i < str_len:
    result.append(adjust_line(string[i:i + j]))
    i += j
    j += 1
  return result

def pyramidal_string_reverse(string, pyramid_lines):
  str_len = len(string)
  result = []
  i = 0
  j = pyramid_lines - 1
  while i < str_len:
    result.append(adjust_line(string[i:i + j]))
    i += j
    j -= 1
  return result

def calculate_pyramid_lines(string):
  str_len = len(string)
  i = 0
  j = 1
  while i < str_len:
    i += j
    j += 1
  return j if str_len == i else -1

def adjust_line(string):
  str_len = len(string)
  str_final = ''
  for i in range(str_len):
    if i < str_len - 1:
      str_final += string[i] + ' '
    else:
      str_final += string[i]
  return str_final
