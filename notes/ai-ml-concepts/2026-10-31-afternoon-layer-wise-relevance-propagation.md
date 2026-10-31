# Layer-wise Relevance Propagation

**Category:** AI/ML Concepts  
**Date:** 2026-10-31 (afternoon)

---

# Layer‑wise Relevance Propagation (LRP)

Layer‑wise Relevance Propagation is a post‑hoc interpretability technique for deep neural networks. After a forward pass, LRP redistributes the prediction score \(f(x)\) backwards through the network layers, assigning a *relevance* value \(R_i\) to each neuron (or input feature) such that the sum of relevances equals the output score. The redistribution follows simple conservation rules, e.g., the **z‑rule**:

\[
R_j = \sum_i \frac{a_j w_{ij}}{\sum_k a_k w_{ik} + \epsilon} \, R_i
\]

where \(a_j\) is the activation of neuron \(j\), \(w_{ij}\) the weight to neuron \(i\), and \(\epsilon\) a stabilizer. The result is a heatmap that highlights which input pixels contributed most to the decision, offering a more faithful alternative to gradient‑based saliency maps.

**Why use LRP?**  
- **Model debugging**: Detect spurious correlations (e.g., a classifier focusing on background).  
- **Regulatory compliance**: Provide explanations required in high‑stakes domains like medical imaging.  
- **Feature importance**: Obtain class‑specific importance without retraining.

**Quick example (PyTorch + innvestigate‑pytorch)**

```python
import torch, torchvision
from innvestigate import LRP
from innvestigate.utils import visualize_heatmap

model = torchvision.models.resnet18(pretrained=True).eval()
lrp = LRP(model, rule="z")          # instantiate with the z‑rule

img = torchvision.io.read_image('cat.jpg').unsqueeze(0).float() / 255
output = model(img)
pred_class = output.argmax(dim=1)

relevance = lrp(img, target=pred_class)   # shape: (1,3,H,W)
heatmap = visualize_heatmap(relevance.squeeze(0))
heatmap.save('lrp_cat_heatmap.png')
```

The generated heatmap shows which regions of the cat image most influenced the network’s prediction.

---
