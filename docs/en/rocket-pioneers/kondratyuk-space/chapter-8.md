---
title: "Part 3 · Chapter 8: Effect of the Atmosphere on Rocket Ascent and Drag Losses"
description: "Yu. V. Kondratyuk's \"Conquest of Interplanetary Space\" (1929), Chapter 8: Effect of the atmosphere on rocket ascent, supersonic aerodynamic drag laws, calculus of velocity losses, and shock-compression aerodynamic heating equations. NASA TT F-9285 full translation."
---

# Chapter 8 · Effect of the Atmosphere on Rocket Ascent
### Section VIII. Effect of the Atmosphere on Rocket Ascent
**By Yuriy Vasil'yevich Kondratyuk (Yu. V. Kondratyuk)**  
*(From NASA TT F-9285, pp. 88–101 / Original work, pp. 37–56)*

---

*[Continued from the previous discussion on physiological adaptation to acceleration]* Under these conditions, no genuinely detrimental physiological effects were observed (see Note 14). Considering that in swing rotations and conventional aircraft maneuvers, the human body frequently sustains loads of several $g$, when acceleration reaches approximately $3g$, it does not pose a serious hazard to bodily functions.

---

## I. Aerodynamic Drag Law and Component Resistance

As a rocket ascends through the atmosphere, the air medium exerts significant aerodynamic drag upon the moving vehicle. The magnitude of air resistance follows the general aerodynamic drag equation:

$$Q = S \cdot k \cdot v^2 \cdot A \cdot 10^{-4} \cdot c \quad (15)$$

where:
* $Q$ is the total aerodynamic resistance acting on the rocket body (in $\text{kg}$);
* $S$ is the maximum cross-sectional projected area of the vehicle (in $\text{m}^2$);
* $k$ is a coefficient of proportionality, approximately constant in standard sea-level air;
* $v$ is the relative flight velocity of the rocket with respect to the air medium (in $\text{m/s}$);
* $A$ is the relative density of the atmosphere at a given altitude referenced to sea level standard density ($A = \rho_h / \rho_0 \le 1$);
* $c$ is the aerodynamic drag coefficient (form factor) of the vehicle.

In detailed dynamic analysis, medium resistance must be divided into two components of distinct physical nature:
1. **Form drag (pressure drag, $d_p$)**: Caused by the fluid dynamic pressure differential between the forward and aft surfaces of the body and by shock waves formed in displacing air at high speed; macroscopically, it is proportional to the square of the relative velocity ($v^2$);
2. **Skin friction drag ($d_v$)**: Caused by molecular viscous friction within the fluid boundary layer; its dependence upon velocity is relatively more gradual.

At low sea-level speeds (a few meters per second), skin friction of a streamlined body constitutes a substantial fraction; however, as the rocket accelerates into transonic and supersonic regimes, pressure drag and wave drag rise precipitously, becoming overwhelmingly dominant.

---

## II. Vertical Distribution of Atmospheric Density and Altitude-Integrated Drag Curves (Figure 3)

Although directly measured empirical data regarding the exact physical composition of the atmosphere at extreme altitudes remain incomplete, according to existing upper-atmosphere physics, atmospheric density $A$ exhibits an exponential decay with increasing altitude $h$ above the Earth's surface:
$$A(h) \approx 10^{-\frac{h}{H}}$$

For a rocket ascending vertically or at a specified trajectory angle, Kondratyuk formulated the characteristic drag loss integral function $J_0 = F(h)$. In Figure 3, for the characteristic dimensionless parameter $k_2 = 10$, the quantitative evolutionary profile of this drag function with altitude $h$ is presented:

![Integrated atmospheric drag versus altitude (Figure 3)](/images/rocket-pioneers/space-fig3.png)  
*Figure 3: Drag factor $J_0 = F(h)$ integrated distribution curve as a function of altitude ($k_2 = 10$, Figure 3)*

