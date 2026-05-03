-- ============================================
-- SPORTS TICKETING MANAGEMENT SYSTEM
-- Database Creation Script
-- ============================================

CREATE DATABASE IF NOT EXISTS sports_ticketing
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE sports_ticketing;

-- Table: Events
CREATE TABLE Events (
    EventID     INT           AUTO_INCREMENT PRIMARY KEY,
    EventName   VARCHAR(255)  NOT NULL,
    EventDate   DATETIME      NOT NULL,
    Venue       VARCHAR(255)  NOT NULL,
    Sport       VARCHAR(100)  NOT NULL,
    TotalSeats  INT           DEFAULT 0,
    Status      ENUM('Upcoming','Ongoing','Completed','Cancelled')
                              DEFAULT 'Upcoming',
    CreatedAt   TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

-- Table: Customers
CREATE TABLE Customers (
    CustomerID    INT           AUTO_INCREMENT PRIMARY KEY,
    CustomerName  VARCHAR(255)  NOT NULL,
    PhoneNumber   VARCHAR(20)   UNIQUE NOT NULL,
    Email         VARCHAR(255)  UNIQUE,
    Address       TEXT,
    DateOfBirth   DATE,
    CreatedAt     TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

-- Table: BoxOffices
CREATE TABLE BoxOffices (
    BoxOfficeID  INT           AUTO_INCREMENT PRIMARY KEY,
    OfficeName   VARCHAR(255)  NOT NULL,
    Address      VARCHAR(255)  NOT NULL,
    PhoneNumber  VARCHAR(20),
    OpeningHours VARCHAR(100),
    ManagerName  VARCHAR(255)
);

-- Table: Seats
CREATE TABLE Seats (
    SeatID      INT           AUTO_INCREMENT PRIMARY KEY,
    EventID     INT           NOT NULL,
    SeatNumber  VARCHAR(20)   NOT NULL,
    SeatType    ENUM('VIP','Standard','Student') NOT NULL,
    Section     VARCHAR(50),
    IsAvailable TINYINT(1)    DEFAULT 1,
    CONSTRAINT fk_seat_event FOREIGN KEY (EventID) REFERENCES Events(EventID)
        ON DELETE CASCADE
);

-- Table: Tickets
CREATE TABLE Tickets (
    TicketID     INT             AUTO_INCREMENT PRIMARY KEY,
    EventID      INT             NOT NULL,
    CustomerID   INT,
    SeatID       INT             NOT NULL,
    TicketType   ENUM('VIP','Standard','Student','Group') NOT NULL,
    Price        DECIMAL(10,2)   NOT NULL CHECK (Price >= 0),
    PurchaseDate DATETIME,
    BoxOfficeID  INT,
    Status       ENUM('Available','Sold','Cancelled') DEFAULT 'Available',
    CONSTRAINT fk_ticket_event    FOREIGN KEY (EventID)     REFERENCES Events(EventID),
    CONSTRAINT fk_ticket_customer FOREIGN KEY (CustomerID)  REFERENCES Customers(CustomerID),
    CONSTRAINT fk_ticket_seat     FOREIGN KEY (SeatID)      REFERENCES Seats(SeatID),
    CONSTRAINT fk_ticket_office   FOREIGN KEY (BoxOfficeID) REFERENCES BoxOffices(BoxOfficeID)
);
