-- ============================================================
-- SPORTS TICKETING MANAGEMENT SYSTEM
-- File: 02_sample_data.sql
-- Description: Sample data with realistic sold tickets for demo
-- ============================================================
 
USE sports_ticketing;
 
SET SQL_SAFE_UPDATES = 0;
 
-- ── CLEAR EXISTING DATA ──────────────────────────────────────
DELETE FROM Tickets;
DELETE FROM Seats;
DELETE FROM Customers;
DELETE FROM BoxOffices;
DELETE FROM Events;
 
ALTER TABLE Tickets    AUTO_INCREMENT = 1;
ALTER TABLE Seats      AUTO_INCREMENT = 1;
ALTER TABLE Customers  AUTO_INCREMENT = 1;
ALTER TABLE BoxOffices AUTO_INCREMENT = 1;
ALTER TABLE Events     AUTO_INCREMENT = 1;
 
SET SQL_SAFE_UPDATES = 1;
 
-- ── EVENTS ───────────────────────────────────────────────────
INSERT INTO Events (EventName, EventDate, Venue, Sport, TotalSeats, Status) VALUES
('V.League Football Final 2025',     '2025-06-15 19:00:00', 'My Dinh National Stadium, Hanoi',  'Football',   400, 'Completed'),
('National Swimming Championship',   '2025-07-10 08:00:00', 'Tu Son Aquatic Center, Bac Ninh',  'Swimming',   200, 'Completed'),
('Hanoi Open Badminton 2025',         '2025-07-20 09:00:00', 'Hanoi Sports Palace',              'Badminton',  300, 'Completed'),
('ATP 500 Tennis Tour Vietnam',       '2025-08-05 14:00:00', 'My Dinh Tennis Stadium, Hanoi',   'Tennis',     250, 'Upcoming'),
('SEA 3x3 Basketball Cup',            '2025-09-01 10:00:00', 'Hanoi Sports Arena',               'Basketball', 180, 'Upcoming');
 
-- ── BOX OFFICES ──────────────────────────────────────────────
INSERT INTO BoxOffices (OfficeName, Address, PhoneNumber, OpeningHours, ManagerName) VALUES
('My Dinh Ticket Office',   '141 Le Duc Tho, My Dinh, Hanoi',         '024-3835-1234', '07:00-21:00', 'Nguyen Van An'),
('Tu Son Ticket Office',    'Dinh Bang Ward, Tu Son, Bac Ninh',        '0222-382-0456', '08:00-20:00', 'Tran Thi Binh'),
('Online Ticket Office',    'Nationwide Online System',                 '1800-1234',     '24/7',        'Le Van Cuong');
 
-- ── CUSTOMERS ────────────────────────────────────────────────
INSERT INTO Customers (CustomerName, PhoneNumber, Email, Address, DateOfBirth) VALUES
('Nguyen Thanh Long',   '0901234567', 'long.nt@email.com',   '12 Tran Duy Hung, Hanoi',        '1995-03-14'),
('Pham Thu Huong',      '0912345678', 'huong.pt@email.com',  '45 Le Van Luong, Hanoi',          '1998-07-22'),
('Do Minh Khoa',        '0923456789', 'khoa.dm@email.com',   '89 Nguyen Chi Thanh, Hanoi',      '2000-11-05'),
('Vu Thi Mai',          '0934567890', 'mai.vt@email.com',    '22 Kim Ma, Hanoi',                '1992-04-18'),
('Hoang Duc Nam',       '0945678901', 'nam.hd@email.com',    '67 Xuan Thuy, Hanoi',             '1997-09-30'),
('Tran Quoc Bao',       '0956789012', 'bao.tq@email.com',    '15 Doi Can, Hanoi',               '1993-01-20'),
('Le Thi Lan',          '0967890123', 'lan.lt@email.com',    '88 Nguyen Trai, Hanoi',           '1999-05-11'),
('Phan Van Duc',        '0978901234', 'duc.pv@email.com',    '33 Hoang Cau, Hanoi',             '1996-08-25'),
('Nguyen Bich Ngoc',    '0989012345', 'ngoc.nb@email.com',   '55 Lang Ha, Hanoi',               '2001-12-03'),
('Cao Minh Tri',        '0990123456', 'tri.cm@email.com',    '77 Cau Giay, Hanoi',              '1994-06-17');
 
