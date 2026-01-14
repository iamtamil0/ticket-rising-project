# MySQL Setup – Ticket Rising Project

## Offline (Company LAN)
- Install MySQL on server or VM
- Create database: ticket_rising
- Open port 3306 internally
- Flask connects via private IP

## Online (Cloud)
- Use AWS RDS / Azure DB
- Restrict access using security groups
- Use environment variables for credentials

## Note
MySQL is not run inside development containers.