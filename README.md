# AC Calculator Power and Impedance (My Own Project)

I made a calculator to calculate AC power and resistance. I used teh following formulas to calculate:

Apparent Power: S = U * I
Active (Real) Power: P = S * cos_phi
Reactive Power: Q = S * sin_phi

Total Impedance: Z = U / I
Ressistance (Active): R = Z * cos_phi
Reactance (Reactive): X = Z * sin_phi

When converting cos to sin i use this formula: sin_phi = sqrt(1 - cos_phi ** 2)

