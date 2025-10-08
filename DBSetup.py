import sqlite3

db = sqlite3.connect('airlineDb')
print("connected to database")

cursor = db.cursor()

# creating tables
cursor.execute("CREATE TABLE IF NOT EXISTS flight (flightID VARCHAR(6) PRIMARY KEY, destinationID VARCHAR(3) NOT NULL REFERENCES destination, pilotID VARCHAR(6) REFERENCES pilot, departureDate DATE NOT NULL, flightStatus VARCHAR(10) NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS pilot (pilotID VARCHAR(6) PRIMARY KEY, pilotName VARCHAR(20) NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS destination (destinationID VARCHAR(3) PRIMARY KEY, destinationCity VARCHAR(20) NOT NULL, destinationCountry VARCHAR(20) NOT NULL)")
db.commit()
# inserting flight values
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('QF3868','DEL','BBB','2025-10-05','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('KN827','CAN','RY9','2025-10-06','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('SB140','JFK','AW20','2025-10-07','Cancelled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('QF2432','AMS','CR7','2025-10-08','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('RF156','MAD','LM10','2025-12-09','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('PL908','FRA','DH18','2025-10-10','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('XG2234','SIN','MJ','2025-10-11','Delayed')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('VC4352','ICN','JPM14','2025-11-12','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('JQ273','PEK','WH19','2025-10-13','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('UN2892','BCN','DH1','2025-10-14','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('QF18','CDG','BBB','2025-10-15','In-Air')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('QF3354','SYD','RY9','2025-11-16','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('JK090','FCO','AW20','2025-10-17','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('JB007','MLE','CR7','2025-10-18','Diverted')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('FR2104','SYD','LM10','2025-10-19','Arrived')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('PL722','ATL','MW463','2026-10-20','Cancelled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('VF4','DXB','LW47','2025-12-21','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('DC243','MLE','MG6','2025-10-22','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('FR243','IST','MX5','2025-10-23','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('BA7707','LHR','YP10','2026-03-24','Delayed')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('FR99','AMS','EN9','2025-10-25','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('SL090','MAD','BS24','2025-10-26','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('LH054','FRA','DH1','2025-10-27','Scheduled')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('CP98','SIN','DM2','2025-12-28','In-Air')")
cursor.execute("INSERT OR IGNORE INTO flight VALUES ('HN7777','ICN','MG6','2025-10-29','Scheduled')")



# inserting pilot values
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('MW463','Matthew Williams')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('LW47','Luke Westmoreland')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('BBB','Benedict Bemand')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('RY9','Riya Young')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('AW20','Adam Wharton')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('CR7','Cristiano Ronaldo')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('LM10','Lionel Messi')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('DH18','Daichi Kamada')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('MJ','Michael Jackson')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('JPM14','Jean-Phillipe Mateta')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('WH19','Will Hughes')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('DH1','Dean Henderson')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('DM2','Daniel Munoz')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('MG6','Marc Guehi')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('ML5','Max Lacroix')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('CR26','Chris Richards')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('IS7','Ismail Sarr')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('YP10','Yeremy Pino')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('EN9','Eddie Nketiah')")
cursor.execute("INSERT OR IGNORE INTO pilot VALUES ('BS24','Borna Sosa')")


# inserting destination values
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('ATL','Atlanta','United States')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('DXB','Dubai','Dubai')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('DFW','Dallas','United States')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('IST','Istanbul','Turkey')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('LAX','Los Angeles','United States')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('DEL','Delhi','India')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('CAN','Guangazhou','China')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('JFK','New York','United States')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('AMS','Amsterdam','Netherlands')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('MAD','Madrid','Spain')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('FRA','Frankfurt','Germany')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('SIN','Singapore','Singapore')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('ICN','Seoul','South Korea')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('PEK','Beijing','China')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('BCN','Barcelona','Spain')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('CDG','Paris','France')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('LHR','London','United Kingdom')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('FCO','Rome','Italy')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('MLE','Malé','Maldives')")
cursor.execute("INSERT OR IGNORE INTO destination VALUES ('SYD','Sydney','Australia')")

db.commit()

# SQL Queries

# Flight Retrieval
# SELECT * FROM flight WHERE pilotID = 'MW463' AND flightStatus = 'Cancelled'
# SELECT * FROM flight WHERE destinationID = 'MLE' and departure = '2025/12/25'
# SELECT

# Flight Schedule Modification
# UPDATE flight SET flightStatus = 'Arrived' WHERE flightID = 'RF156'

# Pilot Assignment
# UPDATE flight SET pilotID = 'BBB' WHERE flightID = 'JB007'

# Destination Management
# SELECT * FROM flight WHERE destinationID = 'MLE'
# INSERT INTO destination VALUES ('LGW','London','United Kingdown')

# Data Summary
# SELECT destinationID,  COUNT(flightID) FROM flight GROUP BY destinationID SORT BY ASC
# SELECT pilotID, pilotName, COUNT(flightID) FROM flight,pilot GROUP BY destinationID
# SELECT * FROM flight WHERE departureDate = '2025/12/25'