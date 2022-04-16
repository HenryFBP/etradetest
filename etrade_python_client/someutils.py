from typing import Dict, Any, Union


def user_choose_dict(
        d=None,
        prompt: str = "Please choose:",
        quitkey: str = 'q',
        invalidmsg: str = "Invalid choice."
) -> Union[Any, None]:
    if d is None:
        d = {1: 'apple', '2': 'banana', 3: 'potato'}

    while True:
        for k in d.keys():
            v = d[k]
            print("- [{:^3s}] {}".format(k, v))
        selection = input(
            prompt +
            (" ({} to quit)".format(quitkey) if quitkey else '') +
            "\n > "
        )
        if quitkey and (selection == quitkey):
            return None

        if selection in d.keys():
            return d[selection]
        else:
            print(invalidmsg)
