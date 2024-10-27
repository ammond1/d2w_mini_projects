

def merge(array: list, p: int, q: int, r: int) -> None:
    nleft = q - p+1
    nright = r-q
    left = 0
    right = 0
    dest = p
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    while left<nleft and right<nright:
        if left_array[left] <= right_array[right]:
            array[dest] = left_array[left]
            left+=1
        else:
            array[dest] = right_array[right]
            right+=1
        dest +=1
    while left<nleft:
        array[dest] = left_array[left]
        left+=1
        dest+= 1
    while right<nright:
        array[dest] = right_array[right]
        right+=1
        dest+=1
    return array
        

def mergesort_recursive(array: list, p: int, r: int) -> None:
    if r-p ==0:
        return array
    elif r-p > 0:
        q = int((p+r)/2)
        mergesort_recursive(array,p,q)
        mergesort_recursive(array,q+1,r)
        merge(array, p,q,r)
        return array
        

def mergesort(array: list , byfunc = None) -> None:
    p = 0 
    r = len(array)-1
    if byfunc == None:
        mergesort_recursive(array,p,r)
        return array
    else:
        ls = []
        n_array = []
        for i in range(len(array)):
            ls.append(byfunc(array[i]))
        mergesort_recursive(ls,p,r)
        for i in range(len(ls)):
            n_array += [n for n in array if byfunc(n) == ls[i]]
        array[:] = n_array
        return array
    




class Stack:
  pass

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





