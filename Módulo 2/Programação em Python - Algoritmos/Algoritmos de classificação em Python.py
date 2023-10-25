# Insertion Sort

# def insertion_sort(arr, n):
#     for i in range(1, n):

#         current_position = i
#         current_element = arr[i]

#         while current_position > 0 and current_element < arr[current_position -1]:
#             arr[current_position] = arr[current_position -1]
#             current_position -= 1

#         arr[current_position] = current_element


# arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
# insertion_sort(arr, 9)

# print(str(arr))



# Selection Sort

# def selection_sort(arr, n):
#     for i in range(n):

#         min_element_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_element_index]:
#                 min_element_index = j
        
#         arr[i], arr[min_element_index] = arr[min_element_index], arr[i]

# arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
# selection_sort(arr, len(arr))
# print(arr)



# Bubble Sort

# def bubble_sort(arr, n):
#     for i in range(n):
#         # (n - i - 1) ignora os últimos elementos pois a medida que o codigo avança os ultimos elementos já vão se oorganizando.
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
# bubble_sort(arr, len(arr))
# print(arr)



# Merge Sort

def merge(arr, left_index, mid_index, right_index):
    left_array = arr[left_index:mid_index+1]
    right_array = arr[mid_index+1:right_index+1]

    left_array_length = mid_index - left_index + 1   
    right_array_length = right_index - mid_index

    i = j = 0

    k = left_index

    while i < left_array_length and j < right_array_length:
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1
    
    while i < left_array_length:
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < right_array_length:
        j += 1
        k += 1

def merge_sort(arr, left_index, right_index):
    if left_index >= right_index:
        return
    mid_index = (left_index + right_index) // 2

    merge_sort(arr, left_index, mid_index)
    merge_sort(arr, mid_index + 1, right_index)

    merge(arr, left_index, mid_index, right_index)


arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
merge_sort(arr, 0, 8)

print(arr)