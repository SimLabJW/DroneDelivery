DRONE = {
    "ID" : [1,2,3],
    "Store" : "None",
    "Home" : "None",
    "State" : "None"
}

CAR = {
    "ID" : [1,2,3],
    "Store" : "None",
    "Home" : "None",
    "State" : "None"
}

STATE = ["STAY", "DELIVERY", "ACCIDENT", "CANCEL"]

STAY = {
    "STAY" : 40, 
    "DELIVERY" : 55, 
    "ACCIDENT" : 5, 
}

DELIVERY = {
    "DELIVERY" : 90, 
    "ACCIDENT" : 5, 
    "CANCEL" : 5
}

ACCIDENT = {
    "ACCIDENT" : 95, 
    "CANCEL" : 5
}

CANCEL = {
    "STAY" : 100
}
