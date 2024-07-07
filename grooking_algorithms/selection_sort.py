
def arrange_min_to_max(array):
    for i in range(len(array)):  # This loop iterates over the total lenght of the list
        min_index = i  # This variable tests the minimum value that will be changed over the below iteration

        for j in range(i+1, len(array)):  # This is a second loop iteration that makes sure all values are compared
            # on every arrangement
            if array[j] < array[min_index]:  # This finds along the iteration the minimum value, starting from the
                # next value that was previpously arranged on the prior iteration
                min_index = j  # Assign the index of the value every time a lesser value is found.

        array[i], array[min_index] = array[min_index], array[i]  # This swaps the values sorting them in order

    return array  # Returns the array sorted


lista = [5,12,8,1,10,14,7,3,6,15,4,11,2,13,9]

print(arrange_min_to_max(lista))

