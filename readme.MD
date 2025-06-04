# Three-Stage Rocket Mass Simulator

This project simulates the minimum total mass and stage breakdowns required for a three-stage rocket to deliver a payload into Low Earth Orbit (LEO) or achieve Escape Velocity. The calculations are based on derivations of the rocket equation, as detailed in the accompanying paper (see Reference section below).

## Project Structure

- [`velocity_script.py`](velocity_script.py): Core calculation script. Computes the ratios of stage and total masses relative to payload mass for a given velocity. **Do not modify this script.**
- [`data_script.py`](data_script.py): Generates total and stage masses for payloads ranging from 10,000 kg (10T) to 50,000 kg (50T), for both LEO and Escape velocities. Useful for charting and data analysis.

## User Manual

### To Generate Mass Data for Charting

Simply run [`data_script.py`](data_script.py):

```sh
python data_script.py
```

This will output the minimum total mass and stage breakdowns for payloads from 10T to 50T, for both orbital and escape velocities.

### To Calculate Masses for a Specific Velocity

If you wish to see the mass breakdown for a specific velocity and payload:

1. **Open [`velocity_script.py`](velocity_script.py).**
2. Locate the following lines near the end of the script:
   ```python
   orbital_velocity_mps = 7824
   orbital_result = calculate_rocket_masses(orbital_velocity_mps, A_kg=1)
   ...
   escape_velocity_mps = 11038
   payload_mass_kg = 227
   escape_result = calculate_rocket_masses(escape_velocity_mps, A_kg=payload_mass_kg)
   ```
3. **Change the values of `orbital_velocity_mps`, `escape_velocity_mps`, and `payload_mass_kg`** to your desired velocity (in m/s) and payload mass (in kg).
4. Run the script:
   ```sh
   python velocity_script.py
   ```
5. The script will print the minimum total engine mass and stage breakdowns for your specified parameters.

> **Note:** The formulas and ratios are based on the derivations in the accompanying paper (see Reference). The `velocity_script.py` computes ratios relative to payload mass and should not be modified.

## Reference

For the theoretical background and derivations, see the accompanying paper provided with this project.

---

**Author:**  
Bulboaca Teodor, Chircan Laurentiu-Andrei

**License:**  
MIT License

---

MIT License

Copyright (c) 2025 Bulboaca Teodor, Chircan Laurentiu-Andrei

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.