---
title: "Part 3 · Chapter 11: Rocket Control, Measurement, and Navigational Instrumentation"
description: "Yu. V. Kondratyuk's \"Conquest of Interplanetary Space\" (1929), Chapter 11: Closed-loop integrating accelerometers, automatic thrust throttling, dual-range apparent weight meters, propellant mass gauges, jet vane gyroscopic stabilization, and autonomous deep-space celestial navigation."
---

# Chapter 11 · Rocket Control, Measurement, and Navigational Instrumentation
### Section XI. Control and Measurement Instruments. Orientation
**By Yuriy Vasil'yevich Kondratyuk (Yu. V. Kondratyuk)**  
*(From NASA TT F-9285, pp. 120–123 / Original work, pp. 80–84)*

---

To achieve active flight guidance, state determination, and spatial orientation/navigation, the spacecraft must be equipped with the following specialized measurement and control instruments:

---

## I. Apparent Weight Indicator (Integrating Spring Accelerometer and Dual-Range Architecture)

The internal apparent weight indicator operates on the physical principle of a **known proof mass suspended by a calibrated spring**, with its pointer directly indicating the instantaneous apparent weight (i.e., apparent acceleration) experienced inside the vehicle.

This indicator should be coupled to a **revolving recording drum driven by a clockwork mechanism**, continuously plotting and preserving a physical trace of acceleration over time. The area bounded beneath the resulting recorded curve is expressed by the integral:

$$\int_0^t (J_0 - J_e)\, dt = v_v - L_d$$

This apparent weight meter must be linked in a closed loop to the **automatic throttling valve** controlling engine thrust output, thereby ensuring that during the active boost interval $I_i$, the acceleration $J_0$ is maintained precisely at the preset design target $J$ (equal to the maximum permissible physiological acceleration $J_{\max}$).

The vehicle should be outfitted with **two distinct sets of such apparent weight indicators**:
1. **High-acceleration indicator**: Designed to measure large accelerations from zero up to the maximum permissible threshold $J_{\max}$ (with a range spanning hundreds to thousands of $\text{cm/s}^2$), dedicated to ground launch ascent and major orbital maneuvers;
2. **Micro-acceleration indicator**: Engineered for high-precision measurement of extremely faint micro-accelerations in the range of $0.01 \sim 10\ \text{cm/s}^2$ (i.e., $10^{-5} \sim 10^{-2}\ g$). This instrument is specifically employed during interplanetary return to measure subtle drag decelerations upon initial grazing contact with the upper rarified atmosphere, as well as for executing minute orbital corrections.

It must be emphasized that attempting to combine the measurement of strong $1000\ \text{cm/s}^2$ accelerations and faint $0.01\ \text{cm/s}^2$ micro-forces within a single mechanical instrument is entirely impractical.

---

## II. Atmospheric Drag Sensors and Propellant Mass Consumption Gauges

### 2. Atmospheric Drag Sensor
Constructed as a specialized sensor plate protruding from the outer hull into the windward airstream, connected via mechanical transmission cables to an internal force-sensing dynamometer. Because mechanical linkages unavoidably introduce friction, such external air plates lack sufficient sensitivity during the earliest grazing phase through the extreme upper atmosphere, and therefore cannot replace the high-sensitivity micro-accelerometer during initial entry.

### 3. Rocket Mass Gauge (Thrust and Characteristic Velocity Computing System)
Utilizing high-precision propellant flowmeters and totalizers, this instrument continuously displays the instantaneous total mass of the rocket $M(t)$ as a function of consumed propellant.

By linking these instruments mechanically or electrically, vital ballistic parameters can be automatically resolved:
* **Coupling the second instrument (aerodynamic drag $F_{\text{drag}}$) with the third instrument (instantaneous mass $M$)**: Yields a real-time computation of the deceleration induced purely by atmospheric resistance, $a_{\text{drag}} = F_{\text{drag}} / M$;
* **Synthesizing this drag deceleration with the first instrument (total apparent vehicle acceleration)**: Allows exact isolation of the **intrinsic rocket acceleration** $j_u$ generated solely by engine reactive thrust;
* **Continuously integrating this intrinsic acceleration over time**: Namely $\int j_u\, dt$, the instrumentation directly displays in real time the **total effective characteristic velocity $W$** imparted to the craft by the engines!

---

## III. Gyroscopic Stabilization, Jet Vanes, and Autonomous Deep-Space Celestial Navigation

### 1. Roll Stabilization and Elimination of Parasitic Spin
To automatically prevent uncommanded roll rotation about the rocket's longitudinal axis (a parasitic spin frequently induced by minor manufacturing asymmetries or slight aerodynamic and thrust misalignments), the rocket must incorporate a **free gyroscope whose spin axis is aligned perpendicular to the rocket's longitudinal axis**.

The gimbaled spin axis maintains inertial orientation in space. Its relative angular displacement with respect to the airframe directly drives and commands a set of **rotatable deflectors (gas rudders / jet vanes) inserted into the high-temperature exhaust jet of the engine**. By deflecting the exhaust stream asymmetrically, these jet vanes generate an immediate restorative roll torque that neutralizes unwanted spin.

### 2. Pitch/Yaw Stabilization and Programmed Trajectory Steering
To maintain stable spatial pointing of the longitudinal axis, or to execute programmed turns along a predetermined orbital profile, the vehicle must be equipped with a **second gyroscope**.

The axis of this gyroscope is aligned parallel to the longitudinal axis of the rocket, with its output controlling another set of steerable jet vanes in the engine exhaust, providing fully autonomous closed-loop servo control of pitch and yaw attitudes in the vacuum of space.

### 3. Deep-Space Autonomous Celestial Navigation
To provide the crew with dependable spatial position fixing and dead reckoning, specialized compact astronomical instruments and rapid ephemeris reduction methods must be developed. These will enable astronauts to determine the rocket's spatial coordinates and osculating orbital elements relative to Earth rapidly and with high precision.

Such autonomous celestial position determination is exceptionally critical immediately prior to entering the atmosphere to dissipate return velocity, imposing the most stringent demands on angular sighting and orbital calculation precision.

Finally, during unpowered free-coasting phases in deep space, the vehicle can deploy tethered counterweights or momentum transfer mechanisms (as discussed on pages 107–109) to further enhance the passive pointing stability of the rocket's major axis in inertial space.
