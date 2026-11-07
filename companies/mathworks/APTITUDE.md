# MathWorks OA: aptitude questions

The OA has **5 aptitude MCQs** next to the 3 coding questions. Candidates called them easy.
Two were captured in screenshots; they're reproduced below. Answers are at the bottom, so try first.

---

## A1. Poisson distribution

A chart shows the probability mass function P(X = k) of a Poisson distribution for three different
expected rates of occurrence, named A, B and C (k on the x-axis from 0 to 20):

- **A** peaks at about 0.37 at k = 0 and k = 1, and is almost 0 by k = 5.
- **B** peaks at about 0.20 around k = 3 and k = 4, and is almost 0 by k = 10.
- **C** peaks at about 0.13 around k = 9 and k = 10, and spreads out to about k = 20.

What is the relationship between them?

- (a) A > B > C
- (b) A < B < C
- (c) A = B = C
- (d) Cannot be determined

---

## A2. Interpret charts

The chart and table give the per-unit production cost, the producer's selling price and the retailer's
selling price of 5 articles, A to E (prices in rupees).

| | A | B | C | D | E |
|---|---|---|---|---|---|
| Production cost | 20 | 50 | 12 | 25 | 15 |
| Producer's selling price | 25 | 52 | 15 | 28 | 18 |
| Retailer's selling price | 30 | 58 | 16 | 32 | 20 |

The retailer sells products A, B, C and D at a 10% discount on the reported "Retailer's Selling Price".
Which of the 4 products is sold at a loss?

- (a) A
- (b) D
- (c) C
- (d) B

> Note: the photo of this question was blurry. The numbers in the table are my best reading of it
> (cross-checked against the bar heights), so the real test may have used slightly different values.
> The method is what matters.

---

## Answers

**A1: (b) A < B < C.** A Poisson distribution with rate λ peaks at k ≈ λ (at k = λ − 1 and k = λ when λ is
a whole number), and its mean is λ. A peaks at 0–1 (λ ≈ 1), B at 3–4 (λ ≈ 4), C at 9–10 (λ ≈ 10).
Larger λ also means a lower, wider peak, which matches the chart.

**A2: (c) C.** The retailer buys at the producer's selling price and sells at 90% of the retailer's price:

| | A | B | C | D |
|---|---|---|---|---|
| Buys at | 25 | 52 | 15 | 28 |
| Sells at (0.9 × retail) | 27 | 52.2 | 14.4 | 28.8 |
| Result | profit 2 | profit 0.2 | **loss 0.6** | profit 0.8 |
