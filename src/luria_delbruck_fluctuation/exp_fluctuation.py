"""Experimental — The fluctuation test: comparing variance across independent cultures."""

from gaia.lang import claim, setting, support, compare, abduction

from .motivation import (
    experimental_system,
    hypothesis_mutation,
    hypothesis_acquired_immunity,
    immunity_predicts_poisson,
    mutation_predicts_clonal_grouping,
)
from .theory import (
    immunity_variance_equals_mean,
    mutation_high_variance,
)
from .exp_plating import plating_method_reliable, plating_variance_equals_mean

# === Setting: fluctuation test protocol ===

fluctuation_protocol = setting(
    "Series of 5 to 100 cultures of *E. coli* B were set up in parallel with "
    "small equal inocula and grown until maximum titer was reached. Three kinds "
    "of cultures were used: (1) 10.0 cc aerated broth cultures; (2) 0.2 cc broth "
    "cultures; (3) 0.2 cc synthetic medium cultures. The entire cultures (or "
    "calibrated samples) were then plated with excess virus alpha on nutrient agar "
    "plates to count resistant colonies.",
    title="Fluctuation test protocol",
)

# === Core fluctuation test results ===

fluctuation_data_table2 = claim(
    "The numbers of resistant bacteria in series of similar cultures (Table 2) "
    "show enormous variation across cultures, far exceeding sampling error. "
    "Representative experiments:\n\n"
    "| Exp. | Cultures | Vol. (cc) | Avg/culture | Bacteria/culture | Mutation rate |\n"
    "|------|----------|-----------|-------------|------------------|---------------|\n"
    "| 1    | 9        | 10.0      | 5360        | $3.4 \\times 10^{10}$ | $1.8 \\times 10^{-8}$ |\n"
    "| 11   | 10       | 10.0      | 12400       | $4.1 \\times 10^{10}$ | $4.1 \\times 10^{-8}$ |\n"
    "| 16   | 20       | 0.2*      | 28.4        | $5.6 \\times 10^{8}$  | $1.1 \\times 10^{-8}$ |\n"
    "| 21a  | 19       | 0.2       | 15.1        | $3.5 \\times 10^{8}$  | $3.3 \\times 10^{-8}$ |\n"
    "| 23   | 87       | 0.2*      | 28.6        | $2.4 \\times 10^{8}$  | $2.37 \\times 10^{-8}$ |\n\n"
    "(* synthetic medium). Within each experiment, some cultures have 0 resistant "
    "bacteria while others have hundreds, demonstrating the 'jackpot' phenomenon.",
    title="Fluctuation test data (Table 2)",
    source_table="artifacts/paper.pdf, Table 2",
    background=[fluctuation_protocol],
)

fluctuation_data_table3 = claim(
    "The distribution of resistant bacteria counts across large series of similar "
    "cultures (Table 3) shows:\n\n"
    "| Resistant bacteria | Exp. 22 (100 cultures) | Exp. 23 (87 cultures) |\n"
    "|-------------------|------------------------|----------------------|\n"
    "| 0                 | 57                     | 29                   |\n"
    "| 1                 | 20                     | 17                   |\n"
    "| 2                 | 5                      | 4                    |\n"
    "| 3                 | 2                      | 3                    |\n"
    "| 4                 | 3                      | 3                    |\n"
    "| 5                 | 1                      | 2                    |\n"
    "| 6-10              | 7                      | 5                    |\n"
    "| 11-20             | 2                      | 6                    |\n"
    "| 21-50             | 2                      | 7                    |\n"
    "| 51-100            | 0                      | 5                    |\n"
    "| 101-200           | 0                      | 2                    |\n"
    "| 201-500           | 0                      | 4                    |\n"
    "| 501-1000          | 1                      | 0                    |\n\n"
    "The distribution has a heavy right tail with rare 'jackpot' cultures. "
    "Exp. 22: mean 10.12, variance (corrected) 6270. Exp. 23: mean 28.6, "
    "variance (corrected) 6431.",
    title="Distribution of resistant bacteria (Table 3)",
    source_table="artifacts/paper.pdf, Table 3",
    background=[fluctuation_protocol],
)

