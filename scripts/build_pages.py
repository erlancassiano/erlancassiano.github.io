#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate case-study HTML pages from project data. Run from repo root."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "projects"

NAV = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Erlan Cassiano</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://erlancassiano.github.io/projects/{slug}/">
<link rel="icon" href="/favicon.png" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=Syne:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" integrity="sha384-nB0miv6/jRmo5UMMR1wu3Gz6NLtoTAtOmEupStiWXk1gV3" crossorigin="anonymous">
<link rel="stylesheet" href="/assets/css/site.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" integrity="sha384-nB0miv6/jRmo5UMMR1wu3Gz6NLtoTAtOmEupStiWXk1gV3" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" integrity="sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzw=" crossorigin="anonymous"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:false}});"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="/">Erlan Cassiano <span>Mech · Space</span></a>
    <button class="icon-btn menu-toggle" type="button" data-menu-toggle aria-expanded="false" aria-controls="nav-links" aria-label="Open menu">?</button>
    <ul class="nav-links" id="nav-links" data-nav-links>
      <li><a href="/#projects">Projects</a></li>
      <li><a href="/#timeline">Timeline</a></li>
      <li><a href="/#calculations">Calculations</a></li>
      <li><a href="/#gallery">Gallery</a></li>
      <li><a href="/#publications">Publications</a></li>
      <li><a href="/resume.html" aria-current="false">Resume</a></li>
      <li><a href="/#contact">Contact</a></li>
    </ul>
    <div class="nav-actions">
      <button class="icon-btn" type="button" data-theme-toggle aria-pressed="false" title="Toggle theme">DK</button>
    </div>
  </div>
</header>
"""

FOOTER = """
<footer class="site-footer">
  <div class="wrap">
    <p>© <span data-year></span> Erlan Cassiano · Spacecraft Mechanical Design</p>
    <p><a href="/#projects">Projects</a> · <a href="/resume.html">Resume</a> · <a href="https://www.linkedin.com/in/erlancassiano">LinkedIn</a></p>
  </div>
</footer>
<script src="/assets/js/site.js"></script>
</body>
</html>
"""

# KaTeX CDN integrity hashes above may be wrong - I'll fix with known good URLs without integrity or correct ones
# Better: use jsdelivr without integrity for simplicity in generated files - I'll fix in the template below

PROJECTS = [
    {
        "slug": "satvhr-stm",
        "title": "SATVHR mechanical architecture & STM vibration qualification",
        "meta": "Visiona · LEO Earth observation · Phase B/C · 2023present",
        "tags": ["CAD", "FEA", "Thermal", "Test", "Calculations"],
        "image": "/assets/img/satvhr/satvhr-card.jpg",
        "summary": "Mechanical and thermal architecture of a below-300 kg LEO Earth-observation satellite, including STM vibration qualification at INPE/LIT (May 2026).",
        "context": """
<p>SATVHR is a below-300 kg, 5-year-life LEO Earth-observation satellite in phase B/C. As Mechanical Architect, I own the mechanical and thermal architecture: Creo layouts, payload accommodation, sandwich-panel structure, mass budget, and interface control documents (ICDs).</p>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-02-visiona.jpg" alt="SatVHR Structural Thermal Model standing in an integration hall with solar-array panels and copper MLI, observed by engineers in blue cleanroom smocks at INPE/LIT" width="1024" height="624" loading="lazy">
  <figcaption>
    <span class="figure-cap">SatVHR Structural Thermal Model (STM) in the integration hall — solar-array faces and copper MLI visible — with the AIT team looking on.</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Mechanical configuration that accommodates the payload within a below-300 kg system mass budget.</li>
  <li>Sandwich-panel primary structure sized for launch environments (flight: CFRP faces; STM: aluminium faces on aluminium honeycomb).</li>
  <li>GD&amp;T and tolerance stack-up per ISO GPS on mechanical drawings.</li>
  <li>Structuralthermal model (STM) vibration qualification correlated with the FEM.</li>
</ul>
<p class="todo"><strong>TODO</strong> - Erlan: paste quantified requirements that are cleared for public release (loads, margins policy, etc.).</p>
""",
        "approach": """
