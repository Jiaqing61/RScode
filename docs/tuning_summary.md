# 🔧 Hyperparameter Tuning Results

## 1. BPR (Bayesian Personalized Ranking)
BPR is a **pairwise ranking** algorithm that learns by comparing item pairs during training—optimizing for a user to rank a positive item higher than a sampled negative one.

| Parameter                 | Value on Amazon Beauty | Value on MovieLens 1M |
| ------------------------- | ---------------------- | --------------------- |
| **Sweep ID**              | `y8o40b8x`             | –                     |
| **Embedding Size**        | 128                    | 64                    |
| **Learning Rate**         | 0.001                  | 0.001                 |
| **Train Batch Size**      | 512                    | 1024                  |
| **Epochs**                | 60                     | 60                    |
| **Regularization Weight** | 0.0001                 | 0.0002                |
| **Seed**                  | 42                     | 42                    |
| **Duration**              | 7m 21s                 | 7m 52s                |
| **Best Validation Score** | 0.36926                | 0.07745               |
| **Gini @10**              | 0.56331                | –                |
| **Tail% @10**             | 0.03206                | –                     |

### Interpretation of Validation Scores:

* **Higher NDCG\@10 scores** are common on **smaller, sparser datasets** like **Amazon Beauty**, where the **signal-to-noise ratio is higher** and models like BPR can more easily **overfit to limited user interactions**.
* In contrast, **MovieLens 1M** is **less sparse (95.16%)**, significantly **larger**, and includes **more interactions per user**, resulting in **broader and more complex user preference distributions**. These factors make it more difficult to rank truly relevant items at the top, often leading to lower NDCG\@10 scores.

> **Note:** The higher validation score on Amazon Beauty (NDCG\@10 = 0.36926) compared to MovieLens 1M (NDCG\@10 = 0.07745) primarily reflects **Amazon Beauty’s extreme sparsity (99.74%) and smaller scale**. This does **not indicate better generalization**, but rather highlights the **ease with which BPR can distinguish between positives and negatives** in such limited settings.
>
> By contrast, **MovieLens 1M**, with its **richer interaction histories and denser user-item coverage**, presents a **more realistic generalization challenge**. As a result, the lower NDCG\@10 score on MovieLens is likely a **more representative measure of real-world model performance**.



## 2. SLIMElastic

**SLIMElastic** is a **sparse linear item-item model** that learns a similarity matrix by fitting each item's interactions as a sparse linear combination of others, regularized with L1 and L2 penalties.

| Parameter                 | Value on Amazon Beauty | Value on MovieLens 1M |
| ------------------------- | ---------------------- | --------------------- |
| **Sweep ID**              | `2q0qqmxa`             | `shi7v2cd`            |
| **Alpha**                 | 0.6                    | 0.1                   |
| **L1 Ratio**              | 0.0001                 | 0.1                   |
| **Train Batch Size**      | 1024                   | 2048                  |
| **Duration**              | 13.47s                 | 3m 50s                |
| **Seed**                  | 42                     | 42                    |
| **Best Validation Score** | 0.03623                | 0.1037                |
| **Gini @10**              | 0.7824                 | 0.9686                |
| **Tail% @10**             | 0.00997                | 0                     |
---

### Interpretation:

* SLIMElastic performs **substantially better on MovieLens 1M** than on Amazon Beauty, which aligns with expectations given the **lower sparsity and higher interaction density** of MovieLens.
* In **Amazon Beauty**, the extreme sparsity limits item co-occurrence signals, constraining SLIMElastic's ability to learn meaningful relationships—resulting in lower accuracy and fairness.
* Conversely, **MovieLens 1M** offers sufficient co-rated item data, allowing SLIMElastic to leverage its **linear item-item modeling** more effectively, especially with a **larger batch size** and **moderate regularization**.

> **Note:** The higher validation score on MovieLens 1M (NDCG\@10 = 0.1037) versus Amazon Beauty (NDCG\@10 = 0.03623) reflects SLIMElastic’s strong dependence on **item-item co-occurrence patterns**.
>
> The **extreme sparsity (99.74%)** of Amazon Beauty limits learning opportunities, leading to poorer performance and higher concentration on popular items (as seen in the low Tail\@10 and lower Gini).
>
> In contrast, **MovieLens 1M**, with its **denser interaction matrix**, better supports SLIM’s assumptions and design. The resulting improvement in both accuracy and moderate item coverage demonstrates the model’s potential when applied to well-connected domains.

