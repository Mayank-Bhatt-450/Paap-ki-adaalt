from Tkinter import*
import ttk,json,os,datetime
def raise_frame(frame):
    ##print"ddd"
    frame.tkraise()
try:
    w=open('txt.txt','r')
    dict= json.loads(w.read())
    w.close()
except:
    dict = {'MAYANK BHATT': {'Smartness': [], 'Looks': [], 'Tube Light': [], 'Chirand': [], 'Dogula': [], 'Chidchida(chidkut)': [], 'Hapsi': [], 'Gulaam': [], 'Budhdhan': [], 'Faiku': [],'Gobar budhdhi':[]},
            'MAYANK VISHWAKARMA': {'Smartness': [], 'Looks': [], 'Tube Light': [], 'Chirand': [], 'Dogula': [], 'Chidchida(chidkut)': [], 'Hapsi': [], 'Gulaam': [], 'Budhdhan': [], 'Faiku': [],'Gobar budhdhi':[]},
            'VARUN VISHWAKARMA': {'Smartness': [], 'Looks': [], 'Tube Light': [], 'Chirand': [], 'Dogula': [], 'Chidchida(chidkut)': [], 'Hapsi': [], 'Gulaam': [], 'Budhdhan': [], 'Faiku': [],'Gobar budhdhi':[]},
            'TUSHAR': {'Smartness': [], 'Looks': [], 'Tube Light': [], 'Chirand': [], 'Dogula': [], 'Chidchida(chidkut)': [],'Hapsi': [], 'Gulaam': [], 'Budhdhan': [], 'Faiku': [], 'Gobar budhdhi': []},
            'VAIBHAV JAIN': {'Smartness': [], 'Looks': [], 'Tube Light': [], 'Chirand': [], 'Dogula': [], 'Chidchida(chidkut)': [],'Hapsi': [], 'Gulaam': [], 'Budhdhan': [], 'Faiku': [], 'Gobar budhdhi': []},
            'VAIBHAV BHATT': {'Smartness': [], 'Looks': [], 'Tube Light': [], 'Chirand': [], 'Dogula': [], 'Chidchida(chidkut)': [],'Hapsi': [], 'Gulaam': [], 'Budhdhan': [], 'Faiku': [], 'Gobar budhdhi': []}
            }
    w = open('txt.txt', 'w')
    w.write(json.dumps(dict))
    w.close()

#dict={'mayank':{'name':[],'class':[],'rollno':[],'me':[]},'mayankv':{'name':[],'class':[],'rollno':[],'me':[]},'mayankv1':{'name':[],'class':[],'rollno':[],'me':[]}}
names=dict.keys()
root=Tk()
root.title('PAAP KI ADAALT')
root.resizable(False,False  )
#root.geometry('1028x599+100+50')
f1 = Frame(root)#,width=1028,height=599)#home
f2 = Frame(root)#,width=1028,height=599)#entry
f3 = Frame(root)#,width=1028,height=599)#search
f4 = Frame(root)#,width=1028,height=599)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')
def vot(i2,host1,host,s):
    l=dict[host].keys()
    for i in range(len(s)):
        dict[host][l[i]].append(0)
        dict[host][l[i]][len(dict[host][l[i]])-1]=s[i].get()
        #print i.get()
    vote(i2 + 1, host1)
def voting(i2,host1,host):
    if i2<len(names):
        d = ttk.Label(f2, text=host,font=('bold'),foreground="blue" )
        d.grid(row=0, column=0, sticky='news')
        f = dict[host].keys()
        x = 1
        li = []
        star = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(len(f)):
            li.append('0')
            li[i] = StringVar(f2)
            li[i].set(0)
            d = ttk.Label(f2, text=f[i])
            d.grid(row=x, column=0, sticky='news')
            w = OptionMenu(f2, li[i], *star)  # ,command= dis)
            w.grid(row=x, column=1, sticky='news')
            x += 1
        b = ttk.Button(f2, text="send it", command=lambda: vot(i2,host1,host, li))
        b.grid(row=x, column=0, sticky='news')  # .grid(column=0, row=2)

def vote(i,host):
    if i<len(names):
        raise_frame(f2)
        s=dict.keys()
        #print i ,'pre'
        if names[i] != host and i<len(names):
            #print names, i, '----------', names[i]
            voting(i,host,names[i])

        else:
            #print i, '----------', names[i]
            vote(i+1,host)

    else:
        raise_frame(f1)
        w = open('txt.txt', 'w')
        w.write(json.dumps(dict))
        w.close()
       #print dict
        #exit(0)
def pri(t):
    if t=='987456321':

        di={}
        for i in names:
            d = {}
            #print i,'i'
            for j in dict[i].keys():
                #print j,'j'
                g=0
                for k in range(len(dict[i][j])):
                    g+=int(dict[i][j][k])
                #print g
                g=(float(g)/50)*10
                #print g
                #raw_input()
                d[j]=g
            di[i]=d
        s=''
        for h in di.keys():
            s+='\n'+h+'-'*27+'\n'
            for n in di[h].keys():
                s+=str(n)+' '*(18-len(str(n)))+'    :'+str(di[h][n])+'\n'
        p=str(datetime.datetime.today())[:10]
        w=open(p+' print.txt','w')
        w.write(s)
        w.close()
        os.startfile(p+" print.txt", "print")
        print s
    else:
        pass

var=StringVar(f1)
var.set("")
ddmm2 = OptionMenu(f1, var, *names)#,command= dis)
ddmm2.grid(row=0, column=0, sticky='news')
button2 = ttk.Button(f1, text="login",command=lambda: vote(0,var.get()))
button2.grid(row=0, column=1, sticky='news')  # .grid(column=0, row=2)
#dmm2.configure(indicatoron=0, compound='right',image= w001,bg='white',bd=0)
button = ttk.Button(f1, text="make result and print ",command=lambda: pri(e.get()))
button.grid(row=2, column=0, sticky='news')  # .grid(column=0, row=2)
e=Entry(f1)
e.grid(row=2, column=1, sticky='news')
raise_frame(f1)
def on_closing():
    #print 'distroy'
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
