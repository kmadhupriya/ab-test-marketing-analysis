# Marketing A/B Test Analysis

## Problem
Determine if showing ads to users significantly increases conversion rate compared to a control group (PSA).

## Data
User-level data with test group (ad/psa) and conversion status (marketing_AB dataset from Kaggle).

## Method
Python (pandas, scipy) — calculated conversion rates by group, ran Chi-square test for statistical significance.

## Key Findings
- Ad group conversion rate: 2.55%
- PSA (control) group conversion rate: 1.79%
- Chi-square test: p-value < 0.0001 — difference is statistically significant

## Recommendation
Ads significantly increase conversion rate (~42% relative lift). Continued investment in ad campaigns is data-backed and justified. ab-test-marketing-analysis
Statistical A/B test analysis on marketing data using Python — determined if ad campaigns significantly increase conversion rate using Chi-square test.
