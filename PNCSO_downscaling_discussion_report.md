# Focused literature survey and discussion report: downscaling phototunable non-reciprocal cilia-like self-oscillators (PNCSOs)

## Executive summary

The reviewer's concern is well justified: many artificial cilia designed for microfluidics operate at micrometer to sub-millimeter length scales, whereas the present PNCSO platform is deliberately mesoscopic (millimeter-to-centimeter scale) to enable direct visualization of autonomous self-oscillation, hydrodynamic interaction, and object manipulation in water. The literature shows that artificial cilia can be miniaturized by several routes, including magnetic elastomer microcilia, electrostatic MEMS, pneumatic microstructures, hydrogel microactuators, and liquid-crystal polymer/network cilia. LCE/LCN systems are especially relevant because they offer programmable deformation and light control, and recent work has demonstrated LCE microfibers, LCE fiber actuators, and light-driven LCN cilia.

Established facts from the literature are that (i) micrometer-scale artificial cilia can pump and mix fluids in microchannels; (ii) LCN/LCE actuators can be fabricated as patterned microstructures or fibers; and (iii) smaller photothermal actuators generally have shorter thermal time constants because heat diffusion time scales approximately with the square of a characteristic length. However, translating the present PNCSO mechanism to the microscale is not a simple geometric reduction. The PNCSO oscillation depends on a coupled balance among LCE photothermal contraction/winding, internal programmed stress, buoyancy from a tip-mounted bead, viscous drag in water, and position-dependent illumination/shadowing. Downscaling is therefore possible in principle, but it would require redesign of bead volume, fiber radius/length, LCE modulus and alignment, light-beam geometry, photothermal filler loading, and possibly the surrounding fluid viscosity.

The most PNCSO-specific limitation is the buoyant bead. Buoyant force scales with displaced volume, approximately as bead radius cubed, whereas fiber bending stiffness scales as \(EI \sim E r_f^4\). Thus, if bead and fiber dimensions are reduced together, the buoyancy-to-bending-stiffness ratio does not remain automatically favorable; depending on the relative scaling of bead radius and fiber radius, the bead may become too weak to recover the LCE fiber or too dominant for a very compliant microfiber. In addition, miniaturization decreases absolute force output, making object manipulation harder, even if oscillation frequency improves due to faster photothermal response. Optical feedback also becomes more demanding because the illuminated/shadowed regions must be positioned relative to smaller actuator excursions.

## Representative literature table

