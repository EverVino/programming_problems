def solution(pivot_index, A):
    print("test Case")
    print(A, pivot_index)

    pivot = A[pivot_index]
    i, j = 0, len(A) - 1 
    A[pivot_index], A[i] = A[i], A[pivot_index]
    i += 1 
    while i < j:
        if A[i] <= pivot:
            i += 1
        else:
            A[i], A[j] = A[j], A[i]
            j -= 1

    A[0], A[i-1] = A[i-1], A[0]
    print('Result')
    print(A)
    return A

