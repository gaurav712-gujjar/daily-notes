# Untitled Note - 1142

**Category:** Deep Learning  
**Date:** 2026-11-12 (morning)

---

# Neural Architecture Search (NAS)

Neural Architecture Search is an automated method for discovering high‑performing neural network structures. Instead of manually designing layers, connections, and hyper‑parameters, NAS treats the architecture itself as a searchable space and employs an optimization algorithm (e.g., reinforcement learning, evolutionary strategies, or Bayesian optimization) to explore it. The search controller proposes candidate architectures, which are trained (often partially) to estimate their performance; the controller then updates its policy to favor better designs.

**Why use NAS?**  
- **Efficiency:** Saves expert time, especially for novel domains where intuition about good architectures is limited.  
- **Performance:** Often yields models that outperform hand‑crafted baselines, as seen in image classification (e.g., EfficientNet) and language modeling.  
- **Adaptability:** Can tailor architectures to specific hardware constraints (latency, memory) by incorporating them into the reward function.

**Simple example with Keras Tuner (Bayesian optimization)**

```python
import tensorflow as tf
from tensorflow import keras
from keras_tuner import BayesianOptimization

def build_model(hp):
    model = keras.Sequential()
    # Search over number of Conv layers
    for i in range(hp.Int('conv_layers', 1, 3)):
        model.add(
            keras.layers.Conv2D(
                filters=hp.Choice(f'filters_{i}', [32, 64, 128]),
                kernel_size=hp.Choice(f'kernel_{i}', [3, 5]),
                activation='relu',
                padding='same'
            )
        )
        model.add(keras.layers.MaxPooling2D())
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(
        units=hp.Int('dense_units', 64, 256, step=64),
        activation='relu'
    ))
    model.add(keras.layers.Dense(10, activation='softmax'))
    model.compile(
        optimizer=keras.optimizers.Adam(
            hp.Float('lr', 1e-4, 1e-2, sampling='log')
        ),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return
