from api import utils
from requests import get

def get_data(values, endpoint, names):

   # define endpoint
   url = utils.build_url(values, endpoint, names)

   # send request and save response
   response_obj = get(url)

   # return response   
   return response_obj
