co2_achv = 0
rr_achv = 0
poker_achv = 0
land_e_cont_achv = 0
antartica_achv = 0
defeat_god_achv = 0
free_god_achv = 0

achv_set = set()

def achievement_check():
    while True:
        if free_god_achv in achv_set and free_god_achv == 0:
            for key in type_bonus_dict:
                type_bonus_dict[key] *= 2
        if co2_achv in achv_list and co2_achv == 0:
            for


