graph = {
    'n1': ['n2', 'n3', 'n4'],
    'n2': ['n5', 'n6'],
    'n3': ['n7', 'n8'],
    'n4': ['n9', 'n10'],
    'n5': ['n11', 'n12'],
    'n6': ['n13', 'n14'],
    'n7': ['n15', 'n16'],
    'n8': ['n17', 'n18'],
    'n9': ['n19', 'n20'],
    'n10': ['n21', 'n22']
}

for i in range(11, 23):
    graph['n'+str(i)] = None

values = {
    'n11': 3,
    'n12': 5,
    'n13': 6,
    'n14': 9,
    'n15': 1,
    'n16': 2,
    'n17': 0,
    'n18': -1,
    'n19': 7,
    'n20': 8,
    'n21': 2,
    'n22': 4
}

for i in range(1, 11):
    values['n'+str(i)] = None

def minimax(node, alpha, beta, ismax):
    if not graph[node]:
        return values[node]

    if ismax:
        best = float('-inf')
        for i in graph[node]:
            best = max(best, minimax(i, alpha, beta, 0))
            alpha = max(alpha, best)
            if alpha>=beta:
                print("yes")
                break

    else:
        best = float('inf')
        for i in graph[node]:
            best = min(best, minimax(i, alpha, beta, 1))
            beta = min(beta, best)
            if alpha>=beta:
                print("yes")
                break
    print(f"{node} : {best}")
    return best;

print(minimax('n1', float('-inf'), float('inf'), 1))