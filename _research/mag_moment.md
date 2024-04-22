---
title: "Nuclear magnetic moment"
layout: single-portfolio
excerpt: "<img src='/images/research/mag-moment.png'>"
collection: research
order_number: 40
date: 2024-04-22
---
<h6>Last update: {{ page.date | date: "%B %d, %Y" }}</h6>
A nucleus consists of one or more nucleon. Each nucleon carry two types of magnetic moment: orbital magnetic moment $\mu_l$ and spin magnetic moment $\mu_s$

$$
\begin{align}
\mu_l &= -g_l {e \over 2m_e} l \\
\mu_s &= -g_s {e \over 2m_e} s
\end{align}
$$

Nuclear magnetic moment vector $\vec{\mu} = g_l \vec{l} + g_s \vec{s}$

Nuclear magnetic moment $\mu$
$$
\begin{align}
\mu &= \langle (l,s),j,m_j=j | \mu_z | (l,s),j,m_j=j \rangle \\
&= \langle (l,s),j,m_j=j | \vec{\mu} \cdot \hat{j} | (l,s),j,m_j=j \rangle
\end{align}
$$

We have

$$
{\mu \over \mu_N} = {g_s\left[j(j+1)+s(s+1)-l(l+1)\right] + g_l \left[ j(j+1)+l(l+1)-s(s+1) \right] \over 2(j+1)}
$$
where $\mu_N={e \hbar \over 2m_p}$ is nuclear magneton (do not confuse with Bohr magneton $\mu_B={e \hbar \over 2m_e}$).
Since the paired nucleons will cancel out each other, we only need to calculate the unpair ones

$$
{\mu \over \mu_N} =
\begin{cases}
    g_l \,l + {1\over2} g_s &\quad j=l+{1\over2} \\
    {j\over j+1} \left[ g_l\, (l+1) - {1\over2}g_s \right]  &\quad j=l-{1\over2}
\end{cases}
$$


## ${\mu \over \mu_N}$ value table

| orbit | proton | neutron |
| ----  | - | - |
|  $0g_{7/2}$  | 3.007  | 0.5417 |
|  $1d_{5/2}$  | 3.851  | -0.9765 |
|  $0h_{11/2}$ | 7.2415 | -1.155 |
|  $1d_{3/2}$  | 0.8304 | 0.5829 |
|  $2s_{1/2}$  | 1.782  | -1.005 |


## More accurate calculation
[PhysRevC.71.044317](https://journals.aps.org/prc/pdf/10.1103/PhysRevC.71.044317) calculates effective $g$ factor using nuclear shell model.
Take $0g_{7/2}$ for an example. The table IV shows

|  | proton | neutron |
| ----  | - | - |
|  $g_s$  | 5.587  | -3.826 |
|  $g_l$  | 1  | 0 |
|  $\delta g_s$  | -2.19  | 1.933 |
|  $\delta g_l$  | 0.113  | -0.05 |

The new $g_l \rightarrow g_{l_\text{eff}}=g_l + \delta g_l$ and $g_s \rightarrow g_{s_\text{eff}}=g_s + \delta g_s$ can then be inserted to the formulae above to have a more precise estimation.


## Reference and further reading
- [Cover image source](https://www.researchgate.net/figure/Nuclear-magnetic-moment-vectors-a-pointing-in-random-directions-and-b-aligned-in_fig1_268291283)
- [PhysRevC.71.044317](https://journals.aps.org/prc/pdf/10.1103/PhysRevC.71.044317)
