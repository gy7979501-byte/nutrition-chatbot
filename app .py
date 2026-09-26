
import streamlit as st
import google.generativeai as genai

# 1. عنوان الصفحة
st.title("🥗 مساعد الصحة والتغذية الذكي")
st.write("أهلاً بك! أنا مساعدك الشخصي للأنظمة الغذائية والحياة الصحية.")

# 2. إعداد مفتاح الـ API
API_KEY = "AQ.Ab8RN6LNj5e50wiRNzuFtcPQYbL1utBKlpyAEErIS5sZlRvcCwا"
genai.configure(api_key=API_KEY)

# 3. إعداد الموديل مع التعليمات
system_prompt = "أنت مساعد ذكي متخصص في الصحة والتغذية فقط. قدّم نصائح غذائية وحساب سعرات بلطف وبساطة. إذا سئلت في مجال آخر اعتذر بلطف."
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# 4. إدارة ذاكرة الشات
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "أهلاً بك! 👋 أنا مساعدك الذكي للتغذية والصحة. كيف يمكنني مساعدتك اليوم؟"
        }
    ]

# عرض الرسائل القديمة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. استقبال وتجهيز الردود
if user_input := st.chat_input("اكتب سؤالك عن التغذية أو الأكل..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = model.generate_content(user_input)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"حدث خطأ أثناء الاتصال بالخدمة: {e}"

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
 
