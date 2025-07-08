# étudiez et executez le code suivant pour le comprendre
# modifiez ensuite la fonction imbriquée pour qu'on puisse changer la température d'une station
# et qu'un subscriber puisse définir une température à partir de laquelle il est notifié

def create_weather_station(localisation):
    observers = []
    temperature = 0

    def subscribe(nom_observateur, seuil_temperature):
        observers.append({
            "nom": nom_observateur,
            "seuil": seuil_temperature
        })

    def change_temperature(nouvelle_temp):
        nonlocal temperature
        temperature = nouvelle_temp
        notify()

    def notify():
        for observer in observers:
            if temperature >= observer["seuil"]:
                print(
                    f"{localisation} : Notification envoyée à {observer['nom']} (température actuelle : {temperature}°C ≥ seuil {observer['seuil']}°C)")
    return subscribe, change_temperature

quimper_subscribe, quimper_change_temp = create_weather_station("quimper")
quimper_subscribe("olivier", 30)
quimper_subscribe("pierre", 27)
quimper_subscribe("marie", 29)

quimper_change_temp(24)
# notifications non envoyées
quimper_change_temp(30)
# notifications envoyées
quimper_change_temp(32)
# notifications envoyées
