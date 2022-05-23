from tkinter import *
import math
from pygame import mixer
mixer.init()
import speech_recognition
def click(value):
    ex = entryfield.get()
    ans=" "
    try:
        if(value=="C"):
            ex=ex[0:len(ex)-1]
            entryfield.delete(0,END)
            entryfield.insert(0,ex)
            return

        elif(value=="CE"):
            entryfield.delete(0, END)
        elif (value == "√"):
            ans=math.sqrt(eval(ex))
        elif (value == "π"):
            ans=math.pi
        elif (value == "cosθ"):
            ans=math.cos(math.radians(eval(ex)))
        elif (value == "tanθ"):
            ans=math.tan(math.radians(eval(ex)))
        elif (value == "sinθ"):
            ans=math.sin(math.radians(eval(ex)))
        elif (value == "2π"):
            ans=2*math.pi
        elif (value == "cosh"):
            ans=math.cosh(eval(ex))
        elif (value == "tanh"):
            ans=math.tanh(eval(ex))
        elif (value == "sinh"):
            ans=math.sinh(eval(ex))
        elif (value == chr(8731)):
            ans = eval(ex)**(1/3)
        elif (value == "x\u02b8"):
            entryfield.insert(END,"**")
            return
        elif (value == "x\u00B3"):
            ans = eval(ex) ** (3)
        elif (value == "x\u00B2"):
            ans = eval(ex) ** (2)
        elif (value == "rad"):
            ans = math.radians(eval(ex))
        elif (value =="e"):
            ans = math.e
        elif (value =="log₁₀"):
            ans = math.log10(eval(ex))
        elif (value =="ln"):
            ans = math.log2(eval(ex))
        elif (value =="x!"):
            ans = math.factorial((ex))
        elif (value == chr(247)):
            ans = entryfield.insert(END,"/")
            return
        elif (value =="="):
            ans = eval(ex)
        else:
            entryfield.insert(END,value)
            return
        entryfield.delete(0, END)
        entryfield.insert(0, ans)

    except SyntaxError:
        pass

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(a,b):
    l=math.lcm(a,b)
    return l
def hcf(a,b):
    h=math.gcd(a,b)
    return h
def findnumbers(t):
    l=[]
    for num in t:
        try:
            l.append(float(num))
        except ValueError:
            pass
    return l

operations={"ADD":add,"ADDITION":add,"sum":add,"plus":add,
            "SUBTRATION":sub,"SUB":sub,"":sub,"DIFFRENCE":sub,"SUBTRACT":sub,"PRODUCT":mul,"MULTIPLICATION":mul,"MULTIPLY":mul,
            "DIVISION":div,"DIV":div,"DIVIDE":div,"HCF":hcf,"lcm":lcm,"MOD":mod,"MODULUS":mod,"REMAINDER":mod}
def audio():
    mixer.music.load("music1.mp3")
    mixer.music.play()
    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        try:
            sr.adjust_for_ambient_noise(mic,duration=0.2)
            voice=sr.listen(mic)
            text=sr.recognize_google(voice)
            mixer.music.load("music2.mp3")
            mixer.music.play()
            text_list=text.split(" ")
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findnumbers(text_list)
                    result=operations[word.upper()](l[0],l[1])
                    entryfield.delete(0,END)
                    entryfield.insert(END,result)
                else:
                    pass
        except:
            pass



root=Tk()
root.title("smart calcy")
root.config(bg="sky blue")
root.geometry("680x486+100+100")

logo_image=PhotoImage(file="logo.png")
logolabel=Label(root,image=logo_image)
logolabel.grid(row=0,column=0)



entryfield=Entry(root,font=('ariel',20,'bold'),bg="sky blue",fg="white",bd=10,relief=SUNKEN,width=30)

entryfield.grid(row=0,column=0,columnspan=8)

mic_image=PhotoImage(file="microphone.png")
mic_button=Button(root,image=mic_image,bd=0 ,bg="sky blue",activebackground="blue",command=audio)

mic_button.grid(row=0,column=7)


button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",".",
                    "0", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue=1
columnvalue=0
for i in button_text_list:
    button=Button(root,width=5,height=2,relief=SUNKEN,text=i,bg="sky blue",fg="white",font=("ariel",18,"bold"),activebackground="blue",command=lambda button=i: click(button))
    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>7:
        rowvalue+=1
        columnvalue=0




root.mainloop()