---


## 3. LightGCN
**LightGCN** is a **simplified graph convolutional network** that propagates user-item embeddings across the interaction graph without feature transformation or non-linearity, relying purely on collaborative signals.

| Parameter                 | Value on Amazon Beauty   | Value on MovieLens 1M |
| ------------------------- |---| --------------------- |
| **Sweep ID**              |   | `zvscx2mp`            |
| **Embedding Size**        |   | 128                   |
| **Learning Rate**         |   | 0.0016164032755262689 |
| **Train Batch Size**      |   | 2048                  |
| **Epochs**                |   | 60                    |
| **Number of Layers**      |   | 5                     |
| **Regularization Weight** |   | 0.0004201582529973613 |
| **Seed**                  |   | 42                    |
| **Duration**              |   | 38m 8s                |
| **Best Validation Score** |   | 0.08344               |
| **Gini @10**              |   | 0.9296                |
| **Tail% @10**             |   | 0.00023               |


---

## 4. NeuMF (Neural Matrix Factorization)
**NeuMF** combines generalized matrix factorization with multi-layer perceptrons to capture both linear and nonlinear user-item interaction patterns.

*(Add table when values are available)*

---

## 5. DiffRec
**DiffRec** models recommendations using **diffusion processes over user-item graphs**, learning how preferences spread through local and global neighborhood structures.

*(Add table when values are available)*

---

## 6. NCL (Neural Contrastive Learning)
**NCL** applies **contrastive learning objectives** to collaborative filtering, encouraging similar users/items to have similar representations by maximizing agreement between augmentations.

*(Add table when values are available)*

---

## 7. NGCF (Neural Graph Collaborative Filtering)
**NGCF** extends GCNs to recommendation by modeling **high-order connectivity** in user-item graphs with nonlinear feature transformations and message passing.

*(Add table when values are available)*

---
## 8.  MultiVae (Optoinal)

**MultiVAE** is a **variational autoencoder for collaborative filtering**, modeling user preferences probabilistically while regularizing latent factors through a KL-divergence penalty.

*(Add table when values are available)*

---


## Expected Performance

### Overview

Model performance varies across datasets due to differences in **sparsity**, **scale**, and **interaction richness**:

* On **sparse datasets** like **Amazon Beauty** (99.74% sparse), models may achieve deceptively **high validation scores** by overfitting to the limited number of interactions. However, these scores often **fail to reflect generalization ability**, especially in real-world settings.
* On **denser datasets** like **MovieLens 1M** (95.16% sparse), models encounter **richer user–item interaction patterns**, resulting in **more challenging but reliable evaluations**. Scores are typically lower but more reflective of real-world performance.
* **Linear models** (e.g., SLIM) rely on co-occurrence signals and tend to **underperform on sparse datasets**, where such patterns are weak or inconsistent.
* **Graph-based models** (e.g., LightGCN, NGCF) and **neural models** (e.g., NeuMF, NCL) tend to perform **better on denser datasets**, where structural and semantic patterns are more pronounced.
* **Diffusion-based** and **generative models** (e.g., DiffRec, MultiVAE) are more flexible and can perform well in both sparse and dense settings, but are typically **more sensitive to hyperparameter tuning and regularization**.
* **NCL**, which incorporates contrastive learning, may perform better than other neural models in sparse scenarios by extracting structure from limited interactions.

> All models are tuned separately for each dataset. As such, performance reflects the **best achievable outcome per setting**, and any observed gaps are more likely due to **fundamental differences in model design or suitability**, rather than tuning quality.

---

### Expected Relative Performance by Model and Dataset (After Dataset-Specific Tuning)