<p>Layouts and accommodation were driven in Creo. Structural work used Femap/Nastran models for design reviews and troubleshooting; thermal architecture used Thermal Desktop/SINDA. Margin reports documented the structural and thermal posture ahead of system reviews (PRR, PDR), with system / structure / thermal CDRs targeted for end of 2026.</p>
<div class="math-block">
<p>Illustrative modal check (placeholder - replace with cleared formula):</p>
$$\\omega_n = \\sqrt{\\frac{k}{m}}$$
<p>where $k$ is an effective stiffness and $m$ a modal mass. <span class="todo" style="display:inline;border:none;padding:0;background:none"><strong>TODO</strong>: Erlan to supply the actual relation used in the public write-up.</span></p>
</div>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-01-visiona.jpg" alt="Close-up of the SatVHR STM showing copper multi-layer insulation and a large black cylindrical optical baffle on a grey mounting plate" width="1024" height="624" loading="lazy">
  <figcaption>
    <span class="figure-cap">Close-up of the SatVHR STM: copper MLI blankets and the black cylindrical optical baffle on the payload interface plate.</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid">
  <div><strong>&lt; 300 kg</strong><span>System mass class</span></div>
  <div><strong>May 2026</strong><span>STM vib. qual. passed</span></div>
  <div><strong>&lt; 0.1 µm</strong><span>Jitter measurement precision</span></div>
</div>
<p>STM vibration qualification (sine, random, and sine burst) passed at INPE/LIT in May 2026 and was correlated with the FEM. Jitter on the STM (main telescope mirror displacement under reaction-wheel imbalance) was measured with precision better than 0.1 µm.</p>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-03-visiona.jpg" alt="Eight engineers in light-blue cleanroom smocks posing beside SatVHR solar-array and STM hardware in a high-bay integration facility" width="1024" height="624" loading="lazy">
  <figcaption>
    <span class="figure-cap">AIT team with SatVHR hardware in the integration facility — solar-array panel (left) and STM hardware (right).</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
<p class="todo"><strong>TODO</strong> - Erlan: add cleared FRF / mode-shape plots and any public numeric margins.</p>
""",
        "mfg_test": """
<p>STM AIT and vibration campaign at INPE/LIT. Thermal-vacuum (TVAC) campaign for SATVHR: <strong>not yet done</strong>.</p>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-pr-2026-05-13.jpg" alt="Engineers in white lab coats inspecting the SatVHR STM on a metal stand, with copper MLI and a black optical baffle, consulting a laptop in a cleanroom" width="1280" height="878" loading="lazy">
  <figcaption>
    <span class="figure-cap">Engineers inspecting the SatVHR STM on its ground stand during the AIT campaign — copper MLI and optical baffle in view.</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
""",
        "lessons": """
<p class="todo"><strong>TODO</strong> - Erlan: 24 lessons learned cleared for publication (configuration trades, correlation practices, MGSE interfaces, etc.).</p>
""",
        "tools": ["Creo Parametric", "Femap/Nastran", "Thermal Desktop/SINDA", "GD&T / ISO GPS", "MATLAB", "Python"],
    },
    {
        "slug": 'sgdc-propulsion',
        "title": 'SGDC propulsion technology transfer',
        "meta": 'Thales Alenia Space · Cannes · AEB programme · 2014–2016',
        "tags": ['Calculations', 'Test', 'CAD'],
        "image": '/assets/img/sgdc/sgdc-card.jpg',
        "summary": 'On-the-job training on Brazil’s SGDC bipropellant propulsion subsystem; showed that more than 16 kg of additional propellant could be loaded, giving ~2.5 months of life and ~R$ 36M.',
        "context": """
