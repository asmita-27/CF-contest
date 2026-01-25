n = int(input())
data = []

for _ in range(n):
    ticketId, action = input().split()
    data.append((ticketId, action))
    openTicket =set()
    invalidTickets = set()
    
    for ticketId, action in data:
        if action =="open":
            openTicket.add(ticketId)
        elif action=="close":
            if ticketId in openTicket:
                openTicket.remove(ticketId)
            else:
                invalidTickets.add(ticketId)
    
    print(invalidTickets)