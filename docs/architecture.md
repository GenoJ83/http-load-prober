# Architecture

```mermaid
flowchart TD
    CLI --> Engine[Worker Pool]
    Engine --> Probes[Async Probes]
    Probes --> Aggregator[Percentile Stats]
    Aggregator --> Output[Terminal / JSON]
```
