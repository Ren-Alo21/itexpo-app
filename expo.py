import streamlit as st

# إعداد الصفحة وتغيير اللون الأساسي ليكون قريباً من تصميمك
st.set_page_config(page_config_title="الجسر المهني - تجربة الطالب", layout="wide")

# إضافة لمسة جمالية بالألوان (CSS) لتشبه الصور التي أرسلتها
st.markdown("""
    <style>
    .main {
        background-color: #f8fbfb;
    }
    .stButton>button {
        background-color: #20b2aa;
        color: white;
        border-radius: 10px;
        width: 100%;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #20b2aa;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .skill-tag {
        background-color: #e0f2f1;
        color: #00796b;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# الهيدر (العنوان العلوي)
st.title("🎓 مسارك الوظيفي في تخصصك")
st.write("هذه هي المهارات والمسارات المناسبة بناءً على تخصصك")

# القائمة الجانبية بشكل مبسط
st.sidebar.header("لوحة التحكم")
major = st.sidebar.selectbox("حدد تخصصك:", ["نظم معلومات", "هندسة حاسب", "ذكاء اصطناعي"])

# قسم "ابدأ رحلتك" (زي المربع الأخضر في تصميمك)
st.info("💡 ابدأ رحلتك المهنية اليوم! اختبر مهاراتك واحصل على خارطة طريق مخصصة.")

# توزيع العناصر في أعمدة (زي البطاقات في صورك)
st.markdown("### | المسارات المطلوبة")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📍 مطور واجهات (Frontend)</h3>
        <p>تصميم وبناء واجهات المستخدم التفاعلية باستخدام أحدث التقنيات.</p>
        <span class="skill-tag">HTML/CSS</span> <span class="skill-tag">React</span> <span class="skill-tag">UI Design</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📍 محلل بيانات (Data Analyst)</h3>
        <p>تحليل وتفسير البيانات المعقدة لمساعدة الشركات في اتخاذ القرارات.</p>
        <span class="skill-tag">Python</span> <span class="skill-tag">SQL</span> <span class="skill-tag">Power BI</span>
    </div>
    """, unsafe_allow_html=True)

# قسم المهارات والتدريبات (الجدول الملون)
st.divider()
st.markdown("### | تدريبات مقترحة لك")

tab1, tab2 = st.tabs(["التدريبات التقنية", "المهارات الناعمة"])

with tab1:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.success("**تطوير تطبيقات الويب**")
        st.caption("مستوى: متوسط")
    with c2:
        st.success("**أساسيات الأمن السيبراني**")
        st.caption("مستوى: مبتدئ")
    with c3:
        st.success("**هياكل البيانات**")
        st.caption("مستوى: متقدم")

with tab2:
    st.write("• حل المشكلات واتخاذ القرار")
    st.write("• العمل الجماعي والقيادة")

# زر إنهاء التجربة في الأسفل
if st.button("استكشاف المزيد من التفاصيل"):
    st.balloons()
    st.write("جاري تجهيز خارطة طريق كاملة لك...")
