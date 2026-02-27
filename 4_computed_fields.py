#computed field
#scenario is-> like we have weight and height in our model, so we can calculate bmi also on run ime so that bmi known as computed field
from pydantic import BaseModel, EmailStr, AnyUrl,computed_field
from typing import List, Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    linkedin_url:AnyUrl
    weight:float # kg
    height:float # meters
    married:bool 
    allergies:List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self)->float:   # here i named as calculate_bmi, so in model , yhi naam bn jaayega, so we will change to bmi
        bmi= round(self.weight/(self.height**2),2)
        return bmi





def insert_patients_data(patient: Patient):
    print(patient)
    print(patient.bmi)
    print(patient.age)
    print(patient.name)

patient_info = {
        'name':'nitishu',
        'email':'abc@hdfc.com',
        'linkedin_url':'http://linkedin.com/',
        'age':'30',
        'weight':55.2,
        'height':1.72,
        'married':True,
        'allergies':['dust','pollen'],
        'contact_details':
            {
                'phone':'968574120'
            }
       }

patient1  = Patient(**patient_info) #  in this step vaidation checked, type coercion also checked

insert_patients_data(patient1)
