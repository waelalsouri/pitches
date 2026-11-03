/* Muslim Sales Accelerator · shared funnel behaviour (reveal, countdown, opt-in modal) */
(function () {
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -8% 0px" }) : null;
  document.querySelectorAll(".reveal").forEach(function (el, i) {
    el.style.transitionDelay = (Math.min(i % 4, 3) * 70) + "ms";
    io ? io.observe(el) : el.classList.add("in");
  });
})();

(function () {
  var cd = document.querySelector(".countdown"); if (!cd) return;
  var t = new Date(cd.getAttribute("data-target"));
  if (isNaN(t.getTime()) || t < Date.now()) t = new Date(Date.now() + 3 * 864e5 + 5 * 36e5);
  var u = { d: cd.querySelector("[data-u=d]"), h: cd.querySelector("[data-u=h]"), m: cd.querySelector("[data-u=m]"), s: cd.querySelector("[data-u=s]") };
  function p(n) { return n < 10 ? "0" + n : "" + n; }
  function tick() {
    var x = Math.max(0, Math.floor((t - Date.now()) / 1000));
    var d = Math.floor(x / 86400); x -= d * 86400; var h = Math.floor(x / 3600); x -= h * 3600; var m = Math.floor(x / 60), s = x - m * 60;
    [[u.d, d, 30], [u.h, h, 24], [u.m, m, 60], [u.s, s, 60]].forEach(function (a) {
      if (!a[0]) return; a[0].textContent = p(a[1]); a[0].parentNode.style.setProperty("--p", (a[1] / a[2] * 100) + "%");
    });
  }
  tick(); setInterval(tick, 1000);
})();

(function () {
  var modal = document.getElementById("optinModal"); if (!modal) return;
  var form = document.getElementById("optinForm"), n = document.getElementById("optinName"), em = document.getElementById("optinEmail"), err = document.getElementById("optinErr"), last;
  function open(e) { if (e) e.preventDefault(); last = document.activeElement; modal.classList.add("open"); document.body.style.overflow = "hidden"; setTimeout(function () { n.focus(); }, 60); }
  function close() { modal.classList.remove("open"); document.body.style.overflow = ""; if (last && last.focus) last.focus(); }
  document.querySelectorAll("[data-open-modal]").forEach(function (b) { b.addEventListener("click", open); });
  document.getElementById("modalClose").addEventListener("click", close);
  modal.addEventListener("click", function (e) { if (e.target === modal) close(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("open")) close(); });
  form.addEventListener("submit", function (e) {
    e.preventDefault(); n.classList.remove("err"); em.classList.remove("err"); err.textContent = "";
    if (!n.value.trim()) { n.classList.add("err"); err.textContent = "Please enter your name."; return n.focus(); }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value.trim())) { em.classList.add("err"); err.textContent = "Please enter a valid email."; return em.focus(); }
    location.href = "../thank-you/";
  });
})();
