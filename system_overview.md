# System Overview & Operational Guide

---

## תוכן עניינים
- [1. מבוא כללי למערכת](#1)
- [2. מדריך פתיחה לצ'אט חדש](#2)
- [3. מטרות ממוקדות בצ'אט זה](#3)

---

## 1. מבוא כללי למערכת
# Real Estate Automation System – Chat Boot Package

**Purpose**:  
This environment enables full continuity for any new ChatGPT thread working on the real estate investment automation project.

## What's included
- `task_status_master.csv`: All 45 tasks with progress, status, and assigned chat.
- `project_config.*`: System configuration files.
- `Copy of מודולים קובץ 18.docx`: Core logic definitions.
- `template.html`: Output template.
- `analyze_and_push.py`: Main automation script.
- `input_adapter.py`: CSV field mapping handler.
- `deal_files.csv`: Example deal dataset.
- `transition_guide.md`: Step-by-step onboarding guide.

## Immediate actions
1. Load the config: `project_config.json`
2. Review current tasks: `task_status_master.csv`
3. Use `analyze_and_push.py` to run on `deal_files.csv`
4. For new addresses, activate the input adapter.
5. For repair estimates – connect to Kofez18 logic or `Vision API` if available.

## Notes
- All tasks are documented. Each can be split into a separate Chat if needed.
- Every output should include a `Full Analysis Link` column pointing to HTML.
- “צפה” = “View full analysis”

---

System Ready: 100%  
Last verified: 2025-05-27


---

## 2. מדריך פתיחה לצ'אט חדש
# Chat Transition Guide

This document outlines the exact steps to continue the project in a new ChatGPT thread, preserving all data and logic from the previous chat.

---

## 1. Upload the following files to the new chat:

- `project_config.json`
- `project_config.md`
- `project_config_updated.txt`
- `deal_files.csv`
- `template.html`
- `input_adapter.py`
- `analyze_and_push.py`
- `Copy of מודולים קובץ 18.docx`

## 2. Then upload the transition package files:

- `chat_transition_verification_prompt.md`
- `status_table.csv`
- `transition_patch_log.txt`
- `system_transition_summary.md`
- `todo_next.txt`
- `init_checklist.txt`

## 3. Paste this message into the new chat:

```
Hi, this is a continuation of a real estate automation project. I’ve uploaded all relevant files and system configurations. You should now:
- Load all transition context
- Restore status of open tasks
- Resume project execution from where it left off
```

## 4. Important Notes

- Do not skip the CSV and JSON files – they contain logic/state.
- After loading, run an initial test on a sample address.
- If you encounter “404” errors, ensure the GitHub HTML links are correct, or use local file simulation.

---

## Ready for Transition

---

## 3. מטרות ממוקדות בצ'אט זה (אם רלוונטי)
# Chat Focus Hint – עבור כל צ'אט חדש

המטרה שלך כצ'אט היא:
1. להמשיך בצורה עצמאית להריץ משימות פתוחות, כפי שמוגדרות בקובץ `task_status_master.csv`.
2. לקבל את ההקשר הכללי של כל המערכת מתוך הקבצים המצורפים, במיוחד `transition_guide.md` ו־`README.md`.
3. להתמקד במשימות הרלוונטיות אליך, כפי שצוינו בעמודת "צ’אט שייך" בקובץ המשימות.
4. לשמור על רצף, דיוק, ואיכות מרבית – כל תוצר שאתה מפיק יהיה חלק מתהליך גדול.

כדי להתחיל:
- סרוק את הקובץ `task_status_master.csv` ומצא את כל המשימות שהשדה "צ’אט שייך" תואם לשמך.
- לכל משימה כזו:
  - פתח את הקובץ המתאים (אם יש).
  - הרץ אותה עד הסוף.
  - עדכן את אחוז הביצוע וסטטוס המשימה.

בכל מקרה של חוסר ודאות – חזור לקובץ `transition_guide.md`.

בהצלחה – כל פלט שלך משפיע על הצלחת הפרויקט כולו.
---

### קבצי הרצה קריטיים (TXT לצ’אטים חדשים)
- `analyze_and_push.txt` – גרסת טקסט של סקריפט הניתוח המלא
- `input_adapter.txt` – גרסת טקסט של מתאם הנתונים (input mapping)

> יש לכלול את שני הקבצים האלו בכל פתיחה של צ'אט חדש – אחרת הסקריפטים לא ייקראו כראוי


> קובץ חובה נוסף לצ’אט חדש: `master_files_list.txt` – מרכז את כל מבנה המערכת בפורמט טכני