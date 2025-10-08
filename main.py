import argparse
import sqlite3

# set up of command line interface:
def main():
    db = sqlite3.connect('airlineDb')
    print("connected to database")

    # cursor is how python interacts with sqlite3 database
    cursor = db.cursor()

    #help menus
    createMenu = "\n Create Commands: " \
    "\n to add flight: python main.py add -f [flightID] [destinationID] [pilotID] [departureDate] [flightStatus] " \
    "\n to add destination: python main.py add -d [destinationID] [destinationCity] [destinationCountry] " \
    "\n to add pilot, provide both attributes and use only Forename and Surname, use: python main.py add -p [pilotID] [pilotForename] [pilotSurname] "

    readMenu = "\n Read Commands: " \
    "\n to view by multiple criteria, use any of: view -flightID [flightID] -pilotID [pilotID] -destinationID [destinationID] -departureDate [departureDate] -flightStatus [flightStatus]" \
    "\n e.g. python main.py view -destinationID AMS -flightStatus Scheduled" \
    "\n to view summary by destination use: python main.py view -sd" \
    "\n to view summary by pilot use: python main.py view -sp" \
    "\n to view summary by departure date use: python main.py view -sdd"

    updateMenu = "\n Update Commands: " \
    "\n to update pilot, use: python main.py update -fp [flightID] [pilotID] " \
    "\n to update destination, use: python main.py update -fd [flightID] [destinationID] " \
    "\n to update flight status, use: python main.py update -fs [flightID] [flightStatus] " \
    "\n to update flight departure, date (ensure departure date is in YYYY/MM/DD format) use: python main.py update -fdd [flightID] [departureDate] "

    deleteMenu = "\n Delete Commands: " \
    "\n to delete flight, use: python main.py delete -f [flightID]" \
    "\n to delete pilot:, use: python main.py delete -p [pilotID]" \
    "\n to delete destination, use: python main.py delete -d [destinationID]"

    #parser is used to take user input
    parser = argparse.ArgumentParser(description="flight database management command line interface")
    #subparsers allow specific actions based on different user input command
    subparsers = parser.add_subparsers(dest="command", help="Available commands: Add, View, Update")
    intro = "Menu: " + createMenu + readMenu + updateMenu + deleteMenu

    # subparser to do add commands
    add_parser = subparsers.add_parser("add", help="add commands")
    add_parser.add_argument("-f", nargs=5, help="to add flight, provide all 5 attributes, use: add -f [flightID] [destinationID] [pilotID] [departureDate] [flightStatus]")
    add_parser.add_argument("-d", nargs=3, help="to add destination, provide all 3 attributes, use: add -d [destinationID] [destinationCity] [destinationCountry]")
    add_parser.add_argument("-p", nargs=3, help="to add pilot, provide both attributes and use only Forename and Surname, use: add -p [pilotID] [pilotForename] [pilotSurname]")

    # subparser to do view commands
    view_parser = subparsers.add_parser("view", help="use to view information from database")
    view_parser.add_argument("-flightID", help="flight to view")
    view_parser.add_argument("-pilotID", help="pilotID to view")
    view_parser.add_argument("-destinationID", help="destination to view")
    view_parser.add_argument("-departureDate", help="flights departing on date to view")
    view_parser.add_argument("-flightStatus", help="flight Status to view")
    view_parser.add_argument("-sd", action="store_true", help="view flights summary by destination")
    view_parser.add_argument("-sp", action="store_true", help="view flights summary by pilot")
    view_parser.add_argument("-sdd", action="store_true", help="view flights summary by departure date")


    # subparser to do update commands
    update_parser = subparsers.add_parser("update", help="update commands ")
    update_parser.add_argument("-fp", nargs=2, help="to update pilot use: update -fp [flightID] [pilotID]")
    update_parser.add_argument("-fd", nargs=2, help="to update destination use: update -fd [flightID] [destinationID]")
    update_parser.add_argument("-fs", nargs=2, help="to update flight status use: update -fs [flightID] [flightStatus]")
    update_parser.add_argument("-fdd", nargs=2, help="to update flight departure date (ensure departure date is in YYYY/MM/DD format) use: update -fdd [flightID] [departureDate]")
    update_parser.add_argument("-pn", nargs=3, help="to update pilot name (only forename and surname) use: update -pn [pilotID] [pilotForename] [pilotSurname]")

    # subparser to do delete commands

    delete_parser = subparsers.add_parser("delete", help="delete commands ")
    delete_parser.add_argument("-f", nargs=1, help="to delete flight use: delete -f [flightID]")
    delete_parser.add_argument("-p", nargs=1, help="to delete pilot use: delete -p [pilotID]")
    delete_parser.add_argument("-d", nargs=1, help="to delete destination use: delete -d [destinationID]")

    # feeds arguments in from parser
    args = parser.parse_args()
    
    #commands

    

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
            print(createMenu)

    elif args.command == "view":

        if args.sd:
            # summary by destiantion
            try:
                results = cursor.execute("SELECT destinationID,COUNT(flightID) FROM flight GROUP BY destinationID ORDER BY COUNT(flightID) DESC")
                for row in results:
                    print(row)
            except sqlite3.Error as e:
                print("Error: " + e + "\n" + readMenu)
        elif args.sp:
            #summary by pilot
            results = cursor.execute("SELECT pilotID,COUNT(pilotID) FROM flight GROUP BY pilotID ORDER BY pilotID ASC")
            for row in results:
                print(row)
        elif args.sdd:
            #summary by departure date
            results = cursor.execute("SELECT departureDate,COUNT(departureDate) FROM flight GROUP BY departureDate")
            for row in results:
                print(row)
        else: 
            try:

                # creates list of valid columns to be used in SQL query
                valid_columns = ["flightID", "pilotID", "destinationID", "departureDate", "flightStatus"]
                # creates dictionary of valid column headers from args: ignores irrelevant values like command that would be in NameSpace / none values
                filters = {key: value for key, value in vars(args).items() if key in valid_columns and value is not None}
                # creates string variable that will form basis of SQL query. ? is SQLite's placeholder and k will input the valid column name e.g. flightID
                columns =" AND ".join([f"{k}=?" for k in filters.keys()])
                # SQLite takes as list or tuple, so we convert to tuple to allow passing to SLQite3 query
                values = tuple(filters.values())
                # combining SQlite query with whatever column headers are required, based on user input 
                statement = f"SELECT * FROM flight WHERE {columns}"
                results = cursor.execute(statement, values)
                for row in results:
                    print(row)
            except:
                print(readMenu)

    elif args.command == "update":
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
        else:
            print(updateMenu)
    elif args.command == "delete":
        if args.f:
            cursor.execute(f"DELETE from flight WHERE flightID = '{args.f[0]}'")
            db.commit()
        elif args.p:
            cursor.execute(f"DELETE FROM pilot WHERE pilotID = '{args.p[0]}'")
            db.commit()    
        elif args.d:
            cursor.execute(f"DELETE from destination WHERE destinationID = '{args.d[0]}'")
            db.commit()
        else:
            print(deleteMenu)
    
    else:
        print(intro)

    db.close()

#ensures that script can run smoothly when closed and reopened
if __name__ == "__main__":
    main()