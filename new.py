def find_invalid_tickets(events):
    NEW = "NEW"
    OPEN = "OPEN"
    CLOSED = "CLOSED"

    state = {}     
    invalid = set()

    for ticket_id, action in events:
        curr = state.get(ticket_id, NEW)

        if action == "OPEN":
            if curr != NEW:
                invalid.add(ticket_id)
            else:
                state[ticket_id] = OPEN

        elif action == "CLOSE":
            if curr != OPEN:
                invalid.add(ticket_id)
            else:
                state[ticket_id] = CLOSED

        elif action == "REOPEN":
            if curr != CLOSED:
                invalid.add(ticket_id)
            else:
                state[ticket_id] = OPEN

        elif action == "COMMENT": 
            continue

    return list(invalid)
