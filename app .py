import streamlit as st
from google import genai

# 1. عنوان الصفحة
st.title("🥗 مساعد الصحة والتغذية الذكي")
st.write("أهلاً بك! أنا مساعدك الشخصي للأنظمة الغذائية والحياة الصحية.")

# 2. مفتاح الـ API
API_KEY = "AQ.Ab8RN6LNj5e50wiRNzuFtcPQYbL1utBKlpyAEErIS5sZlRvcCwا"
client = genai.Client(api_key=API_KEY)

# 3. إدارة ذاكرة الشات
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

# 4. استقبال وتجهيز الردود
if user_input := st.chat_input("اكتب سؤالك عن التغذية أو الأكل..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # تجهيز النص بالتعليمات بأسلوب آمن تماماً للترميز
    prompt = f"أنت مساعد متخصص في التغذية والصحة فقط. أجب بأسلوب بسيط ولطيف على السؤال التالي: {user_input}"

    with st.chat_message("assistant"):
        with st.spinner("جاري التفكير..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                bot_reply = response.text
            except Exception as e:
                bot_reply = f"حدث خطأ أثناء الاتصال بالخدمة: {e}"
            st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
 
