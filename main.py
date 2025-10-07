import argparse
import sqlite3

# set up of command line interface:
def main():
    db = sqlite3.connect('airlineDb')
    print("connected to database")

    cursor = db.cursor()

    parser = argparse.ArgumentParser(description="flight database management command line interface")
    subparsers = parser.add_subparsers(dest="command", help="Available commands: Add, View, Update")
    intro = "Menu: to update pilot use: update -fp [flightID] [pilotID] \n to update destination use: update -fd [flightID] [destinationID] \n to update flight status use: update -fs [flightID] [flightStatus] \n to update flight departure date (ensure departure date is in YYYY/MM/DD format) use: update -fdd [flightID] [departure] "

    # subparser to do add commands
    add_parser = subparsers.add_parser("add", help="add ")
    add_parser.add_argument("-f", nargs=5, help="flight to create, provide all 5 attributes: -f [flightID] [destinationID] [pilotID] [departure] [flightStatus]")

    # subparser to do view commands
    view_parser = subparsers.add_parser("view", help="use to view information from database")
    view_parser.add_argument("--flightID", help="flight to view")

    # subparser to do update commands
    update_parser = subparsers.add_parser("update", help="update commands: -fp [flightID] [pilotID] to update pilot \n -fd")
    update_parser.add_argument("-fp", nargs=2, help="to update pilot use: update -fp [flightID] [pilotID]")
    update_parser.add_argument("-fd", nargs=2, help="to update destination use: update -fd [flightID] [destinationID]")
    update_parser.add_argument("-fs", nargs=2, help="to update flight status use: update -fs [flightID] [flightStatus]")
    update_parser.add_argument("-fdd", nargs=2, help="to update flight departure date (ensure departure date is in YYYY/MM/DD format) use: update -fdd [flightID] [departure]")

    args = parser.parse_args()
    
    #commands

    if args.command == "view":
        lol

    if args.command == "add":
        cursor.execute(f"INSERT INTO flight VALUES ('{args.f[0]}','{args.f[1]}','{args.f[2]}','{args.f[3]}','{args.f[4]}')")
        db.commit()
        print("Confirming update...")
        results = cursor.execute(f"SELECT * FROM flight WHERE flightID = '{args.f[0]}'")
        for row in results:
            print("Flight ID: ", row[0])
            print("Destination ID: ", row[1])
            print("Pilot ID: ", row[2])
            print("Departure Date: ", row[3])
            print("Flight Status: ", row[4])    
    
    if args.command == "update":
        if args.fp:
            cursor.execute(f"UPDATE flight SET pilotID = '{args.fp[1]}' WHERE flightID = '{args.fp[0]}'")
            print(f"updated flight '{args.fp[0]}' with new pilot '{args.fp[1]}'")
            db.commit()
            print("Confirming update...")
            results = cursor.execute(f"SELECT * FROM flight WHERE flightID = '{args.fp[0]}'")
            for row in results:
                print("Flight ID: ", row[0])
                print("Destination ID: ", row[1])
                print("Pilot ID: ", row[2])
                print("Departure Date: ", row[3])
                print("Flight Status: ", row[4])
        # update flight destination with inputted flightID and inputted pilotID 
        elif args.fd:    
            cursor.execute(f"UPDATE flight SET destinationID = '{args.fd[1]}' WHERE flightID = '{args.fd[0]}'")
            print(f"updated flight '{args.fd[0]}' with new destination '{args.fd[1]}'")
            db.commit()
            print("Confirming update...")
            results = cursor.execute(f"SELECT * FROM flight WHERE flightID = '{args.fd[0]}'")
            for row in results:
                print("Flight ID: ", row[0])
                print("Destination ID: ", row[1])
                print("Pilot ID: ", row[2])
                print("Departure Date: ", row[3])
                print("Flight Status: ", row[4])
        # update flight status with inputted flightID and inputted pilotID 
        elif args.fs:    
            cursor.execute(f"UPDATE flight SET flightStatus = '{args.fs[1]}' WHERE flightID = '{args.fs[0]}'")
            print(f"updated flight '{args.fs[0]}' with new flight status '{args.fs[1]}'")
            db.commit()
            print("Confirming update...")
            results = cursor.execute(f"SELECT * FROM flight WHERE flightID = '{args.fs[0]}'")
            for row in results:
                print("Flight ID: ", row[0])
                print("Destination ID: ", row[1])
                print("Pilot ID: ", row[2])
                print("Departure Date: ", row[3])
                print("Flight Status: ", row[4])
        # update flight departure date using inputted arguments
        elif args.fdd:
            cursor.execute(f"UPDATE flight SET departure = '{args.fdd[1]}' WHERE flightID = '{args.fdd[0]}'")
            db.commit()
            print("Confirming update...")
            results = cursor.execute(f"SELECT * FROM flight WHERE flightID = '{args.fdd[0]}'")
            for row in results:
                print("Flight ID: ", row[0])
                print("Destination ID: ", row[1])
                print("Pilot ID: ", row[2])
                print("Departure Date: ", row[3])
                print("Flight Status: ", row[4])

if __name__ == "__main__":
    main()

# retrieve flight information based on multiple criteria such as destination, status, departure
# done: update flight information
# done: update flight pilot
# view destination information
# update destination information
# summarise data based on destination
# summarise data based on flights per pilot
# summarise data based on departure date