import os
import csv
import re
import requests
from datetime import datetime


# def get coordinates from city name
def coordinates(city: str) -> tuple | None:
    resp = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1, "language": "pt", "format": "json"},
        timeout=15,
    )
    resp.raise_for_status()

    results = resp.json().get("results")
    if not results:
        return None

    local = results[0]
    state = local.get("admin1", "")
    country = local.get("country", "")
    label = (
        f"{local['name']} ({state} - {country})"
        if (state or country)
        else local["name"]
    )
    return local["latitude"], local["longitude"], label


# def fetch weather forecast
def weather(lat: float, lon: float) -> dict:
    resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_probability_max",
            ],
            "timezone": "America/Sao_Paulo",
        },
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()


# def format and display report
def report(daily_data: dict, local: str) -> list[dict]:
    dates = daily_data.get("time", [])
    min_temps = daily_data.get("temperature_2m_min", [])
    max_temps = daily_data.get("temperature_2m_max", [])
    rain = daily_data.get("precipitation_probability_max", [])

    if not dates or not min_temps or not max_temps or not rain:
        print(f"\n--- {local} ---")
        print("No weather data available")
        return []

    records = []
    for i, data in enumerate(dates):
        try:
            formatted_date = datetime.fromisoformat(data).strftime("%d/%m/%Y")
        except ValueError:
            formatted_date = data

        records.append(
            {
                "Date": formatted_date,
                "Min (°C)": min_temps[i],
                "Max (°C)": max_temps[i],
                "Rain (%)": rain[i],
            }
        )

    media = (sum(min_temps) + sum(max_temps)) / (2 * len(min_temps))
    idx_max = max(range(len(max_temps)), key=lambda i: max_temps[i])
    idx_min = min(range(len(min_temps)), key=lambda i: min_temps[i])

    print(f"\n{local}")
    print(f"Period: {records[0]['Date']} to {records[-1]['Date']}")
    print(f"Average: {media:.1f}°C")
    print(f"Max:     {max_temps[idx_max]}°C on {records[idx_max]['Date']}")
    print(f"Min:     {min_temps[idx_min]}°C on {records[idx_min]['Date']}")
    print()

    data_width = max(len(r["Date"]) for r in records)
    min_width = max(len(str(r["Min (°C)"])) for r in records)
    max_width = max(len(str(r["Max (°C)"])) for r in records)
    rain_width = max(len(str(r["Rain (%)"])) for r in records)

    header = f"{{:>{data_width}}} | {{:>{min_width}}} | {{:>{max_width}}} | {{:>{rain_width}}}".format(
        "Date", "Min", "Max", "Rain"
    )
    print(header)
    print("-" * len(header))
    for r in records:
        print(
            f"{r['Date']:{data_width}} | {r['Min (°C)']:{min_width}} | {r['Max (°C)']:{max_width}} | {r['Rain (%)']:{rain_width}}"
        )
    print()

    return records


# def export to csv
def save_csv(records, city):
    name_clean = city.strip().lower().replace(" ", "_")
    name_clean = re.sub(r"[^a-zA-Z0-9_-]", "_", name_clean)
    name = f"forecast_{name_clean}.csv"
    path = os.path.abspath(name)

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["Date", "Min (°C)", "Max (°C)", "Rain (%)"], delimiter=";"
        )
        writer.writeheader()
        for r in records:
            writer.writerow(r)

    print(f"Saved in: {path}")


# def main program loop
def main() -> None:
    print("Quick weather consultation\n")

    while True:
        city = input("Enter 'exit' to close or enter a city to continue: ").strip()

        if not city:
            continue
        if city.lower() == "exit":
            break

        try:
            results = coordinates(city)
        except requests.RequestException as e:
            print(f"Error in search: {e}")
            continue

        if results is None:
            print(f"'{city}' not found.")
            continue

        lat, lon, local = results

        try:
            dados = weather(lat, lon)
        except requests.RequestException as e:
            print(f"Error fetching forecast: {e}")
            continue

        records = report(dados["daily"], local)
        if records and input("Save CSV? (Y/N): ").strip().lower() == "y":
            save_csv(records, city)


if __name__ == "__main__":
    main()
