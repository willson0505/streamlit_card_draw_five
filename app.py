import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="五張抽牌", layout="centered")
st.title("🌟 五張抽牌卡牌系統")

# 讀取 Excel 牌卡資料
df = pd.read_excel("梅爾達49張牌卡.xlsx")
card_names = df["牌卡名稱"].tolist()
card_descs = dict(zip(df["牌卡名稱"], df["牌卡說明"]))

# 對應五張牌的意義
positions = [
    "事情的成因",
    "現在的狀況",
    "當前的功課",
    "最好的未來",
    "集體意識的收穫"
]

# 初始化狀態（抽過的牌、目前位置）
if "drawn_cards" not in st.session_state:
    st.session_state.drawn_cards = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# 抽牌按鈕邏輯
if st.button("抽一張牌 ✨"):
    if st.session_state.current_index < 5:
        remaining_cards = list(set(card_names) - set(st.session_state.drawn_cards))
        new_card = random.choice(remaining_cards)
        st.session_state.drawn_cards.append(new_card)
        st.session_state.current_index += 1
    else:
        st.info("你已經抽完五張牌了！")

# 顯示抽到的牌與解釋
for i, card in enumerate(st.session_state.drawn_cards):
    st.subheader(f"🔹 {positions[i]}：{card}")
    st.write(card_descs.get(card, "（此牌無說明）"))

# 重設按鈕
if st.button("重新開始 🔄"):
    st.session_state.drawn_cards = []
    st.session_state.current_index = 0
    st.experimental_rerun()
