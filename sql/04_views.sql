-- ============================================
-- VIEWS
-- ============================================

-- View 1: Sold-out events
CREATE OR REPLACE VIEW vw_soldout_events AS
SELECT
    e.EventID,
    e.EventName,
    e.EventDate,
    e.Venue,
    COUNT(t.TicketID)                                     AS TotalTickets,
    SUM(CASE WHEN t.Status = 'Sold' THEN 1 ELSE 0 END)   AS SoldTickets
FROM Events e
JOIN Tickets t ON e.EventID = t.EventID
GROUP BY e.EventID, e.EventName, e.EventDate, e.Venue
HAVING TotalTickets = SoldTickets;

-- View 2: Revenue by event
CREATE OR REPLACE VIEW vw_revenue_by_event AS
SELECT
    e.EventID,
    e.EventName,
    e.EventDate,
    e.Venue,
    COUNT(t.TicketID)                                          AS TicketsSold,
    SUM(CASE WHEN t.Status='Sold' THEN t.Price ELSE 0 END)    AS TotalRevenue,
    AVG(CASE WHEN t.Status='Sold' THEN t.Price ELSE NULL END)  AS AvgTicketPrice
FROM Events e
LEFT JOIN Tickets t ON e.EventID = t.EventID
GROUP BY e.EventID, e.EventName, e.EventDate, e.Venue
ORDER BY TotalRevenue DESC;

-- View 3: Seat availability by event
CREATE OR REPLACE VIEW vw_seat_availability AS
SELECT
    e.EventName,
    s.SeatType,
    COUNT(s.SeatID)                      AS TotalSeats,
    SUM(s.IsAvailable)                   AS AvailableSeats,
    COUNT(s.SeatID) - SUM(s.IsAvailable) AS OccupiedSeats
FROM Events e
JOIN Seats s ON e.EventID = s.EventID
GROUP BY e.EventID, e.EventName, s.SeatType;

-- Query the views
SELECT * FROM vw_revenue_by_event;
SELECT * FROM vw_seat_availability WHERE EventName LIKE '%Football%';