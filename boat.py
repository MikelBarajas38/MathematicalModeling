import random

in_dist = [0.13, 0.17, 0.15, 0.25, 0.20, 0.10]
out_dist = [0.05, 0.15, 0.5, 0.2, 0.1]

in_acum = None
out_acum = None

def get_acum(dist):

    acum = []
    acum.append(in_dist[0])

    for i in range(1, len(dist)):
        acum.append(acum[i-1] + dist[i])

    return acum


def match_dist(x, dist):

    for i in range(len(dist)):
        if x < dist[i]:
            return i
        
    return len(dist)

def get_state(qi):

    rand_a = random.random()
    rand_b = random.random()

    ins = match_dist(rand_a, in_acum)
    out = match_dist(rand_b, out_acum) + 1

    qs = qi + ins - out
    qs = max(0, qs)

    return [qi, ins, out, qs]


in_acum = get_acum(in_dist)
out_acum = get_acum(out_dist)

curr = 0
for i in range(10):
    line = get_state(curr)
    print(line)
    curr = line[3]
