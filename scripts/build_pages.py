#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate EN + PT-BR case-study HTML pages from project data. Run from repo root."""
from pathlib import Path
import re

from pt_generated_cases import PT_GENERATED, PT_MEDIA_SECTIONS
from pt_hand_cases import EN_HAND_CASES, PT_HAND_CASES

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "projects"
PT_PROJECTS_DIR = ROOT / "pt" / "projects"
SITE = "https://erlancassiano.github.io"
OG_IMAGE = f"{SITE}/assets/img/og-share.jpg"
FONT_HREF = (
    "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400"
    "&family=IBM+Plex+Sans:wght@400;500&family=Syne:wght@700&display=swap"
)

TEXT_KEYS = (
    "title",
    "meta",
    "summary",
    "context",
    "requirements",
    "approach",
    "results",
    "mfg_test",
    "lessons",
    "tools",
    "confidentiality",
)

UI = {
    "en": {
        "html_lang": "en",
        "brand_sub": "Mech · Space",
        "home": "/",
        "skip": "Skip to content",
        "open_menu": "Open menu",
        "toggle_theme": "Toggle theme",
        "nav": [
            ("/#projects", "Projects"),
            ("/#timeline", "Timeline"),
            ("/#publications", "Publications"),
            ("/#certifications", "Skills"),
            ("/media/", "In the Media"),
            ("/resume.html", "Resume"),
            ("/#contact", "Contact"),
        ],
        "footer_tag": "Spacecraft Mechanical Design",
        "footer_projects": "Projects",
        "footer_resume": "Resume",
        "case_kicker": "Case study",
        "on_this_page": "On this page",
        "on_this_page_aria": "On this page",
        "all_projects": "← All projects",
        "all_projects_href": "/#projects",
        "sections": {
            "context": "Context",
            "requirements": "Requirements",
            "approach": "Approach",
            "results": "Results",
            "mfg_test": "Manufacturing &amp; test",
            "lessons": "Lessons",
            "tools": "Tools",
            "media": "In the media",
            "confidentiality": "Confidentiality",
        },
        "default_confidentiality": (
            "No confidential Visiona or Thales Alenia Space data, drawings, or "
            "datasets are published on this page. TVAC for SATVHR is not yet done "
            "and is not claimed here."
        ),
    },
    "pt": {
        "html_lang": "pt-BR",
        "brand_sub": "Mec · Espaço",
        "home": "/pt/",
        "skip": "Ir ao conteúdo",
        "open_menu": "Abrir menu",
        "toggle_theme": "Alternar tema",
        "nav": [
            ("/pt/#projects", "Projetos"),
            ("/pt/#timeline", "Linha do tempo"),
            ("/pt/#publications", "Publicações"),
            ("/pt/#certifications", "Competências"),
            ("/pt/media/", "Na mídia"),
            ("/pt/resume.html", "Currículo"),
            ("/pt/#contact", "Contato"),
        ],
        "footer_tag": "Projeto Mecânico de Satélites",
        "footer_projects": "Projetos",
        "footer_resume": "Currículo",
        "case_kicker": "Estudo de caso",
        "on_this_page": "Nesta página",
        "on_this_page_aria": "Nesta página",
        "all_projects": "← Todos os projetos",
        "all_projects_href": "/pt/#projects",
        "sections": {
            "context": "Contexto",
            "requirements": "Requisitos",
            "approach": "Abordagem",
            "results": "Resultados",
            "mfg_test": "Fabricação e ensaio",
            "lessons": "Lições",
            "tools": "Ferramentas",
            "media": "Na mídia",
            "confidentiality": "Confidencialidade",
        },
        "default_confidentiality": (
            "Nenhum dado, desenho ou conjunto de dados confidencial da Visiona ou "
            "da Thales Alenia Space é publicado nesta página. O TVAC do SATVHR "
            "ainda não foi realizado e não é reivindicado aqui."
        ),
    },
}

SECTION_DEFS = [
    ("context", "context"),
    ("requirements", "requirements"),
    ("approach", "approach"),
    ("results", "results"),
    ("mfg_test", "mfg_test", "manufacturing-test"),
    ("lessons", "lessons"),
]

