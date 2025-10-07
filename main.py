import argparse
import sqlite3

db = sqlite3.connect('airlineDb')
print("connected to database")

cursor = db.cursor()


def dbConnect():
    return sqlite3.connect('airlineDb')

# set up of command line interface:
def main():
    parser = argparse.ArgumentParser(description="flight database management command line interface")
    subparsers = parser.add_subparsers(dest="command", help="Available commands: Add, View, Update")

    # subparser to do add commands
    add_parser = subparsers.add_parser("add", help="add ")
    add_parser.add_argument("--flightID", help="flight to create")

    # subparser to do view commands
    view_parser = subparsers.add_parser("view", help="use to view information from database")
    view_parser.add_argument("--flightID", help="flight to view")

    # subparser to do update commands
    update_parser = subparsers.add_parser("update", help="update commands: -fp [flightID] [pilotID] to update pilot \n -fd")
    update_parser.add_argument("-fp", nargs=2)
    update_parser.add_argument("-fd", nargs=2)
    update_parser.add_argument("-fs", nargs=2)
    update_parser.add_argument("-fdd", nargs=2)

    args = parser.parse_args()
    print("Menu: to update pilot use: update -fp [flightID] [pilotID] \n to update destination use: update -fd [flightID] [destinationID] \n to update flight status use: update -fs [flightID] [flightStatus] \n to update flight departure date (ensure departure date is in YYYY/MM/DD format) use: update -fdd [flightID] [departure] ")
    #commands

    if args.command == "update":
        if args.fp:
            
            cursor.execute(f"UPDATE flight SET pilotID = '{args.fp[1]}' WHERE flightID = '{args.fp[0]}'")
            print(f"updated flight '{args.fp[0]}' with new pilot '{args.fp[1]}'")
            

        elif args.fd:
            
            cursor.execute(f"UPDATE flight SET destinationID = '{args.fd[1]}' WHERE flightID = '{args.fd[0]}'")
            print(f"updated flight '{args.fd[0]}' with new destination '{args.fd[1]}'")
            db.commit()
        elif args.fs:
            
            cursor.execute(f"UPDATE flight SET flightStatus = '{args.fs[1]}' WHERE flightID = '{args.fs[0]}'")
            print(f"updated flight '{args.fs[0]}' with new flight status '{args.fs[1]}'")
            db.commit()
        elif args.fdd:
            cursor.execute(f"UPDATE flight SET departure = '{args.fdd[0]}' WHERE flightID = '{args.fdd[0]}'")
            db.commit()
            results = cursor.execute(f"SELECT * FROM flight WHERE flightID = '{args.fdd[1]}'")
            for row in results:
                print("FlightID: ", row[0])
                print("Destination: ", row[1])
                print("Pilot ID: ", row[2])
                print("Departure Date: ", row[3])
                print("Flight Status: ", row[4])
            
            # print(f"updated flight '{args.fdd[1]}' with new departure date '{args.fdd[0]}'")
            # db.close()



        

    #parser.add_argument("-f","--flightNumber", type=str, help="Enter flightID of flight to amend")
    #parser.add_argument("-d","--destinationID", type=str, help="enter new destination")
    #parser.add_argument("-p","--pilotID", type=str, help="update pilot to new pilotID")
    #parser.add_argument("-dep","--departure", type=str, help="enter new departure date")
    #parser.add_argument("-fs","--flightStatus", type=str, help="enter new flight status")
    
    
    #cursor.execute(f"SELECT * FROM flight WHERE flightNumber = '{args.flightNumber}'")
    #results = cursor.fetchall()
    #for row in results:
    #    print(f"Flight Number: {row[0]}, Destination: {row[1]}, Pilot: {row[2]}, Departure: {row[3]}, Flight Status: {row[4]}")
    # print(f"Hello, {args.name}! How are you my gwee")

if __name__ == "__main__":
    main()

# retrieve flight information based on multiple criteria such as destination, status, departure
# update flight information
# update flight pilot
# view destination information
# update flight information
# 