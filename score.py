import streamlit as st
import pandas as pd

# Load the Excel file
@st.cache_data
def load_data():
    df = pd.read_excel("수학단원db_최종_틀린문제포함.xlsx")
    return df

df = load_data()

st.title("학생 점수 조회")
name = st.text_input("이름을 입력하세요:")

if name:
    student_row = df[df['이름'] == name]
    if not student_row.empty:
        score = student_row.iloc[0]['점수']
        wrongs = student_row.iloc[0]['틀린문제']

        st.success(f"✅ {name} 학생의 점수는 {score}점입니다.")
        st.info(f"❌ 틀린 문제: {wrongs}")
    else:
        st.error("해당 이름을 찾을 수 없습니다.")
