import streamlit as st

# MBTI별 진로 데이터 예시
career_dict = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "연구원"],
    "ENFP": ["광고 기획자", "창업가", "작가", "디자이너"],
    "ISTP": ["엔지니어", "파일럿", "응급구조사"],
    "INFJ": ["심리상담가", "작가", "사회운동가"],
    # ... 나머지 유형 추가
}

st.title("🌱 MBTI 기반 진로 추천 서비스")
st.write("당신의 MBTI에 맞는 진로를 찾아보세요!")

# MBTI 입력
mbti = st.text_input("당신의 MBTI를 입력하세요 (예: ENFP)").upper()

if mbti in career_dict:
    st.subheader(f"🔎 {mbti} 유형의 추천 진로")
    for job in career_dict[mbti]:
        st.write(f"- {job}")
else:
    if mbti:
        st.error("❌ 해당 MBTI 유형이 존재하지 않습니다. 다시 입력해주세요.")
