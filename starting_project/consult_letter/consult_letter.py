"""
Your task is to implement `create_consult_letter` function to generate a consult letter based on the SOAP note.

The input parameters are:
- user_info: a dictionary contains the bio of the doctor, such as
    {
        "name": "Dr. John Doe", # the name of the doctor
        "email": "drjohndoe@clinic.com", # the email of the doctor
    }
- specialty: a string represents the specialty of the doctor, such as "Obstetrics and Gynecology"
- note_content: a dictionary contains the content of the SOAP note, where the key is the section name and the value is the content of the section, such as
    {
        "Chief Complaint": "The patient is a 34-year-old G2P1 at 38 weeks gestation who presents for a routine prenatal visit.",
        "History of Present Illness": "The patient is a 34-year-old G2P1 at 38 weeks gestation who presents for a routine prenatal visit.",
        ...
    }
- note_date: a string represents the date of the SOAP note, such as "2022-01-01"
"""

import json
from typing import Optional

from openai_chat import chat_content


def create_consult_letter(
    user_info: dict, specialty: str, note_content: dict[str, Optional[str]], note_date: str
) -> str:
    """
    Your prompts here
    """