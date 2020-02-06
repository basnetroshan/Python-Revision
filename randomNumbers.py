import random 

greetings = ['Hello', 'Hi', 'Hola', 'Ola', 'Namastey']
value = random.choice(greetings) #Returns a random element/choice from the given sequence/ list
print(value + ' Roshan!')

colors = ['Red', 'Black', 'Green']
results = random.choices(colors, k=10)
print(results)

print(random.randrange(1,100)) # Returns a random number between the given range

value = random. random() #random method is used to get random value between 0(inclusive) and 1(non- inclusive)
print (value)

value = random.uniform(1, 10) # Returns a random float number between two given parameters
print (value)

value = random.randint(1, 6) # Returns a random number between the given range
print (value)