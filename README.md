# Sports Ticketing Management System
**Project 16 — Introduction to Database | DATCOM Lab, NEU**

## Overview
A relational database system for managing sports event ticket sales, including event scheduling, seat booking, customer management, and revenue reporting.

## Technology Stack
- **Database:** MySQL 8.0+
- **Language:** Python 3.x
- **Connector:** mysql-connector-python
- **Tool:** MySQL Workbench

## Database Schema
The system consists of 5 main tables:
- `Events` — Sports event information
- `Tickets` — Ticket records per event and seat
- `Customers` — Customer profiles
- `Seats` — Seat availability per event
- `BoxOffices` — Ticket sales counters

## Project Structure
sports-ticketing/
├── sql/
│   ├── 01_create_tables.sql       # Database and table creation
│   ├── 02_sample_data.sql         # Sample data insertion
│   ├── 03_indexes.sql             # Performance indexes
│   ├── 04_views.sql               # Revenue and availability views
│   ├── 05_stored_procedures.sql   # Booking and reporting procedures
│   ├── 06_functions.sql           # User-defined functions
│   ├── 07_triggers.sql            # Seat status automation
│   └── 08_security.sql            # User roles and access control
├── python/
│   └── main.py                    # Console application
└── README.md

## Features
- Event scheduling and match information management
- Seat booking with real-time availability tracking
- Customer management and purchase history
- Revenue reporting and sales statistics
- Role-based access control (admin, manager, cashier)
- AES-256 encryption for sensitive customer data

## Setup Instructions
1. Install MySQL 8.0+ and Python 3.x
2. Run SQL scripts in order (01 → 08)
3. Install Python dependency: `pip install mysql-connector-python`
4. Update database credentials in `python/main.py`
5. Run: `python python/main.py`

## Supervisor
Dr. Hung Tran — hung.tran@neu.edu.vn — DATCOM Lab, National Economics University