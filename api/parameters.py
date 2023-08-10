from api import utils
from pprint import pprint
from itertools import product, chain

def params_to_single_obj(path):
   # in the ibge query builder api params assumes the order (agregados → periodos → variaveis → localidades)
   # so params is a list where [agregados, periodos, variaveis, localidades]
   objects = utils.read_objects(path)

   return objects

def build_params_list(object):
   params = list()
   for i in object.keys():
      temp = object[i]
      loop = utils.nested_dict_levels(temp)
      params.append(utils.combine_nested_dicts(loop, temp))
   
   combinations = list()
   for i in range(0, len(params) - 1):
      if i <= 0:
         combinations.append([
            list(map(list, product([x], [y])))[0] 
            for x in params[i] 
            for y in params[i + 1]
            ])
      else:
         combinations.append([
            list(map(list, product([x], [y])))[0] 
            for x in combinations[i - 1] 
            for y in params[i + 1]
            ])
   
   params_list = list()
   for i in combinations[-1]:
      print(i)
      loops = utils.nested_list_levels(i)
      dissolved = list()
      for j in range(0, loops - 1):
         if type(i) == "list":
            for k in i:
               dissolved.append(k)
         else:
            dissolved.append(i)
      pprint(dissolved)
      params_list.append(temp)
   
   pprint(params_list)
   print("\n")
