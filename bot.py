from google import genai

def generate_trend_content():
    # تم وضع مفتاحك الخاص هنا بشكل صحيح
    client = genai.Client(api_key="AQ.Ab8RN6KISq_tZw1HxBD2QMYZ3KrBN...")
    
    prompt = """
    أنت صانع محتوى تيك توك محترف. اقترح علي فكرة فيديو قصيرة جداً (ترند حالياً)، واكتب:
    1. عنوان الفيديو.
    2. النص الذي سيتم قراءته في الفيديو (أقل من 40 كلمة، مشوق ومثير للفضول).
    3. وصف الفيديو مع الهاشتاقات المناسبة.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    print("--- تم توليد محتوى الترند بنجاح ---")
    print(response.text)

if __name__ == "__main__":
    generate_trend_content()
