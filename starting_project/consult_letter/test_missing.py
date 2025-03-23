from openai_chat import chat_content


def get_missing(note):
    """
    Please note that there is no obstetric history, test results, estimated date of confinement, or past surgical history provided in the SOAP note.
    Therefore, these details are not included in this consultation letter.
    """
    missing = []
    for key in note:
        if note[key] is None:
            missing.append(key)
    print(missing)

    result = chat_content(
        messages=[
            {
                "role": "system",
                "content": f"""
                You are a professional medical specialist who examined a patient from a referring Family Doctor, \
         you are given a list of items that were missing from the patient's information and should generate a sentence explaining which items were missing",

                Example inputs and expected outputs:
                "["Obstetric history", "Test Results", "Estimated date of confinement", "Past surgical history"] -> "Please note that there is no obstetric history, test results, estimated date of confinement, or past surgical history provided in the SOAP note. Therefore, these details are not included in this consultation letter."
                """
            },
            {
                "role": "user",
                "content": f"""\
                Information about the patient is detailed as follows delimited by ```:
                ```
                {missing}
                ```
                """,
            },
        ])
    print(result)
    return result

test_note = {"Current Medications": None,
            "Allergies": None,
            "Vital Signs": None,
            "Physical Examination": None,
            "Investigations": None,
            "Problem": "1. Previous cesarean section (654.21)",
            "Differential Diagnosis": None}

# Run function with test input
get_missing(test_note)