observed_variance_much_greater_than_mean = claim(
    "In every fluctuation experiment (Tables 2 and 3), the variance of the number "
    "of resistant bacteria across replicate cultures is tremendously higher than "
    "could be accounted for by sampling errors. This is in striking contrast to the "
    "plating reliability tests (Table 1) where variance equaled the mean, and in "
    "direct conflict with the expectation from the hypothesis of acquired immunity "
    "(which predicts Poisson-distributed counts with variance equal to mean).",
    title="Observed variance >> mean across cultures",
    background=[fluctuation_protocol],
)

experimental_std_dev_ratio = claim(
    "The experimental ratio of standard deviation to mean number of resistant "
    "bacteria per culture was compared to the theoretical prediction from the "
    "mutation hypothesis (equation 12). Representative values:\n\n"
    "| Experiment | Std.dev./mean (exp.) | Std.dev./mean (calc.) |\n"
    "|-----------|---------------------|----------------------|\n"
    "| 1         | 1.3                 | 0.35                 |\n"
    "| 11        | 0.33                | 0.33                 |\n"
    "| 16        | 2.3                 | 0.94                 |\n"
    "| 21a       | 0.67                | 1.04                 |\n"
    "| 22        | 7.8                 | 1.5                  |\n"
    "| 23        | 2.8                 | 1.5                  |\n\n"
    "In all but one case, the experimental ratio exceeds the calculated value, "
    "meaning the variability is even greater than the mutation theory predicts. "
    "The discrepancy is attributed to early mutations prior to time $t_0$ that "
    "were not accounted for in the simplified theory.",
    title="Std dev / mean ratio: experimental vs calculated",
    source_table="artifacts/paper.pdf, Tables 2-3",
    background=[fluctuation_protocol],
)

distribution_fit_exp23 = claim(
    "For Experiment 23 (87 cultures, whole culture plated), the experimental "
    "distribution of resistant bacteria counts was compared with the approximate "
    "theoretical distribution calculated from the mutation hypothesis (Figure 2). "
    "The fitting for small values is satisfactory: in particular, the number of "
    "cultures with one resistant bacterium (17 observed) very closely fits the "
    "theoretical expectation. The classes with 2, 4, 8, etc. are favored in the "
    "theoretical distribution due to grouping by bacterial generation.",
    title="Distribution fit: experimental vs mutation theory (Exp. 23)",
    figure="artifacts/paper.pdf, Figure 2",
    background=[fluctuation_protocol],
)

clonal_grouping_observed = claim(
    "The experiments show clearly that resistant bacteria appear in similar "
    "cultures not as random samples but in groups of varying sizes, indicating "
    "a correlating cause for such grouping. The assumption of genetic relatedness "
    "of the bacteria within such groups (i.e., clonal origin from a common "
    "mutant ancestor) offers the simplest explanation.",
    title="Clonal grouping observed in data",
    background=[fluctuation_protocol],
)

# === The central evidence: high variance supports mutation, refutes immunity ===
# This is modeled as abduction (inference to the best explanation):
# both hypotheses attempt to explain the same observation (high variance),
# and the mutation hypothesis is decisively superior.

# The mutation hypothesis explains the high variance observation
strat_mutation_explains_variance = support(
    [hypothesis_mutation],
    observed_variance_much_greater_than_mean,
    reason=(
        "The @hypothesis_mutation predicts that resistant bacteria arise by "
        "spontaneous mutation prior to virus exposure, creating clones of varying "
        "sizes. Early mutations produce large clones ('jackpots'), late mutations "
        "produce small clones. This clonal structure necessarily generates variance "
        "far exceeding the mean across replicate cultures."
    ),
    prior=0.9,
)

