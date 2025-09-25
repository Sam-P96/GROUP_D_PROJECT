achv_dict = {
"co2": ["Global Warming", 0],
"rr": ["Sinful Transgression", 2],
"poker": ["Heart of The Cards", 1],
"continent": ["Sightseer", 7],
"polar": ["Polar Opposites", 1],
"defeat god": ["One Above All", 1],
"free god": ["Father's Blessing", 1],
}

player_achv = []

def achievement_check():
    if achv_dict["co2"][1] <= 0:
        achv_dict["co2"][1] = 9999999999999999999999999999999999999999999
        player_achv.append(achv_dict["co2"][0])
    if achv_dict["rr"][1] <= 0:
        achv_dict["rr"][1] = 99999999999999999999999999999999999999999999
        player_achv.append(achv_dict["rr"][0])
    if achv_dict["poker"][1] <= 0:
        achv_dict["poker"][1] = 99999999999999999999999999999999999999999999
        player_achv.append(achv_dict["poker"][0])
    if achv_dict["continent"][1] <= 0:
        achv_dict["continent"][1] = 99999999999999999999999999999999999999999999
        player_achv.append(achv_dict["continent"][0])
    if achv_dict["polar"][1] <= 0:
        achv_dict["polar"][1] = 99999999999999999999999999999999999999999999
        player_achv.append(achv_dict["polar"][0])
    if achv_dict["defeat god"][1] <= 0:
        achv_dict["defeat god"][1] = 99999999999999999999999999999999999999999999
        player_achv.append(achv_dict["defeat god"][0])
    if achv_dict["free god"][1] <= 0:
        achv_dict["free god"][1] = 99999999999999999999999999999999999999999999
        player_achv.append(achv_dict["free god"][0])

achievement_check()
print(player_achv)

# for key in achv_dict:
#     print(achv_dict[key])
# achievement_check()
# for key in achv_dict:
#     print(achv_dict[key])