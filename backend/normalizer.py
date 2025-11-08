# Data normalizer
from typing import List, Dict

def normalize_metrics(metrics: List[Dict]):
    # fill missing numeric fields with zeros and sort by timestamp
    for m in metrics:
        m.setdefault('likes', 0)
        m.setdefault('comments', 0)
        m.setdefault('followers', None)
    metrics.sort(key=lambda x: x.get('timestamp'))
    return metrics
