# when one model is used a s fiel in anothr model

from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str


class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict={'city':'gurgaon','state':'haryana','pin':'122001'}

address1 = Address(**address_dict)

patient_dic = {'name':'nitish','gender':'male','age':35,'address':address1}

patient = Patient(**patient_dic)

print(patient)

# better organization of related data
# resuability
# readablity
# validation