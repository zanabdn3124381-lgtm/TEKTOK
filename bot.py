import os
import random
from gtts import gTTS
from moviepy import AudioFileClip, ColorClip

def run_tiktok_automation():
    print("--- 1. اختيار أقوى أفكار الترند المربحة ---")
    trends = [
        "أسرار لا يمكن للشركات الكبرى إخفاءها بعد الآن حول كيفية جلب أرباح ضخمة من الإنترنت وأنت في منزلك في 2026!",
        "ثلاث قواعد ذهبية يتبعها أثرياء العالم لكي تتضاعف ثرواتهم باستمرار.. دمر عادات الفقراء وابدأ الآن!",
        "كيف تحول شغفك اليومي إلى مصدر دخل أسطوري بطريقة لم يخبرك بها أحد من قبل؟ تابع التفاصيل!"
    ]
    script_text = random.choice(trends)
    print(f"--- النص المختار: {script_text} ---")
    
    print("--- 2. تحويل النص إلى تعليق صوتي احترافي ---")
    tts = gTTS(text=script_text, lang='ar', slow=False)
    audio_path = "voiceover.mp3"
    tts.save(audio_path)
    
    print("--- 3. إنتاج الفيديو السينمائي الخلفي برمجياً لضمان الجودة ---")
    audio_clip = AudioFileClip(audio_path)
    target_duration = audio_clip.duration
    
    # إنشاء خلفية ملونة احترافية وبمقاسات تيك توك (1080x1920) تطابق مدة الصوت تماماً
    bg_clip = ColorClip(size=(1080, 1920), color=(15, 23, 42), duration=target_duration)
    final_video = bg_clip.set_audio(audio_clip)
    
    output_video = "tiktok_video.mp4"
    final_video.write_videofile(output_video, fps=24, codec='libx264', audio_codec='aac', logger=None)
    print(f"--- تم إنتاج الفيديو بنجاح تام (المدة: {target_duration} ثانية) ---")
    
    print("--- 4. إرسال الفيديو والوصف المربح إلى قناتك على تيليجرام ---")
    import requests
    bot_token = "8341287362:AAF0hO6PMtcP5O2Y-sF34OffcN_zeLbIKNo"
    chat_id = "-1003151787212"
    
    # إرسال النص مع هاشتاقات الترند والأرباح
    full_message = f"💰 فيديو ترند احترافي لجلب المشاهدات والأرباح:\n\n{script_text}\n\n#تيك_توك #أرباح #ترند_2026 #فيديوهات_مربحة"
    text_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(text_url, data={"chat_id": chat_id, "text": full_message})
    
    # إرسال الفيديو
    vid_url = f"https://api.telegram.org/bot{bot_token}/sendVideo"
    with open(output_video, "rb") as vid_file:
        requests.post(vid_url, data={"chat_id": chat_id}, files={"video": vid_file})
        
    print("--- تم الإرسال بنجاح تام إلى قناتك على تيليجرام! ---")

if __name__ == "__main__":
    run_tiktok_automation()