From Figure 3, several key characteristics emerge with absolute clarity:
* From $h = 0$ (sea level) through low altitudes, as flight velocity begins to build up, the drag integral function rises steeply from zero;
* At a specific transitional altitude (approximately in the range of $10 \sim 20\ \text{km}$), the drag function attains a pronounced **maximum peak**;
* Thereafter, because the exponential decay of atmospheric density dominates overwhelmingly, external aerodynamic drag plummets steeply despite the continuous acceleration of the rocket, eventually decaying to negligible values at higher altitudes.

---

## III. Evolution of Drag with Time and Characteristic Integrals (Figure 4)

To analyze the temporal evolution of drag during ascent, Kondratyuk adopted a standard baseline calculation for analytical convenience: vertical launch acceleration $j = 5000\ \text{cm/s}^2$ (i.e., $50\ \text{m/s}^2 \approx 5.1\ g$), with an initial elevation angle $\theta = 90^\circ$.

Accordingly, the drag deceleration function over time, $J_0 = F(t)$, is presented in Figure 4 (for characteristic parameter $k_4 = 1/3$):

![Atmospheric active boost drag versus time curve (Figure 4)](/images/rocket-pioneers/space-fig4.png)  
*Figure 4: Drag time function curve $J_0 = F(t)$ (characteristic parameter $k_4 = 1/3$, Figure 4)*

Integrating this curve over the entire trajectory, $\int J_0(t) \, dt$, yields an effective velocity loss approximately equal to $2000 k_4\ \text{cm/s}$. The mechanical implication of Figure 4 is profound: rigorous quantitative integration proves that **the period of severe low-altitude aerodynamic drag is confined to an extremely brief window of mere minutes**; once this narrow temporal window is swiftly penetrated, atmospheric resistance ceases to impede the rocket.

---

## IV. Optimum Thrust Program Angle and Minimization of Total Velocity Losses

During ascent through a real atmosphere, the total characteristic velocity loss $L_s$ sustained by the rocket comprises three distinct terms:
$$L_s = L_g + L_d + L_\beta \to \min \quad (22)$$

where:
* $L_g$ is the gravitational delay loss;
* $L_d$ is the aerodynamic drag loss;
* $L_\beta$ is the steering loss induced by thrust vector misalignment with the trajectory tangent.

To determine the optimum thrust pitch angle $\beta_1$ that minimizes $L_s$, the variational extremum condition $\frac{\partial L_s}{\partial \beta} = 0$ must be established.

If aerodynamic lifting surfaces (wings) are incorporated onto the rocket airframe, the normal thrust component can be partially or wholly supplanted by aerodynamic wing lift, thereby allowing the rocket to climb smoothly under lower active accelerations without suffering prohibitive thrust angle deviation losses.

---

## V. Quantitative Relations Between Characteristic Velocity Loss and Trajectory Parameters (Figure 5)

By coupling the gravitational loss integral equations with aerodynamic drag equations, Kondratyuk derived analytical expressions relating trajectory inclination $\theta$ to velocity loss $L_d$. For a representative aerodynamic parameter ratio $c/P = 1/62,500$ (where $c = 0.04$ is the drag coefficient and $P = 2500$ is the vehicle area-to-mass loading parameter), curves of velocity loss are plotted in Figure 5:

![Aerodynamic drag and velocity loss relations (Figure 5)](/images/rocket-pioneers/space-fig5.png)  
*Figure 5: Variation of velocity loss $L_d$ with trajectory parameters (Figure 5)*  
*(Curve a corresponds to short-duration high-drag profiles; curve b corresponds to extended shallow ascent profiles)*

From Figure 5, the following critical engineering conclusions are deduced:
1. The shallower the climb angle $\theta$, the longer the flight path traversed within the atmosphere, causing accumulated aerodynamic drag losses $L_d$ to increase exponentially;
2. Conversely, penetrating the atmosphere vertically or at steep elevation angles minimizes $L_d$, but increases gravitational delay loss $L_g$;
3. The optimal ascent trajectory achieves a global system minimum precisely at the intersection of these two competing curves!

---

## VI. Adiabatic Compression and Surface Aerodynamic Heating Equations (Figure 6)

When a rocket moves at extreme velocities through dense air, the air directly ahead of it undergoes intense adiabatic compression, leading to a steep rise in temperature. Let $P_v$ be the air pressure (in standard atmospheres), $T_0$ the absolute ambient temperature, $\rho$ as in formula (34), and $m$ the mean molecular weight of the atmospheric gas.

