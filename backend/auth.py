from flask import Blueprint, request, redirect, url_for, session, render_template_string

auth = Blueprint("auth", __name__)

# Temporary in-memory users
users = {}

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        users[email] = {
            "password": password,
            "role": role
        }
        return redirect(url_for("auth.login"))

    return render_template_string("""
    <h2>Register</h2>
    <form method="post">
        Email: <input name="email" required><br>
        Password: <input type="password" name="password" required><br>
        Role:
        <select name="role">
            <option value="user">User</option>
            <option value="technician">Technician</option>
            <option value="admin">Admin</option>
        </select><br>
        <button type="submit">Register</button>
    </form>
    """)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in users and users[email]["password"] == password:
            session["user"] = email
            session["role"] = users[email]["role"]
            return redirect(url_for("dashboard"))

        return "Invalid credentials"

    return render_template_string("""
    <h2>Login</h2>
    <form method="post">
        Email: <input name="email" required><br>
        Password: <input type="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
    """)