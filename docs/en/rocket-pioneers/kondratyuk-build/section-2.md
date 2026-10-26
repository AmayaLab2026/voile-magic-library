---
title: "Part II · Section 2: Orbital Ascent, Physiological Protection & Advanced Propellants"
description: "Yuri Kondratyuk, \"To Whomsoever Will Read in Order to Build\" (1918–1919), Section 2: Horizontal orbital ascent, physiological protection via liquid immersion, and cathode-ray (ion) propulsion concepts."
---

# Section 2 · Orbital Ascent, Physiological Protection & Advanced Propellants
### Orbital Ascent, Physiological Protection & Advanced Propellants
**Yuri Vasilievich Kondratyuk**  
*(From NASA TT F-9285, pp. 23–27 / Russian Manuscript, pp. 508–514)*

---

## Second Method of Flight (Tangential Orbital Ascent) and Its Formula

The **second method of flight** consists of imparting to the vehicle an actual acceleration directed approximately **perpendicular to the geocentric radius vector** (that is, parallel to the tangent to the Earth's surface); during return braking, a deceleration is likewise applied tangentially, allowing the vehicle to glide smoothly into near-Earth orbit (see Figure 1).

![Tangential acceleration vector diagram for the second method of flight (Figure 1)](/images/rocket-pioneers/build-fig1.png)  
*Figure 1*

According to the parallelogram rule of acceleration vectors, if we impart a resultant thrust acceleration to the spacecraft such that, when vectorially added to the local gravitational acceleration, the net resultant acceleration is strictly perpendicular to the radial direction toward the Earth's center, the effective acceleration is:
$$a_{\text{eff}} = \sqrt{k^2 j^2 - j^2} = j \sqrt{k^2 - 1}$$

In the initial stage of applying such tangential acceleration, the velocity-generating work capacity of the active propellant is degraded by only a relatively minor factor:
$$\frac{k}{\sqrt{k^2 - 1}}$$

What is especially critical is that **this degradation occurs only at the very inception of the launch acceleration**!

As the tangential orbital velocity climbs rapidly and the centrifugal acceleration continuously intensifies, this ratio approaches $1$ with extraordinary speed (the ideal state of zero gravitational loss). When the circular orbital velocity reaches the point where centrifugal acceleration surpasses the local gravitational acceleration $j$, the spacecraft naturally transitions into an **elliptical orbit** around the Earth.

Thereafter, we need only apply subsequent thrust impulses precisely at specific characteristic points of the elliptical orbit (namely, near the two ends of the major orbital axis where the velocity vector is strictly perpendicular to the radius vector, i.e., at perigee and apogee), where the effective propellant work factor is exceedingly close to $1$. The return flight follows precisely the same orbital maneuvering principles.

Since I cannot perform the complete, intricate numerical integration of the orbit here, I shall substitute the penalty factor $\frac{k}{\sqrt{k^2 - 1}}$ corresponding to the worst-case initial condition into the mass equation. While this coefficient is far more conservative than the true integrated efficiency factor over the entire acceleration course, it already offers an **incomparable, overwhelming advantage** over the direct vertical ascent of the first method: even for modest thrust ratios $k$, the factor $\frac{k}{\sqrt{k^2 - 1}}$ remains exceedingly close to $1$.

This yields the rocket mass formula for the second method of flight:
$$M = m \cdot e^{\frac{k}{\sqrt{k^2 - 1}} \sqrt{\frac{rj}{p}}}$$

![Orbital ascent trajectory of the second method of flight (Figure 2)](/images/rocket-pioneers/build-fig2.png)  
*Figure 2*

Figure 2 illustrates the flight path of the spacecraft gradually accelerating tangentially to Earth, progressively transitioning into an elliptical parking orbit, and ultimately escaping the Earth's gravitational field.

As is evident, while the second method is far more intricate in terms of navigation, attitude control, and guidance algorithms, the quantity of active propellant it consumes is **substantially reduced** (especially in the realistic engineering regime where $k$ is not exceptionally large, e.g., $k \approx 20$).

> **Author's Original Note**: In the presence of a significant gravitational field, the universally valid basic mechanical rule is always: **the more perpendicular the direction of thrust acceleration is relative to the direction of gravity, the more economical and efficient the propellant utilization** (naturally keeping in mind that optimal tangential thrust acceleration should always remain parallel to the instantaneous velocity vector already possessed by the vehicle). The second method of flight is the consummate application of this mechanical principle (see Note 4 at the end of the text).

---

## A Revolutionary Scheme to Elevate Human Physiological Overload Tolerances

As demonstrated in the preceding derivation, the limited tolerance of the human body to acceleration loads constitutes a severe inert weight penalty in the rocket mass formula (particularly in direct vertical launch schemes). We shall now examine, from the fundamentals of hydrostatics and biomechanics, the underlying physical causes of human vulnerability to g-forces, and propose an effective engineering solution to overcome them.

The human body's inability to withstand high mechanical accelerations stems from:
1. **The ultimate compressive mechanical strength limits of the skeleton and connective tissues**;
2. **The presence of large volumes of mobile fluid tissues (blood, lymph, etc.) throughout the body**;
3. **The pronounced disparities in absolute density among various internal organs and anatomical structures**.

It is common knowledge that when a person falls from a height and impacts the ground, their bones fracture instantaneously because the structural tissues cannot withstand the colossal deceleration impact force imposed by the ground.

Furthermore, if a human remains for an extended period in an unnatural posture (such as hanging upside down), or more visibly, is subjected to high-speed rotation on a centrifuge, the centrifugal acceleration forces blood to rush massively toward the head or the lower extremities, resulting in cerebral ischemia, syncope, or severe vascular rupture.

Even if an astronaut reclines horizontally on a flat bed to prevent steep longitudinal blood shifts, when the transverse acceleration reaches $10\ g$, the cosmonaut's effective body weight is abruptly multiplied tenfold. The skeletal prominences of the back in direct contact with the rigid surface will endure extreme local pressure concentrations, causing severe tissue bruising, displacement of internal organs, and agonizing respiratory distress.

Addressing these physiological failure mechanisms, **the definitive physical remedy to withstand extreme g-loads is: to immerse the cosmonaut's body entirely in a specialized bath filled with a liquid of density exactly equal to the average density of the human body!**

![Astronaut anti-overload liquid immersion tank (Figure 3)](/images/rocket-pioneers/build-fig3.png)  
*Figure 3*

Figure 3 depicts the operational concept of this **anti-overload liquid immersion chamber**:
* The chamber is filled with an inert liquid whose density is finely calibrated to match human tissue;
* The acceleration is applied in the direction indicated by the arrow in the figure (transversely across the astronaut's body);
* In this immersed state, according to Archimedes' principle of hydrostatic buoyancy, the opposing hydrostatic pressure exerted by the surrounding fluid on the surface of the body microscopically balances and neutralizes the inertial gravitational load generated within the body tissues at every point!
* External structural support pressure is no longer concentrated upon one or two skeletal contact points, but is distributed with perfect uniformity and gentleness across the entire projected surface area of the human body.

To prevent the immersion fluid from entering the cosmonaut's body cavities, the astronaut must wear specialized pressure-resistant goggles, earplugs, and a breathing mask connected to an external oxygen system. The breathing gas pressure inside the mask must be regulated via automatic pressure-reducing valves to match the local hydrostatic fluid pressure exerted at the chest level, thereby ensuring that the chest cage can expand and contract effortlessly for normal respiration even under colossal acceleration loads.

By adopting this hermetic liquid immersion method, the mechanical overload endurable by the human body will no longer be limited to a few $g$'s, but can safely leap to **$20\ g$ or even $30\ g$** and higher! This physiological breakthrough directly compresses the duration of the powered boost phase by several-fold, thereby diminishing gravitational losses to a virtually negligible magnitude.

---

## On Other Conceivable Reactive Devices

### 1. Mechanical Reaction Devices (Coiled Steel Wire Recoil Launcher)
A mechanical reaction device might consist of a spool of steel wire whose hub is connected to a crew compartment. If we impart a sudden, rapid rotational acceleration to the spool (in the direction opposite to the wire winding) and then release the free end of the wire, the wire will fly off tangentially in one direction around the circumference, while the spool with the cabin will recoil in the opposite direction (Figure 4).

![Schematic diagram of the coiled steel wire recoil mechanical reaction device (Figure 4)](/images/rocket-pioneers/build-fig4.png)  
*Figure 4: Coiled Steel Wire Recoil Device*

Such devices are utterly unsuited for launch from Earth, because even a spool manufactured from the highest grade alloy steel cannot withstand a peripheral tangential linear speed exceeding approximately $300\ \text{m/s}$ (an absolute speed, independent of radius); beyond this velocity, the spool will rupture under centrifugal forces. Because the achievable velocity is so meager, to attain escape velocity the device would have to be colossal: the required ratio of launch mass to empty payload mass would reach approximately $M = m \cdot 55^{10}$.

### 2. Reactive Propulsion via Expulsion of Matter Streams (Cathode-Ray Propulsion)
Cathode rays consist of charged subatomic particles possessing mass, traveling at velocities up to $200,000\ \text{km/s}$. Consequently, they are capable of exerting a corresponding reaction force or recoil, which can be harnessed provided a sufficient beam intensity is generated. Their drawback lies in the staggering expenditure of energy required, with particle velocities far in excess of practical needs; the higher the exhaust velocity, the greater the energy that must be dissipated to generate a given thrust, accompanied by the useless accumulation of strong high-potential electric charges. However, if these rays are passed through an anode grid to strip them of excess velocity and charge, recovering the heat liberated during deceleration, energy dissipation could potentially be mitigated.

---

## Selection of Active Propellants and Chemical Propulsion Limits

Chemical substances intended to supply reactive propulsive power to a rocket must satisfy requirements of extremely high specific energy (calorific value per unit mass) and high exhaust velocity.

From the standpoint of chemical thermodynamics, the most efficient chemical propellant combination currently known is undeniably **the combustion of liquid hydrogen and liquid oxygen** ($\text{H}_2 + \text{O}$). Hydrogen burning in oxygen produces superheated high-pressure water vapor, with a heat of reaction reaching approximately $3300\ \text{cal/g}$. Water vapor consists of low-molecular-weight molecules capable of converting thermal energy into extremely high characteristic exhaust velocities during adiabatic nozzle expansion.

Beyond liquid hydrogen, certain high-energy light metals and their hydrides (such as metallic lithium, beryllium, boron, and light hydrocarbons) combined with liquid oxygen or liquid ozone theoretically contain immense combustion energies.

Nevertheless, regardless of how chemical fuels are optimized, their exhaust velocity remains fundamentally bounded by the molecular binding energy released during chemical bond dissociation and recombination, imposing an upper theoretical limit on exhaust velocity in the range of several kilometers per second (approximately $4000 \sim 5000\ \text{m/s}$).

In view of this ceiling, Kondratyuk advanced in this manuscript an epochal concept: **deep-space electric propulsion and cathode-ray (electron/ion stream) reactive propulsion**:

Suppose that instead of relying on traditional chemical combustion, we employ an electrostatic acceleration apparatus powered by high-voltage electrical energy to ionize the atoms of the propellant working fluid, accelerating them across an intense electrostatic field as a high-energy **cathode ray (high-speed electron or ion stream)** expelled backward at tremendous velocity!

Because charged particles accelerated by strong electrostatic fields can effortlessly achieve exhaust velocities of tens of thousands of kilometers per second, approaching the speed of light in vacuum ($c \approx 300,000\ \text{km/s}$):
* According to momentum conservation $m \cdot \Delta V = m_{\text{prop}} \cdot c$;
* Elevating the exhaust velocity $c$ by several orders of magnitude allows the propellant mass consumption $m_{\text{prop}}$ required to reach cosmic velocities to shrink to an almost negligible fraction!
* The spacecraft is completely freed from the crushing inert mass of mammoth propellant tanks, enabling high-speed deep-space voyages approaching relativistic speeds, which could be utilized to empirically test Einstein's relativistic effects across cosmic distances!

The immense electrical energy required to operate such a particle beam thruster would not require hauling heavy generator fuel through space; instead, it could be continuously drawn directly from the inexhaustible **solar radiant energy** permeating interplanetary space—collected and concentrated by ultra-light space mirrors to generate power (as explored in detail in Section 6) (see Note 6 at the end of the text).
