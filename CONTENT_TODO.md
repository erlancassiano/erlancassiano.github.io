# Content Erlan still needs to provide

The site ships with real facts from the existing CV/site text and clearly marked **TODO** / **PLACEHOLDER** slots. Do not invent numbers when filling these.

## Images (replace placeholders under `assets/img/placeholders/`)

- [ ] SATVHR public CAD / accommodation views (no confidential Visiona data)
- [ ] STM vibration / AIT photos from INPE/LIT (cleared)
- [ ] FEA / mode-shape or FRF figures cleared for public use
- [ ] VCUB1 assembly / flight-hardware photos (cleared)
- [ ] MGSE as-built photos (no confidential markings)
- [ ] MHD thesis figures / prototypes (when available)
- [ ] 3D-print gallery set
- [ ] Fox17 chimney / flange drawings or photos (cleared)
- [ ] UnB hybrid-rocket bench photos
- [ ] Optional portrait for About/Contact

## Case-study prose

- [ ] SATVHR: quantified public requirements, lessons learned, cleared plots
- [ ] VCUB1: extra public interface numbers; AIT photos
- [ ] MGSE: public load / FoS basis; supplier lessons
- [ ] MHD wheel: torque/momentum/mass/power targets once frozen; status
- [ ] Additive manufacturing: which projects are public + real measured fits
- [ ] Fox17: codes/standards and export context if publishable
- [ ] UnB bench: thrust/instrumentation details from 2013 if still accurate

## Calculations section (`/calculations/`)

- [ ] Mass-budget / CG notebook or PDF excerpt (non-confidential)
- [ ] Modal / sine teaching example or public FRF snippet
- [ ] Optional SGDC propellant-sensitivity plot if cleared
- [ ] Drop `.ipynb` or static HTML exports and link from the home section

## Resume / CV files

- [ ] Confirm the embedded PT-BR Mechanical Design PDF (`cv/Erlan-Cassiano_CV_Mechanical-Design-PT-BR_22ec.pdf`) is the preferred public version
- [ ] Optionally refresh EN-targeted PDFs already in `/cv/` so they match the new headline (Mechanical Design, not Space Systems; no “manage 4 junior engineers”; SATVHR below 300 kg)

## Copy polish

- [ ] Short personal tagline variants if you want a different hero sentence
- [ ] PT-BR full portfolio translation (currently `/pt/` is a short bridge page)
- [ ] Any awards/volunteer blurbs you want surfaced on the home page

## Featured flags

Each CV-like item uses `data-featured="true|false"` (projects also have `"featured"` in `scripts/projects.json`). Flip the attribute (and JSON for projects) to change what appears before **See more**.

| Section | Featured (`true`) | Collapsed (`false`) |
|---|---|---|
| Work timeline | Visiona (both roles), Fox17, Thales Alenia Space | RuaDois, Funcate, CIV, SET-G/CNPq/AEB/INPE, Autotrac |
| Education timeline | ITA M.Sc., UnB bachelor’s | Certifications & courses summary, MBA |
| Certifications | TSTI, SENAI CNC, Creo (Mult-e), ATI | SENAI CAM, Awari Data Science, HubSpot |
| Publications | IAC 2024 (VCUB1 TVAC) | Bertoldi 2016, UnB 2013, COBEF 2013, P&D Design 2012 |
| Projects | SATVHR, SGDC, VCUB1 | MGSE, MHD wheel, AM, Fox17 chimneys, UnB hybrid |
| Media | All current SGDC / SATVHR / VCUB1 items | _(none yet)_ |
| Skills groups | All groups | _(none)_ |
| Languages | Portuguese, English, French | _(none)_ |
| Calculations | Propellant load sensitivity (SGDC) | Mass budget, modal/sine, Python notebooks (TODO slots) |
| Gallery | First two placeholders | Remaining placeholders |
| Hero stats | All four headline numbers | _(none)_ |
| Contact | Direct card, Profile card, and all Direct details | _(none)_ |
| Resume “Also available” | Mechanical Design (EN), Currículo PT-BR | Mechanical Structures, Thermal & AIT, Space Systems |
| Case-study results grids | All result cells (where present) | _(none)_ |

## Certifications / LinkedIn gaps

Public LinkedIn profile HTML was not reliably fetchable (direct page errors); Certifications & Courses were filled from CV PDFs in `/cv/` plus indexed public LinkedIn Licenses & Certifications / Courses content. Confirm or supply:

- [ ] Year for **CAM programming (SENAI)** — listed on CV next to the 2024 CNC course and on LinkedIn Courses without a year
- [ ] Credential / certificate links for TSTI, SENAI, Mult-e, ATI, and Awari (only HubSpot had a public credential URL)
- [ ] Whether **Data Science (Awari)** and **Service Hub Software (HubSpot, expired)** should stay on the mechanical portfolio page
- [ ] Any additional Licenses & Certifications on LinkedIn not captured in the index (CSM / leadership items intentionally omitted; no PMP or Green Belt found)
- [ ] Optional: CATIA V5 (academic) under CAD if you want it listed (mentioned in LinkedIn reverse-engineering work; not added by default)

## Hard rules already applied on the site

- Headline focus: **Spacecraft Mechanical Design Engineer**
- No “manage / lead a team of N juniors” wording
- SATVHR: **below 300 kg** (never 500 kg)
- SGDC: **more than 16 kg** propellant, **~2.5 months**, **~R$ 36M**
- Jitter: **precision better than 0.1 µm**
- MGSE: **led the concept** (detailed & built by subcontractor)
- SATVHR **TVAC not yet done**
- **No confidential Visiona/Thales data**
