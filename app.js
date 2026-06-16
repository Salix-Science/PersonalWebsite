  // ---- Mode selector ----
  (function(){
    var btns = Array.prototype.slice.call(document.querySelectorAll('.modebtn'));
    function apply(mode){
      document.documentElement.setAttribute('data-theme', mode);
      btns.forEach(function(b){ b.setAttribute('aria-pressed', String(b.dataset.mode === mode)); });
      try{ localStorage.setItem('willow-theme', mode); }catch(e){}
    }
    var current = document.documentElement.getAttribute('data-theme') || 'light';
    apply(current);
    btns.forEach(function(b){ b.addEventListener('click', function(){ apply(b.dataset.mode); }); });
  })();

  // ---- Scrollspy: highlight the nav tab for the section in view ----
  (function(){
    var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
    function tabFor(id){ return tabs.find(function(t){ return t.getAttribute('href') === '#'+id; }); }
    var spy = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(en.isIntersecting){
          tabs.forEach(function(t){ t.classList.remove('active'); });
          var t = tabFor(en.target.id);
          if(t) t.classList.add('active');
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    document.querySelectorAll('main section[id]').forEach(function(s){ spy.observe(s); });
  })();

  // ---- Gentle scroll reveal (skipped under reduced-motion) ----
  (function(){
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var items = document.querySelectorAll('.rise');
    if(reduce || !('IntersectionObserver' in window)){
      items.forEach(function(el){ el.classList.add('in'); });
      return;
    }
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function(el){ io.observe(el); });
  })();

// ---- Back to top ----
(function(){
  var btn = document.querySelector('.to-top');
  if(!btn) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function onScroll(){
    if(window.pageYOffset > 400) btn.classList.add('show');
    else btn.classList.remove('show');
  }
  window.addEventListener('scroll', onScroll, {passive:true});
  onScroll();
  btn.addEventListener('click', function(){
    window.scrollTo({ top:0, behavior: reduce ? 'auto' : 'smooth' });
  });
})();

// ---- Email dropdown contact form (Web3Forms) ----
(function(){
  var toggle = document.getElementById('emailToggle');
  var form   = document.getElementById('emailForm');
  if(!toggle || !form) return;
  toggle.addEventListener('click', function(){
    var willOpen = form.hasAttribute('hidden');
    if(willOpen){ form.removeAttribute('hidden'); } else { form.setAttribute('hidden',''); }
    toggle.setAttribute('aria-expanded', String(willOpen));
    if(willOpen){
      var first = form.querySelector('input:not([type=hidden]):not(.ef-hp), textarea');
      if(first) first.focus();
    }
  });
  var status = document.getElementById('emailStatus');
  form.addEventListener('submit', function(e){
    e.preventDefault();
    var btn = form.querySelector('.ef-send');
    if(status){ status.className='ef-status'; status.textContent='Sending\u2026'; }
    if(btn) btn.disabled = true;
    var payload = Object.fromEntries(new FormData(form).entries());
    fetch('https://api.web3forms.com/submit', {
      method:'POST',
      headers:{'Content-Type':'application/json','Accept':'application/json'},
      body: JSON.stringify(payload)
    })
    .then(function(r){ return r.json(); })
    .then(function(j){
      if(j.success){
        if(status){ status.className='ef-status ok'; status.textContent="Sent \u2014 thanks! I'll get back to you."; }
        form.reset();
      } else {
        if(status){ status.className='ef-status err'; status.textContent='Couldn\u2019t send. Email me directly at willowpichardo06@gmail.com'; }
      }
    })
    .catch(function(){
      if(status){ status.className='ef-status err'; status.textContent='Network error. Email me directly at willowpichardo06@gmail.com'; }
    })
    .finally(function(){ if(btn) btn.disabled = false; });
  });
})();

