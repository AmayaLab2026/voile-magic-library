---
title: "Part 3 · Chapter 9: Dissipation of Return Velocity Using Atmospheric Drag"
description: "Yu. V. Kondratyuk's \"Conquest of Interplanetary Space\" (1929), Chapter 9: Aerodynamic glider design, controlled multi-pass aerobraking, ceramic corundum heat tile radiative equilibrium, and analytical derivation of orbital decay."
---

# Chapter 9 · Dissipation of Return Velocity Using Atmospheric Drag
### Section IX. Dissipation of Return Velocity by Atmospheric Drag
**By Yuriy Vasil'yevich Kondratyuk (Yu. V. Kondratyuk)**  
*(From NASA TT F-9285, pp. 102–115 / Original work, pp. 57–73)*

---

Upon returning to Earth, we must reduce the rocket's relative velocity to zero; consequently, atmospheric resistance will always be extraordinarily advantageous to us. Our sole objective is to determine how to utilize this resistance most rationally and effectively while traversing the atmosphere at velocities of several kilometers per second, without allowing the vehicle to be destroyed by intense aerodynamic heating.

Atmospheric resistance can be applied in two distinct ways:
1. **Dissipating the entire return velocity** $w_v = 11,185\ \text{m/s}$; or
2. **Dissipating only the so-called "circular orbital velocity"**, namely $w_c = 7909\ \text{m/s} + \beta$ (where $\beta$, in the present absence of reliable empirical measurements of the upper atmosphere, represents an uncertainty on the order of tens of meters per second).

The second method is technically much simpler to implement; we shall therefore first examine the process of dissipating this latter portion of velocity (i.e., $7909\ \text{m/s} + \beta$).

---

## I. Transition to Circular Orbit and Glider Landing Craft Configuration (Figure 7)

We establish the following initial operating assumptions:

