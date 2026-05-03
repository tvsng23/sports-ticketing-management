-- ============================================
-- USER DEFINED FUNCTIONS
-- ============================================

DELIMITER $$

-- Function 1: Total revenue for an event
CREATE FUNCTION fn_total_revenue(p_event_id INT)
RETURNS DECIMAL(15,2)
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE v_total DECIMAL(15,2) DEFAULT 0;
    SELECT COALESCE(SUM(Price), 0)
    INTO   v_total
    FROM   Tickets
    WHERE  EventID = p_event_id AND Status = 'Sold';
    RETURN v_total;
END$$

-- Function 2: Total tickets sold for an event
CREATE FUNCTION fn_tickets_sold(p_event_id INT)
RETURNS INT
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE v_count INT DEFAULT 0;
    SELECT COUNT(*) INTO v_count
    FROM   Tickets
    WHERE  EventID = p_event_id AND Status = 'Sold';
    RETURN v_count;
END$$

DELIMITER ;

-- Use the functions in a query
SELECT
    EventID,
    EventName,
    fn_total_revenue(EventID)  AS TotalRevenue,
    fn_tickets_sold(EventID)   AS TicketsSold
FROM Events;