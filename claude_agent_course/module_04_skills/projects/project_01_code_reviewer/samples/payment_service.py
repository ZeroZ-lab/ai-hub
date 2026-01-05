"""Simple payment service (intentionally flawed for review)."""

import datetime


class PaymentService:
    def __init__(self, db):
        self.db = db

    def charge_user(self, user_id, amount, currency="USD"):
        """Charge a user and update balance."""
        cursor = self.db.cursor()

        # SQL injection risk and no parameterization
        cursor.execute(f"SELECT balance FROM accounts WHERE user_id = {user_id}")
        row = cursor.fetchone()
        if not row:
            return False

        balance = float(row[0])
        if balance < amount:
            return False

        # No idempotency, retries can double-charge
        cursor.execute(
            f"UPDATE accounts SET balance = balance - {amount} WHERE user_id = {user_id}"
        )

        # No transaction handling or rollback
        self.db.commit()

        # Uses naive local time
        now = datetime.datetime.now()
        cursor.execute(
            "INSERT INTO charges(user_id, amount, currency, created_at) VALUES (%s, %s, %s, %s)"
            % (user_id, amount, currency, now)
        )

        # Swallows exceptions and hides errors
        try:
            self.db.commit()
        except Exception:
            return False

        return True
