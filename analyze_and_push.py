
import pandas as pd
import os
from jinja2 import Template
from input_adapter import adapt_input

input_file = "deal_files.csv"
df = pd.read_csv(input_file)

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

with open("template.html", "r", encoding="utf-8") as f:
    template = Template(f.read())

results = []

for index, row in df.iterrows():
    data = adapt_input(row)
    html_output = template.render(**data)

    filename = f"{data['id']}.html"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_output)

    url = f'https://friesiancapital.github.io/analysis/{filename}'
    results.append(["עסקה " + str(index + 1), data["score"], f'=HYPERLINK("{url}", "צפה")',
                    data["address"], data["asking_price"], data["all_in"],
                    data["arv"], data["roi_flip"], data["roi_rent"], data["equity_stuck"]])

summary_df = pd.DataFrame(results, columns=["עסקה", "ציון", "ניתוח מלא", "כתובת מלאה", "מחיר מבוקש",
                                            "All-In", "ARV", "ROI Flip", "ROI Rent", "הון עצמי תקוע"])
summary_df = summary_df.T
summary_df.columns = summary_df.iloc[0]
summary_df = summary_df[1:]
summary_df.to_csv("analysis_table.csv", index=True, encoding="utf-8-sig")


# ביצוע git push אוטומטי (מתוך הסקריפט)
import subprocess

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "auto update from script"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("הקבצים הועלו בהצלחה ל-GitHub.")
except subprocess.CalledProcessError as e:
    print("שגיאה בהרצת git:", e)