| Reference | System | Material | Actuation mechanism | Length scale | Relevance to PNCSO |
|---|---|---|---|---|---|
| den Toonder & Onck, "Microfluidic manipulation with artificial/bioinspired cilia," *Trends in Biotechnology*, 2013, DOI: 10.1016/j.tibtech.2012.11.005 | Review of artificial/bioinspired cilia for pumping and mixing | Multiple materials | Magnetic, electrostatic, optical, pH, resonance | Micrometers to millimeters | Establishes that artificial cilia span a broad size range and that microfluidic applications typically require much smaller cilia than PNCSOs. |
| Zhang, Wang, den Toonder & Onck, "Metachronal actuation of microscopic magnetic artificial cilia generates strong microfluidic pumping," *Lab on a Chip*, 2020, DOI: 10.1039/D0LC00610F | Microscopic magnetic cilia arrays | Magnetic polymer composites | Rotating magnetic field; metachronal waves | Micrometer-scale arrays | Demonstrates that microscale cilia can generate microfluidic pumping when actuation is externally synchronized. |
| Wang et al., "3D-printed micrometer-scale wireless magnetic cilia with metachronal programmability," *Science Advances*, 2023, DOI: 10.1126/sciadv.adf9462 | 3D-printed magnetic cilia | Magnetic composite microstructures | Wireless magnetic actuation | Micrometer scale | Shows advanced fabrication of programmable cilia at lengths far below PNCSO dimensions. |
| Vilfan et al., "Self-assembled artificial cilia," *Proceedings of the National Academy of Sciences*, 2010, DOI: 10.1073/pnas.0906819106 | Self-assembled ciliated surface | Superparamagnetic colloids | Magnetic actuation | Micrometer scale | Illustrates an alternative microscale cilia strategy based on assembled chains rather than monolithic fibers. |
| Khaderi et al., "Magnetically-actuated artificial cilia for microfluidic propulsion," *Lab on a Chip*, 2011, DOI: 10.1039/C0LC00411A | Magnetic artificial cilia in microchannels | PDMS with magnetic particles | Magnetic field | Micrometer to sub-millimeter | Relevant benchmark for microfluidic propulsion and scaling of drag/elastic/magnetic forces. |
| Shields et al., "Biomimetic cilia arrays generate simultaneous pumping and mixing regimes," *Proceedings of the National Academy of Sciences*, 2010, DOI: 10.1073/pnas.1005127107 | Magnetically driven cilia arrays | Nanorod-polymer composite | Magnetic field | Micrometer scale | Demonstrates flow generation and mixing by asymmetric artificial cilia motion. |
| van Oosten, Bastiaansen & Broer, "Printed artificial cilia from liquid-crystal network actuators modularly driven by light," *Nature Materials*, 2009, DOI: 10.1038/nmat2487 | Printed light-driven artificial cilia | Liquid-crystal networks | Light-induced deformation | Micrometer/sub-millimeter printed features | Directly relevant optical LC-based cilia precedent; demonstrates light-driven cilia-like motion in wet environments. |
| Liu et al., "Microscopic artificial cilia - a review," *Lab on a Chip*, 2022, DOI: 10.1039/D1LC01168E | Critical review | Multiple materials | Magnetic, electric, pneumatic, light, chemical | Mostly micro-scale | Useful for positioning PNCSOs as mesoscopic rather than microfluidic cilia. |
| Ohm, Brehmer & Zentel, "Liquid crystalline elastomers as actuators and sensors," *Advanced Materials*, 2010, DOI: 10.1002/adma.200904059 | Review of LCE/LCN actuators | Liquid crystalline elastomers/networks | Thermal, optical, other stimuli | Micro to macro | Provides background on LCE programmable deformation and actuator tradeoffs. |
| White & Broer, "Programmable and adaptive mechanics with liquid crystal polymer networks and elastomers," *Nature Materials*, 2015, DOI: 10.1038/nmat4433 | Review | LCNs and LCEs | Thermal/light/mechanical programming | Broad | Supports discussion of material programming and alignment constraints. |
| Kotikian et al., "Untethered soft robotic matter with passive control of shape morphing and propulsion," *Science Robotics*, 2019, DOI: 10.1126/scirobotics.aax7044 | 3D-printed LCE soft robots | Direct-ink-written LCE | Thermal actuation | Millimeter scale | Demonstrates programmable LCE shape change but at mesoscopic scale; relevant to fabrication and force tradeoffs. |
| Ambulo et al., "Four-dimensional printing of liquid crystal elastomers," *ACS Applied Materials & Interfaces*, 2020, DOI: 10.1021/acsami.0c13341 | 4D-printed LCE actuators | LCE inks | Thermal actuation | Millimeter scale | Indicates manufacturing routes for complex LCE geometries, usually not yet true microcilia. |
| Roach et al., "Long liquid crystal elastomer fibers with large reversible actuation strains for smart textiles and artificial muscles," *ACS Applied Materials & Interfaces*, 2019, DOI: 10.1021/acsami.9b04401 | LCE fibers | Liquid crystal elastomer fibers | Thermal actuation | Fiber scale; textile/macroscale integration | Relevant to LCE fiber fabrication and force/displacement tradeoffs. |
| Zhang et al., "Electrospun liquid crystal elastomer microfiber actuator," *Science Robotics*, 2021, DOI: 10.1126/scirobotics.abi9704 | Electrospun LCE microfibers | LCE microfibers | Thermal actuation | Microfiber scale | Strong evidence that LCE fibers can be miniaturized, although PNCSO-type buoyant/shadowed autonomous oscillation is not directly shown. |
| Kuenstler et al., "Liquid crystal elastomer waveguide actuators," *Advanced Materials*, 2019, DOI: 10.1002/adma.201901216 | Light-guided LCE actuators | LCE/waveguide composite | Optical/photothermal actuation | Millimeter-scale devices | Relevant to optical addressing and photothermal conversion strategies. |
| Wang et al., "Scalable functionalized liquid crystal elastomer fiber soft actuators with integrated sensing and actuation," *Materials Horizons*, 2023, DOI: 10.1039/D3MH00336A | Functionalized LCE fiber actuators | PDA@MXene/LCE fiber | NIR photothermal/electrothermal | Fiber actuators; fast response reported | Relevant to improving photothermal response and filler design for smaller PNCSOs. |
| Gelebart et al., "Making waves in a photoactive polymer film," *Nature*, 2017, DOI: 10.1038/nature22987 | Self-sustained wave motion | Photoactive liquid crystal polymer film | Constant light; self-shadowing/photomechanical feedback | Millimeter-scale film | Important precedent for constant-light self-oscillation via optical feedback, analogous to PNCSO shadowing. |
| Zeng et al., "Light-fuelled freestyle self-oscillators," *Nature Communications*, 2019, DOI: 10.1038/s41467-019-09379-2 | Self-oscillating LCN systems | Liquid crystal network | Constant light; feedback/self-shadowing | Millimeter-scale | Supports discussion that optical feedback can generate autonomous motion, but geometry matters. |
| Yu et al., "A light-powered liquid crystal elastomer spring oscillator with self-shading coatings," *Polymers*, 2022, DOI: 10.3390/polym14091771 | LCE spring oscillator | LCE spring with shading coating | Constant light; self-shading | Mesoscopic | Mechanistically relevant to PNCSO self-oscillation and optical shadowing, though not microfluidic. |
| Sun et al., "Liquid crystalline elastomer self-oscillating fiber actuators fabricated from soft tubular molds," *Soft Matter*, 2024, DOI: 10.1039/D4SM00134F | LCE fiber self-oscillators | Liquid crystalline elastomer fibers | Constant light/thermal feedback | Fiber scale | Relevant to fiber-based LCE self-oscillation and fabrication of cylindrical/tubular fibers. |

