# Knowledge Distillation

**Category:** Machine Learning  
**Date:** 2026-09-10 (afternoon)

---

# Knowledge Distillation

Knowledge Distillation is a model compression technique where a **large, high‑capacity “teacher” network** transfers its learned representations to a **smaller “student” model**. Instead of training the student only on hard class labels, it is trained on the **soft probability distribution** (logits) produced by the teacher, usually after applying a temperature‑scaled softmax. The softened outputs contain richer information about inter‑class similarities, guiding the student to mimic the teacher’s decision surface.

**Why use it?**  
- Deploy models on edge devices with limited memory or compute.  
- Reduce inference latency while retaining most of the teacher’s accuracy.  
- Enable ensembling benefits without the runtime cost of multiple models.

**Typical workflow**
1. Train a powerful teacher (e.g., ResNet‑152).  
2. Freeze the teacher and generate soft targets for the training set.  
3. Train the student (e.g., MobileNet‑V2) using a combined loss:
   \[
   L = \alpha \, L_{\text{CE}}(y, p_{\text{student}}) + (1-\alpha) \, L_{\text{KD}}(p_{\text{teacher}}^{T}, p_{\text{student}}^{T})
   \]
   where \(T\) is the temperature and \(\alpha\) balances hard and soft losses.

**Simple PyTorch example**

```python
import torch, torch.nn as nn, torch.nn.functional as F

def distillation_loss(student_logits, teacher_logits, targets,
                      T=4.0, alpha=0.7):
    # Soft targets
    soft_teacher = F.log_softmax(teacher_logits / T, dim=1)
    soft_student = F.log_softmax(student_logits / T, dim=1)
    kd_loss = F.kl_div(soft_student, soft_teacher, reduction='batchmean') * (T ** 2)

    # Hard targets
    ce_loss = F.cross_entropy(student_logits, targets)

    return alpha * ce_loss + (1 - alpha) * kd_loss
```

The function combines cross‑entropy with Kullback‑Leibler divergence, enabling the student to learn both from true labels and the teacher’s nuanced predictions.

---
