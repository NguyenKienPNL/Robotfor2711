#ROBOT PROJECT

-Có 2 đội thực hiện dự án:
* Làm phần cứng
* Làm phần mềm

-Đội làm phần cứng sẽ lo việc hàn, cắt, tạo hình phía ngoài, trang trí; trong khi đội phần mềm chịu trách nhiệm thiết kế giao diện, xây dựng "bộ não" cho robot.

Sau đây là mô tả chi tiết phần xây dựng trung tâm xử lý cho robot

Để giúp cho con robot có thể nhận diện giọng nói từ người dùng, xử lý dữ liệu đồng thời xuất kết quả cũng như chương trình bổ trợ, bao gồm 5 file(hoặc hơn), được viết dưới dạng module.

FILE1: HEAR.PY
Bước đầu tiên trong quá trình xây dựng hệ thống xử lý cho robot là nhận dữ liệu vào. Mục đích của file hear.py là nhận dữ liệu vào dưới dạng giọng nói trực tiếp, sau đó chuyển về dạng text( hay string).
Trong file đã sử dụng speech_recognition. Đây là một API rất hữu ích của Google và cách sử dụng cũng rất đơn giản.
Một vài dòng code ví dụ:
```sh
import speech_recognition as sr
reg = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    reg.adjust_for_ambient_noise(source)
    inp = reg.listen(source)
    text = reg.recognize_google(inp)
```

Vậy chỉ sau nột vài dòng code(tất nhiên là đơn giản hơn nhiều so với thực tế), ta đã có biến text là một xâu dữ liệu và sẵn sàng để tới bước tiếp theo.

FILE2: LOGIC.PY
Đây chính là nơi robot sẽ đối chiếu dữ liệu vào với những dữ liệu đã được lưu để thực hiện câu lệnh. Không chỉ trả về những dòng text bình thường, người dùng có thể lệnh cho robot phát nhạc, hỏi ngày tháng, giờ hiện tại và thêm nhiều tính năng nữa
File sử dụng nhiều thư viện trong hệ thống thư viện đầy phong phú của python như: datetime, time, pygame, ...

FILE3: SPEAK.PY
Đây là file được tạo ra giúp robot xuất dữ liệu dươi dạng âm thanh thay vì in ra terminal như những chương trình bình thường. Sở dĩ làm được như vậy là nhờ pyttsx3. Đây cũng là một thư viện hay khi có thể đưa string sang giọng nói một cách trực tiếp mà không cần phải tạo file audio rồi mở file như thư viện os.
Một vài dòng code ví dụ(biến text ở đây có thể hiểu là dữ liệu đầu ra từ file logic.py)
```sh
import pyttsx3 as pt3
speaker = pt3.init()
speaker.say(text)
speaker.runAndWait()
```

FILE4: CALCMODULO.py
Đây là một file bổ trợ giúp robot có thể thực hiện các phép tính đơn giản được người dùng nói ra. Vì file này khá nặng về tính thuật toán nên mạn phép không nói ra. Nhưng nhìn chung, file calcmodulo.py chạy song song với file logic.py, nghĩa là từ chế độ bình thường, người dùng phải nói lệnh để robot chuyển sang chế độ tính toán đơn thuần.

FILE5: MAIN.py
Đây là file quan trọng nhất vì nó kết nối các file thành phần lại với nhau. Các file đó được import vào file main dưới dạng module và ghép với nhau để tạo thành khối hoàn chỉnh.
