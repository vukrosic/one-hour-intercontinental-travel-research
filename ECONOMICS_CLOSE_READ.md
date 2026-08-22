# Historical economics close read

## Question

What does public historical and current NASA evidence actually establish about
the economics of faster civilian passenger aircraft?

The narrow answer is: the historical Mach 2 anchor has adverse economics in a
dated, explicit comparison, while current high-speed market viability remains
an open research question. No source in this close read establishes a current
commercial business case or a universal cost penalty for every future speed
class.

## Primary evidence

| Record | Extracted claim | Evidence state |
|---|---|---|
| NASA 1988 HSCT propulsion paper (`NASA_HSCT_PROPULSION_1988`) | Concorde is described as about three times the fuel per seat-mile and about twice the total operating cost of comparable-era subsonic transports. | Quantified historical adverse evidence; comparator era is explicit and dated. |
| NASA 1989 HSCT study (`NASA_HSCT_STUDY_1989`) | A high-speed civil-transport system study treats technological, economic, and environmental constraints together. | Historical programme context; not a current cost dataset. |
| NASA 2020 high-speed market studies (`NASA_HIGH_SPEED_MARKET_STUDIES_2020`) | NASA reports independent studies investigating economic viability, while environmental restrictions remain relevant. | Current research status; no numerical business case extracted. |
| NASA 2023 historical synthesis (`NASA_SP4539_SUPERSONIC_2023`) | Higher passenger cost and technical/political development risk recur in the civil-supersonic history. | Qualitative synthesis; not a current utilization or fare forecast. |

The structured extraction is in [`economics_close_read.csv`](economics_close_read.csv).
It contains one quantified historical row, one current market-research row, one
qualitative synthesis row, zero current empirical business-case rows, and zero
economic practical passes.

## Reproducibility

```text
python3 economics_close_read.py
python3 economics_close_read_independent_check.py
```

The first command writes [`economics_close_read_summary.csv`](economics_close_read_summary.csv).
The independent bookkeeping implementation writes
[`economics_close_read_independent_check.csv`](economics_close_read_independent_check.csv)
and reproduces all seven summary metrics.

## Interpretation and limits

- The historical NASA comparison corroborates the repository's separate
  Concorde energy-intensity result, but the two are not independent modern
  forecasts.
- A historical total-operating-cost ratio is not a current fare, profit,
  utilization, reliability, maintenance, or lifecycle-climate model.
- The NASA market-study page establishes research activity, not commercial
  readiness or profitability.
- No aircraft size, engine, fuel, material, route, operating procedure, or cost
  remedy is inferred.
- The economics gate remains **adverse historically and unresolved for future
  speed classes**. No practicality-matrix status changes follow.
