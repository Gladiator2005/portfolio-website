#!/bin/bash
# Script to merge the feature branch into main
# Run this script from the repository root directory

set -e  # Exit on error

echo "========================================"
echo "Portfolio Website - Branch Merge Script"
echo "========================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if we're in a git repository
if [ ! -d .git ]; then
    echo -e "${RED}Error: Not in a git repository!${NC}"
    echo "Please run this script from the repository root directory."
    exit 1
fi

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
FEATURE_BRANCH="copilot/create-interactive-portfolio-website"
TARGET_BRANCH="main"

echo "Current branch: $CURRENT_BRANCH"
echo ""

# Fetch latest changes
echo -e "${YELLOW}Step 1: Fetching latest changes from remote...${NC}"
git fetch origin
echo -e "${GREEN}✓ Fetched latest changes${NC}"
echo ""

# Check if feature branch exists
if ! git show-ref --verify --quiet "refs/heads/$FEATURE_BRANCH" && \
   ! git show-ref --verify --quiet "refs/remotes/origin/$FEATURE_BRANCH"; then
    echo -e "${RED}Error: Feature branch '$FEATURE_BRANCH' not found!${NC}"
    exit 1
fi

# Switch to main branch
echo -e "${YELLOW}Step 2: Switching to main branch...${NC}"
if ! git show-ref --verify --quiet "refs/heads/$TARGET_BRANCH"; then
    echo "Main branch doesn't exist locally. Creating from remote..."
    git checkout -b "$TARGET_BRANCH" "origin/$TARGET_BRANCH"
else
    git checkout "$TARGET_BRANCH"
fi
echo -e "${GREEN}✓ Switched to main branch${NC}"
echo ""

# Pull latest main
echo -e "${YELLOW}Step 3: Pulling latest main branch...${NC}"
git pull origin "$TARGET_BRANCH" || echo "No changes to pull (this is okay)"
echo -e "${GREEN}✓ Main branch is up to date${NC}"
echo ""

# Show what will be merged
echo -e "${YELLOW}Step 4: Preview of changes to be merged:${NC}"
echo "Commits that will be added to main:"
git log "$TARGET_BRANCH..$FEATURE_BRANCH" --oneline
echo ""

# Ask for confirmation
echo -e "${YELLOW}Ready to merge '$FEATURE_BRANCH' into '$TARGET_BRANCH'${NC}"
read -p "Do you want to continue? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ] && [ "$CONFIRM" != "y" ]; then
    echo "Merge cancelled."
    exit 0
fi

# Perform the merge
echo ""
echo -e "${YELLOW}Step 5: Merging $FEATURE_BRANCH into $TARGET_BRANCH...${NC}"
if git merge "$FEATURE_BRANCH" --no-edit; then
    echo -e "${GREEN}✓ Merge completed successfully!${NC}"
else
    echo -e "${RED}Merge conflict detected!${NC}"
    echo "Please resolve the conflicts manually, then run:"
    echo "  git add <resolved-files>"
    echo "  git commit"
    echo "  git push origin $TARGET_BRANCH"
    exit 1
fi
echo ""

# Push to remote
echo -e "${YELLOW}Step 6: Pushing merged code to GitHub...${NC}"
git push origin "$TARGET_BRANCH"
echo -e "${GREEN}✓ Pushed to GitHub${NC}"
echo ""

# Ask about deleting feature branch
echo -e "${YELLOW}Merge completed successfully!${NC}"
echo ""
read -p "Do you want to delete the feature branch? (yes/no): " DELETE_BRANCH

if [ "$DELETE_BRANCH" = "yes" ] || [ "$DELETE_BRANCH" = "y" ]; then
    echo ""
    echo "Deleting feature branch locally and remotely..."
    git branch -d "$FEATURE_BRANCH" 2>/dev/null || echo "Local branch already deleted or doesn't exist"
    git push origin --delete "$FEATURE_BRANCH" 2>/dev/null || echo "Remote branch already deleted or doesn't exist"
    echo -e "${GREEN}✓ Feature branch deleted${NC}"
fi

echo ""
echo "========================================"
echo -e "${GREEN}✓ All Done!${NC}"
echo "========================================"
echo ""
echo "Your portfolio code is now in the main branch!"
echo ""
echo "Next steps:"
echo "1. Test the application: python manage.py runserver"
echo "2. Add your content via admin panel"
echo "3. Deploy to production"
echo ""
echo "For more information, see:"
echo "  - README.md"
echo "  - GETTING_STARTED.md"
echo "  - MERGE_GUIDE.md"
echo ""
