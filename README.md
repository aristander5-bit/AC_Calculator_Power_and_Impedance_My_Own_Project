# AC Calculator Power and Impedance (My Own Project)

I made a calculator to calculate AC power and resistance. I used the following formulas to calculate:
  
### POWER
* Apparent Power: S = U * I
* Active (Real) Power: P = S * cos_phi
* Reactive Power: Q = S * sin_phi
* When converting cos to sin i use this formula: sin_phi = sqrt(1 - cos_phi ** 2)

### IMPEDANCE
* Total Impedance: Z = U / I
* Resistance (Active): R = Z * cos_phi
* Reactance (Reactive): X = Z * sin_phi



