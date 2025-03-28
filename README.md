# Empathia.ai Interview
Task: Develop a Specialty Enhanced Consult Letter Generation Function for Medical Reports

Contains three files: `consult_letter.py` for prompting the generation of the consult letter, `test_consult_letter.py` for testing letter generation on an input, and `openai_chat.py` to import OpenAI and its chat functionalities.

## Generating the letter: 

The `create_consult_letter` function in `consult_letter.py` generates the consult letter using `chat_content` from `openai_chat.py`.

I relied entirely on prompting to generate the consult letter. I included instructions such as writing the letter in an email format and organizing it by SOAP.

Through testing the ```create_consult_letter``` function on input in ```test_consult_letter.py```, I fine-tuned the prompt to add instructions like including dates associated with past procedures and noting if any fields like physical examination or past surgical history were missing.

## **Running the test file**: 

Enter this line in the terminal to test ```create_consult_letter``` on a sample input in `test_consult_letter.py` (originally run on PyCharm):

```python3 -m  pytest -vv test_consult_letter.py```

