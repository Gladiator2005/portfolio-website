#!/bin/bash
# Script to generate static site for GitHub Pages deployment

echo "=== Building Static Site for GitHub Pages ==="
echo ""

# Step 1: Collect static files
echo "Step 1: Collecting static files..."
python manage.py collectstatic --noinput --clear

# Step 2: Generate HTML files
echo ""
echo "Step 2: Generating static HTML pages..."
python manage.py generate_static

# Step 3: Copy static files to docs directory
echo ""
echo "Step 3: Copying static files to docs directory..."
mkdir -p docs/static
cp -r staticfiles/* docs/static/ 2>/dev/null || cp -r main/static/* docs/static/ 2>/dev/null || true

# Step 4: Copy media files if they exist
if [ -d "media" ] && [ "$(ls -A media)" ]; then
    echo ""
    echo "Step 4: Copying media files..."
    mkdir -p docs/media
    cp -r media/* docs/media/
fi

echo ""
echo "=== Static site generated successfully! ==="
echo "Location: ./docs/"
echo ""
echo "To deploy to GitHub Pages:"
echo "1. Commit the docs/ directory"
echo "2. Push to GitHub"
echo "3. Enable GitHub Pages in repository settings (use 'docs' folder)"