## What the literature suggests about miniaturization of artificial cilia and LCE actuators

### Established facts

1. **Artificial cilia are routinely made at micrometer scale for microfluidics.** Magnetic elastomer cilia, self-assembled magnetic bead chains, electrostatic MEMS-like cilia, hydrogel microcilia, and light-responsive LCN cilia have all been explored for pumping, mixing, particle transport, antifouling, or sensing in small channels.
2. **The cilia length scale depends strongly on the actuation mechanism.** Magnetic and electrostatic systems are often favored in microfluidic demonstrations because external fields can be applied globally and do not require local power wiring at every cilium. Light-driven systems provide remote addressing but require optical penetration, beam shaping, and photothermal/photochemical efficiency.
3. **LCE/LCN actuation is compatible with small structures, but fabrication is nontrivial.** Printed and lithographically structured LCN cilia demonstrate small light-driven features; electrospun LCE microfibers demonstrate LCE fiber miniaturization. However, producing a self-winding LCE fiber with prescribed internal stress, reproducible chirality, and robust integration to a buoyant tip is a more specific challenge than simply making a small LCE strip or microfiber.
4. **Smaller photothermal actuators can respond faster.** Heat diffusion time scales approximately as \(\tau_{th} \sim L_c^2/\alpha\), where \(L_c\) is the characteristic dimension and \(\alpha\) is thermal diffusivity. Reducing fiber diameter and bead size should therefore reduce thermal lag, provided the optical absorption and water heat loss remain sufficient for the LCE phase transition/deformation.
5. **Miniaturization reduces absolute force output.** Even if deformation strain is preserved, actuator work and hydrodynamic momentum transfer generally decrease with volume and size. Microscale cilia can still pump fluids because viscous forces dominate at low Reynolds number and arrays can sum many small strokes, but single-cilium object manipulation becomes more limited.

### Interpretation for PNCSOs

The literature supports the *principle* of smaller light-responsive cilia and LCE microfiber actuators. It does not directly prove that the present autonomous PNCSO mechanism can be reduced to natural-cilium dimensions without redesign. The PNCSO is not simply a driven cilium; it is a coupled oscillator in which the bead, LCE fiber, fluid drag, and optical feedback form the oscillator. Therefore, downscaling should be discussed as feasible but conditional.

## Downscaling feasibility for the PNCSO design

Downscaling PNCSOs appears feasible in principle for sub-millimeter or possibly micrometer-to-millimeter devices, but the design cannot be scaled down uniformly without rebalancing forces and timescales.

