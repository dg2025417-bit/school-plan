# -*- coding: utf-8 -*-
"""
스쿨플랜 · School Plan  (순수 Streamlit 버전 + 모바일 한 화면 완벽 고정)

기능
  1) 시간표     : 요일 × 교시 표 편집 / 조회 (HTML Grid로 가로 스크롤 완벽 방지)
  2) 시험       : 과목 · 날짜 · 범위 관리 (D-day 계산)
  3) 수행평가   : 과목 · 마감일 · 내용 관리 (D-day 계산)
  4) To Do List : 할 일 체크 / 삭제

데이터는 실행 폴더의 schoolplan_data.json 파일에 저장됩니다.
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

# ── 디자인 (모바일 기기 크기에 맞춰 알맞게 줄어들도록 설정) ────────────────────────
st.markdown(
    """
    <style>
      .stApp {
        background: linear-gradient(160deg, #F8F6FD 0%, #F1FAF5 100%);
      }
      
      .block-container { 
        padding-top: 1.5rem; 
        max-width: 780px; 
      }
      
      #MainMenu, footer { visibility: hidden; }

      /* 오늘 카드 */
      .today-card {
        background: linear-gradient(135deg, #C9B8F5 0%, #A8DFF0 55%, #A8ECD6 100%);
        border-radius: 26px;
        padding: 22px 24px;
        color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(140,116,214,0.18);
        margin-bottom: 18px;
      }
      .today-day  { font-size: 26px; font-weight: 700; }
      .today-sub  { font-size: 13px; opacity: 0.92; margin-top: 4px; }
      .chip-wrap  { margin-top: 14px; }
      .class-chip {
        display: inline-block;
        background: rgba(255,255,255,0.30);
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 13px;
        margin: 0 6px 6px 0;
      }
      .class-chip b { margin-right: 5px; opacity: 0.85; }

      /* 항목 카드 */
      .item-card {
        background: #FFFFFF;
        border-radius: 18px;
        padding: 14px 18px;
        box-shadow: 0 3px 10px rgba(140,116,214,0.10);
        margin-bottom: 4px;
      }
      .tag {
        display: inline-block; color: #fff; font-size: 11.5px; font-weight: 700;
        padding: 3px 11px; border-radius: 999px; margin-right: 6px;
      }
      .tag-exam   { background: #4693C4; }
      .tag-assign { background: #EE8A52; }
      .dday       { display:inline-block; font-size: 11.5px; font-weight: 700;
                    color: #8C74D6; background: #F1ECFC;
                    padding: 3px 10px; border-radius: 999px; }
      .dday-today { color: #D96760; background: #FCECEA; }
      .dday-past  { color: #B0A8C9; background: #F2F0F7; }
      .item-title { font-size: 15px; font-weight: 700; color: #39324D; margin-top: 6px; }
      .item-desc  { font-size: 13px; color: #7A7392; margin-top: 3px; line-height: 1.5; }

      /* 빈 상태 */
      .empty-box {
        background:#FFFFFF; border-radius:18px; padding:34px 20px;
        text-align:center; color:#B0A8C9; font-size:13.5px;
        box-shadow: 0 3px 10px rgba(140,116,214,0.10);
      }
      .empty-box .ic { font-size: 30px; display:block; margin-bottom:8px; }

      /* ★ 시간표 전용 HTML 그리드 (가로 스크롤 완벽 방지) ★ */
      .timetable-wrapper {
        display: grid;
        grid-template-columns: 0.6fr 1fr 1fr 1fr 1fr 1fr;
        gap: 6px;
        width: 100%;
        margin-top: 10px;
      }
      .tt-filled {
        background: linear-gradient(135deg,#EFE9FC,#E7F6EF);
        border-radius: 10px; padding: 12px 2px; text-align:center;
        font-size: 13px; font-weight: 700; color:#39324D; 
        display: flex; align-items: center; justify-content: center;
        min-height: 44px; word-break: keep-all;
      }
      .tt-empty {
        background: #FBFAFF; border: 1.5px solid #E9E3F8;
        border-radius: 10px; padding: 12px 2px; text-align:center;
        font-size: 13px; color:#D5CEE8; 
        display: flex; align-items: center; justify-content: center;
        min-height: 44px;
      }
      .tt-head {
        text-align:center; font-size:12.5px; font-weight:700; color:#7A7392;
        padding-bottom: 4px;
      }
      .tt-period {
        text-align:center; font-size:12px; font-weight:700; color:#B0A8C9;
        display: flex; align-items: center; justify-content: center;
      }

      /* =========================================
         모바일 기기 전용 (글자 및 여백 축소)
         ========================================= */
      @media (max-width: 640px) {
        .block-container { 
          padding-top: 1rem !important; 
          padding-left: 0.5rem !important; 
          padding-right: 0.5rem !important; 
        }
        
        .today-card { padding: 16px 16px; border-radius: 20px; }
        .today-day  { font-size: 22px; }
        .class-chip { font-size: 11.5px; padding: 5px 10px; margin: 0 4px 4px 0; }
        
        /* 모바일용 시간표 그리드 조정 (간격을 극단적으로 줄임) */
        .timetable-wrapper {
          gap: 3px;
        }
        .tt-filled, .tt-empty { 
          font-size: 10.5px; 
          padding: 6px 1px; 
          min-height: 36px; 
          border-radius: 6px; 
          word-break: break-all; /* 긴 과목명이 모바일에서 줄바꿈되도록 강제 */
        }
        .tt-head { font-size: 10.5px; }
        .tt-period { font-size: 10px; }
        
        .item-card { padding: 12px; }
        .item-title { font-size: 14px; }
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
        st.warning("저장에 실패했어요. (읽기 전용 환경일 수 있습니다)")


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
    if not iso:
        return "날짜 미정"
    try:
        d = datetime.strptime(iso, "%Y-%m-%d").date()
        return f"{d.month}월 {d.day}일"
    except ValueError:
        return "날짜 미정"


def dday(iso: str):
    if not iso:
        return "날짜 미정", "dday"
    try:
        target = datetime.strptime(iso, "%Y-%m-%d").date()
    except ValueError:
        return "날짜 미정", "dday"

    diff = (target - date.today()).days
    if diff == 0:
        return "D-DAY", "dday dday-today"
    if diff > 0:
        return f"D-{diff}", "dday"
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
        sub = "주말이에요! 다음 등교일을 준비해보세요"
        chips = ""
    else:
        classes = [
            (p, DATA["timetable"][f"{day_ko}-{p}"])
            for p in PERIODS
            if DATA["timetable"].get(f"{day_ko}-{p}")
        ]
        if classes:
            sub = f"오늘 {len(classes)}개의 수업이 있어요"
            chips = "".join(
                f'<span class="class-chip"><b>{p}교시</b>{s}</span>' for p, s in classes
            )
        else:
            sub = "아직 등록된 시간표가 없어요"
            chips = '<span class="class-chip">시간표 탭에서 등록해보세요</span>'

    st.markdown(
        f"""
        <div class="today-card">
          <div class="today-day">오늘은 {day_ko}요일</div>
          <div class="today-sub">{today.month}월 {today.day}일 · {sub}</div>
          <div class="chip-wrap">{chips}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    "<h2 style='color:#8C74D6; font-weight:700;'>🗓️ 스쿨플랜</h2>",
    unsafe_allow_html=True,
)
render_today_card()


# ══════════════════════════════════════════════════════════
# 5. 탭 구성
# ══════════════════════════════════════════════════════════
tab_tt, tab_exam, tab_assign, tab_todo = st.tabs(
    ["🗓️ 시간표", "📝 시험", "📌 수행평가", "✅ To Do"]
)


# ──────────────────────────────────────────────────────────
# 5-1. 시간표 탭 (HTML Grid 렌더링 방식)
# ──────────────────────────────────────────────────────────
with tab_tt:
    st.markdown("#### 시간표")
    st.caption("아래에서 요일과 교시를 고른 뒤 과목명을 입력하면 표에 반영돼요.")

    with st.form("tt_form", clear_on_submit=False):
        c1, c2, c3 = st.columns([1, 1, 2])
        with c1:
            sel_day = st.selectbox("요일", DAYS, key="tt_day")
        with c2:
            sel_period = st.selectbox("교시", PERIODS, key="tt_period")
        with c3:
            key = f"{sel_day}-{sel_period}"
            cur = DATA["timetable"].get(key, "")
            subject = st.text_input("과목명", value=cur, max_chars=12, key="tt_subject")

        b1, b2 = st.columns(2)
        with b1:
            submitted = st.form_submit_button("💾 저장", use_container_width=True)
        with b2:
            deleted = st.form_submit_button("🗑️ 이 칸 지우기", use_container_width=True)

    if submitted:
        if subject.strip():
            DATA["timetable"][key] = subject.strip()
            save_data()
            st.success(f"{sel_day}요일 {sel_period}교시 → {subject.strip()}")
        else:
            st.warning("과목명을 입력해주세요.")
        st.rerun()

    if deleted:
        DATA["timetable"].pop(key, None)
        save_data()
        st.info(f"{sel_day}요일 {sel_period}교시를 비웠어요.")
        st.rerun()

    st.markdown("---")

    # 가로 스크롤 방지를 위해 Streamlit Columns 대신 순수 HTML/CSS Grid로 그리기
    html_grid = '<div class="timetable-wrapper">'
    
    # 요일 헤더
    html_grid += '<div class="tt-head"></div>'
    for d in DAYS:
        html_grid += f'<div class="tt-head">{d}</div>'
        
    # 교시 본문
    for p in PERIODS:
        html_grid += f'<div class="tt-period">{p}</div>'
        for d in DAYS:
            val = DATA["timetable"].get(f"{d}-{p}", "")
            cls = "tt-filled" if val else "tt-empty"
            txt = val if val else "-"
            html_grid += f'<div class="{cls}">{txt}</div>'
            
    html_grid += '</div>'
    
    # 화면 출력
    st.markdown(html_grid, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if DATA["timetable"]:
        if st.button("전체 시간표 비우기", key="tt_clear"):
            DATA["timetable"] = {}
            save_data()
            st.rerun()


# ──────────────────────────────────────────────────────────
# 5-2. 시험 탭
# ──────────────────────────────────────────────────────────
with tab_exam:
    st.markdown("#### 시험")

    with st.expander("➕ 시험 추가하기", expanded=len(DATA["exams"]) == 0):
        with st.form("exam_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                e_subject = st.text_input("과목", placeholder="예: 수학", max_chars=20)
            with c2:
                e_date = st.date_input("시험 날짜", value=date.today())
            e_range = st.text_area(
                "시험 범위", placeholder="예: 2단원 이차방정식 ~ 3단원 이차함수"
            )
            if st.form_submit_button("저장", use_container_width=True):
                if e_subject.strip():
                    DATA["exams"].append(
                        {
                            "id": new_id(),
                            "subject": e_subject.strip(),
                            "date": e_date.isoformat(),
                            "range": e_range.strip(),
                        }
                    )
                    save_data()
                    st.success("시험을 등록했어요!")
                    st.rerun()
                else:
                    st.warning("과목을 입력해주세요.")

    if not DATA["exams"]:
        st.markdown(
            "<div class='empty-box'><span class='ic'>📝</span>"
            "등록된 시험이 없어요<br>위에서 시험을 추가해보세요</div>",
            unsafe_allow_html=True,
        )
    else:
        for ex in sort_by_date(DATA["exams"]):
            label, cls = dday(ex["date"])
            col_a, col_b = st.columns([6, 1])
            with col_a:
                desc = (
                    f"<div class='item-desc'>{ex['range']}</div>" if ex["range"] else ""
                )
                st.markdown(
                    f"""
                    <div class="item-card">
                      <span class="tag tag-exam">{ex['subject']}</span>
                      <span class="{cls}">{label}</span>
                      <div class="item-title">{fmt_date(ex['date'])}</div>
                      {desc}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col_b:
                if st.button("🗑️", key=f"del_ex_{ex['id']}", help="삭제"):
                    DATA["exams"] = [x for x in DATA["exams"] if x["id"] != ex["id"]]
                    save_data()
                    st.rerun()


# ──────────────────────────────────────────────────────────
# 5-3. 수행평가 탭
# ──────────────────────────────────────────────────────────
with tab_assign:
    st.markdown("#### 수행평가")

    with st.expander("➕ 수행평가 추가하기", expanded=len(DATA["assignments"]) == 0):
        with st.form("assign_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                a_subject = st.text_input("과목", placeholder="예: 국어", max_chars=20)
            with c2:
                a_date = st.date_input("마감 날짜", value=date.today())
            a_content = st.text_area(
                "수행평가 내용", placeholder="예: 독서 감상문 A4 1장 제출"
            )
            if st.form_submit_button("저장", use_container_width=True):
                if a_subject.strip():
                    DATA["assignments"].append(
                        {
                            "id": new_id(),
                            "subject": a_subject.strip(),
                            "date": a_date.isoformat(),
                            "content": a_content.strip(),
                        }
                    )
                    save_data()
                    st.success("수행평가를 등록했어요!")
                    st.rerun()
                else:
                    st.warning("과목을 입력해주세요.")

    if not DATA["assignments"]:
        st.markdown(
            "<div class='empty-box'><span class='ic'>📌</span>"
            "등록된 수행평가가 없어요<br>위에서 추가해보세요</div>",
            unsafe_allow_html=True,
        )
    else:
        for ag in sort_by_date(DATA["assignments"]):
            label, cls = dday(ag["date"])
            col_a, col_b = st.columns([6, 1])
            with col_a:
                desc = (
                    f"<div class='item-desc'>{ag['content']}</div>"
                    if ag["content"]
                    else ""
                )
                st.markdown(
                    f"""
                    <div class="item-card">
                      <span class="tag tag-assign">{ag['subject']}</span>
                      <span class="{cls}">{label}</span>
                      <div class="item-title">{fmt_date(ag['date'])} 마감</div>
                      {desc}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col_b:
                if st.button("🗑️", key=f"del_ag_{ag['id']}", help="삭제"):
                    DATA["assignments"] = [
                        x for x in DATA["assignments"] if x["id"] != ag["id"]
                    ]
                    save_data()
                    st.rerun()


# ──────────────────────────────────────────────────────────
# 5-4. To Do 탭
# ──────────────────────────────────────────────────────────
with tab_todo:
    st.markdown("#### To Do List")

    with st.form("todo_form", clear_on_submit=True):
        c1, c2 = st.columns([3, 2])
        with c1:
            t_text = st.text_input(
                "할 일", placeholder="예: 수학 문제집 3장 풀기", max_chars=60
            )
        with c2:
            t_date = st.date_input("날짜", value=date.today())
        if st.form_submit_button("➕ 추가", use_container_width=True):
            if t_text.strip():
                DATA["todos"].insert(
                    0,
                    {
                        "id": new_id(),
                        "text": t_text.strip(),
                        "date": t_date.isoformat(),
                        "done": False,
                    },
                )
                save_data()
                st.rerun()
            else:
                st.warning("할 일을 입력해주세요.")

    st.markdown("---")

    if not DATA["todos"]:
        st.markdown(
            "<div class='empty-box'><span class='ic'>✅</span>"
            "등록된 할 일이 없어요<br>위에서 추가해보세요</div>",
            unsafe_allow_html=True,
        )
    else:
        todos = sorted(
            DATA["todos"], key=lambda t: (t["done"], t.get("date") or "9999-99-99")
        )

        done_cnt = sum(1 for t in todos if t["done"])
        st.progress(
            done_cnt / len(todos),
            text=f"완료 {done_cnt} / 전체 {len(todos)}",
        )

        for td in todos:
            c1, c2, c3 = st.columns([1, 6, 1])

            with c1:
                checked = st.checkbox(
                    "완료",
                    value=td["done"],
                    key=f"chk_{td['id']}",
                    label_visibility="collapsed",
                )
                if checked != td["done"]:
                    td["done"] = checked
                    save_data()
                    st.rerun()

            with c2:
                text = td["text"]
                if td["done"]:
                    st.markdown(
                        f"<span style='color:#B0A8C9;text-decoration:line-through;'>"
                        f"{text}</span> "
                        f"<span style='font-size:11px;color:#C9C2DC;'>"
                        f"{fmt_date(td['date'])}</span>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f"<span style='color:#39324D;font-weight:500;'>{text}</span> "
                        f"<span style='font-size:11px;color:#B0A8C9;'>"
                        f"{fmt_date(td['date'])}</span>",
                        unsafe_allow_html=True,
                    )

            with c3:
                if st.button("🗑️", key=f"del_td_{td['id']}", help="삭제"):
                    DATA["todos"] = [x for x in DATA["todos"] if x["id"] != td["id"]]
                    save_data()
                    st.rerun()


# ══════════════════════════════════════════════════════════
# 6. 하단 : 백업 · 초기화
# ══════════════════════════════════════════════════════════
st.markdown("---")
col_l, col_r = st.columns(2)

with col_l:
    st.download_button(
        "⬇️ 내 데이터 백업 (JSON)",
        data=json.dumps(DATA, ensure_ascii=False, indent=2),
        file_name="schoolplan_backup.json",
        mime="application/json",
        use_container_width=True,
    )

with col_r:
    if st.button("🔄 전체 초기화", use_container_width=True):
        st.session_state["confirm_reset"] = True

if st.session_state.get("confirm_reset"):
    st.error("시간표, 시험, 수행평가, 할 일이 **모두 삭제**돼요. 계속할까요?")
    y, n = st.columns(2)
    with y:
        if st.button("네, 초기화합니다", use_container_width=True):
            st.session_state.data = empty_state()
            save_data()
            st.session_state["confirm_reset"] = False
            st.rerun()
    with n:
        if st.button("아니요", use_container_width=True):
            st.session_state["confirm_reset"] = False
            st.rerun()

st.caption("데이터는 이 앱이 실행 중인 컴퓨터에 저장돼요.")
