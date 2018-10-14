# One Way Flight Trip

"""
You've booked a really cheap one-way flight. Unfortunately, that means you have tons of layovers before you reach your destination. The morning of, you woke up late and had to scramble to the airport to catch your first flight. However, in your rush, you accidentally scrambled all your flight tickets. You don't know the route of your entire trip now!

Write a function reconstruct_trip to reconstruct your trip from your mass of flight tickets. Each ticket is a two-element array with the source airport as the first element and the destination airport as the second element. The ticket for your first flight has a destination but no source, and the ticket for your final flight has a source, but no destination.

An example input might look like this:

tickets = [
  ('PIT', 'ORD'),
  ('XNA', 'CID'),
  ('SFO', 'BHM'),
  ('FLG', 'XNA'),
  (None, 'LAX'), 
  ('LAX', 'SFO'),
  ('CID', 'SLC'),
  ('ORD', None),
  ('SLC', 'PIT'),
  ('BHM', 'FLG'),
]
Your function should output an array with the route of your trip. For the above example, it should look like this:

['LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD']
Your solution should run in linear time and also be able to handle incorrect ticket chains, namely when the input list of tickets is not cohesive such that there is a ticket that has a starting location which isn't the ending location of some other ticket in the chain or a ticket has an ending location that isn't the starting location of another ticket in the chain. In such cases, your solution should return an empty list.

Hints
The crux of this problem requires us to 'link' tickets together to reconstruct the entire trip. For example, if we have a ticket ('SJC', 'BOS') that has us flying from San Jose to Boston, then there exists another ticket where Boston is the starting location, ('BOS', 'JFK').
We can hash each ticket such that the starting location is the key and the destination is the value. Then, when constructing the entire route, the ith location in the route can be found by checking the hash table for the i-1th location.
"""


# Self Solution:
def reconstruct_trip(tickets):
    ht = {}
    for ticket in tickets:
        ht[ticket[0]] = ticket[1]

    # One of the keys will contain None, that value will be our starting destination.
    trip = []
    trip.append(ht[None])

    for i in range(len(ht)-2):
        try:
            # Each time, we find in the dictionary the key from our trip list.
            trip.append(ht[trip[i]])
        except:
            # If there is a missing layover, it will return an empty array.
            trip = []
            return trip
    return trip

# Official solution:


def reconstruct_trip(tickets):
    ticket_dict = {}
    route = [''] * (len(tickets) - 1)
    for ticket in tickets:
        ticket_dict[ticket[0]] = ticket[1]
        if ticket[0] is None:
            route[0] = ticket[1]
    for i in range(1, len(route)):
        if route(i - 1) in ticket_dict:
            route[i] = ticket_dict[route[i - 1]]
        else:
            return []
    return route
