from tenacity import retry, wait_exponential
import datetime

@retry(wait = wait_exponential(multiplier=2, min=4, max=10))
def wait_exponential_1():
   print(datetime.datetime.now())
   raise Exception
   

wait_exponential_1()