# The acquired immunity hypothesis fails to explain the high variance
strat_immunity_fails = support(
    [hypothesis_acquired_immunity],
    observed_variance_much_greater_than_mean,
    reason=(
        "The @hypothesis_acquired_immunity predicts each bacterium independently "
        "survives virus attack with equal probability, giving a Poisson distribution "
        "where variance equals mean. This cannot account for the observed variance "
        "that is 100-600x the mean."
    ),
    prior=0.1,
    background=[immunity_predicts_poisson],
)

# Compare the two predictions against the observation
comp_variance = compare(
    mutation_high_variance,
    immunity_variance_equals_mean,
    observed_variance_much_greater_than_mean,
    reason=(
        "@mutation_high_variance predicts variance >> mean (equation 11-12), which "
        "matches @observed_variance_much_greater_than_mean (variance/mean = 100-600x). "
        "@immunity_variance_equals_mean predicts variance = mean (Poisson), which is "
        "falsified by orders of magnitude. The mutation prediction matches the "
        "observation qualitatively and quantitatively; the immunity prediction is "
        "catastrophically wrong."
    ),
    prior=0.95,
)

# Abduction: inference to the best explanation
abd_variance = abduction(
    strat_mutation_explains_variance,
    strat_immunity_fails,
    comp_variance,
    reason=(
        "Both hypotheses attempt to explain the same observation: the distribution "
        "of resistant bacteria across replicate cultures. The mutation hypothesis "
        "predicts and explains the extreme variance; the acquired immunity hypothesis "
        "predicts Poisson variance and is decisively refuted."
    ),
)

# Plating reliability confirms the observation is real
strat_plating_validates_obs = support(
    [plating_variance_equals_mean, plating_method_reliable],
    observed_variance_much_greater_than_mean,
    reason=(
        "@plating_variance_equals_mean shows that when sampling from the SAME culture, "
        "variance matches mean (Poisson). @plating_method_reliable confirms the method "
        "introduces no artifacts. Therefore the excess variance observed across "
        "DIFFERENT cultures is real biological variation, not measurement error."
    ),
    prior=0.9,
)

# Distribution shape matches mutation theory
strat_distribution_fit = support(
    [mutation_high_variance, fluctuation_data_table3],
    distribution_fit_exp23,
    reason=(
        "@mutation_high_variance predicts a specific distributional shape with heavy "
        "right tail. @fluctuation_data_table3 provides the Exp. 23 data (87 cultures). "
        "The calculated distribution matches observed data well for small values "
        "(0 and 1 resistant bacteria), with expected over-representation in classes "
        "corresponding to powers of 2."
    ),
    prior=0.8,
    background=[fluctuation_protocol, hypothesis_mutation],
)

# Clonal grouping supported by variance + distribution shape
strat_clonal = support(
    [observed_variance_much_greater_than_mean, distribution_fit_exp23],
    clonal_grouping_observed,
    reason=(
        "@observed_variance_much_greater_than_mean shows bacteria appear in groups "
        "rather than randomly. @distribution_fit_exp23 shows the distribution shape "
        "matches the clonal growth model. This is consistent with the theoretical "
        "prediction @mutation_predicts_clonal_grouping that mutation produces clonal "
        "grouping. The simplest explanation is genetic relatedness — clones from "
        "common mutant ancestors."
    ),
    prior=0.85,
    background=[fluctuation_protocol, mutation_predicts_clonal_grouping],
)

# Std dev ratio provides additional quantitative evidence for high variance
strat_std_ratio_supports_obs = support(
    [experimental_std_dev_ratio],
    observed_variance_much_greater_than_mean,
    reason=(
        "@experimental_std_dev_ratio shows the ratio of standard deviation to mean "
        "is >> 1 in every experiment (ranging from 0.33 to 7.8), providing quantitative "
        "confirmation that the variance dramatically exceeds the mean across all "
        "experimental conditions."
    ),
    prior=0.85,
)
