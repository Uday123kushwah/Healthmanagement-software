def datetime():
    import datetime
    return datetime.datetime.now()
print(datetime())

print("what do you want 1 for retreive and 2 for lock:")
n=int(input())
if n==1:
    print("What is your name 1 for harry 2 for rohan 3 for jack::")
    name=int(input())
    if name==1:
        print("what do you want 1 for exercise and 2 for food::")
        ef=int(input())
        if ef==1:
            with open("harry-exer.txt","a") as f:
                print("type here:: \n")
                value=input()
                f.write(str([str(datetime())])+":"+value+"\n")
        else:
            with open("harry-food.txt","a") as f1:
                print("type hare:: \n")
                value1=input()
                f1.write(str([str(datetime())])+":"+value1+"\n")
    elif name==2:
        print("what do you want 1 for exercise and 2 for food::")
        ef = int(input())
        if ef == 1:
            with open("rohan-exer.txt", "a") as f:
                print("type here:: \n ")
                value = input()
                f.write(str([str(datetime())])+":"+value+"\n")
        else:
            with open("rohan-food.txt", "a") as f1:
                print("type hare:: \n ")
                value1 = input()
                f1.write(str([str(datetime())])+":"+value1+"\n")

    else:
        print("what do you want 1 for exercise and 2 for food::")
        ef = int(input())
        if ef == 1:
            with open("jack-exer.txt", "a") as f:
                print("type here:: \n ")
                value = input()
                f.write(str([str(datetime())])+":"+value+"\n")
        else:
            with open("jack-food.txt", "a") as f1:
                print("type hare:: \n")
                value1 = input()
                f1.write(str([str(datetime())])+":"+value1+"\n")

elif n==2:
    print("Who are you 1 for harry 2 for rohan and 3 for jack::")
    name1=int(input())
    if name1==1:
        print("what do you want 1 for exercise 2 for food::")
        ef1=int(input())
        if ef1==1:
            f=open("harry-exer.txt")
            a=f.read()
            print(a,"\n")
            f.close()

        else:
            f=open("harry-food.txt")
            a=f.read()
            print(a,"\n")
            f.close()

    elif name1==2:
        print("what do you want 1 for exercise 2 for food::")
        ef1 = int(input())
        if ef1 == 1:
            f = open("rohan-exer.txt")
            a = f.read()
            print(a,"\n")
            f.close()

        else:
            f = open("rohan-food.txt")
            a = f.read()
            print(a,"\n")
            f.close()

    else:
        print("what do you want 1 for exercise 2 for food::")
        ef1 = int(input())
        if ef1 == 1:
            f = open("jack-exer.txt")
            a = f.read()
            print(a,"\n")
            f.close()

        else:
            f = open("jack-food.txt")
            a = f.read()
            print(a,"\n")
            f.close()
