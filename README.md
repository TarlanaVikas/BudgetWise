<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=180&section=header&text=BudgetWise&fontSize=55&fontColor=ffffff&fontAlignY=35&desc=Smart%20Personal%20Finance%20Management&descAlignY=60&descSize=18&animation=fadeIn" width="100%"/>

# BudgetWise

### 💰 Smart Personal Finance Management Application

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Finance-Management-2C5364?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Testing-Unittest-555555?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-2E7D32?style=for-the-badge"/>
</p>

<p>
  <b>Track • Budget • Analyze • Manage</b>
</p>

</div>

---

## 📌 About

**BudgetWise** is a personal finance management application designed to help users organize, monitor, and understand their day-to-day financial activities from a single platform.

The application provides functionality for managing income and expenses, setting category-based budgets, generating financial reports, and protecting important financial records through backup and restore capabilities.

BudgetWise focuses on making financial tracking simple and structured, allowing users to maintain a clear view of their spending habits, available budget, total income, expenses, and savings.

---

## 🎯 Problem Statement

Managing personal finances manually can become difficult when income, expenses, budgets, and financial records are maintained across different sources.

Common challenges include:

* Difficulty tracking daily expenses
* Lack of organized financial records
* Overspending in specific categories
* Limited visibility into monthly and yearly spending
* Difficulty comparing income with expenses
* Risk of losing important financial records
* Manual calculation of savings and remaining budgets

**BudgetWise** addresses these challenges by bringing essential personal finance management functions together into one application.

---

## ✨ Key Features

### 👤 User Management

* User registration
* User login
* Account-based access
* Organized personal financial records

### 💵 Income Management

* Add income transactions
* Categorize income sources
* Record income amounts
* View income history
* Track total income

### 💸 Expense Management

* Add expense transactions
* Categorize expenses
* Record spending amounts
* View expense history
* Monitor overall spending

### 📊 Budget Management

* Create category-based budgets
* Set monthly spending limits
* Monitor budget utilization
* Check remaining budget
* Identify categories approaching their limits

### 📈 Financial Reports

* Generate monthly financial reports
* Generate yearly financial reports
* View total income
* View total expenses
* Calculate savings
* Analyze spending by category

### 💾 Backup & Restore

* Backup financial data
* Preserve important records
* Restore previously backed-up data
* Reduce the risk of losing financial information

---

## 🔄 Application Workflow

```text
                    ┌─────────────────┐
                    │     BudgetWise  │
                    └────────┬────────┘
                             │
                     ┌───────▼───────┐
                     │ Register/Login │
                     └───────┬───────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────▼─────┐  ┌────▼─────┐  ┌────▼─────┐
        │   Income  │  │ Expenses │  │  Budgets │
        └─────┬─────┘  └────┬─────┘  └────┬─────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                      ┌──────▼──────┐
                      │   Reports   │
                      └──────┬──────┘
                             │
                 ┌───────────┴───────────┐
                 │                       │
          ┌──────▼──────┐        ┌──────▼──────┐
          │   Savings   │        │   Analysis  │
          └─────────────┘        └─────────────┘

                      ┌──────────────┐
                      │Backup/Restore│
                      └──────────────┘
```

---

## 🧩 Core Modules

| Module                 | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| **User Management**    | Handles registration and login functionality                |
| **Income Management**  | Records and manages income transactions                     |
| **Expense Management** | Records and categorizes expenses                            |
| **Budget Management**  | Creates and monitors spending limits                        |
| **Report Generation**  | Produces monthly and yearly financial summaries             |
| **Backup & Restore**   | Protects and recovers financial records                     |
| **Testing**            | Validates application functionality through automated tests |

---

## 💡 Example Financial Scenario

A user records the following transactions:

### Income

```text
Salary
₹5,000
```

### Expenses

```text
Food
₹1,000

Transport
₹500

Entertainment
₹300
```

### Monthly Budget

```text
Food
Budget: ₹3,000
Spent: ₹1,000
Remaining: ₹2,000
```

BudgetWise can use these records to provide an overview of:

```text
Total Income     : ₹5,000
Total Expenses   : ₹1,800
Remaining Amount : ₹3,200
```

This gives the user a clearer understanding of their current financial position.

---

## 📊 Financial Insights

BudgetWise organizes financial information into meaningful categories, helping users understand:

* Total income received
* Total amount spent
* Remaining funds
* Category-wise spending
* Budget utilization
* Monthly savings
* Yearly financial activity

This structured information can help users identify spending patterns and maintain better control over their budgets.

---

## 🛡️ Data Management

Financial information is important and should be protected from accidental loss.

BudgetWise includes **backup and restore functionality** that allows users to preserve their financial records and recover them when required.

The backup mechanism is designed to provide an additional layer of protection for important income, expense, and budget information.

---

## 🧪 Testing

BudgetWise includes automated testing using Python's built-in **UnitTest** framework.

Tests can be used to validate important application functionality such as:

* User operations
* Income management
* Expense management
* Budget calculations
* Report generation
* Data handling
* Backup and restore functionality

The testing structure helps maintain application reliability as new functionality is added.

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python" height="60"/>

<br><br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/UnitTest-Testing-555555?style=for-the-badge&logo=python&logoColor=white"/>

</div>

---

## 📂 Project Structure

```text
BudgetWise/
│
├── main.py
│
├── tests/
│   └── ...
│
└── README.md
```

---

## 🌟 Benefits

BudgetWise provides a centralized way to manage personal financial information.

### ✔ Organized Finance Tracking

Keep income and expense records structured and accessible.

### ✔ Better Budget Awareness

Monitor spending against predefined category budgets.

### ✔ Financial Visibility

Understand income, expenses, and savings through reports.

### ✔ Data Protection

Maintain backups of important financial information.

### ✔ Simple Management

Bring everyday financial activities into a single application.

### ✔ Testable Architecture

Automated tests help verify important application functionality.

---

## 🎯 Use Cases

BudgetWise can be useful for:

* 👨‍🎓 Students managing monthly expenses
* 👩‍💼 Professionals tracking personal spending
* 🏠 Individuals managing household budgets
* 💰 Users monitoring savings goals
* 📊 Anyone looking for a structured way to track personal finances


---

## 🏆 Project Vision

BudgetWise aims to provide a simple and reliable financial management experience where users can **record their finances, control their spending, monitor budgets, and understand their financial progress**.

The project combines practical finance management with structured data handling and automated testing to create a maintainable personal finance solution.

---

<div align="center">

### 💰 Budget Smarter. Spend Better. Live Better.

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=120&section=footer" width="100%"/>

</div>
