# 🎫 Ticket Rising Project

A web-based **Ticket Raising (Helpdesk) System** designed for **company internal IT support**.
Supports both **Offline (Local Network)** and **Online (Cloud)** deployment.

## 🔧 Features
- Raise & track IT tickets
- Role-based login (User / Admin / Technician)
- Local Network (LAN) database support
- Online cloud deployment
- Secure and scalable design

## 🛠 Tech Stack
- Backend: Python (Flask)
- Frontend: HTML, CSS, JavaScript
- Database: MySQL
- Server: Local / AWS / Azure

## 🌐 Deployment Modes
### Offline (LAN)
Access using:

http://192.168.1.10:5000
### Online (Cloud)

http://public-ip:5000

---
## 📁 Folder Structure
- `backend/` - Flask application code
- `frontend/` - HTML templates and static files
- `database/` - MySQL database schema and scripts
- `docs/` - Documentation
- `requirements.txt` - Python dependencies

---
## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- MySQL Server
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/iamtamil0/ticket-rising-project.git
   cd ticket-rising-project
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up MySQL database:
   - Create a database named `ticket_system`
   - Run the SQL script in `database/init.sql`

4. Configure database connection in `backend/app.py`:
   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'your_username'
   app.config['MYSQL_PASSWORD'] = 'your_password'
   app.config['MYSQL_DB'] = 'ticket_system'
   ```

5. Run the application:
   ```bash
   python backend/app.py
   ```

6. Access the application at `http://localhost:5000`

### Deployment
- For LAN deployment, run on a server accessible to the local network
- For cloud deployment, deploy to AWS/Azure and update the database config accordingly

---
## 👨‍💻 Author
GitHub: https://github.com/iamtamil0
