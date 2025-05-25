
import csv
import pandas as pd
import os
from jinja2 import Template
import subprocess

# Load the CSV
data = pd.read_csv("deal_files.csv")

# Load the template
with open("template.html", "r", encoding="utf-8") as f:
    template_html = f.read()
template = Template(template_html)

# Load adapter
from input_adapter import adapt_input

# Create HTML files
summary = []
for _, row in data.iterrows():
    context = adapt_input(row)
    filename = f"{context['id']}.html"
    html_path = filename  # HTML יישמר ישירות בשורש
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(template.render(**context))
    url = f'https://friesiancapital.github.io/analysis/{filename}'
    summary.append({
        "ID": context["id"],
        "ציון": context["score"],
        "ניתוח מלא": f'=HYPERLINK("{url}", "צפה")',
        "כתובת": context["address"],
        "מחיר מבוקש": context["asking_price"],
        "All-In": context["all_in"],
        "ARV": context["arv"],
        "ROI Flip": context["roi_flip"],
        "ROI Rent": context["roi_rent"],
        "הון עצמי תקוע": context["equity_stuck"]
    })

# Save summary CSV
summary_df = pd.DataFrame(summary).T
summary_df.columns = [f"עסקה {i+1}" for i in range(len(summary_df.columns))]
summary_df.to_csv("analysis_table.csv", index=True, encoding="utf-8-sig")

# Git push
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "auto update from script"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("הקבצים הועלו בהצלחה ל-GitHub.")
except subprocess.CalledProcessError as e:
    print("שגיאה בהרצת git:", e)
