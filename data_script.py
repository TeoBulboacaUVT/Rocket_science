for a in range(10000, 50500, 5000):
    print("For orbital velocity (~7,824 m/s) with payload of " + str(a) + " kg:")
    print(f"Minimum total mass: {89.47 * a / 1000:.2f} t")
    print(f"Stage 1 mass: {70.32 * a / 1000:.2f} t")
    print(f"Stage 2 mass: {15.66 * a / 1000:.2f} t")
    print(f"Stage 3 mass: {3.49 * a / 1000:.2f} t")
    print("\n")

for a in range(10000, 50500, 5000):
    print("For escape velocity (~11,038 m/s) with payload of " + str(a) + " kg:")
    print(f"Minimum total mass: {2081.55 * a / 1000:.2f} t")
    print(f"Stage 1 mass: {1531.77 * a / 1000:.2f} t")
    print(f"Stage 2 mass: {404.22 * a / 1000:.2f} t")
    print(f"Stage 3 mass: {145.56 * a / 1000:.2f} t")
    print("\n")
