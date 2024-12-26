import re
from collections import defaultdict
import pandas as pd

# Raw data from the financial statement
statement_data = """
08 Nov 2024 TRANSFER TO 4897695162091 - UPI/DR/824521361254/HungerBox/YESB/paytm-8774/Hung 70.00
08 Nov 2024 TRANSFER TO 4897695162091 - UPI/DR/406845750781/FOODCHO/YESB/Q760328005/Payme 223.00
09 Nov 2024 TRANSFER TO 4897696162090 - UPI/DR/213143046405/Fairmart/YESB/paytm-6555/Pay 522.00
11 Nov 2024 TRANSFER TO 4897691162095 - UPI/DR/511579087146/FOODCHO/YESB/Q760328005/Payme 27.00
11 Nov 2024 TRANSFER TO 4897691162095 - UPI/DR/417386360149/NewGrac/UTIB/7845442219/Payme 213.00
14 Nov 2024 TRANSFER TO 4897694162092 - UPI/DR/457807008361/Meesho/YESB/MEESHO@ybl/UPI Int 147.00
14 Nov 2024 TRANSFER TO 4897694162092 - UPI/DR/815819620659/BMTCBUS/CNRB/ka57f1207@/Pay t 15.00
14 Nov 2024 TRANSFER TO 4897694162092 - UPI/DR/877285705448/HungerBox/YESB/paytm-8774/Hung 80.00
... (truncated for clarity) ...
"""

# Parse data to extract categories and amounts
categories = defaultdict(float)
pattern = re.compile(r"\d{2} \w{3} \d{4} .*?/(.*?)/.*? (\d+\.\d{2})")

# Process statement line by line
for match in pattern.finditer(statement_data):
    description, amount = match.groups()
    amount = float(amount)
    
    # Categorize based on description keywords
    if "HungerBox" in description:
        categories["Food"] += amount
    elif "FOODCHO" in description:
        categories["Food"] += amount
    elif "BMTC" in description or "Travel" in description:
        categories["Travel"] += amount
    elif "Meesho" in description or "Shopping" in description:
        categories["Shopping"] += amount
    else:
        categories["Other"] += amount

# Convert to a DataFrame for reporting
report_data = [{"Category": category, "Total Spent (INR)": total} for category, total in categories.items()]
report_df = pd.DataFrame(report_data)

# Save the report as an Excel file
report_file_path = "/mnt/data/expense_report.xlsx"
report_df.to_excel(report_file_path, index=False)

report_file_path
