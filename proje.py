# ^1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten_list(lst):
    flattened_list= []
    for item in lst:
        if type(item) == list:
            flattened_list.extend(flatten_list(item))
        else :
            flattened_list.append(item)
            
            
    return flattened_list

print(flatten_list(liste))


# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

liste= [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list_elements(input_list):
     reversed_list = []
     for element in input_list:
         if type(element) == list:
             reversed_sublist = reverse_list_elements(element)
             reversed_list.append(reversed_sublist)
         else:
             reversed_list.append(element)
     return list(reversed(reversed_list))


reverse_list_elements(liste)
