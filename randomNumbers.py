import random 


greetings = ['Hello', 'Hi', 'Hola', 'Ola', 'Namastey']
value = random.choice(greetings) #Returns a random element/choice from the given sequence/ list
print(value + ' Roshan!')

colors = ['Red', 'Black', 'Green']
results = random.choices(colors, weights= [18, 18, 2], k=10) # K = how many time we want to pick a value, 
# weight: what we want to weigh eg: what are the odds that green will appear 
print(results)

print(random.randrange(1,100)) # Returns a random number between the given range

value = random. random() #random method is used to get random value between 0(inclusive) and 1(non- inclusive)
print (value)

value = random.uniform(1, 10) # Returns a random float number between two given parameters
print (value)

value = random.randint(1, 6) # Returns a random number between the given range
print (value)



deck = list(range(1, 53)) #1 is inclusive and 53 is exclusive
random.shuffle(deck) # Takes a sequence/list and returns the sequence in a random order
print(deck)

hand = random.choices(deck, k = 5)  # Cannot use choice to generate unique set of 5 cards so we use sample method
print(hand)

hand = random.sample(deck, k=5) #returns unique samples of sequence
print(hand)