<p>Selected by the Brazilian Space Agency (AEB) for the SGDC Technology Absorption Programme at Thales Alenia Space in Cannes: about 5,500 h of full-time on-the-job training on the SGDC bipropellant propulsion subsystem (tanks, valves, lines, interfaces), from requirements and design through production, procedures, testing and operation.</p>
<figure class="case-figure">
  <img src="/assets/img/sgdc/sgdc-satellite-completed.jpg" alt="Fully assembled SGDC satellite in a cleanroom, with a large circular antenna, stowed solar arrays, and gold and black thermal blankets; Thales Alenia Space balloons in the background" width="1169" height="780" loading="lazy">
  <figcaption>
    <span class="figure-cap">SGDC (SGDC-1) fully assembled in the cleanroom — circular antenna, stowed solar arrays, and MLI blankets visible.</span>
    <span class="figure-credit"><a href="https://visionaespacial.com/imprensa/" rel="noopener noreferrer">© Visiona Tecnologia Espacial</a></span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Understand and follow the bipropellant propulsion lifecycle under ECSS-driven V&amp;V as a trainee on SGDC.</li>
  <li>Assess propulsion performance over life (pressure, thrusters, temperature, propellant gauging), including tank deformation under pressurisation where relevant to loading.</li>
</ul>
<p class="todo"><strong>TODO</strong> - Erlan: any additional public requirements or scope notes cleared for this case study.</p>
""",
        "approach": """
<p>Worked across the bipropellant propulsion lifecycle with Thales engineers. Showed that more than 16 kg of additional propellant could be loaded on SGDC when accounting for tank deformation under pressurisation.</p>
<figure class="case-figure">
  <img src="/assets/img/sgdc/sgdc-service-module.jpg" alt="Dark cylindrical SGDC service-module primary structure on a white assembly stand, inspected by two technicians in Thales Alenia Space cleanroom coats" width="1170" height="780" loading="lazy">
  <figcaption>
    <span class="figure-cap">SGDC service-module central structure on the assembly stand during integration at Thales Alenia Space.</span>
    <span class="figure-credit"><a href="https://visionaespacial.com/imprensa/" rel="noopener noreferrer">© Visiona Tecnologia Espacial</a></span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/sgdc/sgdc-payload-module.jpg" alt="SGDC payload module open in a silver integration frame, showing dense wiring harnesses and electronics panels before closure" width="1170" height="780" loading="lazy">
  <figcaption>
    <span class="figure-cap">SGDC payload module in its integration frame — internal electronics and harnesses before panel closure.</span>
    <span class="figure-credit"><a href="https://visionaespacial.com/imprensa/" rel="noopener noreferrer">© Visiona Tecnologia Espacial</a></span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid">
  <div><strong>&gt; 16 kg</strong><span>Additional propellant</span></div>
  <div><strong>~2.5 months</strong><span>Extra service life</span></div>
  <div><strong>~R$ 36M</strong><span>Life-extension value shown</span></div>
</div>
<p>AEB later recognised the propellant-loading method that extends SGDC lifetime (Mar 2017). Witnessed SGDC propulsion-related tests in Cannes as a trainee.</p>
<figure class="case-figure">
  <img src="/assets/img/sgdc/sgdc-solar-panel-deployment.jpg" alt="SGDC solar-array wing fully extended across a white cleanroom, attached to the satellite body covered in silver and gold MLI" width="1169" height="780" loading="lazy">
  <figcaption>
    <span class="figure-cap">SGDC solar-array wing fully deployed during ground testing in the cleanroom.</span>
    <span class="figure-credit"><a href="https://visionaespacial.com/imprensa/" rel="noopener noreferrer">© Visiona Tecnologia Espacial</a></span>
  </figcaption>
</figure>
""",
        "mfg_test": """
<p>Press photographs below are from Visiona’s public SGDC assembly, integration and test gallery (Thales Alenia Space facilities). Propulsion tests were witnessed in Cannes during the technology-transfer programme.</p>
<p class="todo"><strong>TODO</strong> - Erlan: optional cleared notes on which propulsion tests were witnessed (no confidential data).</p>
""",
        "lessons": """
<p class="todo"><strong>TODO</strong> - Erlan: 2–3 public lessons from the SGDC propulsion transfer (gauging, tank deformation, V&amp;V practices).</p>
""",
        "tools": ['Propulsion subsystem V&amp;V', 'ECSS (tailored)', 'Propellant gauging / loading analysis'],
    },
    {
        "slug": "vcub1-assembly",
        "title": "VCUB1 final flight assembly",
        "meta": "Visiona · 12 kg CubeSat · Falcon 9 Transporter-7 · 2023",
        "tags": ["CAD", "Test", "Additive Manufacturing"],
        "image": "/assets/img/vcub1/vcub1-card.jpg",
        "summary": "Final flight assembly of the 12 kg VCUB1 CubeSat, including delta vibration and solar-panel deployment checks ahead of Falcon 9 launch.",
        "context": """
