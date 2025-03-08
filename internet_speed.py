from tkinter import * 
import speedtest 

def speedcheck():
    sp=speedtest.Speedtest()
    #sp.get_servers()
    sp.get_best_server()
    down=str(round(sp.download()/(10**6),3))+"Mbps"
    up=str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp=Tk()
sp.title("Speed test")
sp.geometry("500x600")
sp.config(bg="brown")
lab=Label(text="Internet Speed Test ", font="Arial 25 bold",bg="brown")
lab.place(x=50,y=20,height=30,width=380)
lab=Label(text="Downloading Speed", font="Arial 20 bold",bg="brown")
lab.place(x=50,y=100,height=30,width=380)

lab_down=Label(text="00", font="Arial 20 bold",bg="brown")
lab_down.place(x=50,y=150,height=30,width=380)

lab=Label(text="Uploading Speed  ", font="Arial 20 bold",bg="brown")
lab.place(x=50,y=200,height=30,width=380)

lab_up=Label(text="00", font="Arial 20 bold",bg="brown")
lab_up.place(x=50,y=250,height=30,width=380)

btn =Button (sp,text="Check Speed Test", font="Arial 20 bold",bg="brown",relief=RAISED,command=speedcheck)
btn.place(x=50,y=300,height=35,width=380)

sp.mainloop()
