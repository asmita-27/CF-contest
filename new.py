# n = int(input())
data = [("T1","OPEN"),("T2","COMMENT"),("T1","CLOSE"),("T3","CLOSE"),("T2","CLOSE")]


def find_invalid_tickets(events):
    opened = set()
    invalid = set()

    for ticket_id, action in events:
        if action == "OPEN":
            opened.add(ticket_id)
        elif action == "CLOSE":
            if ticket_id not in opened:
                invalid.add(ticket_id)
        # COMMENT is ignored

    return list(invalid)

invalid_tickets = find_invalid_tickets(data)
print(invalid_tickets)