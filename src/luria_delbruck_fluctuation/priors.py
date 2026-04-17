"""Leaf-node priors for the Luria-Delbrück fluctuation test package."""

from . import (
    # Competing hypotheses (now premises of abduction)
    hypothesis_mutation,
    hypothesis_acquired_immunity,
    # Theoretical predictions (established math derivations)
    immunity_variance_equals_mean,
    mutation_high_variance,
    p0_mutation_rate_relation,
    mean_method_mutation_rate,
    # Experimental observations
    plating_variance_equals_mean,
    fluctuation_data_table2,
    fluctuation_data_table3,
    experimental_std_dev_ratio,
    # Mutation rate observations
    obs_broth_rate,
    obs_synth_rate,
    # Discussion
    aging_cultures_constant_fraction,
)

PRIORS = {
    # Competing hypotheses — uninformative priors; evidence determines belief
    hypothesis_mutation: (
        0.5,
        "Uninformative prior. Evidence should determine belief.",
    ),
    hypothesis_acquired_immunity: (
        0.5,
        "Uninformative prior. Evidence should determine belief.",
    ),
    # Theoretical predictions — sound mathematical derivations
    immunity_variance_equals_mean: (
        0.95,
        "Textbook Poisson result: independent events → variance = mean.",
    ),
    mutation_high_variance: (
        0.9,
        "Sound derivation with simplifying assumptions. Qualitative result robust.",
    ),
    p0_mutation_rate_relation: (
        0.95,
        "Direct Poisson property: P(0 events) = e^{-m}. Textbook result.",
    ),
    mean_method_mutation_rate: (
        0.85,
        "Sound derivation with finite-sample approximation.",
    ),
    # Experimental observations — directly measured data
    plating_variance_equals_mean: (
        0.9,
        "Three independent experiments, all consistent with Poisson sampling.",
    ),
    fluctuation_data_table2: (
        0.9,
        "Primary data from 10 experiments. Directly observed counts.",
    ),
    fluctuation_data_table3: (
        0.9,
        "Full distributions from 100 and 87 cultures. Large samples.",
    ),
    experimental_std_dev_ratio: (
        0.85,
        "Computed from raw data. Straightforward arithmetic.",
    ),
    # Mutation rate observations from Table 4
    obs_broth_rate: (
        0.85,
        "Mutation rates from five broth experiments.",
    ),
    obs_synth_rate: (
        0.85,
        "Mutation rates from four synthetic medium experiments.",
    ),
    # Aging culture result
    aging_cultures_constant_fraction: (
        0.8,
        "Single experiment, qualitatively clear.",
    ),
}