| Model                     | Amazon Beauty (Sparse) | MovieLens 1M (Dense) |
| ------------------------- | ---------------------- | -------------------- |
| **BPR**                   | ★★☆☆☆ (moderate)       | ★★★☆☆ (moderate)     |
| **SLIMElastic**           | ★☆☆☆☆ (low)            | ★★★★★ (very high)    |
| **LightGCN**              | ★★★★☆ (high)           | ★★★★☆ (high)         |
| **NeuMF**                 | ★★★★☆ (high)           | ★★★★☆ (high)         |
| **NGCF**                  | ★★☆☆☆ (moderate)       | ★★★★☆ (high)         |
| **NCL**                   | ★★★★☆ (high)           | ★★★☆☆ (moderate)     |
| **DiffRec**               | ★★★★☆ (high)           | ★★★☆☆ (moderate)     |
| **MultiVAE** *(Optional)* | ★★☆☆☆ (moderate)       | ★★☆☆☆ (moderate)     |

> ★★★★★ = highest expected performance
> ★☆☆☆☆ = lowest expected performance
>
> Performance reflects **dataset-specific tuning**. Stars indicate the **relative performance ceiling** under best-case configuration.

---

### 🧠 Model Categorization

| Model           | Category                  | Optimization | Description                                                                   |
| --------------- | ------------------------- | ------------ | ----------------------------------------------------------------------------- |
| **BPR**         | Matrix Factorization (MF) | Pairwise     | Classical MF model optimized via Bayesian pairwise ranking.                   |
| **LightGCN**    | Graph-based               | Pairwise     | Lightweight GCN that propagates embeddings over the user–item graph.          |
| **DiffRec**     | Diffusion-based           | Pairwise     | Uses diffusion over interaction graphs to model preference propagation.       |
| **SLIMElastic** | Linear Model              | Pointwise    | Sparse linear model that learns item–item similarity through regression.      |
| **NeuMF**       | Neural MF                 | Pointwise    | Combines MF and MLP to capture complex user–item interactions.                |
| **NGCF**        | Graph-based (neural)      | Pointwise    | GCN model with embedding transformations to capture high-order connectivity.  |
| **MultiVAE**    | Generative (VAE-based)    | Pointwise    | Variational autoencoder for collaborative filtering using user-item profiles. |
| **NCL**         | Neural (contrastive)      | Contrastive  | Learns representations by contrasting augmented user/item views.              |

---

### 🔍 Notes

* **Pointwise**: Predicts scores for individual user–item pairs.
* **Pairwise**: Optimizes relative ranking between items (e.g., one item over another).
* **Contrastive**: Learns representations by enforcing similarity between augmented views.
* **Linear vs Neural**: Linear models assume additive patterns; neural models capture nonlinear relationships.
* **Graph-based**: Leverage user–item graphs to propagate or transform embeddings.

---

| Split | Recall\@10 | Recall\@20 | Precision\@10 | Precision\@20 | NDCG\@10 | NDCG\@20 | MAP\@10 | MAP\@20 | Hit\@10 | Hit\@20 |
| ----- | ---------- | ---------- | ------------- | ------------- | -------- | -------- | ------- | ------- | ------- | ------- |
| Valid | 0.07538    | 0.13552    | 0.05515       | 0.05158       | 0.07442  | 0.09455  | 0.03159 | 0.03373 | 0.42282 | 0.63084 |
| Test  | 0.07806    | 0.14117    | 0.05442       | 0.05166       | 0.07514  | 0.09701  | 0.03225 | 0.03509 | 0.42845 | 0.64425 |

| Split | Gini\@10 | Gini\@20 | Shannon\@10 | Shannon\@20 | Tail% @10 | Tail% @20 | ItemCoverage\@10 | ItemCoverage\@20 | AvgPopularity\@10 | AvgPopularity\@20 |
| ----- | -------- | -------- | ----------- | ----------- | --------- | --------- | ---------------- | ---------------- | ----------------- | ----------------- |
| Valid | 0.93190  | 0.91450  | 0.00445     | 0.00372     | 0.00022   | 0.00025   | 0.37213          | 0.46826          | 1312.80787        | 1238.19427        |
| Test  | 0.93190  | 0.91450  | 0.00445     | 0.00372     | 0.00022   | 0.00025   | 0.37213          | 0.46826          | 1312.80787        | 1238.19427        |



## Note
x epoch y loss for item, user groups.
