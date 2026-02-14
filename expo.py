import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="منصة الجسر المهني", layout="wide")

# حقن CSS لتصميم يشبه الصور (ألوان ونوع الخط)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .main { background-color: #f9fdfd; }
    .stButton>button { background-color: #00c2cb; color: white; border-radius: 10px; width: 100%; height: 50px; font-size: 18px; border: none; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 20px; border-top: 5px solid #00c2cb; }
    .step-box { background: #e0f7f7; padding: 15px; border-radius: 10px; text-align: center; border: 1px dashed #00c2cb; }
    </style>
    """, unsafe_allow_html=True)

# إدارة الصفحات باستخدام Session State
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- الصفحة الأولى: الصفحة الرئيسية ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: #1a365d;'>نحوّل التخصص الجامعي إلى مسار وظيفي يقودك لسوق العمل بثقة</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>منصة ذكية تربط بين الطلاب، الخريجين، والشركات.. وتغلق فجوة المهارات</p>", unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        if st.button("ابدأ الآن"):
            st.session_state.page = 'input'
            st.rerun()
    with col_btn2:
        st.button("تعرّف على الفكرة")

    st.divider()
    st.markdown("<h2 style='text-align: center;'>كيف نساعدك؟</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c3: st.markdown("<div class='step-box'><h3>1</h3><p>اختر هويتك</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='step-box'><h3>2</h3><p>أدخل بياناتك</p></div>", unsafe_allow_html=True)
    with c1: st.markdown("<div class='step-box'><h3>3</h3><p>احصل على مسارك</p></div>", unsafe_allow_html=True)

# --- الصفحة الثانية: إدخال البيانات ---
elif st.session_state.page == 'input':
    st.markdown("<h2 style='text-align: center;'>لنبدأ بناء مسارك الوظيفي</h2>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        uni = st.selectbox("🎓 الجامعة", ["جامعة الملك عبدالعزيز", "جامعة الملك سعود", "جامعة طيبة"])
        major = st.selectbox("📚 التخصص الجامعي", ["علوم حاسب", "نظم معلومات", "هندسة برمجيات"])
        year = st.select_slider("📅 السنة الدراسية", options=["سنة تحضيرية", "سنة 2", "سنة 3", "سنة 4", "خريج"])
        interests = st.multiselect("💡 الاهتمامات المهنية", ["تحليل البيانات", "الأمن السيبراني", "البرمجة", "التصميم"])
        
        if st.button("عرض المسار الوظيفي ✨"):
            st.session_state.page = 'results'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- الصفحة الثالثة: صفحة النتائج ---
elif st.session_state.page == 'results':
    st.markdown("<h1 style='text-align: center;'>مسارك الوظيفي في تخصصك 🚀</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'><h3>📍 مطور واجهات</h3><p>نسبة الملاءمة: 85%</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'><h3>📍 محلل بيانات</h3><p>نسبة الملاءمة: 92%</p></div>", unsafe_allow_html=True)

    st.subheader("📊 المهارات المطلوبة")
    st.info("✅ مهارات تمتلكها: Python, تحليل البيانات")
    st.warning("⚠️ مهارات تحتاجها: SQL المتقدم، تعلم الآلة")
    
    if st.button("العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()
