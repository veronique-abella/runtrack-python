def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60

    if heures == 0:
        if minutes_restantes == 1:
            print(f"{minutes_restantes} minute")
        else:
            print(f"{minutes_restantes} minutes")
    elif heures == 1:
        if minutes_restantes == 0:
            print("1 heure")
        elif minutes_restantes == 1:
            print("1 heure et 1 minute")
        else:
            print(f"1 heure et {minutes_restantes} minutes")
    else:
        if minutes_restantes == 0:
            print(f"{heures} heures")
        elif minutes_restantes == 1:
            print(f"{heures} heures et 1 minute")
        else:
            print(f"{heures} heures et {minutes_restantes} minutes")

time_to_text(160)