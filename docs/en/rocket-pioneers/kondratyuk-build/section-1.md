---
title: "Part II · Section 1: Fundamental Principles of Reactive Propulsion and Ideal Velocity Equation"
description: "Yuri Kondratyuk, \"To Whomsoever Will Read in Order to Build\" (1918–1919), Section 1: Basic astronautical assumptions, reactive thrust derivation, and gravitational potential energy calculations."
---

# Section 1 · Fundamental Principles of Reactive Propulsion & Theoretical Equations
### The Fundamental Principles of Reactive Propulsion & Theoretical Equations
**Yuri Vasilievich Kondratyuk**  
*(From NASA TT F-9285, pp. 18–22 / Russian Manuscript, pp. 501–508)*

---

## Preface and Author's Foreword

First of all, I beg the reader not to be frightened by the subject of this work, nor, on account of its difficulty, to abandon the realization of the basic fact that: **from the standpoint of pure theoretical mechanics, flying into outer space by rocket is by no means an impossible or extravagant fantasy**.

In what follows, I shall frequently have to resort to expressions that are generally considered unacceptable in rigorous scientific treatises, such as: "not excessively large," "sufficiently," "moderately," etc., without providing strictly defined quantitative values. This is due to the complete lack of empirical experimental data at my disposal required to draw a sharp boundary between "sufficient" and "insufficient"; in truth, the vast majority of engineering material properties indispensable for constructing a manned rocket have never yet been systematically determined or compiled. In a few instances, it is simply because I was too lazy to perform elementary mathematical calculations that anyone can readily carry out with pencil and paper.

Permit me also a remark concerning terminology: in many cases, I have coined my own technical terms; in others, I may have adopted or inadvertently distorted existing scientific expressions. Should the reader encounter such instances, I ask him not to dwell on verbal imperfections, but rather to look for the substantive reality underlying them.

The ultimate realization of this grand undertaking will demand testing, testing, and more testing, on an ever-expanding scale. Particularly in manned flight trials, one must proceed with extreme caution and deliberate gradualism. In a field so utterly unexplored, it is impossible to foresee every contingency; and in the void of interplanetary space, the cosmonaut cannot count upon any outside assistance.

---

## Fundamental Theoretical Principles of Space Flight

Manned flight departing from Earth into outer space and returning safely must fulfill two primary prerequisites:
1. **First Principle: The voyage must under no circumstances endanger the life and health of the passengers**;
2. **Second Principle: The vehicle must possess completely autonomous maneuvering capabilities in space**.

The First Principle encompasses two distinct mechanical and physiological requirements:
* First, the **mechanical acceleration** imparted to the manned vehicle must never exceed a well-defined physiological tolerance threshold; once this threshold is crossed, the resulting excessive g-load causes severe physical trauma or fatality (methods to elevate this limit will be discussed in detail later);
* Second, the crew cabin must possess **absolute hermetic sealing** to prevent the escape of breathing air, must provide continuous air replenishment and oxygen regeneration, and the thermal environment inside the vehicle must be maintained within the normal comfort envelope of the human body.

The second set of requirements regarding hermetic sealing and life support can be readily solved using modern engineering, but the first condition demands in-depth mechanical analysis: in order for a vehicle to completely escape the gravitational bond of the Earth, it must attain an immense speed—an escape velocity of approximately **$11\ \text{km/s}$** (see Note 1 at the end of the text).

To attain such an extraordinary speed without catastrophic physiological consequences, the thrust acceleration must be applied continuously over a considerable duration (measured in hours) and distributed across a vast spatial distance (hundreds or thousands of kilometers).

From this, it becomes evident that any traditional concept of a **giant artillery cannon**:
* Is not merely constrained by the tensile strength of contemporary materials, which cannot impart such extreme velocity to a projectile;
* But is fundamentally, physically impossible—because a human being seated inside the shell would be instantaneously crushed to pulp by the tens of thousands of $g$'s generated in the gun barrel during explosive firing.

