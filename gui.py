import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy
#load the trained model to classify sign
from keras.models import load_model
model = load_model('traffic_classifier.h5')

#dictionary to label all traffic signs class.
# classes = { 1:'Speed limit (20km/h)',
#             2:'Speed limit (30km/h)', 
#             3:'Speed limit (50km/h)', 
#             4:'Speed limit (60km/h)', 
#             5:'Speed limit (70km/h)', 
#             6:'Speed limit (80km/h)', 
#             7:'End of speed limit (80km/h)', 
#             8:'Speed limit (100km/h)', 
#             9:'Speed limit (120km/h)', 
#             10:'No passing', 
#             11:'No passing veh over 3.5 tons', 
#             12:'Right-of-way at intersection', 
#             13:'Priority road', 
#             14:'Yield', 
#             15:'Stop', 
#             16:'No vehicles', 
#             17:'Veh > 3.5 tons prohibited', 
#             18:'No entry', 
#             19:'General caution', 
#             20:'Dangerous curve left', 
#             21:'Dangerous curve right', 
#             22:'Double curve', 
#             23:'Bumpy road', 
#             24:'Slippery road', 
#             25:'Road narrows on the right', 
#             26:'Road work', 
#             27:'Traffic signals', 
#             28:'Pedestrians', 
#             29:'Children crossing', 
#             30:'Bicycles crossing', 
#             31:'Beware of ice/snow',
#             32:'Wild animals crossing', 
#             33:'End speed + passing limits', 
#             34:'Turn right ahead', 
#             35:'Turn left ahead', 
#             36:'Ahead only', 
#             37:'Go straight or right', 
#             38:'Go straight or left', 
#             39:'Keep right', 
#             40:'Keep left', 
#             41:'Roundabout mandatory', 
#             42:'End of no passing', 
#             43:'End no passing veh > 3.5 tons' }

# Dictionary với các biển báo bằng tiếng Việt
classes = {
    1: 'Giới hạn tốc độ (20km/h)',
    2: 'Giới hạn tốc độ (30km/h)',
    3: 'Giới hạn tốc độ (50km/h)',
    4: 'Giới hạn tốc độ (60km/h)',
    5: 'Giới hạn tốc độ (70km/h)',
    6: 'Giới hạn tốc độ (80km/h)',
    7: 'Hết giới hạn tốc độ (80km/h)',
    8: 'Giới hạn tốc độ (100km/h)',
    9: 'Giới hạn tốc độ (120km/h)',
    10: 'Cấm vượt',
    11: 'Cấm vượt xe trên 3.5 tấn',
    12: 'Nhường đường tại giao lộ',
    13: 'Đường ưu tiên',
    14: 'Nhường đường',
    15: 'Dừng lại',
    16: 'Cấm xe cộ',
    17: 'Cấm xe > 3.5 tấn',
    18: 'Cấm vào',
    19: 'Cảnh báo chung',
    20: 'Đoạn đường cong trái nguy hiểm',
    21: 'Đoạn đường cong phải nguy hiểm',
    22: 'Đoạn đường cong đôi',
    23: 'Đường gồ ghề',
    24: 'Đường trơn trượt',
    25: 'Đoạn đường thu hẹp bên phải',
    26: 'Công trình đường bộ',
    27: 'Đèn giao thông',
    28: 'Người đi bộ',
    29: 'Trẻ em qua đường',
    30: 'Xe đạp qua đường',
    31: 'Cảnh báo băng tuyết',
    32: 'Động vật hoang dã qua đường',
    33: 'Hết giới hạn tốc độ và vượt',
    34: 'Quẹo phải phía trước',
    35: 'Quẹo trái phía trước',
    36: 'Chỉ đi thẳng',
    37: 'Đi thẳng hoặc rẽ phải',
    38: 'Đi thẳng hoặc rẽ trái',
    39: 'Đi bên phải',
    40: 'Đi bên trái',
    41: 'Vòng xuyến bắt buộc',
    42: 'Hết cấm vượt',
    43: 'Hết cấm vượt xe trên 3.5 tấn',
}


#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)

    # Dự đoán lớp với phương thức predict()
    pred = model.predict(image)
    
    # Lấy chỉ số của lớp có xác suất cao nhất
    class_idx = numpy.argmax(pred, axis=1)[0]
    
    # Kiểm tra xem biển báo có trong dictionary không
    if class_idx + 1 in classes:
        sign = classes[class_idx + 1]  # Thêm 1 vì lớp bắt đầu từ 1, không phải 0
    else:
        sign = "Biển báo không xác định"  # Thông báo nếu không có trong dictionary
    
    print(sign)
    
    # Hiển thị kết quả
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Lisence plate recognition",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()