from math import sqrt

def ac_calculator_power_impedance():
    print("AC Calculator Power Impedance")
    try:
        u = float(input("Please enter Voltage (U) in Volts [V]:"))
        i = float(input("Please enter Current (I) in Amps [A]:"))
        cos_phi = float(input("Please enter Power Factor (cos phi) between [0, 1]:"))
        if not (0 <= cos_phi <= 1):
            print("Error: Power factor must be between 0 and 1!!!")
            return
        if i == 0:
            print("Error: Current must be greater than 0!!!")
            return
        # power_calculations
        sin_phi = sqrt(1 - cos_phi**2)
        s = u * i
        p = u * i * cos_phi
        q = s * sin_phi
        # impedance_calculations
        z = u / i
        r = z * cos_phi
        x = z * sin_phi

        # output_results
        print("\n Results:Power")
        print(f"Apparent Power (S): {s:.2f} VA")
        print(f"Active Power (P): {p:.2f} W")
        print(f"Reactive Power (Q): {q:.2f} VAR")

        print("\n Results:Impedance")
        print(f"Impedance (Z): {z:.2f} Ohms")
        print(f"Resistance (R): {r:.2f} Ohms")
        print(f"Reactance (X): {x:.2f} Ohms")

    except ValueError:
        print("Error: Please enter valid numbers only!!!")

ac_calculator_power_impedance()

