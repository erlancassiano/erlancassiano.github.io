# -*- coding: utf-8 -*-
"""Hand-authored EN/PT case-study content for Fox17 and AEB pages.

Generator-owned bilingual payload for:
  fox17-chimney-bolivia, fox17-chimney-strakes, fox17-plant-ventilation,
  fox17-blast-cabin, fox17-pulleys, fox17-solar-pv, aeb-parachute-cansat-bench.

EN text is extracted from the existing English HTML; PT is faithful pt-BR.
summary prefers the page lede when richer than the meta description.
"""

# Card / hero images (from projects.json)
IMAGES = {
    "fox17-chimney-bolivia": "/assets/img/fox17/chimney-itacamba-01.jpg",
    "fox17-chimney-strakes": "/assets/img/fox17/chimney-cimesa-03.jpg",
    "fox17-plant-ventilation": "/assets/img/fox17/intercement-caf-07.jpg",
    "fox17-blast-cabin": "/assets/img/fox17/blast-cabin-01.jpg",
    "fox17-pulleys": "/assets/img/fox17/pulley-largo-01.jpg",
    "fox17-solar-pv": "/assets/img/fox17/solar-pv-003a.jpg",
    "aeb-parachute-cansat-bench": "/assets/img/aeb-cansat-bench/card.jpg",
}

CONF_FOX17_EN = (
    "Client names on this case study are kept generic. No confidential Visiona or "
    "Thales Alenia Space data are published here. Title-block text, prices, and "
    "program chrome were cropped or redacted from CAD screenshots where present."
)
CONF_FOX17_PT = (
    "Os nomes de clientes neste estudo de caso são mantidos genéricos. Nenhum dado "
    "confidencial da Visiona ou da Thales Alenia Space é publicado aqui. Texto de "
    "carimbo, preços e elementos de programa foram recortados ou omitidos das "
    "capturas de CAD quando presentes."
)
CONF_AEB_EN = (
    "Only facts confirmed for this page are stated above. No invented dimensions, "
    "loads, or dates. No confidential Visiona or Thales Alenia Space data are "
    "published here."
)
CONF_AEB_PT = (
    "Somente fatos confirmados para esta página constam acima. Sem dimensões, "
    "cargas ou datas inventadas. Nenhum dado confidencial da Visiona ou da "
    "Thales Alenia Space é publicado aqui."
)

