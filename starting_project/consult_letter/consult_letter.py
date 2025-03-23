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
    Using information about the doctor, specialty, the patient's SOAP note, and date, create a consult letter
    providing information about the referred patient's basic diagnosis, along with the treatment plan and recommendations.
    """
    result = chat_content(
        messages=[
            {
                "role": "system",
                "content": f"""You are a professional medical specialist who examined a patient from a referring Family Doctor, \
         you are given a dictionary containing the bio of the specialist doctor, including name and email, a String representing the specialty of the doctor, 
         a Dictionary with sections like "Chief Complaint," "History of Present Illness," etc., and a String representing the date of the note.
                - Generate an email-style Consult Letter from the specialist's perspective, covering the patient's diagnosis, treatment plan, and recommendations. The letter should focus on details mentioned in the note, including age, gender, symptoms, examination results, and treatment plan. The output should be consistent, error-free, and maintain a stable format across multiple function executions. The output must adhere to the convention of an email format, including the specialist’s sign-off.
                - Start by thanking the doctor for their referral of the patient and note the date of the examination. Then, mention their chief complaint and concisely describe their medical history, social history, or any history relevant to the patient. Be sure to note any allergies.
                - Describe any observations from the physical examination. Then, concisely describe the assessment and treatment plan. 
                - Remember to organize by paragraphs; do not use sub-headings. Do not use lists.
                - Include all important dates associated with previous procedures
                - If any information in the note contents like physical examination details, patient history, test results, estimated date of confinement, or past surgical history, is not provided, please indicate that in the letter.
                
                
                Example inputs and expected outputs:
                ""Patient Name": "Betty",
                "Chief Complaint": "Ear pain",
                "History of Present Illness": "\n• Left-sided ear pain\n• No drainage noted\n• Intermittent hearing loss reported\n• Pain worsens with chewing\n• Inconsistent use of mouthpiece for teeth clenching\n• Pain relief when lying on contralateral side",
                "Social History": "\n• Occasional Reactive use for allergies\n• Allergy to salt",
                "The Review of Systems": "\n• Intermittent hearing loss\n• No swallowing issues\n• No nasal congestion\n• Allergies present, takes Reactive occasionally",
                "Current Medications": "\n• Reactive for allergies",
                "Allergies": "\n• Allergic to salt",
                "Physical Examination": "\n• Right ear canal clear\n• Right tympanic membrane intact\n• Right ear space aerated\n• Left ear canal normal\n• Left eardrum normal, no fluid or infection\n• Nose patent\n• Paranasal sinuses normal\n• Oral cavity clear\n• Tonsils absent\n• Good dentition\n• Pain along pterygoid muscles\n• Heart and lungs clear\n• No neck tenderness or lymphadenopathy",
                "Assessment and Plan": "Problem 1:\nEar pain\nDDx:\n• Temporomandibular joint disorder: Likely given the jaw pain, history of teeth clenching, and normal ear examination.\nPlan:\n- Ordered audiogram to check hearing\n- Advised to see dentist for temporomandibular joint evaluation\n- Recommended ibuprofen for pain\n- Suggested soft foods diet\n- Avoid chewing gum, hard candies, hard fruits, ice, and nuts\n- Follow-up if symptoms persist"
                " -> "Thank you for your referral of Betty, for Otolaryngology Consultation. She was examined on January 1, 2022.

                Betty presented with a chief complaint of left-sided ear pain, which worsens with chewing and is relieved when lying on the contralateral side. She reports intermittent hearing loss and has a history of inconsistent use of a mouthpiece for teeth clenching. There is no past medical or surgical history reported. Betty has an allergy to salt and occasionally uses Reactive for allergies. Her social history includes occasional use of Reactive for allergies.

                Upon examination, the ear canals and tympanic membranes were found to be clear and normal, with no signs of fluid or infection. There was pain along the pterygoid muscles, but the heart and lungs were clear, and there was no neck tenderness or lymphadenopathy. No investigations have been recorded at this time.

                The assessment suggests a likely diagnosis of temporomandibular joint disorder, given the jaw pain, history of teeth clenching, and normal ear examination. The plan includes ordering an audiogram to check her hearing, advising a visit to the dentist for temporomandibular joint evaluation, recommending ibuprofen for pain, and suggesting a soft foods diet. She has been advised to avoid chewing gum, hard candies, hard fruits, ice, and nuts, and to follow up if symptoms persist.

                Please note that there is no obstetric history, test results, estimated date of confinement, or past surgical history provided in the SOAP note. Therefore, these details are not included in this consultation letter.

                If you have any further questions or require additional information, please do not hesitate to contact me at drjohndoe@clinic.com.

                Sincerely,

                Dr. John Doe
                Otolaryngology
                drjohndoe@clinic.com"
                """
            },
            {
                "role": "user",
                "content": f"""\
                Information about the patient is detailed as follows delimited by ```:
                ```
                {user_info}
                {specialty}
                {note_content}
                {note_date}
                ```
                """,
            },
        ])

    return result
