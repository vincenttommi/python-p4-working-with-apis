import requests
import json


# requests is a Python library
# that allows your program 
# or application to send HTTP requests.


class GetPrograms:
  
  def get_programs():
    # we use the JSON library to parse the API response into nicely formatted JSON
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
      
     
    response  = requests.get(URL)
    return response.content
   
   
   
   
  def  program_school(self):
    
    programs_list = []
    programs =(self.get_programs())
    for program in programs:
      #introducing a loop that iterates over the variable programs and that  using append method to append it to program list
      # programs_list.append(program["agency"])
      programs_list.append(program["agency"])
      
    return programs_list
    #returning program_list to give out an output
    
programs = GetPrograms()
programs_schools=programs.program_school()
    
for school  in set(programs_schools):
  print(school)


    
   
# Programs  = GetPrograms.get_programs()
# # get_programs method that uses the
# # requests library to send an HTTP request 
# # from our program.
# print(Programs)

   

     
   