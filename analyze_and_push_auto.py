
import pandas as pd
from pathlib import Path
import os
import subprocess

# חיפוש הקובץ האחרון בתיקייה עם סיומת .csv
csv_files = sorted(Path('.').glob("*.csv"), key=os.path.getmtime, reverse=True)
if not csv_files:
    raise FileNotFoundError("לא נמצא קובץ CSV בתיקייה.")
input_csv = csv_files[0]

# קריאת הקובץ
df = pd.read_csv(input_csv)

# פונקציית ניתוח בסיסית
def analyze(row):
    arv = row.get("Estimated ARV", 0)
    price = row.get("Asking Price", 0)
    rent = row.get("Estimated Rent", 0)
    repair = 25000
    all_in = price + repair
    roi_flip = (arv - all_in) / all_in if all_in else 0
    roi_rent = ((rent * 12) / all_in) if all_in else 0
    return {
        "ID": f"deal{row.name+1:03}",
        "כתובת": row.get("Address", ""),
        "ZIP": row.get("Zip", ""),
        "ARV": f"${arv:,.0f}",
        "מחיר מבוקש": f"${price:,.0f}",
        "שיפוץ": f"${repair:,.0f}",
        "All-In": f"${all_in:,.0f}",
        "ROI פליפ": f"{roi_flip:.2%}",
        "ROI שכירות": f"{roi_rent:.2%}",
        "מאושר": "כן" if roi_flip > 0.12 else "לא",
        "סיכום": "רווחי" if roi_flip > 0.12 else "גבולי/לא משתלם"
    }

# הפקת תוצאות
results = [analyze(row) for _, row in df.iterrows()]
df_out = pd.DataFrame(results)

# בניית קובצי HTML
for row in results:
    html = f"""<!DOCTYPE html>
<html lang='he' dir='rtl'>
<head><meta charset='UTF-8'><title>{row['ID']}</title></head>
<body>
<h2>ניתוח עסקה – {row['כתובת']}</h2>
<ul>
<li><strong>ZIP:</strong> {row['ZIP']}</li>
<li><strong>ARV:</strong> {row['ARV']}</li>
<li><strong>מחיר מבוקש:</strong> {row['מחיר מבוקש']}</li>
<li><strong>שיפוץ:</strong> {row['שיפוץ']}</li>
<li><strong>All-In:</strong> {row['All-In']}</li>
<li><strong>ROI פליפ:</strong> {row['ROI פליפ']}</li>
<li><strong>ROI שכירות:</strong> {row['ROI שכירות']}</li>
<li><strong>מאושר:</strong> {row['מאושר']}</li>
</ul>
<h3>סיכום:</h3>
<p>{row['סיכום']}</p>
</body></html>"""
    Path(f"{row['ID']}.html").write_text(html, encoding="utf-8")

# הוספת לינק “צפה”
df_out["צפה"] = df_out["ID"].apply(lambda x: f'=HYPERLINK("https://friesiancapital.github.io/Analysis-/{x}.html", "צפה")')
df_out.to_excel("deal_links.xlsx", index=False)

# git add + commit + push
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Auto push full batch"], check=True)
subprocess.run(["git", "push"], check=True)

print(f"✓ סיימנו! הקובץ שנותח: {input_csv.name}")
