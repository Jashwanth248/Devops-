# PulseCart SLOs

## Gateway availability
- **SLI:** successful non-5xx requests / all requests
- **SLO:** 99.9% over a rolling 30-day window
- **Error budget:** approximately 0.1% failed requests in the window

## Gateway latency
- **SLI:** proportion of requests under 500 ms
- **SLO:** 99% under 500 ms over 30 days

## Operational policy
If the availability error budget burns too quickly, feature rollout slows and reliability work takes priority. Canary analysis is intentionally stricter than the long-window SLO so bad releases can be stopped early.
