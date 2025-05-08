# AI-Powered Financial Health Summary 💸🤖

## 📌 Project Overview

AI-Powered Financial Health Summary is a Python-based application that uses OpenAI's GPT to analyze bank statements and generate a financial summary report. This helps users understand their spending habits and provides insights for better budgeting.

---

## 🚀 Features

- Accepts `.txt` and `.csv` bank statements as input.
- Uses OpenAI API to generate a summarized financial report.
- Categorizes expenses and provides suggestions for better financial management.
- Error handling for:

  - File not found
  - Unsupported file formats
  - Empty files
  - API connection issues

---

## 🗂️ Folder Structure

```
ai-financial-summary/
│
├── main.py                  # Main application entry point
├── bank_statement.py        # Reads and processes the bank statement
├── financial_analyzer.py    # Sends data to OpenAI and retrieves summary
├── .env                     # Stores environment variables (API key)
├── .gitignore               # Prevents secret files from being tracked
├── requirements.txt         # Lists all dependencies
├── statement.txt            # Sample bank statement
└── README.md                # Project documentation
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Ladyhelen-dev/AI-Powered-Financial-Health-Summary.git
   cd AI-Powered-Financial-Health-Summary
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your OpenAI API key:**

   - Create a `.env` file in the root of the project:

   ```bash
   touch .env
   ```

   - Add your API key inside:

   ```env
   OPENAI_API_KEY=sk-your-openai-api-key
   ```

5. **Run the application:**

   ```bash
   python3 main.py
   ```

---

## 💡 Usage Example

```bash
💡 AI-Powered Financial Health Summary

Enter the path to your bank statement file (.txt or .csv): statement.txt

📄 File content preview:
04/01 - Uber - ₦4000
04/02 - Jumia - ₦8500
...

🔎 Analyzing your statement...

=== Financial Summary ===
- Total Income: Nil
- Total Expenses: ₦49,000

Breakdown:
- Transportation: ₦4000
- Online Shopping: ₦8500
...
```

---

## 🔄 Future Improvements

- Add support for PDF bank statements
- Multi-language support
- Graphical representation of spending categories

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
