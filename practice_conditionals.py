# the exercise in conditionals
# by @stevemeisterr
# 
# 2021 - 03 - 23 #

print('Hi, how the heck are ya?')
response = input('Respond...')

if response.startswith("I'm great"):
    greeting = "Well, fuck you then! "
elif response == "I'm grreat!":
    greeting = "Well if it isn't Tony the FUCKING Tiger.. "
else:
    greeting = "Well if you're not having a good day, I hope it get's better soon. "

greeting = greeting + '\n'
message = greeting + 'Anyway... \n' + 'Have a good one!'

print(message)
