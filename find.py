def binary_search(element, vetor, steps = 0):
    metade = int(len(vetor)/2)
    steps+=1
    if element < vetor[metade]:
        return binary_search(element, vetor[:metade], steps)
    elif element > vetor[metade]:
        return binary_search(element, vetor[metade:], steps)
    else:
        return steps


def index_search(element, vetor):
    i = 0
    steps = 0
    index = []
    while i < 105:
        index.append(vetor[i])
        if element < vetor[i]:
            break
        steps += 1
        i+=7
    pos = 0
    metade = int(len(index) / 2)

    for i in index:
        if element < i:
            break
        elif element == i:
            return 1
        else:
            pos+=1

    for v in vetor[(pos*7)-7:pos*7]:
        if v == element:
            return steps
        steps+=1