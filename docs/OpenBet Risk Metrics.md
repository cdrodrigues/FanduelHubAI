## OpenBet (OB) Risk Metrics

Here are the data that can be extracted from Openbet (OB) and visualised in the CRS UI (Customer Risk Settings UI)

***Profits & Losses***

*Bet Count*

The total number of bets a customer has placed.

*Gross Stake*

The total amount of money wagered by the customer, regardless of bet outcome.

*Settled Stake*

The total amount staked on bets that have been resolved (i.e., not pending). Only settled bets can be used to calculate real profit/loss.

*Trading Revenue*

The net revenue earned from a customer.

Trading Revenue = Gross Stake - Payouts to Customer

A positive number = customer loss (platform gain), negative = customer profit (platform loss).

*Trading Margin*

The percentage of revenue retained from the settled stake.

Formula:
Trading Margin = (Trading Revenue / Settled Stake) × 100

Indicates profitability of a customer from the platform's perspective.

---

***Other Metrics***

*Expected Margin*

The theoretical or statistical edge the platform has on the bets placed by a customer, based on expected outcomes (not actual results).

Helps identify if a bettor consistently bets on high-margin or low-margin events.



*MikePrice Stake*

The total stake placed on events where MikePrice odds (a type of model or internal pricing system) were available or used.

*MikePrice Exp Margin*

Expected margin on the MikePrice bets.

Reflects how valuable or risky a customer is when betting on internally priced markets.

*BNN Shrewd Stake*

The total stake placed on bets identified by a BNN (Bet Neural Network) model as "shrewd" or sharp (i.e., potentially profitable for the customer and risky for the book).

A high value might signal a smart or professional bettor.

*Average Stake*

The average size of the customer's bets.

Formula:
Average Stake = Gross Stake / Bet Count

*Straight Stake*

Total stake on straight bets (i.e., single bets on one outcome, not parlays or multis).

*OddsBoost Stake*

Total stake on bets that were placed with an odds boost promotion (i.e., artificially inflated odds to attract betting activity).

---

***Profitable or Risky from the sportsbook's perspective***

*Trading Margin*

Good (Safe):	10–30%

Warning / Bad (Risk): < 0% (customer is profitable)

*Expected Margin*

Good (Safe): 	> 5%

Warning / Bad (Risk): < 2% or negative

*BNN Shrewd Stake*

Good (Safe): 	< 5% of total stake

Warning / Bad (Risk): > 20% of total stake

*OddsBoost Stake*

Good (Safe): 	< 10% of total stake

Warning / Bad (Risk): > 30% of total stake

*MikePrice Exp Margin*|

Good (Safe): 	> 5%

Warning / Bad (Risk): < 0%

*Average Stake*

Good (Safe): €1–€25 (recs), up to €100 (VIP)

Warning / Bad (Risk): > €100 (with low margin = risk)


