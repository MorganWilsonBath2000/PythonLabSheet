import argparse
import sqlite3

# set up of command line interface:
def main():
    db = sqlite3.connect('airlineDb')
    print("connected to database")

    cursor = db.cursor()

    parser = argparse.ArgumentParser(description="flight database management command line interface")
    subparsers = parser.add_subparsers(dest="command", help="Available commands: Add, View, Update")
    intro = "Menu: \n Flight Info Update Commands: \n to update pilot use: update -fp [flightID] [pilotID] \n to update destination use: update -fd [flightID] [destinationID] \n to update flight status use: update -fs [flightID] [flightStatus] \n to update flight departure date (ensure departure date is in YYYY/MM/DD format) use: update -fdd [flightID] [departureDate] " \
    " \n Add Entity Commands: \n to add flight: add -f [flightID] [destinationID] [pilotID] [departureDate] [flightStatus] \n to add destination: add -d [destinationID] [destinationCity] [destinationCountry] \n "

    # subparser to do add commands
    add_parser = subparsers.add_parser("add", help="add commansd")
    add_parser.add_argument("-f", nargs=5, help="to add flight, provide all 5 attributes, use: add -f [flightID] [destinationID] [pilotID] [departureDate] [flightStatus]")
    add_parser.add_argument("-d", nargs=3, help="to add destination, provide all 3 attributes, use: add -d [destinationID] [destinationCity] [destinationCountry]")
    add_parser.add_argument("-p", nargs=3, help="to add pilot, provide both attributes and use only Forename and Surname, use: add -p [pilotID] [pilotForename] [pilotSurname]")

    # subparser to do view commands
    view_parser = subparsers.add_parser("view", help="use to view information from database")
    view_parser.add_argument("-flightID", required=False, help="flight to view")
    view_parser.add_argument("-pilotID", required=False, help="pilotID to view")
    view_parser.add_argument("-destina", required=False, help="destination to view")
    view_parser.add_argument("-dd", required=False, help="flights departing on date to view")
    view_parser.add_argument("-s", required=False, help="flight Status to view")
    view_parser.add_argument("-c", required=False, help="view flights by country")


    # subparser to do update commands
    update_parser = subparsers.add_parser("update", help="update commands ")
    update_parser.add_argument("-fp", nargs=2, help="to update pilot use: update -fp [flightID] [pilotID]")
    update_parser.add_argument("-fd", nargs=2, help="to update destination use: update -fd [flightID] [destinationID]")
    update_parser.add_argument("-fs", nargs=2, help="to update flight status use: update -fs [flightID] [flightStatus]")
    update_parser.add_argument("-fdd", nargs=2, help="to update flight departure date (ensure departure date is in YYYY/MM/DD format) use: update -fdd [flightID] [departureDate]")
    update_parser.add_argument("-pn", nargs=3, help="to update pilot name (only forename and surname) use: update -pn [pilotID] [pilotForename] [pilotSurname]")

    args = parser.parse_args()
    
    #commands

    if args.command == "view":
        
        tables = ', '
        columns = ', '
        args = args.__dict__
        columns.join([a+'=%s' for a in args if args[a]])
        values = tuple([args[a] for a in args if args[a]])
    #    if args.p:
    #        print("1")
    #    if args.d:
    #        print("2")
    #    if args.dd:
    #        print("3")
    #    if args.s:
    #        print("4")
    #    if args.c:
    #        print("5")

        statement = "SELECT * FROM flight WHERE " + columns
        cursor.execute(statement,values)

    if args.command == "add":
        if args.f:
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
        elif args.d:
            cursor.execute(f"INSERT INTO destination VALUES ('{args.d[0]}','{args.d[1]}','{args.d[2]}')")
            db.commit()
            print("Confirming update...")
            results = cursor.execute(f"SELECT * FROM destination WHERE destinationID = '{args.d[0]}'")
            for row in results:
                print("Destination ID: ", row[0])
                print("Destination City: ", row[1])
                print("Destination Country: ", row[2])
        elif args.p:        
            cursor.execute(f"INSERT INTO pilot VALUES ('{args.p[0]}','{args.p[1] + " " + args.p[2]}')")
            db.commit()
            print("Confirming update...")
            results = cursor.execute(f"SELECT * FROM pilot WHERE pilotID = '{args.p[0]}'")
            for row in results:
                print("Pilot ID: ", row[0])
                print("Pilot Name: ", row[1])
        else:
            print("Add Menu: \n to create flight, provide all 5 attributes, use: add -f [flightID] [destinationID] [pilotID] [departureDate] [flightStatus] \n to add destination, provide all 3 attributes, use: add -d [destinationID] [destinationCity] [destinationCountry] \n to add pilot, provide both attributes and use only Forename and Surname, use: add -p [pilotID] [pilotForename] [pilotSurname]")

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
            cursor.execute(f"UPDATE flight SET departureDate = '{args.fdd[1]}' WHERE flightID = '{args.fdd[0]}'")
            db.commit()
            print("Confirming update...")
            results = cursor.execute(f"SELECT * FROM flight WHERE flightID = '{args.fdd[0]}'")
            for row in results:
                print("Flight ID: ", row[0])
                print("Destination ID: ", row[1])
                print("Pilot ID: ", row[2])
                print("Departure Date: ", row[3])
                print("Flight Status: ", row[4])
        elif args.pn:
            cursor.execute(f"UPDATE pilot SET pilotName = '{args.pn[1] + " " + args.pn[2]}' WHERE pilotID = '{args.pn[0]}'")
            db.commit()
            print("Confirming update...")
            results = cursor.execute(f"SELECT * FROM pilot WHERE pilotID = '{args.pn[0]}'")
            for row in results:
                print("Pilot ID: ", row[0])
                print("Pilot Name: ", row[1])
        # else:
            #print("Update Menu: \n to update pilot use: update -fp [flightID] [pilotID] \n to update destination use: update -fd [flightID] [destinationID] \n to update flight status use: update -fs [flightID] [flightStatus] \n to update flight departure date (ensure departure date is in YYYY/MM/DD format) use: update -fdd [flightID] [departureDate] \n to update pilot name (only forename and surname) use: update -pn [pilotID] [pilotForename] [pilotSurname]")

    else:
        print(intro)

if __name__ == "__main__":
    main()

# retrieve flight information based on multiple criteria such as destination, status, departure
## ?add argument for each permutation: f just for flight search, fdest for flight destination.
# done: update flight information
# done: update flight pilot
# view destination information
# update destination information
# summarise data based on destination
# summarise data based on flights per pilot
# summarise data based on departure date