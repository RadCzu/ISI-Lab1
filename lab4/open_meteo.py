import numpy as np
import requests
from matplotlib import pyplot as plt

# Documentation: https://open-meteo.com/en/docs/

# Weather codes for open-meteo API (for later usage)
weather_codes = {
    (0,): "czyste niebo",
    (1,): "głównie bezchmurnie",
    (2,): "częściowo pochmurno",
    (3,): "pochmurno",
    (45,): "mgła",
    (48,): "opadająca mgła szronowa",
    (51,): "mżawka lekka",
    (53,): "mżawka umiarkowana",
    (55,): "mżawka gęsta",
    (56,): "zamrażająca mżawka: lekka",
    (57,): "zamrażająca mżawka: gęsta intensywność",
    (61,): "deszcz słaby",
    (63,): "deszcz umiarkowany",
    (65,): "deszcz intensywny",
    (66,): "marznący deszcz: intensywność lekka",
    (67,): "marznący deszcz: intensywność ciężka",
    (71,): "opady śniegu: intensywność niewielka",
    (73,): "opady śniegu: intensywność umiarkowana",
    (75,): "opady śniegu: intensywność duża",
    (77,): "ziarna śniegu",
    (80,): "przelotne opady deszczu: słabe",
    (81,): "przelotne opady deszczu: umiarkowane",
    (82,): "przelotne opady deszczu: gwałtowne",
    (85,): "opady śniegu lekkie",
    (86,): "opady śniegu intensywne",
    (95,): "burza: Słaba lub umiarkowana",
    (96,): "burza z lekkim gradem",
    (99,): "burza z silnym gradem",
}

# Coordinates for few places in the format (latitude, longitude)
coordinates = {
    "Gdynia": ("54.52", "18.53"),
    "Bydgoszcz": ("53.123482", "18.008438"),
    "Radom": ("51.402658", "21.139960"),
    "Sosnowiec": ("50.286263", "19.104078"),
    "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch": ("53.221662", "-4.207674")
}

if __name__ == '__main__':
    for place in coordinates:
        weather_url = (f"https://api.open-meteo.com/v1/forecast"
                       f"?latitude={coordinates[place][0]}&longitude={coordinates[place][1]}"
                       f"&hourly=temperature_2m,rain,weather_code"
                       "&forecast_days=16"
                       "&past_days=14")

        print(f"Pogoda dla {place}: {weather_url}\n")
        place_weather = requests.get(weather_url).json()

        print (place_weather)
        temperatures = place_weather["hourly"]["temperature_2m"]
        rainfall = place_weather["hourly"]["rain"]
        dates = place_weather["hourly"]["time"]

        fig, axs = plt.subplots(1, 2, figsize=(15, 5))

        # Wykres temperatury
        axs[0].plot(dates, temperatures, label='Temperatura (°C)')
        axs[0].set_title(f'Temperatura w {place} ({place_weather["latitude"]}, {place_weather["longitude"]})')
        axs[0].set_xlabel('Data')
        axs[0].set_ylabel('Temperatura (°C)')
        n = len(dates)
        step = max(1, n // 20)  # Show only every 20th date
        axs[0].set_xticks(np.arange(0, n, step))
        axs[0].set_xticklabels([dates[i] for i in range(0, n, step)], rotation=45)
        axs[0].legend()
        axs[0].grid(True)

        # Wykres opadów
        axs[1].bar(dates, rainfall, color='blue', alpha=0.7, label='Opady (mm)')
        axs[1].set_title(f'Opady w {place} ({place_weather["latitude"]}, {place_weather["longitude"]})')
        axs[1].set_xlabel('Data')
        axs[1].set_ylabel('Opady (mm)')
        axs[1].set_xticks(np.arange(0, n, step))
        axs[1].set_xticklabels([dates[i] for i in range(0, n, step)], rotation=45)
        axs[1].legend()
        axs[1].grid(True)

        plt.tight_layout()
        plt.show()

        # Pogoda na 30 dni
        for key, value in place_weather.items():
            if key != 'hourly':
                print(f"{key}: {value}")
            else:
                for key1, value1 in value.items():
                    print(f"{key1}: {value1}")
        print("\n")
