command = ""

started = False

while  True:
    command = input("> ").lower()

if command == "start":
    if started:
        print("Car has already been started!")
    else:
        started = True
    print("Car started...")

elif command.lower() == "stop":
    if not started: 
        print("Car has already been stopped!")
    else:
        started = False
        print("Car stopped...")

elif command == "help":
    print("""
start - to start the car
stop - to stop the car
quit - to quit
          """)

elif command == "quit": 
    break

else: 
    print("Sorry I dont understand that!")