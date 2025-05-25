
import pandas as pd
from pathlib import Path
import os
import subprocess

# קריאה לקובץ CSV הגולמי
input_csv = "raw_propstream_like.csv"
df = pd.read_csv(input_csv)

# פונקציית ניתוח בסיסית - הערכת ROI ופליפ
def analyze_deal(row):
    arv = row["Estimated ARV"]
    price = row["Asking Price"]
    sqft = row["Square Footage"]
    repair_cost = 25_000  # ערך פיקטיבי
    all_in = price + repair_cost
    roi_flip = (arv - all_in) / all_in
    return {
        "ID": f"deal{row.name+1:03}",
        "כתובת": row["Address"],
        "ZIP": row["Zip"],
        "ARV": f"${arv:,}",
        "מחיר מבוקש": f"${price:,}",
        "שיפוץ": f"${repair_cost:,}",
        "All-In": f"${all_in:,}",
        "ROI פליפ": f"{roi_flip:.2%}",
        "מאושר": "כן" if roi_flip > 0.12 else "לא",
        "סיכום": "רווחי" if roi_flip > 0.12 else "סיכון גבוה"
    }

# ניתוח כל העסקאות
results = [analyze_deal(row) for _, row in df.iterrows()]
df_output = pd.DataFrame(results)

# יצירת קבצי HTML
base_path = Path(".")
for row in results:
    html = f"""<!DOCTYPE html>
<html lang='he' dir='rtl'>
<head>
    <meta charset='UTF-8'>
    <title>{row['ID']}</title>
</head>
<body>
    <h2>ניתוח עסקה – {row['כתובת']}</h2>
    <ul>
        <li><strong>ZIP:</strong> {row['ZIP']}</li>
        <li><strong>ARV:</strong> {row['ARV']}</li>
        <li><strong>מחיר מבוקש:</strong> {row['מחיר מבוקש']}</li>
        <li><strong>שיפוץ:</strong> {row['שיפוץ']}</li>
        <li><strong>All-In:</strong> {row['All-In']}</li>
        <li><strong>ROI פליפ:</strong> {row['ROI פליפ']}</li>
        <li><strong>מאושר:</strong> {row['מאושר']}</li>
    </ul>
    <h3>סיכום:</h3>
    <p>{row['סיכום']}</p>
</body>
</html>"""
    html_path = base_path / f"{row['ID']}.html"
    html_path.write_text(html, encoding="utf-8")

# כתיבת קובץ אקסל עם קישורים ל-HTML
df_output["צפה"] = df_output["ID"].apply(lambda x: f'=HYPERLINK("https://friesiancapital.github.io/Analysis-/{x}.html", "צפה")')
df_output.to_excel("deal_links.xlsx", index=False)

# ביצוע git add, commit, push
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Auto-upload deals"], check=True)
subprocess.run(["git", "push"], check=True)

print("ההרצה הושלמה – HTML נוצר, קובץ Excel מוכן והכל עלה ל-GitHub.")
