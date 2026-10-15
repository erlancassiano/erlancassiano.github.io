(function () {
  const root = document.documentElement;
  const stored = localStorage.getItem("theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const initial = stored || (prefersDark ? "dark" : "light");
  root.setAttribute("data-theme", initial);

  const themeBtn = document.querySelector("[data-theme-toggle]");
  if (themeBtn) {
    const sync = () => {
      const dark = root.getAttribute("data-theme") === "dark";
      themeBtn.setAttribute("aria-pressed", String(dark));
      themeBtn.textContent = dark ? "☀" : "☾";
      themeBtn.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
      themeBtn.title = dark ? "Switch to light theme" : "Switch to dark theme";
    };
    sync();
    themeBtn.addEventListener("click", () => {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      sync();
    });
  }

  const menuBtn = document.querySelector("[data-menu-toggle]");
  const navLinks = document.querySelector("[data-nav-links]");
  if (menuBtn && navLinks) {
    menuBtn.addEventListener("click", () => {
      const open = navLinks.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", String(open));
    });
    navLinks.querySelectorAll("a").forEach((a) => {
      a.addEventListener("click", () => {
        navLinks.classList.remove("open");
        menuBtn.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Year
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });

  // Featured lists: show featured items only; "See more" reveals the rest.
  // No-JS and print show everything (CSS gate is html.js-featured).
  document.querySelectorAll("[data-featured-list]").forEach((list, index) => {
    const extras = list.querySelectorAll(':scope > [data-featured="false"]');
    if (!extras.length) return;

    if (!list.id) {
      list.id = "featured-list-" + String(index + 1);
    }

    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "featured-toggle";
    btn.setAttribute("aria-expanded", "false");
    btn.setAttribute("aria-controls", list.id);
    const moreLabel = list.getAttribute("data-more-label") || "See more";
    const lessLabel = list.getAttribute("data-less-label") || "See less";
    btn.textContent = moreLabel;

    btn.addEventListener("click", () => {
      const expanded = list.classList.toggle("is-expanded");
      btn.setAttribute("aria-expanded", String(expanded));
      btn.textContent = expanded ? lessLabel : moreLabel;
    });

    list.insertAdjacentElement("afterend", btn);
  });

  document.documentElement.classList.add("js-featured");
})();
