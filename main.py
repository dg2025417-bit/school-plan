# -*- coding: utf-8 -*-
"""
스쿨플랜 · School Plan  (순수 Streamlit 버전 + 여백/공백 극단적 최적화)
"""

import json
import os
import uuid
from datetime import date, datetime

import streamlit as st

# ══════════════════════════════════════════════════════════
# 1. 기본 설정
# ══════════════════════════════════════════════════════════
DATA_FILE = "schoolplan_data.json"
DAYS = ["월", "화", "수", "목", "금"]
PERIODS = [1, 2, 3, 4, 5, 6, 7]
WEEK_KO = ["월", "화", "수", "목", "금", "토", "일"]

st.set_page_config(
    page_title="스쿨플랜 · School Plan",
    page_icon="🗓️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── 디자인 (모바일 화면의 불필요한 여백/공백 완벽 제거) ────────────────────────
st.markdown(
    """
    <style>
      .stApp {
        background: linear-gradient(160deg, #F8F6FD 0%, #F1FAF5 100%);
      }
      
      /* 상단 헤더, 메뉴, 푸터 숨김 */
      header, #MainMenu, footer { visibility: hidden !important; display: none !important; }

      /* 전체 페이지 상하좌우 여백 최소화 */
      .block-container { 
        padding: 0.8rem 0.5rem 0.5rem 0.5rem !important; 
        max-width: 780px; 
      }

      /* Streamlit 기본 요소들 사이의 세로/가로 갭(여백) 강제 축소 */
      div[data-testid="stVerticalBlock"] { gap: 0.3rem !important; }
      div[data-testid="stHorizontalBlock"] { gap: 0.3rem !important; }
      
      /* 탭(Tabs) 여백 및 크기 축소 */
      button[data-baseweb="tab"] {
        padding-top: 0.4rem !important; 
        padding-bottom: 0.4rem !important;
      }
      div[data-baseweb="tab-list"] { gap: 0px !important; margin-bottom: 0.2rem !important; }
      
      /* 기본 마진/구분선 압축 */
      p, h1, h2, h3, h4, h5, h6 { margin-bottom: 0.2rem !important; }
      hr { margin: 0.5em 0 !important; padding: 0 !important; }

      /* 오늘 카드 */
      .today-card {
        background: linear-gradient(135deg, #C9B8F5 0%, #A8DFF0 55%, #A8ECD6 100%);
        border-radius: 16px;
        padding: 14px 16px;
        color: #FFFFFF;
        box-shadow: 0 4px 15px rgba(140,116,214,0.15);
        margin-bottom: 8px;
      }
      .today-day  { font-size: 22px; font-weight: 700; line-height: 1.1; }
      .today-sub  { font-size: 12px; opacity: 0.92; margin-top: 4px; }
      .chip-wrap  { margin-top: 10px; }
      .class-chip {
        display: inline-block;
        background: rgba(255,255,255,0.30);
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 11.5px;
        margin: 0 4px 4px 0;
      }
      .class-chip b { margin-right: 4px; opacity: 0.85; }

      /* 항목 카드 */
      .item-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 10px 12px;
        box-shadow: 0 2px 6px rgba(140,116,214,0.08);
        margin-bottom: 4px;
      }
      .tag {
        display: inline-block; color: #fff; font-size: 10.5px; font-weight: 700;
        padding: 2px 8px; border-radius: 999px; margin-right: 4px;
      }
      .tag-exam   { background: #4693C4; }
      .tag-assign { background: #EE8A52; }
      .dday       { display:inline-block; font-size: 10.5px; font-weight: 700;
                    color: #8C74D6; background: #F1ECFC;
                    padding: 2px 8px; border-radius: 999px; }
      .dday-today { color: #D96760; background: #FCECEA; }
      .dday-past  { color: #B0A8C9; background: #F2F0F7; }
      .item-title { font-size: 13.5px; font-weight: 700; color: #39324D; margin-top: 4px; line-height: 1.2; }
      .item-desc  { font-size: 12px; color: #7A7392; margin-top: 2px; line-height: 1.3; }

      /* 빈 상태 */
      .empty-box {
        background:#FFFFFF; border-radius:12px; padding:20px 10px;
        text-align:center; color:#B0A8C9; font-size:12.5px;
        box-shadow: 0 2px 6px rgba(140,116,214,0.08);
      }
      .empty-box .ic { font-size: 24px; display:block; margin-bottom:4px; }

      /* 시간표 전용 HTML 그리드 (간격 극단적 최소화) */
      .timetable-wrapper {
        display: grid;
        grid-template-columns: 0.5fr 1fr 1fr 1fr 1fr 1fr;
        gap: 3px;
        width: 100%;
        margin-top: 4px;
      }
      .tt-filled {
        background: linear-gradient(135deg,#EFE9FC,#E7F6EF);
        border-radius: 6px; padding: 4px 1px; text-align:center;
        font-size: 11px; font-weight: 700; color:#39324D; 
        display: flex; align-items: center; justify-content: center;
        min-height: 34px; word-break: break-all; line-height: 1.1;
      }
      .tt-empty {
        background: #FBFAFF; border: 1px solid #E9E3F8;
        border-radius: 6px; padding: 4px 1px; text-align:center;
        font-size: 11px; color:#D5CEE8; 
        display: flex; align-items: center; justify-content: center;
        min-height: 34px;
      }
      .tt-head {
        text-align:center; font-size:11px; font-weight:700; color:#7A7392;
        padding-bottom: 2px;
      }
      .tt-period {
        text-align:center; font-size:10.5px; font-weight:700; color:#B0A8C9;
        display: flex; align-items: center; justify-content: center;
      }
      
      /* 모바일 미디어 쿼리 - 더 좁은 화면 대비 */
      @media (max-width: 480px) {
        .block-container { padding: 0.5rem 0.3rem 0.3rem 0.3rem !important; }
        .timetable-wrapper { gap: 2px; }
        .tt-filled, .tt-empty { font-size: 10px; min-height: 30px; }
        .tt-head { font-size: 10px; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)


# ══════════════════════════════════════════════════════════
# 2. 데이터 저장 / 불러오기
# ══════════════════════════════════════════════════════════
def empty_state() -> dict:
    return {"timetable": {}, "exams": [], "assignments": [], "todos": []}

def load_data() -> dict:
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            base = empty_state()
            base.update(data)
            return base
        except (json.JSONDecodeError, OSError):
            return empty_state()
    return empty_state()

def save_data() -> None:
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(st.session_state.data, f, ensure_ascii=False, indent=2)
    except OSError:
        pass

if "data" not in st.session_state:
    st.session_state.data = load_data()

DATA = st.session_state.data


# ══════════════════════════════════════════════════════════
# 3. 유틸 함수
# ══════════════════════════════════════════════════════════
def new_id() -> str:
    return uuid.uuid4().hex[:10]

def today_ko() -> str:
    return WEEK_KO[date.today().weekday()]

def fmt_date(iso: str) -> str:
    if not iso: return "미정"
    try:
        d = datetime.strptime(iso, "%Y-%m-%d").date()
        return f"{d.month}/{d.day}"
    except ValueError:
        return "미정"

def dday(iso: str):
    if not iso: return "미정", "dday"
    try:
        target = datetime.strptime(iso, "%Y-%m-%d").date()
    except ValueError:
        return "미정", "dday"

    diff = (target - date.today()).days
    if diff == 0: return "D-DAY", "dday dday-today"
    if diff > 0: return f"D-{diff}", "dday"
    return "지남", "dday dday-past"

def sort_by_date(items: list) -> list:
    return sorted(items, key=lambda x: x.get("date") or "9999-99-99")


# ══════════════════════════════════════════════════════════
# 4. 상단 : 오늘 카드
# ══════════════════════════════════════════════════════════
def render_today_card():
    today = date.today()
    day_ko = today_ko()

    if day_ko in ("토", "일"):
        sub = "주말이에요!"
        chips = ""
    else:
        classes = [
            (p, DATA["timetable"][f"{day_ko}-{p}"])
            for p in PERIODS if DATA["timetable"].get(f"{day_ko}-{p}")
        ]
        if classes:
            sub = f"오늘 {len(classes)}개 수업"
            chips = "".join(f'<span class="class-chip"><b>{p}교시</b>{s}</span>' for p, s in classes)
        else:
            sub = "등록된 시간표 없음"
            chips = '<span class="class-chip">시간표를 등록해보세요</span>'

    st.markdown(
        f"""
        <div class="today-card">
          <div class="today-day">{day_ko}요일</div>
          <div class="today-sub">{today.month}월 {today.day}일 · {sub}</div>
          <div class="chip-wrap">{chips}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<h3 style='color:#8C74D6; font-weight:800; margin:0;'>🗓️ 스쿨플랜</h3>", unsafe_allow_html=True)
render_today_card()


# ══════════════════════════════════════════════════════════
# 5. 탭 구성
# ══════════════════════════════════════════════════════════
tab_tt, tab_exam, tab_assign, tab_todo = st.tabs(["🗓️ 시간표", "📝 시험", "📌 과제", "✅ ToDo"])


# ──────────────────────────────────────────────────────────
# 5-1. 시간표 탭
# ──────────────────────────────────────────────────────────
with tab_tt:
    with st.form("tt_form", clear_on_submit=False):
        c1, c2, c3 = st.columns([1, 1, 2])
        with c1:
            sel_day = st.selectbox("요일", DAYS, key="tt_day", label_visibility="collapsed")
        with c2:
            sel_period = st.selectbox("교시", PERIODS, key="tt_period", label_visibility="collapsed")
        with c3:
            key = f"{sel_day}-{sel_period}"
            cur = DATA["timetable"].get(key, "")
            subject = st.text_input("과목명", value=cur, max_chars=12, key="tt_subject", placeholder="과목 입력", label_visibility="collapsed")

        b1, b2 = st.columns(2)
        with b1:
            submitted = st.form_submit_button("💾 저장", use_container_width=True)
        with b2:
            deleted = st.form_submit_button("🗑️ 지우기", use_container_width=True)

    if submitted and subject.strip():
        DATA["timetable"][key] = subject.strip()
        save_data()
        st.rerun()
    elif deleted:
        DATA["timetable"].pop(key, None)
        save_data()
        st.rerun()

    # 시간표 HTML 그리드 렌더링
    html_grid = '<div class="timetable-wrapper">'
    html_grid += '<div class="tt-head"></div>'
    for d in DAYS:
        html_grid += f'<div class="tt-head">{d}</div>'
        
    for p in PERIODS:
        html_grid += f'<div class="tt-period">{p}</div>'
        for d in DAYS:
            val = DATA["timetable"].get(f"{d}-{p}", "")
            cls = "tt-filled" if val else "tt-empty"
            txt = val if val else "-"
            html_grid += f'<div class="{cls}">{txt}</div>'
            
    html_grid += '</div>'
    st.markdown(html_grid, unsafe_allow_html=True)

    if DATA["timetable"]:
        if st.button("초기화", key="tt_clear", use_container_width=True):
            DATA["timetable"] = {}
            save_data()
            st.rerun()


# ──────────────────────────────────────────────────────────
# 5-2. 시험 탭
# ──────────────────────────────────────────────────────────
with tab_exam:
    with st.expander("➕ 시험 추가", expanded=len(DATA["exams"]) == 0):
        with st.form("exam_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                e_subject = st.text_input("과목", placeholder="수학", max_chars=20, label_visibility="collapsed")
            with c2:
                e_date = st.date_input("날짜", value=date.today(), label_visibility="collapsed")
            e_range = st.text_area("범위", placeholder="시험 범위 입력", label_visibility="collapsed", height=68)
            if st.form_submit_button("저장", use_container_width=True) and e_subject.strip():
                DATA["exams"].append({"id": new_id(), "subject": e_subject.strip(), "date": e_date.isoformat(), "range": e_range.strip()})
                save_data()
                st.rerun()

    if not DATA["exams"]:
        st.markdown("<div class='empty-box'>등록된 시험이 없어요</div>", unsafe_allow_html=True)
    else:
        for ex in sort_by_date(DATA["exams"]):
            label, cls = dday(ex["date"])
            col_a, col_b = st.columns([6, 1])
            with col_a:
                desc = f"<div class='item-desc'>{ex['range']}</div>" if ex["range"] else ""
                st.markdown(
                    f"""<div class="item-card"><span class="tag tag-exam">{ex['subject']}</span><span class="{cls}">{label}</span>
                    <div class="item-title">{fmt_date(ex['date'])}</div>{desc}</div>""", unsafe_allow_html=True)
            with col_b:
                if st.button("🗑️", key=f"del_ex_{ex['id']}"):
                    DATA["exams"] = [x for x in DATA["exams"] if x["id"] != ex["id"]]
                    save_data()
                    st.rerun()


# ──────────────────────────────────────────────────────────
# 5-3. 수행평가(과제) 탭
# ──────────────────────────────────────────────────────────
with tab_assign:
    with st.expander("➕ 과제 추가", expanded=len(DATA["assignments"]) == 0):
        with st.form("assign_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                a_subject = st.text_input("과목", placeholder="국어", max_chars=20, label_visibility="collapsed")
            with c2:
                a_date = st.date_input("날짜", value=date.today(), label_visibility="collapsed")
            a_content = st.text_area("내용", placeholder="수행평가 내용 입력", label_visibility="collapsed", height=68)
            if st.form_submit_button("저장", use_container_width=True) and a_subject.strip():
                DATA["assignments"].append({"id": new_id(), "subject": a_subject.strip(), "date": a_date.isoformat(), "content": a_content.strip()})
                save_data()
                st.rerun()

    if not DATA["assignments"]:
        st.markdown("<div class='empty-box'>등록된 수행평가가 없어요</div>", unsafe_allow_html=True)
    else:
        for ag in sort_by_date(DATA["assignments"]):
            label, cls = dday(ag["date"])
            col_a, col_b = st.columns([6, 1])
            with col_a:
                desc = f"<div class='item-desc'>{ag['content']}</div>" if ag["content"] else ""
                st.markdown(
                    f"""<div class="item-card"><span class="tag tag-assign">{ag['subject']}</span><span class="{cls}">{label}</span>
                    <div class="item-title">{fmt_date(ag['date'])} 마감</div>{desc}</div>""", unsafe_allow_html=True)
            with col_b:
                if st.button("🗑️", key=f"del_ag_{ag['id']}"):
                    DATA["assignments"] = [x for x in DATA["assignments"] if x["id"] != ag["id"]]
                    save_data()
                    st.rerun()


# ──────────────────────────────────────────────────────────
# 5-4. To Do 탭
# ──────────────────────────────────────────────────────────
with tab_todo:
    with st.form("todo_form", clear_on_submit=True):
        c1, c2, c3 = st.columns([3, 2, 1.5])
        with c1:
            t_text = st.text_input("할 일", placeholder="할 일 입력", max_chars=60, label_visibility="collapsed")
        with c2:
            t_date = st.date_input("날짜", value=date.today(), label_visibility="collapsed")
        with c3:
            if st.form_submit_button("추가", use_container_width=True) and t_text.strip():
                DATA["todos"].insert(0, {"id": new_id(), "text": t_text.strip(), "date": t_date.isoformat(), "done": False})
                save_data()
                st.rerun()

    if not DATA["todos"]:
        st.markdown("<div class='empty-box'>등록된 할 일이 없어요</div>", unsafe_allow_html=True)
    else:
        todos = sorted(DATA["todos"], key=lambda t: (t["done"], t.get("date") or "9999-99-99"))
        done_cnt = sum(1 for t in todos if t["done"])
        st.progress(done_cnt / len(todos) if len(todos) > 0 else 0, text=f"완료 {done_cnt}/{len(todos)}")

        for td in todos:
            c1, c2, c3 = st.columns([1, 6, 1.2])
            with c1:
                checked = st.checkbox("완료", value=td["done"], key=f"chk_{td['id']}", label_visibility="collapsed")
                if checked != td["done"]:
                    td["done"] = checked
                    save_data()
                    st.rerun()
            with c2:
                text = td["text"]
                if td["done"]:
                    st.markdown(f"<span style='color:#B0A8C9;text-decoration:line-through;'>{text}</span> <span style='font-size:10px;color:#C9C2DC;'>{fmt_date(td['date'])}</span>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<span style='color:#39324D;font-weight:500;'>{text}</span> <span style='font-size:10px;color:#B0A8C9;'>{fmt_date(td['date'])}</span>", unsafe_allow_html=True)
            with c3:
                if st.button("🗑️", key=f"del_td_{td['id']}"):
                    DATA["todos"] = [x for x in DATA["todos"] if x["id"] != td["id"]]
                    save_data()
                    st.rerun()