EN_HAND_CASES = {
    "fox17-chimney-bolivia": {
        "title": "Export steel chimney, 102.7 m (cement plant, Bolivia)",
        "meta": "Fox17 · cement plant export · 2016",
        "summary": (
            "Author and designer of a 102.7 m export steel chimney and its bolted "
            "flanges for a cement-plant project in Bolivia — ~128 t, base Ø3.83 m, "
            "ten flanges, ASME STS-1-2011."
        ),
        "tags": ["CAD", "Calculations", "FEA"],
        "tools": ["SolidWorks", "ASME STS-1-2011", "Fabrication drawings"],
        "image": IMAGES["fox17-chimney-bolivia"],
        "confidentiality": CONF_FOX17_EN,
        "context": """
<p>As co-founder &amp; CTO at Fox17, I was the author and designer of a 102.7 m steel chimney and its bolted structural flanges for export to a cement plant in Bolivia (2016).</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-01.jpg" alt="3D model of 102.7 m stack flange region" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">3D model of the 102.7 m stack (ASME STS-1-2011, ≈128 t).</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>102.7 m stack height; base diameter 3.83 m; mass on the order of ~128 t.</li>
  <li>Ten bolted structural flanges suitable for fabrication and export.</li>
  <li>Design to ASME STS-1-2011 for steel stacks.</li>
</ul>
""",
        "approach": """
<p>Mechanical design of the chimney shell and bolted flanges in CAD, with detailing for fabrication and assembly.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-02.jpg" alt="Base reinforcement of steel chimney" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Base reinforcement.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-03.jpg" alt="Flange 3D model for steel chimney" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Flange 3D model.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-04.jpg" alt="Flange detail of steel chimney" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Flange detail.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-05.jpg" alt="Flange 3D model for steel chimney" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Flange 3D model.</span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid" id="fox17-chimney-bolivia-results" data-featured-list>
  <div data-featured="true"><strong>102.7 m</strong><span>Stack height</span></div>
  <div data-featured="true"><strong>~128 t</strong><span>Chimney mass</span></div>
  <div data-featured="true"><strong>Ø3.83 m</strong><span>Base diameter</span></div>
  <div data-featured="true"><strong>10</strong><span>Bolted flanges</span></div>
</div>
<p>Designed to ASME STS-1-2011 as author/designer of the chimney and flanges.</p>
""",
        "mfg_test": """
<p>Export-oriented detailing of shells and flanges for fabrication and bolted assembly.</p>
""",
        "lessons": """
<p>Large bolted flange interfaces and stack segmentation lessons transfer to heavy MGSE and ground-support structures.</p>
""",
    },
    "fox17-chimney-strakes": {
        "title": "Steel chimney, ~95 m with helical strakes (cement plant)",
        "meta": "Fox17 · cement plant · 2015",
        "summary": (
            "~95.5 m cement-plant steel chimney with helical strakes — three bolted "
            "structural flanges, baseplate at Ø5.04 m — checked for vortex shedding, "
            "wind, seismic and fatigue in MECASTACK. Technical data report and QC/approval."
        ),
        "tags": ["CAD", "Calculations", "FEA"],
        "tools": ["MECASTACK", "SolidWorks", "Technical reporting"],
        "image": IMAGES["fox17-chimney-strakes"],
        "confidentiality": CONF_FOX17_EN,
        "context": """
<p>In 2015 at Fox17 I wrote the technical data report and performed QC/approval for a ~95.5 m steel chimney (top elevation 115 m context) with helical strakes for a cement plant.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-03.jpg" alt="Stack elevation of ~95.5 m chimney with helical strakes" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">MECASTACK stack elevation (~95.5 m, three bolted flanges).</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>~95.5 m stack with helical strakes; base diameter 5.04 m.</li>
  <li>Three bolted structural flanges plus baseplate.</li>
  <li>Checks for vortex shedding, wind, seismic and fatigue.</li>
</ul>
""",
        "approach": """
<p>Structural modelling and verification in MECASTACK; 3D detailing of flanges and baseplate for fabrication.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-01.jpg" alt="MECASTACK model figure of chimney base" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">MECASTACK model, figure 2.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-02.jpg" alt="MECASTACK model figure of chimney" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">MECASTACK model, figure 3.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-04.jpg" alt="Structural flange 3D model" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Structural flange 3D model.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-05.jpg" alt="Bolted structural flange 3D model" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Bolted structural flange 3D.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-06.jpg" alt="Chimney baseplate 3D model" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Baseplate 3D model (base Ø5.04 m).</span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid" id="fox17-chimney-strakes-results" data-featured-list>
  <div data-featured="true"><strong>~95.5 m</strong><span>Stack height</span></div>
  <div data-featured="true"><strong>Ø5.04 m</strong><span>Base diameter</span></div>
  <div data-featured="true"><strong>3 + base</strong><span>Bolted flanges</span></div>
  <div data-featured="true"><strong>MECASTACK</strong><span>Wind / seismic / fatigue</span></div>
</div>
<p>Helical strakes included for vortex-shedding control; report authored with QC/approval responsibility.</p>
""",
        "mfg_test": """
<p>Flange and baseplate models prepared for fabrication; stack segmented at bolted joints.</p>
""",
        "lessons": """
<p>Combining aerodynamic appendages (strakes) with bolted segmentation is a useful pattern for tall slender structures.</p>
""",
    },
    "fox17-plant-ventilation": {
        "title": "Compressor-room ventilation & plant piping (cement plant)",
        "meta": "Fox17 · cement plant · 2016–17",
        "summary": (
            "Cement-plant mechanical engineering: compressor-room ventilation with CFD, "
            "compressed-air and industrial-water piping, and a palletizer reuse study "
            "(2016–17)."
        ),
        "tags": ["CAD", "CFD", "Piping"],
        "tools": ["SolidWorks", "SolidWorks Flow Simulation", "AutoCAD"],
        "image": IMAGES["fox17-plant-ventilation"],
        "confidentiality": CONF_FOX17_EN,
        "context": """
<p>At Fox17 I supported cement-plant mechanical design covering compressor-room ventilation, compressed-air and industrial-water piping, and reuse studies for palletizer filtration.</p>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-07.webp"><img src="/assets/img/fox17/intercement-caf-07.jpg" alt="Compressor-room 3D ventilation layout" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Compressor-room 3D.</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Ventilation concept for a compressor room, verified with CFD.</li>
  <li>Compressed-air and industrial-water piping layouts.</li>
  <li>Palletizer filter reuse study.</li>
</ul>
""",
        "approach": """
<p>CAD layouts for ducts and piping; CFD velocity checks in SolidWorks Flow Simulation; site coordination against as-built ducts.</p>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-05.webp"><img src="/assets/img/fox17/intercement-caf-05.jpg" alt="CFD velocity plot along duct length" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">CFD velocity plot (SolidWorks Flow Simulation).</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-04.webp"><img src="/assets/img/fox17/intercement-caf-04.jpg" alt="Compressor-room layout drawing" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Compressor-room layout.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-01.webp"><img src="/assets/img/fox17/intercement-caf-01.jpg" alt="Plant elevation with piping and ventilation" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Compressed-air / plant piping CAD (elevation).</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-02.webp"><img src="/assets/img/fox17/intercement-caf-02.jpg" alt="Plant plan with new filter annotation" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Compressed-air / plant piping CAD (plan).</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-03.webp"><img src="/assets/img/fox17/intercement-caf-03.jpg" alt="Supply duct 3D model" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Supply duct 3D.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-06.webp"><img src="/assets/img/fox17/intercement-caf-06.jpg" alt="Palletizer filter duct schematic" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Palletizer filter CAD.</span>
  </figcaption>
</figure>
""",
        "results": """
<p>Ventilation and piping packages delivered for plant execution; CFD used to check duct velocity along the network.</p>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-08.webp"><img src="/assets/img/fox17/intercement-caf-08.jpg" alt="Site photo of installed ducts" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Site photo of ducts.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-09.webp"><img src="/assets/img/fox17/intercement-caf-09.jpg" alt="Site photo of duct installation" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Site photo of ducts.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-10.webp"><img src="/assets/img/fox17/intercement-caf-10.jpg" alt="Compressor room photo" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Compressor room photo.</span>
  </figcaption>
</figure>
""",
        "mfg_test": """
<p>Field photos document duct installation and the compressor room as built.</p>
""",
        "lessons": """
<p>Pairing CFD spot-checks with CAD piping layouts catches velocity bottlenecks before fabrication.</p>
""",
    },
    "fox17-blast-cabin": {
        "title": "Blast-cleaning cabin in a 40-ft container",
        "meta": "Fox17 · fabrication · 2015",
        "summary": (
            "Blast-cleaning cabin integrated into a 40-ft shipping container — "
            "fabrication photos from the 2015 build."
        ),
        "tags": ["CAD", "Manufacturing"],
        "tools": ["SolidWorks", "Fabrication"],
        "image": IMAGES["fox17-blast-cabin"],
        "confidentiality": CONF_FOX17_EN,
        "context": """
<p>Fox17 project to fit a blast-cleaning cabin inside a standard 40-ft container for portable abrasive cleaning.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/blast-cabin-01.jpg" alt="Container cabin fabrication photo looking down the length" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Container cabin fabrication photo.</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Fit blast-cabin structure and workflow inside a 40-ft ISO container envelope.</li>
</ul>
""",
        "approach": """
<p>Structural fit-out of the container interior for blast operations.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/blast-cabin-02.jpg" alt="Container cabin fabrication photo" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Container cabin fabrication photo.</span>
  </figcaption>
</figure>
""",
        "results": """
<p>Cabin fabricated inside the container shell for field deployment.</p>
""",
        "mfg_test": """
<p>Fabrication documented in shop photos during assembly.</p>
""",
        "lessons": """
<p>Containerized process equipment forces tight packaging and access planning.</p>
""",
    },
    "fox17-pulleys": {
        "title": "Machined pulleys & shaft (mining)",
        "meta": "Fox17 · mining · 2017",
        "summary": (
            "Machined pulleys and shaft for a mining customer (2017) — as-built "
            "hardware after machining."
        ),
        "tags": ["CAD", "Manufacturing"],
        "tools": ["SolidWorks", "Machining follow-up"],
        "image": IMAGES["fox17-pulleys"],
        "confidentiality": CONF_FOX17_EN,
        "context": """
<p>Fox17 delivered machined pulleys and an associated shaft for a mining application in 2017.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/pulley-largo-01.jpg" alt="Machined pulleys on a pallet after dye-penetrant inspection" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Machined pulleys, real product photo.</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Machined pulleys and shaft to customer drawing/specification for mining service.</li>
</ul>
""",
        "approach": """
<p>Detailing and follow-up through machining and inspection (product photo after processing).</p>
""",
        "results": """
<p>Hardware completed and photographed after machining/inspection.</p>
""",
        "mfg_test": """
<p>As-built photo shows pulleys after dye-penetrant inspection marking.</p>
""",
        "lessons": """
<p>Close machining follow-up matters when replacing wear parts in mining plant.</p>
""",
    },
    "fox17-solar-pv": {
        "title": "Grid-tied solar PV systems",
        "meta": "Fox17 · SFCR · 2016–17",
        "summary": (
            "Grid-tied photovoltaic (SFCR) systems — roof-mounted arrays from Fox17 "
            "projects in 2016–17."
        ),
        "tags": ["CAD", "Energy"],
        "tools": ["CAD", "SFCR design"],
        "image": IMAGES["fox17-solar-pv"],
        "confidentiality": CONF_FOX17_EN,
        "context": """
<p>Fox17 delivered grid-tied solar PV systems (SFCR). Client and personal names are omitted on this page.</p>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/solar-pv-003a.webp"><img src="/assets/img/fox17/solar-pv-003a.jpg" alt="Installed photovoltaic array on a corrugated roof" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Installed PV array (project 003-17).</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Roof-mounted grid-tied PV array with appropriate mounting and electrical integration.</li>
</ul>
""",
        "approach": """
<p>Array layout and mounting design for grid-tied residential/commercial roofs.</p>
""",
        "results": """
<p>Installed array photographed after mounting (polycrystalline modules on rails).</p>
""",
        "mfg_test": """
<p>Field photo documents the as-installed module and rail layout.</p>
""",
        "lessons": """
<p>Mounting hardware and roof interfaces dominate installation quality for small SFCR systems.</p>
""",
    },
    "aeb-parachute-cansat-bench": {
        "title": "Parachute & CanSat deployment test bench (AEB)",
        "meta": "AEB · rocket test bench",
        "summary": (
            "Rocket test bench for parachute deployment and CanSat deployment — a "
            "project for AEB (Brazilian Space Agency)."
        ),
        "tags": ["Test", "CAD", "CanSat"],
        "tools": ["Test bench", "Deployment test"],
        "image": IMAGES["aeb-parachute-cansat-bench"],
        "confidentiality": CONF_AEB_EN,
        "context": """
<p>Project for AEB (Brazilian Space Agency): a rocket test bench used for parachute deployment and CanSat deployment testing.</p>
""",
        "requirements": """
<ul>
  <li>Support parachute-deployment testing.</li>
  <li>Support CanSat-deployment testing.</li>
</ul>
""",
        "approach": "",
        "results": "",
        "mfg_test": """
<figure class="case-figure case-video">
  <div class="video-embed">
    <iframe
      src="https://www.youtube-nocookie.com/embed/OxehKBP85ic"
      title="Cópia de LILE2 test"
      loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen></iframe>
  </div>
  <figcaption>
    <span class="figure-cap">Cópia de LILE2 test</span>
    <span class="figure-credit"><a href="https://youtu.be/OxehKBP85ic" target="_blank" rel="noopener noreferrer">YouTube</a></span>
  </figcaption>
</figure>
""",
        "lessons": "",
    },
}

