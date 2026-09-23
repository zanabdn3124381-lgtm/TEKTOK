import os
import random
import requests
from gtts import gTTS
from moviepy import AudioFileClip, VideoFileClip, concatenate_videoclips

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
    
    print("--- 3. جلب فيديوهات خلفية سينمائية طويلة وعالية الجودة ---")
    # روابط فيديوهات سينمائية واحترافية عالية الجودة بدون حقوق
    cinematic_videos = [
        "https://assets.mixkit.co/videos/preview/mixkit-aerial-view-of-city-traffic-at-night-4152-large.mp4",
        "https://assets.mixkit.co/videos/preview/mixkit-hands-typing-on-a-laptop-keyboard-close-up-42861-large.mp4",
        "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-and-lights-31919-large.mp4"
    ]
    
    audio_clip = AudioFileClip(audio_path)
    target_duration = audio_clip.duration
    
    # تحميل الفيديو وتكراره أو مطابقته ليكون طويلاً وبصرياً مذهلاً
    temp_video_path = "background_video.mp4"
    selected_url = random.choice(cinematic_videos)
    r = requests.get(selected_url, stream=True)
    with open(temp_video_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                
    video_clip = VideoFileClip(temp_video_path)
    
    # جعل الفيديو يتمدد ويطابق مدة الصوت تماماً لضمان عدم قطع الصوت أو الصورة
    clips_list = []
    current_length = 0
    while current_length < target_duration:
        clips_list.append(video_clip)
        current_length += video_clip.duration
        
    final_combined_video = concatenate_videoclips(clips_list)
    final_video = final_combined_video.subclipped(0, target_duration).set_audio(audio_clip)
    
    output_video = "tiktok_video.mp4"
    final_video.write_videofile(output_video, fps=24, codec='libx264', audio_codec='aac', logger=None)
    print(f"--- تم إنتاج الفيديو السينمائي الطويل بنجاح (المدة: {target_duration} ثانية) ---")
    
    print("--- 4. إرسال الفيديو والوصف المربح إلى قناتك على تيليجرام ---")
    bot_token = "8341287362:AAF0hO6PMtcP5O2Y-sF34OffcN_zeLbIKNo"
    chat_id = "-1003151787212"
    
    # إرسال النص مع هاشتاقات الترند لزيادة الأرباح
    full_message = f"💰 فيديو ترند احترافي لجلب المشاهدات والأرباح:\n\n{script_text}\n\n#تيك_توك #أرباح #ترند_2026 #فيديوهات_مربحة"
    text_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(text_url, data={"chat_id": chat_id, "text": full_message})
    
    # إرسال الفيديو
    vid_url = f"https://api.telegram.org/bot{bot_token}/sendVideo"
    with open(output_video, "rb") as vid_file:
        requests.post(vid_url, data={"chat_id": chat_id}, files={"video": vid_file})
        
    print("--- تم الإرسال بنجاح تام إلى قناتك! ---")

if __name__ == "__main__":
    run_tiktok_automation()