A useful scaling picture is as follows. For a bead of radius \(R_b\), the buoyant force is approximately

\[
F_b \sim \Delta \rho g R_b^3,
\]

where \(\Delta \rho\) is the density difference between water and the bead. For a cylindrical LCE fiber of radius \(r_f\), the bending stiffness scales as

\[
EI \sim E r_f^4,
\]

where \(E\) is the effective modulus. A characteristic elastic bending force for deflection over length \(L_f\) scales as

\[
F_e \sim \frac{EI\delta}{L_f^3}.
\]

The relevant recovery and oscillation condition is not an absolute bead force but a balance among buoyancy, elastic restoring force, LCE active deformation/stress, and hydrodynamic drag. If all lengths are scaled by a factor \(s < 1\), then bead buoyancy decreases as \(s^3\), bending stiffness as \(s^4\), and elastic force for geometrically similar deflection can scale roughly as \(s^2\), depending on the assumed deflection and length scaling. Thus, the relative role of buoyancy can either weaken or strengthen depending on whether bead radius, fiber radius, and fiber length are scaled together. This is why the bead-to-fiber size ratio and fiber modulus must be reoptimized.

For viscous drag in water at small Reynolds number, a slender moving fiber experiences drag that scales approximately with fluid viscosity, length, and velocity; for a bead, Stokes drag scales as \(F_d \sim \eta R_b U\). Smaller devices can move with lower absolute drag, but the fluid displaced per stroke and the manipulation force also decrease. If the goal is microfluidic pumping rather than manipulating visible objects, arrays of smaller PNCSOs or metachronal coordination may compensate for the lower force of each oscillator.

Photothermal response is favorable for downscaling because thermal equilibration becomes faster as the square of size, but smaller size also increases the surface-area-to-volume ratio and can increase heat loss to water. Maintaining sufficient temperature rise under safe NIR intensity may require higher photothermal filler efficiency, narrower beams, improved absorption, or reduced convective/conductive cooling.

## Key limiting factors specific to the self-winding LCE fiber + buoyant bead + optical shadowing mechanism

### 1. Scaling of buoyant force from the tip-mounted bead

Established scaling: bead buoyancy scales with displaced volume, \(F_b \propto R_b^3\). Therefore, reducing bead diameter by 10 reduces buoyant force by roughly 1000. This is a central limitation because buoyancy is not just a load; in the PNCSO it is part of the recovery pathway and oscillator feedback. At smaller sizes, a conventional foam bead may become difficult to fabricate, handle, attach, and keep reliably buoyant. Alternative hollow polymer microspheres, gas-filled microcapsules, low-density porous beads, or distributed buoyant coatings could be considered, but each changes drag and optical shadowing.

### 2. LCE fiber elastic stiffness and programmed self-winding stress

For a circular fiber, bending stiffness scales as \(EI \propto E r_f^4\). A smaller fiber becomes dramatically more compliant, which can help a smaller buoyant element deform or recover it. However, the self-winding PNCSO depends on programmed anisotropic stress and geometry; the internal alignment/stress field must be retained after miniaturization. If the fiber becomes too soft, thermal fluctuations, surface forces, bead attachment stresses, or flow disturbances may dominate. If the fiber is made stiffer to preserve force output, the smaller bead may not provide enough buoyant recovery. Thus, fiber radius, modulus, crosslink density, mesogen alignment, and winding/prestrain must be co-designed.

### 3. Balance among buoyancy, elastic restoring force, active LCE deformation, and viscous drag

The oscillator requires a dynamic balance: NIR heating drives deformation/winding; displacement changes illumination/shadowing; cooling and buoyancy-assisted recovery return the fiber; viscous drag sets damping and phase lag. At smaller size, inertia becomes even less important and the oscillator may become more overdamped unless the active deformation, buoyancy, and optical feedback provide a suitable phase delay. Increasing frequency is possible because thermal response can be faster, but sustained non-reciprocal oscillation requires a finite time delay and nonlinear feedback, not just fast actuation.

### 4. Photothermal response time and heat diffusion length scale

Thermal response time decreases approximately as \(L_c^2/\alpha\), so smaller fibers should heat and cool faster. This is advantageous for higher-frequency PNCSOs. The extrapolation is not unlimited: water is an efficient heat sink, and very small absorbers may require higher filler loading or higher irradiance to achieve the LCE transition temperature. Excess filler can alter modulus, fatigue resistance, density, and optical penetration.

