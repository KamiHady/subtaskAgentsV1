import datetime
import my_ai_lib
import helpers
from tqdm import tqdm

# See: subtask_agent_v1.png

# Meta data for the agent: The files to prompt the different models
instruction_prompt = helpers.load_file('../data/texts/split_instruction.txt')
clear_answers = helpers.load_file('../data/texts/clear_answers.txt')


def subtask_agent_v1(prompt: str, model: str = 'llama3:8b'):
    # The prompt of the split instruction.
    instructed_prompt = instruction_prompt + prompt

    # The splitted answer or the subtasks written like:
    # Subtask 1: ...
    # Subtask 2: ...
    # Subtask 3: ...
    splitted_prompt = my_ai_lib.prompt_model(model=model, prompt=instructed_prompt)

    # Splitting and saving the subtasks in a list.
    subtasks = [subtask.strip() for subtask in splitted_prompt.split('$') if subtask.strip()]

    # Empty solution initialization
    solution = ''

    for j in tqdm(range(len(subtasks))):
        if j == 0:
            think_deep = 'You are part of a multilevel decision process. The above goal is: ' \
                         + prompt + ' And your part in this process is it to solve the subtask: ' + subtasks[0] + \
                         '.' + clear_answers

            # Formatting the answers to workable .md
            first_round = my_ai_lib.prompt_model(model=model, prompt=think_deep)
            solution = solution + '# ' + subtasks[0] + '\n' + first_round + '\n\n'

        else:
            think_deep_i = 'You are part of a multilevel decision process. The above goal is: ' \
                           + prompt + ' And your part in this process is it to solve the subtask: ' + subtasks[j] + \
                           '.' + clear_answers

            # Formatting the answers to workable .md
            i_round = my_ai_lib.prompt_model(model=model, prompt=think_deep_i)
            solution = solution + '# ' + subtasks[j] + '\n' + i_round + '\n\n'

    helpers.save_as_md('subtask_agent_v1: ' + model + ' ' + prompt + ' ' + str(datetime.datetime.now()) + '.md', '../results', solution)

    print('Saved successfully')
