import os
from google import genai
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip, ColorClip, CompositeVideoClip

def generate_trend_content():
    # 1. الاتصال بـ جوجل جميناي لتوليد النص
    client = genai.Client(api_key="AQ.Ab8RN6KISq_tZw1HxBD2QMYZ3KrBN...")
    
    prompt = """
    أنت صانع محتوى تيك توك محترف. اقترح علي فكرة فيديو قصيرة جداً (ترند حالياً)، واكتب:
    1. عنوان الفيديو.
    2. النص الذي سيتم قراءته في الفيديو (أقل من 30 كلمة، مشوق ومثير للفضول باللغة العربية).
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    script_text = response.text
    print("--- تم توليد النص بنجاح ---")
    print(script_text)
    
    # 2. تحويل النص إلى صوت (Audio)
    print("--- جاري تحويل النص إلى صوت ---")
    tts = gTTS(text=script_text, lang='ar')
    audio_path = "voiceover.mp3"
    tts.save(audio_path)
    
    # 3. إنتاج الفيديو باستخدام MoviePy
    print("--- جاري دمج الصوت وتصميم الفيديو ---")
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    
    # إنشاء خلفية ملونة للفيديو (مقاسات تيك توك: 1080x1920)
    bg_clip = ColorClip(size=(1080, 1920), color=(20, 20, 30), duration=duration)
    
    # إضافة الصوت للفيديو
    video = bg_clip.set_audio(audio_clip)
    
    # حفظ الفيديو النهائي
    output_video = "tiktok_video.mp4"
    video.write_videofilerecord(output_video, fps=24) if hasattr(video, 'write_videofilerecord') else video.write_videofile(output_video, fps=24, codec='libx264', audio_codec='aac')
    
    print(تم إنتاج فيديو تيك توك بنجاح وحفظه باسم: {output_video})

if __name__ == "__main__":
    generate_trend_content()
