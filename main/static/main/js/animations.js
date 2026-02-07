// ============================================
// Animations JavaScript - Scroll Animations, Counters, Parallax
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    initScrollReveal();
    initCounters();
    initSkillBars();
    initTypingEffect();
    initTestimonialCarousel();
    initProjectFilter();
    initParallax();
});

// ============================================
// Scroll Reveal with Intersection Observer
// ============================================
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal, .stagger-item');
    
    if (revealElements.length === 0) return;
    
    const observerOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                if (entry.target.classList.contains('stagger-item')) {
                    entry.target.classList.add('animate-fade-in-up');
                }
            }
        });
    }, observerOptions);
    
    revealElements.forEach(element => {
        observer.observe(element);
    });
}

// ============================================
// Counter Animation
// ============================================
function initCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    if (counters.length === 0) return;
    
    const observerOptions = {
        threshold: 0.5
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                animateCounter(entry.target);
                entry.target.classList.add('counted');
            }
        });
    }, observerOptions);
    
    counters.forEach(counter => {
        observer.observe(counter);
    });
}

function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target')) || parseInt(element.textContent);
    const duration = 2000; // 2 seconds
    const increment = target / (duration / 16); // 60fps
    let current = 0;
    
    const updateCounter = () => {
        current += increment;
        if (current < target) {
            element.textContent = Math.floor(current);
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target;
        }
    };
    
    updateCounter();
}

// ============================================
// Skill Bar Animation
// ============================================
function initSkillBars() {
    const skillBars = document.querySelectorAll('.skill-bar');
    
    if (skillBars.length === 0) return;
    
    const observerOptions = {
        threshold: 0.5
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                const proficiency = entry.target.getAttribute('data-proficiency');
                entry.target.style.width = proficiency + '%';
                entry.target.classList.add('animated');
            }
        });
    }, observerOptions);
    
    skillBars.forEach(bar => {
        observer.observe(bar);
    });
}

// ============================================
// Typing Effect
// ============================================
function initTypingEffect() {
    const typingElements = document.querySelectorAll('[data-typing]');
    
    typingElements.forEach(element => {
        const text = element.getAttribute('data-typing');
        const speed = parseInt(element.getAttribute('data-typing-speed')) || 100;
        let index = 0;
        
        element.textContent = '';
        
        const typeWriter = () => {
            if (index < text.length) {
                element.textContent += text.charAt(index);
                index++;
                setTimeout(typeWriter, speed);
            }
        };
        
        // Start typing after a delay
        setTimeout(typeWriter, 1000);
    });
}

// ============================================
// Testimonial Carousel
// ============================================
function initTestimonialCarousel() {
    const slider = document.querySelector('.testimonials-slider');
    if (!slider) return;
    
    const testimonials = slider.querySelectorAll('.testimonial-card');
    if (testimonials.length === 0) return;
    
    let currentIndex = 0;
    const autoPlayInterval = 5000; // 5 seconds
    
    // Hide all testimonials except the first one
    testimonials.forEach((testimonial, index) => {
        if (index !== 0) {
            testimonial.style.display = 'none';
        }
    });
    
    // Create navigation dots
    const dotsContainer = document.createElement('div');
    dotsContainer.className = 'testimonial-dots';
    dotsContainer.style.cssText = 'display: flex; justify-content: center; gap: 0.5rem; margin-top: 2rem;';
    
    testimonials.forEach((_, index) => {
        const dot = document.createElement('span');
        dot.className = 'testimonial-dot';
        dot.style.cssText = 'width: 12px; height: 12px; border-radius: 50%; background: var(--glass-border); cursor: pointer; transition: background 0.3s ease;';
        if (index === 0) {
            dot.style.background = 'var(--primary)';
        }
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });
    
    slider.appendChild(dotsContainer);
    
    function goToSlide(index) {
        // Hide current testimonial
        testimonials[currentIndex].style.display = 'none';
        
        // Update dots
        const dots = dotsContainer.querySelectorAll('.testimonial-dot');
        dots[currentIndex].style.background = 'var(--glass-border)';
        
        // Show new testimonial
        currentIndex = index;
        testimonials[currentIndex].style.display = 'block';
        testimonials[currentIndex].classList.add('animate-fade-in');
        dots[currentIndex].style.background = 'var(--primary)';
    }
    
    function nextSlide() {
        const nextIndex = (currentIndex + 1) % testimonials.length;
        goToSlide(nextIndex);
    }
    
    // Auto-play
    setInterval(nextSlide, autoPlayInterval);
}

// ============================================
// Project Filter
// ============================================
function initProjectFilter() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    
    if (filterButtons.length === 0) return;
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            const filterValue = this.getAttribute('data-filter');
            
            projectCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                
                if (filterValue === 'all' || cardCategory === filterValue) {
                    card.style.display = 'block';
                    card.classList.add('animate-fade-in');
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

// ============================================
// Parallax Effect
// ============================================
function initParallax() {
    const parallaxElements = document.querySelectorAll('[data-parallax]');
    
    if (parallaxElements.length === 0) return;
    
    window.addEventListener('scroll', function() {
        const scrolled = window.scrollY;
        
        parallaxElements.forEach(element => {
            const speed = parseFloat(element.getAttribute('data-parallax')) || 0.5;
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    });
}

// ============================================
// Stagger Animation on Scroll
// ============================================
function staggerAnimation(elements, animationClass) {
    elements.forEach((element, index) => {
        setTimeout(() => {
            element.classList.add(animationClass);
        }, index * 100);
    });
}

// Apply stagger animations to specific sections
const projectCards = document.querySelectorAll('.project-card');
if (projectCards.length > 0) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.hasAttribute('data-animated')) {
                entry.target.classList.add('animate-fade-in-up');
                entry.target.setAttribute('data-animated', 'true');
            }
        });
    }, { threshold: 0.1 });
    
    projectCards.forEach(card => observer.observe(card));
}

// ============================================
// Lazy Loading Images
// ============================================
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if (images.length === 0) return;
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.getAttribute('data-src');
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

initLazyLoading();
