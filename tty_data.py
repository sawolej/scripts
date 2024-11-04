import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import argparse

def read_serial_data(port='/dev/ttyUSB0', baudrate=9600, duration=10):
    ser = serial.Serial(port, baudrate)
    ser.flushInput()
    start_time = time.time()
    times = []
    values = []
    while (time.time() - start_time) < duration:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            try:
                value = float(line)
                current_time = time.time() - start_time
                times.append(current_time)
                values.append(value)
            except ValueError:
                pass
    ser.close()
    return times, values

def analyze_data(times, values):
    data_array = np.array(values)
    stats = {
        'średnia': np.mean(data_array),
        'odchylenie standardowe': np.std(data_array),
        'mediana': np.median(data_array),
        'minimum': np.min(data_array),
        'maksimum': np.max(data_array),
        'liczba pomiarów': len(data_array)
    }
    return stats

def plot_data(times, values):
    plt.figure(figsize=(10, 5))
    plt.plot(times, values, marker='o', linestyle='-')
    plt.xlabel('Czas [s]')
    plt.ylabel('Wartość')
    plt.title('Dane w funkcji czasu')
    plt.grid()
    plt.show()

parser = argparse.ArgumentParser(description="Zbieranie danych z portu szeregowego przez określony czas")
parser.add_argument('-S', type=int, help="Czas zbierania danych w sekundach", required=True)
args = parser.parse_args()

port = '/dev/ttyUSB0'
duration = args.S

times, values = read_serial_data(port=port, duration=duration)
stats = analyze_data(times, values)

print("Statystyki zebranych danych:")
for key, value in stats.items():
    print(f"{key}: {value}")

plot_data(times, values)
