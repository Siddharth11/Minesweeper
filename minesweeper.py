print "Enter 2 numbers greater than 1 to create a minesweeper field"

i=int(raw_input())
j=int(raw_input())

field=[]

for x in range(0,i):
    field.append([0]*j)
    
from random import randint
num1=(i*j)/7

list1=[]
for x in range(0,num1):
    a=randint(1,i)
    b=randint(1,j)
    list1.append([a,b])

def print_field(o):

    display_up=[]
    for s in range(65,65+j):
        display_up.append(chr(s))
    print "     ",
    for s in display_up:
        print s,
    print "\n"
    for s in range(0,i):
        print s+1,
        if(0<=((s+1)/10.0)<=.9):
            print '   '+('|' + '|'.join(o[s]) + '|')
        elif(1<=((s+1)/10.0)<10):
            print '  '+('|' + '|'.join(o[s]) + '|')
    print"\n"
        
uniq=set(tuple(element) for element in list1)#to remove duplicate elements and also lists are unhashable so first we have to tuple it
num=len(uniq)
print "Number of mines:{}".format(num)
#print "Mines position: ",

for x in uniq:
    a=x[0]
    b=x[1]
    #print [a,b],
    field[a-1][b-1]='*'

print "\n"
    
for x in range(0,i):
    for y in range(0,j):
        if(type(field[x][y])==int):#no mine condition
            if(0<x<i-1 and 0<y<j-1):#centre
                if(field[x][y+1]=='*'):
                    field[x][y]+=1
                if(field[x][y-1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y]=='*'):
                    field[x][y]+=1
                if(field[x-1][y]=='*'):
                    field[x][y]+=1
                if(field[x+1][y+1]=='*'):
                    field[x][y]+=1
                if(field[x-1][y-1]=='*'):
                    field[x][y]+=1
                if(field[x-1][y+1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y-1]=='*'):
                    field[x][y]+=1
            if(x==0 and y==0):#top left corner
                if(field[x][y+1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y+1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y]=='*'):
                    field[x][y]+=1
            if(x==i-1 and y==0):#bottom left corner
                if(field[x-1][y]=='*'):
                    field[x][y]+=1
                if(field[x-1][y+1]=='*'):
                    field[x][y]+=1
                if(field[x][y+1]=='*'):
                    field[x][y]+=1
            if(x==0 and y==j-1):#top right corner
                if(field[x][y-1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y-1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y]=='*'):
                    field[x][y]+=1
            if(x==i-1 and y==j-1):#bottom right corner
                if(field[x][y-1]=='*'):
                    field[x][y]+=1
                if(field[x-1][y]=='*'):
                    field[x][y]+=1
                if(field[x-1][y-1]=='*'):
                    field[x][y]+=1
            if(x==0 and y!=0 and y!=j-1):#top side
                if(field[x][y+1]=='*'):
                    field[x][y]+=1
                if(field[x][y-1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y]=='*'):
                    field[x][y]+=1
                if(field[x+1][y-1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y+1]=='*'):
                    field[x][y]+=1
            if(x==i-1 and y!=j-1 and y!=0):#bottom side
                if(field[x][y+1]=='*'):
                    field[x][y]+=1
                if(field[x][y-1]=='*'):
                    field[x][y]+=1
                if(field[x-1][y-1]=='*'):
                    field[x][y]+=1
                if(field[x-1][y]=='*'):
                    field[x][y]+=1
                if(field[x-1][y+1]=='*'):
                    field[x][y]+=1
            if(x!=0 and x!=i-1 and y==0):#left side
                if(field[x][y+1]=='*'):
                    field[x][y]+=1
                if(field[x-1][y]=='*'):
                    field[x][y]+=1
                if(field[x-1][y+1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y+1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y]=='*'):
                    field[x][y]+=1
            if(x!=0 and x!=i-1 and y==j-1):#right side
                if(field[x][y-1]=='*'):
                    field[x][y]+=1
                if(field[x-1][y-1]=='*'):
                    field[x][y]+=1
                if(field[x-1][y]=='*'):
                    field[x][y]+=1
                if(field[x+1][y-1]=='*'):
                    field[x][y]+=1
                if(field[x+1][y]=='*'):
                    field[x][y]+=1

