primes = [2,3,5,7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupitor', 'Saturn', 'Uranus', 'Neptune']
hands = [
    ['j', 'q', 'k'],
    ['2', '2', '2'],
    ['6', 'a', 'k'],
]
hands_again = [['j', 'q', 'k'], ['2', '2', '2'], ['6', 'a', 'k']]

my_favorite_thing = [32, 'raindrop on roses', help]
i=0
print(primes)
for i in range(4):
    print(primes[i])

print(primes[-1])
print(primes[-2])
print(planets)
print(hands[0])

#changing the list

planets[3] = 'Malacandra'
print(planets)
print(sorted(planets))

print(len(planets))

print(sum(primes))
print(max(primes))

#**************interclude:Objects*********
x=12
print(x.imag)
y= 12+3j
print((y.imag))

help(planets.append)

print(planets.index('Mercury'))

for planet in planets:
    print(planet, end=' ')
