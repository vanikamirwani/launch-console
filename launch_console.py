name = ("Vanika Mirwani ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Exit")
    choice = input("Pick 1-3: ")
    if choice == "1":
        print("I am a junior who is interested in STEM careers.")
    elif choice == "2":
        print("I want to create projects this term and I also want to make an impact in my community.")
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, or 3.")