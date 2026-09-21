import os
import time
from google import genai
from moviepy.editor import TextClip, AudioFileClip

def generate_trend_content():
    """الخطوة الأولى: توليد فكرة وسكريبت ترند عبر الذكاء الاصطناعي"""
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    prompt = """
    أنت صانع محتوى تيك توك محترف. اقترح علي فكرة فيديو قصيرة جداً (ترند حالياً)، واكتب:
    1. عنوان الفيديو.
    2. النص الذي سيتم قراءته في الفيديو (أقل من 40 كلمة، مشوق ومثير للفضول).
    3. وصف الفيديو مع الهاشتاقات المناسبة (مثل #اكسبلور #تيك_توك).
    اجعل الإجابة منظمة بوضوح.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    print("--- تم توليد محتوى الترند بنجاح ---")
    print(response.text)
    return response.text

if __name__ == "__main__":
    # تشغيل توليد المحتوى كخطوة أولى للبوت
    content = generate_trend_content()
