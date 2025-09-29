# 🔄 Updating Your Fork with the Original Project

When you forked `python-kickstart`, you created your own copy on GitHub.  
But the original project (`r-/python-kickstart`) may get new updates.  
Follow these steps to pull in those updates into your own fork.

---

## 1. Add the original project as `upstream` (only once)

    git remote add upstream https://github.com/r-/python-kickstart.git

Check that it worked:

    git remote -v

You should now see both:

- `origin` → your fork (your GitHub repo)  
- `upstream` → r-/python-kickstart  

---

## 2. Get the latest changes from upstream

    git fetch upstream

---

## 3. Merge upstream changes into your branch

Usually you are working on `main`:

    git checkout main
    git merge upstream/main

---

## 4. Push the updated branch back to *your fork*

    git push origin main

---

Done! Now your fork has the latest changes from `r-/python-kickstart`.