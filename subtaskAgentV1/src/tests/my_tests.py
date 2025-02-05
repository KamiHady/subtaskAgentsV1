import my_ai_lib


# Some simple tests to show some of the functionality of the ai.py library
def yes_no_test():
    print('Assert YES: ' + my_ai_lib.yes_no("Do you see that?", "vision"))
    print('Assert NO: ' + my_ai_lib.yes_no("Wow did you cook als this food?", "rocket science"))
    print('Assert YES: ' + my_ai_lib.yes_no("Green, blue, yellow, orange and red tshirts? wow that great!",
                                            "colors"))
    print('Assert NO: ' + my_ai_lib.yes_no("A big lion is crossing the street", "social science"))


def vision_test():
    print('Assert a description tropical island: ')
    print(my_ai_lib.vision("llava:7b", "describe what you see", "../data/images/img1.png")['message']['content'])
