<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">
<title>스쿨플랜 · School Plan</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
  :root{
    --bg-a:#F3EEFC;
    --bg-b:#EAF7F1;
    --card:#FFFFFF;
    --card-soft:#FBFAFF;
    --lavender:#B9A8EA;
    --lavender-deep:#8C74D6;
    --mint:#9FE3CF;
    --mint-deep:#43A98C;
    --peach:#FFC9A0;
    --peach-deep:#EE8A52;
    --sky:#A7D8F0;
    --sky-deep:#4693C4;
    --text:#39324D;
    --text-soft:#7A7392;
    --text-faint:#B0A8C9;
    --border:#E9E3F8;
    --danger:#EE8E88;
    --danger-deep:#D96760;
    --radius-lg:26px;
    --radius-md:18px;
    --radius-sm:12px;
    --shadow: 0 10px 30px rgba(140,116,214,0.12);
    --shadow-sm: 0 3px 10px rgba(140,116,214,0.10);
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    font-family:'Noto Sans KR', sans-serif;
    color:var(--text);
    background:
      radial-gradient(circle at 10% 0%, var(--bg-a) 0%, transparent 55%),
      radial-gradient(circle at 90% 10%, var(--bg-b) 0%, transparent 50%),
      linear-gradient(160deg, #F8F6FD 0%, #F1FAF5 100%);
    background-attachment:fixed;
    min-height:100vh;
    padding-bottom:96px;
  }
  h1,h2,h3,.brand,.tab-label{font-family:'Gowun Dodum', sans-serif;}
  button{font-family:inherit;}
  .app{max-width:720px;margin:0 auto;padding:20px 16px 40px;}

  /* Header */
  .topbar{display:flex;align-items:center;justify-content:space-between;padding:6px 4px 18px;}
  .brand{display:flex;align-items:center;gap:8px;font-size:22px;font-weight:400;color:var(--lavender-deep);}
  .brand .dot{width:10px;height:10px;border-radius:50%;background:linear-gradient(135deg,var(--lavender),var(--mint));display:inline-block;}
  .date-pill{font-size:13px;color:var(--text-soft);background:var(--card);padding:7px 14px;border-radius:999px;box-shadow:var(--shadow-sm);}

  /* Today card - signature element */
  .today-card{
    position:relative;
    background:linear-gradient(135deg, #C9B8F5 0%, #A8DFF0 55%, #A8ECD6 100%);
    border-radius:var(--radius-lg);
    padding:22px 20px 18px;
    color:#fff;
    overflow:hidden;
    box-shadow:var(--shadow);
    margin-bottom:22px;
  }
  .today-card::before{
    content:"";position:absolute;width:180px;height:180px;border-radius:50%;
    background:rgba(255,255,255,0.18);top:-70px;right:-50px;
  }
  .today-card::after{
    content:"";position:absolute;width:120px;height:120px;border-radius:50%;
    background:rgba(255,255,255,0.14);bottom:-60px;left:-30px;
  }
  .today-head{display:flex;justify-content:space-between;align-items:baseline;position:relative;z-index:1;}
  .today-day{font-family:'Gowun Dodum',sans-serif;font-size:26px;}
  .today-sub{font-size:12.5px;opacity:0.9;margin-top:2px;}
  .today-classes{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 14px;position:relative;z-index:1;}
  .class-chip{background:rgba(255,255,255,0.28);backdrop-filter:blur(2px);padding:7px 12px;border-radius:999px;font-size:13px;font-weight:500;}
  .class-chip b{font-weight:900;margin-right:4px;opacity:0.85;}
  .today-empty{font-size:13px;opacity:0.9;position:relative;z-index:1;}
  .today-todo{position:relative;z-index:1;background:rgba(255,255,255,0.9);border-radius:var(--radius-md);padding:12px 14px;margin-top:6px;}
  .today-todo-title-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;}
  .today-todo-title{font-size:12.5px;color:var(--text-soft);font-weight:700;}
  .today-todo-list{display:flex;flex-direction:column;gap:6px;max-height:150px;overflow-y:auto;}
  .cam-mini-btn{
    border:none;background:var(--lavender-deep);color:#fff;border-radius:999px;padding:6px 12px;
    font-size:12px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:4px;
  }
  .cam-mini-btn:active{transform:scale(0.96);}
  .today-btn-group{display:flex;gap:6px;}
  .pencil-mini-btn{
    border:1.5px solid rgba(255,255,255,0.7);background:rgba(255,255,255,0.15);color:#fff;border-radius:999px;padding:6px 12px;
    font-size:12px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:4px;
  }
  .pencil-mini-btn:active{transform:scale(0.96);}
  .quick-add{display:flex;gap:8px;margin-top:10px;}
  .quick-add input{
    flex:1;border:1.5px solid rgba(255,255,255,0.6);border-radius:var(--radius-sm);padding:9px 12px;font-size:14px;color:var(--text);background:#fff;
  }
  .quick-add input:focus{outline:none;border-color:var(--lavender-deep);}
  .quick-add button{
    border:none;background:var(--lavender-deep);color:#fff;border-radius:var(--radius-sm);padding:0 16px;font-size:13.5px;font-weight:700;cursor:pointer;
  }
  .quick-add button:active{transform:scale(0.97);}

  /* Tabs */
  .tabs{display:flex;gap:6px;background:var(--card);padding:6px;border-radius:999px;box-shadow:var(--shadow-sm);margin-bottom:20px;}
  .tab-btn{
    flex:1;border:none;background:transparent;padding:10px 4px;border-radius:999px;
    font-size:13.5px;font-weight:700;color:var(--text-soft);cursor:pointer;
    display:flex;flex-direction:column;align-items:center;gap:2px;transition:all .18s ease;
  }
  .tab-btn .ic{font-size:17px;}
  .tab-btn.active{background:linear-gradient(135deg,var(--lavender),var(--sky));color:#fff;box-shadow:0 4px 10px rgba(140,116,214,0.35);}

  .panel{display:none;}
  .panel.active{display:block;animation:fadeIn .25s ease;}
  @keyframes fadeIn{from{opacity:0;transform:translateY(4px);}to{opacity:1;transform:translateY(0);}}

  .panel-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;gap:8px;}
  .panel-title{font-size:18px;font-weight:400;color:var(--text);}
  .cam-btn{
    border:none;background:linear-gradient(135deg,var(--lavender-deep),var(--sky-deep));color:#fff;font-weight:700;font-size:13px;
    padding:10px 16px;border-radius:999px;cursor:pointer;box-shadow:var(--shadow-sm);display:flex;align-items:center;gap:6px;white-space:nowrap;
  }
  .cam-btn:active{transform:scale(0.97);}
  .btn-group{display:flex;gap:8px;flex-wrap:wrap;}
  .manual-btn{
    border:1.5px solid var(--border);background:var(--card);color:var(--lavender-deep);font-weight:700;font-size:13px;
    padding:10px 16px;border-radius:999px;cursor:pointer;display:flex;align-items:center;gap:6px;white-space:nowrap;
  }
  .manual-btn:active{transform:scale(0.97);}

  .hint-banner{
    background:var(--card-soft);border:1.5px dashed var(--border);border-radius:var(--radius-md);
    padding:14px 16px;font-size:12.5px;color:var(--text-soft);margin-bottom:14px;line-height:1.6;
  }

  /* Timetable */
  .timetable-wrap{overflow-x:auto;background:var(--card);border-radius:var(--radius-md);box-shadow:var(--shadow-sm);padding:12px;}
  table.timetable{border-collapse:separate;border-spacing:6px;width:100%;min-width:520px;}
  table.timetable th{font-size:12.5px;color:var(--text-soft);font-weight:700;padding:4px;}
  table.timetable td.period-cell{font-size:12px;color:var(--text-faint);text-align:center;font-weight:700;width:34px;}
  .tt-cell{
    background:var(--card-soft);border-radius:var(--radius-sm);min-height:52px;height:52px;text-align:center;
    cursor:pointer;font-size:13px;font-weight:500;color:var(--text);border:1.5px solid var(--border);
    transition:all .15s ease;padding:4px;display:flex;align-items:center;justify-content:center;
  }
  .tt-cell:hover{border-color:var(--lavender);}
  .tt-cell.filled{background:linear-gradient(135deg,#EFE9FC,#E7F6EF);border-color:transparent;color:var(--text);font-weight:700;}
  .tt-cell.empty-cell{color:var(--text-faint);font-weight:400;}

  /* List cards (exam / assignment / todo) */
  .list{display:flex;flex-direction:column;gap:10px;}
  .item-card{
    background:var(--card);border-radius:var(--radius-md);padding:14px 16px;box-shadow:var(--shadow-sm);
    display:flex;justify-content:space-between;align-items:flex-start;gap:10px;
  }
  .item-main{flex:1;min-width:0;}
  .item-top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:5px;}
  .subject-tag{
    font-size:11.5px;font-weight:700;padding:3px 10px;border-radius:999px;color:#fff;
  }
  .tag-exam{background:var(--sky-deep);}
  .tag-assign{background:var(--peach-deep);}
  .dday{font-size:11.5px;font-weight:700;color:var(--lavender-deep);background:#F1ECFC;padding:3px 9px;border-radius:999px;}
  .dday.today{color:var(--danger-deep);background:#FCECEA;}
  .dday.past{color:var(--text-faint);background:#F2F0F7;}
  .item-title{font-size:15px;font-weight:700;color:var(--text);}
  .item-desc{font-size:13px;color:var(--text-soft);margin-top:4px;line-height:1.5;white-space:pre-wrap;}
  .item-actions{display:flex;gap:6px;flex-shrink:0;}
  .icon-btn{
    border:none;background:var(--card-soft);width:30px;height:30px;border-radius:50%;cursor:pointer;font-size:13px;
    display:flex;align-items:center;justify-content:center;color:var(--text-soft);
  }
  .icon-btn:hover{background:var(--border);}

  .todo-row{display:flex;align-items:center;gap:10px;}
  .todo-check{
    width:22px;height:22px;border-radius:7px;border:2px solid var(--lavender);flex-shrink:0;cursor:pointer;
    display:flex;align-items:center;justify-content:center;font-size:13px;color:#fff;background:transparent;
  }
  .todo-check.done{background:var(--lavender-deep);border-color:var(--lavender-deep);}
  .todo-text{font-size:14.5px;font-weight:500;flex:1;}
  .todo-text.done{text-decoration:line-through;color:var(--text-faint);}
  .todo-date-tag{font-size:11px;color:var(--text-faint);}

  .empty-state{
    text-align:center;padding:36px 20px;color:var(--text-faint);font-size:13.5px;
    background:var(--card);border-radius:var(--radius-md);box-shadow:var(--shadow-sm);
  }
  .empty-state .em-ic{font-size:30px;display:block;margin-bottom:8px;}
  .empty-state .em-btns{display:flex;gap:8px;justify-content:center;margin-top:14px;flex-wrap:wrap;}
  .empty-state .em-cam{
    border:none;background:var(--lavender-deep);color:#fff;font-weight:700;font-size:13px;
    padding:10px 18px;border-radius:999px;cursor:pointer;
  }
  .empty-state .em-manual{
    border:1.5px solid var(--border);background:#fff;color:var(--lavender-deep);font-weight:700;font-size:13px;
    padding:10px 18px;border-radius:999px;cursor:pointer;
  }

  /* Modal */
  .modal-overlay{
    position:fixed;inset:0;background:rgba(57,50,77,0.4);display:none;align-items:flex-end;justify-content:center;z-index:100;
  }
  .modal-overlay.open{display:flex;}
  .modal{
    background:#fff;border-radius:24px 24px 0 0;padding:20px;width:100%;max-width:520px;
    box-shadow:0 -10px 30px rgba(0,0,0,0.15);animation:slideUp .22s ease;
    max-height:88vh;overflow-y:auto;
  }
  @media(min-width:620px){
    .modal-overlay{align-items:center;}
    .modal{border-radius:24px;}
  }
  @keyframes slideUp{from{transform:translateY(30px);opacity:0;}to{transform:translateY(0);opacity:1;}}
  .modal h3{margin:0 0 4px;font-size:17px;color:var(--text);font-weight:400;}
  .modal .modal-sub{font-size:12.5px;color:var(--text-soft);margin-bottom:16px;line-height:1.5;}

  .field label{display:block;font-size:12px;color:var(--text-soft);font-weight:700;margin-bottom:5px;}
  .field input, .field textarea, .field select{
    width:100%;border:1.5px solid var(--border);border-radius:var(--radius-sm);padding:10px 12px;font-size:14px;color:var(--text);background:#FCFBFF;
  }
  .field input:focus, .field textarea:focus, .field select:focus{outline:none;border-color:var(--lavender);background:#fff;}
  .field textarea{resize:vertical;min-height:56px;}
  .form-row{display:flex;gap:10px;}
  .form-row .field{flex:1;}
  .form-actions{display:flex;gap:8px;justify-content:flex-end;margin-top:14px;}
  .btn-primary{
    border:none;background:var(--lavender-deep);color:#fff;font-weight:700;font-size:13.5px;
    padding:10px 18px;border-radius:999px;cursor:pointer;
  }
  .btn-primary:disabled{opacity:0.45;cursor:not-allowed;}
  .btn-ghost{
    border:1.5px solid var(--border);background:transparent;color:var(--text-soft);font-weight:700;font-size:13.5px;
    padding:10px 18px;border-radius:999px;cursor:pointer;
  }

  /* capture ui */
  .capture-drop{
    border:2px dashed var(--border);border-radius:var(--radius-md);padding:26px 16px;text-align:center;
    background:var(--card-soft);cursor:pointer;
  }
  .capture-drop .cap-ic{font-size:34px;display:block;margin-bottom:8px;}
  .capture-drop .cap-txt{font-size:13.5px;font-weight:700;color:var(--text);}
  .capture-drop .cap-sub{font-size:12px;color:var(--text-faint);margin-top:4px;}
  .capture-preview{width:100%;border-radius:var(--radius-md);margin-top:12px;max-height:260px;object-fit:contain;background:#F4F2FA;}
  .analyzing{display:flex;flex-direction:column;align-items:center;gap:10px;padding:24px 10px;}
  .spinner{
    width:34px;height:34px;border-radius:50%;border:3.5px solid var(--border);border-top-color:var(--lavender-deep);
    animation:spin 0.8s linear infinite;
  }
  @keyframes spin{to{transform:rotate(360deg);}}
  .analyzing-txt{font-size:13.5px;color:var(--text-soft);font-weight:700;}

  .review-row{
    background:var(--card-soft);border-radius:var(--radius-sm);padding:12px;margin-bottom:10px;
    display:flex;flex-direction:column;gap:8px;position:relative;
  }
  .review-row .row-remove{
    position:absolute;top:8px;right:8px;border:none;background:transparent;color:var(--text-faint);
    cursor:pointer;font-size:13px;width:24px;height:24px;
  }
  .review-row .form-row{gap:8px;}
  .add-row-btn{
    border:1.5px dashed var(--border);background:transparent;color:var(--text-soft);font-weight:700;font-size:13px;
    padding:10px;border-radius:var(--radius-sm);cursor:pointer;width:100%;
  }

  /* Bottom mobile nav wrapper (tabs become fixed on mobile) */
  @media (max-width:640px){
    .app{padding-bottom:110px;}
    .tabs{
      position:fixed;bottom:14px;left:12px;right:12px;z-index:50;margin:0;
    }
    .panel-head{flex-wrap:wrap;}
  }

  .toast{
    position:fixed;bottom:120px;left:50%;transform:translateX(-50%);
    background:var(--text);color:#fff;padding:10px 18px;border-radius:999px;font-size:13px;
    box-shadow:var(--shadow);opacity:0;pointer-events:none;transition:opacity .25s ease, transform .25s ease;z-index:200;
    max-width:88%;text-align:center;
  }
  .toast.show{opacity:1;transform:translateX(-50%) translateY(-6px);}

  .footer-note{text-align:center;font-size:11.5px;color:var(--text-faint);margin-top:26px;}
  .footer-note button{background:none;border:none;color:var(--text-faint);text-decoration:underline;cursor:pointer;font-size:11.5px;}
</style>
</head>
<body>

<div class="app">
  <div class="topbar">
    <div class="brand"><span class="dot"></span>스쿨플랜</div>
    <div class="date-pill" id="topDate">-</div>
  </div>

  <div class="today-card">
    <div class="today-head">
      <div>
        <div class="today-day" id="todayDayLabel">오늘</div>
        <div class="today-sub" id="todaySub">오늘 일정을 확인해보세요</div>
      </div>
    </div>
    <div class="today-classes" id="todayClasses"></div>
    <div class="today-todo">
      <div class="today-todo-title-row">
        <div class="today-todo-title">✅ 오늘 할 일</div>
      </div>
      <div class="today-todo-list" id="todayTodoList"></div>
      <div class="quick-add">
        <input type="text" id="quickAddInput" placeholder="오늘 할 일을 입력하세요" maxlength="60">
        <button id="quickAddBtn">추가</button>
      </div>
    </div>
  </div>

  <div class="tabs">
    <button class="tab-btn active" data-tab="timetable"><span class="ic">🗓️</span><span class="tab-label">시간표</span></button>
    <button class="tab-btn" data-tab="exams"><span class="ic">📝</span><span class="tab-label">시험</span></button>
    <button class="tab-btn" data-tab="assignments"><span class="ic">📌</span><span class="tab-label">수행평가</span></button>
    <button class="tab-btn" data-tab="todos"><span class="ic">✅</span><span class="tab-label">To Do</span></button>
  </div>

  <!-- 시간표 -->
  <section class="panel active" id="panel-timetable">
    <div class="panel-head">
      <div class="panel-title">시간표</div>
      <div class="btn-group">
        <button class="cam-btn" data-cap="timetable">📷 촬영</button>
      </div>
    </div>
    <div class="hint-banner">📷 시간표 사진을 올리면 자동으로 채워져요. 표의 칸을 직접 눌러서 과목을 입력하거나 수정할 수도 있어요.</div>
    <div class="timetable-wrap">
      <table class="timetable" id="timetableGrid"></table>
    </div>
  </section>

  <!-- 시험 -->
  <section class="panel" id="panel-exams">
    <div class="panel-head">
      <div class="panel-title">시험</div>
      <div class="btn-group">
        <button class="cam-btn" data-cap="exam">📷 촬영</button>
        <button class="manual-btn" data-manual="exam">✏️ 직접 입력</button>
      </div>
    </div>
    <div class="list" id="examList"></div>
  </section>

  <!-- 수행평가 -->
  <section class="panel" id="panel-assignments">
    <div class="panel-head">
      <div class="panel-title">수행평가</div>
      <div class="btn-group">
        <button class="cam-btn" data-cap="assignment">📷 촬영</button>
        <button class="manual-btn" data-manual="assignment">✏️ 직접 입력</button>
      </div>
    </div>
    <div class="list" id="assignList"></div>
  </section>

  <!-- To Do -->
  <section class="panel" id="panel-todos">
    <div class="panel-head">
      <div class="panel-title">To Do List</div>
      <div class="btn-group">
        <button class="manual-btn" data-manual="todo">✏️ 할 일 추가</button>
      </div>
    </div>
    <div class="list" id="todoList"></div>
  </section>

  <div class="footer-note">내 브라우저에만 저장돼요 · <button id="resetAllBtn">전체 초기화</button></div>
</div>

<div class="modal-overlay" id="modalOverlay">
  <div class="modal" id="modalBody"></div>
</div>
<div class="toast" id="toast"></div>

<script>
const DAYS = ['월','화','수','목','금'];
const PERIODS = [1,2,3,4,5,6,7];

let state = { timetable:{}, exams:[], assignments:[], todos:[] };

/* ---------- storage helpers ---------- */
async function loadKey(key, fallback){
  try{
    const res = await window.storage.get(key, false);
    return res ? JSON.parse(res.value) : fallback;
  }catch(e){ return fallback; }
}
async function saveKey(key, value){
  try{ await window.storage.set(key, JSON.stringify(value), false); }
  catch(e){ console.error('저장 실패', key, e); showToast('저장에 실패했어요. 다시 시도해주세요'); }
}
function uid(){ return Date.now().toString(36)+Math.random().toString(36).slice(2,7); }

/* ---------- date helpers ---------- */
function todayISO(){
  const d = new Date();
  return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
}
function fmtDateLabel(iso){
  if(!iso) return '날짜 미정';
  const [y,m,d] = iso.split('-');
  return `${m}월 ${d}일`;
}
function ddayInfo(iso){
  if(!iso) return {label:'날짜 미정', cls:''};
  const today = new Date(todayISO()+'T00:00:00');
  const target = new Date(iso+'T00:00:00');
  const diff = Math.round((target-today)/86400000);
  if(diff===0) return {label:'D-DAY', cls:'today'};
  if(diff>0) return {label:'D-'+diff, cls:''};
  return {label:'지남', cls:'past'};
}
function todayKoreanDay(){
  const idx = new Date().getDay();
  const map = ['일','월','화','수','목','금','토'];
  return map[idx];
}

/* ---------- toast ---------- */
let toastTimer;
function showToast(msg){
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(()=>t.classList.remove('show'), 2200);
}

/* ---------- modal ---------- */
function openModal(html){
  document.getElementById('modalBody').innerHTML = html;
  document.getElementById('modalOverlay').classList.add('open');
}
function closeModal(){
  document.getElementById('modalOverlay').classList.remove('open');
}
document.getElementById('modalOverlay').addEventListener('click', (e)=>{
  if(e.target.id === 'modalOverlay') closeModal();
});

/* ---------- tabs ---------- */
document.querySelectorAll('.tab-btn').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
    document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('panel-'+btn.dataset.tab).classList.add('active');
  });
});

/* ---------- header date ---------- */
function renderHeaderDate(){
  const d = new Date();
  document.getElementById('topDate').textContent = `${d.getMonth()+1}월 ${d.getDate()}일 (${todayKoreanDay()})`;
}

/* ================= TIMETABLE render ================= */
function buildTimetableGrid(){
  const table = document.getElementById('timetableGrid');
  let html = '<tr><th></th>' + DAYS.map(d=>`<th>${d}</th>`).join('') + '</tr>';
  PERIODS.forEach(p=>{
    html += `<tr><td class="period-cell">${p}교시</td>`;
    DAYS.forEach(day=>{
      const key = day+'-'+p;
      const val = state.timetable[key];
      html += `<td><div class="tt-cell ${val?'filled':'empty-cell'}" data-key="${key}">${val ? escapeHtml(val) : ''}</div></td>`;
    });
    html += '</tr>';
  });
  table.innerHTML = html;
  table.querySelectorAll('.tt-cell').forEach(cell=>{
    cell.addEventListener('click', ()=> openCellFixModal(cell.dataset.key));
  });
}
function openCellFixModal(key){
  const [day, period] = key.split('-');
  const current = state.timetable[key] || '';
  openModal(`
    <h3>${day}요일 ${period}교시</h3>
    <div class="modal-sub">과목명을 직접 입력하거나 수정할 수 있어요.</div>
    <div class="field"><label>과목명</label><input type="text" id="cellInput" value="${escapeHtml(current)}" maxlength="12"></div>
    <div class="form-actions">
      <button class="btn-ghost" id="cellDelete">삭제</button>
      <button class="btn-ghost" id="cellCancel">취소</button>
      <button class="btn-primary" id="cellSave">저장</button>
    </div>
  `);
  document.getElementById('cellCancel').addEventListener('click', closeModal);
  document.getElementById('cellSave').addEventListener('click', async ()=>{
    const val = document.getElementById('cellInput').value.trim();
    if(val) state.timetable[key] = val; else delete state.timetable[key];
    await saveKey('timetable', state.timetable);
    buildTimetableGrid(); renderTodayCard(); closeModal();
  });
  document.getElementById('cellDelete').addEventListener('click', async ()=>{
    delete state.timetable[key];
    await saveKey('timetable', state.timetable);
    buildTimetableGrid(); renderTodayCard(); closeModal();
  });
}

/* ================= TODAY CARD ================= */
function renderTodayCard(){
  const dayKo = todayKoreanDay();
  document.getElementById('todayDayLabel').textContent = `오늘은 ${dayKo}요일`;
  const isWeekend = (dayKo === '토' || dayKo === '일');
  const classesEl = document.getElementById('todayClasses');
  const subEl = document.getElementById('todaySub');

  if(isWeekend){
    subEl.textContent = '주말이에요! 다음 등교일을 준비해보세요';
    classesEl.innerHTML = '';
  } else {
    const todays = PERIODS.map(p=>({p, subject: state.timetable[dayKo+'-'+p]})).filter(x=>x.subject);
    if(todays.length){
      subEl.textContent = `오늘 ${todays.length}개의 수업이 있어요`;
      classesEl.innerHTML = todays.map(t=>`<div class="class-chip"><b>${t.p}교시</b>${escapeHtml(t.subject)}</div>`).join('');
    } else {
      subEl.textContent = '아직 등록된 시간표가 없어요';
      classesEl.innerHTML = `<div class="today-empty">시간표 탭에서 시간표 사진을 등록해보세요</div>`;
    }
  }

  const todoListEl = document.getElementById('todayTodoList');
  const todays = state.todos.filter(t=>t.date === todayISO()).sort((a,b)=>a.done-b.done);
  if(todays.length===0){
    todoListEl.innerHTML = `<div style="font-size:13px;color:rgba(57,50,77,0.7);padding:4px 0;">오늘 할 일이 없어요. 메모나 알림장을 촬영해보세요</div>`;
  } else {
    todoListEl.innerHTML = todays.map(t=>`
      <div class="todo-row">
        <button class="todo-check ${t.done?'done':''}" data-id="${t.id}">${t.done?'✓':''}</button>
        <div class="todo-text ${t.done?'done':''}">${escapeHtml(t.text)}</div>
      </div>`).join('');
    todoListEl.querySelectorAll('.todo-check').forEach(btn=>{
      btn.addEventListener('click', ()=>toggleTodo(btn.dataset.id));
    });
  }
}
document.getElementById('quickAddBtn').addEventListener('click', quickAddTodo);
document.getElementById('quickAddInput').addEventListener('keydown', (e)=>{ if(e.key==='Enter') quickAddTodo(); });
async function quickAddTodo(){
  const input = document.getElementById('quickAddInput');
  const val = input.value.trim();
  if(!val) return;
  state.todos.unshift({id:uid(), text:val, date: todayISO(), done:false});
  await saveKey('todos', state.todos);
  input.value = '';
  renderTodayCard();
  renderTodos();
  showToast('오늘 할 일에 추가했어요');
}

/* ================= RENDER: exams / assignments / todos ================= */
function renderExams(){
  const el = document.getElementById('examList');
  if(state.exams.length===0){
    el.innerHTML = `<div class="empty-state"><span class="em-ic">📝</span>등록된 시험이 없어요<br>사진을 올리거나 직접 입력해보세요
      <div class="em-btns"><button class="em-cam" data-cap="exam">📷 촬영하기</button><button class="em-manual" data-manual="exam">✏️ 직접 입력</button></div></div>`;
    el.querySelector('.em-cam').addEventListener('click', ()=>openCaptureFlow('exam'));
    el.querySelector('.em-manual').addEventListener('click', ()=>openManualAddModal('exam'));
    return;
  }
  const sorted = [...state.exams].sort((a,b)=> (a.date||'9999').localeCompare(b.date||'9999'));
  el.innerHTML = sorted.map(ex=>{
    const dd = ddayInfo(ex.date);
    return `
    <div class="item-card">
      <div class="item-main">
        <div class="item-top">
          <span class="subject-tag tag-exam">${escapeHtml(ex.subject)}</span>
          <span class="dday ${dd.cls}">${dd.label}</span>
        </div>
        <div class="item-title">${fmtDateLabel(ex.date)}</div>
        ${ex.range ? `<div class="item-desc">${escapeHtml(ex.range)}</div>` : ''}
      </div>
      <div class="item-actions">
        <button class="icon-btn" data-act="edit" data-id="${ex.id}">✏️</button>
        <button class="icon-btn" data-act="del" data-id="${ex.id}">🗑️</button>
      </div>
    </div>`;
  }).join('');
  el.querySelectorAll('[data-act="del"]').forEach(b=>b.addEventListener('click', ()=>deleteItem('exams', b.dataset.id, renderExams)));
  el.querySelectorAll('[data-act="edit"]').forEach(b=>b.addEventListener('click', ()=>editExam(b.dataset.id)));
}
function editExam(id){
  const ex = state.exams.find(e=>e.id===id);
  if(!ex) return;
  openModal(`
    <h3>시험 정보 수정</h3>
    <div class="modal-sub">사진 인식 결과가 틀렸다면 고쳐주세요.</div>
    <div class="field"><label>과목</label><input type="text" id="mExamSubject" value="${escapeHtml(ex.subject)}"></div>
    <div class="field"><label>시험 날짜</label><input type="date" id="mExamDate" value="${ex.date||''}"></div>
    <div class="field"><label>시험 범위</label><textarea id="mExamRange">${escapeHtml(ex.range||'')}</textarea></div>
    <div class="form-actions">
      <button class="btn-ghost" id="mCancel">취소</button>
      <button class="btn-primary" id="mSave">저장</button>
    </div>
  `);
  document.getElementById('mCancel').addEventListener('click', closeModal);
  document.getElementById('mSave').addEventListener('click', async ()=>{
    ex.subject = document.getElementById('mExamSubject').value.trim() || ex.subject;
    ex.date = document.getElementById('mExamDate').value;
    ex.range = document.getElementById('mExamRange').value.trim();
    await saveKey('exams', state.exams);
    renderExams(); closeModal();
  });
}

function renderAssignments(){
  const el = document.getElementById('assignList');
  if(state.assignments.length===0){
    el.innerHTML = `<div class="empty-state"><span class="em-ic">📌</span>등록된 수행평가가 없어요<br>사진을 올리거나 직접 입력해보세요
      <div class="em-btns"><button class="em-cam" data-cap="assignment">📷 촬영하기</button><button class="em-manual" data-manual="assignment">✏️ 직접 입력</button></div></div>`;
    el.querySelector('.em-cam').addEventListener('click', ()=>openCaptureFlow('assignment'));
    el.querySelector('.em-manual').addEventListener('click', ()=>openManualAddModal('assignment'));
    return;
  }
  const sorted = [...state.assignments].sort((a,b)=> (a.date||'9999').localeCompare(b.date||'9999'));
  el.innerHTML = sorted.map(a=>{
    const dd = ddayInfo(a.date);
    return `
    <div class="item-card">
      <div class="item-main">
        <div class="item-top">
          <span class="subject-tag tag-assign">${escapeHtml(a.subject)}</span>
          <span class="dday ${dd.cls}">${dd.label}</span>
        </div>
        <div class="item-title">${fmtDateLabel(a.date)} 마감</div>
        ${a.content ? `<div class="item-desc">${escapeHtml(a.content)}</div>` : ''}
      </div>
      <div class="item-actions">
        <button class="icon-btn" data-act="edit" data-id="${a.id}">✏️</button>
        <button class="icon-btn" data-act="del" data-id="${a.id}">🗑️</button>
      </div>
    </div>`;
  }).join('');
  el.querySelectorAll('[data-act="del"]').forEach(b=>b.addEventListener('click', ()=>deleteItem('assignments', b.dataset.id, renderAssignments)));
  el.querySelectorAll('[data-act="edit"]').forEach(b=>b.addEventListener('click', ()=>editAssign(b.dataset.id)));
}
function editAssign(id){
  const a = state.assignments.find(x=>x.id===id);
  if(!a) return;
  openModal(`
    <h3>수행평가 수정</h3>
    <div class="modal-sub">사진 인식 결과가 틀렸다면 고쳐주세요.</div>
    <div class="field"><label>과목</label><input type="text" id="mASubject" value="${escapeHtml(a.subject)}"></div>
    <div class="field"><label>마감 날짜</label><input type="date" id="mADate" value="${a.date||''}"></div>
    <div class="field"><label>내용</label><textarea id="mAContent">${escapeHtml(a.content||'')}</textarea></div>
    <div class="form-actions">
      <button class="btn-ghost" id="mCancel">취소</button>
      <button class="btn-primary" id="mSave">저장</button>
    </div>
  `);
  document.getElementById('mCancel').addEventListener('click', closeModal);
  document.getElementById('mSave').addEventListener('click', async ()=>{
    a.subject = document.getElementById('mASubject').value.trim() || a.subject;
    a.date = document.getElementById('mADate').value;
    a.content = document.getElementById('mAContent').value.trim();
    await saveKey('assignments', state.assignments);
    renderAssignments(); closeModal();
  });
}

function renderTodos(){
  const el = document.getElementById('todoList');
  if(state.todos.length===0){
    el.innerHTML = `<div class="empty-state"><span class="em-ic">✅</span>등록된 할 일이 없어요<br>할 일을 입력해보세요
      <div class="em-btns"><button class="em-manual" data-manual="todo">✏️ 할 일 추가</button></div></div>`;
    el.querySelector('.em-manual').addEventListener('click', ()=>openManualAddModal('todo'));
    return;
  }
  const sorted = [...state.todos].sort((a,b)=>{
    if(a.done!==b.done) return a.done - b.done;
    return (a.date||'9999').localeCompare(b.date||'9999');
  });
  el.innerHTML = sorted.map(t=>`
    <div class="item-card">
      <div class="todo-row" style="flex:1;">
        <button class="todo-check ${t.done?'done':''}" data-id="${t.id}">${t.done?'✓':''}</button>
        <div style="flex:1;">
          <div class="todo-text ${t.done?'done':''}">${escapeHtml(t.text)}</div>
          <div class="todo-date-tag">${fmtDateLabel(t.date)}</div>
        </div>
      </div>
      <div class="item-actions">
        <button class="icon-btn" data-act="del" data-id="${t.id}">🗑️</button>
      </div>
    </div>`).join('');
  el.querySelectorAll('.todo-check').forEach(b=>b.addEventListener('click', ()=>toggleTodo(b.dataset.id)));
  el.querySelectorAll('[data-act="del"]').forEach(b=>b.addEventListener('click', ()=>deleteItem('todos', b.dataset.id, renderTodos)));
}
async function toggleTodo(id){
  const t = state.todos.find(x=>x.id===id);
  if(!t) return;
  t.done = !t.done;
  await saveKey('todos', state.todos);
  renderTodos(); renderTodayCard();
}
async function deleteItem(collection, id, rerender){
  if(!confirm('삭제할까요?')) return;
  state[collection] = state[collection].filter(x=>x.id!==id);
  await saveKey(collection, state[collection]);
  rerender();
  if(collection==='todos') renderTodayCard();
}

/* ================= shared helpers ================= */
function escapeHtml(str){
  return String(str).replace(/[&<>"']/g, (c)=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

/* ================= PHOTO CAPTURE + AI ANALYSIS ================= */
const CAPTURE_CONFIG = {
  timetable: {
    title: '시간표 촬영',
    sub: '주간 시간표 사진을 올리면 요일·교시별 과목을 자동으로 읽어드려요.',
    prompt: `이 이미지는 학생의 주간 시간표 사진입니다. 표를 분석해서 요일(월,화,수,목,금)과 교시(보통 1~7)별 과목명을 추출하세요.
다른 설명 없이 아래 형식의 순수 JSON 배열만 출력하세요. 코드블록 기호(\`\`\`)도 쓰지 마세요.
[{"day":"월","period":1,"subject":"수학"}, {"day":"월","period":2,"subject":"영어"}, ...]
읽을 수 없거나 비어있는 칸은 결과에 포함하지 마세요.`
  },
  exam: {
    title: '시험 안내문 촬영',
    sub: '시험 일정표나 시험 범위 안내문을 올리면 과목·날짜·범위를 자동으로 정리해드려요.',
    prompt: `이 이미지는 학교 시험 일정 또는 시험 범위 안내문입니다. 과목별 시험 날짜와 시험 범위(단원명)를 추출하세요.
다른 설명 없이 아래 형식의 순수 JSON 배열만 출력하세요. 코드블록 기호는 쓰지 마세요.
[{"subject":"수학","date":"2026-09-15","range":"2단원 이차방정식~3단원 이차함수"}, ...]
연도가 안 적혀 있으면 2026년으로 가정하세요. 날짜를 정확히 모르면 date는 빈 문자열("")로 두세요.`
  },
  assignment: {
    title: '수행평가 안내문 촬영',
    sub: '수행평가 안내문이나 알림장을 올리면 과목·마감일·내용을 자동으로 정리해드려요.',
    prompt: `이 이미지는 학교 수행평가 안내문 또는 알림장입니다. 과목별 수행평가 내용과 마감(제출) 날짜를 추출하세요.
다른 설명 없이 아래 형식의 순수 JSON 배열만 출력하세요. 코드블록 기호는 쓰지 마세요.
[{"subject":"국어","date":"2026-09-10","content":"독서 감상문 A4 1장 제출"}, ...]
연도가 안 적혀 있으면 2026년으로 가정하세요. 날짜를 정확히 모르면 date는 빈 문자열("")로 두세요.`
  }
};

document.querySelectorAll('[data-cap]').forEach(btn=>{
  btn.addEventListener('click', ()=>openCaptureFlow(btn.dataset.cap));
});
document.querySelectorAll('[data-manual]').forEach(btn=>{
  btn.addEventListener('click', ()=>openManualAddModal(btn.dataset.manual));
});

/* ================= MANUAL (typed) ADD ================= */
function openManualAddModal(type){
  const titles = { exam:'시험 직접 입력', assignment:'수행평가 직접 입력', todo:'할 일 직접 입력' };
  let fieldsHtml = '';
  if(type === 'exam'){
    fieldsHtml = `
      <div class="form-row">
        <div class="field"><label>과목</label><input type="text" id="manSubject" placeholder="예: 수학" maxlength="20"></div>
        <div class="field"><label>시험 날짜</label><input type="date" id="manDate"></div>
      </div>
      <div class="field"><label>시험 범위 (단원명)</label><textarea id="manExtra" placeholder="예: 2단원 이차방정식 ~ 3단원 이차함수"></textarea></div>`;
  } else if(type === 'assignment'){
    fieldsHtml = `
      <div class="form-row">
        <div class="field"><label>과목</label><input type="text" id="manSubject" placeholder="예: 국어" maxlength="20"></div>
        <div class="field"><label>마감 날짜</label><input type="date" id="manDate"></div>
      </div>
      <div class="field"><label>수행평가 내용</label><textarea id="manExtra" placeholder="예: 독서 감상문 A4 1장 제출"></textarea></div>`;
  } else if(type === 'todo'){
    fieldsHtml = `
      <div class="field"><label>할 일</label><input type="text" id="manSubject" placeholder="예: 수학 문제집 3장 풀기" maxlength="60"></div>
      <div class="field"><label>날짜</label><input type="date" id="manDate"></div>`;
  }
  openModal(`
    <h3>${titles[type]}</h3>
    ${fieldsHtml}
    <div class="form-actions">
      <button class="btn-ghost" id="manCancel">취소</button>
      <button class="btn-primary" id="manSave">저장</button>
    </div>
  `);
  if(type === 'todo'){
    document.getElementById('manDate').value = todayISO();
  }
  document.getElementById('manCancel').addEventListener('click', closeModal);
  document.getElementById('manSave').addEventListener('click', async ()=>{
    const subject = document.getElementById('manSubject').value.trim();
    const date = document.getElementById('manDate').value;
    const extra = document.getElementById('manExtra') ? document.getElementById('manExtra').value.trim() : '';
    if(!subject){ showToast(type==='todo' ? '할 일을 입력해주세요' : '과목을 입력해주세요'); return; }
    if(type === 'exam'){
      state.exams.push({id:uid(), subject, date, range: extra});
      await saveKey('exams', state.exams);
      renderExams();
    } else if(type === 'assignment'){
      state.assignments.push({id:uid(), subject, date, content: extra});
      await saveKey('assignments', state.assignments);
      renderAssignments();
    } else if(type === 'todo'){
      state.todos.unshift({id:uid(), text: subject, date: date || todayISO(), done:false});
      await saveKey('todos', state.todos);
      renderTodos(); renderTodayCard();
    }
    closeModal();
    showToast('저장했어요');
  });
}

function openCaptureFlow(type){
  const cfg = CAPTURE_CONFIG[type];
  openModal(`
    <h3>${cfg.title}</h3>
    <div class="modal-sub">${cfg.sub}</div>
    <label class="capture-drop" id="captureDrop">
      <span class="cap-ic">📷</span>
      <span class="cap-txt">탭해서 사진 촬영 또는 갤러리에서 선택</span>
      <span class="cap-sub">JPG, PNG 사진을 올려주세요</span>
      <input type="file" accept="image/*" capture="environment" id="captureInput" style="display:none;">
    </label>
    <img id="capturePreview" class="capture-preview" style="display:none;">
    <div class="form-actions">
      <button class="btn-ghost" id="capCancel">취소</button>
      <button class="btn-primary" id="capAnalyze" disabled>분석하기</button>
    </div>
  `);
  let base64Data = null, mediaType = null;

  document.getElementById('capCancel').addEventListener('click', closeModal);
  const input = document.getElementById('captureInput');
  input.addEventListener('change', async (e)=>{
    const file = e.target.files[0];
    if(!file) return;
    try{
      const resized = await resizeImageToBase64(file);
      base64Data = resized.base64;
      mediaType = resized.mediaType;
      const preview = document.getElementById('capturePreview');
      preview.src = 'data:'+mediaType+';base64,'+base64Data;
      preview.style.display = 'block';
      document.getElementById('capAnalyze').disabled = false;
    }catch(err){
      showToast('사진을 불러오지 못했어요. 다시 시도해주세요');
    }
  });

  document.getElementById('capAnalyze').addEventListener('click', async ()=>{
    if(!base64Data) return;
    showAnalyzingState(cfg.title);
    try{
      const items = await callClaudeVision(base64Data, mediaType, cfg.prompt);
      if(!Array.isArray(items) || items.length===0){
        showAnalyzeError(type, '사진에서 정보를 찾지 못했어요. 더 밝고 또렷하게 다시 찍어주세요.');
        return;
      }
      showReviewModal(type, items);
    }catch(err){
      console.error(err);
      showAnalyzeError(type, '분석 중 문제가 생겼어요. 다시 시도해주세요.');
    }
  });
}

function showAnalyzingState(title){
  openModal(`
    <h3>${title}</h3>
    <div class="analyzing">
      <div class="spinner"></div>
      <div class="analyzing-txt">사진을 분석하고 있어요...</div>
    </div>
  `);
}
function showAnalyzeError(type, msg){
  openModal(`
    <h3>분석 실패</h3>
    <div class="modal-sub">${msg}</div>
    <div class="form-actions">
      <button class="btn-ghost" id="errCancel">닫기</button>
      <button class="btn-primary" id="errRetry">다시 촬영</button>
    </div>
  `);
  document.getElementById('errCancel').addEventListener('click', closeModal);
  document.getElementById('errRetry').addEventListener('click', ()=>openCaptureFlow(type));
}

/* resize + base64 encode */
function resizeImageToBase64(file, maxWidth=1100, quality=0.82){
  return new Promise((resolve, reject)=>{
    const reader = new FileReader();
    reader.onload = (e)=>{
      const img = new Image();
      img.onload = ()=>{
        let w = img.width, h = img.height;
        if(w > maxWidth){ h = Math.round(h * (maxWidth/w)); w = maxWidth; }
        const canvas = document.createElement('canvas');
        canvas.width = w; canvas.height = h;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0, w, h);
        const dataUrl = canvas.toDataURL('image/jpeg', quality);
        const base64 = dataUrl.split(',')[1];
        resolve({base64, mediaType:'image/jpeg'});
      };
      img.onerror = reject;
      img.src = e.target.result;
    };
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}

/* Anthropic vision call */
async function callClaudeVision(base64, mediaType, promptText){
  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "claude-sonnet-4-6",
      max_tokens: 1000,
      messages: [{
        role: "user",
        content: [
          { type: "image", source: { type: "base64", media_type: mediaType, data: base64 } },
          { type: "text", text: promptText }
        ]
      }]
    })
  });
  const data = await response.json();
  const text = (data.content || []).map(c=>c.text || '').join('\n');
  const clean = text.replace(/```json/gi,'').replace(/```/g,'').trim();
  return JSON.parse(clean);
}

/* Review + edit extracted items before saving */
function showReviewModal(type, items){
  const cfg = CAPTURE_CONFIG[type];
  const rowsHtml = items.map((it, idx)=>renderReviewRow(type, it, idx)).join('');
  openModal(`
    <h3>인식 결과 확인</h3>
    <div class="modal-sub">사진에서 ${items.length}개 항목을 찾았어요. 틀린 부분은 고치고, 필요 없는 항목은 지워주세요.</div>
    <div id="reviewRows">${rowsHtml}</div>
    <button class="add-row-btn" id="addRowBtn">+ 항목 추가</button>
    <div class="form-actions">
      <button class="btn-ghost" id="revCancel">취소</button>
      <button class="btn-primary" id="revSave">전체 저장</button>
    </div>
  `);
  document.getElementById('revCancel').addEventListener('click', closeModal);
  document.getElementById('addRowBtn').addEventListener('click', ()=>{
    const wrap = document.getElementById('reviewRows');
    const idx = wrap.children.length;
    wrap.insertAdjacentHTML('beforeend', renderReviewRow(type, {}, idx));
    bindRemoveButtons();
  });
  bindRemoveButtons();

  document.getElementById('revSave').addEventListener('click', async ()=>{
    const rows = Array.from(document.querySelectorAll('.review-row'));
    let count = 0;
    if(type === 'timetable'){
      rows.forEach(row=>{
        const day = row.querySelector('.f-day').value;
        const period = row.querySelector('.f-period').value;
        const subject = row.querySelector('.f-subject').value.trim();
        if(day && period && subject){
          state.timetable[day+'-'+period] = subject;
          count++;
        }
      });
      await saveKey('timetable', state.timetable);
      buildTimetableGrid(); renderTodayCard();
    } else if(type === 'exam'){
      rows.forEach(row=>{
        const subject = row.querySelector('.f-subject').value.trim();
        if(!subject) return;
        state.exams.push({
          id: uid(),
          subject,
          date: row.querySelector('.f-date').value,
          range: row.querySelector('.f-range').value.trim()
        });
        count++;
      });
      await saveKey('exams', state.exams);
      renderExams();
    } else if(type === 'assignment'){
      rows.forEach(row=>{
        const subject = row.querySelector('.f-subject').value.trim();
        if(!subject) return;
        state.assignments.push({
          id: uid(),
          subject,
          date: row.querySelector('.f-date').value,
          content: row.querySelector('.f-content').value.trim()
        });
        count++;
      });
      await saveKey('assignments', state.assignments);
      renderAssignments();
    } else if(type === 'todo'){
      rows.forEach(row=>{
        const text = row.querySelector('.f-text').value.trim();
        if(!text) return;
        state.todos.unshift({
          id: uid(),
          text,
          date: row.querySelector('.f-date').value || '',
          done:false
        });
        count++;
      });
      await saveKey('todos', state.todos);
      renderTodos(); renderTodayCard();
    }
    closeModal();
    showToast(`${count}개 항목을 저장했어요`);
  });
}

function bindRemoveButtons(){
  document.querySelectorAll('.row-remove').forEach(b=>{
    b.onclick = ()=> b.closest('.review-row').remove();
  });
}

function renderReviewRow(type, it, idx){
  if(type === 'timetable'){
    const dayOpts = DAYS.map(d=>`<option value="${d}" ${it.day===d?'selected':''}>${d}</option>`).join('');
    const periodOpts = PERIODS.map(p=>`<option value="${p}" ${Number(it.period)===p?'selected':''}>${p}교시</option>`).join('');
    return `<div class="review-row">
      <button class="row-remove">✕</button>
      <div class="form-row">
        <div class="field"><label>요일</label><select class="f-day">${dayOpts}</select></div>
        <div class="field"><label>교시</label><select class="f-period">${periodOpts}</select></div>
      </div>
      <div class="field"><label>과목명</label><input type="text" class="f-subject" value="${escapeHtml(it.subject||'')}" maxlength="12"></div>
    </div>`;
  }
  if(type === 'exam'){
    return `<div class="review-row">
      <button class="row-remove">✕</button>
      <div class="form-row">
        <div class="field"><label>과목</label><input type="text" class="f-subject" value="${escapeHtml(it.subject||'')}"></div>
        <div class="field"><label>날짜</label><input type="date" class="f-date" value="${it.date||''}"></div>
      </div>
      <div class="field"><label>시험 범위</label><textarea class="f-range">${escapeHtml(it.range||'')}</textarea></div>
    </div>`;
  }
  if(type === 'assignment'){
    return `<div class="review-row">
      <button class="row-remove">✕</button>
      <div class="form-row">
        <div class="field"><label>과목</label><input type="text" class="f-subject" value="${escapeHtml(it.subject||'')}"></div>
        <div class="field"><label>마감 날짜</label><input type="date" class="f-date" value="${it.date||''}"></div>
      </div>
      <div class="field"><label>내용</label><textarea class="f-content">${escapeHtml(it.content||'')}</textarea></div>
    </div>`;
  }
  // todo
  return `<div class="review-row">
    <button class="row-remove">✕</button>
    <div class="field"><label>할 일</label><input type="text" class="f-text" value="${escapeHtml(it.text||'')}" maxlength="60"></div>
    <div class="field"><label>날짜 (선택)</label><input type="date" class="f-date" value="${it.date||''}"></div>
  </div>`;
}

/* ================= reset ================= */
document.getElementById('resetAllBtn').addEventListener('click', async ()=>{
  if(!confirm('시간표, 시험, 수행평가, 할 일이 모두 삭제돼요. 계속할까요?')) return;
  state = { timetable:{}, exams:[], assignments:[], todos:[] };
  await Promise.all([
    saveKey('timetable', state.timetable),
    saveKey('exams', state.exams),
    saveKey('assignments', state.assignments),
    saveKey('todos', state.todos),
  ]);
  buildTimetableGrid(); renderExams(); renderAssignments(); renderTodos(); renderTodayCard();
  showToast('모두 초기화했어요');
});

/* ================= init ================= */
async function init(){
  renderHeaderDate();
  const [tt, ex, asg, td] = await Promise.all([
    loadKey('timetable', {}),
    loadKey('exams', []),
    loadKey('assignments', []),
    loadKey('todos', []),
  ]);
  state.timetable = tt || {};
  state.exams = ex || [];
  state.assignments = asg || [];
  state.todos = td || [];

  buildTimetableGrid();
  renderExams();
  renderAssignments();
  renderTodos();
  renderTodayCard();
}
init();
</script>
</body>
</html>
