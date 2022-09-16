from fastapi import APIRouter
from schema.schemas import RacesSchema, DriversSchema, CircuitsSchema,ConstructorsSchema,ResultsSchema
from config.db import engine
from model.model import drivers, circuits, constructors, races, results
from typing import List
import sqlalchemy
from sqlalchemy.sql import select

conn = engine.connect()
user = APIRouter()

@user.get("/")
def Index():
    return {"message": "Hi, welcome to my first API made by -----> Chris, with <3"}

@user.get("/races", response_model=List[RacesSchema])
def get_all_races():
  with engine.connect() as conn:
    result = conn.execute(races.select()).fetchall() 

    return result

@user.get("/races/year-w-most-races")
def get_year_with_most_races() -> dict:
    query = (
        select(
         [ races.c.year,
          sqlalchemy.func.count(races.c.year).label("race_count")
          ]
          )
          .group_by(races.c.year)
          .order_by(sqlalchemy.text("race_count desc")) ) 
    most_races = dict(engine.execute(query).first())
    query = select(races).filter_by(year=most_races["year"]) 
    most_races["races"] = engine.execute(query).fetchall() 

    return most_races

@user.get("/drivers", response_model=List[DriversSchema])
def get_all_drivers():
  with engine.connect() as conn:
    result = conn.execute(drivers.select()).fetchall() 

    return result

@user.get("/drivers/driver-w-most-1stplace")
def get_driver_with_most_wins() -> dict:
    query = (
        select(
         [ results.c.driverId.label("id"),
          sqlalchemy.func.sum(results.c.positionOrder).label("wins")
          ]
          )
          .where(results.c.positionOrder == 1)
          .group_by(results.c.driverId)
          .order_by(sqlalchemy.text("wins desc")) ) 
    
    driver = engine.execute(query).first()
    wins = driver ['wins']
    query = select(drivers).filter_by(driverId=driver["id"])
    most_first = dict(engine.execute(query).first())
    most_first['wins'] = wins 

    return most_first


@user.get("/circuits", response_model=List[CircuitsSchema])
def get_all_circuits():
  with engine.connect() as conn:
    result = conn.execute(circuits.select()).fetchall() 

    return result



@user.get("/circuits/most-raced-circuit")
def get_most_raced_circuit() -> dict:
    query = (
        select(
         [ races.c.circuitId.label("most_raced_circuit"),
          sqlalchemy.func.count(races.c.circuitId).label("times_raced")
          ]
          )
          .group_by(races.c.circuitId)
          .order_by(sqlalchemy.text("times_raced desc")) ) 
    
    most_raced = engine.execute(query).first()
    times_raced = most_raced["times_raced"]
    query = select(circuits).where(circuits.c.circuitId == most_raced["most_raced_circuit"])
    most_raced = dict(engine.execute(query).first())
    most_raced["times_raced"] = times_raced

    return most_raced


@user.get("/drivers/driver-w-most-points")
def get_driver_with_most_points() -> dict:
    query = (
        select(
          [(results.c.driverId).label("driver"),
          sqlalchemy.func.sum(results.c.points).label("most_points")
          ]
          )
          
          .group_by(results.c.driverId)
          .order_by(sqlalchemy.text("most_points desc")) ) 
    
    drivercdyp = engine.execute(query).first()
    most_points = drivercdyp["most_points"]
    query = select(drivers).where(drivers.c.driverId == drivercdyp["driver"])
    drivercdyp = dict(engine.execute(query).first())
    drivercdyp["most_points"] = most_points

    return drivercdyp

    subquery = (
        sql_select([constructors_cols.id])
        .where(constructors_cols.nationality.in_(("British", "American")))
        .subquery()
    )
#q#uery = (
   # sql_select(
       # [
           # results_cols.driverId.label("id"),
       #     sql_sum(results_cols.points).label("points_sum"),
        #]
   # )
   # .where(results_cols.constructorId.in_(subquery))
    #.group_by("driverId")
   # .order_by(sql_text("points_sum desc"))


@user.get("/drivers/driver-a-most-points")
def get_driver_with_mast_points() -> dict:
    
    subquery = (
        select([constructors.c.constructorId])
        .where(constructors.c.nationality.in_(("British", "American"))
        .subquery()   ) 
    )
    subquery = (
        select(
        [
            results.c.driverId.label("id"),
            sqlalchemy.func.sum(results.c.points).label("points_sum"),
        ]
    )   
    .where(results.c.constructorId.in_(subquery))
    .group_by("driverId")
    .order_by(sqlalchemy.text("points_sum desc")) )