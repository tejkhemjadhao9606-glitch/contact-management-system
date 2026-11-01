# 💰 Personal Expense Analytics Dashboard - Python

A Python-based Personal Expense Analytics Dashboard that helps users record, manage, track, and analyze their daily expenses using Tkinter, MySQL, Pandas, NumPy, and Matplotlib.

## 📌 Features

- Interactive expense management dashboard
- Add new expense records
- Store expense details in a MySQL database
- View all expense transactions
- Search expenses by ID, category, description, or payment mode
- Update existing expense records
- Delete expense records
- Validate expense dates and amounts
- Display total expenses
- Calculate average transaction amount
- Identify the highest expense
- Display the top spending category
- Generate category-wise expense analysis
- Visualize daily expense trends
- Analyze payment mode distribution
- Display expense records in a table
- Refresh expense data automatically
- User-friendly Tkinter graphical interface

## 💾 Database Storage

The project uses a MySQL database named:

`personal_expense_db`

The database contains a table named:

`expenses`

The following information is stored:

- Expense ID
- Expense Date
- Category
- Description
- Amount
- Payment Mode

**Available Expense Categories:**

- Food
- Transport
- Education
- Shopping
- Rent
- Utilities
- Entertainment
- Healthcare
- Other

**Available Payment Modes:**

- Cash
- UPI
- Card
- Bank Transfer
- Other

## 📊 Expense Analytics

The analytics dashboard provides important financial insights.

**Summary Statistics:**

- Total Expenses – Displays the total amount spent.
- Average Transaction – Calculates the average amount spent per transaction.
- Highest Transaction – Identifies the highest individual expense.
- Top Category – Displays the category with the highest total spending.

**Data Visualization:**

- Category-wise Expenses – Displays spending across different categories using a bar chart.
- Daily Expense Trend – Shows daily spending patterns using a line chart.
- Payment Mode Distribution – Visualizes spending distribution using a pie chart.

## 🧠 Concepts Used

- Python Functions
- Tkinter GUI Development
- MySQL Database Connectivity
- SQL Queries
- Database Creation and Table Creation
- CRUD Operations
- Python Exception Handling
- Pandas DataFrames
- NumPy Numerical Operations
- Data Grouping and Analysis
- Matplotlib Data Visualization
- Bar Charts
- Line Charts
- Pie Charts
- `ttk.Treeview` Widget
- Form Handling
- Input Validation
- Date and Time Handling
- Conditional Statements
- Loops
- Database Transactions

## 📦 Libraries Used

Install the required libraries using:

```bash
pip install mysql-connector-python pandas numpy matplotlib
```

**Built-in Python Libraries:**

- `tkinter`
- `ttk`
- `messagebox`
- `datetime`

## ▶️ How to Run

**1. Install Python**

Make sure Python is installed on your computer.

**2. Install MySQL**

Install MySQL Server and make sure it is running.

**3. Install Required Libraries**

```bash
pip install mysql-connector-python pandas numpy matplotlib
```

**4. Configure MySQL Connection**

Update your MySQL username and password in the Python file.

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_mysql_password"
DB_NAME = "personal_expense_db"
```

**5. Run the Python File**

```bash
python your_file_name.py
```

Replace `your_file_name.py` with your actual Python filename.

**6. Start Managing Expenses**

The application automatically creates the database and required expenses table