To be sure, one can conceive theoretically of a **super-electromagnetic launch cannon** hundreds of kilometers in length, accelerating the vehicle at a mild, comfortable rate over this long track to $11\ \text{km/s}$; however, the construction costs of such an enormous linear launcher would be astronomically prohibitive, and, far more critically, it completely fails to address the problems of orbital maneuvers in space or deceleration and control during return to Earth.

The cannon concept must therefore be rejected outright. There remain only the **centrifugal sling/catapult principle** and the **reactive propulsion device**.

Yet the centrifugal sling principle is unworkable for precisely the same mechanical reasons: to prevent human beings from being crushed by centrifugal acceleration, the rotating arm would have to be inconceivably gigantic and heavy, and it likewise offers no solution for deep-space maneuvering or return braking.

Ultimately, only a **reactive propulsion device** is capable of fulfilling these conditions.

The second principle—autonomous maneuverability in the void of space—inevitably leads to reactive propulsion as well. In the absolute vacuum between celestial bodies, there is no external medium against which to push; the sole support for the spacecraft can only come from the reaction of mass expelling from within itself.

Hence, the core physical question before us reduces to this:  
**From the standpoint of theoretical physics, can a reactive device generate and achieve a velocity of $11\ \text{km/s}$? Can it store and regain this velocity during the return journey? Are the required initial launch mass and physical dimensions an impossible castle in the sky, or do they lie well within the reach of human engineering capabilities?**

We shall adopt the **rocket** as the standard analytical model for a reactive device; for any other form of reaction engine conceivable to my mind either requires absurdly colossal physical dimensions beyond fabrication, or relies on unexplored physical principles which I am unable to investigate at present.

---

## Rigorous Derivation of the Theoretical Rocket Mass Formula

Suppose we possess a substance capable of releasing energy (hereafter termed the **active agent** / *активное вещество*), yielding an effective work $p$ per unit mass (expressed in absolute mechanical units).

Let the instantaneous total mass of the rocket at any given moment be $m$. Suppose that at this moment an infinitesimal mass $h$ of the active agent is consumed and discharged backward. The work liberated by this combustion is $hp$. Assuming that, as a result of the combustion and directed expansion of this working fluid, the vehicle acquires an infinitesimal reactive velocity increment.

According to momentum conservation and the kinetic energy theorem, during the ejection of this infinitesimal working fluid, assuming the rocket mass remains approximately $m$ (since $h$ is infinitesimal), the effective exhaust velocity $c$ of the expelled gases is:
$$c = \sqrt{2p}$$

From the differential equation of momentum conservation, the differential velocity increment gained by the rocket is:
$$dV = - \sqrt{2p} \cdot \frac{dm}{m}$$

Integrating both sides from the initial launch state to burnout—where the total initial mass of the rocket (including all active propellants and structure) is $M$, and the final burnout mass (the "dead weight" comprising empty cabin, equipment, and payload) is $m$:
$$\int_{0}^{V} dV = \sqrt{2p} \int_{m}^{M} \frac{dm}{m}$$

$$V = \sqrt{2p} \cdot \ln \left(\frac{M}{m}\right)$$

Rearranging yields the theoretical mass ratio formula between the initial launch mass $M$ and the final empty mass $m$:
$$\ln \left(\frac{M}{m}\right) = \frac{V}{\sqrt{2p}}$$

That is:
$$M = m \cdot e^{\frac{V}{\sqrt{2p}}}$$

Where:
* $M$: Initial total mass of the rocket at launch;
* $m$: Final dry structural and payload mass (passive mass) after propellant exhaustion;
* $V$: Terminal velocity required by the vehicle;
* $p$: Effective specific energy liberated per unit mass of active propellant ($\text{ergs/g}$ or heat value);
* $e$: Base of natural logarithms ($e \approx 2.71828\dots$).

