# OpenBet (OB) Risk Metrics

Structured data extracted from OpenBet (OB) for use in the CRS UI (Customer Risk Settings UI).

---

## 📊 Profits & Losses

### **Bet Count**

- **Definition**: Total number of bets placed by the customer.

### **Gross Stake**

- **Definition**: Total money wagered, regardless of outcome.

### **Settled Stake**

- **Definition**: Total stake from resolved bets (used in real P&L calculations).

### **Trading Revenue**

- **Formula**:  
  `Trading Revenue = Gross Stake - Payouts to Customer`
- **Interpretation**:
  - Positive = customer loss (platform gain)
  - Negative = customer profit (platform loss)

### **Trading Margin**

- **Formula**:  
  `Trading Margin = (Trading Revenue / Settled Stake) × 100`
- **Use**: Measures customer profitability for the platform.

---

## 📈 Other Metrics

### **Expected Margin**

- **Definition**: Theoretical platform edge based on expected outcomes (not actual results).
- **Use**: Identifies betting behavior in high/low-margin markets.

### **MikePrice Stake**

- **Definition**: Stake on events priced using internal MikePrice model.

### **MikePrice Exp Margin**

- **Definition**: Expected margin from MikePrice bets.
- **Use**: Gauges customer impact on internal markets.

### **BNN Shrewd Stake**

- **Definition**: Stake on bets flagged as "shrewd" by the BNN (Bet Neural Network) model.
- **Use**: High value may indicate a smart/professional bettor.

### **Average Stake**

- **Formula**:  
  `Average Stake = Gross Stake / Bet Count`
- **Use**: Measures bet sizing behavior.

### **Straight Stake**

- **Definition**: Stake on single-outcome bets (non-multis).

### **OddsBoost Stake**

- **Definition**: Stake on bets with promotional odds boosts.

---

## 🚦 Risk Indicators (Platform Perspective)

| Metric                   | Good (Safe)                             | Warning / Bad (Risk)          |
| ------------------------ | --------------------------------------- | ----------------------------- |
| **Trading Margin**       | 10–30%                                  | < 0% (customer is profitable) |
| **Expected Margin**      | > 5%                                    | < 2% or negative              |
| **BNN Shrewd Stake**     | < 5% of total stake                     | > 20% of total stake          |
| **OddsBoost Stake**      | < 10% of total stake                    | > 30% of total stake          |
| **MikePrice Exp Margin** | > 5%                                    | < 0%                          |
| **Average Stake**        | €1–€25 (recreational), up to €100 (VIP) | > €100 with low margin = risk |

---

> ⚠️ Use these metrics to classify customers by profitability and risk level for targeted actions in risk management and segmentation models.
