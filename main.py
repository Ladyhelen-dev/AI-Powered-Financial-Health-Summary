from bank_statement import BankStatement
from financial_analyzer import FinancialAnalyzer

def main():
    print("\n💡 AI-Powered Financial Health Summary\n")
    path = input("Enter the path to your bank statement file (.txt or .csv): ")
    
    statement = BankStatement(path)
    if not statement.read_file():
        print("\n💡 Try again with a valid file path or correct format.")
        return

    content = statement.get_content()
    if content:
        print("\n📄 File content preview:\n")
        print(content[:300])  # Print first 300 characters
        
        analyzer = FinancialAnalyzer()
        print("\n🔎 Analyzing your statement...\n")
        summary = analyzer.analyze(content)
        
        if summary:
            print("\n=== Financial Summary ===")
            print(summary)
        else:
            print("\n❌ Analysis failed. Please try again later.")

    print("\n✅ Program completed successfully. Exiting...")

if __name__ == "__main__":
    main()
