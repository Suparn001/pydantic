# export model in json or dictionary

from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str


class Patient(BaseModel):
    name:str
    gender:str='Male'
    age:int
    address:Address

address_dict={'city':'gurgaon','state':'haryana','pin':'122001'}

address1 = Address(**address_dict)

patient_dic = {'name':'nitish','age':35,'address':address1}

patient = Patient(**patient_dic)


temp=patient.model_dump() # existing pydantic model object to python dic

print(temp)
print(type(temp))


temp3=patient.model_dump(exclude_unset=True) # exclude_unset it removed those whose value is not set

print(temp3)
print(type(temp3))

# # if i need to export particular field then use includes, or if if you want to exclude particular field then use exclude
# temp=patient.model_dump(include=['name'])
# print(temp)
# print(type(temp))

# #exclude
# temp1=patient.model_dump(exclude=['name'])
# print(temp1)
# print(type(temp1))

# #exclude
# temp2=patient.model_dump(exclude={'address':['state']})
# print(temp2)
# print(type(temp2))

# # temp1=patient.model_dump_json() # existing pydantic model object to json and here it is string
# # print(temp1)
# # print(type(temp1))
