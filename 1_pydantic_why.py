from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import List,Dict, Optional

# step 1 create model
class Patient(BaseModel):
    name:str =  Field(max_length=50)
    email:EmailStr
    linkedin_url:AnyUrl
    age:int
    weight:float= Field(gt=0,le=60)
    married:bool =False #this is default value
    allergies:Optional[List[str]] =None # List[str] this is used to check iin list every value is string, but if we use list, ths will validate like, list is there, but does not ensure, itcotains string of not but List[str]does that
    contact_details:Dict[str,str]


def insert_patients_data(patient: Patient):
    print(patient)
    print(patient.age)
    print(patient.name)



patient_info = {
        'name':'nitishuuuuuuuuuuuuuuuuuu',
        'email':'abc@gmail.com',
        'linkedin_url':'http://linkedin.com/',
        'age':30,
        'weight':55.2,
        'married':True,
        'allergies':['dust','pollen'],
        'contact_details':
            {
                'phone':'968574120'
            }
       }         

# step 2
patient1 = Patient(**patient_info)

insert_patients_data(patient1)