for y in range(0,i):
    for x in range(0,j):
        field[y][x]=str(field[y][x])

import copy
field2=copy.deepcopy(field)
#print id(field2)
#print id(field)

for x in range(0,i):
    for y in range(0,j):
        field2[x][y]='_'

print "The field has been created\n\n"

print "\n"
print_field(field2)

print "Enter the place index which you want to open"

def method(option,new):
        print "Enter the row no. and column name"
        p=int(raw_input())
        q=raw_input()
        p=p-1
        if 97<=ord(q)<=122:
            q=ord(q)-97
        else:
            q=ord(q)-65
        field2[p][q]='F'
        count=0
        for p in range(0,i):
            for q in range(0,j):
                if field2[p][q]=='F':
                    count+=1
        return new-count

def flag():
    global num
    temp=num
    choice=raw_input("Do you want to put a flag (y/n)? : ")
    if choice=='y' or choice=='yes' or choice=='Y' or choice=='Yes':
        total=method(choice,temp)
        print "Number of mines left = {}\n".format(total)
        print_field(field2)
        temp=total
        for many in range(0,i*j):
            choice=raw_input("Do you want to put another flag(y/n)? : ")
            if choice=='y' or choice=='yes' or choice=='Y' or choice=='Yes':
                total2=method(choice,total)
                print "Number of mines left = {}\n".format(total2)
                print_field(field2)
                total=total2
            elif choice=='n' or choice=='N' or choice=='No' or choice=='no':
                print "Number of mines left = {}".format(total)
                print "\n"
                break
            else:
                print "Invalid input!"
    elif choice=='n' or choice=='N' or choice=='No' or choice=='no':
        print "Number of mines left = {}".format(temp)
        print "\n"

def win():
    field3=copy.deepcopy(field2)
    flag=0
    for x in range(i):
        for y in range(j):
            if field3[x][y]=='_' or field3[x][y]=='F':
                field3[x][y]='*'
    for x in range(i):
        for y in range(j):
            if field3[x][y]==field[x][y]:
                flag+=1
    if flag==i*j:
        result='Win'
        return result
    
def foo():
    for x in range(0,i):
        for y in range(0,j):
            if(0<x<i-1 and 0<y<j-1):#centre
                if(field2[x][y]=='0'):
                    field2[x][y+1]=field[x][y+1]
                    field2[x][y-1]=field[x][y-1]
                    field2[x+1][y]=field[x+1][y]
                    field2[x-1][y]=field[x-1][y]
                    field2[x+1][y+1]=field[x+1][y+1]
                    field2[x-1][y-1]=field[x-1][y-1]
                    field2[x-1][y+1]=field[x-1][y+1]
                    field2[x+1][y-1]=field[x+1][y-1]
            if(x==0 and y==0):#top left corner
                if(field2[x][y]=='0'):
                    field2[x][y+1]=field[x][y+1]
                    field2[x+1][y+1]=field[x+1][y+1]
                    field2[x+1][y]=field[x+1][y]
            if(x==i-1 and y==0):#bottom left corner
                if(field2[x][y]=='0'):
                    field2[x-1][y]=field[x-1][y]
                    field2[x-1][y+1]=field[x-1][y+1]
                    field2[x][y+1]=field[x][y+1]
            if(x==0 and y==j-1):#top right corner
                if(field2[x][y]=='0'):
                    field2[x][y-1]=field[x][y-1]
                    field2[x+1][y-1]=field[x+1][y-1]
                    field2[x+1][y]=field[x+1][y]
            if(x==i-1 and y==j-1):#bottom right corner
                if(field2[x][y]=='0'):
                    field2[x][y-1]=field[x][y-1]
                    field2[x-1][y]=field[x-1][y]
                    field2[x-1][y-1]=field[x-1][y-1]
            if(x==0 and y!=0 and y!=j-1):#top side
                if(field2[x][y]=='0'):
                    field2[x][y+1]=field[x][y+1]
                    field2[x][y-1]=field[x][y-1]
                    field2[x+1][y]=field[x+1][y]
                    field2[x+1][y-1]=field[x+1][y-1]
                    field2[x+1][y+1]=field[x+1][y+1]
            if(x==i-1 and y!=j-1 and y!=0):#bottom side
                if(field2[x][y]=='0'):
                    field2[x][y+1]=field[x][y+1]
                    field2[x][y-1]=field[x][y-1]
                    field2[x-1][y-1]=field[x-1][y-1]
                    field2[x-1][y]=field[x-1][y]
                    field2[x-1][y+1]=field[x-1][y+1]
            if(x!=0 and x!=i-1 and y==0):#left side
                if(field2[x][y]=='0'):
                    field2[x][y+1]=field[x][y+1]
                    field2[x-1][y]=field[x-1][y]
                    field2[x-1][y+1]=field[x-1][y+1]
                    field2[x+1][y+1]=field[x+1][y+1]
                    field2[x+1][y]=field[x+1][y]
            if(x!=0 and x!=i-1 and y==j-1):#right side
                if(field2[x][y]=='0'):
                    field2[x][y-1]=field[x][y-1]
                    field2[x-1][y-1]=field[x-1][y-1]
                    field2[x-1][y]=field[x-1][y]
                    field2[x+1][y-1]=field[x+1][y-1]
                    field2[x+1][y]=field[x+1][y]

