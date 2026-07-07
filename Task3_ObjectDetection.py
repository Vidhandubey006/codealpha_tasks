# Task 3: Object Detection Simulation  
# CodeAlpha AI Internship - June 2026

print("=== Object Detection Demo ===")
objects = ["cat", "dog", "car", "person", "bicycle"]
print("Available objects:", objects)

img = input("Enter image name: ")
import random
detected = random.sample(objects, 2)

print(f"\nScanning {img}...")
for obj in detected:
    print(f"- {obj}: {random.randint(75,99)}% confidence")