
user_loc = [1,1,0]
user_loc , direction =  user_loc[:2] , user_loc[-1]
game_map = [
            [1,1,1,1],
            [1,0,0,1],
            [1,1,0,1],
            [1,1,1,1]
            ]


{0 : [-1,0] , 1 : [0,1] , 2 : [1,0] , 3 : [0 ,-1]}


def turn_left(direction):
    direct_temp = direction -1
    