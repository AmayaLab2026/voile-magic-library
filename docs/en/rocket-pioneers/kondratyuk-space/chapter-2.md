---
title: "Part 3 · Chapter 2: Boost Phase Trajectory & Propellant Mass"
description: "Yu. V. Kondratyuk's \"Conquest of Interplanetary Space\" (1929), Chapter 2: The Tsiolkovskiy equation, multistage rocket mass allocation, and the continuous infinite staging limit theory."
---

# Chapter 2 · Boost Phase Trajectory & Propellant Mass
### Section II. Formula for the Load Rating & Theory of Multistage Staging
**By Yuriy Vasil'yevich Kondratyuk**  
*(From NASA TT F-9285, pp. 64–66 / Original work, pp. 7–9)*

---

## Application of the Classical Tsiolkovskiy Equation

The fundamental relationship of rocket dynamics linking characteristic velocity $W$, effective exhaust velocity $u$, and load rating (mass ratio) $n$ was first rigorously established by Engineer K. E. Tsiolkovskiy (though with slight differences in mathematical notation):
$$n_i = e^{\frac{W_i}{u_i}}$$

that is:
$$\frac{M_{io}}{M_{if}} = e^{\frac{W_i}{u_i}}$$

where $e$ is the base of natural logarithms ($e \approx 2.71828\dots$), and the subscript $i$ may designate any specific powered active flight segment along the rocket trajectory, or alternatively the entire trajectory as a whole.

---

## The Technical Deadweight Barrier of Single-Stage Rockets

From the above formula, it is evident that when the characteristic velocity $W$ required for a mission substantially exceeds the effective exhaust velocity $u$—as in escaping Earth's gravitational field, where $W \approx 11 \sim 14\ \text{km/s}$ while chemical propellant exhaust velocity $u$ is merely $3 \sim 4.5\ \text{km/s}$, yielding a ratio $\frac{W}{u} \approx 3 \sim 4$:
$$n = e^{\frac{W}{u}} \approx e^3 \sim e^4 \approx 20 \sim 55$$

This implies that the initial liftoff mass $M_0$ must be several tens of times the final mass $M_f$.

In the engineering structure of a single-stage rocket, however, the final mass $M_f$ is by no means composed entirely of cosmonauts and useful payload! Rather, $M_f$ must inevitably include:
* The empty metal shell weight of the entire full-scale propellant tanks;
* The heavy deadweight of high-thrust rocket engines, along with their intricate pumps, valves, and manifold ducting;
* The structural load-bearing airframe running throughout the vehicle.

Within the limits of modern light-alloy engineering materials, the deadweight of empty propellant tanks and propulsion structures routinely constitutes $5\% \sim 15\%$ of the initial total propellant loading. When a single-stage rocket arrives at the conclusion of its powered run with propellants nearly exhausted, the absolute weight of these empty deadweight structures **far exceeds the mass of the scientific payload itself**, in many cases relentlessly squeezing the actual useful payload into negative values!

From this arises a severe engineering corollary: **Single-stage rockets, when confronted with the immense characteristic velocity requirements of escaping Earth, run headlong into an impassable physical deadweight barrier!**

---

## Mathematical Derivation of Multistage Staging

The sole engineering salvation capable of breaking this deadweight shackle is the **multistage rocket architecture** championed independently by Kondratyuk and Tsiolkovskiy: during the acceleration phase, no empty and useless propellant tanks are retained; instead, the entire rocket is subdivided into a series of distinct stages, **and as each portion of propellant is expended, the corresponding empty tanks and structural hardware are immediately and unhesitatingly jettisoned**!

We now present the rigorous mathematical derivation of the rocket load formula for multistage staging:

Let the entire rocket be divided into $z$ discrete stages or active operating segments ($i = 1, 2, \dots, z$).  
During the operation of the $i$-th stage:
* The initial total mass of the stage is $M_{io}$;
* The engine burns propellant, accumulating characteristic velocity $W_i$;
* When that stage's propellant is exhausted, its total mass drops to $M_{if}$;
* Immediately thereafter, the empty structural deadweight of that stage (denoted as $M_{\text{empty}, i}$) is separated and discarded;
* The remaining mass $M_{(i+1)o} = M_{if} - M_{\text{empty}, i}$ serves as the initial mass of the subsequent stage, which ignites and continues accelerating.

We define the **structural deadweight coefficient $q_i$** of that stage as the ratio of the jettisoned empty structural deadweight to the initial total mass of the stage:
$$q_i = \frac{M_{\text{empty}, i}}{M_{io}}$$

Through systematic recursive algebraic simplification, the comprehensive mass multiplier relating the total mission liftoff mass $M_0$ to the final useful payload $M_{\text{payload}}$ is expressed as:
$$\frac{M_0}{M_{\text{payload}}} = \prod_{i=1}^{z} \frac{n_i}{1 - q_i (n_i - 1)}$$

where $n_i = e^{\frac{W_i}{u_i}}$ represents the pure propellant load rating for the $i$-th stage.

---

## Continuous Infinite Staging Limit Theory

Kondratyuk formulated in his manuscript a mathematical proposition of profound theoretical depth: **If, instead of dividing the vehicle into a finite number of discrete stages (such as 2, 3, or 4 stages), we conceive of the spacecraft continuously peeling away and shedding its empty tank material in infinitesimal increments like an onion as propellant is consumed ($z \to \infty$), where does the performance limit of the rocket lead?**

Assume that at any instant during flight, the ratio of infinitesimal structural deadweight jettisoned to the infinitesimal mass of propellant consumed is a constant proportionality factor $q$ (that is, for every $1\ \text{kg}$ of propellant burned, $q\ \text{kg}$ of redundant empty tank material is trimmed and discarded simultaneously).

Over an infinitesimal time increment $dt$, the differential change in rocket mass is:
$$dM = - (1 + q) \, dM_{\text{fuel}}$$

Meanwhile, the differential momentum equation for the effective reactive thrust is:
$$M \cdot dW = - u \cdot dM_{\text{fuel}} = \frac{u}{1 + q} \cdot dM$$

Separating variables and integrating over the entire acceleration phase:
$$\int_{0}^{W} dW = - \frac{u}{1 + q} \int_{M_0}^{M_f} \frac{dM}{M}$$

Solving yields the rocket load formula under the continuous infinite staging limit:
$$M_0 = M_f \cdot e^{\frac{W}{u(1 - q)}}$$

or alternatively:
$$n = e^{\frac{W}{u_{\text{eff}}}}$$

where:
$$u_{\text{eff}} = u \cdot (1 - q)$$

This remarkably elegant and profound theoretical limit formula reveals the ultimate physical truth of multistage staging:  
**The physical essence of multistage rocketry (and of continuously jettisoning structural deadweight) is macroscopically equivalent to slightly derating the propellant's effective exhaust velocity from its thermochemical value $u$ to an equivalent effective velocity $u_{\text{eff}} = u(1 - q)$!**

For example, assuming a structural deadweight coefficient of $q = 0.1$ (empty tanks constituting $10\%$ of propellant mass), the effective exhaust velocity is diminished by merely $10\%$ ($u_{\text{eff}} = 0.9 u$).

Under this effective exhaust velocity, the overall mass ratio of the rocket merely shifts from $e^{\frac{W}{u}}$ to $e^{\frac{W}{0.9 u}}$, **completely banishing the destructive competition between structural deadweight and useful payload that cripples single-stage rockets**! This analytical mechanics proof definitively settled the debate over whether rockets could escape Earth, establishing an unshakeable mathematical foundation for the engineering realization of multistage spaceflight.
