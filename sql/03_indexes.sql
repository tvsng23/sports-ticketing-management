-- ============================================
-- INDEXES
-- ============================================

-- Index: find available seats by event
CREATE INDEX idx_seats_available
    ON Seats(EventID, IsAvailable);

-- Index: look up tickets by customer
CREATE INDEX idx_tickets_customer
    ON Tickets(CustomerID, Status);

-- Index: look up tickets by event
CREATE INDEX idx_tickets_event
    ON Tickets(EventID, Status);

-- Index: search events by date
CREATE INDEX idx_events_date
    ON Events(EventDate);

-- Verify created indexes
SHOW INDEX FROM Seats;
SHOW INDEX FROM Tickets;