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

# ====== 문제 데이터 (시대 순서: 고대 → 고려 → 조선 → 근현대) ======
BASE_QUIZ = [
    {
        "question": "광개토대왕이 활약한 시기의 나라는 어디일까요? 🗡️",
        "options": ["고구려", "백제", "신라", "가야"],
        "answer": "고구려",
        "image": None,
        "level": "어려움",
        "explain": "광개토대왕(재위 391~413)은 고구려 제19대 왕으로, 만주와 한반도 북부까지 영토를 크게 확장했습니다."
    },
    {
        "question": "고려에서 몽골의 침입에 맞서 1270년까지 항쟁을 이어간 무리의 이름은 무엇일까요? ⚔️",
        "options": ["삼별초", "화랑", "의병", "동학군"],
        "answer": "삼별초",
        "image": None,
        "level": "중간",
        "explain": "삼별초는 고려 무신정권의 군사 조직으로, 강화도·진도·제주도로 옮겨가며 끝까지 항몽 항쟁을 이어갔습니다."
    },
    {
        "question": "조선 세종 때 만들어진 과학 기구로, 해시계를 뜻하는 것은 무엇일까요? 🌞",
        "options": ["앙부일구", "혼천의", "측우기", "자격루"],
        "answer": "앙부일구",
        "image": None,
        "level": "중간",
        "explain": "앙부일구는 세종 대에 제작된 해시계로, 백성들이 시간을 쉽게 알 수 있도록 설치되었습니다."
    },
    {
        "question": "대한민국 임시정부가 수립된 해는 언제일까요? 🇰🇷",
        "options": ["1919년", "1945년", "1950년", "1960년"],
        "answer": "1919년",
        "image": None,
        "level": "쉬움",
        "explain": "1919년 3·1 운동 직후, 독립운동가들은 중국 상하이에 대한민국 임시정부를 수립했습니다."
    }
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
    "<div class='big-title'>🎉 시대별 역사 퀴즈 ✨</div>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<span class='badge'>문항 {current_idx+1 if current_idx < num_questions else num_questions}/{num_questions} • 난이도: 어려움1 + 중간2 + 쉬움1</span>",
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
