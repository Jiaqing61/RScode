## 📊 **Dataset Overview**

### Raw Datasets Overview

| **Dataset** | **Users** | **Items** | **Interactions** | **Avg/Use** | **Avg/Item** | **Sparsity** |
| ----------- | --------: | --------: | ---------------: | ----------: | -----------: | -----------: |
| ML-1M       |     6,040 |     3,883 |        1,000,209 |      165.60 |       269.89 |       95.53% |
| Lastfm-360K |   359,347 |   160,167 |       17,559,530 |       48.23 |       108.22 |       99.97% |

---

### 📁 Filtered Datasets Overview

| Dataset         |   Users |   Items | Interactions | Avg/User | Avg/Item | Sparsity | Deduplicated | K-core Applied |
| --------------- | ------: | ------: | -----------: | -------: | -------: | -------- | ------------ |----------------|
| **ML-1M**       |   6,040 |   3,706 |    1,000,209 |   165.60 |   269.89 | 95.53%   | No           | ✅ user≥5       |
| **Lastfm-360K** | 359,103 | 160,161 |   17,332,086 |    48.26 |   108.22 | 99.97%   | Yes          | ✅ user≥5       |

---

## 👤 User Attribute Grouping

### ML-1M

#### Age Groups

| Age Group | Users |
| --------- | ----: |
| 0-24      | 1,325 |
| 25-34     | 2,096 |
| 35-44     | 1,193 |
| 45+       | 1,426 |
| unknown   |     0 |

#### Activity Groups (based on interaction count)

| Group  | Users | Range       |
| ------ | ----: | ----------- |
| low    | 2,044 | [20, 57]    |
| medium | 1,988 | [57, 156]   |
| high   | 2,008 | [156, 2314] |

---

### Last.fm 360K

#### Age Groups

| Age Group |   Users |
| --------- | ------: |
| 0-24      | 168,381 |
| 25-34     |  85,561 |
| 35-44     |  20,752 |
| 45+       |   9,537 |
| unknown   |  74,870 |

#### Activity Groups

| Group  |   Users | Range     |
| ------ | ------: | --------- |
| low    | 121,957 | [5, 46]   |
| medium | 144,824 | [46, 50]  |
| high   |  92,322 | [50, 165] |

---

## 🎵 Item Popularity Grouping

### ML-1M

| Popularity Group | Items | Percentage |
| ---------------- | ----: | ---------: |
| head             | 1,181 |     31.87% |
| tail             | 2,525 |     68.13% |

> **Note**: Last.fm has no item file, so item grouping was not applied.

---

## ✅ Filtered Files Location

| Dataset | Path                                      |
| ------- | ----------------------------------------- |
| ML-1M   | `datasets/filtered_datasets/ml-1m/`       |
| LastFM  | `datasets/filtered_datasets/lastfm-360k/` |

---

## 📌 Notes

- Interactions filtered to ensure minimum 5 per user (for fair test splitting).
- Age groups assigned via binning; unknown ages grouped as `"unknown"`.
- Activity groups based on **quantile** binning of user interaction counts.

---

## 📐 Evaluation Setup

### Evaluation Protocol

- **Split:** Random (`RS`) → 80% Train, 10% Validation, 10% Test
- **Ordering:** Random (`RO`)
- **Group By:** User-level splitting
- **Candidate Strategy:** Full ranking (excluding training items)

### Metrics Used

- **Top-K Metrics:** Evaluated at K = 10
- **Early Stopping:** Based on `NDCG@10`

| **Metric Type**        | **Metrics**                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| **Accuracy**           | Recall, Precision, NDCG, MRR, MAP, Hit Ratio                                                         |
| **Fairness/Diversity** | ItemCoverage, AveragePopularity, GiniIndex, ShannonEntropy, TailPercentage, CumulativeTailPercentage |

> `tail_ratio: 0.2` defines the long-tail bottom 20% of items.
