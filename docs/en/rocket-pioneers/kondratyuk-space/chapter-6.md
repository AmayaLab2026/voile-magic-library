---
title: "Part 3 · Chapter 6: Passive Trajectories & Orbital Maneuvers"
description: "Yu. V. Kondratyuk's \"Conquest of Interplanetary Space\" (1929), Chapter 6: Trajectory classifications, characteristic velocity budgets, radial versus tangential multi-elliptical dynamics, and gravity loss theorems. Complete translation of NASA TT F-9285."
---

# Chapter 6 · Passive Trajectories & Orbital Maneuvers
### Section VI. Types of Trajectories and Rocket Velocities Required
**By Yuriy Vasil'yevich Kondratyuk**  
*(From NASA TT F-9285, pp. 76–85 / Original work, pp. 23–33)*

---

*[Continuing from the preceding discussion of demountable multistage rocket sections]* When the structural sections of the various stages become redundant as the rocket's mass progressively diminishes, they are not discarded into outer space; rather, they are dismantled and transferred into the crew compartment to be melted down and pulverized for subsequent use as chemical components of the propellant charge. This solution is exceptionally advantageous, since the remaining detrimental mass $m_1$ is then restricted merely to the final and smallest section, while all preceding sections have been converted into active propellant charges, progressively consuming the passive deadweight of $m_1$.

Because dismantling and subsequently processing the components of $m_1$ requires a finite amount of time, partitioning the trajectory into segments corresponding to each unchanged structural unit $m_1$ in such a system is no longer arbitrary. The first section replacement cannot be performed before the rocket achieves the state of a free Earth satellite; the final replacement cannot occur after the rocket has decelerated during its return to the point where it loses the status of a free Earth satellite. These two transitions are most advantageously delimited such that they correspond to dividing the trajectory into three segments with roughly equal characteristic velocity increments $W_i$. Dismantling components of $m_1$ in a vacuum and processing them into propellant material requires certain auxiliary equipment. Nevertheless, every effort should be directed toward resolving this approach to $m_1$, as it dramatically alleviates the principal impediment of the entire enterprise—namely, reducing the immense initial liftoff mass of the rocket. An excessively large liftoff mass constitutes a formidable practical obstacle to conquering interplanetary space and celestial bodies of the Solar System, extremely difficult to surmount in engineering practice, although theoretically presenting no special difficulties.

---

## 1. Physical Notation and Definitions

We adopt the following system of physical symbols:

* $I_j$ — An active segment of the trajectory during which the rocket engines are firing (i.e., imparting an active thrust acceleration to the vehicle).
* $W_e$ — The **"escape velocity"** for a given state of the rocket: namely, the additional velocity increment that must be added to the rocket's existing velocity to place it onto a parabolic escape trajectory relative to the geocenter.
* $W_r$ — The **"return velocity"** for a given state of the rocket: namely, the velocity the rocket would attain if it continued coasting unpowered along its existing trajectory until reaching the surface of the Earth (at sea level).
* $w$ — The **"total escape velocity"** and **"total return velocity"**: its numerical value equals $W_e$ computed from a state of rest at the Earth's surface, and likewise equals $W_r$ computed from rest at infinite distance from the Earth or when moving along a parabolic trajectory. This is the classical **parabolic escape velocity (second cosmic velocity)**:
  $$w = \sqrt{2Rg} = 11,185\ \text{m/s}$$
  where $R$ is the mean radius of the Earth, and $g$ is the sea-level gravitational acceleration.
