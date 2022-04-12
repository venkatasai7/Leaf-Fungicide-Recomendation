from tkinter import *

root = Tk()
w= root.winfo_screenwidth() 
h= root.winfo_screenheight() 

root.geometry("%dx%d" % (w, h))
root.minsize(w, h)



root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 3)
root.grid_columnconfigure(0, weight = 1)

left_frame = Frame(root, bg = "red")
left_frame.grid(row = 0, column = 0, sticky = "nesw")
right_frame = Frame(root, bg = "green")
right_frame.grid(row = 1, column = 0, sticky = "nesw")


can3 = Canvas(left_frame,bg = 'white',highlightthickness=0)
can3.place(relx=0.5, rely=0.5, anchor=CENTER)

l1=Button(can3,text="No Input Image")
l1.grid(row=0,column=0)

root.mainloop()