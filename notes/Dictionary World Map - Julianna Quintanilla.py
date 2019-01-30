world_map ={
    'R19A':{
        'NAME': "Wiebe's classroom",
        'DESCRIPTION': "This is the classroom that you are in right now. It has 2 exits to the north side.",
        'PATHS':{
            'NORTH': 'PARKING_LOT'
        }
    }
    'PARKING_LOT' : {
        'NAME': "The Edison Parking Lot",
        'Description': "There are cars parked here. To"
                       "the south is Mr.Wiebe's room.",
        'PATHS': {
            'SOUTH': "R19A"
        }
    }
}
