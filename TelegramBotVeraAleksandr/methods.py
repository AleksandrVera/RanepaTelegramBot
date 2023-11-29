import random 

def greet():
    return "Приветик!"

def how_are_you():
  responses = ['Отлично', 'Все плохо:(', 'Ждал этого вопроса от тебя))))']
  return random.choice(responses)