import streamlit as st
from google import genai
from google.genai import types

# 1. عنوان الصفحة
st.title("🥗 مساعد الصحة والتغذية الذكي")
st.write("أهلاً بك! أنا مساعدك الشخصي للأنظمة الغذائية والحياة الصحية.")

# 2. مفتاح الـ API
API_KEY =API_KEY = "AQ.Ab8RN6Io0mQ3CAxPAU2fNFmd5limUlQJCA4FsusKmrK-GjTD9Q"
client = genai.Client(api_key=API_KEY)

# 3. تعليمات النظام
system_prompt = "أنت مساعد ذكي متخصص في الصحة والتغذية فقط. قدّم نصائح غذائية وحساب سعرات بلطف وبساطة. إذا سئلت في مجال آخر اعتذر بلطف."

# 4. إدارة ذاكرة الشات
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "أهلاً بك! 👋 أنا مساعدك الذكي للتغذية والصحة. كيف يمكنني مساعدتك اليوم؟"
        }
    ]

# عرض الرسائل
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. استقبال وتجهيز الردود
if user_input := st.chat_input("اكتب سؤالك عن التغذية أو الأكل..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=user_input,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"حدث خطأ أثناء الاتصال بالخدمة: {e}"

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
