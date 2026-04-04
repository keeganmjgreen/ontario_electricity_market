---
fonts:
    sans: Archivo
transition: slide-left
layout: cover
background: img/tahoe-groeger-ioCEgIFVLos-unsplash-blur.jpg
---

<style>
    h1 {
        font-family: Instrument Serif;
    }
    img {
        border-radius: 15px;
        padding: 10px;
    }
</style>

# How Electricity Markets Work

## With **Keegan Trujillo-Green**

<br><br><br><br><br><br><br><br><br><br><br><br>

<small style="color: gray;">Original photo by [Tahoe Groeger on Unsplash](https://unsplash.com/@matinar).</small>

---
layout: section
---

## **Part I**

# Introduction to Wholesale <br> Electricity Markets

---
layout: image
image: img/arturo-castaneyra-oBUUbfmHKwM-unsplash-blur.jpg
---

# The Electrical Grid

<v-clicks>

- Systems we rely on every day:

    - The internet
    - The water supply network
    - The electrical grid

- When these systems work, we often take them for granted

- When they fail, we realize how dramatically they improve our quality of life

- What happens when you turn a light on?

    - Over a hundred years of human innovation kick in
    - Transmission and distribution lines supply more current
    - Generators work harder to supply that extra power

</v-clicks>

<small style="color: gray;">Original photo by [Arturo Castaneyra on Unsplash](https://unsplash.com/@arturokst).</small>

---
layout: image-right
image: img/1912EnV114-p142.jpg
---

# The Electrical Grid --- <br> A Brief History

<v-clicks>

- Late 1800s -- early 1900s in US and UK
- Supply and demand initially co-located
- Private utility companies formed
- Some utilities began interconnecting their systems
- Nationalization in UK and France: regional grids $\to$ nationwide grids
- By 1960: nationwide grids across much of Europe

</v-clicks>

<br>

<small style="color: gray;">Photo from [Grace's Guide To British Industrial History](https://www.gracesguide.co.uk/Deptford_Generating_Station).</small>
<!-- https://unsplash.com/s/photos/power-exchanger -->

---
layout: image
image: img/austin-hervias-VLpWpv3oDB4-unsplash-flipped.jpg
---

# The Wholesale Electricity Market

AKA Power Exchange (PX)

<!-- - Incentivizes power that is: $\quad$ Plentiful $\cdot$ Reliable $\cdot$ Affordable -->

<v-clicks depth="2">

- Balances supply and demand at all times

- Minimizes cost of electricity production and maximizes value to consumers

- Market participants:

    - Loads
        - **Bid** to buy power
        - Utility companies and large industrial consumers
    - Generators
        - **Offer** to sell power
        - Power station (e.g., hydro), wind/solar farm, etc.

</v-clicks>

<br>

<small style="color: gray;">Original photo by [Austin Hervias on Unsplash](https://unsplash.com/@ahervias77).</small>

---

# Wholesale Electricity Market Operation

<v-clicks depth="2">

- “Clearing the market” $=$ accept/dispatch certain bids and offers, reject others
- Done by a central authority
- Objective: Maximize benefit to both generators and loads

    - First requirement: Authority is all-knowing of network, participants, bids/offers
    - Second requirement: One, unified decision

- Central authority is usually a government non-profit

    - Government authority $+$ separate from generation/utility companies $=$ fair market operation
    - Independent System Operators (ISOs), for example:
        - [California ISO (CAISO)](https://www.caiso.com/)
        - [Independent Electricity System Operator (IESO)](https://ieso.ca/)

</v-clicks>

---
layout: image
image: img/arno-senoner-6lOxktnqo04-unsplash-flipped-blur.jpg
---

# Different Types of Markets

<v-clicks depth="2">

- Wholesale electricity market
    - Day-to-day operation
    - Real-time operation
- Capacity market
    - Generation for generations™

</v-clicks>

<br><br><br><br><br><br><br><br>

<small>Original photo by [Arno Senoner on Unsplash](https://unsplash.com/@arnosenoner).</small>

---
layout: image-right
image: img/411202c9-ef48-4dca-848c-39db8f491109_1292x604.jpg
backgroundSize: contain
---

# Open Vs. Closed Markets

<v-clicks depth="2">

- System operators should be separate from generation/utility companies
- Generation/utility companies can still be private or government-owned
- Energy liberalization at turn of millennium:

    - Governments opened markets to private generation companies
    - Goal: competition $\Rightarrow$ lower prices
    - AKA “privatization”, “deregulation”
    - Strict market rules still in place
    - Government restructuring, e.g., IESO founded 1998

</v-clicks>

<small style="color: gray;">Graph from [Drax Electric Insights Quarterly – Q2 2022](https://reports.electricinsights.co.uk/wp-content/uploads/2022/09/Drax_Electric_Insights_Report_2022_Q2.pdf).</small>

---
layout: section
---

## **Part II**

# The Supply and Demand of Electricity

---
layout: image-right
image: img/blake-wisz-Kx3o6_m1Yv8-unsplash.jpg
---

# Introduction to Economics

Your Friendly Neighborhood Espresso Market

<v-clicks depth="2">

- Analogy: neighborhood of cafés
- Rate of espresso production $=$ rate of espresso consumption
- Assume all cafés serve identical espresso, only differentiator is price:
    - Café undercuts $\Rightarrow$ others follow
    - Café charges more $\Rightarrow$ others follow
- At a given time and place: one stable espresso price

</v-clicks>

<br><br>

<small style="color: gray;">Photo by [Blake Wisz on Unsplash](https://unsplash.com/@blakewisz).</small>

---
layout: two-cols
---

# Supply and Demand Dynamics

<v-clicks depth="2">

- Demand:
    - Rate of consumption $\, = f(\!$ price per shot $\!)$
    - Higher price $\Rightarrow$ fewer customers
    - <span style="color: #EF6C00;">**Demand curve** (buyer behavior)</span>
- Supply:
    - More espresso $\Rightarrow$ proportionately more spent on espresso beans, labor
    - A lot more espresso $\Rightarrow$ disproportionately higher:
        - Profit (price gauging)
        - Labor costs and production costs in general
    - Price per shot $\, = f(\!$ rate of production $\!)$
    - <span style="color: #1565C0;">**Supply curve** (seller behavior)</span>

</v-clicks>

::right::

<div class="relative w-full h-full">
    <img class="absolute" src="/img/fig_2_1-0.png"/>
    <img v-click=4 class="absolute" src="/img/fig_2_1-1.png"/>
    <img v-click=9 class="absolute" src="/img/fig_2_1-2.png"/>
</div>

---
layout: image-right
image: img/nick-brunner-5dgXQJ7ezuU-unsplash.jpg
---

# Clearing Markets

<v-clicks depth="2">

- Quantity $Q$ of a good is exchanged at price $P$
- At equilibrium: market-clearing quantity $Q^*$ is exchanged at market-clearing price $P^*$
- The market rewards:
    - Sellers who charge a low price
    - Buyers who are willing to pay a high price
- Market clearing process:
    - Allocate buyers to sellers, starting with highest-price buyers and lowest-price sellers
    - Determines buying price $=$ selling price <br> $= \! P^*$

</v-clicks>

<small style="color: gray;">Graphic by [Nick Brunner
 on Unsplash](https://unsplash.com/@nickbrunner).</small>

---
layout: two-cols
---

# Clearing Markets

<v-click>

- $P^*, Q^*$ determined by where <span style="color: #1565C0;">supply</span> and <span style="color: #EF6C00;">demand</span> curves intersect

</v-click>

<v-clicks at=2>

- Area under <span style="color: #1565C0;">supply curve</span> $=$ cost, $C$
- Area under <span style="color: #EF6C00;">demand curve</span> $=$ utility, $U$
- Constraint: $Q$ sold $=$ $Q$ bought $= \! Q^*$
- Maximizes $U$ and minimizes $C$ <br> or <br> Maximizes <span style="color: #2E7D32;">**welfare**, $W = U - C$</span>
- $W =$ producer surplus $+$ consumer surplus

</v-clicks>

::right::

<div class="relative w-full h-full">
    <img class="absolute" src="/img/fig_2_1-2.png"/>
    <img v-click=1 class="absolute" src="/img/fig_2_1-3.png"/>
    <img v-click=2 class="absolute" src="/img/fig_2_1-4.png"/>
</div>
<img v-click=5 class="-mt-55" src="/img/fig_2_1-5.png"/>

---

# Café--Grid Analogy

<v-clicks>

|                | **In the café analogy** | **In the electrical grid** |
|----------------|-------------------------|----------------------------|
| Good:          | Espresso shots          | Megawatt-hours             |
| Quantity unit: | Espresso shots per hour | Megawatts                  |
| Producers:     | Espresso machines       | Generators                 |
| Consumers:     | Café customers          | Loads                      |

</v-clicks>

---

# Electricity as a Commodity

<v-clicks depth="3">

- Commodity goods:

    - Espresso? ❌
    - Wheat
    - Crude oil
    - **Electricity** --- regardless of energy source
        - Nuclear
        - Hydro
        - Etc.

</v-clicks>

---

# The Electricity Market Cannot Clear Itself

<v-clicks>

|                                            | Cafés                                                       | Electricity market                                                 |
|--------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------|
| Buffer between production and consumption? | Yes --- customers can wait for their orders to be fulfilled | No --- loads simply take, without having to wait for power         |
| Resources pooled?                          | No --- each order is fulfilled by one barista               | Yes --- Increases in load can be shared across multiple generators |

</v-clicks>

<img src="/img/katt-galvan-149bjg2Zgzc-unsplash.jpg" style="border-radius: 0px; padding: 0px; height: 180px;"><small style="color: gray;">Photo by [Katt Galvan on Unsplash](https://unsplash.com/@kattgalvan).</small>

---

# Role of the System Operator

<v-clicks depth="2">

- Monitors demand
- Dispatches generators to balance supply and demand
- Nice-to-have: independence from generators (independent system operator)
    - Creates competition
    - Reduces the cost of electricity

</v-clicks>

---
layout: image-left
image: img/chris-liverani-dBI_My696Rk-unsplash.jpg
---

# Time Variance

<v-clicks>

- Seen in supply/demand curves, quantities, and prices
- Fluctuations and spikes in supply/demand <br> $\to$ fluctuations and spikes in electricity prices
- Price changes are characteristic of electricity markets

</v-clicks>

<br><br><br><br><br><br><br>

<small style="color: gray;">Photo by [Chris Liverani on Unsplash](https://unsplash.com/@chrisliverani).</small>

---

# Inelastic Loads

|                   | Café customer                                  | Non-dispatchable load                                                     |
|-------------------|------------------------------------------------|---------------------------------------------------------------------------|
| Elastic consumer? | Yes --- aware of and responsive to café prices | No --- utility customers are unresponsive to real-time electricity prices |

<br>

<v-clicks depth="3">

- Market participants:
    1. Non-dispatchable loads
        - Cause price spikes when demand is high or generation is intermittent
    2. Dispatchable loads
        - Large industrial consumers
        - Utility companies with demand response programs
    3. Non-dispatchable generators
    4. Dispatchable generators

</v-clicks>

---
layout: two-cols
---

# Bids to Buy and <br> Offers to Sell Power

<v-clicks depth="2">

- Bid/offer = price-quantity pairs

    - Specifies max quantity ($\mathrm{MW}$) <br> at each price ($\$/\mathrm{MWh}$)
    - <span style="color: #1565C0;">Offer $P(Q)$ monotonically increasing</span>
    - <span style="color: #EF6C00;">Bid: $P(Q)$ monotonically decreasing</span>

</v-clicks>

**<v-click at=6>Example 1: One generator, one load ⏵</v-click>**

<v-clicks at=7>

- <span style="color: #EF6C00;">Load's price-quantity pairs = demand curve</span>
- <span style="color: #1565C0;">Generator's price-quantity pairs = supply curve</span>
- Intersection determines $(Q^*, P^*)$
- Maximizes <span style="color: #2E7D32;">$W = U - C$</span>

</v-clicks>

::right::

<div class="relative w-full h-full">
    <img class="absolute" src="/img/fig_2_2-0.png"/>
    <img v-click=3 class="absolute" src="/img/fig_2_2-1.png"/>
    <img v-click=4 class="absolute" src="/img/fig_2_2-2.png"/>
    <img v-click=5 class="absolute" src="/img/fig_2_2-3.png"/>
    <img v-click=9 class="absolute" src="/img/fig_2_2-4.png"/>
    <img v-click=10 class="absolute" src="/img/fig_2_2-5.png"/>
</div>
<img v-click=10 class="-mt-55" src="/img/fig_2_2-6.png"/>

---
layout: two-cols
---

**Example 2: Two Generators, Two Loads**

<v-clicks at=2 depth="2">

- Individual <span style="color: #1565C0;">supply</span> / <span style="color: #EF6C00;">demand</span> curves
- Goal: maximize welfare, $W = U - C$
- Total seller cost: <br> $\displaystyle C(Q_\mathrm{G1}, Q_\mathrm{G2}) = \! \int_0^{\, Q_\mathrm{G1}} \!\!\!\!\!\!\! p_{\, \mathrm{G1}}(q) \, \mathrm{d} q \, + \! \int_0^{\, Q_\mathrm{G2}} \!\!\!\!\!\!\! p_{\, \mathrm{G2}}(q) \, \mathrm{d} q$
- Total buyer utility: <br> $\displaystyle U(Q_\mathrm{L1}, Q_\mathrm{L2}) = \! \int_0^{\, Q_\mathrm{L1}} \!\!\!\!\!\!\! p_{\, \mathrm{L1}}(q) \, \mathrm{d} q \, + \! \int_0^{\, Q_\mathrm{L2}} \!\!\!\!\!\!\! p_{\, \mathrm{L2}}(q) \, \mathrm{d} q$
- **Economic Dispatch (ED)** problem:
    - $\max_{Q_\mathrm{G1}, \, Q_\mathrm{G2}, \, Q_\mathrm{L1}, \, Q_\mathrm{L2}} W(Q_\mathrm{G1}, Q_\mathrm{G2}, Q_\mathrm{L1}, Q_\mathrm{L2})$
    - $\text{subject to} \quad Q_\mathrm{G1} + Q_\mathrm{G2} = Q_\mathrm{L1} + Q_\mathrm{L2}$
</v-clicks>

<br>

<v-clicks at=12>

- Solution: $Q^* \! = 11 \ \mathrm{MW} \!, \, P^* \! = \$4 / \mathrm{MWh},$ <br> $C^* \! = \$32.0 / \mathrm{h}, \, U^* \! = \$79.0 / \mathrm{h}, \, W^* \! = \$47.0 / \mathrm{h}$

</v-clicks>

::right::

<div class="relative w-full h-full">
    <img v-click=1 class="absolute" src="/img/fig_2_3.png"/>
    <img v-click=3 class="absolute" src="/img/fig_2_4.png"/>
    <img v-click=9 class="absolute" src="/img/fig_2_5-1.png"/>
    <img v-click=10 class="absolute" src="/img/fig_2_5-2.png"/>
    <img v-click=11 class="absolute" src="/img/fig_2_5-3.png"/>
    <img v-click=12 class="absolute" src="/img/fig_2_5-4.png"/>
</div>

---
layout: image-right
image: img/Open-Infrastructure-Map.jpg
---

# The Market Network

<v-clicks>

- One market price for a given time and market
- **Nodal pricing** / **locational marginal pricing (LMP)**:
    - Grid = multiple pricing nodes, each like a market with its own price
- **Zonal pricing**:
    - Grid level $\to$ zonal level $\to$ nodal level
    - Pricing is at the zonal level

</v-clicks>

<br>

Grid infrastructure spanning Michigan, Ontario, and New York state ⏵
<br>
<small style="color: gray;">Copyright OpenStreetMap and Open Infrastructure Map (https://www.openstreetmap.org/copyright, <br> https://openinframap.org/copyright).</small>

---
layout: image-right
image: img/revtlprojects-CU5vr-d98lI-unsplash.jpg
---

# Power Transmission

<v-clicks depth="2">

- Inter-node power transfer via transmission and distribution lines
- Supply must equal demand at the system level, not necessarily at the nodal level
- Analogous to trade
- The entire grid must be cleared as one market
- Maximizes total welfare
    - Higher with trade than without $\Leftrightarrow$ People trade to increase their welfare

</v-clicks>

<br><br><br>

<small style="color: gray;">Photo by [REVTLProjects on Unsplash](https://unsplash.com/@revtlproj).</small>

---

# Transmission Losses

<v-clicks>

- Transmission and distribution lines have electrical resistance
- Power in $=$ power out $+$ power lost to heat
- Power lost to heat $=$ cost of trade
- Power transfer usually still beneficial to overall welfare
- Transmission losses cause price differences between nodes
- Simple model for the sake of our examples: efficiency $\eta =$ power out $/$ power in
- In the real world: more complex transmission line models

</v-clicks>

---

# Transmission Congestion

<v-clicks depth="2">

- How a line outage occurs:

    - Thermal expansion
    - Line sags too close to nearby object (e.g., a tree)
    - Line shorts
    - Protective relay detects overcurrent and trips

- How line outages are avoided:

    - Rated maximum power

- Line is congested if power $=$ maximum power
- Transmission congestion causes price differences between nodes

</v-clicks>

---
layout: two-cols
---

**Example 3: One Generator Node, One Load Node**

<v-clicks at=5 depth="2">

- Problem: $\max_{Q_\mathrm{G}, \, Q_\mathrm{L}} W(Q_\mathrm{G}, Q_\mathrm{L})$ <br> $\text{subject to}$:
    - $Q_\mathrm{L} = 0.75 \, Q_\mathrm{G}$

</v-clicks>

<br>

<v-clicks at=8>

- Solution: <br> $C^* \! = \$25.\bar{3} / \mathrm{h}, \, U^* \! = \$59.0 / \mathrm{h}, \, W^* \! = \$33.\bar{6} / \mathrm{h}$

</v-clicks>

<div class="relative w-full h-full">
    <img v-click=1 class="absolute" src="/img/diagrams-example_3-1.png"/>
    <img v-click=2 class="absolute" src="/img/diagrams-example_3-2.png"/>
    <img v-click=3 class="absolute" src="/img/diagrams-example_3-3.png"/>
    <img v-click=4 class="absolute" src="/img/diagrams-example_3-4.png"/>
    <img v-click=8 class="absolute" src="/img/diagrams-example_3-5.png"/>
</div>

::right::

<div class="relative w-full h-full">
    <img v-click=7 class="absolute" src="/img/fig_2_6.png"/>
</div>

---
layout: two-cols
---

**Example 3 with Transmission Congestion**

<v-clicks at=1 depth="3">

- Problem: $\max_{Q_\mathrm{G}, \, Q_\mathrm{L}} W(Q_\mathrm{G}, Q_\mathrm{L})$ <br> $\text{subject to}$:
    - $Q_\mathrm{L} = 0.75 \, Q_\mathrm{G}$
    - $Q_\mathrm{G} < 8 \ \mathrm{MW}$

</v-clicks>

<v-clicks at=5>

- Solution: <br> $C^* \! = \$20.0 / \mathrm{h}, \, U^* \! = \$51.0 / \mathrm{h}, \, W^* \! = \$31.0 / \mathrm{h}$

</v-clicks>

<div class="relative w-full h-full">
    <img class="absolute" src="/img/diagrams-example_3-4.png"/>
    <img v-click=3 class="absolute" src="/img/diagrams-example_3b-1.png"/>
    <img v-click=5 class="absolute" src="/img/diagrams-example_3b-2.png"/>
</div>

::right::

<div class="relative w-full h-full">
    <img v-click=4 class="absolute" src="/img/fig_2_6b.png"/>
</div>

---
layout: two-cols
---

**Example 4: One Generator Node, One Combined Generator/Load Node**

<v-clicks at=1 depth="3">

- Problem: $\max_{Q_\mathrm{G2}, \, Q_\mathrm{L}} W(Q_\mathrm{G2}, Q_\mathrm{L})$ <br> $\text{subject to}$:
    - $0.75 \, Q_\mathrm{G1} + Q_\mathrm{G2} = Q_\mathrm{L}$

</v-clicks>

<v-clicks at=5>

- Solution: <br> $C^* \! = \$38.0 / \mathrm{h}, \, U^* \! = \$79.0 / \mathrm{h}, \, W^* \! = \$41.0 / \mathrm{h}$

</v-clicks>

<br>

<div class="relative w-full h-full">
    <img class="absolute" src="/img/diagrams-example_4-1.png"/>
    <img v-click=5 class="absolute" src="/img/diagrams-example_4-2.png"/>
</div>

::right::

<img v-click=3 src="/img/fig_2_7.png"/>
<img v-click=4 src="/img/fig_2_8.png" width=80% style="margin-left: auto; margin-right: auto;"/>

---
layout: cover
background: img/tahoe-groeger-ioCEgIFVLos-unsplash-blur.jpg
---

## Thanks for learning with me.

**Learn more** or get the PDF at: <br> [keeganmjgreen.github.io/blog/<br>introduction-to-wholesale-electricity-markets](https://keeganmjgreen.github.io/blog/introduction-to-wholesale-electricity-markets/)

<img src="/img/pdf_fanout_2x.png" style="height: 200px;">

<br><br>

[linkedin.com/in/keegan-green](https://www.linkedin.com/in/keegan-green/)
