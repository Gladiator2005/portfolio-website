// ============================================
// Particles.js - Custom Particle Background Effect
// ============================================

class ParticleSystem {
    constructor(canvasId, options = {}) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.mouse = { x: null, y: null, radius: 150 };
        
        // Configuration
        this.config = {
            particleCount: options.particleCount || 80,
            particleColor: options.particleColor || 'rgba(99, 102, 241, 0.8)',
            lineColor: options.lineColor || 'rgba(99, 102, 241, 0.2)',
            particleSize: options.particleSize || 2,
            maxSpeed: options.maxSpeed || 0.5,
            connectionDistance: options.connectionDistance || 150,
            mouseInteraction: options.mouseInteraction !== false,
            ...options
        };
        
        this.init();
    }
    
    init() {
        this.setCanvasSize();
        this.createParticles();
        this.addEventListeners();
        this.animate();
    }
    
    setCanvasSize() {
        this.canvas.width = this.canvas.offsetWidth;
        this.canvas.height = this.canvas.offsetHeight;
    }
    
    createParticles() {
        // Adjust particle count based on screen size
        const area = this.canvas.width * this.canvas.height;
        const particleCount = Math.min(
            this.config.particleCount,
            Math.floor(area / 15000)
        );
        
        for (let i = 0; i < particleCount; i++) {
            this.particles.push(new Particle(this.canvas, this.config));
        }
    }
    
    addEventListeners() {
        window.addEventListener('resize', () => {
            this.setCanvasSize();
            this.particles = [];
            this.createParticles();
        });
        
        if (this.config.mouseInteraction) {
            this.canvas.addEventListener('mousemove', (e) => {
                const rect = this.canvas.getBoundingClientRect();
                this.mouse.x = e.clientX - rect.left;
                this.mouse.y = e.clientY - rect.top;
            });
            
            this.canvas.addEventListener('mouseleave', () => {
                this.mouse.x = null;
                this.mouse.y = null;
            });
        }
    }
    
    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Update and draw particles
        this.particles.forEach(particle => {
            particle.update(this.mouse);
            particle.draw(this.ctx);
        });
        
        // Draw connections between nearby particles
        this.connectParticles();
        
        requestAnimationFrame(() => this.animate());
    }
    
    connectParticles() {
        for (let i = 0; i < this.particles.length; i++) {
            for (let j = i + 1; j < this.particles.length; j++) {
                const dx = this.particles[i].x - this.particles[j].x;
                const dy = this.particles[i].y - this.particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < this.config.connectionDistance) {
                    const opacity = 1 - (distance / this.config.connectionDistance);
                    this.ctx.strokeStyle = this.config.lineColor.replace('0.2', opacity * 0.2);
                    this.ctx.lineWidth = 1;
                    this.ctx.beginPath();
                    this.ctx.moveTo(this.particles[i].x, this.particles[i].y);
                    this.ctx.lineTo(this.particles[j].x, this.particles[j].y);
                    this.ctx.stroke();
                }
            }
        }
    }
}

class Particle {
    constructor(canvas, config) {
        this.canvas = canvas;
        this.config = config;
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * this.config.particleSize + 1;
        this.speedX = (Math.random() - 0.5) * this.config.maxSpeed;
        this.speedY = (Math.random() - 0.5) * this.config.maxSpeed;
        this.originalSpeedX = this.speedX;
        this.originalSpeedY = this.speedY;
    }
    
    update(mouse) {
        // Mouse interaction - particles move away from cursor
        if (mouse.x != null && mouse.y != null) {
            const dx = this.x - mouse.x;
            const dy = this.y - mouse.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < mouse.radius) {
                const force = (mouse.radius - distance) / mouse.radius;
                const angle = Math.atan2(dy, dx);
                this.speedX = Math.cos(angle) * force * 5;
                this.speedY = Math.sin(angle) * force * 5;
            } else {
                // Gradually return to original speed
                this.speedX += (this.originalSpeedX - this.speedX) * 0.05;
                this.speedY += (this.originalSpeedY - this.speedY) * 0.05;
            }
        }
        
        // Update position
        this.x += this.speedX;
        this.y += this.speedY;
        
        // Bounce off edges
        if (this.x < 0 || this.x > this.canvas.width) {
            this.speedX *= -1;
            this.originalSpeedX *= -1;
            this.x = Math.max(0, Math.min(this.x, this.canvas.width));
        }
        
        if (this.y < 0 || this.y > this.canvas.height) {
            this.speedY *= -1;
            this.originalSpeedY *= -1;
            this.y = Math.max(0, Math.min(this.y, this.canvas.height));
        }
    }
    
    draw(ctx) {
        ctx.fillStyle = this.config.particleColor;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

// Initialize particle system when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('particles-canvas');
    
    if (canvas) {
        // Get theme colors
        const isDarkTheme = document.documentElement.getAttribute('data-theme') !== 'light';
        
        const particleOptions = {
            particleCount: 80,
            particleColor: isDarkTheme ? 'rgba(99, 102, 241, 0.8)' : 'rgba(99, 102, 241, 0.6)',
            lineColor: isDarkTheme ? 'rgba(99, 102, 241, 0.2)' : 'rgba(99, 102, 241, 0.15)',
            particleSize: 2,
            maxSpeed: 0.5,
            connectionDistance: 150,
            mouseInteraction: true
        };
        
        new ParticleSystem('particles-canvas', particleOptions);
        
        // Update particle colors when theme changes
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'data-theme') {
                    const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
                    // Reinitialize with new colors
                    const newOptions = {
                        ...particleOptions,
                        particleColor: isDark ? 'rgba(99, 102, 241, 0.8)' : 'rgba(99, 102, 241, 0.6)',
                        lineColor: isDark ? 'rgba(99, 102, 241, 0.2)' : 'rgba(99, 102, 241, 0.15)'
                    };
                    new ParticleSystem('particles-canvas', newOptions);
                }
            });
        });
        
        observer.observe(document.documentElement, {
            attributes: true
        });
    }
});
