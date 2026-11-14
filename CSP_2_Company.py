job = {
    'Cooking': ['C', 'D', 'E'],
    'Driving': ['B', 'D'],
    'Painting': ['B', 'D', 'E'],
    'Typing': ['A', 'C', 'D'],
    'Cleaning': ['B', 'D']
}

workers = ['A', 'B', 'C', 'D', 'E']

assigned = {
    'Cooking': None,
    'Driving': None,
    'Painting': None,
    'Typing': None,
    'Cleaning': None
}

jobs = ['Cooking', 'Driving', 'Painting', 'Typing', 'Cleaning']

visited = []

def check():
    for i in assigned:
        if not assigned[i]:
            return False
    return True

def csp(j):
    if check():
        return True
    for i in job[j]:
        if j == "Cleaning":
            if i not in visited:
                visited.append(i)
                assigned[j] = i
                return True
        else:

            if i not in visited:
                visited.append(i)
                assigned[j] = i

                if csp(jobs[(jobs.index(j)+1)]):
                    return True
                else:
                    visited.remove(i)
                    assigned[j] = None
    return False

csp('Cooking')
print(assigned)