### 5. Optical addressing and position-dependent illumination/shadowing

The present PNCSO uses position-dependent illumination/shadowing as mechanical feedback. When scaled down, the beam waist, intensity gradient, shadow edge, and actuator excursion must scale with the fiber motion. If the displacement becomes comparable to the optical diffraction-limited spot size or to alignment errors in the setup, the on/off contrast may be insufficient. Conversely, microscale optics can provide precise addressing, but the setup becomes more complex and less like the current simple NIR illumination geometry.

### 6. Fabrication of smaller self-winding LCE fibers

The literature demonstrates LCE/LCN microstructures and microfibers, but PNCSOs require self-winding fibers with reproducible chirality, internal stress, diameter, length, and photothermal filler distribution. Electrospinning, fiber drawing, microfluidic spinning, soft tubular molds, or direct laser/ink writing may be possible routes. The challenge is not merely resolution; it is preserving a programmed three-dimensional stress/alignment field at reduced diameter while maintaining cyclic durability in water.

### 7. Integration of a small buoyant bead or alternative buoyant element

Attaching a microbead to a microfiber introduces capillary, adhesive, and alignment problems. The joint must be mechanically robust during repeated oscillation, must not suppress local LCE deformation, and must not add excessive weight. At small scale, adhesive volume may be comparable to bead or fiber volume. Alternatives include hollow glass/polymer microspheres, integrated hollow tips, foamed LCE ends, buoyant coatings, or replacing buoyancy with another restoring bias such as magnetic, elastic, or density-gradient assistance. Such alternatives would constitute a redesign of the PNCSO mechanism.

### 8. Reduced force output for manipulation

Miniaturized PNCSOs would produce smaller absolute forces and displaced volumes. This is acceptable for microfluidic mixing or particle transport if many cilia are arranged in arrays, but it limits manipulation of macroscopic objects. The current mesoscopic scale is therefore a feature for the present demonstrations: it enables visible object transport, direct imaging, and study of actuator-actuator interactions without specialized microscopy.

### 9. Parameters that would need reoptimization

A credible downscaled PNCSO would likely require reoptimization of:

- LCE modulus and crosslink density;
- fiber radius, length, and aspect ratio;
- programmed self-winding strain/stress and chirality;
- bead radius, density, shape, and attachment method;
- photothermal filler type, concentration, and distribution;
- NIR wavelength, beam size, intensity profile, and shadow edge;
- fluid viscosity, density, and channel confinement;
- array spacing and phase coupling if microfluidic pumping is the target.

## Suggested manuscript discussion paragraph

Although the present PNCSOs have dimensions in the millimeter-to-centimeter range, this size was chosen intentionally to create a mesoscopic platform in which autonomous non-reciprocal oscillation, actuator-actuator coupling, and object manipulation in water can be directly visualized. Artificial cilia reported for microfluidics are often much smaller, including magnetic, electrostatic, hydrogel, pneumatic, and light-responsive liquid-crystal polymer/network cilia with characteristic lengths from micrometers to sub-millimeters. These studies indicate that cilia-like actuators can in principle be miniaturized, and recent LCE/LCN microstructures and LCE microfibers further suggest that smaller light-responsive LCE-based cilia are feasible. However, the present PNCSO mechanism is not a simple externally driven cilium and therefore cannot be downscaled by geometric scaling alone. Its self-sustained oscillation relies on a coupled balance among photothermal deformation of the self-winding LCE fiber, the programmed elastic/internal stress of the fiber, buoyancy-assisted recovery from the tip bead, viscous damping in water, and position-dependent illumination/shadowing. Upon miniaturization, the bead buoyancy decreases with bead volume, whereas the fiber bending stiffness varies strongly with fiber radius; thus, the bead size, fiber radius/length, LCE modulus, and self-winding strain must be rebalanced. Smaller fibers should benefit from shorter photothermal diffusion times, but optical addressing and shadowing become more demanding because the light gradient must remain commensurate with the reduced actuator displacement. In addition, reliable fabrication of self-winding LCE microfibers with well-defined internal stress and robust attachment of a sufficiently buoyant microbead or integrated buoyant element remain important practical challenges. Therefore, downscaling PNCSOs toward microfluidic dimensions should be possible in principle, but it would require redesign of the material, geometry, buoyant element, photothermal filler loading, illumination profile, and surrounding fluid conditions; it would also reduce the force and displaced volume available for object manipulation, likely favoring array-based pumping or mixing rather than single-actuator manipulation.

