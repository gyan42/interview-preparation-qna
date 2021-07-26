"""
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically smallest one. All flights
must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a
valid itinerary. However, the first one is lexicographically smaller.
"""


def get_values(map, key):
    """
    Get teh value for the key and remove the path from the route map
    Args:
        map:
        key:

    Returns:

    """
    res = None
    for t in map:
        if t[0] == key:
            res = t[1]
            map.remove(t)
    return map, res


def is_key_present(key, map):
    for t in map:
        if t[0] == key:
            return True
    return False


def ordered_dict(d, starting_point):
    curr_sp = starting_point
    res = []
    res.append(curr_sp)
    d, next_sp = get_values(d, curr_sp)
    for i in range(len(d)):
        if is_key_present(next_sp, d):
            res.append(next_sp)
            curr_sp = next_sp
            d, next_sp = get_values(d, curr_sp)

    if len(res) == 1:
        res = None
    else:
        if next_sp:
            res.append(next_sp)
    print(res)
    return res



assert(ordered_dict(d=[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')],
                    starting_point='YUL') == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'])
# None
assert(ordered_dict(d=[('SFO', 'COM'), ('COM', 'YYZ')],
                    starting_point='COM') == None)

# ['A', 'B', 'C', 'A', 'C']
assert(ordered_dict(d=[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')],
                    starting_point='A') == ['A', 'B', 'C', 'A', 'C'])