The rocket approaches Earth along a parabolic or elongated elliptical trajectory whose vertex (closest approach to the Earth's center) lies at an altitude of $400 \sim 600\ \text{km}$ above the Earth's surface. The precise altitude depends upon the precision with which we can control the vehicle's flight vector; we must ensure not only that the rocket does not crash uncontrollably into Earth, but also that it does not disintegrate in the dense lower atmosphere under prohibitive deceleration loads or thermal shock.

Subsequent orbital transition proceeds according to tangential ballistic principles, in an operational sequence exactly inverse to the launch profile depicted in Figure 1. As soon as the rocket reaches the orbital arc closest to Earth, it applies a retro-thrust impulse to decelerate and transition into a circular orbit tangent to the preceding trajectory at that point. The velocity decrement required for this retro-braking maneuver is given by:

$$\beta = \sqrt{\frac{2 R^2 g}{r}} - \sqrt{\frac{R^2 g}{r}} = (\sqrt{2} - 1)\sqrt{\frac{R^2 g}{r}}$$

where $r$ is the radius of the circular orbit from the Earth's center. Assuming $r = R + 500\ \text{km} = 6870\ \text{km}$, we calculate the required braking velocity decrement to be:

$$\beta \approx 3150\ \text{m/s}$$

Following insertion into circular orbit, the rocket coasts along this trajectory outside the atmosphere, with an orbital period of approximately 1.5 hours per revolution. During this interval, the rocket must be assembled and reconfigured into a specialized aerodynamic gliding landing vehicle (Figure 7).

![Vehicle for dissipating return velocity by atmospheric drag (Figure 7)](/images/rocket-pioneers/space-fig7.png)  
*Figure 7: Schematic structural diagram of the vehicle for dissipating return velocity by atmospheric resistance (Figure 7)*

This craft consists of the following primary components:
1. **Main rocket fuselage**;
2. **Lifting surface (wing)**: An elliptical lifting surface possessing an elongated longitudinal major axis, rigidly and firmly joined to the central fuselage;
3. **Twin inclined empennage (V-tail)**: Arranged in a dihedral configuration with an included dihedral angle of approximately $90^\circ$, its edges positioned perpendicular to the flight path, with its plane of symmetry parallel to the trajectory;
4. **Lateral roll auto-stabilizing vane**: Featuring a folded-angle surface geometrically similar to the empennage section but with a narrower angle (about $45^\circ$), mounted above the crew cabin, its leading apex edge aligned perpendicular to both the trajectory and the tail surfaces.

This stabilizing vane is actuated along its folding edge by a gyroscopic mechanism located within the cockpit, pivoting to the left or right to automatically preserve the lateral attitude of the vehicle. Prior to launch, the primary axis of the gyroscope is pre-aligned and locked parallel to the Earth's axis of rotation. During high-velocity flight in an extremely rarified atmosphere, pure aerodynamic stability alone is unlikely to guarantee lateral trim; hence, an automatic servo control surface referenced to a gyroscopic baseline is indispensable.

All the aforementioned external aerodynamic surfaces must be stored in a disassembled, folded state inside internal compartments during Earth launch and interplanetary transit; they are deployed and assembled in space only when the orbit (or its perigee arc) is about to intercept atmospheric layers of sensible density.

A gliding vehicle possessing this configuration—differing essentially from a conventional glider by its much larger angle of attack, specialized heat-resistant tail structure, and dedicated gyroscopic roll stabilization—exhibits a unique flight characteristic: it will automatically maintain itself in an atmospheric density layer where, at the given altitude and instantaneous flight velocity, the vertical component of aerodynamic lift precisely balances the apparent weight of the vehicle. In other words, the excess $K$ of gravitational attraction over the centrifugal force generated along the circular arc is exactly counterbalanced by aerodynamic lift:

$$K = g M \left(1 - \frac{2 v_1^2}{w_c^2}\right) \quad (38)$$

(assuming the vehicle executes an approximately horizontal glide along a great circle arc of the Earth).

---

## II. Great-Circle Horizontal Gliding and Altitude-Velocity Equilibrium Profile (Figure 8)

As the vehicle's velocity decreases continuously under the sustained retarding action of atmospheric drag, it sinks gradually and automatically into denser atmospheric layers, preserving the exact dynamic equilibrium between aerodynamic lift and apparent weight.

Assume the vehicle performs its return gliding entry in the equatorial plane from west to east, aligned with the direction of Earth's rotation (where the relative atmospheric velocity with respect to the Earth's center is $v_1 = v - U$), and that the wing loading per unit surface area is $p\ \text{kg/m}^2$. Applying equations (15) and (38), we formulate the aerodynamic force equilibrium equation per unit area:

$$p \left(1 - \frac{2 v_1^2}{w_c^2}\right) = A c k_1 v_1^2 \quad (39)$$

where:
* $c$ is a function of the lifting surface inclination (angle of attack $\alpha$);
* The left-hand side represents the apparent weight of the vehicle supported per square meter of lifting surface;
* The right-hand side represents the vertical component of atmospheric drag (effective aerodynamic lift) generated per square meter of wing area;
* $A = \rho_h / \rho_0$ is the ratio of atmospheric density at altitude $h$ to standard sea-level density.

Based on equation (39), selecting representative parameter values $p = 200\ \text{kg/m}^2$, $c = 0.7$ (corresponding to an angle of attack $\alpha \approx 40^\circ$), and setting the drag constant $k_1 = 1$ (given the absence of empirical fluid data at such extreme hypersonic speeds, we intentionally choose a smaller, highly conservative value that yields the least favorable aerodynamic deceleration conditions). Coupling this with the atmospheric density profile (equation 17), the functional curve relating flight altitude to velocity, $h = F(v_1)$, is computed and plotted in Figure 8:

![Gliding descent altitude versus velocity curve (Figure 8)](/images/rocket-pioneers/space-fig8.png)  
*Figure 8: Equilibrium gliding deceleration altitude-velocity curve $h = F(v_1)$ (Figure 8)*  
*(Numbers indicated along the curve designate the atmospheric density ratio $A = \rho_h / \rho_0$ corresponding to horizontal velocity $v_1$; altitude $h$ is computed from the density ratio via equation 17)*

