# How the Ontario Electricity Market Works

The world's electricity grids stand alongside the internet and water supply networks as great systems and accomplishments of humanity. The vast majority of us participate and rely on these systems every day, not necessarily understanding how they work, and often taking them for granted. As are the consequences of systems of such complexity and flawlessness. The ability to flip a switch and flood a room with light in the middle of the night is the result of countless years of human innovation and millions of people working around the clock to keep the world's grids running smoothly. What happens every time a light is turned on often eludes us. Nonetheless, without fail, slightly more current gets drawn through tens or hundreds of kilometers of distribution and transmission lines. And, in tandem, the generators at the end of those transmission lines start to work slightly harder, whether in a nuclear, hydro, or gas power plant. But even this is not a full appreciation for what goes into constantly balancing the supply and demand of electricity. The grid is just as much an economic system as a physical one, and it must be operated to create the perfect economic playing field&mdash;one that incentivizes the generation of power that is plentiful, reliable, and affordable. That playing field is the electricity market.

Because an electrical grid is so vast and involves so many people, it cannot operate without some form of oversight. In the early days, electrical grids were small networks owned and operated by private companies. However, it was quickly realized that the electrical grid serves the public good and ought not be entrusted to a regular, private company. This is where the role of an Independent System Operator, or *ISO*, comes into play. An ISO controls an electrical grid and its electricity market. Ontario's ISO is the Independent Electricity System Operator (IESO). They're called *independent* because they don't own or operate any physical generation facilities, only the transmission and distribution network. This allows them to be impartial when choosing who to buy electricity from. The IESO is closely involved in the long-term planning of generation facilities in certain regions and of certain types, and the IESO's permission is required to connect to the grid, but they are a neutral party at the end of the day. This fosters healthy competition between generation facilities.

In an electrical grid, the supply and demand of electricity must be constantly balanced. In other markets, supply and demand are balanced naturally. For example, TODO

The goal of an electricity market is to balance supply and demand. TODO
 
## How does the IESO balance supply and demand?

To balance supply and demand, the IESO first forecasts the demand at each node. Then, they perform Optimal Power Flow (OPF) to determine the optimal supply at each node. The OPF is based on the demand forecasts, the structure of the grid, and the limitations of transmission and distribution lines.

To understand OPF, we first have to understand the electrical grid and power flow analysis.

## The electrical grid *is designed to minimize losses*

The electrical grid is designed to efficiently transmit power from where it is generated to where it is consumed, and to do so safely. Power plants are often distant from cities due to the electricity source (e.g., colocation of a hydroelectric plant with a reservoir), safety reasons (e.g., a gas plant), or space requirements (e.g., a large nuclear plant). Despite increasing adoption of wind and solar, most power is still generated at power plants.

Transmitting power over long distances incurs power losses due to the resistance of transmission lines. To ensure that the desired amount of power is actually delivered at the other end, extra power must be generated. This represents additional costs placed on end consumers. Minimizing the power losses along with their associated costs is achieved by transmitting power at high voltages.

High voltages, however, are obviously unsafe and impractical for most consumers, so the voltage must be lowered as we go from transmission lines to distribution lines, into cities and neighborhoods. At each stage of getting closer and closer to where the power is consumed, transformers (e.g., at substations) are encountered to step down the voltage. Transformers are the easiest and most efficient way to convert between voltage levels, but require Alternating Current (AC) instead of Direct Current (DC) electricity. So, in order to transmit power over long distances to where it is needed, while minimizing losses and delivering power at a safe and convenient voltage, AC power must be used. In addition, most power plants use rotating generators which already produce AC power, and many industrial loads are AC motors anyway. For the loads that require DC, converting from AC to DC is worth it to be able to transmit that power efficiently in the first place.

Note: Some transmission lines, particularly *interties* that connect electrical grids over long distances, use very high voltage *DC* (HVDC) lines.

## Power flow analysis *is used to estimate losses, given the supply and demand of electricity*

Given a supply and demand at each node in the grid, power flow analysis calculates the current that will flow through each transmission and distribution line. Obviously this requires that total supply equals total demand, but more accurately, total supply must equal total demand plus transmission losses. The difficulty with this arises from the fact that the losses depend on the currents, which depend in part on the total supply, which in turn depends on the losses! In this sense, the solution to the power flow problem depends on itself. However, we will see how the concept of the slack bus allows us to work around this. In the mean time, let us formulate the power flow problem.

TODO

## Optimal power flow determines the supply that minimizes losses, given demand

TODO