* $v$ — The instantaneous orbital velocity of the rocket at a given moment relative to the **center of the Earth** (rather than to the Earth's surface).
* $r$ — The instantaneous radius vector from the center of the Earth to the rocket.

The term **"a flight"** as employed herein designates the complete round-trip voyage of a rocket traveling toward a point infinitely distant from Earth and returning from that point, during which the vehicle's velocity at the specified distant point and upon re-touching the Earth's surface must strictly equal zero.

Here, we temporarily neglect the influence of atmospheric drag and disregard gravitational perturbations from celestial bodies other than the Earth. Consequently, the quantitative conclusions derived in this section are approximately correct for trajectory segments lying outside the dense atmosphere, outside the lunar sphere of influence, and for flight paths whose dimensions are not excessively large compared to the radius of Earth's orbit.

---

## 2. Fundamental Energy Relations for Circular Satellite Orbits

For a rocket in an Earth satellite state along a circular orbit, the following relations hold identically in all cases:
$$W_e = v(\sqrt{2} - 1) = w \sqrt{\frac{R}{r}}(\sqrt{2} - 1) \quad (\text{cf. Editorial Note } 12)$$
$$W_r = \sqrt{w^2 - v^2} = w \sqrt{1 - \frac{R}{2r}}$$

When the rocket's orbit does not intersect or touch the surface of the Earth (as is true for any circular orbit), our definition of $W_r$ is formal (hypothetical). In such instances, $W_r$ must be understood as the velocity the rocket would possess if all the energy corresponding to its own mass and the difference in gravitational potential between its current position and the Earth's surface were added to its kinetic energy—regardless of whether such an addition could actually be realized during physical motion along the given orbit.

From this it is evident that along a single orbit, $W_e$ takes on different numerical values at points situated at differing distances from the center of the Earth (provided the orbit is not parabolic, on which $W_e \equiv 0$); on the other hand, $W_r$ possesses a strictly constant value for all points along a given orbit. The quantities $W_e$ and $W_r$ carry the following fundamental dynamic implications:

1. **Proposition 1**: The value of $W_e$ at the **perigee** of a given orbit (the point closest to the geocenter) represents **the theoretical minimum velocity increment $W$ required for the rocket to enter a parabolic escape orbit** in order to accomplish the outward leg of the voyage to infinity (i.e., the theoretical minimum derived solely from energy conservation).
2. **Proposition 2**: $W_r$ represents the theoretical minimum velocity increment $W$ required to bring a rocket moving along a given orbit to a landing on the Earth's surface with zero relative velocity, thereby completing the return leg of the voyage.

---

## 3. Rigorous Mathematical Proof of the Two Extremal Propositions

### Proof of Proposition 1
We compare the values of $W_{e1}$ and $W_{e2}$ calculated for two neighboring points $a_1$ and $a_2$ on the same orbit, where the geocentric gravitational potential difference between the two points is an infinitesimal quantity $\varepsilon$.

If for the more distant point $a_1$, according to the energy equation, we have:
$$W_{e1} = \sqrt{v_1^2 + w^2 \frac{R}{r_1}} - v_1$$

then for point $a_2$ closer to the Earth's center, where potential energy is lower and kinetic energy is correspondingly higher, we derive:
$$W_{e2} = W_{e1} - \frac{\varepsilon}{v} \left( 1 - \frac{v}{w} \sqrt{\frac{r}{R}} \right)$$

(*Note by Prof. V. P. Vetchinkin: Since for any elliptical orbit $v < w \sqrt{R/r}$, it follows that $1/v > \sqrt{r/R}/w$, meaning the quantity inside the brackets is always positive*).

Therefore, in absolute value:
$$W_{e2} < W_{e1}$$

This proves that **$W_e$ attains its strict global minimum at the perigee of a given orbit**. This constitutes the theoretical minimum velocity increment required to transfer to a parabolic escape orbit. Q.E.D.

### Proof of Proposition 2
We compare the return velocity values $W_{r1}$ and $W_{r2}$ obtained in two distinct cases:
* Case 1: The rocket moves along an orbit and receives a retro-braking velocity increment $u$ at point $a_1$;
* Case 2: The rocket moves along the same orbit at the same speed, but receives an identical negative velocity increment at another point $a_2$, the difference in gravitational potential between $a_1$ and $a_2$ being $\varepsilon$.

If the first case yields the value $W_{r1}$, the derivation for the second case gives:
$$W_{r2} < W_{r1}$$

It follows that **the closer to the Earth's surface the retro-braking increment is applied, the smaller the resulting value of $W_r$**. When the negative velocity increment is applied directly at the Earth's surface (sea level), we obtain the minimum $W_r$. To terminate the flight entirely, we must extinguish all remaining residual velocity at the Earth's surface, which for a given orbit is precisely equal to $W_r$. Q.E.D.

---

## 4. Mechanical Energy Conversion & Clarification of the Velocity Increment Paradox

The physical mechanism underlying these two propositions is elucidated as follows:

When a rocket expends a given mass of propellant, it imparts to itself a definite positive or negative velocity increment $\Delta v$, the magnitude of which is completely independent of whether the rocket was initially stationary or moving at high speed. However, **because the kinetic energy of the rocket relative to the Earth is proportional to the square of its geocentric velocity** ($E_k = \frac{1}{2} M v^2$):

$$\Delta E_k = \frac{1}{2} M (v + \Delta v)^2 - \frac{1}{2} M v^2 = M \cdot v \cdot \Delta v + \frac{1}{2} M (\Delta v)^2$$

when the initial velocity $v$ is very large, an identical velocity increment $\Delta v$ produces a vastly greater increase in mechanical energy relative to the geocenter!

> **Numerical Example**:
> * Assume the rocket's current velocity is merely $v = 2$. Imparting a velocity increment of $\Delta v = 4$ yields an increase in kinetic energy per unit mass of:
>   $$\Delta E_k = \frac{6^2 - 2^2}{2} = 16$$
> * Conversely, if the rocket's velocity relative to the center of the Earth is already $v = 20$, imparting the exact same velocity increment $\Delta v = 4$ yields:
>   $$\Delta E_k = \frac{24^2 - 20^2}{2} = 88$$

Thus, evaluated in terms of mechanical energy relative to the Earth, **the higher the rocket's own flight velocity, the greater the effective energy conversion resulting from the ejection of propellant!** Along an unpowered orbital trajectory, the rocket's flight velocity **peaks at its absolute maximum precisely at perigee**, closest to the planetary surface. Consequently, whether injecting energy to escape Earth's gravity or depleting excess energy to land safely on the surface, **applying thrust at orbital perigee represents the optimal point of maximum energy utilization efficiency**.

---

## 5. Velocity Surplus $L$ and the Two Fundamental Rules of Trajectory Design

We observe that only under the necessary (though practically insufficient) assumption that all acceleration and deceleration maneuvers are executed strictly at the surface of the Earth can $W$ attain its theoretical minimum of $2w$. In engineering practice, instantaneous acceleration is impossible; the closer the active powered segment $I_j$ is situated to the surface of the Earth, the smaller the value of $W$.

From this we formulate the **First Rule** governing rocket trajectory design:
> **First Rule**: To prevent unnecessary and detrimental inflation of the required characteristic velocity $W$, all powered operating segments $I_j$ where the rocket accelerates must be located as close to the surface of the Earth as possible!

We define the difference between the actual expended velocity and the ideal theoretical minimum, $W - 2w$, as the **"rocket velocity surplus"**, denoted by the symbol $L$. Letting $L_i$ denote the surplus for a given powered segment:
$$L_i = \int \left( \sqrt{v^2 + w^2 \frac{R}{r}} - v \right) dt \quad (9)$$

In a medium-free vacuum environment, where the potential difference across the powered segment is an infinitesimal $\varepsilon$, the surplus is:
$$L_i = \pm \frac{\varepsilon}{2v} \left( 1 \mp \frac{v}{w}\sqrt{\frac{r}{R}} \right) \quad (10)$$
*(the upper signs applying to elliptical velocities, the lower signs to hyperbolic velocities)*.

We employ subscripts on $L$ to identify the specific physical mechanics causing the velocity surplus:
* $L_g$ — **Gravity delay loss** caused by the Earth's gravitational acceleration;
* $L_\beta$ — **Steering attitude loss** caused by the deviation angle $\beta$ between the thrust vector and the trajectory tangent;
* $L_d$ — **Aerodynamic drag loss** caused by atmospheric resistance (comprising friction and form drag);
* $L_s$ — The cumulative total loss across all physical factors.

From this follows the **Second Rule** for minimizing $L$:
> **Second Rule**: The angle $\beta$ between the direction of thrust and the tangent to the flight trajectory must be maintained at an absolute minimum!

The change in the magnitude of absolute velocity $v$ does not depend on the total vector acceleration $J_0$ of the rocket, but solely on its tangential component $J_0 \cos\beta$. Hence the velocity loss caused by steering misorientation is:
$$L_\beta = W_t (1 - \cos\beta) \quad (11)$$

---

## 6. Mission Trajectory Partitioning & Trajectory Dynamics Trade-offs

We divide the complete mission flight path into three distinct segments:
1. $T_e$ — **"Escape trajectory"**: Beginning at the Earth's surface and terminating at infinity;
2. $T_c$ — **"Connecting trajectory"**: Extending from the termination of $T_e$ through deep space to the vicinity of the target celestial body at infinity;
3. $T_r$ — **"Return trajectory"**: Extending from the termination of $T_c$ to touchdown on the Earth's surface.

At infinite distance from Earth, terrestrial gravity decays to zero and atmospheric resistance is absent. Therefore, $T_c$ may assume any geometric form; along it, the vehicle can traverse space at very low thrust and modest velocity. Consequently, the magnitude of the velocity loss $L$ is determined entirely by the geometry of $T_e$ and $T_r$.

It is immediately evident that simultaneously satisfying both fundamental rules on a single trajectory is impossible:
* **Radial Vertical Trajectory**: While completely satisfying the Second Rule (thrust aligned strictly along the radius vector, $\beta = 0$), it gravely violates the First Rule. Under gravitational acceleration $g$, with mechanical acceleration ratio $\gamma = j/g$, equation (9) yields a gravitational surplus loss of:
  $$L_g \approx \frac{w}{2(\gamma - 1)}$$
  which, for $\gamma \gg 1$, simplifies to:
  $$L_g \approx \frac{w}{2\gamma} \quad (12)$$
  For modest thrust-to-weight ratios $\gamma$, a radial vertical climb incurs disastrous gravity losses.

* **Tangential Trajectory (Figure 1)**: Highly fulfills the First Rule!

![Tangential multi-elliptical acceleration climb trajectory (Figure 1)](/images/rocket-pioneers/space-fig1.png)  
*Figure 1: Tangential and multi-elliptical orbital acceleration climb (Figure 1)*  
*(Solid line segments denote active powered burn segments $I_j$; dashed curves denote unpowered free coasting along elliptical and parabolic orbits)*

According to Figure 1, the rocket accelerates horizontally along a great-circle tangent from departure point $0$ to point $b$:
* To maintain level flight near the surface, the thrust vector must be directed at an inclination angle $\beta$ to the horizon so that the component $M J_0 \sin\beta$ counterbalances gravity exceeding centrifugal force;
* As velocity builds, the vehicle reaches circular velocity at point $d_1$ ($v = w/\sqrt{2}$, first cosmic velocity), where centrifugal force and gravity are in exact equilibrium;
* **Beyond point $d_1$, centrifugal force exceeds gravity; the thrust inclination $\beta$ must reverse to a negative angle (depressing thrust downward to prevent premature outward drift)!**
* When tangential acceleration increases $\beta$ to the point where $L_\beta$ losses become prohibitive, the engine is shut down at point $b_1$, and the spacecraft enters an unpowered elliptical coasting orbit $b_1 - b_2$;
* After completing one revolution and swinging through the symmetrical perigee $b_2$, the engine reignites for a second tangential active burn $I_j$ ($b_2 - c_1$), inserting the vehicle into a higher elliptical orbit $c_1 - c_2$;
* Repeating this cycle, the spacecraft draws kinetic energy at maximum efficiency during each perigee passage, until the final perigee burn propels it into a parabolic escape trajectory!

Along a tangential multi-elliptical trajectory, the theoretical limit of characteristic velocity loss caused by thrust inclination is merely:
$$L_\beta \approx \frac{w}{6\gamma^2} \quad (13)$$
which is vastly smaller than the gravity losses of a vertical launch!

Furthermore, a tangential trajectory offers another immense operational advantage: **launching and returning eastward in the equatorial plane in the direction of Earth's rotation fully harnesses the linear velocity of planetary spin, directly saving twice the surface rotation speed over the round trip**:
$$2U = 920\ \text{m/s}$$

---

## 7. Practical Engineering Compromise: The Hybrid Spiral Launch Trajectory (Figure 2)

Although a purely tangential trajectory is theoretically optimal, it cannot be implemented directly from the Earth's surface: flying horizontally at high speed within the dense lower atmosphere incurs crippling aerodynamic drag losses $L_d$ that completely negate the benefits of planetary rotation.

In engineering practice, the optimum ascent trajectory is therefore a **hybrid compromise trajectory** as illustrated in Figure 2:

![Hybrid spiral launch and transitional trajectory (Figure 2)](/images/rocket-pioneers/space-fig2.png)  
*Figure 2: Hybrid spiral launch trajectory (Figure 2)*

In this hybrid trajectory:
1. At liftoff, the rocket ascends along a moderately steep flight path angle $\theta$ in a spiral arc to rapidly pierce the dense lower atmosphere and escape the high-drag regime;
2. Upon reaching the rarefied upper atmosphere, it smoothly pitches over toward the horizontal tangent, initiating the multi-elliptical perigee impulse acceleration cycle depicted in Figure 1;
3. For climb angles $\theta < 30^\circ$ and load ratios $\gamma \ge 3$ (wingless) or $\gamma \ge 1$ (with lifting surfaces), the composite gravitational velocity surplus loss is accurately estimated by:
   $$L_g \approx \frac{w \sin\theta}{2\gamma} \quad (14)$$

This elegant formula established the theoretical mechanics foundation for what is recognized today in astronautics as the standard gravity-turn launch trajectory.
