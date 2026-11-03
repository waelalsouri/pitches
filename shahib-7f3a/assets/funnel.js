/* MF funnel: reveals, story-video modal, and the application popup.
   Application routing: qualified -> booking (MF Consultation Call) -> thank-you.
   Not qualified -> MF Personalised (£49) downsell. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* reveals */
  var els = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("is-in"); }); }
  else {
    var io = new IntersectionObserver(function (en, o) {
      en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("is-in"); o.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    els.forEach(function (e) { io.observe(e); });
  }

  function lock(on) { document.body.style.overflow = on ? "hidden" : ""; }

  /* story-video modal */
  var vm = document.getElementById("vmodal");
  if (vm) {
    var fr = document.getElementById("vmodal-frame");
    var closeV = function () { vm.classList.remove("open"); lock(false); setTimeout(function () { fr.innerHTML = ""; }, 300); };
    document.querySelectorAll("[data-yt]").forEach(function (b) {
      b.addEventListener("click", function () {
        fr.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + b.getAttribute("data-yt") +
          '?autoplay=1&rel=0&playsinline=1" title="Video" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>';
        vm.classList.add("open"); lock(true);
      });
    });
    document.getElementById("vmodal-close").addEventListener("click", closeV);
    vm.addEventListener("click", function (e) { if (e.target === vm) closeV(); });
  }

  /* application popup */
  var ap = document.getElementById("apply");
  if (!ap) return;
  var qs = Array.prototype.slice.call(ap.querySelectorAll(".q"));
  var total = ap.querySelectorAll(".q[data-count]").length;
  var bar = ap.querySelector(".apply__bar i");
  var countEl = ap.querySelector(".apply__count");
  var answers = {};
  var idx = 0;

  function show(i) {
    idx = i;
    qs.forEach(function (q, n) { q.classList.toggle("on", n === i); });
    var q = qs[i];
    var c = q.getAttribute("data-count");
    if (c) { countEl.textContent = "Question " + c + " of " + total; countEl.hidden = false; bar.style.width = ((c - 1) / total * 100) + "%"; }
    else { countEl.hidden = true; bar.style.width = "100%"; }
    var f = q.querySelector("input"); if (f) setTimeout(function () { f.focus(); }, 60);
  }
  function byId(id) { for (var n = 0; n < qs.length; n++) if (qs[n].id === id) return n; return -1; }
  function next() {
    var q = qs[idx];
    var inputs = q.querySelectorAll("input[required]");
    for (var n = 0; n < inputs.length; n++) { if (!inputs[n].value || !inputs[n].checkValidity()) { inputs[n].focus(); if (inputs[n].reportValidity) inputs[n].reportValidity(); return; } }
    q.querySelectorAll("input").forEach(function (f) { answers[f.name] = f.value; });
    var c = +q.getAttribute("data-count");
    if (c === total) { route(); return; }
    show(idx + 1);
  }
  function route() {
    // qualify: 110kg+ territory, ready to invest. Everyone else gets the £49 plan.
    var ok = answers.weight !== "under" && answers.invest === "yes";
    show(byId(ok ? "q-book" : "q-down"));
  }

  ap.querySelectorAll(".opt").forEach(function (o) {
    o.addEventListener("click", function () {
      var q = o.closest(".q");
      q.querySelectorAll(".opt").forEach(function (x) { x.classList.remove("sel"); });
      o.classList.add("sel");
      answers[q.getAttribute("data-key")] = o.getAttribute("data-v");
      setTimeout(next, reduce ? 0 : 260);
    });
  });
  ap.querySelectorAll("[data-next]").forEach(function (b) { b.addEventListener("click", next); });
  ap.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && e.target.tagName === "INPUT") { e.preventDefault(); next(); }
    var q = qs[idx]; var opts = q.querySelectorAll(".opt");
    var k = e.key.toUpperCase().charCodeAt(0) - 65;
    if (opts.length && e.target.tagName !== "INPUT" && k >= 0 && k < opts.length && e.key.length === 1) opts[k].click();
  });

  /* faux booking calendar */
  ap.querySelectorAll(".calmock__days button, .calmock__times button").forEach(function (b) {
    b.addEventListener("click", function () {
      b.parentNode.querySelectorAll("button").forEach(function (x) { x.classList.remove("sel"); });
      b.classList.add("sel");
      if (b.parentNode.classList.contains("calmock__times")) setTimeout(function () { location.href = "../thank-you/"; }, reduce ? 0 : 450);
    });
  });

  function open() { ap.classList.add("open"); ap.setAttribute("aria-hidden", "false"); lock(true); show(0); }
  function close() { ap.classList.remove("open"); ap.setAttribute("aria-hidden", "true"); lock(false); }
  document.querySelectorAll("[data-apply]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); open(); }); });
  ap.querySelector(".apply__close").addEventListener("click", close);
  ap.addEventListener("click", function (e) { if (e.target === ap) close(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { close(); if (vm) vm.click(); } });
})();
