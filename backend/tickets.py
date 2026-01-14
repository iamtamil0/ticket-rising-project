from flask import Blueprint, request, redirect, url_for, session, render_template_string

tickets_bp = Blueprint("tickets", __name__)

tickets = []
ticket_id = 1

@tickets_bp.route("/create-ticket", methods=["GET", "POST"])
def create_ticket():
    global ticket_id

    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        ticket = {
            "id": ticket_id,
            "title": request.form["title"],
            "description": request.form["description"],
            "priority": request.form["priority"],
            "status": "Open",
            "created_by": session["user"]
        }
        tickets.append(ticket)
        ticket_id += 1
        return redirect(url_for("tickets.view_tickets"))

    return render_template_string("""
    <h2>Create Ticket</h2>
    <form method="post">
        Title: <input name="title" required><br>
        Description:<br>
        <textarea name="description" required></textarea><br>
        Priority:
        <select name="priority">
            <option>Low</option>
            <option>Medium</option>
            <option>High</option>
        </select><br>
        <button type="submit">Submit Ticket</button>
    </form>
    <a href="/tickets">Back</a>
    """)

@tickets_bp.route("/tickets")
def view_tickets():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    role = session["role"]
    user = session["user"]

    if role in ["admin", "technician"]:
        visible_tickets = tickets
    else:
        visible_tickets = [t for t in tickets if t["created_by"] == user]

    rows = ""
    for t in visible_tickets:
        rows += f"""
        <tr>
            <td>{t['id']}</td>
            <td>{t['title']}</td>
            <td>{t['priority']}</td>
            <td>{t['status']}</td>
            <td>{t['created_by']}</td>
        </tr>
        """

    return render_template_string(f"""
    <h2>Tickets</h2>
    <a href="/create-ticket">Create Ticket</a><br><br>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Priority</th>
            <th>Status</th>
            <th>Created By</th>
        </tr>
        {rows}
    </table>
    <br>
    <a href="/dashboard">Dashboard</a>
    """)