<p>VCUB1 is a 12 kg CubeSat that was launched on Falcon 9 (SpaceX Transporter-7, April 2023) and operated in orbit. In early 2023 I supported final integration and performed the final flight assembly.</p>
""",
        "requirements": """
<ul>
  <li>Complete flight assembly with controlled procedures for solar panels and deployer interfaces.</li>
  <li>Delta vibration and solar-panel deployment verification before launch.</li>
  <li>6U deployer-rail fit-check and integration tooling readiness for Falcon 9.</li>
</ul>
<p class="todo"><strong>TODO</strong> - Erlan: add any public mass / volume / interface numbers cleared for this page.</p>
""",
        "approach": """
<p>Revised the solar-panel assembly procedure, ran delta vibration and deployment tests, executed the 6U deployer-rail fit-check, reviewed qualification test data, and prepared integration tooling for launch.</p>

<figure class="case-figure">
  <img src="/assets/img/vcub1/vcub1-nanosats.jpg" alt="VCUB1 CubeSat with two solar-panel wings fully deployed, resting on a white stand in a laboratory" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">VCUB1 with solar panels deployed on a laboratory stand — central bus with a circular antenna/sensor aperture and body-mounted cells between the wings.</span>
    <span class="figure-credit"><a href="https://www.nanosats.eu/sat/vcub1" rel="noopener noreferrer">Image: nanosats.eu</a></span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid">
  <div><strong>12 kg</strong><span>CubeSat mass</span></div>
  <div><strong>Apr 2023</strong><span>Transporter-7 launch</span></div>
  <div><strong>IAC 2024</strong><span>TVAC campaign paper</span></div>
</div>
<p>Satellite operated in orbit after launch. Co-authored the IAC 2024 paper on the VCUB1 thermal-vacuum test campaign (IAC-24-B4.IP.21).</p>
""",
        "mfg_test": """
<p>Delta vibration, solar-panel deployment, deployer fit-check, and the TVAC campaign documented in the IAC 2024 paper. No confidential Visiona/Thales datasets are shown here.</p>
""",
        "lessons": """
<p class="todo"><strong>TODO</strong> - Erlan: procedure and fit-check lessons suitable for a public case study.</p>
""",
        "tools": ["SolidWorks / Onshape", "Assembly procedures", "AIT tooling"],
    },
    {
        "slug": "mgse-lifting",
        "title": "Lifting & handling MGSE  concept",
        "meta": "Visiona · SATVHR STM AIT · concept lead",
        "tags": ["CAD", "Test", "Calculations"],
        "image": "/assets/img/placeholders/structure.png",
        "summary": "Led the concept for the lifting and handling MGSE; detailed design and build by a subcontracted supplier; tested during the STM AIT campaign.",
        "context": """
<p>Ground support equipment was required to lift and handle the SATVHR STM safely during AIT and vibration preparation at INPE/LIT.</p>
""",
        "requirements": """
<ul>
  <li>Safe lift / handle interfaces compatible with the STM mechanical architecture.</li>
  <li>Supplier-deliverable detailed design and manufacture from a clear concept package.</li>
  <li>Verification during the STM AIT campaign.</li>
</ul>
<p class="todo"><strong>TODO</strong> - Erlan: public load / factor-of-safety requirements if cleared.</p>
""",
        "approach": """
<p>I <strong>led the concept</strong>; detailed design and manufacturing were executed by a subcontracted supplier. Concept work covered lift points, handling envelopes, and interface definition against the STM configuration.</p>
<div class="math-block">
<p>Illustrative static lift check (placeholder):</p>
$$F = n \\, mg$$
<p>with proof factor $n$ per the applicable MGSE standard. <strong>TODO</strong>: Erlan to replace with the cleared sizing relation.</p>
</div>
<figure class="case-figure">
  <img src="/assets/img/placeholders/cad-panel.png" alt="Placeholder MGSE concept CAD" width="960" height="600">
  <figcaption>PLACEHOLDER  MGSE concept CAD</figcaption>
</figure>
""",
        "results": """
