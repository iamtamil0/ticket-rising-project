# Nginx + HTTPS Setup – Ticket Rising Project

## Why Nginx
- Acts as reverse proxy
- Handles SSL/TLS
- Protects application server

## Architecture
Browser → Nginx (80/443) → Gunicorn (8000) → Flask

## Offline (LAN)
- Self-signed SSL
- Internal IP access
- Gunicorn bound to localhost

## Online (Cloud)
- Public domain
- Let’s Encrypt SSL
- Secure HTTPS access

## Note
Nginx is not run inside development containers.
