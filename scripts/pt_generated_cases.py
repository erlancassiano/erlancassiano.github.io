# -*- coding: utf-8 -*-
"""Brazilian Portuguese (pt-BR) content for generator-owned case studies.

Keys match PROJECTS slugs and MEDIA_SECTIONS in scripts/build_pages.py.
Faithful natural pt-BR; facts and numbers unchanged from the English source.
"""

PT_GENERATED = {
    "satvhr-stm": {
        "title": "Arquitetura mecânica do SATVHR e qualificação por vibração do STM",
        "meta": "Visiona · observação da Terra em LEO · Fase B/C · 2023–presente",
        "summary": (
            "Arquitetura mecânica e térmica de um satélite de observação da Terra "
            "em LEO com massa abaixo de 300 kg, incluindo a qualificação por vibração "
            "do STM no INPE/LIT (maio de 2026)."
        ),
        "tags": ["CAD", "FEA", "Térmico", "Teste", "Cálculos"],
        "context": """
<p>O SATVHR é um satélite de observação da Terra em LEO, com massa abaixo de 300 kg e vida útil de 5 anos, em fase B/C. Como Arquiteto Mecânico, sou responsável pela arquitetura mecânica e térmica: layouts em Creo, acomodação de payload, estrutura em painéis sanduíche, orçamento de massa e documentos de controle de interface (ICDs).</p>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-02-visiona.jpg" alt="Modelo Estrutural Térmico do SatVHR em pé em um hall de integração, com painéis de arranjo solar e MLI cobre, observado por engenheiros em macacões azuis de sala limpa no INPE/LIT" width="1024" height="624" loading="lazy">
  <figcaption>
    <span class="figure-cap">Modelo Estrutural Térmico (STM) do SatVHR no hall de integração — faces do arranjo solar e MLI cobre visíveis — com a equipe de AIT acompanhando.</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Configuração mecânica que acomode o payload dentro de um orçamento de massa do sistema abaixo de 300 kg.</li>
  <li>Estrutura primária em painéis sanduíche dimensionada para os ambientes de lançamento (voo: faces em CFRP; STM: faces de alumínio sobre honeycomb de alumínio).</li>
  <li>GD&amp;T e acumulação de tolerâncias conforme ISO GPS nos desenhos mecânicos.</li>
  <li>Qualificação por vibração do modelo estrutural–térmico (STM) correlacionada com o FEM.</li>
</ul>
""",
        "approach": """
<p>Layouts e acomodação foram conduzidos em Creo. O trabalho estrutural usou modelos Femap/Nastran para revisões de projeto e troubleshooting; a arquitetura térmica usou Thermal Desktop/SINDA. Relatórios de margem documentaram a postura estrutural e térmica antes das revisões de sistema (PRR, PDR), com CDRs de sistema / estrutura / térmico previstos para o fim de 2026.</p>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-01-visiona.jpg" alt="Close-up do STM do SatVHR mostrando isolamento multicamada cobre e um grande baffle óptico cilíndrico preto sobre uma placa de montagem cinza" width="1024" height="624" loading="lazy">
  <figcaption>
    <span class="figure-cap">Close-up do STM do SatVHR: cobertores MLI cobre e o baffle óptico cilíndrico preto na placa de interface do payload.</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid" data-featured-list>
  <div data-featured="true"><strong>&lt; 300 kg</strong><span>Classe de massa do sistema</span></div>
  <div data-featured="true"><strong>maio 2026</strong><span>Qual. vib. do STM aprovada</span></div>
  <div data-featured="true"><strong>&lt; 1 µm</strong><span>Precisão da medição de jitter</span></div>
</div>
<p>A qualificação por vibração do STM (senoidal, aleatória e sine burst) foi aprovada no INPE/LIT em maio de 2026 e correlacionada com o FEM. O jitter no STM (deslocamento do espelho principal do telescópio sob desbalanceamento de roda de reação) foi medido com precisão melhor que 1 µm.</p>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-03-visiona.jpg" alt="Oito engenheiros em macacões azul-claros de sala limpa posando ao lado do arranjo solar e do hardware do STM do SatVHR em um hangar alto de integração" width="1024" height="624" loading="lazy">
  <figcaption>
    <span class="figure-cap">Equipe de AIT com o hardware do SatVHR na instalação de integração — painel de arranjo solar (esquerda) e hardware do STM (direita).</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
""",
        "mfg_test": """
<p>AIT do STM e campanha de vibração no INPE/LIT. Campanha de vácuo térmico (TVAC) do SATVHR: <strong>ainda não realizada</strong>.</p>
<figure class="case-figure">
  <img src="/assets/img/satvhr/satvhr-pr-2026-05-13.jpg" alt="Engenheiros de jaleco branco inspecionando o STM do SatVHR em um suporte metálico, com MLI cobre e baffle óptico preto, consultando um laptop em sala limpa" width="1280" height="878" loading="lazy">
  <figcaption>
    <span class="figure-cap">Engenheiros inspecionando o STM do SatVHR no suporte de solo durante a campanha de AIT — MLI cobre e baffle óptico à vista.</span>
    <span class="figure-credit">© Visiona Tecnologia Espacial</span>
  </figcaption>
</figure>
""",
        "lessons": "",
        "tools": ["Creo Parametric", "Femap/Nastran", "Thermal Desktop/SINDA", "GD&T / ISO GPS", "MATLAB", "Python"],
    },
    "sgdc-propulsion": {
        "title": "Transferência de tecnologia de propulsão do SGDC",
        "meta": "Thales Alenia Space · Cannes · programa AEB · 2014–2016",
        "summary": (
            "Treinamento on-the-job no subsistema de propulsão bipropelente do SGDC "
            "do Brasil; demonstrou que mais de 16 kg de propelente adicional poderiam "
            "ser carregados, conferindo ~2.5 meses de vida e ~R$ 36M."
        ),
        "tags": ["Cálculos", "Teste", "CAD"],
        "context": """
<p>Selecionado pela Agência Espacial Brasileira (AEB) para o Programa de Absorção de Tecnologia do SGDC na Thales Alenia Space em Cannes: cerca de 5.500 h de treinamento on-the-job em tempo integral no subsistema de propulsão bipropelente do SGDC (tanques, válvulas, linhas, interfaces), desde requisitos e projeto até produção, procedimentos, ensaios e operação.</p>
<figure class="case-figure">
  <img src="/assets/img/sgdc/sgdc-satellite-completed.jpg" alt="Satélite SGDC totalmente montado em sala limpa, com uma grande antena circular, arranjos solares recolhidos e cobertores térmicos dourados e pretos; balões da Thales Alenia Space ao fundo" width="1169" height="780" loading="lazy">
  <figcaption>
    <span class="figure-cap">SGDC (SGDC-1) totalmente montado na sala limpa — antena circular, arranjos solares recolhidos e cobertores MLI visíveis.</span>
    <span class="figure-credit"><a href="https://visionaespacial.com/imprensa/" rel="noopener noreferrer">© Visiona Tecnologia Espacial</a></span>
  </figcaption>
</figure>
""",
        "requirements": """
<ul>
  <li>Compreender e acompanhar o ciclo de vida da propulsão bipropelente sob V&amp;V orientada por ECSS, como trainee no SGDC.</li>
  <li>Avaliar o desempenho da propulsão ao longo da vida (pressão, thrusters, temperatura, medição de propelente), incluindo deformação do tanque sob pressurização quando relevante ao carregamento.</li>
</ul>
""",
        "approach": """
<p>Atuei ao longo do ciclo de vida da propulsão bipropelente com engenheiros da Thales. Demonstrei que mais de 16 kg de propelente adicional poderiam ser carregados no SGDC ao considerar a deformação do tanque sob pressurização.</p>
<figure class="case-figure">
  <img src="/assets/img/sgdc/sgdc-service-module.jpg" alt="Estrutura primária cilíndrica escura do módulo de serviço do SGDC em um suporte branco de montagem, inspecionada por dois técnicos de jaleco de sala limpa da Thales Alenia Space" width="1170" height="780" loading="lazy">
  <figcaption>
    <span class="figure-cap">Estrutura central do módulo de serviço do SGDC no suporte de montagem durante a integração na Thales Alenia Space.</span>
    <span class="figure-credit"><a href="https://visionaespacial.com/imprensa/" rel="noopener noreferrer">© Visiona Tecnologia Espacial</a></span>
  </figcaption>
</figure>
<figure class="case-figure">
  <img src="/assets/img/sgdc/sgdc-payload-module.jpg" alt="Módulo de payload do SGDC aberto em uma estrutura de integração prateada, mostrando chicotes densos e painéis eletrônicos antes do fechamento" width="1170" height="780" loading="lazy">
  <figcaption>
    <span class="figure-cap">Módulo de payload do SGDC em sua estrutura de integração — eletrônica interna e chicotes antes do fechamento dos painéis.</span>
    <span class="figure-credit"><a href="https://visionaespacial.com/imprensa/" rel="noopener noreferrer">© Visiona Tecnologia Espacial</a></span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid" data-featured-list>
  <div data-featured="true"><strong>&gt; 16 kg</strong><span>Propelente adicional</span></div>
  <div data-featured="true"><strong>~2.5 months</strong><span>Vida útil adicional</span></div>
  <div data-featured="true"><strong>~R$ 36M</strong><span>Valor da extensão de vida demonstrado</span></div>
</div>
<p>A AEB reconheceu posteriormente o método de carregamento de propelente que estende a vida útil do SGDC (mar. 2017). Acompanhei ensaios relacionados à propulsão do SGDC em Cannes como trainee.</p>
<figure class="case-figure">
  <img src="/assets/img/sgdc/sgdc-solar-panel-deployment.jpg" alt="Asa de arranjo solar do SGDC totalmente estendida em uma sala limpa branca, acoplada ao corpo do satélite coberto com MLI prata e ouro" width="1169" height="780" loading="lazy">
  <figcaption>
    <span class="figure-cap">Asa de arranjo solar do SGDC totalmente desdobrada durante ensaio em solo na sala limpa.</span>
    <span class="figure-credit"><a href="https://visionaespacial.com/imprensa/" rel="noopener noreferrer">© Visiona Tecnologia Espacial</a></span>
  </figcaption>
</figure>
""",
        "mfg_test": """
<p>As fotografias de imprensa abaixo são da galeria pública de montagem, integração e ensaio do SGDC da Visiona (instalações da Thales Alenia Space). Os ensaios de propulsão foram acompanhados em Cannes durante o programa de transferência de tecnologia.</p>
""",
        "lessons": "",
        "tools": [
            "V&amp;V do subsistema de propulsão",
            "ECSS (adaptada)",
            "Análise de medição / carregamento de propelente",
        ],
    },
    "vcub1-assembly": {
        "title": "Montagem final de voo do VCUB1",
        "meta": "Visiona · CubeSat de 12 kg · Falcon 9 Transporter-7 · 2023",
        "summary": (
            "Montagem final de voo do CubeSat VCUB1 de 12 kg, incluindo vibração "
            "delta e verificações de desdobramento dos painéis solares antes do "
            "lançamento no Falcon 9."
        ),
        "tags": ["CAD", "Teste", "Manufatura aditiva"],
        "context": """
<p>O VCUB1 é um CubeSat de 12 kg lançado no Falcon 9 (SpaceX Transporter-7, abril de 2023) e operado em órbita. No início de 2023 apoiei a integração final e realizei a montagem final de voo.</p>
""",
        "requirements": """
<ul>
  <li>Concluir a montagem de voo com procedimentos controlados para painéis solares e interfaces do deployer.</li>
  <li>Vibração delta e verificação de desdobramento dos painéis solares antes do lançamento.</li>
  <li>Fit-check dos trilhos do deployer 6U e prontidão do ferramental de integração para o Falcon 9.</li>
</ul>
""",
        "approach": """
<p>Revisei o procedimento de montagem dos painéis solares, executei ensaios de vibração delta e de desdobramento, realizei o fit-check dos trilhos do deployer 6U, revisei dados de ensaio de qualificação e preparei o ferramental de integração para o lançamento.</p>

<figure class="case-figure">
  <img src="/assets/img/vcub1/vcub1-nanosats.jpg" alt="CubeSat VCUB1 com duas asas de painéis solares totalmente desdobradas, apoiado em um suporte branco em laboratório" width="1200" height="800" loading="lazy">
  <figcaption>
    <span class="figure-cap">VCUB1 com painéis solares desdobrados em suporte de laboratório — barramento central com abertura circular de antena/sensor e células montadas no corpo entre as asas.</span>
    <span class="figure-credit"><a href="https://www.nanosats.eu/sat/vcub1" rel="noopener noreferrer">Image: nanosats.eu</a></span>
  </figcaption>
</figure>
""",
        "results": """
<div class="results-grid" data-featured-list>
  <div data-featured="true"><strong>12 kg</strong><span>Massa do CubeSat</span></div>
  <div data-featured="true"><strong>abr. 2023</strong><span>Lançamento Transporter-7</span></div>
  <div data-featured="true"><strong>IAC 2024</strong><span>Artigo da campanha TVAC</span></div>
</div>
<p>O satélite operou em órbita após o lançamento. Coautor do artigo IAC 2024 sobre a campanha de ensaio de vácuo térmico do VCUB1 (IAC-24-B4.IP.21).</p>
""",
        "mfg_test": """
<p>Vibração delta, desdobramento dos painéis solares, fit-check do deployer e a campanha TVAC documentada no artigo IAC 2024. Nenhum conjunto de dados confidencial da Visiona/Thales é mostrado aqui.</p>
""",
        "lessons": "",
        "tools": ["SolidWorks / Onshape", "Procedimentos de montagem", "Ferramental de AIT"],
    },
    "mgse-lifting": {
        "title": "MGSE de içamento e manuseio — conceito",
        "meta": "Visiona · AIT do STM do SATVHR · liderança de conceito",
        "summary": (
            "Liderei o conceito do MGSE de içamento e manuseio; projeto detalhado e "
            "fabricação por fornecedor subcontratado; ensaiado durante a campanha "
            "de AIT do STM."
        ),
        "tags": ["CAD", "Teste", "Cálculos"],
        "context": """
<p>Era necessário equipamento de suporte em solo para içar e manusear o STM do SATVHR com segurança durante a AIT e a preparação de vibração no INPE/LIT.</p>
""",
        "requirements": """
<ul>
  <li>Interfaces seguras de içamento / manuseio compatíveis com a arquitetura mecânica do STM.</li>
  <li>Projeto detalhado e fabricação entregáveis pelo fornecedor a partir de um pacote de conceito claro.</li>
  <li>Verificação durante a campanha de AIT do STM.</li>
</ul>
""",
        "approach": """
<p><strong>Liderei o conceito</strong>; o projeto detalhado e a fabricação foram executados por um fornecedor subcontratado. O trabalho de conceito cobriu pontos de içamento, envelopes de manuseio e definição de interfaces em relação à configuração do STM.</p>
""",
        "results": """
<p>O MGSE foi fabricado pelo fornecedor e ensaiado durante a campanha de AIT do STM.</p>
""",
        "mfg_test": """
<p>Detalhado e construído por um subcontratado; verificações funcionais/de manuseio durante a AIT do STM. TVAC do satélite: ainda não realizada (separada do MGSE).</p>
""",
        "lessons": "",
        "tools": ["Creo Parametric", "Definição de ICD", "Acompanhamento de fornecedor"],
    },
    "mhd-reaction-wheel": {
        "title": "Roda de reação de fluido magnético MHD",
        "meta": "Dissertação de M.Sc. no ITA · em andamento · 2025–2027",
        "summary": (
            "Dissertação de M.Sc. no ITA: desenvolvimento de uma roda de reação de "
            "fluido magnético magnetohidrodinâmica (MHD) para controle de atitude "
            "de CubeSat."
        ),
        "tags": ["CAD", "Cálculos", "Teste", "Manufatura aditiva"],
        "context": """
<p>Pesquisa de mestrado no Instituto Tecnológico de Aeronáutica (ITA), programa EAM-1 — Projeto Aeronáutico, Estruturas e Sistemas Aeroespaciais. Orientador: Prof. Tiago de Paula. Conclusão prevista para julho de 2027.</p>
""",
        "requirements": """
<ul>
  <li>Função de roda de reação usando um fluido magnético sob atuação MHD, dimensionada para controle de atitude de CubeSat.</li>
</ul>
""",
        "approach": """
<p>Trabalho de dissertação em andamento sobre modelagem e desenvolvimento de protótipo de uma roda de reação de fluido magnético. Detalhe técnico público será acrescentado conforme os resultados forem liberados para divulgação.</p>
""",
        "results": """
<p>Pesquisa em andamento (conclusão prevista para julho de 2027). Figuras de desempenho medidas ainda não são publicadas aqui.</p>
""",
        "mfg_test": "",
        "lessons": "",
        "tools": ["Creo / CAD", "MATLAB", "Python", "Instrumentação de laboratório"],
    },
    "additive-manufacturing": {
        "title": "Projetos de impressão 3D",
        "meta": "Pessoal / hardware de apoio · AM",
        "summary": "Trabalho de manufatura aditiva para dispositivos, protótipos e hardware de apoio.",
        "tags": ["Manufatura aditiva", "CAD", "Teste"],
        "context": """
<p>Hardware de apoio e protótipos produzidos com métodos de manufatura aditiva, em paralelo a competências de usinagem convencional.</p>
""",
        "requirements": "",
        "approach": """
<p>Formação prática em CNC / CAM (curso SENAI de usinagem aeroespacial, 120 h) complementa a prototipagem FDM/AM para suporte em solo e hardware de conceito.</p>
""",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": ["Onshape / SolidWorks / Creo", "FDM", "CAM / CNC"],
    },
    "unb-hybrid-rocket": {
        "title": "Bancada de ensaio estático de foguete híbrido da UnB",
        "meta": "Universidade de Brasília · pesquisa · 2012–2013",
        "summary": (
            "Pesquisa voluntária em bancadas de ensaio estático de foguetes híbridos "
            "na UnB; publicação relacionada no 19º Congresso de Iniciação Científica "
            "da UnB (2013)."
        ),
        "tags": ["CAD", "Teste", "Cálculos"],
        "context": """
<p>Durante a graduação em Engenharia Mecânica na Universidade de Brasília, atuei como pesquisador voluntário em bancadas de ensaio estático de foguetes híbridos (mar. 2012 – jun. 2013). Extracurriculares relacionados: Apuama Racing (Formula SAE) e N-Prize.</p>
""",
        "requirements": """
<ul>
  <li>Bancada experimental que permita o ensaio estático de motores-foguete híbridos.</li>
</ul>
""",
        "approach": """
<p>Projeto de uma bancada experimental para ensaios de propulsão híbrida (documentado no artigo do Congresso de Iniciação Científica da UnB de 2013). Trabalho posterior de CFD em um atomizador pressure-swirl apareceu no CILAMCE 2016 (ANSYS CFX).</p>
""",
        "results": """
<p>Publicado: Cassiano, E. (2013). <em>Projeto de uma Bancada Experimental para o Teste de Motores Foguetes com Propulsão Híbrida</em>. 19º Congresso de Iniciação Científica da UnB.</p>
""",
        "mfg_test": "",
        "lessons": "",
        "tools": ["SolidWorks", "Instrumentação de ensaio", "ANSYS CFX (CFD relacionado)"],
    },
    "pulse-jet-dust-filter": {
        "title": "Filtro de coleta de pó tipo baghouse com pulse-jet",
        "meta": "Mecânico · industrial",
        "summary": "Filtro de coleta de pó tipo pulse-jet / baghouse.",
        "tags": ["CAD", "Fabricação"],
        "context": """
<p>Filtro de coleta de pó tipo pulse-jet / baghouse.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "educational-rocket-model": {
        "title": "Modelo educacional de foguete",
        "meta": "Aeroespacial · foguetaria",
        "summary": "Modelo educacional de foguete.",
        "tags": ["CAD", "Teste"],
        "context": """
<p>Modelo educacional de foguete.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "co2-nose-cone-ejector": {
        "title": "Ejetor de ogiva a CO2",
        "meta": "Aeroespacial · foguetaria",
        "summary": "Ejetor de ogiva a CO2 para um foguete.",
        "tags": ["CAD", "Teste"],
        "context": """
<p>Ejetor de ogiva a CO2 para um foguete.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "side-ejecting-parachute": {
        "title": "Sistema de paraquedas de ejeção lateral para foguete",
        "meta": "Aeroespacial · foguetaria",
        "summary": "Sistema de paraquedas de ejeção lateral para um foguete.",
        "tags": ["CAD", "Teste"],
        "context": """
<p>Sistema de paraquedas de ejeção lateral para um foguete.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "cloud-seeding-rocket": {
        "title": "Foguete de semeadura de nuvens",
        "meta": "Aeroespacial · foguetaria",
        "summary": "Foguete de semeadura de nuvens.",
        "tags": ["CAD", "Teste"],
        "context": """
<p>Foguete de semeadura de nuvens.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "omega-power-flywheel": {
        "title": "Armazenamento de energia por volante Omega Power",
        "meta": "Mecânico · energia",
        "summary": "Volante Omega Power para armazenamento de energia.",
        "tags": ["CAD", "Energia"],
        "context": """
<p>Volante Omega Power para armazenamento de energia.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "truck-antenna-mount": {
        "title": "Suporte de antena para caminhão",
        "meta": "Mecânico · industrial",
        "summary": "Suporte de antena para caminhões.",
        "tags": ["CAD", "Fabricação"],
        "context": """
<p>Suporte de antena para caminhões.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "compact-antennas": {
        "title": "Projeto estrutural e térmico de antenas compactas",
        "meta": "Mecânico · antenas",
        "summary": "Projeto estrutural e térmico de antenas compactas.",
        "tags": ["CAD", "Térmico", "FEA"],
        "context": """
<p>Projeto estrutural e térmico de antenas compactas.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "rua-dois-system": {
        "title": "Sistema e aplicativo Rua Dois",
        "meta": "Software · Rua Dois",
        "summary": "Sistema e aplicativo Rua Dois.",
        "tags": ["Software"],
        "context": """
<p>Sistema e aplicativo Rua Dois.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "civ-system": {
        "title": "Sistema CIV",
        "meta": "Software · CIV",
        "summary": "Sistema CIV.",
        "tags": ["Software"],
        "context": """
<p>Sistema CIV.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
    "comida-verificada": {
        "title": "Plataforma de verificação de alimentos Comida Verificada (CoV)",
        "meta": "Software · organização sem fins lucrativos",
        "summary": "Comida Verificada (CoV), plataforma sem fins lucrativos de verificação de alimentos.",
        "tags": ["Software"],
        "context": """
<p>Comida Verificada (CoV), plataforma sem fins lucrativos de verificação de alimentos.</p>
""",
        "requirements": "",
        "approach": "",
        "results": "",
        "mfg_test": "",
        "lessons": "",
        "tools": [],
    },
}

PT_MEDIA_SECTIONS = {
    "sgdc-propulsion": """
      <section id="in-the-media">
        <h2>Na mídia</h2>
        <div class="project-media">
          <ul>
            <li><a href="https://www.gov.br/aeb/pt-br/assuntos/noticias/engenheiro-da-aeb-desenvolve-metodo-que-aumenta-tempo-de-vida-do-sgdc" target="_blank" rel="noopener noreferrer">AEB (2017-03-23)</a> - método de carregamento de tanque que estende a vida do SGDC. <span class="media-badge">Menciona Erlan</span></li>
            <li><a href="https://www.defesanet.com.br/defesa/sgdc-chega-a-posicao-definitiva-ate-sabado/" target="_blank" rel="noopener noreferrer">DefesaNet (2017-05-05)</a> - contribuições de engenheiros da AEB, incluindo extensão de vida. <span class="media-badge">Menciona Erlan</span></li>
          </ul>
          <a class="media-more" href="/media/#sgdc">Toda a cobertura de SGDC →</a>
        </div>
      </section>
""",
    "satvhr-stm": """
      <section id="in-the-media">
        <h2>Na mídia</h2>
        <div class="project-media">
          <ul>
            <li><a href="https://telesintese.com.br/satelite-brasileiro-satvhr-conclui-teste-critico-de-vibracao-para-lancamento/" target="_blank" rel="noopener noreferrer">Telesíntese (2026-05-13)</a> - ensaio de vibração do STM no INPE/LIT.</li>
            <li><a href="https://visionaespacial.com/2026-05-13-visiona-conclui-com-sucesso-teste-critico-de-desenvolvimento-do-satelite-satvhr/" target="_blank" rel="noopener noreferrer">Visiona (2026-05-13)</a> - release oficial da campanha de vibração do STM.</li>
            <li><a href="https://fiesc.com.br/pt-br/imprensa/senaisc-integra-projeto-premiado-com-maior-grau-de-conteudo-nacional-da-historia-espacial" target="_blank" rel="noopener noreferrer">FIESC/SENAI-SC (2026-03-19)</a> - SatVHR vence o Prêmio FINEP de Inovação 2025.</li>
          </ul>
          <a class="media-more" href="/media/#satvhr">Toda a cobertura de SATVHR →</a>
        </div>
      </section>
""",
    "vcub1-assembly": """
      <section id="in-the-media">
        <h2>Na mídia</h2>
        <div class="project-media">
          <ul>
            <li><a href="https://pesquisaparainovacao.fapesp.br/primeiro_satelite_de_observacao_da_terra_e_coleta_de_dados_projetado_pela_industria_nacional_e_lancado_nos_eua/2703" target="_blank" rel="noopener noreferrer">FAPESP (2023-04-15)</a> - cobertura do lançamento do VCUB1.</li>
            <li><a href="https://visionaespacial.com/visiona-comemora-um-ano-do-lancamento-do-satelite-vcub1/" target="_blank" rel="noopener noreferrer">Visiona (2024-04-15)</a> - um ano em órbita.</li>
          </ul>
          <a class="media-more" href="/media/#vcub1">Toda a cobertura de VCUB1 →</a>
        </div>
      </section>
""",
}
