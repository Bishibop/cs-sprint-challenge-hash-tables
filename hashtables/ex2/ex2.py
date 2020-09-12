class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


'''
For each ticket store the ticket as a value in a hash with it's source as
the key. Start with the first ticket, look up it's destination in the hash,
add it to the route and iterate through all the ticket's destinations.
'''


def reconstruct_trip(tickets, length):
    sources = {}

    for ticket in tickets:
        sources[ticket.source] = ticket

    route = []
    current_ticket = sources["NONE"]

    while True:
        route.append(current_ticket.destination)
        if current_ticket.destination == "NONE":
            break
        else:
            current_ticket = sources[current_ticket.destination]

    return route
