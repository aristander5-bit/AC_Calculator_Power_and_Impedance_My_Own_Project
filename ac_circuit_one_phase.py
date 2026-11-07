from math import sqrt


class ACCircuit:
    def __init__(self, voltage: float, current: float, cos_phi: float):
        if not (0 <= cos_phi <= 1):
            raise ValueError("Power factor must be between 0 and 1.")
        if voltage <= 0 or current <= 0:
            raise ValueError("Voltage and Current must be greater than 0.")

        self.u = voltage
        self.i = current
        self.cos_phi = cos_phi
        self.sin_phi = sqrt(1 - cos_phi ** 2)

    @property
    def apparent_power(self):
        return self.u * self.i

    @property
    def active_power(self):
        return self.apparent_power * self.cos_phi

    @property
    def reactive_power(self):
        return self.apparent_power * self.sin_phi

    @property
    def impedance(self):
        return self.u / self.i

    @property
    def resistance(self):
        return self.impedance * self.cos_phi

    @property
    def reactance(self):
        return self.impedance * self.sin_phi

    def display_results(self):
        print("\n=== Power Results ===")
        print(f"Apparent Power (S): {self.apparent_power:.2f} VA")
        print(f"Active Power (P): {self.active_power:.2f} W")
        print(f"Reactive Power (Q): {self.reactive_power:.2f} VAR")

        print("\n=== Impedance Results ===")
        print(f"Impedance (Z): {self.impedance:.2f} Ohms")
        print(f"Resistance (R): {self.resistance:.2f} Ohms")
        print(f"Reactance (X): {self.reactance:.2f} Ohms")

try:
    u_input = float(input("Enter Voltage (U) [V]: "))
    i_input = float(input("Enter Current (I) [A]: "))
    cos_input = float(input("Enter Power Factor (cos phi): "))

    circuit = ACCircuit(u_input, i_input, cos_input)
    circuit.display_results()

except ValueError as e:
    print(f"Error: {e}")