def quick(c,d):
    if(field[c][d]!='*'):
        field2[c][d]=field[c][d]

def plus1_condition1(x,y):
        if(0<x<i-1 and 0<y<j-1):#centre
            quick(x,y+1)
            quick(x,y-1)
            quick(x+1,y)
            quick(x-1,y)
            quick(x+1,y+1)
            quick(x-1,y-1)
            quick(x-1,y+1)
            quick(x+1,y-1)
        if(x==0 and y==0):#top left corner
            quick(x,y+1)
            quick(x+1,y+1)
            quick(x+1,y)
        if(x==i-1 and y==0):#bottom left corner
            quick(x-1,y)
            quick(x-1,y+1)
            quick(x,y+1)
        if(x==0 and y==j-1):#top right corner
            quick(x,y-1)
            quick(x+1,y-1)
            quick(x+1,y)
        if(x==i-1 and y==j-1):#bottom right corner
            quick(x,y-1)
            quick(x-1,y)
            quick(x-1,y-1)
        if(x==0 and y!=0 and y!=j-1):#top side
            quick(x,y+1)
            quick(x,y-1)
            quick(x+1,y)
            quick(x+1,y-1)
            quick(x+1,y+1)
        if(x==i-1 and y!=j-1 and y!=0):#bottom side
            quick(x,y+1)
            quick(x,y-1)
            quick(x-1,y-1)
            quick(x-1,y)
            quick(x-1,y+1)
        if(x!=0 and x!=i-1 and y==0):#left side
            quick(x,y+1)
            quick(x-1,y)
            quick(x-1,y+1)
            quick(x+1,y+1)
            quick(x+1,y)
        if(x!=0 and x!=i-1 and y==j-1):#right side
            quick(x,y-1)
            quick(x-1,y-1)
            quick(x-1,y)
            quick(x+1,y-1)
            quick(x+1,y)
            
def incorrect(g):
    if g<=0:
        print "Enter a number greater than or equal to 1"
        g=int(raw_input())
        incorrect(g)

for E in range(0,i*j):
    game=win()
    if game=='Win':
        print "You won the game"
        print_field(field)
        break
    print "(open a box)"
    u=int(raw_input("Row no. : "))
    incorrect(u)
    v=raw_input("Column name : ")
    if 97<=ord(v)<=122:
        v=ord(v)-96
    else:
        v=ord(v)-64
    incorrect(v)
    print "\n"
    e=u-1
    f=v-1
    if(field[e][f]=='*'):
        print "You lost the game\n"
        field[e][f]='X'
        print_field(field)
        break
    elif(field[e][f]!='*'):
        field2[e][f]=field[e][f]
        plus1_condition1(e,f)
        for one in range(0,i*j):
            foo()
        game=win()
        if game=='Win':
            print "You won the game"
            print_field(field)
            break
        print_field(field2)
        flag()
        game=win()
        if game=='Win':
            print "You won the game"
            print_field(field)
            break
    
raw_input("press enter to exit")