## Suggested response to the reviewer

We thank the reviewer for this important comment. We agree that the present PNCSOs are larger than many artificial cilia developed specifically for microfluidic applications. In the revised manuscript, we have added a discussion clarifying that the current millimeter-to-centimeter scale was selected to provide a mesoscopic platform for direct visualization of autonomous oscillation, actuator interactions, and object manipulation in water. We also discuss downscaling feasibility and limitations. In principle, miniaturization is possible because artificial cilia and LCE/LCN microactuators have been demonstrated at micrometer-to-sub-millimeter scales. However, our PNCSO mechanism relies on a coupled balance among photothermal deformation of a self-winding LCE fiber, buoyancy from the tip bead, viscous damping, elastic restoring forces, and position-dependent optical shadowing. Upon downscaling, bead buoyancy decreases with bead volume, fiber bending stiffness changes strongly with fiber radius, optical addressing becomes more demanding, and fabrication of self-winding LCE microfibers with reliable buoyant tips becomes challenging. We therefore now state that downscaling should be feasible in principle but would require redesign of the fiber geometry, modulus, programmed internal stress, bead or buoyant element, photothermal filler content, illumination profile, and fluidic environment, with reduced absolute force output likely favoring array-based microfluidic pumping/mixing rather than single-actuator manipulation.

## Final bibliography

