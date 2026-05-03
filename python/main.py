# 6.1. Data Connection

# Install: pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error
from datetime import datetime

def get_connection():
    """Establish a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host     = 'localhost',
            user     = 'admin_ticketing',
            password = 'Admin@Secure2025!',
            database = 'sports_ticketing',
            charset  = 'utf8mb4'
        )
        if conn.is_connected():
            print(f'Connected. Server version: {conn.get_server_info()}')
        return conn
    except Error as e:
        print(f'Connection error: {e}')
        return None

#########################################################################    
# 6.2. Booking Module

def search_events(keyword=''):
    """Search for upcoming events by keyword."""
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    query = '''
        SELECT EventID, EventName, EventDate, Venue, Sport,
               fn_tickets_sold(EventID) AS TicketsSold,
               TotalSeats
        FROM   Events
        WHERE  EventName LIKE %s AND Status = 'Upcoming'
        ORDER  BY EventDate
    '''
    cursor.execute(query, (f'%{keyword}%',))
    results = cursor.fetchall()
    cursor.close(); conn.close()
    return results

def get_available_seats(event_id):
    """Retrieve all available seats for a given event."""
    conn = get_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    query = '''
        SELECT s.SeatID, s.SeatNumber, s.SeatType, s.Section, t.Price
        FROM   Seats s
        JOIN   Tickets t ON s.SeatID = t.SeatID
        WHERE  s.EventID = %s AND s.IsAvailable = 1 AND t.Status = 'Available'
        ORDER  BY s.SeatType, s.SeatNumber
    '''
    cursor.execute(query, (event_id,))
    results = cursor.fetchall()
    cursor.close(); conn.close()
    return results

def book_ticket(customer_id, seat_id, box_office_id=1):
    """Call sp_book_ticket stored procedure to reserve a seat."""
    conn = get_connection()
    if not conn: return None, 'Unable to connect to database'
    cursor = conn.cursor()
    try:
        cursor.callproc('sp_book_ticket',
                        [customer_id, seat_id, box_office_id, 0, ''])
        cursor.execute('SELECT @_sp_book_ticket_3, @_sp_book_ticket_4')
        row = cursor.fetchone()
        ticket_id, message = row[0], row[1]
        conn.commit()
        return ticket_id, message
    except Error as e:
        conn.rollback()
        return -1, str(e)
    finally:
        cursor.close(); conn.close()

###########################################################################
# 6.3. Reporting Module

def generate_revenue_report(event_id=None):
    """Print revenue report. Pass event_id for a specific event, or None for all."""
    conn = get_connection()
    if not conn: return
    cursor = conn.cursor(dictionary=True)
    if event_id:
        cursor.callproc('sp_revenue_report', [event_id])
        rows = []
        for result in cursor.stored_results():
            rows = result.fetchall()
    else:
        cursor.execute('SELECT * FROM vw_revenue_by_event')
        rows = cursor.fetchall()
    cursor.close(); conn.close()

    print('=' * 65)
    print(f'  REVENUE REPORT  |  {datetime.now().strftime("%d/%m/%Y %H:%M")}')
    print('=' * 65)
    print(f"{'Event':<30} {'Tickets':>8} {'Revenue (VND)':>15}")
    print('-' * 65)
    total = 0
    for row in rows:
        rev  = float(row.get('TotalRevenue') or row.get('Revenue', 0))
        sold = int(row.get('TicketsSold')   or row.get('SoldCount', 0))
        name = str(row.get('EventName', ''))[:28]
        print(f"{name:<30} {sold:>8,d} {rev:>15,.0f}")
        total += rev
    print('=' * 65)
    print(f"{'TOTAL REVENUE':>40} {total:>15,.0f}")

#############################################################################
# 6.4. Console Interface (Main Menu)

def main():
    """Main console menu for the Sports Ticketing System."""
    while True:
        print('\n' + '='*52)
        print('   SPORTS TICKETING MANAGEMENT SYSTEM')
        print('='*52)
        print('1. Search events')
        print('2. View available seats')
        print('3. Book a ticket')
        print('4. Revenue report')
        print('5. Exit')
        print('='*52)
        choice = input('Select option (1-5): ').strip()

        if choice == '1':
            kw = input('Enter keyword (press Enter to list all): ')
            events = search_events(kw)
            if not events:
                print('No events found.')
            else:
                print(f"{'ID':>4} {'Event Name':<30} {'Date':>12} {'Venue':>18}")
                for e in events:
                    print(f"{e['EventID']:>4} {str(e['EventName'])[:28]:<30}"
                          f" {str(e['EventDate'])[:10]:>12} {str(e['Venue'])[:16]:>18}")

        elif choice == '2':
            eid = int(input('Enter EventID: '))
            seats = get_available_seats(eid)
            if not seats:
                print('No available seats or event not found.')
            else:
                print(f"{'SeatID':>8} {'Number':>8} {'Type':>10} {'Section':>14} {'Price':>12}")
                for s in seats:
                    print(f"{s['SeatID']:>8} {s['SeatNumber']:>8} {s['SeatType']:>10}"
                          f" {str(s['Section'])[:12]:>14} {float(s['Price']):>12,.0f}")

        elif choice == '3':
            cid = int(input('CustomerID: '))
            sid = int(input('SeatID to book: '))
            tid, msg = book_ticket(cid, sid)
            print(f'Result: {msg}')

        elif choice == '4':
            generate_revenue_report()

        elif choice == '5':
            print('Goodbye!'); 
            break

if __name__ == '__main__':
    main()
