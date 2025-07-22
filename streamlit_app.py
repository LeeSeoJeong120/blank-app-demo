import streamlit as st
import numpy as np

st.title("🎲 주사위 실험기")
st.write("슬라이더로 주사위 개수를 선택한 후 '주사위 굴리기' 버튼을 눌러보세요!")

# 1. 주사위 개수 슬라이더 (1 ~ 200개)
dice_count = st.slider("주사위 개수 선택", min_value=1, max_value=200, value=10)

# 2. 버튼 누르면 주사위 굴리기
if st.button("주사위 굴리기"):
    rolls = np.random.randint(1, 7, size=dice_count)
    average = np.mean(rolls)
    st.write(f"🎯 {dice_count}개의 주사위를 굴린 평균값은 **{average:.2f}**입니다.")
    st.write("굴린 주사위 값들:", rolls)
