from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import List,Dict, Optional, Annotated

# step 1 create model
class Patient(BaseModel):
    name:Annotated[str ,Field(max_length=50,title='Name of Subscriber',description='Give the name of patient in less then 50 chars',examples=['Nitish','Ajay'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int
    weight: Annotated[float,Field(gt=0,le=60, strict=True)] # strict = True mean, type coercin wont bethere, weight has o be float number, it cannot be string      
    married:Annotated[bool, Field(default=False,description='Is the patient married or not')]
    allergies:Annotated[Optional[List[str]], Field(default=None, description="allergies are optional", max_length=5)]  # List[str] this is used to check iin list every value is string, but if we use list, ths will validate like, list is there, but does not ensure, itcotains string of not but List[str]does that
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