From this exponential formula, an extraordinarily profound and milestone theoretical conclusion emerges:  
**Given a sufficient propellant mass ratio, it is theoretically possible to accelerate any given payload mass $m$ to any required high velocity $V$—even if the active substance employed possesses only a modest or moderate specific energy $p$!**

The magnitude of the specific energy $p$ essentially affects only the expansion factor of the initial mass $M$. To be sure, as the specific energy $p$ decreases, $M$ grows with fierce exponential steepness, rapidly exceeding practical engineering limits; but as long as the specific energy is sufficiently high, the exponential term can be constrained within thoroughly practical engineering bounds.

---

## Velocity Formula for Overcoming Earth's Gravitational Potential

The gravitational potential at the Earth's surface can be expressed as $r \cdot j$, where:
* $r$ is the Earth's radius (approximately $6.37 \times 10^8\ \text{cm}$);
* $j$ is the gravitational acceleration at the Earth's surface (approximately $981\ \text{cm/s}^2$).

Converting this gravitational potential into the escape velocity (second cosmic velocity) required to break free from the Earth's gravitational field:
$$V_{\text{esc}} = \sqrt{2rj} \approx 1.12 \times 10^6\ \text{cm/s} = 11.2\ \text{km/s}$$

Substituting this escape velocity into the general rocket mass equation gives the **fundamental mass formula for leaving Earth**:
$$M = m \cdot e^{\frac{\sqrt{2rj}}{\sqrt{2p}}} = m \cdot e^{\sqrt{\frac{rj}{p}}}$$

If a round-trip voyage is considered—namely, expending an equivalent velocity impulse in deep space or during return landing under the most conservative assumption of purely propulsive retro-braking (disregarding atmospheric braking for the moment)—the velocity requirement doubles:
$$\ln M = \ln m + 2\sqrt{\frac{rj}{p}}$$

$$M = m \cdot e^{2\sqrt{\frac{rj}{p}}}$$

Now let us substitute quantitative data for specific chemical propellants:  
Assume a hydrogen-oxygen combustion system ($\text{H}_2 + \text{O}$), whose chemical heat of reaction is approximately:
$$p \approx \frac{10}{3}\ \text{kcal/g} \approx 3333\ \text{cal/g} \approx 1.4 \times 10^{11}\ \text{ergs/g}$$

Evaluating the exponent:
$$\sqrt{\frac{rj}{p}} \approx \sqrt{\frac{6.37 \times 10^8 \times 981}{1.4 \times 10^{11}}} \approx \sqrt{4.46} \approx 2.11$$

Therefore, for a one-way departure escaping Earth's gravity:
$$\frac{M}{m} = e^{\sqrt{\frac{rj}{p}}} \approx e^2 \approx 7.4$$

If we account for slight one-way losses or rely entirely on rocket retro-propulsion for return (taking the exponent to be approximately $4$):
$$\frac{M}{m} \approx e^4 \approx 55$$

This theoretical mass ratio of approximately **$55$** (even if in practical engineering, due to nozzle expansion inefficiencies, non-ideal gas dynamics, and tank structural mass, the actual mass ratio must be scaled up to $100$, $200$, $500$, or even $1000$) is **by no means an astronomical impossibility**! This demonstrates irrefutably that **building a rocket to reach outer space is fully feasible in physical engineering!**

*(Note: All physical symbols used by the author are based on the absolute CGS system.)*

---

## Complex Corrections for Human and Structural Mechanical Tolerances

In deriving the idealized formula above, we did not incorporate the **time history** of thrust acceleration. In other words, the sole condition under which the formula strictly applies is: **the acceleration is imparted instantaneously to the spacecraft**.

In the real physical world, however, as the rocket burns propellant during its climb away from Earth, the Earth's gravitational field relentlessly exerts a downward gravitational acceleration toward the center of the Earth at every second.

