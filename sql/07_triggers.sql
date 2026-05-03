-- ============================================
-- TRIGGERS
-- ============================================

DELIMITER $$

-- Trigger 1: Release seat when a ticket is cancelled
CREATE TRIGGER trg_ticket_cancelled
AFTER UPDATE ON Tickets
FOR EACH ROW
BEGIN
    IF NEW.Status = 'Cancelled' AND OLD.Status = 'Sold' THEN
        UPDATE Seats
        SET    IsAvailable = 1
        WHERE  SeatID = NEW.SeatID;
    END IF;
END$$

-- Trigger 2: Mark seat as occupied when a ticket is sold
CREATE TRIGGER trg_ticket_sold
AFTER UPDATE ON Tickets
FOR EACH ROW
BEGIN
    IF NEW.Status = 'Sold' AND OLD.Status = 'Available' THEN
        UPDATE Seats
        SET    IsAvailable = 0
        WHERE  SeatID = NEW.SeatID;
    END IF;
END$$

DELIMITER ;

-- Verify trigger: cancel a sold ticket
-- Before: check seat status
SELECT SeatID, IsAvailable FROM Seats WHERE SeatID = 4;
-- Cancel the ticket
UPDATE Tickets SET Status = 'Cancelled' WHERE SeatID = 4 AND Status = 'Sold';
-- After: seat must automatically return to IsAvailable = 1
SELECT SeatID, IsAvailable FROM Seats WHERE SeatID = 4;