In Figure 8, the low-speed regime where $v_1 < 1000\ \text{m/s}$ has been omitted, as aerodynamic gliding in this subsonic regime is of negligible consequence to the high-altitude orbital deceleration process.

---

## III. Severe Aerodynamic Heating and Radiative Cooling Equilibrium of Refractory Ceramic Tiles

As the craft glides and descends through the atmosphere at hypersonic velocities of several kilometers per second, it is vital to guarantee that the thermal energy radiated outward into space per unit time by the vehicle is no less than the heat transferred to the airframe by the incandescents shock-compressed air volume ahead.

Owing to the paucity of empirical data on flow phenomena around bodies moving at extreme hypersonic velocities, as well as the absence of accurate measurements of gaseous radiative emission at several thousand degrees, a closed-form analytical solution for this heat exchange cannot yet be definitively formulated.

However, according to the Stefan-Boltzmann law of thermal radiation, radiant flux emitted by a body is proportional to the fourth power of absolute temperature ($T^4$). Therefore, the heated structural surfaces supporting the aerodynamic loads—first and foremost the lifting wings—must possess the highest degree of refractory heat resistance, even if this entails an increase in structural surface density $p$.

For the load-bearing empennage and stabilizing control surfaces, the most rational and feasible engineering design is configured as follows:
* **Primary metallic structural framework**: Constructed from high-temperature alloys;
* **External heavy refractory tile cladding**: Densely tiled with plates or bricks fabricated from high-melting-point refractory materials, such as **graphite**, **retort carbon**, **high-purity limestone**, or **specialized porcelain/ceramics**;
* These refractory tiles must be arrayed on the forward windward face of the framework, completely shielding the underlying metallic spars from direct aerodynamic impingement;
* Metallic structural components in direct contact with the refractory tiles should be manufactured from refractory metals; the supporting skeleton can be constructed from high-strength seamless steel tubing, cooled internally by circulating water and steam (the hazardous high-heat phase of gliding reentry lasts no more than 20 minutes), while an internal ceramic insulation blanket lines the underside of the refractory tiles to prevent conductive and radiative transfer into the interior structure.

When incandescent gas streams sweep over the airframe at several kilometers per second, the time during which any individual air parcel remains in contact with the forward surface during the critical high-heating phase is extraordinarily fleeting—**not exceeding 0.002 seconds**. During this fleeting contact, the compressed air parcel can radiate away only a small fraction $q$ of the total thermal energy $Q$ accumulated through adiabatic compression.

Accordingly, the upper limit of aerodynamically absorbed radiant heat flux received per square meter of lifting surface per unit time satisfies:

$$q Q_1 < 1.5\, p\, q \times 10^{11}\ \text{erg/s} \quad (40)$$

According to the Stefan-Boltzmann law, the radiant emission of an absolute blackbody surface is $0.57 \times 10^{-4} T^4\ \text{erg/s}$ per square meter. Treating the surface as an absolute blackbody is fully justified here, since in our heat absorption derivation we already assumed that the lifting surface absorbs all incident radiation; the emissivity coefficient affects absorption and radiation in equal measure and thus does not alter the thermodynamic balance.

Adopting a representative structural areal density $p = 200\ \text{kg/m}^2$, and assuming the peak compressed air temperature reaches $T_1 = 3000\ \text{K} = 2730^\circ\text{C}$ (approaching the maximum theoretically conceivable limit), calculations indicate:
* The self-emitted thermal radiation power directed outward (into both upper and lower hemispheres) from each square meter of lifting surface can reach $9.2 \times 10^{13}\ \text{erg/s}$;
* Meanwhile, the incident thermal flux actually absorbed by the lifting surface (per equation 40) does not exceed $3 \times 10^{13} q\ \text{erg/s}$.

