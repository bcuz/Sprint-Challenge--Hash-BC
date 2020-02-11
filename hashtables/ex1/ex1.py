#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
            hash_table_insert,
            hash_table_remove,
            hash_table_retrieve,
            hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):
  ht = HashTable(16)

  for i in range(len(weights)):
    hash_table_insert(ht, i, weights[i])

  # # it overwrites the weight, tho, if there's a dup
  # # as it should. like the advice is flipped..
  # for i in range(len(ht.storage)):
  #   if ht.storage[i] != None:
  #     print(ht.storage[i].key, hash_table_retrieve(ht, ht.storage[i].key))

  # the keys in the hash arent order like the are in the arr.
  # the largest index has to go first.

  # print(ht.storage)

  counter = 0
  counter2 = 0
  total = 0
  values = [None] * 2
  while True:
    if len(weights) == 1:
      return None

    if counter == len(weights):
      counter2 += 1
      # counter starts at 0th element and checks each element to the right,
      # then starts at the 1th element repeats the process from there, and so on
      counter = counter2
      total = 0
      values = [None] * 2

    # print(counter)
    # if ht.storage[counter] != None:

    # will always store the current element being looked at as 
    # the first element in the values array.
    if total == 0:
      total = hash_table_retrieve(ht, counter)
      # print(total == 7, counter
      values[0] = counter
      # print(values)
    else:
      current = hash_table_retrieve(ht, counter)

      # add starter index to other element to check if it equals the limit
      if (total + current) == limit:
        values[1] = counter          
        # total += hash_table_retrieve(ht, ht.storage[counter].key)          
        break

    counter += 1

  if values[0] < values[1]:
    temp = values[0]
    values[0] = values[1]
    values[1] = temp

  return (values[0], values[1])

  # print(ht.storage)
  # # for item in ht.storage:
  # current = ht.storage[0]
  # while current is not None:
  #   print(current.key, current.value)
  #   current = current.next

def print_answer(answer):
  if answer is not None:
    print(str(answer[0] + " " + answer[1]))
  else:
    print("None")

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)

weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(answer_3)

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_4)

weights_1 = [9]
answer_1 = get_indices_of_item_weights(weights_1, 1, 9)