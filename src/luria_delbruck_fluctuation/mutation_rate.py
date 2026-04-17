"""Mutation Rate — Two estimation methods and consistent results across experiments."""

from gaia.lang import claim, setting, support, induction

from .motivation import experimental_system, hypothesis_mutation
from .theory import (
    exponential_growth_model,
    mutation_rate_definition,
    p0_mutation_rate_relation,
    mean_method_mutation_rate,
)
from .exp_fluctuation import fluctuation_data_table2, fluctuation_data_table3

# === Mutation rate estimates ===

mutation_rate_p0_method_exp23 = claim(
    "Using the $p_0$ method (proportion of cultures with zero resistant bacteria) "
    "on Experiment 23: out of 87 cultures, 29 had no resistant bacteria "
    "($p_0 = 0.33$). From $p_0 = e^{-m}$, the average number of mutations per "
    "culture is $m = 1.10$. Since total bacteria per culture was $2.4 \\times 10^8$, "
    "the mutation rate is:\n\n"
    "$a = 0.47 \\times 10^{-8}$ mutations per bacterium per time unit\n\n"
    "$= 0.32 \\times 10^{-8}$ mutations per bacterium per division cycle.\n\n"
    "This method uses only the fraction of zero-resistant cultures and is therefore "
    "inefficient in its use of the experimental data.",
    title="Mutation rate by p0 method (Exp. 23)",
    background=[exponential_growth_model, mutation_rate_definition],
)

strat_p0_est = support(
    [p0_mutation_rate_relation, fluctuation_data_table3],
    mutation_rate_p0_method_exp23,
    reason=(
        "@p0_mutation_rate_relation gives $p_0 = e^{-m}$. @fluctuation_data_table3 "
        "provides the Exp. 23 data: 29 out of 87 cultures have zero resistant "
        "bacteria, so $p_0 = 29/87 = 0.33$. Solving: $m = -\\ln(0.33) = 1.10$. "
        "With $N_t = 2.4 \\times 10^8$, equation (4) gives "
        "$a = m/N_t = 0.47 \\times 10^{-8}$. The calculation is straightforward "
        "but the $p_0$ estimate discards all information from non-zero cultures."
    ),
    prior=0.85,
)

mutation_rate_mean_method = claim(
    "Using the mean method (equation 8: $r = a N_t \\ln(N_t C a)$) across all "
    "experiments, the mutation rates are consistent (Table 4):\n\n"
    "| Experiment | Cultures | Vol. (cc) | Mutation rate |\n"
    "|-----------|----------|-----------|---------------|\n"
    "| 1         | 9        | 10.0      | $1.8 \\times 10^{-8}$ |\n"
    "| 10        | 8        | 10.0      | $1.4 \\times 10^{-8}$ |\n"
    "| 11        | 10       | 10.0      | $4.1 \\times 10^{-8}$ |\n"
    "| 15        | 10       | 10.0      | $2.1 \\times 10^{-8}$ |\n"
    "| 16        | 20       | 0.2*      | $1.1 \\times 10^{-8}$ |\n"
    "| 17        | 12       | 0.2*      | $3.0 \\times 10^{-8}$ |\n"
    "| 21a       | 19       | 0.2       | $3.3 \\times 10^{-8}$ |\n"
    "| 21b       | 5        | 10.0      | $3.0 \\times 10^{-8}$ |\n"
    "| 22        | 100      | 0.2*      | $2.3 \\times 10^{-8}$ |\n"
    "| 23        | 87       | 0.2*      | $2.4 \\times 10^{-8}$ |\n\n"
    "Average: $2.45 \\times 10^{-8}$ mutations per bacterium per time unit. "
    "(* synthetic medium). The consistency across different culture volumes, "
    "media, and numbers of cultures supports the mutation hypothesis.",
    title="Mutation rates across experiments (mean method, Table 4)",
    source_table="artifacts/paper.pdf, Table 4",
    background=[exponential_growth_model, mutation_rate_definition],
)

strat_mean_est = support(
    [mean_method_mutation_rate, fluctuation_data_table2],
    mutation_rate_mean_method,
    reason=(
        "@mean_method_mutation_rate provides the transcendental equation "
        "$r = a N_t \\ln(N_t C a)$. @fluctuation_data_table2 provides the observed "
        "average resistant bacteria per culture $r$ and total bacteria $N_t$ for "
        "each experiment. Solving equation (8) numerically for each experiment "
        "yields the mutation rate values in Table 4. The computation is numerical "
        "but straightforward."
    ),
    prior=0.85,
)

mutation_rate_consistent_across_conditions = claim(
    "The mutation rate calculated by the mean method does not vary greatly from "
    "experiment to experiment. In particular: (1) there is no significant "
    "difference between broth cultures and synthetic medium cultures, despite "
    "considerable differences in metabolic activity and growth rate; (2) there is "
    "no significant difference between 10 cc cultures and 0.2 cc cultures; "
    "(3) there is no significant difference between experiments with many and "
    "few cultures. This shows that the simple assumption of a fixed small chance "
    "of mutation per physiological time unit is vindicated by the results.",
    title="Mutation rate consistent across conditions",
    background=[experimental_system],
)

