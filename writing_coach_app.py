import streamlit as st
from ai_helper import ask_ai

st.set_page_config(page_title="글쓰기 코치", layout="wide")

st.title("✍️ 글쓰기 코치")
st.markdown("당신의 글을 AI가 분석하고 개선해드립니다")

# 사이드바 - 글의 종류 선택
st.sidebar.header("설정")
writing_type = st.sidebar.selectbox(
    "글의 종류를 선택하세요",
    ["일반", "이메일", "보고서", "블로그", "에세이", "논문", "기타"]
)

# 메인 입력 영역
st.header("1️⃣ 당신의 글을 입력하세요")
user_text = st.text_area(
    "글을 여러 줄로 입력해주세요",
    height=200,
    placeholder="여기에 당신이 쓴 글을 붙여넣어주세요..."
)

# 분석 버튼
col1, col2, col3 = st.columns(3)
with col1:
    analyze_button = st.button("🚀 분석하기", use_container_width=True, type="primary")

# 분석 로직
if analyze_button and user_text:
    st.divider()

    # 1차: 좋은 점과 고칠 점 정리
    with st.spinner("📝 1차 피드백을 생성 중입니다..."):
        feedback_prompt = f"""다음 {writing_type} 글을 분석해주세요. 좋은 점과 고칠 점을 명확하게 정리해주세요.

글:
{user_text}

다음 형식으로 답변해주세요:
## 좋은 점 ✨
- (좋은 점 1)
- (좋은 점 2)
- (좋은 점 3)

## 고칠 점 🔧
- (고칠 점 1)
- (고칠 점 2)
- (고칠 점 3)"""

        feedback = ask_ai(feedback_prompt)

    # 피드백 표시
    st.header("2️⃣ AI 피드백")
    st.markdown(
        f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 4px solid #1f77b4;">
        {feedback}
        </div>
        """,
        unsafe_allow_html=True
    )

    # 2차: 피드백을 반영해 다듬기
    with st.spinner("✨ 2차 다듬기를 진행 중입니다..."):
        refinement_prompt = f"""다음은 사용자의 원본 글과 AI의 피드백입니다. 피드백을 적극 반영해서 글을 다듬어주세요. 더 나은 표현, 더 명확한 의도 전달, 더 자연스러운 흐름으로 개선해주세요.

【원본 글】
{user_text}

【피드백】
{feedback}

【다듬어진 글】
(여기에 개선된 글을 작성해주세요. 원본 글의 의도는 유지하면서 피드백을 반영해주세요)"""

        refined_text = ask_ai(refinement_prompt)

    # 다듬어진 글 표시
    st.header("3️⃣ 다듬어진 글")
    st.markdown(
        f"""
        <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 4px solid #2e7d32;">

{refined_text}

        </div>
        """,
        unsafe_allow_html=True
    )

    # 비교 보기
    st.header("4️⃣ 원본과 비교")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 원본 글")
        st.text_area("원본", user_text, disabled=True, height=200)

    with col2:
        st.subheader("✨ 다듬어진 글")
        st.text_area("개선", refined_text, disabled=True, height=200)

elif analyze_button and not user_text:
    st.warning("⚠️ 글을 입력해주세요!")

st.divider()
st.markdown("""
### 💡 팁
- 여러 줄의 글을 입력해주세요
- 글의 종류를 선택하면 더 정확한 분석을 받을 수 있습니다
- AI의 피드백을 참고하여 글을 개선할 수 있습니다
""")
