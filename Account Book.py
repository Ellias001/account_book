import _pickle

class Person():
    def __init__(self):
        try:
            fileAcc = open("Accounts.bin", "rb")
        except FileNotFoundError:
            self.account = dict()
        else:
            try:
                self.account = dict(_pickle.load(fileAcc))
            except EOFError:
                self.account = dict()
            fileAcc.close()

        try:
            fileGr = open("Groups.bin", "rb")
        except FileNotFoundError:
            self.groups = dict()
        else:
            try:
                self.groups = dict(_pickle.load(fileGr))
            except EOFError:
                self.groups = dict()
            fileGr.close()
    
    def createAccount(self, name, number):
        self.account[name] = number

    def deleteAccount(self, name):
        del(self.account[name])

    def printAll(self):
        j = 0
        for i in self.account:
            j -=- 1
            print(str(j) + ": " + i + "\t" + self.account[i])

    def search(self, name):
        print(self.account[name])

    def modifyAccount(self, name, number):
        self.account[name] = number

    def isExist(self, name):
        try:
            self.account[name]
        except KeyError:
            return 0
        return 1
    
    def addToGroup(self, groupName):
        n = str("a")
        print("Type in existing name or press enter to exit: ", end = "")
        if not self.groups[groupName] in locals():
            self.groups[groupName] = ""
        while n != "":
            n = str(input())
            self.groups[groupName] += n + " "

    def printGroup(self, groupName):
        try:
            self.groups[groupName]
        except KeyError:
            print("This group does not exist. Try again.")
            return
        j = 0
        for i in self.groups[groupName].split():
            j -=- 1
            print(str(j) + ": " + i + "\t" + self.account[i])

    def changeName(self, nameCur, nameNew):
        self.account[nameNew] = self.account[nameCur]
        del self.account[nameCur]

    def __del__(self):
        fileAcc = open("Accounts.bin", "w+b")
        fileGr = open("Groups.bin", "w+b")
        _pickle.dump(self.account, fileAcc)
        _pickle.dump(self.groups, fileGr)
        fileAcc.close()
        fileGr.close()

p = Person()
a = 1
print("""1: Create new account
2: Delete account
3: Search number
4: Print all numbers
5: Add account(s) to group
6: Print whole group
7: Change account name/contact number
0: Exit""")
while a != 0:
    print("Input number: ", end = "")

    try:
        a = int(input())
    except ValueError:
        print("Eror: Not a number. Please, try again.")
        continue

    if a == 1:
        print("Enter name:", end = " ")
        name = str(input())
        
        if p.isExist(name):
            print("This name is in account book. Do you want to modify? (Y/N)")
            confirm = str(input())
            if confirm == "n" or confirm == "N":
                continue
            del confirm
            
        print("Enter contact number:", end = " ")
        num = str(input())
        p.createAccount(name, num)
    elif a == 2:
        print("Enter name:", end = " ")
        name = str(input())
        
        if not p.isExist(name):
            print("Eror: This contact does not exist.")
            continue
        
        print("Do you want to delete \"%s\" account? (Y/N)" % name)
        confirm = str(input())

        if confirm == "n" or confirm == "N":
            continue
        del confirm

        p.deleteAccount(name)
    elif a == 3:
        print("Enter name:", end = " ")
        name = str(input())
        if not p.isExist(name):
            print("This name does not exist. Try again.")
            continue
        p.search(name)
    elif a == 4:
        p.printAll()
    elif a == 5:
        print("Enter group name: ", end = "")
        groupName = str(input())
        p.addToGroup(groupName)
    elif a == 6:
        print("Enter group name: ", end = "")
        groupName = str(input())
        p.printGroup(groupName)
    elif a == 7:
        print("Type N if you want to change name\nC if you want to change a contact number")
        confirm = str(input())
        print("Enter current account name: ", end = "")
        nameCur = str(input())
        if not p.isExist(nameCur):
            print("This name does not exist. Try again.")
            continue
        if confirm == "C" or confirm == "c":
            print("Enter new contact number:", end = " ")
            num = str(input())
            p.createAccount(nameCur, num)
        elif confirm == "N" or confirm == "n":
            print("Enter new account name: ", end = "")
            nameNew = str(input())
            p.changeName(nameCur, nameNew)
        del confirm
    elif a == 0:
        print("Saving all information.")
    else:
        print("Unknown command, please try again")
del p