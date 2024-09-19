# Sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to generate new unique ticket ID
def generate_ticket_id():
    ticket_number = len(service_tickets) + 1
    return f"Ticket{ticket_number:03d}"

# Function to open a new service ticket
def open_ticket(customer_name, issue_description):
    ticket_id = generate_ticket_id()
    service_tickets[ticket_id] = {
        "Customer": customer_name,
        "Issue": issue_description,
        "Status": "open"
    }
    print(f"New ticket opened: {ticket_id}")

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} updated to status: {new_status}")
    else:
        print(f"Ticket ID {ticket_id} not found!")

# Function to display all tickets or filter by status
def display_tickets(filter_status=None):
    if filter_status:
        filtered_tickets = {tid: info for tid, info in service_tickets.items() if info["Status"] == filter_status}
        if filtered_tickets:
            print(f"Tickets with status '{filter_status}':")
            for ticket_id, ticket_info in filtered_tickets.items():
                print(f"{ticket_id}: {ticket_info}")
        else:
            print(f"No tickets with status '{filter_status}'.")
    else:
        print("All service tickets:")
        for ticket_id, ticket_info in service_tickets.items():
            print(f"{ticket_id}: {ticket_info}")

# Testing the functionality

# Open a new ticket
open_ticket("Charlie", "Account locked")

# Update ticket status
update_ticket_status("Ticket001", "closed")

# Display all tickets
display_tickets()

# Display only open tickets
display_tickets("open")
