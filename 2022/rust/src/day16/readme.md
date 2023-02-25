## [Day 16](https://adventofcode.com/2022/day/16)

Approaching this problem with dynamic programming

1. subproblem

What is the greatest amount of preassure we can decreasse beeing in valve A in time left T ?

having:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II

When T=1 and Valve BB -> 13
When T=2 and Valve BB -> 13
When T=3 and Valve BB -> 13 (open valve BB) -> Go to CC -> Open CC

Preassure[T](A)

Preassure[1](BB) -> 13
Preassure[3](BB) -> Preassure[1] + Preassure[]
