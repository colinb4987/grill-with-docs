# A worked session

A complete but small session, to show the machine in motion. The plan:
the user runs a profitable coffee shop and wants to open a second site.
Supplied documents:

- `Business plan v2.docx` (the user's one-pager)
- `Lease offer - High Street.pdf` (the landlord's terms)
- `Loan term sheet - Meridian Bank.pdf`

## Round 0 — inventory and tree

**Documents:** all three read. Dates: plan undated (assumed current);
lease offer dated 2026-08-01, expiry 2026-09-01; term sheet dated
2026-07-15, no expiry stated (flagged: *assumed* current).

**Tree.** The outcome "second site open by the planned date" branches:

- D1 — Which site? (settled: High Street, per plan)
- D2 — Can we sign this lease? (depends on D1)
- D3 — Can we fund the fit-out? (depends on D2, D4)
- D4 — What does the fit-out actually cost? (no dependencies)
- D5 — When can it open? (depends on D2, D3)

Frontier: **D2, D4** (D3 and D5 wait on D4).

## Round 1

    ❓ **Q1 — Can we sign this lease? (D2):** The offer expires
       2026-09-01 (Lease offer, p. 1) and gives 14 days to respond.
       The plan names no decision date for the lease.
       ➡️ **Recommendation:** Treat the lease deadline as the binding
       constraint and work backwards from it; decide on terms before
       the expiry, not the fit-out budget first.

    ❓ **Q2 — What does the fit-out actually cost? (D4):** Your plan
       (Business plan v2, p. 2) says "fit-out est. £45k". The term
       sheet (p. 3) will lend up to £60k *against approved quotes*.
       ➡️ **Recommendation:** Get three quotes before any signature;
       until then £45k is a tier-4 assumption, not a number. (I
       cannot establish a fit-out cost from these documents — that is
       a fact only you can supply; I will mark D4 *blocked on
       unknown* until then.)

    ❓ **Q3 — The disbursement conflict (D3):** The term sheet
       (p. 4) disburses in **two tranches: 50% at drawdown, 50% on
       completion certificate**. The plan (p. 2) assumes the full
       £60k "available at opening". A completion certificate normally
       follows a building-control sign-off, i.e. *after* the
       fit-out — so the second half may arrive only after most of the
       spend.
       ➡️ **Recommendation:** Do not assume availability at opening.
       Two options: (a) negotiate a completion definition that
       triggers the second tranche on practical completion of fit-out,
       or (b) hold a cash buffer of at least the second tranche from
       existing profits. I recommend (a) with (b) as fallback.

## Round 2 — after the user's answers

The user answers Q1 "yes, we can sign by August", Q2 "I'll get
quotes", and **challenges Q3**: "The bank said verbally that the
second tranche is automatic."

    ❓ **Q4 — Is the verbal assurance good enough? (D3, re-derived):**
       The written term sheet says "completion certificate" — the
       verbal "automatic" is a tier-4 claim with no document behind
       it. A tier-4 claim cannot overturn a tier-2 written term.
       ➡️ **Recommendation:** Ask Meridian to confirm the disbursement
       trigger in writing (an email suffices). If they confirm a
       different trigger than their own term sheet, the written
       change supersedes it; until then, plan on the certificate.

    ❓ **Q5 — Opening date (D5, now unblocked):** With the lease
       expiry 2026-09-01 and a typical 8–10 week fit-out, an opening
       before late November is only achievable if the lease is signed
       by mid-August *and* quotes arrive within two weeks.
       ➡️ **Recommendation:** Set the internal deadline: signed lease
       by 2026-08-14, quotes by 2026-08-28. Anything later pushes
       opening into January — which is fine *if it is a decision*,
       but the plan currently presents the November date as a fact.

## Synthesis

- **Settled:** D1 (site), D2 (sign before expiry; internal date
  2026-08-14), D3 (disbursement risk real; written confirmation
  required), D5 (target depends on the two internal deadlines;
  January is the fallback, to be chosen consciously).
- **Unresolved risk:** D4 — fit-out cost is a tier-4 assumption until
  quotes arrive; every downstream number (buffer size, loan drawdown)
  moves with it.
- **Explicit assumptions:** term sheet is still current (no expiry
  stated — verify); plan is the latest version.
- **Rejected alternative:** "Rely on the bank's verbal assurance" —
  rejected on evidence grounds (tier-4 vs tier-2).
- **Evidence base:** Lease offer p. 1 (expiry), p. 6 (response period);
  term sheet p. 3–4 (limits, tranches); plan p. 2 (cost, opening date).
- **Resulting plan:** Sign lease by 2026-08-14 → quotes by 2026-08-28
  → written confirmation of the disbursement trigger from Meridian →
  drawdown, fit-out, target opening 2026-11; fallback opening 2027-01
  if either internal deadline slips.

*The facilitator stops here and waits for the user to confirm shared
understanding.*