<p>MGSE was manufactured by the supplier and tested during the STM AIT campaign.</p>
<p class="todo"><strong>TODO</strong> - Erlan: add cleared photos of the as-built MGSE in use (no confidential markings).</p>
""",
        "mfg_test": """
<p>Detailed and built by a subcontractor; functional/handling checks during STM AIT. TVAC for the satellite: not yet done (separate from MGSE).</p>
""",
        "lessons": """
<p class="todo"><strong>TODO</strong> - Erlan: supplier-follow-up and concept-to-build interface lessons.</p>
""",
        "tools": ["Creo Parametric", "ICD definition", "Supplier follow-up"],
    },
    {
        "slug": "mhd-reaction-wheel",
        "title": "MHD magnetic-fluid reaction wheel",
        "meta": "ITA M.Sc. thesis · in progress · 20252027",
        "tags": ["CAD", "Calculations", "Test", "Additive Manufacturing"],
        "image": "/assets/img/placeholders/cad-panel.png",
        "summary": "M.Sc. thesis at ITA: development of a magnetohydrodynamic (MHD) magnetic-fluid reaction wheel for CubeSat attitude control.",
        "context": """
<p>Masters research at Instituto Tecnológico de Aeronáutica (ITA), programme EAM-1  Aeronautical Design, Structures, and Aerospace Systems. Advisor: Prof. Tiago de Paula. Expected completion July 2027.</p>
""",
        "requirements": """
<ul>
  <li>Reaction-wheel function using a magnetic fluid under MHD actuation, sized for CubeSat attitude control.</li>
  <li class="todo"><strong>TODO</strong> - Erlan: torque, momentum, mass, and power targets once frozen for public release.</li>
</ul>
""",
        "approach": """
<p class="todo"><strong>TODO</strong> - Erlan: describe modelling approach (MHD equations, FEM/CFD, prototypes) with only cleared content.</p>
<div class="math-block">
<p>Representative MHD body force (placeholder form):</p>
$$\\mathbf{f} = \\mathbf{J} \\times \\mathbf{B}$$
<p><strong>TODO</strong>: Erlan to confirm the formulation used in the thesis public summary.</p>
</div>
""",
        "results": """
<p class="todo"><strong>TODO</strong> - Erlan: status, prototypes, and any measured numbers cleared for the site. Do not invent performance figures.</p>
""",
        "mfg_test": """
<p class="todo"><strong>TODO</strong> - Erlan: prototype manufacturing (incl. AM if used) and lab test plan/status.</p>
""",
        "lessons": """
<p class="todo"><strong>TODO</strong> - Erlan: research lessons so far.</p>
""",
        "tools": ["Creo / CAD", "MATLAB", "Python", "Lab instrumentation"],
    },
    {
        "slug": "additive-manufacturing",
        "title": "3D printing projects",
        "meta": "Personal / supporting hardware · AM",
        "tags": ["Additive Manufacturing", "CAD", "Test"],
        "image": "/assets/img/placeholders/print-am.png",
        "summary": "Additive manufacturing work for fixtures, prototypes, and supporting hardware. Content to be filled with cleared examples.",
        "context": """
<p class="todo"><strong>TODO</strong> - Erlan: introduce which print projects are public (fixtures, education, personal prototypes). No confidential flight hardware data.</p>
""",
        "requirements": """
<p class="todo"><strong>TODO</strong> - Erlan: requirements per selected print (tolerance, material, load).</p>
""",
        "approach": """
<p>Practical CNC / CAM background (SENAI aerospace machining course, 120 h) complements FDM/AM prototyping for ground support and concept hardware.</p>
<figure class="case-figure">
  <img src="/assets/img/placeholders/print-am.png" alt="Placeholder 3D printed part" width="960" height="600">
  <figcaption>PLACEHOLDER  printed part gallery item</figcaption>
</figure>
""",
        "results": """
<p class="todo"><strong>TODO</strong> - Erlan: outcomes with real numbers only (print time, mass, measured fit).</p>
""",
        "mfg_test": """
<p class="todo"><strong>TODO</strong> - Erlan: process (FDM/SLA/etc.), post-processing, and fit checks.</p>
""",
        "lessons": """
