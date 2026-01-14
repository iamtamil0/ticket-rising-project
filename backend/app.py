from flask import Flask, session, redirect, url_for
from auth import auth
from tickets import tickets_bp

app = Flask(__name__)
app.secret_key = "ticket-secret-key"

app.register_blueprint(auth)
app.register_blueprint(tickets_bp)

@app.route("/")
def home():
    return redirect(url_for("auth.login"))

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    return f"""
    <h2>Dashboard</h2>
    Logged in as: {session['user']}<br>
    Role: {session['role']}<br><br>
    <a href="/create-ticket">Create Ticket</a><br>
    <a href="/tickets">View Tickets</a><br><br>
    <a href="/logout">Logout</a>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)