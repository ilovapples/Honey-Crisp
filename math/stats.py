# MY USERNAME IS ilovapples ON GITHUB
# GOTO https://github.com/ilovapples FOR MY WORK

import random
import math

# TITLE:
# 
# Stat Calculator for Datasets
# Calculates:
# 
# Total,
# Length (number of data points),
# Sorted,
# Mean,
# Median,
# Mode,
# Range, and
# Standard Deviation.
#
# UPDATE: Median has been confirmed to work!!!
# UPDATE: It's 10:32 PM, but I fixed the mode function using some code
# I got from this website:
""">> https://datagy.io/python-get-dictionary-key-with-max-value <<"""
# UPDATE: It’s 11:08 PM, but I added Standard Deviation calculation (after poring over the formula to make sure I understood it, of course)!


# int: 5
# str: “hi”
# dict: {“j”: “d”}
# list: [5, “5”, {“hi”: “hi”}, [5, ”8”]]
# None: None
# bool: True or False




def randdataset(length: int, min_: int, max_: int) -> list:
  dataset = []
  x = 0
  while x <= length:
      dataset.append(random.randint(min_, max_))
      x += 1
  return dataset


def mean(dataset: list) -> float:
  total = sum(dataset)
  length = len(dataset)
  mean = total/length
  return total, length, mean


def median(dataset: list) -> float:
  sorted = dataset.copy()
  sorted.sort()
  # if the length is even
  if len(dataset)%2 == 0:
    strsorted = str(sorted).replace('[', '').replace(']', '')
    middles = [
        sorted[int(len(sorted)/2 - 1)],
        sorted[int(len(sorted)/2)]      
    ]
   
    theaverage = mean(middles)[2]
    return strsorted, theaverage
  # if the length is not even (if its odd)
  else:
    strsorted = str(sorted).replace('[', '').replace(']', '')
    return strsorted, sorted[int(len(sorted)/2 - 0.5)]
 
 
def mode(dataset: list) -> float:
  frequencies = {str(i): dataset.count(i) for i in dataset}
  max_keys = [int(key) for key, value in frequencies.items() if value == max(frequencies.values())]
  if max_keys == dataset:
    return [None]
  return max_keys
 
 
def range(dataset: list) -> float:
  return max(dataset) - min(dataset)


def standard_deviation(dataset: list) -> float:
  return math.sqrt(
    sum(
      [abs(val - mean(dataset)[2])**2 for val in dataset]
    )/len(dataset)
  )

# DEFINE YOUR DATASET AS 'data = [val1, val2, val3...]' where val1-3 is your values, 
# continuing if you have more than three values
data = [6, 3, 2, 1]

datasum, datalen, datamean = mean(data)
datasort, datamedian = median(data)

def printEverything():
  print(f"Total: {str(datasum)}")
  print(f"Length: {str(datalen)}")
  print(f"Mean: {str(datamean)}")
  print(f"Mode: {str(mode(data)).replace('[', '').replace(']', '')}")
  print(f"Sorted: {datasort}")
  print(f"Median: {str(datamedian)}")
  print(f"Range: {str(range(data))}")
  print(f"Standard Deviation: {str(standard_deviation(data))}")
  
  
printEverything()
