---
title: "7operator"
layout: single-portfolio
excerpt: "<img src='/images/research/nuclear_response.png'>"
collection: research
order_number: 40
date: 2024-04-22
---
<h6>Last update: {{ page.date | date: "%B %d, %Y" }}</h6>

## Intro
It's recommended to read [this post]({{ base_path }}/research/bigstick) about nuclear shell model code BIGSTICK first.

BIGSTICK outputs density matrix (.dres), which basically includes everything. This post will demonstrate how to convert density matrix to nuclear response and scattering cross section

The steps are the following
- Run [res2den.py]({{ base_path }}/research/bigstick_examples/C12_YSOX/res2den.py) to convert to .dat
- Open the mathematica notebook and input the .dat file
- Run the mathematica notebook

Each of the steps will be explained in the next sections

## Python conversion
[res2den.py]({{ base_path }}/research/bigstick_examples/C12_YSOX/res2den.py) converts density matrix from BIGSTICK output (.dres) to mathematica input (.dat).
The script does nothing special but merely reformat the data to be compatible with the mathematica notebook.


## Mathematica package - 7operator
[inelastic_nu_multipole.nb]({{ base_path }}/research/bigstick_examples/C12_YSOX/inelastic_nu_multipole.nb) and [inelastic_DM_multipole.nb]({{ base_path }}/research/bigstick_examples/C12_YSOX/inelastic_DM_multipole.nb) in [C12_YSOX folder]({{ base_path }}/research/bigstick_examples/C12_YSOX/) show examples of inelastic neutrino-C12 scattering and inelastic dark matter-C12 scattering.
In the notebooks, the scattering cross section is expressed by multipole operators, which are made of nuclear response functions.
The mathematica package `7operator` is used to calculate nuclear response function from density matrix.
The instructions and details are included in the notebooks.
I recommend to start with the neutrino, because it's closer to the Standard Model.


## Reference and further reading
- [Cover image source](https://www.researchgate.net/figure/Electroweak-nuclear-response-as-a-function-of-the-energy-transfer-The-dominant-channels_fig1_325873651)
- [7operator script](https://arxiv.org/pdf/0706.2210.pdf)
- [My publication: inelastic nuclear scattering from neutrinos and dark matter](https://inspirehep.net/literature/2097598)
- [Theoretical Nuclear and Subnuclear Physics](https://www.amazon.com/THEORETICAL-NUCLEAR-SUBNUCLEAR-PHYSICS-SECOND/dp/9812387951): chapter 45 and 46 specifically
- [Semileptonic weak interactions with C12](https://inspirehep.net/literature/83069)
- [nuclear physics of dark matter detection](https://www.worldscientific.com/doi/abs/10.1142/S0218301392000023)
- [Weakly interacting massive particle-nucleus elastic scattering response](https://journals.aps.org/prc/abstract/10.1103/PhysRevC.89.065501)
- [Coherent elastic neutrino-nucleus scattering: EFT analysis and nuclear responses](https://arxiv.org/abs/2007.08529)
- [Coherency and incoherency in neutrino-nucleus elastic and inelastic scattering](https://arxiv.org/abs/1806.08768)
- [Elastic and inelastic scattering of neutrinos and weakly interacting massive particles on nuclei](https://arxiv.org/abs/2004.04055)
- [Nuclear responses to astrophysical neutrinos through the neutral Gamow-Teller strength](https://inspirehep.net/literature/2171509)
- [A Model Independent Approach to Inelastic Dark Matter Scattering](https://arxiv.org/abs/1409.0536)
- [Ab initio nuclear response functions for dark matter searches](https://arxiv.org/abs/1612.09165)
- [Model-independent WIMP Scattering Responses and Event Rates: A Mathematica Package for Experimental Analysis](https://arxiv.org/abs/1308.6288)
- [Spin-dependent WIMP scattering off nuclei](https://arxiv.org/abs/1208.1094)
- [Analysis strategies for general spin-independent WIMP–nucleus scattering](https://arxiv.org/abs/1605.08043)
- [Large-scale nuclear structure calculations for spin-dependent WIMP scattering with chiral effective field theory currents](https://arxiv.org/abs/1304.7684)
- [The Effective Field Theory of Dark Matter Direct Detection](https://arxiv.org/abs/1203.3542)
- [Signatures of dark matter scattering inelastically off nuclei](https://arxiv.org/abs/1309.0825)
- [Spin-dependent WIMP-nucleus scattering off 125Te, 129Xe, and 131Xe in the microscopic interacting boson-fermion model](https://www.sciencedirect.com/science/article/pii/S037594741930199X)
- [Inelastic dark matter nucleus scattering](https://arxiv.org/abs/1906.10466)