PROJECTS = [
    {
        "slug": "satvhr-stm",
        "title": "SATVHR mechanical architecture & STM vibration qualification",
        "meta": "Visiona · LEO Earth observation · Phase B/C · 2023–present",
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
  <li>Structural–thermal model (STM) vibration qualification correlated with the FEM.</li>
</ul>
""",
        "approach": """
<p>Layouts and accommodation were driven in Creo. Structural work used Femap/Nastran models for design reviews and troubleshooting; thermal architecture used Thermal Desktop/SINDA. Margin reports documented the structural and thermal posture ahead of system reviews (PRR, PDR), with system / structure / thermal CDRs targeted for end of 2026.</p>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-01-visiona.jpg" alt="Close-up of the SatVHR STM showing copper multi-layer insulation and a large black cylindrical optical baffle on a grey mounting plate" width="1024" height="624" loading="lazy">
  <figcaption>
    <span class="figure-cap">Close-up of the SatVHR STM: copper MLI blankets and the black cylindrical optical baffle on the payload interface plate.</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid" data-featured-list>
  <div data-featured="true"><strong>&lt; 300 kg</strong><span>System mass class</span></div>
  <div data-featured="true"><strong>May 2026</strong><span>STM vib. qual. passed</span></div>
  <div data-featured="true"><strong>&lt; 1 µm</strong><span>Jitter measurement precision</span></div>
</div>
<p>STM vibration qualification (sine, random, and sine burst) passed at INPE/LIT in May 2026 and was correlated with the FEM. Jitter on the STM (main telescope mirror displacement under reaction-wheel imbalance) was measured with precision better than 1 µm.</p>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-03-visiona.jpg" alt="Eight engineers in light-blue cleanroom smocks posing beside SatVHR solar-array and STM hardware in a high-bay integration facility" width="1024" height="624" loading="lazy">
  <figcaption>
    <span class="figure-cap">AIT team with SatVHR hardware in the integration facility — solar-array panel (left) and STM hardware (right).</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
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
        "lessons": "",
        "tools": ["Creo Parametric", "Femap/Nastran", "Thermal Desktop/SINDA", "GD&T / ISO GPS", "MATLAB", "Python"],
    },
    {
        "slug": "sgdc-propulsion",
        "title": "SGDC propulsion technology transfer",
        "meta": "Thales Alenia Space · Cannes · AEB programme · 2014–2016",
        "tags": ["Calculations", "Test", "CAD"],
        "image": "/assets/img/sgdc/sgdc-card.jpg",
        "summary": "On-the-job training on Brazil’s SGDC bipropellant propulsion subsystem; showed that more than 16 kg of additional propellant could be loaded, giving ~2.5 months of life and ~R$ 36M.",
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
<div class="results-grid" data-featured-list>
  <div data-featured="true"><strong>&gt; 16 kg</strong><span>Additional propellant</span></div>
  <div data-featured="true"><strong>~2.5 months</strong><span>Extra service life</span></div>
  <div data-featured="true"><strong>~R$ 36M</strong><span>Life-extension value shown</span></div>
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
""",
        "lessons": "",
        "tools": ["Propulsion subsystem V&amp;V", "ECSS (tailored)", "Propellant gauging / loading analysis"],
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
<div class="results-grid" data-featured-list>
  <div data-featured="true"><strong>12 kg</strong><span>CubeSat mass</span></div>
  <div data-featured="true"><strong>Apr 2023</strong><span>Transporter-7 launch</span></div>
  <div data-featured="true"><strong>IAC 2024</strong><span>TVAC campaign paper</span></div>
</div>
<p>Satellite operated in orbit after launch. Co-authored the IAC 2024 paper on the VCUB1 thermal-vacuum test campaign (IAC-24-B4.IP.21).</p>
""",
        "mfg_test": """
<p>Delta vibration, solar-panel deployment, deployer fit-check, and the TVAC campaign documented in the IAC 2024 paper. No confidential Visiona/Thales datasets are shown here.</p>
""",
        "lessons": "",
        "tools": ["SolidWorks / Onshape", "Assembly procedures", "AIT tooling"],
    },
    {
        "slug": "mgse-lifting",
        "title": "Lifting & handling MGSE — concept",
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
""",
        "approach": """
<p>I <strong>led the concept</strong>; detailed design and manufacturing were executed by a subcontracted supplier. Concept work covered lift points, handling envelopes, and interface definition against the STM configuration.</p>
""",
        "results": """
<p>MGSE was manufactured by the supplier and tested during the STM AIT campaign.</p>
""",
        "mfg_test": """
<p>Detailed and built by a subcontractor; functional/handling checks during STM AIT. TVAC for the satellite: not yet done (separate from MGSE).</p>
""",
        "lessons": "",
        "tools": ["Creo Parametric", "ICD definition", "Supplier follow-up"],
    },
    {
        "slug": "mhd-reaction-wheel",
        "title": "MHD magnetic-fluid reaction wheel",
        "meta": "ITA M.Sc. thesis · in progress · 2025–2027",
        "tags": ["CAD", "Calculations", "Test", "Additive Manufacturing"],
        "image": "/assets/img/placeholders/cad-panel.png",
        "summary": "M.Sc. thesis at ITA: development of a magnetohydrodynamic (MHD) magnetic-fluid reaction wheel for CubeSat attitude control.",
        "context": """
<p>Master’s research at Instituto Tecnológico de Aeronáutica (ITA), programme EAM-1 — Aeronautical Design, Structures, and Aerospace Systems. Advisor: Prof. Tiago de Paula. Expected completion July 2027.</p>
""",
        "requirements": """
<ul>
  <li>Reaction-wheel function using a magnetic fluid under MHD actuation, sized for CubeSat attitude control.</li>
</ul>
""",
        "approach": """
<p>Thesis work in progress on modelling and prototype development for a magnetic-fluid reaction wheel. Public technical detail will be added as results are cleared for release.</p>
""",
        "results": """
<p>Research in progress (expected completion July 2027). Measured performance figures are not published here yet.</p>
""",
        "mfg_test": "",
        "lessons": "",
        "tools": ["Creo / CAD", "MATLAB", "Python", "Lab instrumentation"],
    },
    {
        "slug": "additive-manufacturing",
        "title": "3D printing projects",
        "meta": "Personal / supporting hardware · AM",
        "tags": ["Additive Manufacturing", "CAD", "Test"],
        "image": "/assets/img/placeholders/print-am.png",
        "summary": "Additive manufacturing work for fixtures, prototypes, and supporting hardware.",
        "context": """
<p>Supporting hardware and prototypes produced with additive manufacturing methods, alongside conventional machining skills.</p>
""",
        "requirements": "",
        "approach": """
<p>Practical CNC / CAM background (SENAI aerospace machining course, 120 h) complements FDM/AM prototyping for ground support and concept hardware.</p>
""",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": ["Onshape / SolidWorks / Creo", "FDM", "CAM / CNC"],
    },
    {
        "slug": "unb-hybrid-rocket",
        "title": "UnB hybrid rocket static-fire test bench",
        "meta": "Universidade de Brasília · research · 2012–2013",
        "tags": ["CAD", "Test", "Calculations"],
        "image": "/assets/img/placeholders/test-ait.png",
        "summary": "Volunteer research on hybrid rocket static-fire test benches at UnB; related publication at the 19th UnB Scientific Initiation Congress (2013).",
        "context": """
<p>During the Mechanical Engineering bachelor’s at Universidade de Brasília, I worked as a volunteer researcher on hybrid rocket static-fire test benches (Mar 2012 – Jun 2013). Related extracurriculars: Apuama Racing (Formula SAE) and N-Prize.</p>
""",
        "requirements": """
<ul>
  <li>Experimental bench enabling static-fire testing of hybrid rocket motors.</li>
</ul>
""",
        "approach": """
<p>Design of an experimental bench for hybrid propulsion tests (documented in the 2013 UnB Scientific Initiation Congress paper). Later CFD work on a pressure-swirl atomizer appeared at CILAMCE 2016 (ANSYS CFX).</p>
""",
        "results": """
<p>Published: Cassiano, E. (2013). <em>Projeto de uma Bancada Experimental para o Teste de Motores Foguetes com Propulsão Híbrida</em>. 19th UnB Scientific Initiation Congress.</p>
""",
        "mfg_test": "",
        "lessons": "",
        "tools": ["SolidWorks", "Test instrumentation", "ANSYS CFX (related CFD)"],
    },
    {
        "slug": "pulse-jet-dust-filter",
        "title": "Pulse-jet baghouse dust collection filter",
        "meta": "Mechanical · industrial",
        "tags": ["CAD", "Manufacturing"],
        "image": "/assets/img/placeholders/structure.png",
        "summary": "Pulse-jet / baghouse dust collection filter.",
        "context": """
<p>Pulse-jet / baghouse dust collection filter.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "educational-rocket-model",
        "title": "Educational rocket model",
        "meta": "Aerospace · rocketry",
        "tags": ["CAD", "Test"],
        "image": "/assets/img/placeholders/test-ait.png",
        "summary": "Educational rocket model.",
        "context": """
<p>Educational rocket model.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "co2-nose-cone-ejector",
        "title": "CO2 nose-cone ejector",
        "meta": "Aerospace · rocketry",
        "tags": ["CAD", "Test"],
        "image": "/assets/img/placeholders/test-ait.png",
        "summary": "CO2 nose-cone ejector for a rocket.",
        "context": """
<p>CO2 nose-cone ejector for a rocket.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "side-ejecting-parachute",
        "title": "Side-ejecting parachute system for a rocket",
        "meta": "Aerospace · rocketry",
        "tags": ["CAD", "Test"],
        "image": "/assets/img/placeholders/test-ait.png",
        "summary": "Side-ejecting parachute system for a rocket.",
        "context": """
<p>Side-ejecting parachute system for a rocket.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "cloud-seeding-rocket",
        "title": "Cloud-seeding rocket",
        "meta": "Aerospace · rocketry",
        "tags": ["CAD", "Test"],
        "image": "/assets/img/placeholders/test-ait.png",
        "summary": "Cloud-seeding rocket.",
        "context": """
<p>Cloud-seeding rocket.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "omega-power-flywheel",
        "title": "Omega Power flywheel energy storage",
        "meta": "Mechanical · energy",
        "tags": ["CAD", "Energy"],
        "image": "/assets/img/placeholders/fea-mode.png",
        "summary": "Omega Power flywheel for energy storage.",
        "context": """
<p>Omega Power flywheel for energy storage.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "truck-antenna-mount",
        "title": "Truck antenna mount",
        "meta": "Mechanical · industrial",
        "tags": ["CAD", "Manufacturing"],
        "image": "/assets/img/placeholders/structure.png",
        "summary": "Antenna mount for trucks.",
        "context": """
<p>Antenna mount for trucks.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "compact-antennas",
        "title": "Structural and thermal design of compact antennas",
        "meta": "Mechanical · antennas",
        "tags": ["CAD", "Thermal", "FEA"],
        "image": "/assets/img/placeholders/fea-mode.png",
        "summary": "Structural and thermal design of compact antennas.",
        "context": """
<p>Structural and thermal design of compact antennas.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "rua-dois-system",
        "title": "Rua Dois system and app",
        "meta": "Software · Rua Dois",
        "tags": ["Software"],
        "image": "/assets/img/placeholders/cad-panel.png",
        "summary": "Rua Dois system and app.",
        "context": """
<p>Rua Dois system and app.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "civ-system",
        "title": "CIV system",
        "meta": "Software · CIV",
        "tags": ["Software"],
        "image": "/assets/img/placeholders/cad-panel.png",
        "summary": "CIV system.",
        "context": """
<p>CIV system.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    {
        "slug": "comida-verificada",
        "title": "Comida Verificada (CoV) food-verification platform",
        "meta": "Software · non-profit",
        "tags": ["Software"],
        "image": "/assets/img/placeholders/cad-panel.png",
        "summary": "Comida Verificada (CoV), a non-profit food-verification platform.",
        "context": """
<p>Comida Verificada (CoV), a non-profit food-verification platform.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
]

MEDIA_SECTIONS_EN = {
    "sgdc-propulsion": """
      <section id="in-the-media">
        <h2>In the media</h2>
        <div class="project-media">
          <ul>
            <li><a href="https://www.gov.br/aeb/pt-br/assuntos/noticias/engenheiro-da-aeb-desenvolve-metodo-que-aumenta-tempo-de-vida-do-sgdc" target="_blank" rel="noopener noreferrer">AEB (2017-03-23)</a> - tank-loading method that extends SGDC life. <span class="media-badge">Mentions Erlan</span></li>
            <li><a href="https://www.defesanet.com.br/defesa/sgdc-chega-a-posicao-definitiva-ate-sabado/" target="_blank" rel="noopener noreferrer">DefesaNet (2017-05-05)</a> - AEB engineers' contributions, including life extension. <span class="media-badge">Mentions Erlan</span></li>
          </ul>
          <a class="media-more" href="/media/#sgdc">All SGDC coverage →</a>
        </div>
      </section>
""",
    "satvhr-stm": """
      <section id="in-the-media">
        <h2>In the media</h2>
        <div class="project-media">
          <ul>
            <li><a href="https://telesintese.com.br/satelite-brasileiro-satvhr-conclui-teste-critico-de-vibracao-para-lancamento/" target="_blank" rel="noopener noreferrer">Telesíntese (2026-05-13)</a> - STM vibration testing at INPE/LIT.</li>
            <li><a href="https://visionaespacial.com/2026-05-13-visiona-conclui-com-sucesso-teste-critico-de-desenvolvimento-do-satelite-satvhr/" target="_blank" rel="noopener noreferrer">Visiona (2026-05-13)</a> - official STM vibration campaign release.</li>
            <li><a href="https://fiesc.com.br/pt-br/imprensa/senaisc-integra-projeto-premiado-com-maior-grau-de-conteudo-nacional-da-historia-espacial" target="_blank" rel="noopener noreferrer">FIESC/SENAI-SC (2026-03-19)</a> - SatVHR wins 2025 FINEP Innovation Award.</li>
          </ul>
          <a class="media-more" href="/media/#satvhr">All SATVHR coverage →</a>
        </div>
      </section>
""",
    "vcub1-assembly": """
      <section id="in-the-media">
        <h2>In the media</h2>
        <div class="project-media">
          <ul>
            <li><a href="https://pesquisaparainovacao.fapesp.br/primeiro_satelite_de_observacao_da_terra_e_coleta_de_dados_projetado_pela_industria_nacional_e_lancado_nos_eua/2703" target="_blank" rel="noopener noreferrer">FAPESP (2023-04-15)</a> - VCUB1 launch coverage.</li>
            <li><a href="https://visionaespacial.com/visiona-comemora-um-ano-do-lancamento-do-satelite-vcub1/" target="_blank" rel="noopener noreferrer">Visiona (2024-04-15)</a> - one year in orbit.</li>
          </ul>
          <a class="media-more" href="/media/#vcub1">All VCUB1 coverage →</a>
        </div>
      </section>
""",
}


def tags_html(tags):
    return "<ul class=\"tags\">" + "".join(f"<li>{t}</li>" for t in tags) + "</ul>"


def tools_html(tools):
    return "<ul class=\"tags\">" + "".join(f"<li>{t}</li>" for t in tools) + "</ul>"


def has_content(html: str) -> bool:
    if not html or not html.strip():
        return False
    text = re.sub(r"<[^>]+>", " ", html)
    return bool(re.sub(r"\s+", "", text))


def esc_attr(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def page_url(slug: str, lang: str) -> str:
    if lang == "en":
        return f"{SITE}/projects/{slug}/"
    return f"{SITE}/pt/projects/{slug}/"


def page_path(slug: str, lang: str) -> Path:
    if lang == "en":
        return PROJECTS_DIR / slug / "index.html"
    return PT_PROJECTS_DIR / slug / "index.html"


def lang_switcher(slug: str, lang: str) -> str:
    en_href = f"/projects/{slug}/"
    pt_href = f"/pt/projects/{slug}/"
    if lang == "en":
        return (
            f'<nav class="lang-switch" aria-label="Language">'
            f'<a href="{en_href}" hreflang="en" lang="en" aria-current="page">EN</a>'
            f'<span aria-hidden="true">|</span>'
            f'<a href="{pt_href}" hreflang="pt-BR" lang="pt-BR">PT</a>'
            f"</nav>"
        )
    return (
        f'<nav class="lang-switch" aria-label="Idioma">'
        f'<a href="{en_href}" hreflang="en" lang="en">EN</a>'
        f'<span aria-hidden="true">|</span>'
        f'<a href="{pt_href}" hreflang="pt-BR" lang="pt-BR" aria-current="page">PT</a>'
        f"</nav>"
    )


def nav_html(ui: dict) -> str:
    return "\n".join(f'      <li><a href="{href}">{label}</a></li>' for href, label in ui["nav"])


def footer_html(ui: dict) -> str:
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <p>© <span data-year></span> Erlan Cassiano · {ui["footer_tag"]}</p>
    <p><a href="{ui["all_projects_href"]}">{ui["footer_projects"]}</a> · <a href="{ui["nav"][5][0]}">{ui["footer_resume"]}</a> · <a href="https://www.linkedin.com/in/erlancassiano">LinkedIn</a></p>
  </div>
</footer>
<script src="/assets/js/site.js"></script>
</body>
</html>
"""


def head_html(title: str, description: str, slug: str, lang: str, ui: dict) -> str:
    url = page_url(slug, lang)
    en_url = page_url(slug, "en")
    pt_url = page_url(slug, "pt")
    return f"""<!doctype html>
<html lang="{ui["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Erlan Cassiano</title>
<meta name="description" content="{esc_attr(description)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="pt-BR" href="{pt_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc_attr(title)} · Erlan Cassiano">
<meta property="og:description" content="{esc_attr(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(title)} · Erlan Cassiano">
<meta name="twitter:description" content="{esc_attr(description)}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{FONT_HREF}">
<link rel="stylesheet" href="{FONT_HREF}" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="{FONT_HREF}"></noscript>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
<link rel="stylesheet" href="/assets/css/site.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:false}});"></script>
</head>
<body>
<a class="skip" href="#main">{ui["skip"]}</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="{ui["home"]}">Erlan Cassiano <span>{ui["brand_sub"]}</span></a>
    <button class="icon-btn menu-toggle" type="button" data-menu-toggle aria-expanded="false" aria-controls="nav-links" aria-label="{ui["open_menu"]}">☰</button>
    <ul class="nav-links" id="nav-links" data-nav-links>
{nav_html(ui)}
    </ul>
    <div class="nav-actions">
      {lang_switcher(slug, lang)}
      <button class="icon-btn" type="button" data-theme-toggle aria-pressed="false" title="{ui["toggle_theme"]}">DK</button>
    </div>
  </div>
</header>
"""


def localize_project(base: dict, lang: str) -> dict:
    """Merge EN base fields with PT overlay when lang=pt."""
    out = {
        "slug": base["slug"],
        "tags": list(base.get("tags") or []),
        "image": base.get("image", ""),
    }
    for key in TEXT_KEYS:
        out[key] = base.get(key, "" if key != "tools" else [])
    if lang == "pt":
        overlay = PT_GENERATED.get(base["slug"]) or PT_HAND_CASES.get(base["slug"])
        if not overlay:
            raise KeyError(f"Missing PT overlay for {base['slug']}")
        for key in TEXT_KEYS:
            if key in overlay:
                out[key] = overlay[key]
        if "tags" in overlay:
            out["tags"] = overlay["tags"]
    return out


def all_base_projects() -> list:
    projects = list(PROJECTS)
    existing = {p["slug"] for p in projects}
    for slug, en in EN_HAND_CASES.items():
        if slug in existing:
            continue
        projects.append(
            {
                "slug": slug,
                "title": en["title"],
                "meta": en["meta"],
                "tags": en["tags"],
                "image": en.get("image", ""),
                "summary": en["summary"],
                "context": en.get("context", ""),
                "requirements": en.get("requirements", ""),
                "approach": en.get("approach", ""),
                "results": en.get("results", ""),
                "mfg_test": en.get("mfg_test", ""),
                "lessons": en.get("lessons", ""),
                "tools": en.get("tools", []),
                "confidentiality": en.get("confidentiality", ""),
            }
        )
    return projects


def render(project: dict, lang: str) -> str:
    ui = UI[lang]
    labels = ui["sections"]
    sections = []
    toc = []
    for item in SECTION_DEFS:
        key = item[0]
        sid = item[2] if len(item) > 2 else key
        body = project.get(key, "")
        if not has_content(body):
            continue
        label = labels[key]
        sections.append(f"""      <section id="{sid}">
        <h2>{label}</h2>
        {body}
      </section>""")
        toc.append(f'        <li><a href="#{sid}">{label}</a></li>')

    tools = project.get("tools") or []
    if tools:
        sections.append(f"""      <section id="tools">
        <h2>{labels["tools"]}</h2>
        {tools_html(tools)}
      </section>""")
        toc.append(f'        <li><a href="#tools">{labels["tools"]}</a></li>')

    if lang == "en":
        media = MEDIA_SECTIONS_EN.get(project["slug"], "")
    else:
        media = PT_MEDIA_SECTIONS.get(project["slug"], "")
        # Fix media "more" links to PT media page
        media = media.replace('href="/media/', 'href="/pt/media/')
    if media:
        sections.append(media)
        toc.append(f'        <li><a href="#in-the-media">{labels["media"]}</a></li>')

    conf = project.get("confidentiality") or ui["default_confidentiality"]
    sections.append(f"""      <section id="confidentiality">
        <h2>{labels["confidentiality"]}</h2>
        <p class="note">{conf}</p>
      </section>""")
    toc.append(f'        <li><a href="#confidentiality">{labels["confidentiality"]}</a></li>')

    return f"""{head_html(project["title"], project["summary"], project["slug"], lang, ui)}
<main id="main">
  <header class="case-hero">
    <div class="wrap">
      <p class="kicker">{ui["case_kicker"]}</p>
      <h1>{project["title"]}</h1>
      <p class="lede">{project["summary"]}</p>
      <p class="case-meta">{project["meta"]}</p>
      {tags_html(project["tags"])}
    </div>
  </header>
  <div class="wrap case-layout">
    <article class="case-body">
{chr(10).join(sections)}
      <p style="margin-top:2rem"><a class="btn ghost" href="{ui["all_projects_href"]}">{ui["all_projects"]}</a></p>
    </article>
    <aside class="case-toc" aria-label="{ui["on_this_page_aria"]}">
      <p>{ui["on_this_page"]}</p>
      <ol>
{chr(10).join(toc)}
      </ol>
    </aside>
  </div>
</main>
{footer_html(ui)}
"""


def write_chimneys_redirect(lang: str) -> None:
    if lang == "en":
        out = PROJECTS_DIR / "fox17-chimneys" / "index.html"
        bolivia = "/projects/fox17-chimney-bolivia/"
        strakes = "/projects/fox17-chimney-strakes/"
        title = "Redirecting…"
        body = (
            f'This case study has been split. Continue to '
            f'<a href="{bolivia}">Export steel chimney, 102.7 m</a> or '
            f'<a href="{strakes}">Steel chimney, ~95 m with helical strakes</a>.'
        )
        canonical = f"{SITE}/projects/fox17-chimney-bolivia/"
        refresh = bolivia
    else:
        out = PT_PROJECTS_DIR / "fox17-chimneys" / "index.html"
        bolivia = "/pt/projects/fox17-chimney-bolivia/"
        strakes = "/pt/projects/fox17-chimney-strakes/"
        title = "Redirecionando…"
        body = (
            f'Este estudo de caso foi dividido. Continue para '
            f'<a href="{bolivia}">Chaminé de aço para exportação, 102,7 m</a> ou '
            f'<a href="{strakes}">Chaminé de aço, ~95 m com strakes helicoidais</a>.'
        )
        canonical = f"{SITE}/pt/projects/fox17-chimney-bolivia/"
        refresh = bolivia
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        f"""<!doctype html>
<html lang="{"en" if lang == "en" else "pt-BR"}">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={refresh}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<title>{title}</title>
</head>
<body>
<p>{body}</p>
</body>
</html>
""",
        encoding="utf-8",
    )
    print("wrote", out.relative_to(ROOT))


def main():
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    PT_PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    bases = all_base_projects()
    missing_pt = [p["slug"] for p in bases if p["slug"] not in PT_GENERATED and p["slug"] not in PT_HAND_CASES]
    if missing_pt:
        raise SystemExit(f"Missing PT overlays for: {missing_pt}")
    for base in bases:
        for lang in ("en", "pt"):
            localized = localize_project(base, lang)
            out = page_path(base["slug"], lang)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render(localized, lang), encoding="utf-8")
            print("wrote", out.relative_to(ROOT))
    for lang in ("en", "pt"):
        write_chimneys_redirect(lang)
    print("skipped projects.json (hand-maintained catalog with PT fields)")


if __name__ == "__main__":
    main()
