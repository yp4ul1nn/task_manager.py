document.addEventListener('DOMContentLoaded', () => {

    /* --- 1. AWWWARDS: CUSTOM CURSOR & LERP --- */
    const dot = document.querySelector('.cursor-dot');
    const outline = document.querySelector('.cursor-outline');
    let mouseX = 0, mouseY = 0;
    let outlineX = 0, outlineY = 0;

    // Apenas ativa mouse fx em resoluções maiores
    if(window.innerWidth > 992 && dot && outline) {
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            // Dot é instantâneo
            dot.style.left = mouseX + 'px';
            dot.style.top = mouseY + 'px';
        });

        const loop = () => {
            // Lerp (Interpolação linear para atraso suave)
            let distX = mouseX - outlineX;
            let distY = mouseY - outlineY;
            outlineX += distX * 0.15;
            outlineY += distY * 0.15;
            
            outline.style.left = outlineX + 'px';
            outline.style.top = outlineY + 'px';
            requestAnimationFrame(loop);
        };
        loop();

        // Expansão do cursor ao passar em elementos interativos
        const hoverTags = document.querySelectorAll('button, a, input, select, textarea, .magnetic-elem');
        hoverTags.forEach(el => {
            el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
            el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
        });
    }

    /* --- 2. MAGNETIC ELEMENTS --- */
    const magnetics = document.querySelectorAll('.magnetic-elem');
    magnetics.forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            // Força magnética
            el.style.transform = `translate(${x * 0.2}px, ${y * 0.2}px)`;
        });
        el.addEventListener('mouseleave', () => {
            el.style.transform = 'translate(0px, 0px)';
        });
    });

    /* --- 3. DYNAMIC GLOW (CARD EFFECT) --- */
    const cards = document.querySelectorAll('.task-card');
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const glow = card.querySelector('.card-glow');
            if(!glow) return;
            const rect = card.getBoundingClientRect();
            glow.style.left = (e.clientX - rect.left) + 'px';
            glow.style.top = (e.clientY - rect.top) + 'px';
        });
    });

    /* --- 4. VANILLA TILT INITIATOR --- */
    // A biblioteca é chamada dinamicamente no HTML se existir
    if (typeof VanillaTilt !== 'undefined') {
        VanillaTilt.init(document.querySelectorAll(".tilt-effect"), {
            max: 5,
            speed: 400,
            glare: true,
            "max-glare": 0.05,
            scale: 1.01
        });
    }

    /* --- 5. THEME SYSTEM & LOCAL STORAGE --- */
    const htmlEl = document.documentElement;
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.querySelector('.theme-icon');
    const themeText = document.querySelector('.theme-text');

    const savedTheme = localStorage.getItem('nexus_theme') || 'dark';
    htmlEl.setAttribute('data-theme', savedTheme);
    updateThemeUI(savedTheme);

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = htmlEl.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            htmlEl.setAttribute('data-theme', newTheme);
            localStorage.setItem('nexus_theme', newTheme);
            updateThemeUI(newTheme);
        });
    }

    function updateThemeUI(theme) {
        if(!themeIcon || !themeText) return;
        if(theme === 'dark') {
            themeIcon.className = 'bi bi-sun text-warning theme-icon';
            themeText.textContent = 'Modo Claro';
        } else {
            themeIcon.className = 'bi bi-moon-stars theme-icon';
            themeText.textContent = 'Modo Escuro';
        }
    }

    /* --- 6. MODAL SYSTEM --- */
    window.toggleModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.toggle('active');
            if(modalId === 'commandPaletteModal' && modal.classList.contains('active')) {
                setTimeout(() => document.getElementById('spotlight-input').focus(), 100);
            }
        }
    };

    document.querySelectorAll('.modal-overlay').forEach(overlay => {
        overlay.addEventListener('click', function(e) {
            if (e.target === this) this.classList.remove('active');
        });
    });

    /* --- 6.1. COMMAND PALETTE (SPOTLIGHT) --- */
    const spotlightInput = document.getElementById('spotlight-input');
    const spotlightResults = document.getElementById('spotlight-results');
    
    // Keybinds (Ctrl+K / Cmd+K e Esc)
    document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
            e.preventDefault();
            toggleModal('commandPaletteModal');
        }
        if (e.key === 'Escape') {
            document.getElementById('commandPaletteModal').classList.remove('active');
            document.getElementById('addTaskModal').classList.remove('active');
        }
    });

    // Real-time Search em Cartões Ativos
    if(spotlightInput && spotlightResults) {
        spotlightInput.addEventListener('input', function() {
            const term = this.value.toLowerCase().trim();
            const cards = document.querySelectorAll('.task-grid .task-card');
            let hasResults = false;
            
            spotlightResults.innerHTML = '';

            if (term === '') {
                spotlightResults.innerHTML = '<div class="text-center py-4 text-muted font-space small msg-placeholder"><i class="bi bi-magic d-block fs-3 mb-2"></i>Comece a digitar.</div>';
                return;
            }

            cards.forEach(card => {
                const title = card.querySelector('.task-title').innerText.toLowerCase();
                const descEl = card.querySelector('.task-desc');
                const desc = descEl ? descEl.innerText.toLowerCase() : '';

                if(title.includes(term) || desc.includes(term)) {
                    hasResults = true;
                    // Clonar o card para renderizar no spotlight
                    const clone = card.cloneNode(true);
                    clone.className = 'glass-subpanel hover-bright mb-2 cursor-pointer font-space text-white w-100 border-0 p-3';
                    clone.style.cursor = 'pointer';
                    // Deixa funcional o click do clone redirecionar 
                    clone.addEventListener('click', () => {
                        const editBtn = card.querySelector('.action-btn[href^="/editar"]');
                        if (editBtn) window.location.href = editBtn.getAttribute('href');
                    });
                    
                    spotlightResults.appendChild(clone);
                }
            });

            if(!hasResults) {
                spotlightResults.innerHTML = '<div class="text-center py-4 text-danger font-space msg-placeholder fw-bold"><i class="bi bi-x-circle d-block fs-3 mb-2"></i>Nenhuma tarefa identificada com esse termo.</div>';
            }
        });
    }

    /* --- 6.2. POMODORO TIMER (HYPER FOCUS) --- */
    const timerBtn = document.getElementById('timer-btn');
    const timerLabel = document.getElementById('timer-label');
    const timerIcon = document.getElementById('timer-icon');
    const timerDisplay = document.getElementById('timer-display');
    const circleSvg = document.getElementById('pomodoro-circle');
    
    let timerInterval = null;
    let timeTotal = 25 * 60; // 25 Minutos
    let timeLeft = timeTotal;
    const circleCircumference = 226.2; // 2 * pi * 36

    function formatTime(secs) {
        const m = Math.floor(secs / 60).toString().padStart(2, '0');
        const s = (secs % 60).toString().padStart(2, '0');
        return `${m}:${s}`;
    }

    if(timerBtn && circleSvg && timerDisplay) {
        timerBtn.addEventListener('click', () => {
            if(timerInterval) {
                // Em pause
                clearInterval(timerInterval);
                timerInterval = null;
                timerLabel.innerText = "RESUME";
                timerIcon.className = "bi bi-play-fill";
                timerBtn.classList.replace('bg-danger', 'bg-white');
                timerBtn.classList.replace('text-white', 'text-dark');
            } else {
                // Rodando
                timerLabel.innerText = "PAUSE";
                timerIcon.className = "bi bi-pause-fill";
                timerBtn.classList.replace('bg-white', 'bg-danger');
                timerBtn.classList.replace('text-dark', 'text-white');

                timerInterval = setInterval(() => {
                    if (timeLeft > 0) {
                        timeLeft--;
                        timerDisplay.innerText = formatTime(timeLeft);
                        
                        // Atualiza Offset do Anel (Animação Circular)
                        const offset = circleCircumference - (timeLeft / timeTotal) * circleCircumference;
                        circleSvg.style.strokeDashoffset = offset;
                    } else {
                        clearInterval(timerInterval);
                        timerInterval = null;
                        timerDisplay.innerText = "DONE!";
                        circleSvg.style.strokeDashoffset = 0;
                        document.body.classList.add('cursor-hover'); // Animação
                    }
                }, 1000);
            }
        });
    }

    /* --- 7. ENTRADA/SAIDA & AJAX MOCKS --- */
    const revealElements = document.querySelectorAll('.scroll-reveal');
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0) translateZ(0)';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -20px 0px' });
        
        revealElements.forEach(el => revealObserver.observe(el));
    }

    // Saída com Lasers / Strike
    const actionLinks = document.querySelectorAll('.action-link');
    actionLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault(); 
            const targetUrl = this.getAttribute('href');
            const taskItem = this.closest('.task-card');
            
            if (taskItem) {
                if(this.getAttribute('data-action') === 'complete') {
                    taskItem.classList.add('completed-strike');
                } else {
                    taskItem.style.transition = 'all 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
                    taskItem.style.opacity = '0';
                    taskItem.style.transform = 'scale(0.8) translateY(-30px)';
                }
                setTimeout(() => { window.location.href = targetUrl; }, 400);
            } else {
                window.location.href = targetUrl;
            }
        });
    });

    /* --- 8. LOGIC DE FILTROS E ABAS (NAVBAR & TOOLBAR) --- */
    const filterBadges = document.querySelectorAll('.filter-badge');
    const navTabs = document.querySelectorAll('.nav-item[data-tab]');
    const allTaskCards = document.querySelectorAll('.task-grid .task-card');
    const currentViewLabel = document.getElementById('current-view-label');
    const currentPageTitle = document.getElementById('current-page-title');

    let currentTab = 'dashboard';
    let currentFilter = 'all';

    function applyFilters() {
        allTaskCards.forEach(card => {
            let showContext = false;
            let showPriority = false;

            if (currentTab === 'dashboard') {
                showContext = true;
            } else if (currentTab === 'archive') {
                const hasConcluir = card.querySelector('a[href^="/concluir"]');
                showContext = !hasConcluir;
            }

            if (currentFilter === 'all') {
                showPriority = true;
            } else {
                const cardText = card.innerText.toLowerCase();
                const targetText = currentFilter.toLowerCase();
                const badgePriori = card.querySelector('.badge:not(.bg-secondary)'); 
                if (badgePriori && badgePriori.innerText.toLowerCase().includes(targetText)) {
                    showPriority = true;
                } else if (!badgePriori && cardText.includes(targetText)) {
                    showPriority = true;
                }
            }

            if (showContext && showPriority) {
                card.style.display = 'block';
                card.style.animation = 'fadeIn 0.4s ease forwards';
            } else {
                card.style.display = 'none';
            }
        });
    }

    if(navTabs.length > 0) {
        navTabs.forEach(tab => {
            tab.addEventListener('click', function() {
                navTabs.forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                currentTab = this.getAttribute('data-tab');
                
                if (currentTab === 'dashboard') {
                    if (currentViewLabel) currentViewLabel.innerText = 'VISÃO GERAL';
                    if (currentPageTitle) currentPageTitle.innerText = 'Dashboard Space.';
                } else if (currentTab === 'archive') {
                    if (currentViewLabel) currentViewLabel.innerText = 'HISTÓRICO';
                    if (currentPageTitle) currentPageTitle.innerText = 'Arquivo Morto.';
                }
                
                applyFilters();
            });
        });
    }

    if (filterBadges.length > 0) {
        filterBadges.forEach(badge => {
            badge.addEventListener('click', function() {
                filterBadges.forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                currentFilter = this.getAttribute('data-filter');
                applyFilters();
            });
        });
    }
});
