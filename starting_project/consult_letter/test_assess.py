from openai_chat import chat_content

def get_assess(note):
    result = chat_content(
        messages=[
            {
                "role": "system",
                "content": f"""
                    You are a professional medical specialist who examined a patient from a referring Family Doctor, \
                    you are given information about the patient's assessment and plan and should summarize the information \
                    into a concise paragraph.
                    
                    Example input and expected output:
                    ""Assessment and Plan": "Problem 1:\nEar pain\nDDx:\n• Temporomandibular joint disorder: Likely given the jaw pain, history of teeth clenching, and normal ear examination.\nPlan:\n- Ordered audiogram to check hearing\n- Advised to see dentist for temporomandibular joint evaluation\n- Recommended ibuprofen for pain\n- Suggested soft foods diet\n- Avoid chewing gum, hard candies, hard fruits, ice, and nuts\n- Follow-up if symptoms persist" ->  "The assessment suggests a likely diagnosis of temporomandibular joint disorder, given the jaw pain, history of teeth clenching, and normal ear examination. The plan includes ordering an audiogram to check her hearing, advising a visit to the dentist for temporomandibular joint evaluation, recommending ibuprofen for pain, and suggesting a soft foods diet. She has been advised to avoid chewing gum, hard candies, hard fruits, ice, and nuts, and to follow up if symptoms persist."
                    """
            },
            {
                "role": "user",
                "content": f"""\
                    Information about the patient is detailed as follows delimited by ```:
                    ```
                    {note}
                    ```
                    """,
            },
        ])
    print(result)
    return result


test_note = ["• Scheduled repeat cesarean section at 39 weeks gestation",
"• Instructed patient to present to City Medical Center for emergency cesarean section if labor begins prior to scheduled date",
"• Advised patient to walk daily for 20 to 30 minutes to improve blood pressure and baby's health",
"• Arranged follow-up appointment in three weeks, with subsequent visits every two weeks, then weekly as due date nears"
]

other_note = {"Assessment and Plan": "Problem 1:\nLung pain\nDDx:\n• Cystic fibrosis: Likely given the lung pain, history of breathing problems, and normal lung examination.\nPlan:\n- Ordered cardiogram to check heartbeats\n- Advised to see lung expert for cystic fibrosis evaluation\n- Recommended ibuprofen for pain\n- Suggested soft foods diet\n- Avoid tough exertion like volleyball, frisbee, and marathons\n- Follow-up if symptoms persist"}

# Run function with test input
get_assess(other_note)