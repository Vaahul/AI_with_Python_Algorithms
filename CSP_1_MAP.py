# Map coloring

graph = {
    'KA': ['GA', 'MH', 'TG', 'AP', 'TN', 'KL'],
    'GA': ['KA', 'MH'],
    'MH': ['KA', 'GA', 'TG'],
    'TG': ['KA', 'MH', 'AP'],
    'AP': ['KA', 'TG', 'TN'],
    'TN': ['KA', 'AP', 'KL'],
    'KL': ['KA', 'TN']
}

states = ['KA', 'GA', 'MH', 'TG', 'AP', 'TN', 'KL']
colors = ['Red', 'Green', 'Blue']

color = {
    'KA': None,
    'GA': None,
    'MH': None,
    'TG': None,
    'AP': None,
    'TN': None,
    'KL': None
}

def check(node, col):
    flag = True
    for i in graph[node]:
        if col and color[i] == col:
            flag = False
    return flag

def finish():
    flag = True
    for i in color:
        if not color[i]:
            flag = False
    return flag

def csp(state):
    for col in colors:
        if check(state, col):
            color[state] = col
            for neigh in graph[state]:
                if not color[neigh]:
                    if csp(neigh):
                        return True
                    else:
                        color[state] = None
                        break
    if finish():
        return True
    return False

print(csp('KA'))
print(color)