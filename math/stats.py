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
# Mode, and
# Range
#
# (median coming soon, to a program near you)
# UPDATE: Median has been confirmed to work!!!
# UPDATE: It's 10:32 PM, but I fixed the mode function using some code
# I got from this website:
""">> https://datagy.io/python-get-dictionary-key-with-max-value <<"""


# int: 5
# str: “hi”
# dict: {“j”: “d”}
# list: [5, “5”, {“hi”: “hi”}, [5, ”8”]]
# None: None
# bool: True or False




def randdataset(length: int, min_: int, max_: int) -> list:
  return [random.randint(min_, max_) for i in range(length)]


def mean(dataset: list) -> float:
  return sum(dataset)/len(dataset)


def median(dataset: list) -> float:
  sortedlist = datasorted(dataset)
  # if the length is even
  if len(dataset)%2 == 0:
    middles = [
        sortedlist[int(len(sortedlist)/2 - 1)],
        sortedlist[int(len(sortedlist)/2)]      
    ]
   
    return mean(middles)
  # if the length is not even (if its odd)
  else:
    return sortedlist[int(len(sortedlist)/2 - 0.5)]
 

def datasorted(dataset: list) -> list:
  sortedlist = dataset.copy()
  sortedlist.sort()
  return sortedlist


def mode(dataset: list) -> float:
  frequencies = {str(i): dataset.count(i) for i in dataset}
  max_keys = [int(key) for key, value in frequencies.items() if value == max(frequencies.values())]
  if max_keys == dataset:
    return [None]
  return max_keys
 
 
def getrange(dataset: list) -> float:
  return max(dataset) - min(dataset)


def standard_deviation(dataset: list) -> float:
  return math.sqrt(
    sum(
      [abs(val - mean(dataset))**2 for val in dataset]
    )/len(dataset)
  )
  

def MAD(dataset: list) -> float:
  return mean([abs(x - mean(dataset)) for x in dataset])
  
# DEFINE YOUR DATASET AS 'data = [val1, val2, val3...]' where val1-3 is your values, 
# continuing if you have more than three values
if __name__ == '__main__':
  data = [6, 3, 2, 1]

   
  
  def printEverything():
    vals = {
      "total": str(sum(data)),
      "length": str(len(data)),
      "sorted": str(datasorted(data)),
      "mean": str(mean(data)),
      "median": str(median(data)),
      "mode": str(mode(data)).replace('[', '').replace(']', ''),
      "range": str(getrange(data)),
      "sd": str(round(standard_deviation(data), 10)),
      "mad": str(round(MAD(data), 10)),
    }    
    
    print(f"Total: {vals['total']}")
    print(f"Length: {vals['length']}")
    print(f"Sorted: {vals['sorted']}")
    print(f"Mean: {vals['mean']}")
    print(f"Median: {vals['median']}")
    print(f"Mode: {vals['mode']}")
    print(f"Range: {vals['range']}")
    print(f"Standard Deviation: {vals['sd']}")
    print(f"Mean Absolute Deviation: {vals['mad']}")
    
    
  printEverything()
