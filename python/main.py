"""
Sports Ticketing Management System — Flask Web App
Run: pip install flask mysql-connector-python
     python app.py
Open: http://127.0.0.1:5000
"""

from flask import Flask, render_template_string, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sports_ticketing_2025'

# ── DB CONNECTION ─────────────────────────────────────────────
def get_connection():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',           # change to your MySQL user
            password='',           # change to your MySQL password
            database='sports_ticketing',
            charset='utf8mb4'
        )
        return conn
    except Error as e:
        print(f'DB Error: {e}')
        return None

# ── BASE TEMPLATE ─────────────────────────────────────────────
BASE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sports Ticketing System</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', sans-serif; background: #f5f5f5; color: #222; }

    /* NAV */
    nav { background: #1a1a1a; padding: 0 32px; display: flex; align-items: center; gap: 0; height: 56px; }
    nav .brand { color: #fff; font-size: 16px; font-weight: 600; margin-right: 32px; white-space: nowrap; }
    nav a { color: #ccc; text-decoration: none; padding: 0 16px; height: 56px; display: flex; align-items: center; font-size: 14px; transition: background .15s; }
    nav a:hover, nav a.active { background: #333; color: #fff; }

    /* LAYOUT */
    .container { max-width: 1100px; margin: 32px auto; padding: 0 24px; }
    h1 { font-size: 22px; font-weight: 600; margin-bottom: 20px; color: #111; }
    h2 { font-size: 16px; font-weight: 600; margin-bottom: 12px; color: #333; }

    /* CARDS */
    .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 28px; }
    .card { background: #fff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; }
    .card .num { font-size: 32px; font-weight: 700; color: #111; }
    .card .label { font-size: 13px; color: #666; margin-top: 4px; }
    .card.highlight .num { color: #1a73e8; }

    /* TABLE */
    .table-wrap { background: #fff; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden; margin-bottom: 28px; }
    table { width: 100%; border-collapse: collapse; font-size: 14px; }
    thead { background: #1a1a1a; color: #fff; }
    th { padding: 11px 14px; text-align: left; font-weight: 500; font-size: 13px; }
    td { padding: 10px 14px; border-bottom: 1px solid #f0f0f0; }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background: #fafafa; }

    /* BADGES */
    .badge { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 12px; font-weight: 500; }
    .badge-green  { background: #e6f4ea; color: #1e7e34; }
    .badge-red    { background: #fce8e6; color: #c0392b; }
    .badge-blue   { background: #e8f0fe; color: #1a73e8; }
    .badge-gray   { background: #f1f1f1; color: #555; }
    .badge-orange { background: #fff3e0; color: #e65100; }

    /* FORMS */
    .form-box { background: #fff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 24px; margin-bottom: 28px; }
    .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 14px; }
    .form-group { display: flex; flex-direction: column; gap: 5px; }
    label { font-size: 13px; font-weight: 500; color: #444; }
    select, input { padding: 9px 12px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px; background: #fff; }
    select:focus, input:focus { outline: none; border-color: #1a73e8; }
    .btn { padding: 10px 22px; border: none; border-radius: 6px; font-size: 14px; font-weight: 500; cursor: pointer; transition: opacity .15s; }
    .btn-primary { background: #1a1a1a; color: #fff; }
    .btn-primary:hover { opacity: .85; }
    .btn-sm { padding: 5px 14px; font-size: 13px; border-radius: 5px; text-decoration: none; display: inline-block; }
    .btn-book { background: #1a73e8; color: #fff; border: none; cursor: pointer; }
    .btn-book:hover { opacity: .85; }

    /* ALERTS */
    .alert { padding: 12px 16px; border-radius: 7px; margin-bottom: 16px; font-size: 14px; }
    .alert-success { background: #e6f4ea; color: #1e7e34; border: 1px solid #b7dfbd; }
    .alert-error   { background: #fce8e6; color: #c0392b; border: 1px solid #f5c6c2; }

    /* REVENUE BAR */
    .rev-bar { display: flex; align-items: center; gap: 10px; }
    .rev-bar-fill { height: 8px; border-radius: 4px; background: #1a73e8; min-width: 4px; }
    .rev-amt { font-size: 13px; color: #444; white-space: nowrap; }

    /* SECTION TITLE */
    .section-title { font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: .06em; color: #888; margin-bottom: 12px; }
  </style>
</head>
<body>
<nav>
  <span class="brand">⚽ Sports Ticketing</span>
  <a href="/" class="{{ 'active' if active=='dashboard' else '' }}">Dashboard</a>
  <a href="/events" class="{{ 'active' if active=='events' else '' }}">Events</a>
  <a href="/book" class="{{ 'active' if active=='book' else '' }}">Book Ticket</a>
  <a href="/customers" class="{{ 'active' if active=='customers' else '' }}">Customers</a>
  <a href="/revenue" class="{{ 'active' if active=='revenue' else '' }}">Revenue</a>
</nav>
<div class="container">
  {% for msg in get_flashed_messages(category_filter=['success']) %}
    <div class="alert alert-success">✓ {{ msg }}</div>
  {% endfor %}
  {% for msg in get_flashed_messages(category_filter=['error']) %}
    <div class="alert alert-error">✗ {{ msg }}</div>
  {% endfor %}
  {{ content }}
</div>
</body>
</html>
"""

def render(content, active=''):
    from flask import get_flashed_messages
    return render_template_string(BASE, content=content, active=active)

# ── DASHBOARD ─────────────────────────────────────────────────
@app.route('/')
def dashboard():
    conn = get_connection()
    stats = {'events': 0, 'customers': 0, 'tickets_sold': 0, 'total_revenue': 0}
    recent = []
    top_events = []
    if conn:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT COUNT(*) AS c FROM Events"); stats['events'] = cur.fetchone()['c']
        cur.execute("SELECT COUNT(*) AS c FROM Customers"); stats['customers'] = cur.fetchone()['c']
        cur.execute("SELECT COUNT(*) AS c FROM Tickets WHERE Status='Sold'"); stats['tickets_sold'] = cur.fetchone()['c']
        cur.execute("SELECT COALESCE(SUM(Price),0) AS r FROM Tickets WHERE Status='Sold'"); stats['total_revenue'] = cur.fetchone()['r']
        cur.execute("""
            SELECT t.TicketID, c.CustomerName, e.EventName, s.SeatNumber, t.TicketType,
                   t.Price, t.PurchaseDate
            FROM Tickets t
            JOIN Events e ON t.EventID=e.EventID
            JOIN Seats s ON t.SeatID=s.SeatID
            LEFT JOIN Customers c ON t.CustomerID=c.CustomerID
            WHERE t.Status='Sold'
            ORDER BY t.PurchaseDate DESC LIMIT 8
        """)
        recent = cur.fetchall()
        cur.execute("""
            SELECT e.EventName, e.Sport,
                   COUNT(CASE WHEN t.Status='Sold' THEN 1 END) AS Sold,
                   COALESCE(SUM(CASE WHEN t.Status='Sold' THEN t.Price ELSE 0 END),0) AS Revenue
            FROM Events e LEFT JOIN Tickets t ON e.EventID=t.EventID
            GROUP BY e.EventID ORDER BY Revenue DESC LIMIT 5
        """)
        top_events = cur.fetchall()
        cur.close(); conn.close()

    max_rev = max((r['Revenue'] for r in top_events), default=1) or 1

    rows = ''.join(f"""
      <tr>
        <td>#{r['TicketID']}</td>
        <td>{r['CustomerName'] or '—'}</td>
        <td>{r['EventName']}</td>
        <td>{r['SeatNumber']}</td>
        <td><span class="badge badge-blue">{r['TicketType']}</span></td>
        <td>{int(r['Price']):,} VND</td>
        <td>{str(r['PurchaseDate'])[:16] if r['PurchaseDate'] else '—'}</td>
      </tr>""" for r in recent)

    ev_rows = ''.join(f"""
      <tr>
        <td>{r['EventName']}</td>
        <td>{r['Sport']}</td>
        <td>{r['Sold']}</td>
        <td>
          <div class="rev-bar">
            <div class="rev-bar-fill" style="width:{int(r['Revenue']/max_rev*180)}px"></div>
            <span class="rev-amt">{int(r['Revenue']):,} VND</span>
          </div>
        </td>
      </tr>""" for r in top_events)

    content = f"""
    <h1>Dashboard</h1>
    <div class="cards">
      <div class="card"><div class="num">{stats['events']}</div><div class="label">Total Events</div></div>
      <div class="card"><div class="num">{stats['customers']}</div><div class="label">Registered Customers</div></div>
      <div class="card highlight"><div class="num">{stats['tickets_sold']}</div><div class="label">Tickets Sold</div></div>
      <div class="card highlight"><div class="num">{int(stats['total_revenue']):,}</div><div class="label">Total Revenue (VND)</div></div>
    </div>
    <h2>Revenue by Event</h2>
    <div class="table-wrap">
      <table><thead><tr><th>Event</th><th>Sport</th><th>Sold</th><th>Revenue</th></tr></thead>
      <tbody>{ev_rows}</tbody></table>
    </div>
    <h2>Recent Transactions</h2>
    <div class="table-wrap">
      <table><thead><tr><th>Ticket</th><th>Customer</th><th>Event</th><th>Seat</th><th>Type</th><th>Price</th><th>Date</th></tr></thead>
      <tbody>{rows}</tbody></table>
    </div>"""
    return render(content, 'dashboard')

# ── EVENTS ────────────────────────────────────────────────────
@app.route('/events')
def events():
    conn = get_connection()
    rows_html = ''
    if conn:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT e.*, 
                   COUNT(DISTINCT s.SeatID) AS TotalSeatsCreated,
                   SUM(s.IsAvailable) AS AvailSeats,
                   COUNT(CASE WHEN t.Status='Sold' THEN 1 END) AS SoldTickets,
                   COALESCE(SUM(CASE WHEN t.Status='Sold' THEN t.Price ELSE 0 END),0) AS Revenue
            FROM Events e
            LEFT JOIN Seats s ON e.EventID=s.EventID
            LEFT JOIN Tickets t ON e.EventID=t.EventID
            GROUP BY e.EventID ORDER BY e.EventDate
        """)
        events_data = cur.fetchall()
        cur.close(); conn.close()
        badge = {'Upcoming':'badge-blue','Ongoing':'badge-orange','Completed':'badge-gray','Cancelled':'badge-red'}
        for ev in events_data:
            b = badge.get(ev['Status'], 'badge-gray')
            rows_html += f"""<tr>
              <td><strong>{ev['EventName']}</strong></td>
              <td>{ev['Sport']}</td>
              <td>{str(ev['EventDate'])[:10]}</td>
              <td>{ev['Venue']}</td>
              <td><span class="badge {b}">{ev['Status']}</span></td>
              <td>{ev['SoldTickets']}</td>
              <td>{int(ev['Revenue']):,} VND</td>
              <td><a href="/book?event_id={ev['EventID']}" class="btn btn-sm btn-book">Book</a></td>
            </tr>"""

    content = f"""
    <h1>Events</h1>
    <div class="table-wrap">
      <table><thead><tr>
        <th>Event Name</th><th>Sport</th><th>Date</th><th>Venue</th>
        <th>Status</th><th>Sold</th><th>Revenue</th><th></th>
      </tr></thead><tbody>{rows_html}</tbody></table>
    </div>"""
    return render(content, 'events')

# ── BOOK TICKET ───────────────────────────────────────────────
@app.route('/book', methods=['GET', 'POST'])
def book():
    conn = get_connection()
    events_list, seats_list, customers_list = [], [], []
    selected_event = request.args.get('event_id', '')

    if conn:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT EventID, EventName, EventDate FROM Events WHERE Status IN ('Upcoming','Ongoing') ORDER BY EventDate")
        events_list = cur.fetchall()
        cur.execute("SELECT CustomerID, CustomerName, PhoneNumber FROM Customers ORDER BY CustomerName")
        customers_list = cur.fetchall()
        if selected_event:
            cur.execute("""
                SELECT s.SeatID, s.SeatNumber, s.SeatType, s.Section, t.Price
                FROM Seats s JOIN Tickets t ON s.SeatID=t.SeatID
                WHERE s.EventID=%s AND s.IsAvailable=1 AND t.Status='Available'
                ORDER BY s.SeatType, s.SeatNumber
            """, (selected_event,))
            seats_list = cur.fetchall()
        cur.close(); conn.close()

    if request.method == 'POST':
        customer_id  = request.form.get('customer_id')
        seat_id      = request.form.get('seat_id')
        box_office   = request.form.get('box_office_id', 1)
        event_id_post = request.form.get('event_id')

        conn2 = get_connection()
        if conn2:
            cur2 = conn2.cursor()
            try:
                cur2.execute("SET @tid=0; SET @msg='';")
                cur2.execute("CALL sp_book_ticket(%s,%s,%s,@tid,@msg)", (customer_id, seat_id, box_office))
                conn2.commit()
                cur2.execute("SELECT @tid, @msg")
                res = cur2.fetchone()
                tid, msg = res[0], res[1]
                if tid and tid > 0:
                    flash(f'Booking successful! Ticket ID = {tid}', 'success')
                else:
                    flash(str(msg) or 'Seat already booked.', 'error')
            except Error as e:
                flash(str(e), 'error')
            finally:
                cur2.close(); conn2.close()
        return redirect(url_for('book', event_id=event_id_post or ''))

    ev_opts = ''.join(f'<option value="{e["EventID"]}" {"selected" if str(e["EventID"])==str(selected_event) else ""}>{e["EventName"]} ({str(e["EventDate"])[:10]})</option>' for e in events_list)
    cust_opts = ''.join(f'<option value="{c["CustomerID"]}">{c["CustomerName"]} — {c["PhoneNumber"]}</option>' for c in customers_list)

    seats_html = ''
    if seats_list:
        seat_rows = ''.join(f"""<tr>
          <td>{s['SeatNumber']}</td>
          <td><span class="badge {'badge-orange' if s['SeatType']=='VIP' else 'badge-blue' if s['SeatType']=='Standard' else 'badge-gray'}">{s['SeatType']}</span></td>
          <td>{s['Section']}</td>
          <td>{int(s['Price']):,} VND</td>
          <td><button type="button" class="btn btn-sm btn-book" onclick="selectSeat({s['SeatID']},'{s['SeatNumber']}',{int(s['Price'])})">Select</button></td>
        </tr>""" for s in seats_list)
        seats_html = f"""
        <h2>Available Seats</h2>
        <div class="table-wrap">
          <table><thead><tr><th>Seat</th><th>Type</th><th>Section</th><th>Price</th><th></th></tr></thead>
          <tbody>{seat_rows}</tbody></table>
        </div>"""
    elif selected_event:
        seats_html = '<p style="color:#888;margin-bottom:20px;">No available seats for this event.</p>'

    content = f"""
    <h1>Book a Ticket</h1>
    <form method="GET" style="margin-bottom:20px;display:flex;gap:12px;align-items:flex-end;">
      <div class="form-group" style="flex:1">
        <label>Select Event</label>
        <select name="event_id" onchange="this.form.submit()">
          <option value="">-- Choose an event --</option>
          {ev_opts}
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Load Seats</button>
    </form>
    {seats_html}
    <div id="booking-form" style="display:{'block' if seats_list else 'none'}">
    <form method="POST" class="form-box">
      <input type="hidden" name="event_id" value="{selected_event}">
      <input type="hidden" name="seat_id" id="seat_id_hidden">
      <h2>Confirm Booking</h2>
      <div class="form-row">
        <div class="form-group">
          <label>Customer</label>
          <select name="customer_id" required>
            <option value="">-- Select customer --</option>
            {cust_opts}
          </select>
        </div>
        <div class="form-group">
          <label>Selected Seat</label>
          <input type="text" id="seat_display" readonly placeholder="Click a seat above">
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label>Box Office</label>
          <select name="box_office_id">
            <option value="1">My Dinh Ticket Office</option>
            <option value="2">Tu Son Ticket Office</option>
            <option value="3">Online Ticket Office</option>
          </select>
        </div>
        <div class="form-group">
          <label>Price</label>
          <input type="text" id="price_display" readonly>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Confirm Booking</button>
    </form>
    </div>
    <script>
    function selectSeat(id, num, price) {{
      document.getElementById('seat_id_hidden').value = id;
      document.getElementById('seat_display').value = num;
      document.getElementById('price_display').value = price.toLocaleString() + ' VND';
      document.getElementById('booking-form').style.display = 'block';
    }}
    </script>"""
    return render(content, 'book')

# ── CUSTOMERS ─────────────────────────────────────────────────
@app.route('/customers')
def customers():
    conn = get_connection()
    rows_html = ''
    if conn:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT c.*, 
                   COUNT(t.TicketID) AS TicketsBought,
                   COALESCE(SUM(t.Price),0) AS TotalSpent
            FROM Customers c
            LEFT JOIN Tickets t ON c.CustomerID=t.CustomerID AND t.Status='Sold'
            GROUP BY c.CustomerID ORDER BY TotalSpent DESC
        """)
        for c in cur.fetchall():
            rows_html += f"""<tr>
              <td><strong>{c['CustomerName']}</strong></td>
              <td>{c['PhoneNumber']}</td>
              <td>{c['Address'] or '—'}</td>
              <td>{c['TicketsBought']}</td>
              <td>{int(c['TotalSpent']):,} VND</td>
            </tr>"""
        cur.close(); conn.close()

    content = f"""
    <h1>Customers</h1>
    <div class="table-wrap">
      <table><thead><tr>
        <th>Name</th><th>Phone</th><th>Address</th><th>Tickets Bought</th><th>Total Spent</th>
      </tr></thead><tbody>{rows_html}</tbody></table>
    </div>"""
    return render(content, 'customers')

# ── REVENUE ───────────────────────────────────────────────────
@app.route('/revenue')
def revenue():
    conn = get_connection()
    rev_rows, seat_rows = '', ''
    totals = {'sold': 0, 'revenue': 0, 'cancelled': 0}
    if conn:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM vw_revenue_by_event")
        rev_data = cur.fetchall()
        cur.execute("SELECT * FROM vw_seat_availability ORDER BY EventName, SeatType")
        seat_data = cur.fetchall()
        cur.execute("SELECT COUNT(*) AS c FROM Tickets WHERE Status='Sold'"); totals['sold'] = cur.fetchone()['c']
        cur.execute("SELECT COALESCE(SUM(Price),0) AS r FROM Tickets WHERE Status='Sold'"); totals['revenue'] = cur.fetchone()['r']
        cur.execute("SELECT COUNT(*) AS c FROM Tickets WHERE Status='Cancelled'"); totals['cancelled'] = cur.fetchone()['c']
        cur.close(); conn.close()

        max_r = max((r['TotalRevenue'] for r in rev_data), default=1) or 1
        for r in rev_data:
            pct = int((r['TotalRevenue'] or 0)/max_r*160)
            rev_rows += f"""<tr>
              <td><strong>{r['EventName']}</strong></td>
              <td>{str(r['EventDate'])[:10]}</td>
              <td>{r['TicketsSold']}</td>
              <td>{int(r['TotalRevenue'] or 0):,} VND</td>
              <td>{int(r['AvgTicketPrice'] or 0):,} VND</td>
              <td><div style="background:#e8f0fe;border-radius:4px;height:8px;width:160px">
                  <div style="background:#1a73e8;height:8px;border-radius:4px;width:{pct}px"></div>
              </div></td>
            </tr>"""

        for s in seat_data:
            occ = (s['OccupiedSeats'] or 0)
            tot = (s['TotalSeats'] or 1)
            pct = int(occ/tot*100)
            seat_rows += f"""<tr>
              <td>{s['EventName']}</td>
              <td><span class="badge {'badge-orange' if s['SeatType']=='VIP' else 'badge-blue' if s['SeatType']=='Standard' else 'badge-gray'}">{s['SeatType']}</span></td>
              <td>{s['TotalSeats']}</td>
              <td>{s['AvailableSeats']}</td>
              <td>{s['OccupiedSeats']}</td>
              <td>
                <div style="display:flex;align-items:center;gap:8px">
                  <div style="background:#eee;border-radius:4px;height:8px;width:80px">
                    <div style="background:{'#e53935' if pct>70 else '#43a047'};height:8px;border-radius:4px;width:{int(pct*0.8)}px"></div>
                  </div>
                  <span style="font-size:12px;color:#555">{pct}%</span>
                </div>
              </td>
            </tr>"""

    content = f"""
    <h1>Revenue Report</h1>
    <div class="cards">
      <div class="card highlight"><div class="num">{totals['sold']}</div><div class="label">Total Tickets Sold</div></div>
      <div class="card highlight"><div class="num">{int(totals['revenue']):,}</div><div class="label">Total Revenue (VND)</div></div>
      <div class="card"><div class="num">{totals['cancelled']}</div><div class="label">Cancelled Tickets</div></div>
    </div>
    <h2>Revenue by Event (vw_revenue_by_event)</h2>
    <div class="table-wrap">
      <table><thead><tr>
        <th>Event</th><th>Date</th><th>Tickets Sold</th><th>Total Revenue</th><th>Avg Price</th><th>Bar</th>
      </tr></thead><tbody>{rev_rows}</tbody></table>
    </div>
    <h2>Seat Availability (vw_seat_availability)</h2>
    <div class="table-wrap">
      <table><thead><tr>
        <th>Event</th><th>Seat Type</th><th>Total</th><th>Available</th><th>Occupied</th><th>Occupancy</th>
      </tr></thead><tbody>{seat_rows}</tbody></table>
    </div>"""
    return render(content, 'revenue')

# ── RUN ───────────────────────────────────────────────────────
if __name__ == '__main__':
    print("=" * 50)
    print("  Sports Ticketing Management System")
    print("  Open: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)