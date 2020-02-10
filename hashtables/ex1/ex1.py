#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
            hash_table_insert,
            hash_table_remove,
            hash_table_retrieve,
            hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):
  ht = HashTable(16)

  left = 0
  right = len(weights) - 1

  while left < right:
    sumWeights = weights[left] + weights[right]
    print(sumWeights)

    if sumWeights == limit:
      return (right, left)
    elif sumWeights > limit:
      right -= 1
    else:
      left += 1

  # for i in range(len(weights)):
  #   hash_table_insert(ht, i, weights[i])

  # # it overwrites the weight, tho, if there's a dup
  # # as it should. like the advice is flipped..
  # for i in range(len(ht.storage)):
  #   if ht.storage[i] != None:
  #     print(ht.storage[i].key, hash_table_retrieve(ht, ht.storage[i].key))

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

# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# print(answer_2)

weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(answer_3)