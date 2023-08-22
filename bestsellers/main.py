from typing import List
from scrapy.cmdline import execute
from bestsellers.bestsellers_urls import BESTSELLERS_URLS

bestsellers_keys = list(enumerate(BESTSELLERS_URLS.keys()))

def gen_options():
    options = ''
    for index, value in bestsellers_keys:
        options += f"[{index}] {value}\n"
    return options
        
MESSAGE = f'''Select the categories, separated by spaces
{gen_options()}
'''

def get_user_input() -> List[int]:
    valid_values = [i for i in range(0, len(bestsellers_keys) + 1)]
    user_input = input(MESSAGE)
    while not user_input:
        user_input = input(MESSAGE)
    user_input = user_input.split(' ')
    try:
        values = [int(val) for val in user_input if val.isdigit() and int(val) in valid_values]
        if not values: raise Exception('Invalid Input')
        return values
    except Exception as e:
        raise e


def get_arg(user_input: List[int]) -> str:
  args: List[str] = []
  for index in user_input:
      try:
          args.append(bestsellers_keys[index][1])
      except Exception as e:
          return e
  return f"categories={','.join(args)}"


if __name__ == "__main__":
    try:
        user_input = get_user_input()
        args = get_arg(user_input)
        print(args)
        execute(["scrapy", "crawl", "amazon_bestsellers", "-a", args])
    except Exception as e:
        print(e)


