-- ============================================
-- USER ACCESS CONTROL
-- ============================================

-- Admin user
CREATE USER 'admin_ticketing'@'localhost' IDENTIFIED BY 'Admin@Secure2025!';
GRANT ALL PRIVILEGES ON sports_ticketing.* TO 'admin_ticketing'@'localhost';

-- Manager user (read-only + reports)
CREATE USER 'manager_ticketing'@'localhost' IDENTIFIED BY 'Manager@2025!';
GRANT SELECT ON sports_ticketing.* TO 'manager_ticketing'@'localhost';
GRANT EXECUTE ON PROCEDURE sports_ticketing.sp_revenue_report TO 'manager_ticketing'@'localhost';

-- Cashier user
CREATE USER 'cashier_ticketing'@'localhost' IDENTIFIED BY 'Cashier@2025!';
GRANT SELECT ON sports_ticketing.Events    TO 'cashier_ticketing'@'localhost';
GRANT SELECT ON sports_ticketing.Seats     TO 'cashier_ticketing'@'localhost';
GRANT SELECT ON sports_ticketing.Tickets   TO 'cashier_ticketing'@'localhost';
GRANT INSERT, UPDATE ON sports_ticketing.Customers TO 'cashier_ticketing'@'localhost';
GRANT EXECUTE ON PROCEDURE sports_ticketing.sp_book_ticket TO 'cashier_ticketing'@'localhost';

FLUSH PRIVILEGES;

-- Verify grants
SHOW GRANTS FOR 'cashier_ticketing'@'localhost';
