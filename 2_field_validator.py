#field validator
from pydantic import BaseModel, EmailStr, AnyUrl,  Field, field_validator
from typing import List, Dict, Optional,Annotated


class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    linkedin_url:AnyUrl
    weight:float
    married:bool
    allergies:List[str]
    contact_details: Dict[str, str]

    @field_validator('email') # filed_validator is class method
    @classmethod
    def email_validator(cls,value):
        valid_list=['hdfc.com','icici.com']
        # abc@gmail.com
        domain_name  = value.split('@')[-1]

        if domain_name not in valid_list:
            raise ValueError('Not a valid domain')

        return value
    

    @field_validator('name', mode='after') # field validator works in two modes-> before mode and after mode, by default mode is after, if mode is after then value it will get after type coercion and if mode is before then it will get before type coercion 
    @classmethod      
    def transform_name(cls,value):
        return value.upper()


    @field_validator('age',mode='before') # this is before type co ercion because mode is before, for bypass use mode=after
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        return ValueError("age should e between 0 and 100")



def insert_patients_data(patient: Patient):
    print(patient)
    print(patient.age)
    print(patient.name)

patient_info = {
        'name':'nitishu',
        'email':'abc@hdfc.com',
        'linkedin_url':'http://linkedin.com/',
        'age':'30',
        'weight':55.2,
        'married':True,
        'allergies':['dust','pollen'],
        'contact_details':
            {
                'phone':'968574120'
            }
       }

patient1  = Patient(**patient_info) #  in this step vaidation checked, type coercion also checked


insert_patients_data(patient1)
