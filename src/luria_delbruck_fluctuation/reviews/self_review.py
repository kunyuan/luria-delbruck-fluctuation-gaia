from gaia.review import ReviewBundle, review_claim

from ..motivation import hypothesis_mutation, hypothesis_acquired_immunity
from ..theory import (
    immunity_variance_equals_mean,
    mutation_high_variance,
    p0_mutation_rate_relation,
    mean_method_mutation_rate,
)
from ..exp_plating import plating_variance_equals_mean
from ..exp_fluctuation import (
    fluctuation_data_table2,
    fluctuation_data_table3,
    experimental_std_dev_ratio,
    observed_variance_much_greater_than_mean,
)
from ..mutation_rate import obs_broth_rate, obs_synth_rate
from ..discussion import aging_cultures_constant_fraction

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # === The two competing hypotheses (uninformative priors) ===
        review_claim(hypothesis_mutation, prior=0.5,
            judgment="tentative",
            justification="Uninformative prior. Evidence should determine belief."),
        review_claim(hypothesis_acquired_immunity, prior=0.5,
            judgment="tentative",
            justification="Uninformative prior. Evidence should determine belief."),

        # === Theoretical predictions (established mathematical derivations) ===
        review_claim(immunity_variance_equals_mean, prior=0.95,
            judgment="supporting",
            justification="Textbook Poisson result: independent events → variance = mean."),
        review_claim(mutation_high_variance, prior=0.9,
            judgment="supporting",
            justification="Sound derivation with simplifying assumptions. Qualitative result robust."),
        review_claim(p0_mutation_rate_relation, prior=0.95,
            judgment="supporting",
            justification="Direct Poisson property: P(0 events) = e^{-m}. Textbook result."),
        review_claim(mean_method_mutation_rate, prior=0.85,
            judgment="supporting",
            justification="Sound derivation with finite-sample approximation."),

        # === Experimental observations ===
        review_claim(plating_variance_equals_mean, prior=0.9,
            judgment="supporting",
            justification="Three independent experiments, all consistent with Poisson."),
        review_claim(fluctuation_data_table2, prior=0.9,
            judgment="supporting",
            justification="Primary data from 10 experiments. Directly observed counts."),
        review_claim(fluctuation_data_table3, prior=0.9,
            judgment="supporting",
            justification="Full distributions from 100 and 87 cultures. Large samples."),
        review_claim(observed_variance_much_greater_than_mean, prior=0.95,
            judgment="supporting",
            justification=(
                "Directly observed: variance/mean = 100-600x in every experiment. "
                "Confirmed by plating control (variance = mean for same-culture replicates)."
            )),
        review_claim(experimental_std_dev_ratio, prior=0.85,
            judgment="supporting",
            justification="Computed from raw data. Straightforward arithmetic."),
        review_claim(obs_broth_rate, prior=0.85,
            judgment="supporting",
            justification="Mutation rates from five broth experiments."),
        review_claim(obs_synth_rate, prior=0.85,
            judgment="supporting",
            justification="Mutation rates from four synthetic medium experiments."),
        review_claim(aging_cultures_constant_fraction, prior=0.8,
            judgment="supporting",
            justification="Single experiment, qualitatively clear."),
    ],
)
