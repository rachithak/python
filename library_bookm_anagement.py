books=[]
while True:
    print("\n===== Library Menu=====")
    print("1.Add Book")
    print("2.Veiw Books")
    print("3.search book")
    print("4.exit")
    choice=input("enter your choice:")
    if choice=="1":
        book=input("Enter book name:")
        auther=input("Enter auther name:")
        books.append((book,auther))
        print("Book added successfully")
    elif choice=="2":
        if len(books)==0:
            print("no books available.")
        else:
            print("\nAvailable Books")
            for i,b in enumerate(books,start=1):
                print(f"{i}.{b[0]} by {b[1]}")
    elif choice=="3":
        search=input("enter book name search:")
        found=False
        for b in books:
            if b[0].lower()==search.lower():
                print(f"book Found:{b[0]} by {b[1]}")
                found=True
                break
        if not found:
            print("book not found.")
    elif choice=="4":
        print("thank you for using the library system!")
    else:
        print("invalid choice.try again.")