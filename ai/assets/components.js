/* ==========================================================================
   AI Engineer Course — shared interactive components
   Include at the end of <body>:  <script src="../assets/components.js"></script>

   Components (all declarative — write HTML, this file wires it up):

   1. Copy buttons     every <pre> gets a "copy" button (skip with class="no-copy").
                       Elements with class="p" (shell prompts) are excluded from the copy.

   2. Multiple choice  <div class="quiz">
                         <p class="q">Question?</p>
                         <div class="options">
                           <button class="opt">answer one</button>
                           <button class="opt" data-correct>answer two</button>
                         </div>
                         <div class="explain">Why.</div>
                       </div>
                       Options are shuffled on load. Keep every option the same length.

   3. Predict output   <div class="quiz predict" data-expect="0||zero">
                         <p class="q">What does this print?</p>
                         <pre>...</pre>
                         <div class="explain">Why.</div>
                       </div>
                       Input row is generated. Answers compared trimmed, case-insensitive,
                       quotes normalised; alternatives separated by "||".

   4. Steps checklist  <ol class="steps" data-key="unique-key"><li>...</li></ol>
                       Adds a "done" tick to each step; remembered per browser.

   5. Score            <p class="score"></p>  shows first-try score for quizzes on the page.

   6. Theme toggle     auto / light / dark, remembered per browser.
   ========================================================================== */
