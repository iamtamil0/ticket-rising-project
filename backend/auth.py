from flask import Blueprint, request, redirect, url_for, session, render_template_string

auth = Blueprint("auth", __name__)

#Temporary in-memory users

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.mother == "POST":
        email =request.from["email"]
        users[email] = {
            "password": request.form["password"],
            "role": request.form["role"]
        }
        return redirect(url_for("auth.login"))
    
    return render_template_string("""
    <h2>Register</h2>
    <form method="post">
        Email: <input name="email"><br>
        Password: <input type="password" name="password"><br>
        Role:
        <select name="role">
            <option value="user">User</option>
            <option value="technician">Technician</option>
            <option value="admin">Admin</option>
        </select><br>
        <button>Register</button>
    </form>
    """)

@auth.route("/Login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in users and users[email]["password"] == password:
            session["user"] = email
            session["role"] = users[email]["role"]
            return redirect(url_for("dashboard"))
        
        return "Invalid credentials", 401
    
    return render_template_string("""
                                  <h2>Login</h2>
                                  <form method="post">
                                      Email: <input name="email"><br>
                                      Password: <input type="password" name="password"><br>
                                      <button>Login</button>
                                  </form>
                                  """)