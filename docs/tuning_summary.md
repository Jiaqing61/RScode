# 🔧 Hyperparameter Tuning Results

## 1. BPR (Bayesian Personalized Ranking)
BPR is a **pairwise ranking** algorithm that learns by comparing item pairs during training—optimizing for a user to rank a positive item higher than a sampled negative one.

| Parameter                 | Value on Lastfm NL | Value on MovieLens 1M |
| ------------------------- |--------------------|-----------------------|
| **Embedding Size**        | 128                | 64                    |
| **Learning Rate**         | 0.001              | 0.0005                |
| **Train Batch Size**      | 2048               | 1024                  |
| **Epochs**                | 100                | 100                   |
| **Regularization Weight** | 0.0001             | 0.0003                |
| **Seed**                  | 42                 | 42                    |
| **Duration**              | 7m 21s             | 4m 52s                |
| **Best Validation Score** | 0.36926            | 0.07745               |
| **Gini @10**              | 0.56331            | –                     |
| **Tail% @10**             | 0.03206            | –                     |

### Interpretation of Validation Scores:

* **Higher NDCG\@10 scores** are common on **smaller, sparser datasets** like **Lastfm NL**, where the **signal-to-noise ratio is higher** and models like BPR can more easily **overfit to limited user interactions**.
* In contrast, **MovieLens 1M** is **less sparse (95.16%)**, significantly **larger**, and includes **more interactions per user**, resulting in **broader and more complex user preference distributions**. These factors make it more difficult to rank truly relevant items at the top, often leading to lower NDCG\@10 scores.

> **Note:** The higher validation score on Lastfm NL (NDCG\@10 = 0.36926) compared to MovieLens 1M (NDCG\@10 = 0.07745) primarily reflects **Lastfm NL extreme sparsity (99.86%) and smaller scale**. This does **not indicate better generalization**, but rather highlights the **ease with which BPR can distinguish between positives and negatives** in such limited settings.
>
> By contrast, **MovieLens 1M**, with its **richer interaction histories and denser user-item coverage**, presents a **more realistic generalization challenge**. As a result, the lower NDCG\@10 score on MovieLens is likely a **more representative measure of real-world model performance**.

---
### 🔍 Notes

| Model           | Category                  | Optimization | Description                                                                   |
| --------------- | ------------------------- | ------------ | ----------------------------------------------------------------------------- |
| **BPR**         | Matrix Factorization (MF) | Pairwise     | Classical MF model optimized via Bayesian pairwise ranking.                   |


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
