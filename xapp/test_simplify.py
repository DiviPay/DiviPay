from simplify import Simplify
from random import randint

MAX_VERTICES = 50
MAX_EDGES = 100
MAX_WEIGHT = 100

NUM = randint(1, MAX_VERTICES)
EDGES = randint(NUM, MAX_EDGES)

while EDGES > (NUM*(NUM - 1))/2:
    EDGES = randint(NUM, MAX_EDGES)

nodes = [_ for _ in range(1, NUM + 1)]
l, edges = [], []

while EDGES:
    a = randint(1, NUM)
    b = randint(1, NUM)

    if a == b or (a, b) in l:
        continue
    l.append((a, b))
    amt = randint(1, MAX_WEIGHT)
    d = dict()
    d['lender'] = a
    d['borrower'] = b
    d['amount'] = amt
    edges.append(d)
    EDGES -= 1

for entry in edges:
    print('{} lends {} amount to {}'.format(entry['lender'], entry['borrower'], entry['amount']))

print('\n\n')

smp = Simplify(edges, nodes)
graph = smp.calculate()
for entry in graph:
    print('{} lends {} amount to {}'.format(entry['lender'], entry['borrower'], entry['amount']))