The longer the duration over which thrust is applied to accelerate the vehicle, the greater the cumulative negative velocity stolen away by Earth's gravity; and this lost velocity must be compensated entirely by extra thrust generated by burning additional propellant!

This physical logic is clearly illustrated by the following extreme example:  
*Suppose we fire the rocket engine upward, imparting to the vehicle an acceleration exactly equal to the surface gravitational acceleration $j$ ($1\ g$); the spacecraft will not move an inch away from the Earth, but will merely hover stationary in mid-air! In that case, though thousands of tons of propellant are burned to ash, the vehicle's velocity relative to Earth remains zero forever!*

Therefore, from the sole perspective of minimizing gravitational loss: **the higher the mechanical acceleration applied per unit time, and the shorter the time required to attain escape velocity, the higher the propulsive efficiency and the lower the propellant waste!**

Here, however, we encounter rigid physical and physiological barriers:
1. **The physiological tolerance of the human body has strict limits**: an unprotected healthy human body cannot withstand mechanical accelerations beyond a specific threshold for prolonged periods (revolutionary methods using liquid immersion to elevate this limit will be explored in the next chapter);
2. **The mechanical strength of the hull and propellant tanks must increase proportionally with acceleration**: higher accelerations mean greater inertial loads, necessitating thicker tank walls and heavier structural framing, which drastically degrades the vehicle's inert mass fraction.

Based on these trade-offs, acceleration cannot be increased arbitrarily, but must be kept strictly within an upper allowable engineering and physiological limit $q$.

We define the ratio of the total mechanical acceleration $q$ produced by the engine to the local gravitational acceleration $j$ as the multiple factor $k$:
$$k = \frac{q}{j}$$

In practical engineering, a reasonable expected range for $k$ lies between **$5$ and $10$**.

---

## First Method of Flight (Radial Ascent) and Its Corrected Formula

The **first method of flight** consists of accelerating the vehicle directly upward along the **vertical radial direction** (or a fixed straight line away from Earth); during the return retro-propulsive braking phase, deceleration thrust is applied radially toward the Earth's center.

Let the ratio of engine acceleration to local gravitational acceleration be $k = q / j$.  
Although the local gravitational acceleration $j$ gradually diminishes as the rocket climbs away from the Earth, causing the ratio $k$ to increase accordingly, to avoid excessive mathematical complexity in this preliminary derivation, we assume that $k$ remains constant throughout the powered boost phase (or at least that its variation is modest, particularly in the initial launch phase where $k$ is already large, around $5 \sim 10$).

In vertical radial ascent, the total acceleration delivered by the rocket engines is $k \cdot j$; of this, exactly $1 \cdot j$ must be permanently dedicated solely to overcoming Earth's gravity. The **effective acceleration** genuinely contributing to the vehicle's net space velocity is only:
$$a_{\text{eff}} = (k - 1)j$$

This means that, in terms of physical effectiveness in imparting velocity to the vehicle, the specific work of the propellant is reduced by a correction factor:
$$\frac{k}{k - 1} = 1 + \frac{1}{k - 1}$$

Consequently, this penalty factor $1 + \frac{1}{k-1}$, representing gravitational loss, must be multiplied directly onto the **logarithmic exponent** of the rocket mass equation!

Substituting this yields the mass formula for the first method of flight accounting for gravity losses:
$$M = m \cdot e^{\left(1 + \frac{1}{k-1}\right) \sqrt{\frac{rj}{p}}}$$

Even if we choose a fairly aggressive acceleration factor $k = 5$:
$$1 + \frac{1}{k-1} = 1 + \frac{1}{4} = 1.25$$

This factor of $1.25$, which appears unassuming at first glance, produces a catastrophic, cascading exponential mass penalty when placed in the **power exponent** of the natural base $e$! It represents a crushing propellant burden for direct vertical ascent.

To liberate ourselves from this heavy gravitational shackle, we must search for fundamentally new flight trajectories and physiological breakthroughs—which form the core subject of the next chapter.
