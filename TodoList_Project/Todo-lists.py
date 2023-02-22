# Python 3 Todo-List Project

uinput = ""
data = []


def menu():
    print("\n1. Add an Item")
    print("2. Mark as Done")
    print("3. View full To-do list")
    print("4. Exit App")


def addItem(x):
    data.append(x)
    # print("Added Item:", x)


def delete(deldata):
    if deldata in data:
        data.remove(deldata)
        # print("Completed Task: ", ddata)
        view()
    else:
        print("Task Not Found..!! Cannot Remove\nRecheck the list below\n")
        view()


def view():
    n = 0

    for i in data:
        n = n + 1
        print(n, ')', i)


while uinput != '4':
    menu()
    uinput = input('\nEnter ur choice: ')

    if uinput == '1':
        item = input("Enter Tasks: ")
        addItem(item)

    elif uinput == '2':
        ct = input("Completed Task: ")
        delete(ct)

    elif uinput == '3':
        print("\nList of All-Items")
        view()

    elif uinput == '4':
        print("App Exit")

    else:
        print("Enter with-in 1,2,3 or 4...!!")