The adiabatic compression equation is:

$$\frac{T_1}{T_0} = \left(\frac{P_v}{P_0}\right)^{\frac{k-1}{k}}$$

where the isentropic exponent $k = 1.41$. Treating heating as the direct consequence of adiabatic compression, for velocities $v > 700\ \text{m/s}$ (at which $P_v \gg P_0$, representing the lower threshold of applicability for an oxygen-nitrogen atmosphere; for other gases, this limit is proportional to molecular velocity), we obtain:

$$T_1 = 0.09\, T_0\, v^{\frac{2(k-1)}{k}} m^{\frac{k-1}{k}} = 0.09\, T_0\, v^{0.582} m^{0.291} \quad (37)$$

Substituting into equation (37) the average molecular weight of air $m = 29.3$, the variation of stagnation air temperature with flight velocity $v$ is plotted in Figure 6:

![High-speed aerodynamic adiabatic compression temperature curve (Figure 6)](/images/rocket-pioneers/space-fig6.png)  
*Figure 6: Adiabatically compressed air temperature as a function of velocity: $T_1 = 0.09\, T_0\, v^{0.582} m^{0.291}$; $m = 29.3$ (Figure 6)*

Equation (37) and Figure 6 define the air temperature at the normal cross section perpendicular to the trajectory. Such extreme temperatures occur exclusively on the forward stagnation regions—the apex of the nose cone and the leading edges of the wings; whereas along surfaces inclined at an oblique angle to the airflow, dynamic pressure and corresponding local temperatures are markedly lower.

If we shield the forward nose with a refractory, heat-resistant material, the remainder of the vehicle exterior, even when fabricated from ordinary steel, should withstand velocities up to $v = 4500\ \text{m/s}$ without requiring specialized refractory coating. Detailed calculations of the surface temperature of bodies traveling at high speeds are presented in Section IX below.

Here we employ a second estimation approach based on equation (37), incorporating favorable mitigating factors: namely, that our outer skin is not positioned perpendicular to the velocity vector, but maintains a small angle of attack, whereby both the degree of frontal compression and the resulting thermal elevation are substantially mitigated. When the vehicle reaches $v = 4500\ \text{m/s}$, it is already traversing extremely rarified atmospheric layers, and furthermore (as discussed earlier), aerodynamic lifting surfaces are no longer required at this stage.

A parallel experimental fact provides equally reassuring data: dumdum bullets containing a mercury fulminate charge, when fired through the atmosphere at initial velocities up to $v = 700\ \text{m/s}$, do not spontaneously detonate during flight, despite the diminutive size of the projectile and its rapid rate of heating. The deflagration temperature of mercury fulminate is $170^\circ\text{C}$; therefore, the temperature elevation experienced by the bullet during flight does not exceed the ambient air temperature by more than $150^\circ\text{C}$.

We assume that the absolute surface temperature of a moving body is proportional to a power ($p$) of the root-mean-square molecular velocity of the gaseous medium relative to that body. Knowing that at $0^\circ\text{C}$ the average speed of air molecules is $460\ \text{m/s}$, for a bullet traveling at $v = 700\ \text{m/s}$, the mean relative speed of these molecules with respect to the bullet is:

$$v_r = \sqrt{460^2 + 700^2} = 837\ \text{m/s}$$

Setting up the temperature proportionality relation and substituting $T_0 = 300\ \text{K}$ and $T_1 = 450\ \text{K}$, we determine the exponent $p \approx 0.7$. Consequently:

$$T_1 \propto u^{0.7}$$

(where $u$ is the mean velocity of gas molecules relative to the body, and $v$ is the velocity of the body itself). According to this relationship, when flight velocity reaches $v = 4500\ \text{m/s}$ and ambient temperature is $T_0 = 220\ \text{K} = -53^\circ\text{C}$, the calculated surface temperature satisfies:

$$T < 800^\circ\text{C}$$

This temperature remains well within the safe structural tolerance of heat-resistant steel alloys.
