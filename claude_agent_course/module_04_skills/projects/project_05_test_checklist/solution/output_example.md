Unit tests:
- Validate main account selection rules
- Reject merge when accounts are identical
- Ensure merged profile fields are preserved

Integration tests:
- POST /accounts/merge merges data into primary account
- Secondary account is disabled after merge
- Login is blocked during merge window

Regression tests:
- Existing login flow unaffected for non-merge users
- Account data reads still work after merge

Negative tests:
- Merge fails if primary account is inactive
- Merge fails if secondary account missing
