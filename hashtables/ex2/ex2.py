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
  sources = [None] * length
  # while true and keep looping? 
  # reset i if longer then the length
  for i in range(len(tickets)):
    hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    sources[i] = tickets[i].source
  # print(hashtable.storage)

  k = 0
  route_index_tracker = 0
  while True:
    # if we've gone over the entire array, 
    # start over from the beginning
    if k == len(sources):
      k = 0

    # find the ticket with the source of 'NONE'
    # and sets it as the first element in the route arr
    if route_index_tracker == 0 and sources[k] == 'NONE':

    # if hash_table_retrieve(hashtable, sources[k]) == 'NONE':
      route[route_index_tracker] = hash_table_retrieve(hashtable, sources[k])
      # print(hash_table_retrieve(hashtable, sources[k]))
      route_index_tracker += 1

    # one less than the last index, cause the last index is treated different.

    elif route_index_tracker > 0 and route_index_tracker < len(route) - 1:
      # needs to equal the destination of the last route
      # print(route_index_tracker)
      # print(sources[k], hash_table_retrieve(hashtable, route[route_index_tracker-1]))

      # finds the destination of the last item placed in the routes arr,
      # and adds it into the next spot of the routes arr
      # if sources[k] == hash_table_retrieve(hashtable, route[route_index_tracker-1]):
        # route[route_index_tracker] = hash_table_retrieve(hashtable, sources[k])
      route[route_index_tracker] = hash_table_retrieve(hashtable, route[route_index_tracker-1])

      # print(route)
      route_index_tracker += 1
    # last index
    # feel like i could make this more concise
    elif route_index_tracker == len(route) - 1:
      # print(hash_table_retrieve(hashtable, route[route_index_tracker-1]))
      # route_index_tracker += 1        

      if hash_table_retrieve(hashtable, route[route_index_tracker-1]) == 'NONE':

        route[route_index_tracker] = hash_table_retrieve(hashtable, route[route_index_tracker-1])
      # print(hash_table_retrieve(hashtable, sources[k]))
      route_index_tracker += 1        

      # print(5, route)

    if route_index_tracker == len(route):
      break

    k += 1

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
print(result)