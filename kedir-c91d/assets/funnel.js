/* Dialed funnel behaviour: reveals, ring countdown, opt-in modal, lite YouTube facade. */
(function () {
  var doc = document.documentElement;
  doc.classList.add("js");
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* reveals */
  var els = document.querySelectorAll(".reveal");
  if (reduced || !("IntersectionObserver" in window)) {
    els.forEach(function (e) { e.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    els.forEach(function (e) { io.observe(e); });
  }

  /* next webinar: Thursday 8pm New York time */
  function nextThursday() {
    var now = new Date();
    var t = new Date(now);
    t.setUTCHours(1, 0, 0, 0); /* 20:00 EST = 01:00 UTC next day */
    var day = t.getUTCDay(); /* Friday UTC = Thursday evening ET */
    var add = (5 - day + 7) % 7;
    t.setUTCDate(t.getUTCDate() + add);
    if (t <= now) t.setUTCDate(t.getUTCDate() + 7);
    return t;
  }
  var target = nextThursday();
  document.querySelectorAll("[data-webinar-date]").forEach(function (el) {
    el.textContent = target.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric", timeZone: "America/New_York" });
  });

  /* ring countdown */
  var cd = document.querySelector(".countdown");
  if (cd) {
    var units = { d: [86400, 7], h: [3600, 24], m: [60, 60], s: [1, 60] };
    var C = 301.6;
    var tick = function () {
      var diff = Math.max(0, Math.floor((target - Date.now()) / 1000));
      Object.keys(units).forEach(function (k) {
        var u = cd.querySelector('[data-u="' + k + '"]');
        if (!u) return;
        var val = Math.floor(diff / units[k][0]) % (k === "d" ? 1000 : units[k][1]);
        u.querySelector(".cd-num").textContent = (val < 10 ? "0" : "") + val;
        u.querySelector(".arc").style.strokeDashoffset = C * (1 - Math.min(1, val / units[k][1]));
      });
    };
    tick(); setInterval(tick, 1000);
  }

  /* opt-in modal */
  var modal = document.getElementById("optinModal");
  if (modal) {
    var form = document.getElementById("optinForm");
    var nameI = document.getElementById("optinName");
    var emailI = document.getElementById("optinEmail");
    var err = document.getElementById("optinErr");
    var last = null;
    var open = function (e) { if (e) e.preventDefault(); last = document.activeElement; modal.classList.add("open"); document.body.style.overflow = "hidden"; setTimeout(function () { nameI.focus(); }, 60); };
    var close = function () { modal.classList.remove("open"); document.body.style.overflow = ""; if (last && last.focus) last.focus(); };
    document.querySelectorAll("[data-open-modal]").forEach(function (b) { b.addEventListener("click", open); });
    document.getElementById("modalClose").addEventListener("click", close);
    modal.addEventListener("click", function (e) { if (e.target === modal) close(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("open")) close(); });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      nameI.classList.remove("err"); emailI.classList.remove("err"); err.textContent = "";
      if (!nameI.value.trim()) { nameI.classList.add("err"); err.textContent = "Add your name to save your seat."; nameI.focus(); return; }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailI.value.trim())) { emailI.classList.add("err"); err.textContent = "That email doesn't look right."; emailI.focus(); return; }
      window.location.href = form.getAttribute("data-next") || "../thank-you/index.html";
    });
  }

  /* lite YouTube: thumbnail until clicked, then the real player */
  document.querySelectorAll("[data-yt]").forEach(function (b) {
    b.addEventListener("click", function () {
      var id = b.getAttribute("data-yt");
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      f.allow = "autoplay; encrypted-media; picture-in-picture";
      f.allowFullscreen = true;
      f.title = b.getAttribute("aria-label") || "Video";
      b.appendChild(f);
    }, { once: true });
  });
})();
