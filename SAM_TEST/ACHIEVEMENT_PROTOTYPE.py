achv_dict = {
"co2": ["Global Warming", 0],
"rr": ["Sinful Transgression", 0],
"poker": ["Heart of The Cards", 0],
"continent": ["Sightseer", 0],
"polar": ["Polar Opposites", 0],
"defeat god": ["One Above All", 0],
"free god": ["Father's Blessing", 0],
}


def achievement_check():
    if achv_dict["co2"][1] <= 0:
        print("X")
        print("X")
        print("X")
        achv_dict["co2"][1] = 9999999999999999999999999999999999999999999
    if achv_dict["rr"][1] <= 0:
        achv_dict["rr"][1] = 99999999999999999999999999999999999999999999
    if achv_dict["poker"][1] <= 0:
        achv_dict["poker"][1] = 99999999999999999999999999999999999999999999
    if achv_dict["continent"][1] <= 0:
        achv_dict["continent"][1] = 99999999999999999999999999999999999999999999
    if achv_dict["polar"][1] <= 0:
        achv_dict["polar"][1] = 99999999999999999999999999999999999999999999
    if achv_dict["defeat god"][1] <= 0:
        achv_dict["defeat god"][1] = 99999999999999999999999999999999999999999999
    if achv_dict["free god"][1] <= 0:
        achv_dict["free god"][1] = 99999999999999999999999999999999999999999999


print(achv_dict["co2"][1])
achievement_check()
print(achv_dict["co2"][1])