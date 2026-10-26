---
title: "Part 3 · Chapter 4: Rocket Construction & Lightweight Design"
description: "Yu. V. Kondratyuk's \"Conquest of Interplanetary Space\" (1929), Chapter 4: Combustion chamber and nozzle design, regenerative cooling, and high-temperature thermal protection."
---

# Chapter 4 · Rocket Construction & Lightweight Design
### Section IV. The Combustion Process, Construction of Chamber and Nozzle
**By Yuriy Vasil'yevich Kondratyuk**  
*(From NASA TT F-9285, pp. 72–73 / Original work, pp. 16–18)*

---

## Physical Processes in the Combustion Chamber & Efficient Atomization

To ensure that the chemical reaction heat of high-energy propellants is converted into directed expansion thrust with maximum efficiency, the design of the combustion chamber must satisfy three stringent fluid dynamic criteria:
1. **Complete Molecular-Scale Atomization**: Liquid fuel and oxidizer injected into the chamber must break up and atomize into uniform droplet clouds on the scale of micrometers within microsecond intervals;
2. **Adequate Residence and Evaporation Time**: The chamber volume must ensure that droplets fully absorb radiative heat from surrounding high-temperature combustion gases, undergo phase-change vaporization, and diffuse uniformly before being swept out through the throat by the high-speed gas stream;
3. **Suppression of Low- and High-Frequency Combustion Instabilities**: Preventing localized acoustic and detonation pressure oscillations from inflicting catastrophic resonance destruction on the chamber walls.

Impinging injector arrays at the chamber injector dome utilize fluid collision momentum to rapidly form intermeshing annular or sheet-like fine atomization films, thereby significantly minimizing the required characteristic chamber length ($L^*$).

---

## Profile Design of the De Laval Expansion Nozzle

As high-pressure gases from the combustion chamber pass through the critical throat section into the supersonic expansion section, the geometric contour of the nozzle directly governs the kinetic energy conversion efficiency.

Along the nozzle axis, the cross-sectional area must satisfy the one-dimensional steady isentropic compressible area-Mach relation:
$$\frac{F}{F_{\text{crit}}} = \frac{1}{\text{Ma}} \cdot \left[\frac{2}{\kappa + 1} \left(1 + \frac{\kappa - 1}{2} \text{Ma}^2\right)\right]^{\frac{\kappa + 1}{2(\kappa - 1)}}$$

where:
* $F_{\text{crit}}$ is the critical throat cross-sectional area;
* $F$ is the local cross-sectional area;
* $\text{Ma}$ is the local flow Mach number;
* $\kappa$ is the isentropic specific heat ratio of the combustion gas.

Downstream of the throat, the inner nozzle wall should follow a smooth **paraboloid of revolution** or bell contour:
* The parabolic contour ensures that as expanding exhaust gases approach the nozzle exit plane, boundary streamlines are smoothly deflected parallel to the longitudinal axis of the rocket, thereby suppressing radial divergence thrust losses to within $1\% \sim 2\%$;
* The nozzle expansion area ratio ($\frac{F_{\text{exit}}}{F_{\text{crit}}}$) must be adapted to the ambient atmospheric backpressure. For upper stages operating in the cosmic vacuum, the expansion ratio should be expanded as widely as practicable to extract every joule of pressure work; for booster stages operating at sea level, the expansion ratio must prevent severe overexpansion, boundary layer separation flutter, and acoustic side loads.

---

## Regenerative Cooling of Combustion Chamber and Nozzle Walls

During intense propellant combustion, core flame temperatures within the chamber routinely reach **$2500^\circ\text{C} \sim 3500^\circ\text{C}$**, temperatures far exceeding the melting points of any conventional structural metals (such as copper, steel, or nickel).

To overcome this formidable thermal barrier, Kondratyuk developed and refined the modern architecture of **double-jacket liquid regenerative cooling**:
* The entire combustion chamber and thrust nozzle are constructed with **concentric double-walled thin metallic shells**, separated by narrow high-velocity cooling channel jackets;
* Cryogenic liquid propellant (such as liquid hydrogen, liquid methane, or kerosene), prior to injection into the combustion head, **is forced through the dual-jacket channels enveloping the outer nozzle and chamber walls**;
* The high-velocity coolant absorbs enormous convective and radiative heat flux conducted through the inner metal liner, maintaining the metal temperature well below structural creep and yield limits (typically $600^\circ\text{C} \sim 800^\circ\text{C}$);
* Simultaneously, the propellant absorbs this thermal energy, undergoes preheating and supercritical vaporization, and enters the combustion chamber in a superheated state, **recovering 100% of wall thermal losses directly back into the engine's thermodynamic power cycle**!

This regenerative liquid cooling architecture eliminated the crude reliance on heavy refractory brick linings, boosting rocket engine thrust-to-weight ratios by orders of magnitude and becoming the permanent, unshakeable standard of liquid rocket propulsion.
