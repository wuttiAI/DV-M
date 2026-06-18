import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import contextlib

st.set_page_config(layout="wide")
st.title("💻 ฝึกเขียน Python (Data visualization) :by UPR Wuttichai")

# --- ส่วนของการสร้างไฟล์ CSV จำลองในระบบ ---
@st.cache_data
def create_mock_data():
    # 1. ข้อมูลสำหรับ studentData-noHeader.csv
    std_df = pd.DataFrame({
        'ID': [101, 102, 103, 104],
        'Gender': ['M', 'F', 'M', 'F'],
        'CsScore': [15, 18, 12, 19],
        'Height': [170, 165, 175, 160]
    })
    std_df.to_csv('studentData-noHeader.csv', index=False, header=False)
    
    # 2. ข้อมูลสำหรับ sciScore.csv
    sci_df = pd.DataFrame({
        'เลขประจำตัว': [101, 102, 103, 104],
        'SciScore': [85, 90, 78, 92]
    })
    sci_df.to_csv('sciScore.csv', index=False)

create_mock_data()

# --- โค้ดตั้งต้นที่แสดงในช่องพิมพ์ ---
default_code = """
# ✍️ พิมพ์หรือแก้ไขโค้ดของคุณตรงนี้

"""

# --- ส่วนแสดงหน้าจอแบ่งเป็น 2 ฝั่ง ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 กล่องเขียนโค้ด")
    
    # 🌟 เปลี่ยนมาใช้ st.text_area แทน เพื่อความชัวร์ ไม่ต้องติดตั้งอะไรเพิ่ม
    user_code = st.text_area(
        label="พิมพ์โค้ด Python ด้านล่างนี้:",
        value=default_code,
        height=450
    )

with col2:
    st.subheader("🖥️ ผลลัพธ์การทำงาน")
    if st.button("▶️ รันโค้ด", type="primary"):
        stdout_capture = io.StringIO()
        
        try:
            plt.clf() # ล้างกราฟเก่าก่อนรันใหม่
            
            with contextlib.redirect_stdout(stdout_capture):
                # รันโค้ดที่รับมาจากตัว st.text_area
                exec(user_code, {}, {})
            
            # แสดงข้อความจากคำสั่ง print
            output_text = stdout_capture.getvalue()
            if output_text:
                st.text_area("Console Output:", output_text, height=150)
                
            # ดึงรูปกราฟมาแสดง
            fig = plt.gcf()
            if fig.get_axes(): 
                st.pyplot(fig)
                
        except Exception as e:
            st.error(f"❌ เกิดข้อผิดพลาดในโค้ดของคุณ:\n{e}")
