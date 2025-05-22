# OpenBet (OB) Feature Controls and System Behaviors

---

## 🔍 Bet Search

- Search tool for locating recent or historical bets.
- Filters:
  - **Search Criteria**
  - **Advanced Search**
- Use: Narrow down and display customer bet results.

---

## 🎚️ Stake Factor

- Each customer has a **stake multiplier**.
- Multiplies the **max allowable bet** per customer.
- Range: `0.01` to `999.99`.

---

## 📊 Stake Factor by Class

- Class-based stake scaling per customer.
- Example:
  - Football = `0.5` (lower limit)
  - Ice Hockey = `2.0` (higher limit)
- Use: Limit high-skill customers per sport to control risk.

---

## 📈 Cumulative Stakes

- Global setting (can be disabled).
- Controls **max customer stake per Selection** per time window (e.g., 24h).
- Includes stake factor in calculations.
- Use case: Multi-day events (e.g., golf).

---

## 🚦 Bet Intercept (BI)

- Manual review system for bets that **breach limits** (e.g., max stake or payout).
- Actions on flagged bets:
  - ✅ Accept
  - ❌ Decline
  - 🔁 Counter-offer (e.g., different stake or odds)