# Two independent sets of experiments confirm a consistent mutation rate.

fixed_mutation_rate_law = claim(
    "There exists a fixed mutation rate $a$ per bacterium per physiological time "
    "unit for the transition from virus-sensitive to virus-resistant in *E. coli* B, "
    "independent of culture medium, culture volume, or number of cultures tested. "
    "The average value across all experiments is $a \\approx 2.45 \\times 10^{-8}$ "
    "mutations per bacterium per time unit.",
    title="Law: fixed mutation rate across conditions",
    background=[experimental_system],
)

obs_broth_rate = claim(
    "Experiments in 10.0 cc broth cultures (Exp. 1, 10, 11, 15, 21b) yield "
    "mutation rates of $1.8$, $1.4$, $4.1$, $2.1$, and $3.0 \\times 10^{-8}$ "
    "mutations per bacterium per time unit, respectively (Table 4).",
    title="Mutation rates in broth cultures",
    source_table="artifacts/paper.pdf, Table 4",
    background=[experimental_system],
)

obs_synth_rate = claim(
    "Experiments in 0.2 cc synthetic medium cultures (Exp. 16, 17, 22, 23) "
    "yield mutation rates of $1.1$, $3.0$, $2.3$, and $2.4 \\times 10^{-8}$ "
    "mutations per bacterium per time unit, respectively (Table 4).",
    title="Mutation rates in synthetic medium",
    source_table="artifacts/paper.pdf, Table 4",
    background=[experimental_system],
)

strat_broth_supports = support(
    [obs_broth_rate],
    fixed_mutation_rate_law,
    reason=(
        "@obs_broth_rate shows five independent broth culture experiments yield "
        "mutation rates from $1.4$ to $4.1 \\times 10^{-8}$, clustered within a "
        "narrow range. This consistency across experiments with different numbers "
        "of cultures (5 to 10) and culture volumes supports the existence of a "
        "fixed mutation rate."
    ),
    prior=0.8,
)

strat_synth_supports = support(
    [obs_synth_rate],
    fixed_mutation_rate_law,
    reason=(
        "@obs_synth_rate shows four synthetic medium experiments yield mutation "
        "rates from $1.1$ to $3.0 \\times 10^{-8}$, overlapping with the broth "
        "culture values despite very different metabolic conditions and growth "
        "rates. This cross-medium consistency strongly supports a fixed mutation "
        "rate per physiological time unit."
    ),
    prior=0.8,
)

# Induction: two independent observation sets confirm the same law
ind_mutation_rate = induction(
    strat_broth_supports,
    strat_synth_supports,
    law=fixed_mutation_rate_law,
    reason=(
        "Broth culture experiments and synthetic medium experiments are conducted "
        "under very different metabolic conditions (rich vs minimal medium) and "
        "growth rates, yet yield overlapping mutation rate estimates. This "
        "cross-condition independence strengthens the inductive evidence for a "
        "fixed mutation rate."
    ),
)

strat_consistent = support(
    [fixed_mutation_rate_law, mutation_rate_mean_method],
    mutation_rate_consistent_across_conditions,
    reason=(
        "@fixed_mutation_rate_law is confirmed by independent experiments across "
        "conditions. @mutation_rate_mean_method shows the values from Table 4 are "
        "consistent across culture volume (10 cc vs 0.2 cc) and number of cultures "
        "(5 to 100). This consistency vindicates the assumption of a fixed mutation "
        "rate per physiological time unit."
    ),
    prior=0.85,
)

mutation_rate_discrepancy_two_methods = claim(
    "The mutation rates obtained by the mean method (average $2.45 \\times 10^{-8}$) "
    "are all higher than the value found by the $p_0$ method "
    "($0.47 \\times 10^{-8}$ for Exp. 23). This discrepancy is traced to the same "
    "cause as the excess standard deviation: early mutations (prior to time $t_0$) "
    "give rise to big clones of resistant bacteria. These big clones do not affect "
    "the $p_0$ method (which uses only the fraction of zero-count cultures) but they "
    "do inflate the average used by the mean method.",
    title="Discrepancy between p0 and mean method",
    background=[exponential_growth_model, mutation_rate_definition],
)

strat_discrepancy = support(
    [mutation_rate_p0_method_exp23, mutation_rate_mean_method],
    mutation_rate_discrepancy_two_methods,
    reason=(
        "@mutation_rate_p0_method_exp23 gives $a = 0.47 \\times 10^{-8}$ using "
        "only the zero-count fraction. @mutation_rate_mean_method gives an average "
        "of $2.45 \\times 10^{-8}$ using the full average. The mean method is inflated "
        "by 'jackpot' cultures from early mutations, which contribute large clone "
        "sizes to the average but do not affect the fraction of zero-count cultures. "
        "This discrepancy is itself consistent with the mutation hypothesis's "
        "prediction of a heavy-tailed distribution."
    ),
    prior=0.85,
)
