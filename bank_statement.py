import os

class BankStatement:
    def __init__(self, filepath):
        self._filepath = filepath
        self._content = None

    def read_file(self):
        """Read the file content and store it internally."""
        
        # ✅ Check if the file exists
        if not os.path.exists(self._filepath):
            print("❌ Error: File not found. Please check the path.")
            return False
        
        # ✅ Check if it's a supported file type
        if not self._filepath.endswith(('.txt', '.csv')):
            print("❌ Error: Unsupported file format. Only .txt or .csv files are allowed.")
            return False
        
        try:
            # ✅ Read the file content
            with open(self._filepath, 'r', encoding='utf-8') as file:
                self._content = file.read()
            
            # ✅ Check if it's empty
            if not self._content.strip():
                print("❌ Error: The file is empty.")
                return False

            return True

        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return False

    def get_content(self):
        """Return the raw content of the file."""
        return self._content
