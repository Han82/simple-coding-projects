# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  drink_temperature = get_temperature()
  name = input('Can I get your name, please? \n')
  print('Alright, that\'s a {} {} {}!'.format(size, drink_temperature, drink_type))
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

 

def print_message():
  print ("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
  res = input ("What size drink can I get for you? \n [a] Small \n [b] Medium \n [c] Large \n ")
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input ("What type of drink would you like? \n [a] Brewed Coffee \n [b] Mocha \n [c] Latte ")
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input ("And what kind of milk for your latte? \n [a] 2% milk \n [b] Non-fat milk \n [c] Soy milk ")
  if res == 'a':
    return '2% milk latte'
  elif res == 'b':
    return 'non-fat milk latte'
  elif res == 'c':
    return 'soy milk latte'
  else:
    print_message()
    return order_latte()


def get_temperature():
  res = input ("Would you like your drink hot or iced? \n [a] Hot \n [b] Iced ")
  if res == 'a':
    return 'hot'
  elif res == 'b':
    return 'iced'
  else:
    print_message()
    return get_temperature() 

# Call coffee_bot()!
coffee_bot()

