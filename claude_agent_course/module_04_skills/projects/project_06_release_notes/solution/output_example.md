Release:
- Version: 1.4.0
- Date: 2024-06-30

Added:
- Support exporting invoices to CSV
- New admin dashboard widgets

Changed:
- Default export now excludes cancelled invoices

Fixed:
- Pagination bug in invoices list
- Error when exporting empty dataset

Breaking changes:
- Removed legacy /v1/invoices endpoint

Notes:
- Migrate clients to /v2/invoices
