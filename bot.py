import os
import random
from gtts import gTTS
from moviepy import AudioFileClip, ColorClip
import requests

def run_tiktok_automation():
    print("--- 1. اختيار أحدث فكرة ترند تيك توك ---")
    trends = [
        "أسرار لم تخبرك بها الشركات الكبرى عن الهواتف الذكية وكيف تخدعك لتشتري الأحدث سنوياً!",
        "ثلاث عادات يومية بسيطة تدمر تركيزك وعقلك دون أن تلحظ ذلك.. احذر منها فوراً!",
        "كيف تحول هاتفك الذكي إلى ماكينة إنتاج أرباح حقيقية وأنت تتابع منزلك في 2026؟",
        "القصة الحقيقية وراء اختراع الذكاء الاصطناعي وكيف سيغير شكل العالم الأبدية في الأعوام القادمة!"
    ]
    script_text = random.choice(trends)
    print(f"--- النص المختار: {script_text} ---")
    
    print("--- 2. جاري تحويل النص إلى تعليق صوتي احترافي ---")
    tts = gTTS(text=script_text, lang='ar', slow=False)
    audio_path = "voiceover.mp3"
    tts.save(audio_path)
    
    print("--- 3. جاري تصميم وإنتاج الفيديو بصرياً ---")
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    
    # خلفية ملونة جذابة بمقاسات تيك توك (1080x1920)
    bg_clip = ColorClip(size=(1080, 1920), color=(15, 23, 42), duration=duration)
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
    
    # إرسال الفيديو الطويل والجاهز
    video_url = f"https://api.telegram.org/bot{bot_token}/sendVideo"
    with open(output_video, "rb") as vid_file:
        requests.post(video_url, data={"chat_id": chat_id}, files={"video": vid_file})
        
    print("--- تمت العملية بنجاح تام وتم الإرسال إلى تيليجرام! ---")

if __name__ == "__main__":
    run_tiktok_automation()
