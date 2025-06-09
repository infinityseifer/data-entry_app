import streamlit as st
import pandas as pd
import os
from io import BytesIO
from datetime import datetime

# Function to clear input fields
def clear_form():
    st.session_state["name_input"] = ""
    st.session_state["city_input"] = ""

# Save new data
def save_data():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[st.session_state["name_input"], st.session_state["city_input"], timestamp]],
                            columns=['Name', 'City', 'Timestamp'])
    
    if os.path.exists(filename):
        existing_data = pd.read_excel(filename)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        updated_data = new_data
    
    updated_data.to_excel(filename, index=False)
    st.success(f"✅ Data saved to {filename}!")
    clear_form()

# Clear entire data file
def clear_data():
    empty_df = pd.DataFrame(columns=['Name', 'City', 'Timestamp'])
    empty_df.to_excel(filename, index=False)
    st.warning(f"⚠️ All data cleared from {filename}!")

# Save edited table
def save_edits(edited_df):
    edited_df.to_excel(filename, index=False)
    st.success(f"✅ Edits saved to {filename}!")

# --- APP UI ---

st.title("📋 Interactive Data Entry App")
st.write("Enter **Name** and **City**, auto-add timestamp, edit data, download, clear, or change file name.")

# 1️⃣ File name input
default_filename = 'test_data.xlsx'
filename_input = st.text_input("📁 Current Excel File Name (with .xlsx):", value=default_filename)
filename = filename_input.strip() if filename_input.strip() else default_filename

st.markdown("---")

# 2️⃣ Data entry form
name = st.text_input("Name", key="name_input")
city = st.text_input("City", key="city_input")

st.button("➕ Save Entry", on_click=save_data)

st.markdown("---")

# 3️⃣ Display and edit data if file exists
if os.path.exists(filename):
    st.subheader(f"📄 Current Data in `{filename}`")

    df = pd.read_excel(filename)
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

    # Save edits
    if st.button("💾 Save Edits"):
        save_edits(edited_df)

    st.markdown("---")

    # 4️⃣ Download button
    buffer = BytesIO()
    edited_df.to_excel(buffer, index=False)
    buffer.seek(0)
    st.download_button(
        label="⬇️ Download Excel",
        data=buffer,
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # 5️⃣ Clear all data
    st.button("❌ Clear All Data", on_click=clear_data)
else:
    st.info(f"ℹ️ No file named `{filename}` yet. Add your first entry to create it.")
