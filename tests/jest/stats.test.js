const { calculatePercentiles } = require('../../js/stats');

describe('Latency Percentiles', () => {
  it('computes correct percentiles for sorted and unsorted latency arrays', () => {
    const data = [10, 40, 20, 50, 30, 100];
    const res = calculatePercentiles(data);
    expect(res.p50).toBe(40);
    expect(res.p95).toBe(100);
  });
  it('handles empty input gracefully', () => {
    expect(calculatePercentiles([]).p50).toBe(0);
  });
});
