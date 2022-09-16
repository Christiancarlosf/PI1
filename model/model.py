from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String
from config.db import engine, meta



drivers = Table("drivers", meta,   
                Column("driverId", Integer, primary_key=True),
                Column("driverRef", String(255)),
                Column("number", String(255)),
                Column("code", String(255)),
                Column("dob" , String(255)),
                Column("nationality", String(255)),
                Column("url", String(255)),
                Column("forename",String(255)),
                Column("surname", String(255)))


circuits = Table("circuits", meta,
                Column("circuitId", Integer, primary_key=True),
                Column("circuitRef", String(255)),
                Column("name", String(255)),
                Column("location", String(255)),
                Column("country", String(255)),
                Column("lat", String(255)),
                Column("lng", String(255)),
                Column("alt", String(255)),
                Column("url", String(255)))
               

races = Table("races", meta,
            Column("raceId",Integer, primary_key=True),
            Column("year", Integer),
            Column("round", Integer),
            Column("circuitId", Integer, ForeignKey("circuits.circuitId")),
            Column("name", String(255)),
            Column("date", String(255)),
            Column("time", String(255)),
            Column("url", String(255)))


results = Table("results", meta,
                Column("resulId",Integer, primary_key=True),
                Column("raceId",Integer,ForeignKey("races.raceId")),
                Column("driverId",Integer,ForeignKey("drivers.driverId")),
                Column("constructorId",Integer,ForeignKey("constructors.constructorId")),
                Column("number",String(255)),
                Column("grid",Integer),
                Column("position",String(255)),
                Column("positionText",Integer),
                Column("positionOrder",Integer),
                Column("points",Integer),
                Column("laps",Integer),
                Column("time",Integer),
                Column("milliseconds",Integer),
                Column("fastestLap",Integer),
                Column("rank",Integer),
                Column("fastestLapTime",Integer),
                Column("fastestLapSpeed",Integer),
                Column("statusId",Integer))


constructors = Table("constructors", meta,
                    Column("constructorId", Integer, primary_key=True),
                    Column("constructorRef", String(255)),
                    Column("name",String(255)),
                    Column("nationality",String(255)),
                    Column("url",String(255)))

meta.create_all(engine)