<p class="todo"><strong>TODO</strong> - Erlan: design-for-AM lessons.</p>
""",
        "tools": ["Onshape / SolidWorks / Creo", "FDM (TBD)", "CAM / CNC"],
    },
    {
        "slug": "fox17-chimneys",
        "title": "Fox17  80 t chimneys & flanges",
        "meta": "Fox17 · industrial structures · export · 20152023",
        "tags": ["CAD", "Calculations", "FEA"],
        "image": "/assets/img/placeholders/structure.png",
        "summary": "As co-founder & CTO of Fox17, designed 80 t, 100 m+ steel chimneys and their flanges for export (cement-plant filters and separators).",
        "context": """
<p>Fox17 designed filters and separators for cement plants. Structural design responsibility included large steel chimneys and flange interfaces for export projects.</p>
""",
        "requirements": """
<ul>
  <li>Steel chimneys on the order of 80 t and 100 m+ height, with exportable flange detailing.</li>
  <li class="todo"><strong>TODO</strong> - Erlan: codes/standards and wind/seismic load basis if publishable.</li>
</ul>
""",
        "approach": """
<p>Mechanical design and detailing of chimney shells and flanges for fabrication and export. Supporting analyses as required by the project.</p>
<figure class="case-figure">
  <img src="/assets/img/placeholders/structure.png" alt="Placeholder chimney structure" width="960" height="600">
  <figcaption>PLACEHOLDER  chimney / flange drawing or photo</figcaption>
</figure>
""",
        "results": """
<div class="results-grid">
  <div><strong>80 t</strong><span>Chimney class</span></div>
  <div><strong>100 m+</strong><span>Height class</span></div>
</div>
<p class="todo"><strong>TODO</strong> - Erlan: export destinations / project names only if cleared; no invented performance claims.</p>
""",
        "mfg_test": """
<p class="todo"><strong>TODO</strong> - Erlan: fabrication partners and inspection approach (public).</p>
""",
        "lessons": """
<p class="todo"><strong>TODO</strong> - Erlan: large-structure detailing lessons transferable to space MGSE / ground equipment.</p>
""",
        "tools": ["SolidWorks", "Structural calculations", "Fabrication drawings"],
    },
    {
        "slug": "unb-hybrid-rocket",
        "title": "UnB hybrid rocket static-fire test bench",
        "meta": "Universidade de Brasília · research · 20122013",
        "tags": ["CAD", "Test", "Calculations"],
        "image": "/assets/img/placeholders/test-ait.png",
        "summary": "Volunteer research on hybrid rocket static-fire test benches at UnB; related publication at the 19th UnB Scientific Initiation Congress (2013).",
        "context": """
<p>During the Mechanical Engineering bachelors at Universidade de Brasília, I worked as a volunteer researcher on hybrid rocket static-fire test benches (Mar 2012  Jun 2013). Related extracurriculars: Apuama Racing (Formula SAE) and N-Prize.</p>
""",
        "requirements": """
<ul>
  <li>Experimental bench enabling static-fire testing of hybrid rocket motors.</li>
  <li class="todo"><strong>TODO</strong> - Erlan: thrust / instrumentation requirements from the 2013 project if still accurate.</li>
</ul>
""",
        "approach": """
<p>Design of an experimental bench for hybrid propulsion tests (documented in the 2013 UnB Scientific Initiation Congress paper). Later CFD work on a pressure-swirl atomizer appeared at CILAMCE 2016 (ANSYS CFX).</p>
<div class="math-block">
<p>Illustrative thrust from measured load (placeholder):</p>
$$T = F_{\\mathrm{load\\,cell}}$$
<p><strong>TODO</strong>: Erlan to replace with the data-reduction approach actually used.</p>
</div>
""",
        "results": """
<p>Published: Cassiano, E. (2013). <em>Projeto de uma Bancada Experimental para o Teste de Motores Foguetes com Propulsão Híbrida</em>. 19th UnB Scientific Initiation Congress.</p>
<p class="todo"><strong>TODO</strong> - Erlan: photos of the bench and any cleared measured curves.</p>
""",
        "mfg_test": """
<p class="todo"><strong>TODO</strong> - Erlan: fabrication of the bench and static-fire safety procedure summary.</p>
""",
        "lessons": """
