# simulations.py - Master Registry for all 19 Physical Marvel Algorithm Simulations
# Seamlessly integrates Part 1, Part 2, Part 3, and Part 4

import physical_sims_part1 as p1
import physical_sims_part2 as p2
import physical_sims_part3 as p3
import physical_sims_part4 as p4

SIMULATIONS = {}
SIMULATIONS.update(p1.PHYSICAL_SIMS_PART1)
SIMULATIONS.update(p2.PHYSICAL_SIMS_PART2)
SIMULATIONS.update(p3.PHYSICAL_SIMS_PART3)
SIMULATIONS.update(p4.PHYSICAL_SIMS_PART4)

print(f"Master SIMULATIONS loaded successfully: {len(SIMULATIONS)} engines ready.")
