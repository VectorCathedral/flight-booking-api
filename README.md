# ✈️ Flight Booking Database Project (Areyeng Flights) — Part 2

This is the continuation of the [Flight Booking Database](https://github.com/VectorCathedral/flight-booking-database) project. In this second part, we’ve built a RESTful API using **Flask** in **Python**🐍 and **Microsoft SQL Server** 🗄️ to interact with the flight booking system.

---

## 📦 Features

- ➕ Add a new customer via `POST /add_customer`
- 🔍 Retrieve reservation details via `GET /reservations/<resID>/<custID>`
- ❌ Delete a reservation via `DELETE /delete_reservation/<resID>/<custID>`
- ⚠️ 404 error handler for undefined routes

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/VectorCathedral/flight-booking-database
cd flight-booking-database
Or continue in your own repo if this is a fork or related project.
```

### 2. Create a .env file
Create a .env file in your project root and add the following:

password=YOUR_SQL_SERVER_PASSWORD

This is used to securely connect to your SQL Server instance.

### 3. Customize the SQL Connection String
Inside the Python code, the SQL Server connection string looks like this:

```con_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=SHP\\SQLEXPRESS;"
    "Database=AREYENG_FLIGHTS;"
    "uid=Admin;"
    f"pwd={password};"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)
```
🔧 Update the Server, uid, and Database values to match your local SQL Server setup.

### 4. Install Dependencies
pip install flask python-dotenv pyodbc
Make sure your environment has ODBC Driver 18 for SQL Server installed.

🚀 Run the App
python app.py
The Flask server will start in debug mode at http://127.0.0.1:5000.

📡 Endpoints Overview:

➕ POST /add_customer
Body JSON example:

```json
{
  "idNum": "1234567890123",
  "email": "example@email.com",
  "phone": "0123456789",
  "fName": "John",
  "lName": "Doe",
  "postalAddress": "123 Main Street",
  "age": 30
}
```

🔍 GET /reservations/< resID >/< custID >:

Returns a reservation for a specific reservation ID and customer ID.

❌ DELETE /delete_reservation/< resID >/< custID >:
Deletes a reservation.

🧠 Notes
The database (AREYENG_FLIGHTS) should already exist and be populated as per Part 1 of this project.

You must configure your SQL Server to accept TCP/IP connections and install the correct ODBC driver.
