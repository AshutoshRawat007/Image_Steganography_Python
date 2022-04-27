from tkinter import*
from tkinter import filedialog
import Image_LSB_steganography as steg
		                
# GUI functions code here 
def hide_msg_fromTxt_file():
        root=Tk()
        root.geometry("733x434")
        root.title("Hide Text File")

        global path, message
        path=""
        message=""
        global mc,fc
        fc=0
        mc=0
        def hidefnTXT():
                global message
                global mc         

                filenameTxt = filedialog.askopenfilename()
                txtmsg=open(filenameTxt,'r')
                message=txtmsg.read()
                disp_tf.insert(0,f'{filenameTxt}')
                print(message)
                mc=mc+1
               

        def mainwin():
                root.destroy()
                first_main_window()

        def hidefn():
                global path
                global fc
                filename = filedialog.askopenfilename()
                path = filename
                disp_imagepath.insert(0,f'{path}')
                fc=fc+1
                

        def hideit():
                if(fc>0 and mc>0):
                        
                        print((steg.hide(path,message)))
                        
                else:
                        if(fc==0):
                                disp_imagepath.insert(0,f'{"please select image to be used as cover"}')
                        elif(mc==0):
                                disp_tf.insert(0,f'{"please selct txt file to be used"}')
                
        abc=Button(root,text="Hide",bd='6',command=hideit)
        abc.pack(side=BOTTOM,fill='x',padx=50,pady=5)  

        slctTxt=Button(root,text="Text File TO Hide",bd='6',command=hidefnTXT)
        slctTxt.pack(side=BOTTOM,fill='x',padx=50,pady=5)  

        Label(text="File path :").pack()

        disp_tf = Entry(root,width=60, font=('Arial', 10)  )
        disp_tf.pack(side=TOP,pady=5,padx=10)

        Label(text="Image path :").pack()
        disp_imagepath = Entry(root,width=60, font=('Arial', 10)  )
        disp_imagepath.pack(side=TOP,pady=5,padx=10)

        selctimg=Button(root,text="Select Image to Hide",bd='6',command=hidefn)
        selctimg.pack(side=BOTTOM,fill='x',padx=50,pady=5)
    
        manwin=Button(root,text="Main window",bd='6',command=mainwin)
        manwin.pack(side=BOTTOM,fill='x',padx=50,pady=5)

        root.mainloop()

def hide_msg_window():
        root=Tk()
        root.geometry("700x500")
        root.title("Hide Data")
        
        global message,path
        message=""
        path=""
        def mainwin():
                root.destroy()
                first_main_window()
        def hidefnpath():
                global path
                filename = filedialog.askopenfilename()
                path = filename
                disp_imagepath.insert(0,f'{path}')

        def hideit():
                global message
                message=mesg.get("1.0","end-1c")
                print((steg.hide(path,message)))
                print("done ")
                
        Label(text="Image path :").pack()
        disp_imagepath = Entry(root,width=60, font=('Arial', 10)  )
        disp_imagepath.pack(side=TOP,pady=5,padx=10)

        abc=Button(root,text="Hide",bd='6',command=hideit)
        abc.pack(side=BOTTOM,fill='x',padx=50,pady=5)        

        ab=Button(root,text="Select Image to Hide",bd='6',command=hidefnpath)
        ab.pack(side=BOTTOM,fill='x')

        mesg =  Text(root, height=18,width=70, font=('Arial', 10)  )
        mesg.pack(pady=5,padx=10,fill='x',side =TOP)
    
        a=Button(root,text="clear the window",bd='6',command=root.destroy)
        a.pack(side=BOTTOM,fill='x')    
    
        x=Button(root,text="Main window",bd='6',command=mainwin)
        x.pack(side=BOTTOM,fill='x')

        root.mainloop()


def retrieve_msg_window():
    root=Tk()
    root.geometry("733x434")
    root.title("Retrieve Hidden Data")
    
    def mainwin():
            root.destroy()
            first_main_window()

    def rtrieve():
            filename = filedialog.askopenfilename()
            path=filename
            message=steg.retr(path)
            disp_tf.insert(1.0,f'{message}')
            if(filename[-4:]=='.png'):
                        new_filename=filename[:-4]+"_secret.txt"
            elif(filename[-5:]=='.jpeg'):
                        new_filename=filename[:-5]+"_secret.png"
            secretFile=open(new_filename,'w')
            secretFile.write(message)
            print(message)
        
    disp_tf = Text(root, height=20,width=70, font=('Arial', 10)  )
    disp_tf.pack(pady=5,padx=10,fill='x',side =TOP)
    
    a=Button(root,text="Main Window",bd='6',command=mainwin)
    a.pack(side='bottom',pady=10)    
    
    Button(root,text="click here to get image path",command=rtrieve).pack(side=TOP) 
    root.mainloop()

def first_main_window():

    root=Tk()
    root.geometry("500x200")
    root.title("DATA Hiding using Steganography - Ashutosh Rawat")
    def callhide():
            root.destroy()
            hide_msg_window()
    def callrtrv():
            root.destroy()
            retrieve_msg_window()

    
    def hidefnTXT():
            root.destroy()
            hide_msg_fromTxt_file()

    a=Button(root,text="clear the window",bd='6',command=root.destroy)
    a.pack(side='bottom',pady=15)  
    
    btnhide = Button(root,text=" HIDE message inside image",bg="yellow",command=callhide)
    btnhide.pack(side=LEFT,padx=20)
    
    btnrtv = Button(root,text=" GET hidden message ",bg="green",command=callrtrv)
    btnrtv.pack(side=RIGHT,padx=20)
    
    abc=Button(root,text="Text File TO Hide",bd='6',command=hidefnTXT)
    abc.pack(side=RIGHT,padx=20)
    
    root.mainloop()
    
first_main_window()