"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

speedDict = { "0-200": (15, 34), "200-400": (15, 32), "400-600": (15, 30), "600-1000": (11.428, 28), "1000-1300": (13.333, 26)}

def open_time(control_dist_km, brevet_dist_km, brevet_start_time: arrow):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if (control_dist_km <= 0):
        return brevet_start_time

    if (control_dist_km > (brevet_dist_km)):
        control_dist_km = brevet_dist_km

    if (control_dist_km <= 200):
        speed = speedDict["0-200"][1]
    elif control_dist_km <= 400:
        speed = speedDict["200-400"][1]
    elif control_dist_km <= 600:
        speed = speedDict["400-600"][1]
    elif control_dist_km <= 1000:
        speed = speedDict["600-1000"][1]
    elif control_dist_km <= 1300:
        speed = speedDict["1000-1300"][1]
    else:
        # in the case that they somehow manage to pass in an illegal distance
        # default to the longest distance maximum speed
        speed = 26

    minutes = round((control_dist_km * 60 ) / speed)
    return brevet_start_time.shift(minutes=+minutes)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if (control_dist_km <= 0):
        return brevet_start_time.shift(hours=+1)    

    if (control_dist_km <= 60):
        minutes = 60 + round((control_dist_km * 60) / 20)
        return brevet_start_time.shift(minutes=+minutes)

    if (control_dist_km > (brevet_dist_km)):
        control_dist_km = brevet_dist_km


    if (control_dist_km <= 200):
        speed = speedDict["0-200"][0]
    elif control_dist_km <= 400:
        speed = speedDict["200-400"][0]
    elif control_dist_km <= 600:
        speed = speedDict["400-600"][0]
    elif control_dist_km <= 1000:
        speed = speedDict["600-1000"][0]
    elif control_dist_km <= 1300:
        speed = speedDict["1000-1300"][0]
    else:
        # in the case that they somehow manage to pass in an illegal distance
        # default to the longest distance maximum speed
        speed = 13.333
    minutes = round((control_dist_km * 60) / speed)
    return brevet_start_time.shift(minutes=+minutes)