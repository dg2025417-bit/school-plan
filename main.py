"""
스쿨플랜 · School Plan (API 미사용 버전)
Streamlit + HTML 하이브리드 앱
"""
import streamlit as st
import time

# ──────────────────────────────────────────────
# 페이지 기본 설정 (모바일 호환성 포함)
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="스쿨플랜 · School Plan",
    page_icon="🗓️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
    <style>
        .block-container {padding-top: 1rem; padding-bottom: 0rem;}
        #MainMenu, footer, header {visibility: hidden;}
        
        @media (max-width: 640px) {
            .app { padding-bottom: 110px; }
        }
    </style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# 가상 데이터(Mock) 생성 함수 (API 대체)
# ──────────────────────────────────────────────
def mock_extract_data(mode):
    """API 호출을 대신하여 모드에 맞는 가상(Mock) 결과물을 반환합니다."""
    time.sleep(2)  # 분석하는 척하는 대기 시간 (2초)
    
    if mode == "시간표":
        return [
            {"day": "월", "period": 1, "subject": "수학"},
            {"day": "월", "period": 2, "subject": "영어"},
            {"day": "화", "period": 1, "subject": "과학"}
        ]
    elif mode == "시험":
        return [
            {"subject": "수학", "date": "2026-09-15", "range": "2단원~3단원"},
            {"subject": "영어", "date": "2026-09-16", "range": "Lesson 5~6"}
        ]
    elif mode == "수행평가":
        return [
            {"subject": "국어", "date": "2026-09-20", "content": "독후감 제출"},
            {"subject": "역사", "date": "2026-09-25", "content": "문화재 조사 보고서"}
        ]
    return []

# ──────────────────────────────────────────────
# 메인 화면 구성 및 사진 업로드
# ──────────────────────────────────────────────
st.markdown("## 📷 스마트 스쿨플랜 (오프라인 모드)")
st.caption("외부 API 없이 로컬에서 동작합니다. (현재는 예시 데이터가 출력됩니다.)")

modes = ["시간표", "시험", "수행평가"]
mode = st.radio("무엇을 등록할까요?", modes, horizontal=True)

uploaded_file = st.file_uploader("사진을 촬영하거나 갤러리에서 선택하세요", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="업로드된 이미지", use_column_width=True)
    
    if st.button(f"{mode} 분석하기 (가상 테스트)", use_container_width=True):
        with st.spinner('이미지를 분석하는 중입니다...'):
            # API 대신 가상 데이터 생성 함수 호출
            result = mock_extract_data(mode)
            
            if result:
                st.success("분석 완료! 추출된 데이터를 확인하고 수정하세요.")
                st.session_state["extracted_data"] = result

# ──────────────────────────────────────────────
# 추출된 데이터 확인 및 수동 수정 폼
# ──────────────────────────────────────────────
if "extracted_data" in st.session_state:
    st.markdown("### 📝 추출된 일정 확인")
    
    # 데이터를 화면에 표시하고 수정할 수 있는 입력 폼 제공
    with st.form("edit_form"):
        for i, item in enumerate(st.session_state["extracted_data"]):
            st.markdown(f"**항목 {i+1}**")
            cols = st.columns(len(item))
            for col, (key, value) in zip(cols, item.items()):
                # 사용자가 텍스트박스에서 값을 직접 수정할 수 있도록 함
                col.text_input(key.capitalize(), value, key=f"{key}_{i}")
        
        submit_btn = st.form_submit_button("최종 저장하기", use_container_width=True)
        
        if submit_btn:
            st.info("데이터가 성공적으로 저장되었습니다! (로컬 DB 또는 세션에 저장 로직을 추가하세요)")
            del st.session_state["extracted_data"]
