case = input("What is your Case? ")
motherboard = input("What is your Motherboard? ")
cpu = input("What is your CPU? ")
cpu_cooler = input("What is your CPU Cooler? ")
ram_quantity = int(input("How many used slots of RAM do you use? "))
ram = input("What is your RAM? ")
m2_quantity = int(input("How many M.2's do you use? "))
m2 = []
for i in range(m2_quantity):
    m2_name = input(f"What is your M.2? {i+1}: ")
    m2.append(m2_name)

ssd_quantity = int(input("How many SSD's do you use? "))
ssd = []
for i in range(ssd_quantity):
    ssd_name = input(f"What is your SSD? {i+1}: ")
    ssd.append(ssd_name)

hdd_quantity = int(input("How many HDD's do you use? "))
hdd = []
for i in range(hdd_quantity):
    hdd_name = input(f"What is your HDD? {i+1}: ")
    hdd.append(hdd_name)

gpu_quantity = int(input("How many GPU's do you have? "))
gpu = []
for i in range(gpu_quantity):
    gpu_name = input(f"What is your GPU? {i+1}: ")
    gpu.append(gpu_name)

fan_quantity = int(input("How many fans do you have? "))
fan = []
for i in range(fan_quantity):
    fan_name = input(f"What is your fan? {i+1}: ")
    fan.append(fan_name)

psu = input("What is your PSU? ")

monitor_quantity = int(input("How many monitors do you have? "))
monitor = []
for i in range(monitor_quantity):
    monitor_name = input(f"What is your monitor? {i+1}: ")
    monitor.append(monitor_name)

keyboard = input("What is your Keyboard? ")

mouse = input("What is your Mouse? ")

speaker = input("What is your Speaker? ")

phones = input("What is your Earphone or Headphone? ")

mic = input("What is your Microphone? ")

webcam = input("What is your webcam? ")

tp = input("Thermal Compound")

so = input("Operating System")

print(f"\nYour Desktop:")
print("")
print(f"Case: {case}")
print("")
print(f"Motherboard: {motherboard}")
print("")
print(f"CPU: {cpu}")
print("")

for i in range(ram_quantity):
    print(f"RAM {i+1}: {ram}")

print("")
for i in range(m2_quantity):
    print(f"M.2 {i+1}: {m2[i]}")

print("")
for i in range(ssd_quantity):
    print(f"SSD {i+1}: {ssd[i]}")

print("")
for i in range(hdd_quantity):
    print(f"HDD {i+1}: {hdd[i]}")

print("")
for i in range(gpu_quantity):
    print(f"GPU {i+1}: {gpu[i]}")

print("")
for i in range(fan_quantity):
    print(f"Fan {i+1}: {fan[i]}")

print("")
print(f"PSU: {psu}")

print("")
for i in range(monitor_quantity):
    print(f"Monitor: {monitor[i]}")

print("")
print(f"Keyboard: {keyboard}")

print("")
print(f"Mouse: {mouse}")

print("")
print(f"Speaker: {speaker}")

print("")
print(f"Earphones/Headphones: {phones}")

print("")
print(f"Webcam: {webcam}")

print("")
print(f"Thermal Compound: {tp}")

print("")
print(f"Operating System: {so}")

print("")
input("Press enter to exit....")
