from simple_calculator import *
import requests
print("Imported ",div(20,50))

def say_hobbies(**hobbies):
    for hb in hobbies:
        print(hb,":", hobbies[hb])
    
say_hobbies(one="Reading", two="Traveling", three="Watching move",four="Writing")

response = requests.get('https://docs.python.org/',timeout=5)
print(response.status_code)