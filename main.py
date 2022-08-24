import random

combinations = []

def GenerateCombination():
  list = []
  j = 0
  for j in range(15):
    number = random.randint(1,25)
    while(number in list):
      number = random.randint(1,25)
    list.append(number)
  return list

def CombinationExists (list):
  if(list in combinations):
    return True 
  return False

def main():
  i = 0
  for i in range(120):
    numbers = GenerateCombination()
    while(CombinationExists(numbers)): 
      numbers = GenerateCombination()
    print(i+1, "Jogos Gerados")
    combinations.append(numbers.copy())
    numbers.clear()
  print("------------------------------------------------------")
  combinations.sort()
  print("Jogos: ")
  for comb in combinations:
      comb.sort()
      print(comb)
main()