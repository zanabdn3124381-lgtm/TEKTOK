import os
from gtts import gTTS
from moviepy import AudioFileClip, ColorClip
import requests

def generate_and_send_tiktok():
    # نص تجريبي للتأكد من أن إنتاج الفيديو وتليجرام يعملان 100%
    script_text = "أفضل ثلاث نصائح لزيادة متابعين تيك توك في أسبوع واحد فقط! تابع الحساب للمزيد."
    print("--- تم تجهيز النص بنجاح ---")
    
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
    video = bg_clip.with_audio(audio_clip)
    
    output_video = "tiktok_video.mp4"
    video.write_videofile(output_video, fps=24, codec='libx264', audio_codec='aac')
    print(f"--- تم إنتاج الفيديو بنجاح: {output_video} ---")
    
    # 4. إرسال الفيديو والنص إلى تيليجرام
    print("--- جاري إرسال الفيديو إلى قناتك على تيليجرام ---")
    bot_token = "8341287362:AAF0hO6PMtcP5O2Y-sF34OffcN_zeLbIKNo"
    chat_id = "-1003151787212"
    
    # أولاً: إرسال النص
    text_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(text_url, data={"chat_id": chat_id, "text": f"🎬 فكرة فيديو تيك توك جديدة:\n\n{script_text}"})
    
    # ثانياً: إرسال ملف الفيديو (MP4)
    video_url = f"https://api.telegram.org/bot{bot_token}/sendVideo"
    with open(output_video, "rb") as vid_file:
        requests.post(video_url, data={"chat_id": chat_id}, files={"video": vid_file})
        
    print("--- تم الإرسال إلى تيليجرام بنجاح! ---")

if __name__ == "__main__":
    generate_and_send_tiktok()
