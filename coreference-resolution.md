# Coreference Resolution

---

Referred materials:

> [http://web.stanford.edu/class/cs224n/lectures/lecture13.pdf](http://web.stanford.edu/class/cs224n/lectures/lecture13.pdf)

---

### Notes

Examples of why coreference resolution is difficulty:

> She poured water from the pitcher into **the cup** until **it** was full
>
> She poured water from **the pitcher** into the cup until **it** was empty
>
> **The trophy** would not fit in the suitcase because **it** was too big.
>
> The trophy would not fit in **the suitcase** because **it** was too small.

Fully understanding above sentences can be seen as another form of Strong AI, leading to the **Winograd Schema Challenge **

Mention Detection

* Three types: pronouns, named entities, noun phrase
* Hard =&gt; It is sunny; Every student; No student; The best donut in the world; 100 miles

Anaphora: 首语重复法

* 某mention由其antecedent决定

Bridging anaphora

* Not all anaphoric relations are coreferential

---

##### Approaches

Mention Pair

* Train a binary classifier that assigns every pair of menJons a probability of being coreferent: $$P\(m\_i, m\_j\)$$

* Testing: Pick some threshold \(e.g., 0.5\) and add coreference links between mention pairs where $$P\(m_i, m_\_j\)$$ is above the threshold

* Take the transitive closure to get the clustering

Mention Ranking

* Assign each mention its highest scoring candidate antecedent according to the model
* We want the current mention $$m_j$$ to be linked to any one of the candidate antecedents it’s coreferent with





