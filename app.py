import streamlit as st
import pandas as pd
import io

# ฟังก์ชันจำลองไฟล์ขึ้นมาในระบบโดยไม่ต้องอัพโหลดไฟล์จริง
@st.cache_data
def prepare_system_files():
    # 1. จำลองข้อมูลสำหรับ studentData-noHeader.csv
    # ใส่ข้อมูลจำลองตามที่คุณต้องการ (เรียงตามโครงสร้าง: ID, Gender, CsScore, Height)
    std_raw_data = [
        [101, 'M', 15, 170],
        [102, 'F', 18, 165],
        [103, 'M', 12, 175],
        [104, 'F', 19, 160]
    ]
    df_std = pd.DataFrame(std_raw_data)
    # บันทึกเป็นไฟล์ CSV ไว้ในระบบจำลองของ Streamlit Cloud
    df_std.to_csv('studentData-noHeader.csv', index=False, header=False)

    # 2. จำลองข้อมูลสำหรับ sciScore.csv
    sci_raw_data = {
        'เลขประจำตัว': [101, 102, 103, 104],
        'SciScore': [85, 90, 78, 92]
    }
    df_sci = pd.DataFrame(sci_raw_data)
    df_sci.to_csv('sciScore.csv', index=False)

# เรียกใช้ฟังก์ชันให้ระบบสร้างไฟล์เตรียมไว้ทันทีที่เปิดหน้าเว็บ
prepare_system_files()

# หลังจากบรรทัดนี้ ผู้เรียนจะสามารถใช้คำสั่ง pd.read_csv('sciScore.csv') ได้ปกติเหมือนมีไฟล์อยู่จริงครับ
st.success("ระบบเตรียมไฟล์ข้อมูลเรียบร้อยแล้ว! พร้อมใช้งานไฟล์ sciScore.csv และ studentData-noHeader.csv")
