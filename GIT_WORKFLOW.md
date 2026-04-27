# 🧬 Pediatric Counting Research: Collaboration Protocol

*Director and Partner, this is your guide to working together without "breaking the brain." Git is just a time machine—it lets us explore new ideas in branches without ruining our stable, hard-earned files.*

---

### 1. The Two Worlds (Branching)
We have divided the repository into two distinct "worlds":
-   **`main` (The Vault):** This contains the **Gold Standard** files. We only touch this when we are 100% ready for a presentation or submission. **Never work directly on main.**
-   **`develop` (The Laboratory):** This is where you and your partner should live. It is a safe space to experiment, break things, and rebuild.

---

### 2. The Daily Workflow (The Cycle)
When you want to add a new section (e.g., Chapter 4 or a new LaTeX slide):

#### Step A: Get the latest "Intelligence"
Before you start, make sure you have your partner's latest work:
```bash
git checkout develop
git pull origin develop
```

#### Step B: Create a "Mission Branch"
Don't work on `develop` directly. Create a small branch for your specific task:
```bash
git checkout -b feature-methodology-refinement
```

#### Step C: Do the Work
Edit your files, save them, and test them. When you are happy, "stage" and "commit" them:
```bash
git add .
git commit -m "feat: added allometric ratio math to methodology"
```

#### Step D: Beam it Up (Push)
Send your branch to GitHub so your partner can see it:
```bash
git push origin feature-methodology-refinement
```

---

### 3. Merging (Bringing it all Together)
Once your "Mission Branch" is done and your partner has reviewed it on GitHub:
1.  Go to the GitHub website.
2.  Open a **Pull Request (PR)** from your branch into `develop`.
3.  Click "Merge" once you are both happy.

---

### 4. 🛡️ The Golden Rules
1.  **Always pull before you push.** (Avoids "merge conflicts").
2.  **If it's broken, don't merge it to develop.** Keep the Laboratory stable!
3.  **Write meaningful commit messages.** (e.g., `"fix: corrected typo in Chapter 3"` is better than `"updated file"`).

---
*Stay rigorous. Stay synced. The thesis is only as strong as our collaboration.*
