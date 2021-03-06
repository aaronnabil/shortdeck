from shortdeck import Card, Evaluator, Deck

FD = Evaluator()
SD = Evaluator(game_variant='SHORT_DECK')
TR = Evaluator(game_variant='TRITON')
'''
h1 = []
h1.append(Card.new('Ac'))
h1.append(Card.new('6c'))

h2 = []
h2.append(Card.new('Kh'))
h2.append(Card.new('Kd'))

h3 = []
h3.append(Card.new('8h'))
h3.append(Card.new('9h'))

h4 = []
h4.append(Card.new('2h'))
h4.append(Card.new('2d'))

print(FD.equities(h1,h2,[]))
print(FD.equities(h1,h3,[]))
print(FD.equities(h1,h4,[]))
print(FD.equities(h2,h3,[]))
print(FD.equities(h2,h4,[]))
print(FD.equities(h3,h4,[]))
'''
'''
print('******full deck******')
print(FD.equities(myhand,ophand,[]))

print('******short deck******')
print(SD.equities(myhand,ophand,[]))

print('******triton******')
print(TR.equities(myhand,ophand,[]))
'''
b = []
boat = []
boat.append(Card.new('Jc'))
boat.append(Card.new('Ts'))
boat.append(Card.new('9d'))
boat.append(Card.new('8c'))
boat.append(Card.new('7d'))

flush = []
flush.append(Card.new('8s'))
flush.append(Card.new('8h'))
flush.append(Card.new('8c'))
flush.append(Card.new('9c'))
flush.append(Card.new('Jc'))

print(FD.evaluate(boat,b))
print(SD.evaluate(boat,b))
print(TR.evaluate(boat,b))

print(FD.evaluate(flush,b))
print(SD.evaluate(flush,b))
print(TR.evaluate(flush,b))


'''
print(FD.evaluate(boat,[]))
print(FD.evaluate(flush,[]))

print(SD.evaluate(boat,[]))
print(SD.evaluate(flush,[]))

print(TR.evaluate(boat,[]))
print(TR.evaluate(flush,[]))
'''
p1 = []
p2 = []

p1.append(Card.new('8c'))
p1.append(Card.new('8h'))

p2.append(Card.new('9d'))
p2.append(Card.new('Jh'))

b.append(Card.new('8s'))
b.append(Card.new('7d'))
b.append(Card.new('Tc'))


print(SD.equities(p2,p1,b))
#print(TR.equities(p1,p2,b))
