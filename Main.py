from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import json
from datetime import date,datetime
import cv2
import ModelFunctions as MF


if os.path.exists("input.jpg"):
  os.remove("input.jpg")

today = date.today()

root = Tk()

def open_img():
	x = openfilename()
	img = Image.open(x)
	img = img.resize((250, 250), Image.ANTIALIAS)
	img.save("input.jpg")
	for widgets in can2.winfo_children():
		widgets.destroy()
	img = ImageTk.PhotoImage(img)
	for widgets in can3.winfo_children():
		widgets.destroy()
	panel = Label(can2, image = img)
	panel.image = img
	panel.grid(row=1,column=0,padx=5,pady=5)

	l = Label(left_frame_center_left, text="Input Image",bg="white")
	l.grid(row=1,column=0)
	l = Label(left_frame_center_right, text="Input Image Details",bg="white")
	l.grid(row=1,column=0)
	image = Image.open("input.jpg")
	info_dict = {
    "Image Size": image.size,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Frames in Image": getattr(image, "n_frames", 1),
	"Date":str(today),
	"Time":str(datetime.now().time())

	}
	count=1
	for label,value in info_dict.items():
		t=f"{label:25}: {value}"
		p = Message(can3,text=t,width=300,bg="white", fg="#000",justify=LEFT)
		p.grid(row=count,column=1)
		count+=1


def openfilename():
	filename = filedialog.askopenfilename(title ='pen')
	return filename


def predict_btn():
	if os.path.exists("input.jpg"):
		for widgets in right_can.winfo_children():
			widgets.destroy()		
		predicted_class,confidence=MF.predict()
		print(predicted_class,confidence)
		Name=Label(right_can,text=" "+str(predicted_class),font= ('Helvetica 13 '))
		Name.grid(row=3,column=0)
		
		Name=Label(right_can,text=" Predicted Disease:"+str(predicted_class),font= ('Helvetica 13 '))
		Name.grid(row=3,column=0)

		Confidence=Label(right_can,text=" Confidence:"+str(confidence),font= ('Helvetica 13'))
		Confidence.grid(row=4,column=0)
		
		path="CAUSE AND CURE.json"
		for widgets in right_frame_bottom.winfo_children():
			widgets.destroy()
		f=open(path)
		data=json.load(f)
		f.close()
		frame1=LabelFrame(right_frame_bottom  ,text=predicted_class,font= ('Helvetica 16'),)
		frame1.grid(row=0,column=0,padx=15,pady=15)
		About=Label(frame1,text="About",font= ('Helvetica 14 underline'))
		About.grid(row=1,column=0)

		l = Message(frame1,
		text= data[predicted_class]["About"],
		font= ('Helvetica 13'),
		width=610)
		l.grid(row=2,column=0,padx=10)

		Cause=Label(frame1,text="Cause",font= ('Helvetica 14 underline'))
		Cause.grid(row=3,column=0)
		
		l2 = Message(frame1,
		text= data[predicted_class]["Cause"],
		font= ('Helvetica 13'),
		width=610)
		l2.grid(row=4,column=0,padx=10)

		Cure=Label(frame1,text="Cure",font= ('Helvetica 14 underline'))
		Cure.grid(row=5,column=0)
		
		l3 = Message(frame1,
		text= data[predicted_class]["Cure"],
		font= ('Helvetica 13'),
		width=610)
		l3.grid(row=6,column=0,padx=10)
	else:
		l4 = Label(right_can,
		text= "*UPLOAD A IMAGE*",
		font= ('Helvetica 12 underline'),
		fg="red")
		l4.grid(row=0,column=0)


def open_cam():
	cam = cv2.VideoCapture(0)
	cv2.namedWindow("PRESS SPACE TO SAVE IMAGE")
	while True:
		ret, frame = cam.read()
		if not ret:
			print("failed to grab frame")
			break
		cv2.imshow("PRESS SPACE TO SAVE IMAGE", frame)
		k = cv2.waitKey(1)
		if k%256 == 27:
			print("Escape hit, closing...")
			cv2.destroyAllWindows()
			break
		elif k%256 == 32:
			img_name = "input.JPG"
			cv2.imwrite(img_name, frame)
			print("Saved")
			cv2.destroyAllWindows()
			break   
	img=Image.open("input.jpg")
	img = img.resize((250, 250), Image.ANTIALIAS)
	img.save("input.jpg")
	for widgets in can2.winfo_children():
		widgets.destroy()
	img = ImageTk.PhotoImage(img)
	for widgets in can3.winfo_children():
		widgets.destroy()
	panel = Label(can2, image = img)
	panel.image = img
	panel.grid(row=1,column=0,padx=5,pady=5)

	l = Label(left_frame_center_left, text="Input Image",bg="white")
	l.grid(row=1,column=0)
	l = Label(left_frame_center_right, text="Input Image Details",bg="white")
	l.grid(row=1,column=0)
	image = Image.open("input.jpg")
	info_dict = {
    "Image Size": image.size,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Frames in Image": getattr(image, "n_frames", 1),
	"Date":str(today),
	"Time":str(datetime.now().time())

	}
	count=1
	for label,value in info_dict.items():
		t=f"{label:25}: {value}"
		p = Message(can3,text=t,width=300,bg="white", fg="#000",justify=LEFT)
		p.grid(row=count,column=1)
		count+=1