-- ── SEATS FOR EVENT 1 (Football – 20 seats for demo) ─────────
INSERT INTO Seats (EventID, SeatNumber, SeatType, Section) VALUES
(1,'VIP-A01','VIP','VIP Section A'),  (1,'VIP-A02','VIP','VIP Section A'),
(1,'VIP-A03','VIP','VIP Section A'),  (1,'VIP-A04','VIP','VIP Section A'),
(1,'STD-B01','Standard','Section B'), (1,'STD-B02','Standard','Section B'),
(1,'STD-B03','Standard','Section B'), (1,'STD-B04','Standard','Section B'),
(1,'STD-B05','Standard','Section B'), (1,'STD-B06','Standard','Section B'),
(1,'STU-C01','Student','Student C'),  (1,'STU-C02','Student','Student C'),
(1,'STU-C03','Student','Student C'),  (1,'STU-C04','Student','Student C');
 
-- ── SEATS FOR EVENT 2 (Swimming – 10 seats) ──────────────────
INSERT INTO Seats (EventID, SeatNumber, SeatType, Section) VALUES
(2,'VIP-A01','VIP','VIP Section A'),  (2,'VIP-A02','VIP','VIP Section A'),
(2,'STD-B01','Standard','Section B'), (2,'STD-B02','Standard','Section B'),
(2,'STD-B03','Standard','Section B'), (2,'STU-C01','Student','Student C'),
(2,'STU-C02','Student','Student C');
 
-- ── SEATS FOR EVENT 3 (Badminton – 10 seats) ─────────────────
INSERT INTO Seats (EventID, SeatNumber, SeatType, Section) VALUES
(3,'VIP-A01','VIP','VIP Section A'),  (3,'VIP-A02','VIP','VIP Section A'),
(3,'STD-B01','Standard','Section B'), (3,'STD-B02','Standard','Section B'),
(3,'STD-B03','Standard','Section B'), (3,'STU-C01','Student','Student C'),
(3,'STU-C02','Student','Student C');
 
-- ── SEATS FOR EVENT 4 (Tennis – upcoming, 8 seats) ───────────
INSERT INTO Seats (EventID, SeatNumber, SeatType, Section) VALUES
(4,'VIP-A01','VIP','VIP Section A'),  (4,'VIP-A02','VIP','VIP Section A'),
(4,'STD-B01','Standard','Section B'), (4,'STD-B02','Standard','Section B'),
(4,'STU-C01','Student','Student C'),  (4,'STU-C02','Student','Student C');
 
-- ── SEATS FOR EVENT 5 (Basketball – upcoming, 6 seats) ───────
INSERT INTO Seats (EventID, SeatNumber, SeatType, Section) VALUES
(5,'VIP-A01','VIP','VIP Section A'),
(5,'STD-B01','Standard','Section B'), (5,'STD-B02','Standard','Section B'),
(5,'STU-C01','Student','Student C'),  (5,'STU-C02','Student','Student C');
 
-- ── TICKETS (Available) ──────────────────────────────────────
-- Event 1: Football (SeatIDs 1-14)
INSERT INTO Tickets (EventID, SeatID, TicketType, Price, BoxOfficeID, Status) VALUES
(1,1,'VIP',2000000,1,'Available'),  (1,2,'VIP',2000000,1,'Available'),
(1,3,'VIP',2000000,1,'Available'),  (1,4,'VIP',2000000,1,'Available'),
(1,5,'Standard',500000,1,'Available'), (1,6,'Standard',500000,1,'Available'),
(1,7,'Standard',500000,1,'Available'), (1,8,'Standard',500000,2,'Available'),
(1,9,'Standard',500000,2,'Available'), (1,10,'Standard',500000,2,'Available'),
(1,11,'Student',200000,1,'Available'), (1,12,'Student',200000,1,'Available'),
(1,13,'Student',200000,3,'Available'), (1,14,'Student',200000,3,'Available');
 
-- Event 2: Swimming (SeatIDs 15-21)
INSERT INTO Tickets (EventID, SeatID, TicketType, Price, BoxOfficeID, Status) VALUES
(2,15,'VIP',1500000,2,'Available'),  (2,16,'VIP',1500000,2,'Available'),
(2,17,'Standard',400000,2,'Available'), (2,18,'Standard',400000,2,'Available'),
(2,19,'Standard',400000,2,'Available'), (2,20,'Student',150000,3,'Available'),
(2,21,'Student',150000,3,'Available');
 
-- Event 3: Badminton (SeatIDs 22-28)
INSERT INTO Tickets (EventID, SeatID, TicketType, Price, BoxOfficeID, Status) VALUES
(3,22,'VIP',800000,1,'Available'),   (3,23,'VIP',800000,1,'Available'),
(3,24,'Standard',300000,1,'Available'), (3,25,'Standard',300000,1,'Available'),
(3,26,'Standard',300000,2,'Available'), (3,27,'Student',100000,3,'Available'),
(3,28,'Student',100000,3,'Available');
 
