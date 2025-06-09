# 📋 Data Entry App (Streamlit)

A simple, user-friendly **data entry and management app** built using **Python** and **Streamlit**.  
The app allows users to enter data (Name, City), which is automatically saved to a **user-specific Excel file** (`data-USERNAME.xlsx`). Each user gets their own file to prevent data overlap.

## 🚀 Live Demo

👉 [https://data-entryapp-infinity-abs-test.streamlit.app/](https://data-entryapp-infinity-abs-test.streamlit.app/)

## ✨ Features

✅ Username-based file system → ensures each user works with their own Excel file  
✅ Data entry form → Name, City, Timestamp auto-added  
✅ Editable table → users can edit existing data directly in the app  
✅ Save Edits button → updates Excel file in real time  
✅ Download button → download Excel file with current data  
✅ Clear All Data button → clear user’s Excel file  
✅ Responsive design → works on desktop, tablet, mobile  
✅ Deployed via **Streamlit Cloud** → accessible from anywhere via public link

## 🛠️ Tech Stack

- Python  
- Streamlit  
- pandas  
- openpyxl  
- GitHub → version control  
- Streamlit Cloud → deployment

pip install -r requirements.txt

streamlit run app.py

Project Purpose
This project was created to demonstrate:

✅ How to build a simple, user-friendly data entry interface
✅ How to manage user-specific file storage
✅ How to deploy Streamlit apps for broad accessibility
✅ Core principles of full project lifecycle: local → GitHub → cloud deployment

📅 Future Improvements
Add more fields (Phone, Email, Notes, etc.)

Add user authentication

Save files to Google Drive or Dropbox for permanent cloud storage

Email files to users automatically

Improve UI with more styling

🎓 Author
Arnell Seifer
GitHub: infinityseifer
