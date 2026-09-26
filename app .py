import streamlit as st
import requests

# 1. عنوان الصفحة
st.title("🥗 مساعد الصحة والتغذية الذكي")
st.write("أهلاً بك! أنا مساعدك الشخصي للأنظمة الغذائية والحياة الصحية.")

# 2. مفتاح الـ API
API_KEY = "AQ.Ab8RN6LNj5e50wiRNzuFtcPQYbL1utBKlpyAEErIS5sZlRvcCwا"

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

    with st.chat_message("assistant"):
        with st.spinner("جاري التفكير..."):
            try:
                # استخدام رابط الموديل المباشر والآمن تماماً للمفاتيح العادية
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
                
                headers = {"Content-Type": "application/json"}
                payload = {
                    "contents": [{
                        "parts": [{
                            "text": f"أنت مساعد متخصص في الصحة والتغذية فقط. أجب بأسلوب بسيط ولطيف باللغة العربية على السؤال التالي: {user_input}"
                        }]
                    }]
                }
                
                response = requests.post(url, headers=headers, json=payload)
                result = response.json()
                
                if "candidates" in result:
                    bot_reply = result["candidates"][0]["content"]["parts"][0]["text"]
                else:
                    error_msg = result.get('error', {}).get('message', 'خطأ غير معروف')
                    bot_reply = f"حدث خطأ في الاستجابة: {error_msg}"
                    
            except Exception as e:
                bot_reply = f"حدث خطأ أثناء الاتصال بالخدمة: {e}"

            st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
 
