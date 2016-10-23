from operator import itemgetter
class Simplify(object):

    def __init__(self, graph, users):
        self.graph = graph
        self.users = users

    def calculate(self):
        money = dict()
        for user in self.users:
            money[user] = 0

        for entity in self.graph:
            amount = entity['amount']
            money[entity['lender']] -= amount
            money[entity['borrower']] += amount

        new_graph, mney = list(), list()
        for key, value in money.items():
            mney.append([key, value])

        mney.sort(key=itemgetter(1))
        i, j = 0, len(mney) - 1
        while i < j:
            entry = dict({
                'lender': mney[i][0],
                'borrower': mney[j][0]
            })
            if abs(mney[i][1]) > abs(mney[j][1]):
                entry['amount'] = abs(mney[j][1])
                mney[i][1] += mney[j][1]
                mney[j][1] = 0
                j -= 1
            else:
                entry['amount'] = abs(mney[i][1])
                mney[j][1] += mney[i][1]
                mney[i][1] = 0
                i += 1
            if entry['amount'] == 0:
                continue
            new_graph.append(entry)

        return new_graph
