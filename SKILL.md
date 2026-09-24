---
name: upwork-catalog-builder
description: Build a complete, paste-ready Upwork Project Catalog listing from one prompt, covering every step of Upwork's create-project form (overview, pricing tiers, service tier options, add-ons, gallery, requirements, description, steps, FAQs, finalize) with all character limits already checked. Use this whenever the user wants to create, draft, fill in, or improve an Upwork Project Catalog offer, catalog project, fixed-price service listing, or "You will get..." project, for any service such as malware removal, WordPress migration, website maintenance, server setup, speed optimization, or email deliverability, even if they only say "make my next catalog offer" or "create a project for X".
---

# Upwork Project Catalog Builder

Turns one short request (for example "create a catalog project for WordPress migration") into a finished listing the user can paste into Upwork field by field. Upwork has no API for catalog listings, so the output is a paste-ready package, not an automated submission.

## Before writing

1. Read `references/proof-bank.md` for the user's verified proof points, pricing context, and writing rules. Only use proof from that file or from facts the user gives in the prompt. Never invent numbers, clients, or results.
2. Read `references/upwork-form-rules.md` for every field limit and the lessons learned from building the first listing.
3. If the service is malware removal, read `references/example-malware-offer.md` and reuse it as the template. For any other service, use it as the quality and structure benchmark.
4. If the prompt is missing something essential (the service, or a price range the user wants), make a sensible assumption from the proof bank, state it in one line at the top, and continue. Do not stall with questions.

## Output structure

Produce these sections in this order, matching the order of Upwork's form so the user can work top to bottom:

1. **Overview**: title (starts with "You will get"), suggested category, website specialization and plugin guidance, 5 search tags.
2. **Pricing**: three tiers (Starter, Standard, Advanced) with custom title, custom description, price, delivery days, revisions.
3. **Service tier options**: a table marking which options each tier includes.
4. **Add-ons**: which to tick, prices, and one custom add-on with its description.
5. **Gallery**: which images to use, whether to add a video, and a sample document plan (with a ready prompt the user can send to Claude Code to generate an anonymized sample PDF from a real job).
6. **Requirements**: one main requirement (max 250 characters) plus a short separate website URL question.
7. **Description**: project summary (120 to 1,200 characters), 5 project steps, 5 FAQs.
8. **Finalize**: recommended maximum simultaneous projects, with the reason.
9. **Pre-submit checklist**.

Show the character count in brackets after every field that has a limit, for example "(74/80)".

## Checking limits

Always verify lengths before presenting. Put the drafted fields into a JSON file and run:

```bash
python scripts/check_limits.py fields.json
```

The script reports each field's length against its limit. Fix anything over the limit before showing the user. Never guess a character count.

## Quality rules

- Proof must be specific and verifiable. One strong real case beats several vague claims.
- Keep claims consistent with the user's portfolio and any sample report. If the report only proves "clean after cleanup", do not write "stayed clean since".
- No guarantees about outcomes a third party controls (inbox placement, Google review timing, never being hacked again). Say what the user controls instead.
- Tier-defining features (the things that separate Starter from Standard) must never be sold as add-ons, or buyers skip the higher tier.
- Every add-on gets a real price. Never leave $0 add-ons ticked.
- Gallery images: no Upwork logos or badges, no third-party brand names or logos, no visible client domains or IPs, not text-heavy.
- Follow the writing rules in the proof bank (no em dashes, plain English, calm and competent tone).

## After the listing

End with one line suggesting the next catalog offer from the planned list in the proof bank, so the catalog grows one offer at a time.
