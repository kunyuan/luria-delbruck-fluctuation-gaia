"""Discussion — Overall conclusions and implications."""

from gaia.lang import claim, setting, support

from .motivation import (
    experimental_system,
    hypothesis_mutation,
    hypothesis_acquired_immunity,
)
from .exp_fluctuation import (
    clonal_grouping_observed,
    observed_variance_much_greater_than_mean,
)
from .mutation_rate import mutation_rate_consistent_across_conditions

# === Core conclusions ===

resistance_is_heritable_mutation = claim(
    "The resistance to virus in *E. coli* B is due to a heritable change of "
    "the bacterial cell which occurs independently of the action of the virus. "
    "The experimental distribution of resistant bacteria conforms to the mutation "
    "hypothesis and conflicts with the acquired immunity hypothesis.",
    title="Conclusion: resistance arises by spontaneous mutation",
    background=[experimental_system],
)

strat_conclusion = support(
    [observed_variance_much_greater_than_mean,
     clonal_grouping_observed,
     mutation_rate_consistent_across_conditions],
    resistance_is_heritable_mutation,
    reason=(
        "Three lines of evidence converge: (1) @observed_variance_much_greater_than_mean "
        "— the fluctuation data conflicts with the Poisson prediction of the acquired "
        "immunity hypothesis and matches the high-variance prediction of the mutation "
        "hypothesis; (2) @clonal_grouping_observed — resistant bacteria appear in clonal "
        "groups, consistent with common mutant ancestors; (3) "
        "@mutation_rate_consistent_across_conditions — the mutation rate estimated from "
        "diverse experimental conditions is consistent (~$2.45 \\times 10^{-8}$), "
        "confirming the core assumption of a fixed mutation rate per time unit."
    ),
    prior=0.9,
)

aging_cultures_constant_fraction = claim(
    "A culture grown to saturation was tested repeatedly for resistant bacteria "
    "and total bacteria over several days. The proportion of resistant bacteria "
    "did not change, even when the sensitive bacteria began to die. This shows "
    "that resistant bacteria have the same death rate in aging cultures as "
    "sensitive bacteria — resistance to virus does not generally come to expression "
    "in the cell where the mutation occurred, as assumed by the theory.",
    title="Resistant fraction stable in aging cultures",
    background=[experimental_system],
)

strat_aging = support(
    [aging_cultures_constant_fraction],
    resistance_is_heritable_mutation,
    reason=(
        "@aging_cultures_constant_fraction shows that the resistant fraction does not "
        "change in aging cultures, even when sensitive bacteria die. This confirms "
        "a key assumption of the mutation theory: that resistance is expressed in "
        "offspring (not induced by virus contact), and that resistant and sensitive "
        "bacteria have identical growth and death rates. This provides additional "
        "support for the conclusion that resistance arises by spontaneous mutation."
    ),
    prior=0.75,
)
