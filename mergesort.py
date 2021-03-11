from random import randint, seed


def mergesort(T):
  def merge(T, f, m, l):
    L = T[f:m + 1]
    R = T[m + 1: l + 1]
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = j = 0
    for k in range(f, l + 1):
      if L[i] <= R[j]:
        T[k] = L[i]
        i += 1
      else:
        T[k] = R[j]
        j += 1
    

  #f - first element, mid - middle element, l - last element
  def sort(T, f=0, l=len(T) - 1):
    if f < l:
      m = (f + l)//2
      sort(T, f, m)
      sort(T, m + 1, l)
      merge(T, f, m, l)

  sort(T)
  return T
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")