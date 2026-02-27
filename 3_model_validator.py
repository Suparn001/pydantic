from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    linkedin_url: AnyUrl
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return self   # ✅ MUST return self


def insert_patients_data(patient: Patient):
    print(patient)
    print(patient.age)
    print(patient.name)


patient_info = {
    'name': 'nitishu',
    'email': 'abc@hdfc.com',
    'linkedin_url': 'http://linkedin.com/',
    'age': '65',  # type coercion will convert to int
    'weight': 55.2,
    'married': True,
    'allergies': ['dust', 'pollen'],
    'contact_details': {
        'phone': '968574120',
        'emergency': '963215478'
    }
}

patient1 = Patient(**patient_info)

insert_patients_data(patient1)