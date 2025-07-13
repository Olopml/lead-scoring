from pydantic import BaseModel, EmailStr

class LeadData(BaseModel):
    email: EmailStr
    sector: str
    country: str
    company_size: int
    website_visits: int