<p class="todo"><strong>TODO</strong> - Erlan: instrumentation and safety lessons still relevant to spacecraft test setups.</p>
""",
        "tools": ["SolidWorks", "Test instrumentation", "ANSYS CFX (related CFD)"],
    },
]


def tags_html(tags):
    return "<ul class=\"tags\">" + "".join(f"<li>{t}</li>" for t in tags) + "</ul>"


def tools_html(tools):
    return "<ul class=\"tags\">" + "".join(f"<li>{t}</li>" for t in tools) + "</ul>"


HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Erlan Cassiano</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://erlancassiano.github.io/projects/{slug}/">
<link rel="icon" href="/favicon.png" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=Syne:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
<link rel="stylesheet" href="/assets/css/site.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:false}});"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="/">Erlan Cassiano <span>Mech · Space</span></a>
    <button class="icon-btn menu-toggle" type="button" data-menu-toggle aria-expanded="false" aria-controls="nav-links" aria-label="Open menu">?</button>
    <ul class="nav-links" id="nav-links" data-nav-links>
      <li><a href="/#projects">Projects</a></li>
      <li><a href="/#timeline">Timeline</a></li>
      <li><a href="/#calculations">Calculations</a></li>
      <li><a href="/#gallery">Gallery</a></li>
      <li><a href="/#publications">Publications</a></li>
      <li><a href="/resume.html">Resume</a></li>
      <li><a href="/#contact">Contact</a></li>
    </ul>
    <div class="nav-actions">
      <button class="icon-btn" type="button" data-theme-toggle aria-pressed="false" title="Toggle theme">DK</button>
    </div>
  </div>
</header>
"""


def render(project: dict) -> str:
    return f"""{HEAD.format(title=project['title'], description=project['summary'], slug=project['slug'])}
<main id="main">
  <header class="case-hero">
    <div class="wrap">
      <p class="kicker">Case study</p>
      <h1>{project['title']}</h1>
      <p class="lede">{project['summary']}</p>
      <p class="case-meta">{project['meta']}</p>
      {tags_html(project['tags'])}
    </div>
  </header>
  <div class="wrap case-layout">
    <article class="case-body">
      <section id="context">
        <h2>Context</h2>
        {project['context']}
      </section>
      <section id="requirements">
        <h2>Requirements</h2>
        {project['requirements']}
      </section>
      <section id="approach">
        <h2>Approach</h2>
        {project['approach']}
      </section>
      <section id="results">
        <h2>Results</h2>
        {project['results']}
      </section>
      <section id="manufacturing-test">
        <h2>Manufacturing &amp; test</h2>
        {project['mfg_test']}
      </section>
      <section id="lessons">
        <h2>Lessons</h2>
        {project['lessons']}
      </section>
      <section id="tools">
        <h2>Tools</h2>
        {tools_html(project['tools'])}
      </section>
      <section id="confidentiality">
        <h2>Confidentiality</h2>
        <p class="note">No confidential Visiona or Thales Alenia Space data, drawings, or datasets are published on this page. Figures marked PLACEHOLDER must be replaced only with material cleared for public release. TVAC for SATVHR is not yet done and is not claimed here.</p>
      </section>
      <p style="margin-top:2rem"><a class="btn ghost" href="/#projects">? All projects</a></p>
    </article>
    <aside class="case-toc" aria-label="On this page">
      <p>On this page</p>
      <ol>
        <li><a href="#context">Context</a></li>
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#approach">Approach</a></li>
        <li><a href="#results">Results</a></li>
        <li><a href="#manufacturing-test">Manufacturing &amp; test</a></li>
        <li><a href="#lessons">Lessons</a></li>
        <li><a href="#tools">Tools</a></li>
        <li><a href="#confidentiality">Confidentiality</a></li>
      </ol>
    </aside>
  </div>
</main>
{FOOTER}
"""


def main():
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    for p in PROJECTS:
        out = PROJECTS_DIR / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(p), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
    # Export project cards data for index generation check
    cards = ROOT / "scripts" / "projects.json"
    import json
    cards.write_text(json.dumps([{k: p[k] for k in ("slug","title","meta","tags","image","summary")} for p in PROJECTS], indent=2), encoding="utf-8")
    print("wrote", cards.relative_to(ROOT))


if __name__ == "__main__":
    main()