root.title("Leaf Funcigide Recommendation")

w= root.winfo_screenwidth() 
h= root.winfo_screenheight() 

root.geometry("%dx%d" % (w, h))
root.minsize(w, h)
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 1)

left_frame = Frame(root)
left_frame.grid(row = 0, column = 0, sticky = "nesw")
right_frame = Frame(root)
right_frame.grid(row = 0, column = 1, sticky = "nesw")


left_frame.grid_rowconfigure(0, weight = 1)
left_frame.grid_rowconfigure(1, weight = 2)
left_frame.grid_columnconfigure(0, weight = 1)


left_frame_top = Frame(left_frame)
left_frame_top.grid(row = 0, column = 0, sticky = "nesw")
left_frame_top.grid_propagate(False)
left_frame_center = Frame(left_frame)
left_frame_center.grid(row = 1, column = 0, sticky = "nesw")
left_frame_center.grid_propagate(False)

left_frame_center.grid_columnconfigure(0, weight = 1)
left_frame_center.grid_columnconfigure(1, weight = 1)
left_frame_center.grid_rowconfigure(0, weight = 1)

left_frame_center_left = Frame(left_frame_center, bg = "white", highlightthickness=2)
left_frame_center_left.grid(row = 0, column = 0, sticky = "nesw")
left_frame_center_left.grid_propagate(False)
left_frame_center_right = Frame(left_frame_center, bg="white", highlightthickness=2)
left_frame_center_right.grid(row = 0, column = 1, sticky = "nesw")
left_frame_center_right.grid_propagate(False)

can = Canvas(left_frame_top)
can.place(relx=0.5, rely=0.5, anchor=CENTER)

frame1=LabelFrame(can,text="About",font= ('Helvetica 14'),)
frame1.grid(row=0,column=0)

About= Message(frame1,
text= "\n This is a app can load images from your device and can predict its disease in Minimal Possible time,Either Click the below 'Browse Files' button  and select the required Image  or use 'Capture' to take images from camera then click on 'Predict' button to find About ,Cause,Cure of Disease \n",
width=600,
font= ('Helvetica 13'),
justify=CENTER)

About.grid(row=0,column=0,padx=10)

btn1 = Button(can, text ='Browse Files', command = open_img,height=1,width=10).grid(row=1,column=0,pady=10)

btn2=Button(can, text ='Capture ',command =open_cam ,height=1,width=10).grid(row=3,column=0,pady=10)

can2 = Canvas(left_frame_center_left,bg = 'white',highlightthickness=0)
can2.place(relx=0.5, rely=0.5, anchor=CENTER  )

l1=Label(can2,text="No Input Image")
l1.grid(row=0,column=0)


can3 = Canvas(left_frame_center_right,bg = 'white',highlightthickness=0)
can3.place(relx=0.5, rely=0.5, anchor=CENTER)

l2=Label(can3,text="No Input Image")
l2.grid(row=0,column=0)



right_frame.grid_rowconfigure(0, weight = 1)
right_frame.grid_rowconfigure(1, weight = 1)
right_frame.grid_rowconfigure(2, weight = 5)
right_frame.grid_columnconfigure(0, weight = 1)

right_frame.grid_propagate(False)
right_frame_top = Frame(right_frame)
right_frame_top.grid(row = 0, column = 0, sticky = "nesw")
right_frame_top.grid_propagate(False)
right_frame_center = Frame(right_frame)
right_frame_center.grid(row = 1, column = 0, sticky = "nesw")
right_frame_center.grid_propagate(False)
right_frame_bottom = Frame(right_frame)
right_frame_bottom.grid(row = 2, column = 0, sticky = "nesw")
right_frame_bottom.grid_propagate(False)


frame1=LabelFrame(right_frame_bottom,text="Disease Name" ,font= ('Helvetica 14'))
frame1.grid(row=0,column=0,padx=10,pady=10)

About=Label(frame1,text="About",font= ('Helvetica 13 underline'))
About.grid(row=0,column=0)


l = Message(frame1,
text= " "*200,
width=610,
)
l.grid(row=1,column=0,padx=10)

Cause=Label(frame1,text="Cause",font= ('Helvetica 13 underline'))
Cause.grid(row=2,column=0)
	
l2 = Message(frame1,
text="\n"*2,
width=610)
l2.grid(row=3,column=0,padx=10)

Cure=Label(frame1,text="Cure",font= ('Helvetica 13 underline'))
Cure.grid(row=4,column=0)
	
l3 = Message(frame1,
text= "\n"*3,
width=610)
l3.grid(row=5,column=0,padx=10)

canv = Canvas(right_frame_top)
canv.place(relx=0.5, rely=0.5, anchor=CENTER)
right_can= Canvas(right_frame_center)
right_can.place(relx=0.5, rely=0.5, anchor=CENTER)

btn3=Button(canv, text ='predict',command = predict_btn,height=3,width=10).grid(row=1,column=0)


root.mainloop()

if os.path.exists("input.jpg"):
  os.remove("input.jpg")