PT_HAND_CASES = {
    "fox17-chimney-bolivia": {
        "title": "Chaminé de aço para exportação, 102,7 m (fábrica de cimento, Bolívia)",
        "meta": "Fox17 · exportação para fábrica de cimento · 2016",
        "summary": (
            "Autor e projetista de uma chaminé de aço de 102,7 m para exportação e "
            "de seus flanges aparafusados para um projeto de fábrica de cimento na "
            "Bolívia — ~128 t, base Ø3,83 m, dez flanges, ASME STS-1-2011."
        ),
        "tags": ["CAD", "Cálculos", "FEA"],
        "tools": ["SolidWorks", "ASME STS-1-2011", "Desenhos de fabricação"],
        "image": IMAGES["fox17-chimney-bolivia"],
        "confidentiality": CONF_FOX17_PT,
        "context": """
<p>Como cofundador e CTO da Fox17, fui o autor e projetista de uma chaminé de aço de 102,7 m e de seus flanges estruturais aparafusados para exportação a uma fábrica de cimento na Bolívia (2016).</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-01.jpg" alt="Modelo 3D da região de flange da chaminé de 102,7 m" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Modelo 3D da chaminé de 102,7 m (ASME STS-1-2011, ≈128 t).</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Altura da chaminé de 102,7 m; diâmetro da base 3,83 m; massa da ordem de ~128 t.</li>
  <li>Dez flanges estruturais aparafusados adequados à fabricação e à exportação.</li>
  <li>Projeto conforme ASME STS-1-2011 para chaminés de aço.</li>
</ul>
""",
        "approach": """
<p>Projeto mecânico do casco da chaminé e dos flanges aparafusados em CAD, com detalhamento para fabricação e montagem.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-02.jpg" alt="Reforço da base da chaminé de aço" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Reforço da base.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-03.jpg" alt="Modelo 3D de flange da chaminé de aço" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Modelo 3D do flange.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-04.jpg" alt="Detalhe de flange da chaminé de aço" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Detalhe do flange.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-itacamba-05.jpg" alt="Modelo 3D de flange da chaminé de aço" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Modelo 3D do flange.</span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid" id="fox17-chimney-bolivia-results" data-featured-list>
  <div data-featured="true"><strong>102,7 m</strong><span>Altura da chaminé</span></div>
  <div data-featured="true"><strong>~128 t</strong><span>Massa da chaminé</span></div>
  <div data-featured="true"><strong>Ø3,83 m</strong><span>Diâmetro da base</span></div>
  <div data-featured="true"><strong>10</strong><span>Flanges aparafusados</span></div>
</div>
<p>Projetada conforme ASME STS-1-2011 como autor/projetista da chaminé e dos flanges.</p>
""",
        "mfg_test": """
<p>Detalhamento orientado à exportação dos cascos e flanges para fabricação e montagem aparafusada.</p>
""",
        "lessons": """
<p>Lições de interfaces de flanges aparafusados de grande porte e de segmentação da chaminé se transferem para MGSE pesado e estruturas de suporte em solo.</p>
""",
    },
    "fox17-chimney-strakes": {
        "title": "Chaminé de aço, ~95 m com strakes helicoidais (fábrica de cimento)",
        "meta": "Fox17 · fábrica de cimento · 2015",
        "summary": (
            "Chaminé de aço de ~95,5 m para fábrica de cimento com strakes helicoidais "
            "— três flanges estruturais aparafusados, baseplate em Ø5,04 m — verificada "
            "quanto a desprendimento de vórtices, vento, sismo e fadiga no MECASTACK. "
            "Relatório de dados técnicos e QC/aprovação."
        ),
        "tags": ["CAD", "Cálculos", "FEA"],
        "tools": ["MECASTACK", "SolidWorks", "Relatórios técnicos"],
        "image": IMAGES["fox17-chimney-strakes"],
        "confidentiality": CONF_FOX17_PT,
        "context": """
<p>Em 2015, na Fox17, elaborei o relatório de dados técnicos e realizei QC/aprovação de uma chaminé de aço de ~95,5 m (contexto de elevação do topo em 115 m) com strakes helicoidais para uma fábrica de cimento.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-03.jpg" alt="Elevação da chaminé de ~95,5 m com strakes helicoidais" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Elevação da chaminé no MECASTACK (~95,5 m, três flanges aparafusados).</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Chaminé de ~95,5 m com strakes helicoidais; diâmetro da base 5,04 m.</li>
  <li>Três flanges estruturais aparafusados mais baseplate.</li>
  <li>Verificações de desprendimento de vórtices, vento, sismo e fadiga.</li>
</ul>
""",
        "approach": """
<p>Modelagem e verificação estrutural no MECASTACK; detalhamento 3D dos flanges e do baseplate para fabricação.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-01.jpg" alt="Figura do modelo MECASTACK da base da chaminé" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Modelo MECASTACK, figura 2.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-02.jpg" alt="Figura do modelo MECASTACK da chaminé" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Modelo MECASTACK, figura 3.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-04.jpg" alt="Modelo 3D de flange estrutural" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Modelo 3D do flange estrutural.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-05.jpg" alt="Modelo 3D de flange estrutural aparafusado" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Flange estrutural aparafusado em 3D.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/fox17/chimney-cimesa-06.jpg" alt="Modelo 3D do baseplate da chaminé" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Modelo 3D do baseplate (base Ø5,04 m).</span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid" id="fox17-chimney-strakes-results" data-featured-list>
  <div data-featured="true"><strong>~95,5 m</strong><span>Altura da chaminé</span></div>
  <div data-featured="true"><strong>Ø5,04 m</strong><span>Diâmetro da base</span></div>
  <div data-featured="true"><strong>3 + base</strong><span>Flanges aparafusados</span></div>
  <div data-featured="true"><strong>MECASTACK</strong><span>Vento / sismo / fadiga</span></div>
</div>
<p>Strakes helicoidais incluídos para controle do desprendimento de vórtices; relatório elaborado com responsabilidade de QC/aprovação.</p>
""",
        "mfg_test": """
<p>Modelos de flange e baseplate preparados para fabricação; chaminé segmentada nas juntas aparafusadas.</p>
""",
        "lessons": """
<p>Combinar apêndices aerodinâmicos (strakes) com segmentação aparafusada é um padrão útil para estruturas esbeltas e altas.</p>
""",
    },
    "fox17-plant-ventilation": {
        "title": "Ventilação da casa de compressores e tubulação de planta (fábrica de cimento)",
        "meta": "Fox17 · fábrica de cimento · 2016–17",
        "summary": (
            "Engenharia mecânica de fábrica de cimento: ventilação da casa de "
            "compressores com CFD, tubulação de ar comprimido e água industrial, e "
            "estudo de reaproveitamento de paletizadora (2016–17)."
        ),
        "tags": ["CAD", "CFD", "Tubulação"],
        "tools": ["SolidWorks", "SolidWorks Flow Simulation", "AutoCAD"],
        "image": IMAGES["fox17-plant-ventilation"],
        "confidentiality": CONF_FOX17_PT,
        "context": """
<p>Na Fox17, apoiei o projeto mecânico de fábrica de cimento abrangendo ventilação da casa de compressores, tubulação de ar comprimido e água industrial, e estudos de reaproveitamento da filtragem da paletizadora.</p>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-07.webp"><img src="/assets/img/fox17/intercement-caf-07.jpg" alt="Layout 3D de ventilação da casa de compressores" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Casa de compressores em 3D.</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Conceito de ventilação para a casa de compressores, verificado com CFD.</li>
  <li>Layouts de tubulação de ar comprimido e água industrial.</li>
  <li>Estudo de reaproveitamento do filtro da paletizadora.</li>
</ul>
""",
        "approach": """
<p>Layouts em CAD de dutos e tubulação; verificações de velocidade por CFD no SolidWorks Flow Simulation; coordenação de campo com dutos as-built.</p>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-05.webp"><img src="/assets/img/fox17/intercement-caf-05.jpg" alt="Gráfico CFD de velocidade ao longo do duto" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Gráfico CFD de velocidade (SolidWorks Flow Simulation).</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-04.webp"><img src="/assets/img/fox17/intercement-caf-04.jpg" alt="Desenho de layout da casa de compressores" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Layout da casa de compressores.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-01.webp"><img src="/assets/img/fox17/intercement-caf-01.jpg" alt="Elevação da planta com tubulação e ventilação" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">CAD de ar comprimido / tubulação de planta (elevação).</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-02.webp"><img src="/assets/img/fox17/intercement-caf-02.jpg" alt="Planta com anotação de novo filtro" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">CAD de ar comprimido / tubulação de planta (planta).</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-03.webp"><img src="/assets/img/fox17/intercement-caf-03.jpg" alt="Modelo 3D do duto de suprimento" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Duto de suprimento em 3D.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-06.webp"><img src="/assets/img/fox17/intercement-caf-06.jpg" alt="Esquema de duto do filtro da paletizadora" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">CAD do filtro da paletizadora.</span>
  </figcaption>
</figure>
""",
        "results": """
<p>Pacotes de ventilação e tubulação entregues para execução na planta; CFD usado para verificar a velocidade nos dutos ao longo da rede.</p>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-08.webp"><img src="/assets/img/fox17/intercement-caf-08.jpg" alt="Foto de campo dos dutos instalados" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Foto de campo dos dutos.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-09.webp"><img src="/assets/img/fox17/intercement-caf-09.jpg" alt="Foto de campo da instalação de dutos" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Foto de campo dos dutos.</span>
  </figcaption>
</figure>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/intercement-caf-10.webp"><img src="/assets/img/fox17/intercement-caf-10.jpg" alt="Foto da casa de compressores" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Foto da casa de compressores.</span>
  </figcaption>
</figure>
""",
        "mfg_test": """
<p>Fotos de campo documentam a instalação dos dutos e a casa de compressores as-built.</p>
""",
        "lessons": """
<p>Combinar verificações pontuais de CFD com layouts de tubulação em CAD identifica gargalos de velocidade antes da fabricação.</p>
""",
    },
    "fox17-blast-cabin": {
        "title": "Cabine de jateamento em contêiner de 40 pés",
        "meta": "Fox17 · fabricação · 2015",
        "summary": (
            "Cabine de jateamento integrada a um contêiner marítimo de 40 pés — "
            "fotos de fabricação da montagem de 2015."
        ),
        "tags": ["CAD", "Fabricação"],
        "tools": ["SolidWorks", "Fabricação"],
        "image": IMAGES["fox17-blast-cabin"],
        "confidentiality": CONF_FOX17_PT,
        "context": """
<p>Projeto Fox17 para acomodar uma cabine de jateamento dentro de um contêiner padrão de 40 pés para limpeza abrasiva portátil.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/blast-cabin-01.jpg" alt="Foto de fabricação da cabine no contêiner, vista ao longo do comprimento" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Foto de fabricação da cabine no contêiner.</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Acomodar a estrutura e o fluxo de trabalho da cabine de jateamento dentro do envelope de um contêiner ISO de 40 pés.</li>
</ul>
""",
        "approach": """
<p>Adequação estrutural do interior do contêiner para operações de jateamento.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/blast-cabin-02.jpg" alt="Foto de fabricação da cabine no contêiner" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Foto de fabricação da cabine no contêiner.</span>
  </figcaption>
</figure>
""",
        "results": """
<p>Cabine fabricada dentro do casco do contêiner para implantação em campo.</p>
""",
        "mfg_test": """
<p>Fabricação documentada em fotos de oficina durante a montagem.</p>
""",
        "lessons": """
<p>Equipamentos de processo em contêiner exigem empacotamento compacto e planejamento de acesso.</p>
""",
    },
    "fox17-pulleys": {
        "title": "Polias e eixo usinados (mineração)",
        "meta": "Fox17 · mineração · 2017",
        "summary": (
            "Polias e eixo usinados para um cliente de mineração (2017) — hardware "
            "as-built após usinagem."
        ),
        "tags": ["CAD", "Fabricação"],
        "tools": ["SolidWorks", "Acompanhamento de usinagem"],
        "image": IMAGES["fox17-pulleys"],
        "confidentiality": CONF_FOX17_PT,
        "context": """
<p>A Fox17 entregou polias usinadas e um eixo associado para uma aplicação de mineração em 2017.</p>
<figure class="case-figure">
  <img src="/assets/img/fox17/pulley-largo-01.jpg" alt="Polias usinadas em pallet após inspeção por líquido penetrante" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">Polias usinadas, foto do produto real.</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Polias e eixo usinados conforme desenho/especificação do cliente para serviço em mineração.</li>
</ul>
""",
        "approach": """
<p>Detalhamento e acompanhamento ao longo da usinagem e inspeção (foto do produto após o processamento).</p>
""",
        "results": """
<p>Hardware concluído e fotografado após usinagem/inspeção.</p>
""",
        "mfg_test": """
<p>A foto as-built mostra as polias após marcação de inspeção por líquido penetrante.</p>
""",
        "lessons": """
<p>O acompanhamento próximo da usinagem importa na reposição de peças de desgaste em plantas de mineração.</p>
""",
    },
    "fox17-solar-pv": {
        "title": "Sistemas fotovoltaicos conectados à rede",
        "meta": "Fox17 · SFCR · 2016–17",
        "summary": (
            "Sistemas fotovoltaicos conectados à rede (SFCR) — arranjos em telhado "
            "de projetos Fox17 em 2016–17."
        ),
        "tags": ["CAD", "Energia"],
        "tools": ["CAD", "Projeto SFCR"],
        "image": IMAGES["fox17-solar-pv"],
        "confidentiality": CONF_FOX17_PT,
        "context": """
<p>A Fox17 entregou sistemas fotovoltaicos conectados à rede (SFCR). Nomes de clientes e pessoais são omitidos nesta página.</p>
<figure class="case-figure">
  <picture><source type="image/webp" srcset="/assets/img/fox17/solar-pv-003a.webp"><img src="/assets/img/fox17/solar-pv-003a.jpg" alt="Arranjo fotovoltaico instalado em telhado corrugado" width="1200" height="800" loading="lazy"></picture>
  <figcaption>
    <span class="figure-cap">Arranjo FV instalado (projeto 003-17).</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Arranjo FV conectado à rede montado em telhado, com fixação e integração elétrica adequadas.</li>
</ul>
""",
        "approach": """
<p>Layout do arranjo e projeto de fixação para telhados residenciais/comerciais conectados à rede.</p>
""",
        "results": """
<p>Arranjo instalado fotografado após a montagem (módulos policristalinos em trilhos).</p>
""",
        "mfg_test": """
<p>Foto de campo documenta o layout as-installed de módulos e trilhos.</p>
""",
        "lessons": """
<p>A ferragem de fixação e as interfaces com o telhado dominam a qualidade de instalação em sistemas SFCR de pequeno porte.</p>
""",
    },
    "aeb-parachute-cansat-bench": {
        "title": "Bancada de ensaio de ejeção de paraquedas e CanSat (AEB)",
        "meta": "AEB · bancada de ensaio de foguete",
        "summary": (
            "Bancada de ensaio de foguete para ejeção de paraquedas e ejeção de "
            "CanSat — projeto para a AEB (Agência Espacial Brasileira)."
        ),
        "tags": ["Ensaios", "CAD", "CanSat"],
        "tools": ["Bancada de ensaio", "Ensaio de ejeção"],
        "image": IMAGES["aeb-parachute-cansat-bench"],
        "confidentiality": CONF_AEB_PT,
        "context": """
<p>Projeto para a AEB (Agência Espacial Brasileira): bancada de ensaio de foguete usada para testes de ejeção de paraquedas e de ejeção de CanSat.</p>
""",
        "requirements": """
<ul>
  <li>Suportar ensaios de ejeção de paraquedas.</li>
  <li>Suportar ensaios de ejeção de CanSat.</li>
</ul>
""",
        "approach": "",
        "results": "",
        "mfg_test": """
<figure class="case-figure case-video">
  <div class="video-embed">
    <iframe
      src="https://www.youtube-nocookie.com/embed/OxehKBP85ic"
      title="Cópia de LILE2 test"
      loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen></iframe>
  </div>
  <figcaption>
    <span class="figure-cap">Cópia de LILE2 test</span>
    <span class="figure-credit"><a href="https://youtu.be/OxehKBP85ic" target="_blank" rel="noopener noreferrer">YouTube</a></span>
  </figcaption>
</figure>
""",
        "lessons": "",
    },
}
