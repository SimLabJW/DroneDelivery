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
        "STAY": {"STAY": 80, "DELIVERY": 20},
        "DELIVERY": {"DELIVERY": 99, "ACCIDENT": 0.1, "CANCEL": 0.9},
        "ACCIDENT": {"ACCIDENT": 100},
        "CANCEL": {"STAY": 100}
}
