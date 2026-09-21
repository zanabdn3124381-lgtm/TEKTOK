import os
import google.generativeai as genai
from gtts import gTTS
from moviepy import AudioFileClip, ColorClip
import requests

def run_tiktok_automation():
    print("--- 1. جاري الاتصال بالذكاء الاصطناعي لجلب أحدث الترندات والأفكار ---")
    # مفتاحك الصحيح
    genai.configure(api_key="AQ.Ab8RN6KISq_tZw1HxBD2QMYZ3KrBN...")
    
    # استخدام نموذج جميناي لتوليد محتوى ترند طويل ومشوق
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = """
    أنت صانع محتوى تيك توك محترف جداً ويومي. اقترح علي فكرة فيديو عميقة وترند حالياً، واكتب نصاً مشوقاً وطويلاً نسبياً (حوالي 60 إلى 80 كلمة باللغة العربية) ومقسماً بشكل ممتاز ليتم قراءته كتعليق صوتي لفيديو احترافي.
    """
    
    response = model.generate_content(prompt)
    script_text = response.text
    print("--- تم توليد النص والترند بنجاح ---")
    print(script_text)
    
    print("--- 2. جاري تحويل النص الطويل إلى تعليق صوتي احترافي ---")
    tts = gTTS(text=script_text, lang='ar', slow=False)
    audio_path = "voiceover.mp3"
    tts.save(audio_path)
    
    print("--- 3. جاري تصميم وإنتاج الفيديو بصرياً (خلفية متناسقة مع الصوت) ---")
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    
    # خلفية ملونة جذابة بمقاسات تيك توك (1080x1920) وبطول الصوت تماماً
    bg_clip = ColorClip(size=(1080, 1920), color=(15, 23, 42), duration=duration) # لون كحلي داكن أنيق
    video = bg_clip.with_audio(audio_clip)
    
    output_video = "tiktok_video.mp4"
    video.write_videofile(output_video, fps=24, codec='libx264', audio_codec='aac')
    print(f"--- تم إنتاج الفيديو بنجاح ومدة الفيديو {duration} ثانية ---")
    
    print("--- 4. جاري إرسال النص والفيديو مباشرة إلى قناتك على تيليجرام ---")
    bot_token = "8341287362:AAF0hO6PMtcP5O2Y-sF34OffcN_zeLbIKNo"
    chat_id = "-1003151787212"
    
    # إرسال النص والترند
    text_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(text_url, data={"chat_id": chat_id, "text": f"🔥 فكرة ترند تيك توك جديدة:\n\n{script_text}"})
    
    # إرسال الفيديو الطويلة والجاهزة
    video_url = f"https://api.telegram.org/bot{bot_token}/sendVideo"
    with open(output_video, "rb") as vid_file:
        requests.post(video_url, data={"chat_id": chat_id}, files={"video": vid_file})
        
    print("--- تمت العملية بنجاح تام وتم الإرسال إلى تيليجرام! ---")

if __name__ == "__main__":
    run_tiktok_automation()
