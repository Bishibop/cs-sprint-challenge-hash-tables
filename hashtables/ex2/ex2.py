#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


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
