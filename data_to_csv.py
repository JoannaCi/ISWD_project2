import csv

# Dane
data = {
    "Sony ULT Wear": [40, 314, 110.0, 3.50, 10, 50, 255, 899.00],
    "JBL Tune 520BT": [33, 30, 102.0, 2.00, 10, 57, 157, 164.99],
    "Logitech G435": [40, 45, 83.0, 2.00, 10, 18, 165, 289.00],
    "Sony WH-CH520": [30, 101, 100.0, 1.50, 10, 50, 147, 159.00],
    "Logitech G PRO X 2 Lightspeed": [50, 38, 87.8, 2.50, 30, 50, 345, 969.00],
    "SoundCore Space Q45": [40, 16, 93.0, 2.00, 15, 65, 292, 529.00],
    "Sony WH-1000XM4B": [40, 40, 105.0, 3.00, 10, 38, 254, 1299.00],
    "Edifier W800BT Plus": [40, 32, 100.0, 3.00, 10, 50, 267, 149.00],
    "Razer Barracuda X 2022": [40, 32, 96.0, 3.00, 10, 50, 250, 399.00],
    "Sony WH-1000XM5": [30, 48, 102.0, 3.50, 10, 40, 250, 1399.00],
    "JBL Tune 770NC": [40, 32, 100.0, 2.00, 10, 70, 232, 319.00],
    "Philips Fidelio L3": [40, 16, 103.0, 1.25, 10, 38, 360, 549.00],
    "Logitech G733 Lightspeed": [40, 39, 87.5, 4.50, 20, 29, 278, 549.00],
    "Skullcandy Hesh ANC": [40, 32, 99.0, 1.21, 10, 22, 228, 419.00],
    "Philips TAH4205": [32, 32, 110.0, 2.00, 10, 29, 150, 139.00],
    "Razer BlackShark V2 HyperSpeed": [50, 32, 100.0, 1.00, 10, 70, 280, 639.00],
    "Sennheiser MOMENTUM 4 Wireless Denim": [42, 60, 106.0, 2.00, 15, 60, 293, 1299.00],
    "JBL Tune 670NC": [32, 32, 98.0, 2.00, 10, 70, 174, 338.00],
    "Razer Kraken Kitty BT V2": [40, 32, 93.0, 3.00, 10, 40, 325, 549.00]
}

# Nagłówki kolumn
headers = ["Nazwa", "g_1", "g_2", "g_3", "g_4", "g_5", "g_6", "g_7", "g_8"]

# Zapis danych do pliku CSV
with open('dane.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Nagłówki
    for product, values in data.items():
        writer.writerow([product] + values)
