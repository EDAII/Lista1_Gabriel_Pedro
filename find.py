def binary_search(element, vetor, steps = 0):
    print(vetor)
    metade = int(len(vetor)/2)
    steps+=1
    if element < vetor[metade]:
        return binary_search(element, vetor[:metade], steps)
    elif element > vetor[metade]:
        return binary_search(element, vetor[metade:], steps)
    else:
        return steps