from itertools import product

class Loop:
   def __init__(self, keys, values):
      self.keys = keys
      self.values = values
      self.old_keys = []

   def combine_nested_levels(self):
      if not self.old_keys:
         self.combinations = [list(map(list, product([key], [value])))[0] for key in self.keys for value in self.values[self.keys.index(key)]]
         return Loop.check_for_duplicates(self)
      else:
         self.combinations = [list(map(list, product(old_key, [key], value)))[0] for old_key in self.old_keys for key in self.keys for value in self.values]
         return Loop.check_for_duplicates(self)

   def check_for_duplicates(self):
      unique_combinations = list()
      for combination in self.combinations:
         if combination not in unique_combinations:
            unique_combinations.append(combination)
      return unique_combinations
