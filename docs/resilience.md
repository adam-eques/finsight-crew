# Resilience

Network-facing tools use `finsight.net.retry` for exponential-backoff
retries, and `finsight.cache.DiskCache` to avoid re-fetching the same
data within a TTL window. Both are dependency-free and unit-tested.
