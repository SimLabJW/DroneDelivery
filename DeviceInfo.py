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

TRANSITIONS = {
        "STAY": {"STAY": 40, "DELIVERY": 60},
        "DELIVERY": {"DELIVERY": 96, "ACCIDENT": 2, "CANCEL": 2},
        "ACCIDENT": {"ACCIDENT": 100},
        "CANCEL": {"STAY": 100}
}
