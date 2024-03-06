import os
import sys
import openai
import json

import base64

def main(key, model_task, theme):
    openai.api_key = key

    with open(model_task, "r") as file:
        model = file.read()
        file.close()    
    
    # Call openai api to generate question
    # See: https://platform.openai.com/docs/guides/chat/introduction for more information on the call
    
    debug = False
    if debug:
        sys.stdout.write("This is a test\nWith a new line")
    else:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a teacher that wants to help a student by extending their programming task with a new exercise. Here is their overall task:"},
                {"role": "assistant", "content": model},
                {"role": "assistant", "content": "Provide an exercise that builds upon the original series of exercises and but has the following theme:"},
                {"role": "assistant", "content": theme},
                {"role": "assistant", "content": "Format the exercise in markdown and make sure it is a valid JSON string"},
            ]
        )
        fix_apostrophe = response.choices[0]['message']['content'].replace("\'","'")
        remove_quotes = json.dumps(fix_apostrophe)[1:-1]
        print(remove_quotes)

    # Test write
    f = open("testOutput.txt", "w")
    f.write(remove_quotes)
    f.close()
    
    
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])