-- Event 4: Tennis upcoming (SeatIDs 29-34)
INSERT INTO Tickets (EventID, SeatID, TicketType, Price, BoxOfficeID, Status) VALUES
(4,29,'VIP',3000000,1,'Available'),  (4,30,'VIP',3000000,1,'Available'),
(4,31,'Standard',800000,1,'Available'), (4,32,'Standard',800000,3,'Available'),
(4,33,'Student',300000,3,'Available'), (4,34,'Student',300000,3,'Available');
 
-- Event 5: Basketball upcoming (SeatIDs 35-39)
INSERT INTO Tickets (EventID, SeatID, TicketType, Price, BoxOfficeID, Status) VALUES
(5,35,'VIP',1200000,1,'Available'),
(5,36,'Standard',350000,1,'Available'), (5,37,'Standard',350000,2,'Available'),
(5,38,'Student',120000,3,'Available'),  (5,39,'Student',120000,3,'Available');
 
-- ── SIMULATE SALES: sell tickets for completed events ─────────
-- Event 1 Football: sell 2 VIP + 4 Standard + 3 Student
UPDATE Tickets SET CustomerID=1,  PurchaseDate='2025-06-10 09:15:00', Status='Sold' WHERE TicketID=1;
UPDATE Tickets SET CustomerID=2,  PurchaseDate='2025-06-10 10:22:00', Status='Sold' WHERE TicketID=2;
UPDATE Tickets SET CustomerID=3,  PurchaseDate='2025-06-11 14:05:00', Status='Sold' WHERE TicketID=5;
UPDATE Tickets SET CustomerID=4,  PurchaseDate='2025-06-11 14:30:00', Status='Sold' WHERE TicketID=6;
UPDATE Tickets SET CustomerID=5,  PurchaseDate='2025-06-12 08:45:00', Status='Sold' WHERE TicketID=7;
UPDATE Tickets SET CustomerID=6,  PurchaseDate='2025-06-12 09:00:00', Status='Sold' WHERE TicketID=8;
UPDATE Tickets SET CustomerID=7,  PurchaseDate='2025-06-13 16:20:00', Status='Sold' WHERE TicketID=11;
UPDATE Tickets SET CustomerID=8,  PurchaseDate='2025-06-13 16:35:00', Status='Sold' WHERE TicketID=12;
UPDATE Tickets SET CustomerID=9,  PurchaseDate='2025-06-14 11:00:00', Status='Sold' WHERE TicketID=13;
 
-- Event 2 Swimming: sell 1 VIP + 2 Standard + 1 Student
UPDATE Tickets SET CustomerID=3,  PurchaseDate='2025-07-05 10:00:00', Status='Sold' WHERE TicketID=15;
UPDATE Tickets SET CustomerID=7,  PurchaseDate='2025-07-06 11:30:00', Status='Sold' WHERE TicketID=17;
UPDATE Tickets SET CustomerID=9,  PurchaseDate='2025-07-07 14:00:00', Status='Sold' WHERE TicketID=18;
UPDATE Tickets SET CustomerID=10, PurchaseDate='2025-07-08 09:15:00', Status='Sold' WHERE TicketID=20;
 
-- Event 3 Badminton: sell 2 VIP + 1 Standard
UPDATE Tickets SET CustomerID=1,  PurchaseDate='2025-07-15 10:00:00', Status='Sold' WHERE TicketID=22;
UPDATE Tickets SET CustomerID=4,  PurchaseDate='2025-07-15 11:00:00', Status='Sold' WHERE TicketID=23;
UPDATE Tickets SET CustomerID=6,  PurchaseDate='2025-07-16 09:00:00', Status='Sold' WHERE TicketID=24;
 
-- ── UPDATE SEAT AVAILABILITY to match sold tickets ────────────
UPDATE Seats SET IsAvailable=0 WHERE SeatID IN (1,2,5,6,7,8,11,12,13);   -- Event 1
UPDATE Seats SET IsAvailable=0 WHERE SeatID IN (15,17,18,20);             -- Event 2
UPDATE Seats SET IsAvailable=0 WHERE SeatID IN (22,23,24);                -- Event 3
 
-- ── VERIFY ───────────────────────────────────────────────────
SELECT 'Events'     AS TableName, COUNT(*) AS TotalRows FROM Events    UNION ALL
SELECT 'Customers',  COUNT(*) FROM Customers  UNION ALL
SELECT 'BoxOffices', COUNT(*) FROM BoxOffices UNION ALL
SELECT 'Seats',      COUNT(*) FROM Seats      UNION ALL
SELECT 'Tickets',    COUNT(*) FROM Tickets;
 
SELECT '--- SOLD TICKETS BY EVENT ---' AS Info;
SELECT e.EventName, COUNT(*) AS SoldTickets,
       SUM(t.Price) AS TotalRevenue
FROM   Tickets t JOIN Events e ON t.EventID = e.EventID
WHERE  t.Status = 'Sold'
GROUP  BY e.EventName
ORDER  BY TotalRevenue DESC;