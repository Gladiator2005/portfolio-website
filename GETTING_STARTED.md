# Getting Started with Your Portfolio Website

## 🎉 Congratulations! Your portfolio website is ready!

The website has been successfully created and is fully functional. Here's how to get started:

## 🚀 Running the Website

1. **Activate your virtual environment** (if not already activated):
   ```bash
   # On macOS/Linux
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

2. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

3. **Access the website**:
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 🔐 Admin Access

**Username**: `admin`  
**Password**: `admin123`

⚠️ **IMPORTANT**: Change this password in production!

## 📝 Adding Your Content

### 1. Site Configuration (Required First)
1. Login to admin panel
2. Go to **Site Configuration**
3. Fill in:
   - Your name
   - Job title
   - Bio
   - Email, phone, location
   - Social media links (GitHub, LinkedIn, Twitter)
   - Statistics (projects completed, years of experience, etc.)
   - Upload profile image
   - Upload resume (optional)

### 2. Add Projects
1. Go to **Projects** → **Add Project**
2. Fill in:
   - Title and slug (auto-generated from title)
   - Short description (for cards)
   - Full description
   - Upload project image
   - Select category
   - Assign technologies
   - Add project URL and GitHub URL
   - Mark as "Featured" to show on homepage
   - Set display order

### 3. Add Technologies
1. Go to **Technologies** → **Add Technology**
2. Fill in:
   - Technology name (e.g., "Python", "React", "Docker")
   - Icon class from Font Awesome (e.g., `fab fa-python`)
   - Color in hex format (e.g., `#3776ab`)

### 4. Add Categories
1. Go to **Categories** → **Add Category**
2. Examples:
   - Web Applications
   - Mobile Apps
   - APIs
   - Open Source

### 5. Add Skills
1. Go to **Skills** → **Add Skill**
2. Fill in:
   - Skill name
   - Category (Frontend, Backend, DevOps, Tools, Other)
   - Proficiency (0-100)
   - Icon class from Font Awesome
   - Display order

### 6. Add Work Experience
1. Go to **Experience** → **Add Experience**
2. Fill in:
   - Company name
   - Position
   - Location
   - Start and end dates
   - Description
   - Check "Current" if still working there

### 7. Add Education
1. Go to **Education** → **Add Education**
2. Fill in:
   - Institution
   - Degree
   - Field of study
   - Start and end dates
   - Description (optional)

### 8. Add Testimonials (Optional)
1. Go to **Testimonials** → **Add Testimonial**
2. Fill in:
   - Client name
   - Position and company
   - Testimonial content
   - Upload client photo (optional)
   - Rating (1-5 stars)
   - Mark as "Featured" to show on homepage

## 🎨 Customization

### Changing Colors
Edit `main/static/main/css/style.css`:

```css
:root {
    /* Change these values */
    --primary: #6366f1;        /* Primary color */
    --secondary: #ec4899;      /* Secondary color */
    --accent: #f59e0b;         /* Accent color */
}
```

### Changing Fonts
Edit `main/templates/main/base.html` and update the Google Fonts link.

## 🌐 Deploying to Production

### Heroku
```bash
# Install Heroku CLI, then:
heroku create your-app-name
heroku addons:create heroku-postgresql:mini
heroku config:set SECRET_KEY='your-new-secret-key'
heroku config:set DEBUG=False
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Railway
1. Connect your GitHub repo to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically

## 📚 Useful Font Awesome Icons

For Technologies and Skills, use these icon classes:

**Languages:**
- Python: `fab fa-python`
- JavaScript: `fab fa-js`
- Java: `fab fa-java`
- PHP: `fab fa-php`

**Frontend:**
- React: `fab fa-react`
- Vue: `fab fa-vuejs`
- Angular: `fab fa-angular`
- HTML5: `fab fa-html5`
- CSS3: `fab fa-css3-alt`

**Backend:**
- Node.js: `fab fa-node-js`
- Django: (use) `fas fa-server`
- Docker: `fab fa-docker`

**Tools:**
- Git: `fab fa-git-alt`
- GitHub: `fab fa-github`
- AWS: `fab fa-aws`
- Linux: `fab fa-linux`

Search for more icons at: https://fontawesome.com/icons

## 🐛 Troubleshooting

**Static files not loading?**
```bash
python manage.py collectstatic
```

**Database issues?**
```bash
python manage.py migrate
```

**Need to reset database?**
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📖 Documentation

Full documentation is available in the README.md file.

## 🎯 Tips

1. **Images**: Use high-quality images (recommended: 1200x800px for projects)
2. **SEO**: Update meta descriptions in templates
3. **Performance**: Optimize images before uploading
4. **Backup**: Regularly backup your database and media files
5. **Security**: Change SECRET_KEY and admin password before deploying

## 🆘 Need Help?

- Check the README.md for detailed documentation
- Django documentation: https://docs.djangoproject.com/
- Font Awesome icons: https://fontawesome.com/icons

---

**Happy coding! 🚀**
