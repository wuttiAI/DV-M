import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💻 ระบบฝึกเขียนโค้ด Python Data Science")

# ระบบจะดึงไฟล์จากโฟลเดอร์เดียวกันบน GitHub มาอ่านโดยอัตโนมัติ
stdData = pd.read_csv('studentData-noHeader.csv', delimiter=',', names=['ID','Gender','CsScore','Height'])
sciData = pd.read_csv('sciScore.csv', delimiter=',')

# ทดลองแสดงผลข้อมูลในระบบให้ผู้เรียนเห็นว่ามีไฟล์อยู่จริง
st.subheader("📊 ตรวจสอบข้อมูลในระบบ")
col1, col2 = st.columns(2)
with col1:
    st.write("ข้อมูลจาก studentData-noHeader.csv", stdData.head())
with col2:
    st.write("ข้อมูลจาก sciScore.csv", sciData.head())

# ... ส่วนของกล่องเขียนโค้ดและปุ่มรันโค้ด (เหมือนตัวอย่างก่อนหน้านี้) ...