Referring to proven engineering facts: in modern internal combustion engine cylinders, where burning gases remain in contact with cylinder walls for approximately $0.1\ \text{s}$, the gas transfers only about half of its heat to the walls. In our gliding flight, the contact duration of high-temperature air with the surface does not exceed $0.002\ \text{s}$ (more than 50 times shorter than in an engine cylinder). There are thus solid grounds to conclude that the actual heat absorption fraction $q$ will not exceed a few hundredths ($q < 0.01$).

This provides an immense thermal safety margin, ensuring that the steady-state dynamic equilibrium temperature $T_2$ of the skin will remain vastly below $3000\ \text{K}$. Calculating for $T_1 = 1800\ \text{K}$, the dynamic radiative equilibrium temperature of the airframe surface is found to be merely:

$$T_2 \approx 1500\ \text{K} = 1227^\circ\text{C}$$

In actual flight, the radiant emissivity of a solid surface is markedly higher than that of high-temperature gases; hence, the actual equilibrium surface temperature will be lower still. This fundamental calculation demonstrates conclusively: **The thermal protection shield of the glider's lifting surfaces can be manufactured directly using specialized ceramic tiles or corundum (alumina refractory) plates!**

---

## IV. Suborbital Terminal Descent and Final Touchdown

Once the gliding craft decelerates to $v_1 = 2000\ \text{m/s}$, all danger of destructive overheating is entirely eliminated (see equation 33 and Figure 5). Subsequent aerodynamic deceleration to landing speeds is completed rapidly in the lower atmosphere at altitudes of 1 to 2 kilometers above the ground.

In early interplanetary missions, the precise landing coordinates cannot be determined prior to launch with pinpoint accuracy; it is impossible to predict beforehand whether the vehicle will touch down over the open ocean or on land. Permitting the craft to land directly on rugged, unprepared terrain at high gliding speeds of tens of meters per second would pose an unacceptable hazard to the crew. Consequently, the vehicle must be equipped with a dedicated parachute deceleration landing system.

If airframe volume and weight allow carrying a parachute of sufficient canopy area, a primary recovery parachute can be deployed to suspend and lower the entire craft gently to the ground. If an all-vehicle parachute proves excessively bulky and heavy, individual ejection survival parachute systems must be provided for the crew, allowing the astronauts to parachute to safety while the unmanned airframe impacts the ground or water surface as a conventional glider.

If the landing zone lies over water, the craft can execute an emergency ditching directly onto the sea. In that event, at altitudes between 10 and 20 km, the pilot should deflect the tail surfaces downward to reduce the wing angle of attack, flattening the glide slope and minimizing the vertical sink rate at the instant of touchdown. Although this slightly increases the horizontal water skimming velocity, the vertical impact shock is greatly attenuated. For water landings, the underside of the fuselage should incorporate reinforced hydro-skis or planing hull structures analogous to those of seaplanes.

---

## V. Second Return Method: Controlled Multi-Pass Atmospheric Deceleration (Aerobraking)

We now turn to the **second method** of dissipating return velocity by aerodynamic resistance—namely, utilizing atmospheric drag directly to extinguish the entire return velocity $w_v = 11,185\ \text{m/s}$.

In this method, the rocket does not expend enormous amounts of propulsive energy outside the atmosphere to establish an initial circular parking orbit. Instead, it transitions directly from its interplanetary return trajectory into an elongated elliptical orbit whose perigee is calibrated to graze the outermost fringes of Earth's rarified atmosphere.

The selection of this entry perigee altitude demands extreme precision: it must provide a sufficient margin of safety to accommodate orbital tracking errors and guidance tolerances, ensuring that the rocket, entering at second cosmic velocity ($11\ \text{km/s}$), is not destroyed by thermal loads; yet it must maintain an appropriately sized semi-major axis. A smaller semi-major axis improves the accuracy of perigee determination and minimizes third-body gravitational perturbations from the Moon, but necessitates a slightly larger initial retro-burn executed at apogee.

When the rocket's perigee first dips into the upper atmosphere, it undergoes a distinct orbital evolution:
The rocket does not fire its engines at perigee; rather, it relies entirely upon the drag of the rarified atmosphere for deceleration. With each passage through perigee, the orbit's semi-major axis and apogee altitude contract significantly. Through repeated passes, the orbit is progressively circularized into a contracting, flat spiral entirely embedded within the atmosphere.

