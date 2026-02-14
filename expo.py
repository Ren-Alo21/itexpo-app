import streamlit as st

# تصحيح السطر الرابع (كان فيه كلمة زائدة)
st.set_page_config(page_title="الجسر المهني - تجربة الطالب", layout="wide")

# إضافة التنسيقات (CSS) لتطابق صور الستوري بورد
st.markdown("""
    <style>
    .main { background-color: #f0fdfa; }
    .stApp { background-image: linear-gradient(to bottom, #f0fdfa, #ffffff); }
    
    /* تنسيق البطاقات (Cards) */
    .feature-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-top: 5px solid #00c2cb;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: right;
        margin-bottom: 20px;
    }
    
    .skill-bar {
        background-color: #00c2cb;
        color: white;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
    }
    
    h1, h2, h3 { color: #1a365d; font-family: 'Cairo', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# الصفحة الرئيسية - الهيدر
st.markdown("<h1 style='text-align: center;'>مسارك الوظيفي في تخصصك 🚀</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>هذه هي الوظائف والمهارات والتدريبات المناسبة لك بناءً على بياناتك</p>", unsafe_allow_html=True)

# قسم الوظائف المناسبة (زي الصور اللي فيها نسب مئوية)
st.subheader("📍 الوظائف المناسبة لك")
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="feature-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="skill-bar">85%</span>
            <h3>مطور واجهات</h3>
        </div>
        <p>تصميم وبناء واجهات المستخدم التفاعلية باستخدام أحدث التقنيات</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="skill-bar">92%</span>
            <h3>محلل بيانات</h3>
        </div>
        <p>تحليل وتفسير البيانات المعقدة لمساعدة الشركات في اتخاذ القرارات</p>
    </div>
    """, unsafe_allow_html=True)

# قسم المهارات المطلوبة (المربعات البيضاء)
st.divider()
st.subheader("📊 المهارات المطلوبة")
col_a, col_b = st.columns(2)

with col_a:
    st.info("**مهارات تمتلكها ✅**")
    st.write("• تحليل البيانات")
    st.write("• لغة Python")
    st.write("• العمل الجماعي")

with col_b:
    st.warning("**مهارات تحتاج تطوير ⚠️**")
    st.write("• Machine Learning")
    st.write("• SQL المتقدم")
    st.write("• إدارة المشاريع")

# البانر السفلي (المربع التركوازي)
st.markdown("""
    <div style="background-color: #00c2cb; padding: 40px; border-radius: 20px; text-align: center; color: white;">
        <h2>ابدأ رحلتك المهنية اليوم</h2>
        <p>اختر مسارك واطلع على التدريبات والفرص المتاحة</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("استكشف المزيد"):
    st.balloons()
