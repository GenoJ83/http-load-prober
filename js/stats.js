function calculatePercentiles(latencies) {
  if (!latencies || latencies.length === 0) return { p50: 0, p90: 0, p95: 0, p99: 0 };
  const sorted = [...latencies].sort((a, b) => a - b);
  const getP = (p) => {
    const idx = Math.min(sorted.length - 1, Math.floor((p / 100) * sorted.length));
    return sorted[idx];
  };
  return { p50: getP(50), p90: getP(90), p95: getP(95), p99: getP(99) };
}
module.exports = { calculatePercentiles };
