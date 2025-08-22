import streamlit as st
import random

st.set_page_config(page_title="역사 퀴즈 ✨", page_icon="📚", layout="centered")

# ====== 스타일 (화려하게!) ======
st.markdown(
    """
    <style>
      .stApp {background: linear-gradient(135deg,#f9f5ff 0%, #e7fbff 50%, #fff7e5 100%);} 
      .big-title {font-size: 2.2rem; font-weight: 900; line-height: 1.2;}
      .caption {opacity: .8;}
      .badge {display:inline-block; padding:6px 12px; border-radius:999px; font-weight:700; font-size:.8rem; 
              background:#ffffffaa; border:1px solid rgba(0,0,0,.06); box-shadow:0 8px 20px rgba(0,0,0,.06);} 
      .card {padding:1rem 1.2rem; border-radius:1.25rem; background:rgba(255,255,255,.9); 
              border:1px solid rgba(0,0,0,.06); box-shadow:0 16px 40px rgba(0,0,0,.08);} 
    </style>
    """,
    unsafe_allow_html=True,
)

# ====== 문제 데이터 (어려운 2, 쉬운 1, 이미지 1) ======
BASE_QUIZ = [
    {
        "question": "다음 사진 속 궁궐은 어디일까요? 🏯",
        "options": ["경복궁", "창덕궁", "덕수궁", "창경궁"],
        "answer": "경복궁",
        "image": "https://share.google/images/n509h7fLfzg8GbxtG",
        "level": "이미지",
        "explain": "사진은 경복궁의 정전인 '근정전'이 보이는 각도예요. 조선의 정궁이죠."
    },
    {
        "question": "광종이 과거제를 실시한 해는 언제일까요? 📜",
        "options": ["958년", "976년", "993년", "1018년"],
        "answer": "958년",
        "image": None,
        "level": "어려움",
        "explain": "광종 9년(958), 후주 출신 쌍기의 건의로 과거제를 실시하여 신라 골품 잔재를 약화시켰어요."
    },
    {
        "question": "『경국대전』이 완성된 왕은 누구일까요? 📖",
        "options": ["세조", "성종", "태종", "정조"],
        "answer": "성종",
        "image": None,
        "level": "어려움",
        "explain": "경국대전은 세조 때 편찬 시작, 성종 16년(1485)에 완성·반포되었습니다."
    },
    {
        "question": "3·1 운동이 일어난 해는? ✊",
        "options": ["1910년", "1919년", "1945년", "1950년"],
        "answer": "1919년",
        "image": None,
        "level": "쉬움",
        "explain": "1919년 3월 1일 전국적 독립만세운동이 전개되었고, 대한민국 임시정부 수립으로 이어졌어요."
    },
]

# ====== 상태 초기화 ======
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.q_num = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.correct = None
    # 보기 순서 섞기 (문제 순서는 고정)
    st.session_state.quiz = []
    for q in BASE_QUIZ:
        opts = q["options"][:]
        random.shuffle(opts)
        st.session_state.quiz.append({**q, "shuffled": opts})

quiz = st.session_state.quiz
current_idx = st.session_state.q_num
num_questions = len(quiz)

# ====== 헤더 ======
st.markdown(
    "<div class='big-title'>🎉 반짝반짝 역사 퀴즈 쇼! ✨</div>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<span class='badge'>문항 {current_idx+1 if current_idx < num_questions else num_questions}/{num_questions} • 도전 등급: 어려운 2 + 쉬운 1 + 이미지 1</span>",
    unsafe_allow_html=True,
)

# 진행도
progress = 0 if num_questions == 0 else int((current_idx/num_questions)*100)
st.progress(progress)

st.write("")

# ====== 본문 ======
if current_idx < num_questions:
    q = quiz[current_idx]
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader(f"Q{current_idx+1}. {q['question']}")
        st.caption(f"난이도: {q['level']} 🏷️")

        if q["image"]:
            st.image(q["image"], use_column_width=True, caption="이미지를 보고 정답을 고르세요")

        # 사용자가 답을 선택
        choice = st.radio("정답을 선택하세요:", q["shuffled"], key=f"choice_{current_idx}")

        cols = st.columns([1, 1])
        with cols[0]:
            if not st.session_state.answered:
                if st.button("✅ 제출하기", use_container_width=True):
                    st.session_state.answered = True
                    st.session_state.correct = (choice == q["answer"])
                    if st.session_state.correct:
                        st.session_state.score += 1
        with cols[1]:
            if st.session_state.answered:
                if st.button("➡️ 다음 문제", use_container_width=True):
                    st.session_state.q_num += 1
                    st.session_state.answered = False
                    st.session_state.correct = None

        # 피드백 & 해설
        if st.session_state.answered:
            if st.session_state.correct:
                st.success("🌟 정답입니다! 대단해요!")
            else:
                st.error(f"🙅‍♀️ 아쉽지만 오답! 정답은 **{q['answer']}** 입니다.")
            with st.expander("🧐 해설 보기"):
                st.write(q["explain"])

        st.markdown("</div>", unsafe_allow_html=True)
else:
    # 결과 화면
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🎊 퀴즈 완료!")
    st.write(f"총 점수: **{st.session_state.score} / {num_questions}**")

    # 수준 판정
    score = st.session_state.score
    if score <= 1:
        st.info("🧒 현재 수준: **초등** — 기초 개념을 조금 더 복습해볼까요?")
    elif score <= 3:
        st.warning("🧑‍🎓 현재 수준: **중등** — 좋아요! 한 단계만 더 가면 고등 수준이에요.")
    else:
        st.success("🎓 현재 수준: **고등** — 완벽해요! 역사 고수 인정!")

    if score >= 3:
        st.balloons()

    # 다시 시작
    st.write("")
    if st.button("🔄 다시 풀기"):
        for k in ["initialized", "q_num", "score", "answered", "correct", "quiz"]:
            if k in st.session_state:
                del st.session_state[k]
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

