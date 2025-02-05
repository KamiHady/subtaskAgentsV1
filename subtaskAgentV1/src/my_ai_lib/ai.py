from langchain_community.llms import Ollama
import ollama
import helpers


# Simple function to access local models with a given prompt.
def prompt_model(model: str, prompt: str):
    llm = Ollama(model=model)
    response = llm.invoke(prompt)
    return response


# The same as def prompt() but for vision models. I recommend llava:7b.
def vision(model: str, prompt: str, img_path: str):
    result = ollama.chat(model=model,
                         messages=[
                             {'role': 'user',
                              'content': prompt,
                              'images': [img_path]
                              }
                         ]
                         )

    return result


# A function that extracts a binary answer out of a text given a topic:
# Example 1: The function returns "yes" if the TEXT is about seeing something and the TOPIC about vision.
# Example 2: The function return "no" if the TEXT is about food and the TOPIC rocket science.
# This function makes it easy to extract a binary (yes/no) answer from a complex input.
# llama3:8b is the basic config since it is quiet smart and fast.
def yes_no(text: str, topic: str):
    context_prompt = helpers.load_file('../data/texts/yes_or_no.txt')
    text_prompt = 'Now here is the text:'
    topic_prompt = "Now here os the topic:"
    prompt = context_prompt + text_prompt + '###' + text + '###' + topic_prompt + '$$$' + topic + '$$$'
    response = prompt_model('llama3:8b', prompt)

    if response.lower() == 'yes':
        return 'yes'

    elif response.lower() == 'no':
        return 'no'

    else:
        print(response)
        return 'I did not understand this, please try it again.'
