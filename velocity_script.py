import numpy as np

def calculate_rocket_masses(vf_mps, A_kg, S=0.2, c_mps=2682.24):
    """
    Calculate minimum total mass and individual stage masses for a three-stage rocket.

    Parameters:
        vf_mps (float): Desired final velocity (m/s)
        A_kg (float): Payload mass (kg)
        S (float): Structural factor (default 0.2)
        c_mps (float): Exhaust speed (m/s, default 2682,24)

    Returns:
        dict: Dictionary containing total mass and individual stage masses
    """
    # Calculate common N value
    N = np.exp(vf_mps / (3 * c_mps))

    # Calculate total mass ratio
    total_mass_ratio = ((1 - S)**3 * N**3) / (1 - S * N)**3

    # Total engine mass
    M = A_kg * (total_mass_ratio - 1)

    denominator = (1 - S * N)

    # Stage 3
    M3_plus_A = A_kg * ((1 - S) * N) / denominator
    M3 = M3_plus_A - A_kg

    # Stage 2
    M2_plus_M3_plus_A = M3_plus_A * ((1 - S) * N) / denominator
    M2 = M2_plus_M3_plus_A - M3_plus_A

    # Stage 1
    M1_plus_all = M2_plus_M3_plus_A * ((1 - S) * N) / denominator
    M1 = M1_plus_all - M2_plus_M3_plus_A

    return {
        'Total Engine Mass (M)': M,
        'Stage 1 Mass (M1)': M1,
        'Stage 2 Mass (M2)': M2,
        'Stage 3 Mass (M3)': M3,
        'Mass Ratios': {
            'M1/M': M1/M,
            'M2/M': M2/M,
            'M3/M': M3/M
        }
    }

# Problem 5a and 5b: Orbital velocity (17,500 mph ≈ 7824 m/s)
orbital_velocity_mps = 7824
orbital_result = calculate_rocket_masses(orbital_velocity_mps, A_kg=1)  # Using A=1 to get masses as multiples of A
print("For orbital velocity (~7,824 m/s):")
print(f"Minimum total engine mass: {orbital_result['Total Engine Mass (M)']:.2f}A kg")
print(f"Stage 1 mass: {orbital_result['Stage 1 Mass (M1)']:.2f}A kg")
print(f"Stage 2 mass: {orbital_result['Stage 2 Mass (M2)']:.2f}A kg")
print(f"Stage 3 mass: {orbital_result['Stage 3 Mass (M3)']:.2f}A kg")
print(f"Mass ratios - Stage1: {orbital_result['Mass Ratios']['M1/M']:.1%}, Stage2: {orbital_result['Mass Ratios']['M2/M']:.1%}, Stage3: {orbital_result['Mass Ratios']['M3/M']:.1%}")

# Problem 6: Escape velocity (24,700 mph ≈ 11038 m/s) with 227 kg payload (≈ 500 lbs)
escape_velocity_mps = 11038
payload_mass_kg = 227
escape_result = calculate_rocket_masses(escape_velocity_mps, A_kg=payload_mass_kg)
print("\nFor escape velocity (~11,038 m/s) with 227 kg payload:")
print(f"Minimum total engine mass: {escape_result['Total Engine Mass (M)']:,.0f} kg")
print(f"Stage 1 mass: {escape_result['Stage 1 Mass (M1)']:,.0f} kg")
print(f"Stage 2 mass: {escape_result['Stage 2 Mass (M2)']:,.0f} kg")
print(f"Stage 3 mass: {escape_result['Stage 3 Mass (M3)']:,.0f} kg")