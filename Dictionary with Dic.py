class Node:
    def __init__(self):
        self.tra=None
        self.word=None
        self.dic = { }
        self.dicLen = len(self.dic)
def showAll(pos):
    if pos.word is not None:
        print(pos.word)
    for item in pos.dic:
        if pos.dic[item].word is not None  :
            print(pos.dic[item].word)
        if  pos.dic[item].dic.__len__():
            for ii in pos.dic[item].dic:
                showAll(pos.dic[item].dic[ii])
lst = []
# tree show
def show(pos):
    for item in pos.dic:
        print(pos.dic[item].dicLen)
        show(pos.dic[item])

def add(pos,str,tra):
    ln = len(str)
    for i in range(ln):
        if not pos.dic.get(str[i]):
            pos.dic.update({str[i]: Node()})
        pos = pos.dic.get(str[i])
        if i == ln - 1:
            pos.tra = tra
            pos.word = str
            pos.dicLen += 1
            return

root = Node()
f = open("E:\\Uni\Dictionary\input.txt","r")
ln=f.readlines().__len__()
f.seek(0)

for i in range(int(ln/2)):
    add(root,f.readline().lower().strip() , f.readline().lower().strip())
while(True):
    flg = False
    # by def is False and
    # if end of str be >*<  flg gonna be true for do some job on it
    pos = root
    n=int(input("1-Add WORD\n2-Search WORD\n3-Remove WORD\n>>>"))
    if(n == 1):
        str = input("Enter:\n>>>").lower().strip()
        tra = input("Enter Meaning\n>>>").lower().strip()
        add(root, str, tra)
    elif(n == 2):
        str = input("Enter:\n>>>").lower().strip()
        ln=len(str)
        if str[-1] == '*':
            ln-=1
            flg = True
        for i in range(ln):
            if pos.dic.get(str[i]) is not None:
                pos = pos.dic.get(str[i])
                if i == ln - 1:
                    if not flg:
                        if pos.tra :
                            print(pos.tra)
                        else :
                            print(f"{str},Translation ISN'T EXIST.")
                    else :
                        showAll(pos)
            else :
                print(f"{str},Translation ISN'T EXIST.")
                break

    elif(n == 3):
        str = input("Enter:\n>>>").lower().strip()
        ln=len(str)
        for i in range(ln):
            if pos.dic.get(str[i]) is not None:
                pos = pos.dic.get(str[i])
                if i == ln - 1:
                    pos.word=None
                    pos.tra=None
                    if pos.dic.__len__() == 0 :
                        del(pos)
            else :
                print(f"{str}, ISN'T EXIST.")
                break