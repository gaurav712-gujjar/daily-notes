# Temporal Fusion

**Category:** Data Science  
**Date:** 2026-10-29 (afternoon)

---

# Temporal Fusion Transformer (TFT)

The Temporal Fusion Transformer is a deep learning architecture designed for multi‑horizon time‑series forecasting. It blends the strengths of recurrent networks (for handling sequential data) with the self‑attention mechanism of Transformers, while adding specialized components such as variable selection networks, gating layers, and static covariate encoders. This enables TFT to automatically learn which inputs are most relevant at each time step and to model both short‑ and long‑range dependencies.

**Why use TFT?**  
- **Mixed data types:** Handles numeric, categorical, known‑future, and observed‑past features in a single model.  
- **Interpretability:** Provides attention weights and variable importance scores, helping analysts understand drivers behind forecasts.  
- **Multi‑horizon forecasts:** Generates predictions for multiple future steps simultaneously, useful for inventory planning, energy demand, and finance.  
- **Robustness to missing data:** Built‑in gating mechanisms mitigate the impact of gaps in the series.

**Quick example with `pytorch‑forecasting`**

```python
import pandas as pd
from pytorch_forecasting import TimeSeriesDataSet, TemporalFusionTransformer
from pytorch_forecasting.data import GroupNormalizer
from pytorch_lightning import Trainer

# Load data (timestamp, series_id, target, and covariates)
df = pd.read_csv("sales.csv", parse_dates=["date"])

# Define dataset
training = TimeSeriesDataSet(
    df,
    time_idx="date_idx",
    target="sales",
    group_ids=["store_id"],
    max_encoder_length=30,
    max_prediction_length=7,
    static_categoricals=["store_id"],
    time_varying_known_categoricals=["promo"],
    time_varying_known_reals=["price"],
    time_varying_unknown_reals=["sales"],
    target_normalizer=GroupNormalizer(groups=["store_id"]),
    add_relative_time_idx=True,
    add_target_scales=True,
)

# Create dataloaders
train_loader = training.to_dataloader(train=True, batch_size=64, num_workers=4)

# Initialise TFT model
tft = TemporalFusionTransformer.from_dataset(
    training,
    learning_rate=1e-3,
    hidden_size=16,
    attention_head_size=1,
    dropout=0.1,
    loss="mae",
)

# Train
trainer = Trainer(gpus=1, max_epochs=20)
trainer.fit(tft, train_loader)
```

The trained TFT can now produce 7‑day‑ahead forecasts for each store, with built‑in methods to extract attention maps and feature importance, turning a black‑box model into a more explainable forecasting tool.
