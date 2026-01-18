'''
Người nói
   ↓
Micro thu âm
   ↓
Google nhận dạng
   ↓
So sánh câu nói
   ↓
Tạo câu trả lời
   ↓
pyttsx3 đọc ra
'''

import speech_recognition  #nhận diện giọng nói → văn bản
import pyttsx3             #chuyển văn bản → giọng nói
from datetime import date,datetime

pc_nghe = speech_recognition.Recognizer()      #Tạo bộ nhận dạng giọng nói
pc_noi = pyttsx3.init()                        #Khởi tạo công cụ phát âm thanh 
pc_hieu = ''

while True:
    with speech_recognition.Microphone() as mic:        # Mở micro máy tính 
        print('Robot: i am listening')
        print('Pc: ...')
        audio = pc_nghe.listen(mic)                     # nghe thông qua mic ghi âm lại và được lưu vào biến audio
            # sử dụng với with khi kết thúc with sẽ tự động đóng lại
    try:
        you = pc_nghe.recognize_google(audio)           # nhận dạng giọng nói từ audio thông qua gg và gửi ra văn bản
    except Exception:                                   # Nếu lỗi sẽ thực hiện except
        you = ''
    print('You: ' + you)



    if you == '':
        pc = "i can't hear you, try again"
    elif you == 'hello':
            pc = 'hello good morning'
    elif you == 'today' or 'today' in you:
        today = date.today()
        pc = today.strftime("%B %d, %Y")
    elif you == 'time now':
        time = datetime.now()
        pc = time.strftime("%H hours %M minute %S second")
    elif 'bye' in you:
        pc = 'bye'
        print(pc)
        pc_noi.say(pc)
        pc_noi.runAndWait()
        break
    else:
        pc = 'i am fine thank you and you'

    print(pc)
    pc_noi.say(pc)    # đưa nội dung cho máy nói
    pc_noi.runAndWait()   # Thực sự nói

