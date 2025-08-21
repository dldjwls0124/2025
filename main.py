import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천",
    page_icon="🌟",
    layout="centered"
)

# CSS 스타일링 (배경, 글꼴 등)
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #FDEB71 10%, #F8D800 100%);
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 50px !important;
        font-weight: bold;
        color: #FF6F61;
        text-shadow: 2px 2px #FFDAB9;
    }
    .subtitle {
        text-align: center;
        font-size: 24px;
        color: #333333;
    }
    .career-box {
        background-color: #fff8e7;
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# MBTI 진로 데이터
career_dict = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 과학자", "🔬 연구원"],
    "ENFP": ["🎨 광고 기획자", "🚀 창업가", "✍️ 작가", "🎭 디자이너"],
    "ISTP": ["⚙️ 엔지니어", "✈️ 파일럿", "⛑️ 응급구조사"],
    "INFJ": ["💬 심리상담가", "📖 작가", "🌍 사회운동가"],
    "ENTJ": ["💼 CEO", "📈 경영 전략가", "🏢 프로젝트 매니저"],
    # ... 나머지 유형 추가 가능
}

# 제목
st.markdown("<h1 class='title'>🌟 MBTI 기반 진로 추천 서비스 🌟</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>당신의 성격 유형에 딱 맞는 진로를 찾아보세요! ✨</p>", unsafe_allow_html=True)

# MBTI 입력
mbti = st.text_input("🔮 당신의 MBTI를 입력하세요 (예: ENFP)").upper()

if mbti in career_dict:
    st.markdown(f"## 🌈 {mbti} 유형의 추천 진로")
    for job in career_dict[mbti]:
        st.markdown(f"<div class='career-box'>{job}</div>", unsafe_allow_html=True)
    
    st.balloons()  # 풍선 효과
    st.success("💡 새로운 길이 열리고 있어요! 🚀")
else:
    if mbti:
        st.error("❌ 해당 MBTI 유형이 존재하지 않아요! 다시 입력해주세요 ✍️")
