from pprint import pprint
import json
import glob
from api.classes.Loop import Loop

# receives a server response and print it's data as a idented object to clarifies view
def res_prettyfy(response):
   object = json.loads(response.text)
   pprint(object)

# receives api params and returns the constructed url to requests operations
def build_url(values, endpoint, names):
    
   # case generic url
   temp_url = ""
   api_url = ""

   for i in range(0, len(values)):
      temp_url = names[i] + str(values[i])
      api_url += temp_url

   # construct and return endpoint url
   return endpoint + api_url

# reads all json in the input path and save the values to a single dictionarie
def read_objects(path):
   objects = {}

   # method to find any .json in the path
   files = glob.glob(path + "\\*.json")

   for file in files:
      name = file.split("\\")[-1].split(".")[0]
      with open(file, "r", encoding="utf-8") as f:
         object = json.load(f)
         objects[name] = object

   # return the single object
   return objects

# extract the n levels of nested dicts
def nested_dict_levels(object):
   return max(nested_dict_levels(i) if isinstance(i, dict) else 0 for i in object.values()) + 1

# extract the n levels of nested lists
def nested_list_levels(nested_lists):
   return max(nested_list_levels(i) if isinstance(i, list) else 0 for i in nested_lists) + 1

def combine_nested_dicts(loop, object):
   for i in range(0, loop):
      if i == 0:
         old_keys = list()
         keys = list(object.keys())
         values = list(object.values())
         iteration = Loop(keys, values)
         combinations = iteration.combine_nested_levels()
      else:
         old_keys.append(iteration.keys)
         for key in iteration.keys:            
            iteration = Loop(object[key].keys(), object[key].values())
            iteration.old_keys = old_keys
         combinations = iteration.combine_nested_levels()

   return combinations
