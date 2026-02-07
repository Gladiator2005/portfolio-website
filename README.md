# 🚀 Modern Portfolio Website

![Django](https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

A complete, modern, interactive portfolio website built with Django, inspired by the design principles of [CubiFlow](https://www.cubiflow.com/). This project showcases technical work, projects, and skills through an interactive and visually engaging interface with beautiful animations, glassmorphism effects, and smooth transitions.

## ✨ Features

### Design & UI
- 🎨 **Modern Dark Theme** with light mode toggle
- 💎 **Glassmorphism Effects** on cards and components
- 🌈 **Dynamic Gradient Backgrounds** with animated transitions
- ✨ **Fluid Animations** with GSAP and AOS libraries
- 🎯 **Custom Particle System** for hero section background
- 📱 **Fully Responsive** design for all devices
- 🎭 **Smooth Page Transitions** and scroll animations
- 🖱️ **Interactive Hover Effects** on all interactive elements

### Functionality
- 🏠 **Dynamic Homepage** with hero, featured projects, skills, stats, and testimonials
- 📂 **Project Portfolio** with category filtering and detailed project pages
- 👤 **About Page** with experience timeline, education, and skills showcase
- 📧 **Contact Form** with validation and message storage
- 🔐 **Django Admin Panel** for easy content management
- 🎚️ **Skill Progress Bars** with animated counters
- 💬 **Testimonial Carousel** with auto-rotation
- 📊 **Animated Statistics Counter**

### Technical Features
- ⚡ **Django 5.0** backend with robust models and views
- 🎨 **CSS Variables** for easy theme customization
- 📦 **Modular Architecture** with separate CSS/JS files
- 🔍 **SEO Friendly** with proper meta tags
- ♿ **Accessible** with ARIA labels and keyboard navigation
- 🌐 **Cross-browser Compatible** (Chrome, Firefox, Safari, Edge)
- 🎯 **Performance Optimized** with lazy loading and efficient animations

## 📸 Screenshots

*Screenshots will be added here once the site is deployed*

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Gladiator2005/portfolio-website.git
cd portfolio-website
```

2. **Create a virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your settings
# Generate a secret key at https://djecrety.ir/
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create a superuser**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```

8. **Visit the site**
- Website: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
portfolio-website/
│
├── portfolio_project/          # Main Django project
│   ├── settings.py            # Project settings
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
│
├── main/                      # Main application
│   ├── models.py              # Database models (Project, Skill, Experience, etc.)
│   ├── views.py               # View functions
│   ├── urls.py                # App URL patterns
│   ├── admin.py               # Admin panel configuration
│   ├── forms.py               # Contact form definition
│   ├── templatetags/          # Custom template filters
│   ├── templates/main/        # HTML templates
│   │   ├── base.html          # Base template
│   │   ├── index.html         # Homepage
│   │   ├── projects.html      # Projects list
│   │   ├── project_detail.html # Project detail
│   │   ├── about.html         # About page
│   │   └── contact.html       # Contact page
│   └── static/main/           # Static files
│       ├── css/
│       │   ├── style.css      # Main stylesheet
│       │   ├── animations.css # Animation keyframes
│       │   └── responsive.css # Media queries
│       ├── js/
│       │   ├── main.js        # Core JavaScript
│       │   ├── animations.js  # Scroll animations
│       │   └── particles.js   # Particle system
│       └── images/            # Image assets
│
├── static/                    # Collected static files (generated)
├── media/                     # User-uploaded files
├── requirements.txt           # Python dependencies
├── .env.example               # Example environment variables
├── .gitignore                 # Git ignore rules
└── manage.py                  # Django management script
```

## 🎨 Customization

### Colors & Theme

Edit CSS variables in `main/static/main/css/style.css`:

```css
:root {
    /* Primary Colors */
    --primary: #6366f1;
    --secondary: #ec4899;
    --accent: #f59e0b;
    
    /* Backgrounds */
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    
    /* Text Colors */
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
}
```

### Site Configuration

1. Login to the admin panel at `/admin/`
2. Navigate to **Site Configuration**
3. Update your personal information, social links, and statistics

### Adding Content

#### Projects
1. Go to Admin → Projects → Add Project
2. Fill in project details, upload images, and assign technologies
3. Mark as "Featured" to display on homepage

#### Skills
1. Go to Admin → Skills → Add Skill
2. Set name, category, proficiency, and icon class
3. Use Font Awesome icon classes (e.g., `fab fa-python`)

#### Experience & Education
1. Add work experience and education entries
2. These will appear on the About page in timeline format

## 🗄️ Database Models

### Core Models

- **Project**: Portfolio projects with images, descriptions, and technologies
- **Technology**: Tech stack items with icons and colors
- **Category**: Project categories for filtering
- **Skill**: Technical skills with proficiency levels
- **Experience**: Work experience timeline
- **Education**: Academic background
- **Testimonial**: Client testimonials and reviews
- **SiteConfiguration**: Site-wide settings (singleton)
- **ContactMessage**: Messages from contact form

## 🚢 Deployment

### Heroku

1. Install Heroku CLI
2. Create a Heroku app
```bash
heroku create your-app-name
```

3. Add PostgreSQL addon
```bash
heroku addons:create heroku-postgresql:mini
```

4. Set environment variables
```bash
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='your-app-name.herokuapp.com'
```

5. Deploy
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Railway

1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically on push

### VPS (DigitalOcean, Linode, etc.)

1. Set up a server with Python 3.12+
2. Install dependencies and configure Nginx/Apache
3. Use Gunicorn as the WSGI server
4. Set up SSL with Let's Encrypt
5. Configure static file serving

## 📦 Dependencies

- **Django** (5.0+): Web framework
- **Pillow**: Image processing
- **python-decouple**: Environment variable management
- **gunicorn**: WSGI HTTP server
- **whitenoise**: Static file serving

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Design Inspiration**: [CubiFlow](https://www.cubiflow.com/)
- **Animation Libraries**: [GSAP](https://greensock.com/gsap/) and [AOS](https://michalsnik.github.io/aos/)
- **Icons**: [Font Awesome](https://fontawesome.com/)
- **Fonts**: [Google Fonts](https://fonts.google.com/) (Inter & Space Grotesk)

## 🗺️ Roadmap

- [ ] Add blog functionality
- [ ] Integrate with third-party APIs (GitHub, LinkedIn)
- [ ] Add more animation presets
- [ ] Implement dark/light theme persistence across sessions
- [ ] Add multi-language support
- [ ] Create project filtering by technology
- [ ] Add search functionality
- [ ] Implement project tags
- [ ] Add RSS feed for projects
- [ ] Create sitemap for SEO

## 📧 Contact

For questions or support, please contact via the contact form on the website or open an issue on GitHub.

---

**Made with ❤️ using Django and modern web technologies**