Throughout this multi-pass aerobraking maneuver, **lifting surfaces with automatically variable angles of attack** provide essential self-stabilizing control:
* **Upon dipping into deeper, denser layers**: Rising dynamic pressure acting on the forward control vanes automatically pitches the lifting surfaces to a **positive angle of attack**. The resulting upward aerodynamic lift halts further descent into denser air, forcing the craft to remain in the rarified upper buffer zone and preventing catastrophic thermal overshoot;
* **Upon passing perigee and climbing out toward space**: As dynamic pressure decays, the vanes adjust the lifting surfaces to a **slightly negative angle of attack**. The resulting downward negative lift prevents the vehicle from ascending too far out of the Earth's gravitational sphere, flattening the exit trajectory and ensuring a gentle, stable entry angle for the subsequent perigee pass.

Through this dynamic adaptation of wing incidence, perigee can be maintained reliably within safe upper atmospheric limits from the very first encounter, until continuous drag circularizes the trajectory into an atmospheric circular orbit (in reality, a gently descending spiral). Thereafter, terminal gliding and landing proceed identically to the first method.

---

## VI. Analytical Derivation of Active Braking Velocity $\beta$ and Substantial Propellant Savings

Employing this second method, we harness the natural aerodynamic drag of Earth's atmosphere to extinguish:

$$11,185\ \text{m/s} - \beta$$

of the total return velocity, rather than being restricted to the $7909\ \text{m/s} + \beta$ of the first approach.

Here, $\beta$ represents the active propulsive velocity that the rocket engines must deliver to deflect the incoming hyperbolic or parabolic return trajectory $T_c$ into an initial elongated ellipse whose perigee grazes the outer atmosphere. Theoretically, given sufficiently accurate guidance and ephemeris calculation, $\beta$ can be made arbitrarily small.

Since the thickness of the sensible atmosphere is negligible compared to the Earth's radius $R$, neglecting higher-order terms, the exact analytical formula for the required active retro-velocity $\beta$ is:

$$\beta = \sqrt{2 \frac{R}{r_1} R g} \left( 1 - \sqrt{\frac{r}{r+r_1}} \right) + \sqrt{2 \frac{R}{r} R g} \left( \sqrt{\frac{r_1}{r+r_1}} - \sqrt{\frac{R}{R+r}} \right)$$

where:
* $R$ is the radius of the Earth;
* $r_1$ is the perigee (closest approach) distance of the initial elliptical orbit from the Earth's center;
* $r$ is the apogee (farthest approach) distance of the initial elliptical orbit from the Earth's center;
* **The first term** represents the retro-velocity needed to brake the rocket from parabolic return trajectory $T_c$ into an initial ellipse with apogee $r$ and safe perigee $r_1$;
* **The second term** represents the secondary trim burn applied at apogee $r$ to lower perigee from $r_1$ into the sensible atmospheric boundary layer ($R$).

Substituting realistic, conservative orbital parameters—$r_1 = 2.5\, R$ and $r = 20\, R$—yields the high-precision numerical solution:

$$\beta \approx 0.05\, w_c = 0.05 \times 11,185\ \text{m/s} \approx 550\ \text{m/s}$$

**This analytical result is of epoch-making engineering significance!**

It demonstrates that **out of the colossal re-entry kinetic energy corresponding to $11,185\ \text{m/s}$, we can dissipate a full $10,360\ \text{m/s}$ entirely through atmospheric resistance!**

The total characteristic velocity $W_v$ that the propulsion system must generate across the entire round-trip mission profile drops precipitously from the $22,370\ \text{m/s}$ required by pure propulsive braking to merely:

$$W_v \approx 12,550\ \text{m/s}$$

This monumental breakthrough transforms round-trip interplanetary flight using chemical propellants from a theoretical impossibility into a fully achievable engineering reality.
