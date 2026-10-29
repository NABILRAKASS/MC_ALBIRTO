import time
import requests

# 1. معلومات البوت الخاص بك
TOKEN = "9077859222:AAEl7_hqE5zqYZgD76QSfKASbGW12a4n4dU"
CHAT_ID = "7408811157"  # معرف حسابك الشخصي على تيليجرام (Chat ID)

# الرابط أو الموقع الذي تريد مراقبته (يمكنك استبداله برابط صفحة العروض أو المتجر)
TARGET_URL = "https://9to5google.com/guides/google-play/"  # رابط تجريبي كمثال فقط

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print("خطأ في إرسال الرسالة:", e)

def monitor_site():
    print("بدأت مراقبـة الموقع/الصفحة...")
    
    # سنحتفظ بالقيمة أو المحتوى القديم كمقارنة
    last_content = None
    
    while True:
        try:
            response = requests.get(TARGET_URL)
            current_content = response.text
            
            if last_content is not None and current_content != last_content:
                # إذا تغير المحتوى (يعني ظهر عرض جديد أو تغير شيئ ما)
                alert_text = "🚨 تنبيه عاجل! تم رصد تحديث أو عرض جديد في الموقع المستهدف! الحق سجل فيديو تيك توك 🎬"
                send_telegram_message(alert_text)
                print("تم إرسال إشعار العرض الجديد بنجاح!")
                
            last_content = current_content
            
        except Exception as e:
            print("خطأ في الاتصال بالموقع:", e)
            
        # الانتظار لمدة 5 دقائق (300 ثانية) قبل الفحص مجدداً لتجنب الحظر
        time.sleep(300)

if __name__ == '__main__':
    # رسالة تجريبية للتأكد أن السكريبت اشتغل
    send_telegram_message("🤖 سكريبت مراقبة العروض يعمل الآن بنجاح على هاتفك!")
    monitor_site()
  
