#!/usr/bin/python3
def validUTF8(data):
  """
  Determines if a given data set represents a valid UTF-8 encoding.

  Args:
    data: A list of integers representing the data set.

  Returns:
    True if data is a valid UTF-8 encoding, else False.
  """

  # Check if the data set is empty.
  if not data:
    return False

  # Check if the first byte of the data set is in the range 0x00 to 0x7F.
  if data[0] < 0x80:
    return True

  # Check if the first byte of the data set is in the range 0xC2 to 0xDF.
  elif data[0] >= 0xC2 and data[0] <= 0xDF:
    return len(data) == 2 and data[1] < 0x80

  # Check if the first byte of the data set is in the range 0xE0 to 0xEF.
  elif data[0] >= 0xE0 and data[0] <= 0xEF:
    return len(data) == 3 and (data[1] & 0xC0) == 0x80 and data[2] < 0x80

  # Check if the first byte of the data set is in the range 0xF0 to 0xF7.
  elif data[0] >= 0xF0 and data[0] <= 0xF7:
    return len(data) == 4 and (data[1] & 0xC0) == 0x80 and (data[2] & 0xC0) == 0x80 and data[3] < 0x80

  # Otherwise, the data set is not a valid UTF-8 encoding.
  else:
    return False
