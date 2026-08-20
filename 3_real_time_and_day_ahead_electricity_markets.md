---
author: Keegan Trujillo-Green
---

# Real-Time and Day-Ahead Electricity Markets

> <div style="display: flex; align-items: center;">
>   <div style="width: 20%; padding-right: 5%;">
>     <img src="img/pdf_fanout.png">
>   </div>
>   <div style="width: 75%;">
>     <a href="https://raw.githubusercontent.com/keeganmjgreen/ontario_electricity_market/main/how_electricity_markets_work.pdf">Download the PDF</a>
>     <br>
>     <a href="https://keeganmjgreen.github.io/blog/">Read more technical, AI-free content on my blog</a>
>   </div>
> </div>

In the previous section, we discussed how the electricity market, and thus the market clearing price, varies over time and space. At different dispatch times, there are different magnitudes of load and available generation. Additionally, the electricity market acts like many electricity markets across many spacial locations in the grid.

In this section, we will learn that the electricity market spans another temporal axis, representing the time when the market was cleared in advance of the dispatch time. There are two instantiations of this: the day-ahead market, which is cleared the day before a given dispatch time, and the real-time market, which is cleared at the time of dispatch.

But why not just clear the market at the time of dispatch? Why do we need to plan ahead? Why bother making decisions in advance based on difficult-to-predict load and renewable generation?

The answer lies in the fact that generators&mdash;even nonrenewable ones&mdash;are not infinitely flexible. You cannot generally ask a generator to output an arbitrary amount of power (within their capacity) at any time. Some generators take time to ramp their output up or down, or need to be kept running or offline for a minimum amount of time. These operational constraints are known as ramp rate limits and minimum uptime/downtime. Some generators also take time to fully start up or shut down.

Due to all these time-based constraints, the choice made for one dispatch time might narrow the possible choices for upcoming dispatch times. This means that the system operator might dispatch generators in a way that maximizes welfare at a particular time, but reduces the welfare-maximizing ability at future times, resulting in less total welfare over time. This is known as greedy optimization, and is avoided by maximizing total welfare, over multiple dispatch times at once, in one optimization problem. With such a time horizon, accurate predictions of non-dispatchable generation and load become crucial.

## The Day-Ahead Market

Because the startup time and minimum up/down time can be many hours long, the optimization problem is solved simultaneously for all 24 hours of the dispatch date $d$, a day in advance (on date $d - 1$). Solving this optimization problem clears what we call the day-ahead market, or DAM. The DAM is typically cleared in one-hour or 15-minute intervals, limited by the resolution at which non-dispatchable generation and load are predicted (a finer resolution would be expecting too much accuracy from the predictions). Each of these one-hour or 15-minute intervals is known as a DAM interval. The solution to the optimization problem determines the values of the market-clearing price $P^\mathrm{DAM}_t$ and quantity $Q^\mathrm{DAM}_t$ throughout the next day ($d \leq t \le d + 1$). However, being based on coarse and imperfect predictions, the prices are not final and the quantities are not used for dispatch. For a given dispatchable generator (or dispatchable load) $g$, the quantity $Q^\mathrm{DAM}_{g,\,t}$ determines whether the generator must be ready to supply that quantity of power; if greater than zero, the generator is said to be "scheduled" in the DAM.

## The Real-Time Market

Dispatch is the role of the real-time market, or RTM. The RTM is cleared every five minutes by formulating and solving an optimization problem in five-minute resolution for the upcoming 60-minute period. With a 55-minute overlap between each instance of the optimization problem, this is a true example of "rolling-horizon" optimization. Although the solution determines the market-clearing prices and quantities throughout the upcoming 60-minute period, only those of the first five-minute RTM interval $t$ are taken as the RTM-clearing price $P^\mathrm{RTM}_t$ and quantity $Q^\mathrm{RTM}_t$, and then used for dispatch. If $Q^\mathrm{RTM}_{g,\,t}$ is greater than zero, then the system operator sends dispatch instructions to $g$, telling it to change its output to that quantity of power.

DAM-clearing prices and quantities are good indicators of what the RTM-clearing prices and quantities will be.

## The Bid/Offer Lifecycle

The lifecycle of a bid or offer through the DAM and RTM is as follows:

1. On date $d - 1$, dispatchable resource $g$ optionally participates in the DAM, submitting a bid or offer for each of date $d$'s DAM intervals. This must be done before the DAM closing time.

2. On date $d - 1$, the DAM closes and clears. If $g$ had bids or offers, clearing the DAM determines whether $g$ is scheduled in the DAM, when, and at what quantity of power.

3. Before the RTM closes for date $d$'s RTM interval $t$, dispatchable resource $g$ participates in the RTM. If they participated in the DAM, they participate in the RTM by keeping or revising their existing bid or offer. Otherwise, they participate in the RTM by submitting a new bid or offer.

4. Just before each RTM interval $t$ on date $d$, the RTM closes and clears. Clearing the RTM determines whether $g$ will be dispatched, and at what quantity of power.

<!-- ## The Two-Settlement System -->