(function () {
  "use strict";

  // ---------- safe storage (private windows / file:// may throw) ----------
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (_) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (_) { /* ignore */ } },
  };

  // ---------- 1. copy buttons ----------
  document.querySelectorAll("pre:not(.no-copy)").forEach((pre) => {
    if (pre.closest(".predict")) return; // don't give away predict answers
    const btn = document.createElement("button");
    btn.className = "copy-btn";
    btn.type = "button";
    btn.textContent = "copy";
    btn.addEventListener("click", async () => {
      const clone = pre.cloneNode(true);
      clone.querySelectorAll(".p, .copy-btn").forEach((n) => n.remove());
      try {
        await navigator.clipboard.writeText(clone.textContent.replace(/^\n+|\n+$/g, ""));
        btn.textContent = "copied";
      } catch (_) {
        btn.textContent = "select & copy";
      }
      setTimeout(() => (btn.textContent = "copy"), 1500);
    });
    pre.appendChild(btn);
  });

  // ---------- score tracking ----------
  const scoreEl = document.querySelector(".score");
  const quizzes = document.querySelectorAll(".quiz");
  let answered = 0;
  let firstTry = 0;
  function updateScore() {
    if (!scoreEl) return;
    scoreEl.textContent = answered === quizzes.length
      ? `First-try score: ${firstTry} / ${quizzes.length}. ` +
        (firstTry === quizzes.length
          ? "Clean sweep. Come back in a few days and see if it still holds."
          : "Revisit the ones you missed tomorrow; the struggle is what makes it stick.")
      : `Answered ${answered} / ${quizzes.length}`;
  }

  function showExplain(quiz, good, lead, withExplain = true) {
    let fb = quiz.querySelector(".feedback");
    const explain = quiz.querySelector(".explain");
    if (!fb) {
      fb = document.createElement("div");
      fb.className = "feedback";
      quiz.appendChild(fb);
    }
    fb.innerHTML = "";
    const v = document.createElement("div");
    v.className = "verdict " + (good ? "good" : "bad");
    v.textContent = lead;
    fb.appendChild(v);
    if (explain && withExplain) {
      explain.hidden = false;
      fb.appendChild(explain);
    }
  }

  function record(quiz, correctFirst) {
    if (quiz.dataset.done) return;
    quiz.dataset.done = "1";
    answered += 1;
    if (correctFirst) firstTry += 1;
    updateScore();
  }

  // ---------- 2. multiple choice ----------
  document.querySelectorAll(".quiz:not(.predict)").forEach((quiz) => {
    const explain = quiz.querySelector(".explain");
    if (explain) explain.hidden = true;
    const box = quiz.querySelector(".options");
    const opts = Array.from(box.querySelectorAll("button.opt"));
    // shuffle so position never hints at the answer
    for (let i = opts.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [opts[i], opts[j]] = [opts[j], opts[i]];
    }
    opts.forEach((o) => { o.type = "button"; box.appendChild(o); });

    opts.forEach((o) => {
      o.addEventListener("click", () => {
        const good = o.hasAttribute("data-correct");
        record(quiz, good);
        opts.forEach((x) => {
          x.disabled = true;
          if (x.hasAttribute("data-correct")) x.classList.add("correct");
        });
        if (!good) o.classList.add("wrong");
        showExplain(quiz, good, good ? "Correct." : "Not quite.");
      });
    });
  });

  // ---------- 3. predict the output ----------
  const norm = (s) => s.trim().replace(/[“”‘’]/g, "'").replace(/"/g, "'").replace(/\s+/g, " ").toLowerCase();
  document.querySelectorAll(".quiz.predict").forEach((quiz) => {
    const explain = quiz.querySelector(".explain");
    if (explain) explain.hidden = true;
    const expected = (quiz.dataset.expect || "").split("||").map(norm);
    const row = document.createElement("div");
    row.className = "row";
    row.innerHTML =
      '<input type="text" spellcheck="false" autocomplete="off" aria-label="Your answer" placeholder="type what gets printed">' +
      '<button type="button" class="btn">Check</button>' +
      '<button type="button" class="btn ghost">Show answer</button>';
    (explain || quiz.lastElementChild).before(row);
    const [input, check, reveal] = row.children;
    let tries = 0;

    function finish(good, lead) {
      input.disabled = check.disabled = reveal.disabled = true;
      showExplain(quiz, good, lead);
    }
    check.addEventListener("click", () => {
      if (!input.value.trim()) return;
      tries += 1;
      if (expected.includes(norm(input.value))) {
        record(quiz, tries === 1);
        finish(true, tries === 1 ? "Correct." : "Correct, second time round.");
      } else if (tries < 2) {
        showExplain(quiz, false, "Not quite. Trace it line by line and try once more.", false);
      } else {
        record(quiz, false);
        finish(false, `Answer: ${quiz.dataset.expect.split("||")[0]}`);
      }
    });
    input.addEventListener("keydown", (e) => { if (e.key === "Enter") check.click(); });
    reveal.addEventListener("click", () => {
      record(quiz, false);
      finish(false, `Answer: ${quiz.dataset.expect.split("||")[0]}`);
    });
  });
  updateScore();

  // ---------- 4. steps checklist ----------
  document.querySelectorAll("ol.steps[data-key]").forEach((ol) => {
    const key = "steps:" + ol.dataset.key;
    let saved = [];
    try { saved = JSON.parse(store.get(key) || "[]"); } catch (_) { saved = []; }
    Array.from(ol.children).forEach((li, i) => {
      const label = document.createElement("label");
      label.className = "tick";
      label.innerHTML = '<input type="checkbox"> done';
      const box = label.firstChild;
      box.checked = saved.includes(i);
      li.classList.toggle("done", box.checked);
      box.addEventListener("change", () => {
        li.classList.toggle("done", box.checked);
        const now = Array.from(ol.children)
          .map((x, j) => (x.classList.contains("done") ? j : -1))
          .filter((j) => j >= 0);
        store.set(key, JSON.stringify(now));
      });
      li.appendChild(label);
    });
  });

  // ---------- 6. theme toggle ----------
  const root = document.documentElement;
  const modes = ["auto", "light", "dark"];
  let mode = store.get("theme") || "auto";
  const apply = () => {
    if (mode === "auto") root.removeAttribute("data-theme");
    else root.setAttribute("data-theme", mode);
  };
  apply();
  const tbtn = document.createElement("button");
  tbtn.className = "theme-toggle";
  tbtn.type = "button";
  tbtn.textContent = "theme: " + mode;
  tbtn.addEventListener("click", () => {
    mode = modes[(modes.indexOf(mode) + 1) % modes.length];
    store.set("theme", mode);
    apply();
    tbtn.textContent = "theme: " + mode;
  });
  document.body.appendChild(tbtn);
})();
