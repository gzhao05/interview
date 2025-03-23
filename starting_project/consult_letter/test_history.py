from consult_letter import create_consult_letter
from openai_chat import chat_content


def history_paragraph(note):
    result = chat_content(
        messages=[
            {
                "role": "system",
                "content": f"You are a professional medical specialist who examined a patient from a referring Family Doctor, \
 your job is to write a paragraph concisely detailing the patient's past medical and surgical history, family and social history,\
 obstretic history, and any other kind of relevant health-related history.",
            },
            {
                "role": "user",
                "content": f"""\
Information about the history is detailed as follows delimited by ```:
```
{note}
```
""",
            },
        ])
    print(result)
    return result


# Test input
test_note = [None,
             'The patient had COVID-19 in 2021, after which she experienced heart pain, but subsequent evaluations by her family doctor and hospital visits confirmed that everything was okay.',
             'The patient had a cesarean section in 2019 and an abortion due to a fetal health issue.',
             None,
             "Jane is employed part-time as a banker, working two to three days per week. She and her spouse reside in a non-specified location without nearby family support. However, they have a local friend network. Postpartum, Jane's mother will assist, and they intend to employ a babysitter for two months.",
             'The patient is currently pregnant with her third child. She has had one previous live birth via cesarean section and one abortion due to fetal health issues. Her first child was born slightly premature at approximately 37 weeks, weighing 2.5 kilograms.',
             'The patient reports no asthma, heart problems, seizures, or migraines. She has experienced chest pain post-COVID-19 but has been evaluated and found to be in good health. She is currently active, engaging in pregnancy yoga once a week and walking when she feels able.',
             'The patient reports no asthma, heart problems, seizures, or migraines. She has experienced chest pain post-COVID-19 but has been evaluated and found to be in good health. '
             'She is currently active, engaging in pregnancy yoga once a week and walking when she feels able.']


# Run function with test input
history_paragraph(test_note)