import argparse
import sqlite3
db = sqlite3.connect('airlineDb')
print("Database created")

cursor = db.cursor()

# creating tables
cursor.execute("CREATE TABLE IF NOT EXISTS flight (flightNumber VARCHAR(6) PRIMARY KEY, destinationID VARCHAR(3) NOT NULL REFERENCES destination, pilotID VARCHAR(6) REFERENCES pilot, departure DATE NOT NULL, flightStatus VARCHAR(10) NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS pilot (pilotID VARCHAR(6) PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS destination (destinationID VARCHAR(3) PRIMARY KEY, destinationCity VARCHAR(20), destinationCountry VARCHAR(20))")
db.commit()
# inserting flight values
cursor.execute("INSERT INTO flight VALUES ('QF3868','DEL','BBB','2025-10-05','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('KN827','CAN','RY9','2025-10-06','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('SB140','JFK','AW20','2025-10-07','Cancelled')")
cursor.execute("INSERT INTO flight VALUES ('QF2432','AMS','CR7','2025-10-08','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('RF156','MAD','LM10','2025-12-09','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('PL908','FRA','DH18','2025-10-10','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('XG2234','SIN','MJ','2025-10-11','Delayed')")
cursor.execute("INSERT INTO flight VALUES ('VC4352','ICN','JPM14','2025-11-12','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('JQ273','PEK','WH19','2025-10-13','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('UN2892','BCN','DH1','2025-10-14','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('QF18','CDG','BBB','2025-10-15','In-Air')")
cursor.execute("INSERT INTO flight VALUES ('QF3354','SYD','RY9','2025-11-16','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('JK090','FCO','AW20','2025-10-17','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('JB007','MLE','CR7','2025-10-18','Diverted')")
cursor.execute("INSERT INTO flight VALUES ('FR2104','SYD','LM10','2025-10-19','Arrived')")
cursor.execute("INSERT INTO flight VALUES ('PL722','ATL','MW463','2026-10-20','Cancelled')")
cursor.execute("INSERT INTO flight VALUES ('VF4','DXB','LW47','2025-12-21','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('DC243','MLE','MG6','2025-10-22','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('FR243','IST','MX5','2025-10-23','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('BA7707','LHR','YP10','2026-03-24','Delayed')")
cursor.execute("INSERT INTO flight VALUES ('FR99','AMS','EN9','2025-10-25','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('SL090','MAD','BS24','2025-10-26','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('LH054','FRA','DH1','2025-10-27','Scheduled')")
cursor.execute("INSERT INTO flight VALUES ('CP98','SIN','DM2','2025-12-28','In-Air')")
cursor.execute("INSERT INTO flight VALUES ('HN7777','ICN','MG6','2025-10-29','Scheduled')")

# inserting pilot values
cursor.execute("INSERT INTO pilot VALUES ('MW463')")
cursor.execute("INSERT INTO pilot VALUES ('LW47')")
cursor.execute("INSERT INTO pilot VALUES ('BBB')")
cursor.execute("INSERT INTO pilot VALUES ('RY9')")
cursor.execute("INSERT INTO pilot VALUES ('AW20')")
cursor.execute("INSERT INTO pilot VALUES ('CR7')")
cursor.execute("INSERT INTO pilot VALUES ('LM10')")
cursor.execute("INSERT INTO pilot VALUES ('DH18')")
cursor.execute("INSERT INTO pilot VALUES ('MJ')")
cursor.execute("INSERT INTO pilot VALUES ('JPM14')")
cursor.execute("INSERT INTO pilot VALUES ('WH19')")
cursor.execute("INSERT INTO pilot VALUES ('DH1')")
cursor.execute("INSERT INTO pilot VALUES ('DM2')")
cursor.execute("INSERT INTO pilot VALUES ('MG6')")
cursor.execute("INSERT INTO pilot VALUES ('MX5')")
cursor.execute("INSERT INTO pilot VALUES ('CR26')")
cursor.execute("INSERT INTO pilot VALUES ('IS7')")
cursor.execute("INSERT INTO pilot VALUES ('YP10')")
cursor.execute("INSERT INTO pilot VALUES ('EN9')")
cursor.execute("INSERT INTO pilot VALUES ('BS24')")

# inserting destination values
cursor.execute("INSERT INTO destination VALUES ('ATL','Atlanta','United States')")
cursor.execute("INSERT INTO destination VALUES ('DXB','Dubai','Dubai')")
cursor.execute("INSERT INTO destination VALUES ('DFW','Dallas','United States')")
cursor.execute("INSERT INTO destination VALUES ('IST','Istanbul','Turkey')")
cursor.execute("INSERT INTO destination VALUES ('LAX','Los Angeles','United States')")
cursor.execute("INSERT INTO destination VALUES ('DEL','Delhi','India')")
cursor.execute("INSERT INTO destination VALUES ('CAN','Guangazhou','China')")
cursor.execute("INSERT INTO destination VALUES ('JFK','New York','United States')")
cursor.execute("INSERT INTO destination VALUES ('AMS','Amsterdam','Netherlands')")
cursor.execute("INSERT INTO destination VALUES ('MAD','Madrid','Spain')")
cursor.execute("INSERT INTO destination VALUES ('FRA','Frankfurt','Germany')")
cursor.execute("INSERT INTO destination VALUES ('SIN','Singapore','Singapore')")
cursor.execute("INSERT INTO destination VALUES ('ICN','Seoul','South Korea')")
cursor.execute("INSERT INTO destination VALUES ('PEK','Beijing','China')")
cursor.execute("INSERT INTO destination VALUES ('BCN','Barcelona','Spain')")
cursor.execute("INSERT INTO destination VALUES ('CDG','Paris','France')")
cursor.execute("INSERT INTO destination VALUES ('LHR','London','United Kingdom')")
cursor.execute("INSERT INTO destination VALUES ('FCO','Rome','Italy')")
cursor.execute("INSERT INTO destination VALUES ('MLE','Malé','Maldives')")
cursor.execute("INSERT INTO destination VALUES ('SYD','Sydney','Australia')")

# SQL Queries

# Flight Retrieval
# SELECT * FROM flight WHERE pilotID = 'MW463' AND flightStatus = 'Cancelled'
# SELECT * FROM flight WHERE 

# Schedule Modification
#

# Pilot Assignment
# 

# Destination Management
# cursor.execute("INSERT INTO destination VALUES ('','','')")

# Data Summary
# SELECT COUNT FROM flight GROUP BY destination

# commands
def view_flights(args):
    cursor.execute()


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



    #parser.add_argument("-f","--flightNumber", type=str, help="Enter flightID of flight to amend")
    #parser.add_argument("-d","--destinationID", type=str, help="enter new destination")
    #parser.add_argument("-p","--pilotID", type=str, help="update pilot to new pilotID")
    #parser.add_argument("-dep","--departure", type=str, help="enter new departure date")
    #parser.add_argument("-fs","--flightStatus", type=str, help="enter new flight status")
    
    args = parser.parse_args()
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