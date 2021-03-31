from random import randint, seed


def mergesort(T):
  temp = [T[i] for i in range(len(T))]
  def merge(T, f, m, l):
    i = j = 0
    for k in range(f, l + 1):
      if (f + i) <= m and (m + 1 + j >= l + 1 or T[f + i] <= T[m + 1 + j]):
        temp[k] = T[f + i]
        i += 1
      else:
        temp[k] = T[m + 1 + j]
        j += 1
    
    for k in range(f, l + 1):
      T[k] = temp[k]
    

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