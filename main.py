from api import requests, utils, parameters
from dotenv import load_dotenv
import os
import json

def main():

   # enable env variables load
   load_dotenv()

   # params definition
   params_path = os.getenv("PARAMS_PATH")  # get location to the json with api parameters
   params_object = parameters.params_to_single_obj(params_path)
   params_values = parameters.build_params_list(params_object)

   # api requests
   for i in params_values:
      endpoint = os.getenv("ENDPOINT")
      params_names = json.loads(os.getenv("PARAMS_NAMES"))
      response = requests.get_data(i, endpoint, params_names)
      utils.res_prettyfy(response)

      # mongodb loadout through looping
      """feature = ""
      for i in len(data):
         print("Loading feature {%s}".format(feature) + " {%d}".format(i/len(data)))   """
   
if __name__ == "__main__":
   main()
