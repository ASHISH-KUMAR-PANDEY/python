def split_into_buckets(phrase, n):
  word_list = phrase.split(" ")
  dictionary = {}
  i = 0
  max_length = len(max(word_list, key=len))
  length = 0
  lst = []
  if (max_length > n):
    return []
  for word in word_list:
    length = len(word)
    if (length > n):
      break
    else:
      if (i not in dictionary): 
        if (len(word) <= n):
          dictionary[i] = word + " "
      elif (len(dictionary[i] + word) <= n):
        dictionary[i] = dictionary[i] + word + " "
      else:
        i = i + 1
        dictionary[i] = word + " "

  for key in dictionary:
    lst.append(dictionary[key].rstrip())

  return lst
