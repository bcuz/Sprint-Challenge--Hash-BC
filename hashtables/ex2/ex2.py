#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
            hash_table_insert,
            hash_table_remove,
            hash_table_retrieve,
            hash_table_resize)

class Ticket:
  def __init__(self, source, destination):
    self.source = source
    self.destination = destination

def reconstruct_trip(tickets, length):
  hashtable = HashTable(length)
  route = [None] * length

  # if source is None, it's the first one
  # if destination is None, it's the last one.

  # while true and keep looping? 
  # reset i if longer then the length
  for i in range(len(tickets)):
    hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
  # print(hashtable.storage)

  k = 0
  while None in route:
    if k == len(hashtable.storage):
      k = 0

    # if hashtable.storage[k] != None:
    #   print((hashtable.storage[k].key), hash_table_retrieve(hashtable, hashtable.storage[k].key))  

    if route[0] == None:
      if hashtable.storage[k] != None:
        # print(hashtable.storage[k].key == 'None')
        if hashtable.storage[k].key == 'NONE':
          # print(5)
          route[0] = hash_table_retrieve(hashtable, hashtable.storage[k].key)

    if k == len(route)-1:
      print(route)
      route = True

    k += 1


  # for i in range(len(hashtable.storage)):
  #   if hashtable.storage[i] != None:
  #     print(hashtable.storage[i].key, hash_table_retrieve(hashtable, hashtable.storage[i].key))

  # while route doesnt equal ticket length
  # start at none. if nothing in arr, get the one with none.
  # then find the one that links to that.

  return route


ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
            "SLC", "PIT", "ORD", "NONE"]
result = reconstruct_trip(tickets, 10)