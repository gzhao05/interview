from consult_letter import create_consult_letter
from openai_chat import chat_content


def test_betty():
    consult_letter = create_consult_letter(
        user_info={"name": "Dr. John Doe", "email": "drjohndoe@clinic.com"},
        specialty="Otolaryngology",
        note_date="2022-01-01",
        note_content={
            "Patient Name": "Betty",
            "Chief Complaint": "Ear pain",
            "History of Present Illness": "\n• Left-sided ear pain\n• No drainage noted\n• Intermittent hearing loss reported\n• Pain worsens with chewing\n• Inconsistent use of mouthpiece for teeth clenching\n• Pain relief when lying on contralateral side",
            "Social History": "\n• Occasional Reactive use for allergies\n• Allergy to salt",
            "The Review of Systems": "\n• Intermittent hearing loss\n• No swallowing issues\n• No nasal congestion\n• Allergies present, takes Reactive occasionally",
            "Current Medications": "\n• Reactive for allergies",
            "Allergies": "\n• Allergic to salt",
            "Physical Examination": "\n• Right ear canal clear\n• Right tympanic membrane intact\n• Right ear space aerated\n• Left ear canal normal\n• Left eardrum normal, no fluid or infection\n• Nose patent\n• Paranasal sinuses normal\n• Oral cavity clear\n• Tonsils absent\n• Good dentition\n• Pain along pterygoid muscles\n• Heart and lungs clear\n• No neck tenderness or lymphadenopathy",
            "Assessment and Plan": "Problem 1:\nEar pain\nDDx:\n• Temporomandibular joint disorder: Likely given the jaw pain, history of teeth clenching, and normal ear examination.\nPlan:\n- Ordered audiogram to check hearing\n- Advised to see dentist for temporomandibular joint evaluation\n- Recommended ibuprofen for pain\n- Suggested soft foods diet\n- Avoid chewing gum, hard candies, hard fruits, ice, and nuts\n- Follow-up if symptoms persist"
        }
    )

    result = chat_content(
        messages=[
            {
                "role": "system",
                "content": f"You are a professional medical assistant of Otolaryngology, \
your job is to verify the content of consult letter",
            },
            {
                "role": "user",
                "content": f"""\
The consult letter is as following, delimited by ```:
```
{consult_letter}
```
""",
            },
            {
                "role": "user",
                "content": f"""\
Follow these test points when verify the consult letter:
- The letter shall have doctor's name "John Doe"
- The letter shall mention patient name as Betty, and the encounter happened at 2022/01/01
- ТThe Patient has a salt allergy. The patient uses Reactive for her allergies.
- The plan suggests a soft food diet. The plan recommends a follow up if symptoms persist
""",
            },
            {
                "role": "user",
                "content": "Write me PASS **ONLY** if the consult letter is correct, and FAIL with reason if not",
            },
        ]
    )
    print(consult_letter)
    assert result.upper() == "PASS"


test_betty()