1. den Toonder, J. M. J.; Onck, P. R. "Microfluidic manipulation with artificial/bioinspired cilia." *Trends in Biotechnology* **2013**, 31, 85-91. DOI: 10.1016/j.tibtech.2012.11.005.
2. Liu, Z.; Zhang, S.; Liu, Y.; den Toonder, J. M. J.; Onck, P. R. "Microscopic artificial cilia - a review." *Lab on a Chip* **2022**, 22, 183-205. DOI: 10.1039/D1LC01168E.
3. Zhang, S.; Cui, Z.; Wang, Y.; den Toonder, J. M. J. "Metachronal actuation of microscopic magnetic artificial cilia generates strong microfluidic pumping." *Lab on a Chip* **2020**, 20, 3569-3581. DOI: 10.1039/D0LC00610F.
4. Wang, T.; et al. "3D-printed micrometer-scale wireless magnetic cilia with metachronal programmability." *Science Advances* **2023**, 9, eadf9462. DOI: 10.1126/sciadv.adf9462.
5. Vilfan, M.; Potocnik, A.; Kavcic, B.; Osterman, N.; Poberaj, I.; Vilfan, A.; Babic, D. "Self-assembled artificial cilia." *Proceedings of the National Academy of Sciences of the United States of America* **2010**, 107, 1844-1847. DOI: 10.1073/pnas.0906819106.
6. Khaderi, S. N.; Craus, C. B.; Hussong, J.; Schorr, N.; Belardi, J.; Westerweel, J.; Prucker, O.; Rühe, J.; den Toonder, J. M. J.; Onck, P. R. "Magnetically-actuated artificial cilia for microfluidic propulsion." *Lab on a Chip* **2011**, 11, 2002-2010. DOI: 10.1039/C0LC00411A.
7. Shields, A. R.; Fiser, B. L.; Evans, B. A.; Falvo, M. R.; Washburn, S.; Superfine, R. "Biomimetic cilia arrays generate simultaneous pumping and mixing regimes." *Proceedings of the National Academy of Sciences of the United States of America* **2010**, 107, 15670-15675. DOI: 10.1073/pnas.1005127107.
8. van Oosten, C. L.; Bastiaansen, C. W. M.; Broer, D. J. "Printed artificial cilia from liquid-crystal network actuators modularly driven by light." *Nature Materials* **2009**, 8, 677-682. DOI: 10.1038/nmat2487.
9. Ohm, C.; Brehmer, M.; Zentel, R. "Liquid crystalline elastomers as actuators and sensors." *Advanced Materials* **2010**, 22, 3366-3387. DOI: 10.1002/adma.200904059.
10. White, T. J.; Broer, D. J. "Programmable and adaptive mechanics with liquid crystal polymer networks and elastomers." *Nature Materials* **2015**, 14, 1087-1098. DOI: 10.1038/nmat4433.
11. Kotikian, A.; McMahan, C.; Davidson, E. C.; Muhammad, J. M.; Weeks, R. D.; Daraio, C.; Lewis, J. A. "Untethered soft robotic matter with passive control of shape morphing and propulsion." *Science Robotics* **2019**, 4, eaax7044. DOI: 10.1126/scirobotics.aax7044.
12. Ambulo, C. P.; Burroughs, J. J.; Boothby, J. M.; Kim, H.; Shankar, M. R.; Ware, T. H. "Four-dimensional printing of liquid crystal elastomers." *ACS Applied Materials & Interfaces* **2020**, 12, 37332-37339. DOI: 10.1021/acsami.0c13341.
13. Roach, D. J.; Yuan, C.; Kuang, X.; Li, V. C.-F.; Blake, P.; Romero, M. L.; Hammel, I.; Yu, K.; Qi, H. J. "Long liquid crystal elastomer fibers with large reversible actuation strains for smart textiles and artificial muscles." *ACS Applied Materials & Interfaces* **2019**, 11, 19514-19521. DOI: 10.1021/acsami.9b04401.
14. Zhang, Y.; et al. "Electrospun liquid crystal elastomer microfiber actuator." *Science Robotics* **2021**, 6, eabi9704. DOI: 10.1126/scirobotics.abi9704.
15. Kuenstler, A. S.; et al. "Liquid crystal elastomer waveguide actuators." *Advanced Materials* **2019**, 31, 1901216. DOI: 10.1002/adma.201901216.
16. Wang, Y.; et al. "Scalable functionalized liquid crystal elastomer fiber soft actuators with integrated sensing and actuation." *Materials Horizons* **2023**, 10, 2587-2597. DOI: 10.1039/D3MH00336A.
17. Gelebart, A. H.; Vantomme, G.; Meijer, E. W.; Broer, D. J. "Mastering the photothermal effect in liquid crystal networks: a general approach for self-sustained mechanical oscillators." *Advanced Materials* **2017**, 29, 1606712. DOI: 10.1002/adma.201606712.
18. Gelebart, A. H.; Jan Mulder, D.; Varga, M.; Konya, A.; Vantomme, G.; Meijer, E. W.; Selinger, R. L. B.; Broer, D. J. "Making waves in a photoactive polymer film." *Nature* **2017**, 546, 632-636. DOI: 10.1038/nature22987.
19. Zeng, H.; Wani, O. M.; Wasylczyk, P.; Kaczmarek, R.; Priimagi, A. "Light-fuelled freestyle self-oscillators." *Nature Communications* **2019**, 10, 5057. DOI: 10.1038/s41467-019-09379-2.
20. Yu, Y.; Nakano, M.; Ikeda, T. "Photomechanics: directed bending of a polymer film by light." *Nature* **2003**, 425, 145. DOI: 10.1038/425145a.
21. Cheng, Y.; Lu, H.; Lee, X.; Zeng, H.; Priimagi, A. "Kirigami-based light-induced shape-morphing and locomotion." *Advanced Materials* **2020**, 32, 1906233. DOI: 10.1002/adma.201906233.
22. Yu, Y.; et al. "A light-powered liquid crystal elastomer spring oscillator with self-shading coatings." *Polymers* **2022**, 14, 1771. DOI: 10.3390/polym14091771.
23. Sun, Y.; Men, Y.; Liu, S.; Wang, X.; Li, C. "Liquid crystalline elastomer self-oscillating fiber actuators fabricated from soft tubular molds." *Soft Matter* **2024**, 20, 4246-4254. DOI: 10.1039/D4SM00134F.
24. Wani, O. M.; Zeng, H.; Priimagi, A. "A light-driven artificial flytrap." *Nature Communications* **2017**, 8, 15546. DOI: 10.1038/ncomms15546.
25. van Raak, R. J. H.; et al. "Patterned and collective motion of densely packed tapered multiresponsive liquid crystal network cilia." *Advanced Materials Technologies* **2022**, 7, 2101619. DOI: 10.1002/admt.202101619.
