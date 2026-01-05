Example:

> tables samples/sample.db
["orders"]

> query samples/sample.db "SELECT customer, amount FROM orders WHERE status='paid'"
[
  {"customer": "Alice", "amount": 120.5},
  {"customer": "Bob", "amount": 75.0},
  {"customer": "Dina", "amount": 50.0}
]

> agg samples/sample.db "SELECT status, COUNT(*) AS count, SUM(amount) AS total FROM orders GROUP BY status"
[
  {"status": "paid", "count": 3, "total": 245.5},
  {"status": "refunded", "count": 1, "total": 200.0}
]
