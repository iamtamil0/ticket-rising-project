-- Create database
CREATE DATABASE IF NOT EXISTS ticket_system;

USE ticket_system;

-- Create accounts table
CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role ENUM('user', 'admin', 'technician') DEFAULT 'user'
);

-- Create tickets table
CREATE TABLE IF NOT EXISTS tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium',
    status ENUM('open', 'in_progress', 'closed') DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES accounts(id)
);

-- Insert sample data
INSERT INTO accounts (username, password, email, role) VALUES
('admin', '$2b$12$examplehashedpassword', 'admin@example.com', 'admin'),
('tech', '$2b$12$examplehashedpassword', 'tech@example.com', 'technician'),
('user', '$2b$12$examplehashedpassword', 'user@example.com', 'user');