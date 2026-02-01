# 🛡️ Network Security Machine Learning Pipeline

This repository hosts an end-to-end ML pipeline designed to analyze network traffic and predict security events.

---

## 🛠️ Tech Stack
* **Database:** MongoDB
* **Experiment Tracking:** MLflow
* **Remote Storage:** Dagshub
* **Web Interface:** FastAPI

---

##  Pipeline Architecture

### 1. Data Ingestion
The ingestion phase extracts raw data from MongoDB and prepares it for the machine learning workflow.

**Key Steps:**
* **Configuration:** Defines paths for the feature store, training/testing sets, and the MongoDB collection.
* **Export to Feature Store:** Raw data is pulled from the database and saved as a baseline CSV.
* **Train-Test Split:** Splitting data based on a predefined ratio (e.g., 80/20).
* **Artifact Generation:** Records metadata and file paths for reproducibility.

**Outputs:**
* `feature_store/raw_data.csv`
* `ingested/train.csv` & `ingested/test.csv`

---

### 2. Data Validation
Ensures data quality and consistency before transformation or training.



**Validation Checks:**
* **Schema Validation:** Verifies column counts and data types against a predefined schema.
* **Numerical Consistency:** Checks for the presence of required numerical features.
* **Data Drift Detection:** Checks if the data distribution has shifted significantly.
* **Artifact Generation:** Produces a final `drift_report.json`.

---

##  Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
