<!--
SOURCE: Paramchoudhary/ResumeSkills — https://github.com/Paramchoudhary/ResumeSkills/blob/main/skills/job-description-analyzer/SKILL.md
Retrieved 2026-06-26, verbatim. License: MIT. Part of a 20-skill job-search collection.
Use BEFORE tailoring a resume: it tells you whether a role is worth the effort.
-->
---
name: job-description-analyzer
description: Analyze job postings, calculate match scores, identify gaps, and create application strategy
---

# Job Description Analyzer

## When to Use This Skill

Use this skill when the user:
- Wants to analyze a job posting
- Asks "should I apply to this job?"
- Wants to know their match percentage for a role
- Needs help understanding job requirements
- Wants to tailor their resume for a specific position
- Mentions: "analyze this job", "am I qualified", "match score", "should I apply"

Use this BEFORE resume tailoring to ensure effort is worth it.

## Core Capabilities

- Extract and categorize job requirements (must-have vs nice-to-have)
- Calculate match score between user's experience and job requirements
- Identify skill gaps and strengths
- Detect red flags in job postings
- Prioritize which experiences to highlight
- Generate resume tailoring strategy
- Create cover letter talking points
- Assess company culture fit indicators

## The Strategic Problem

Most job seekers waste time on:
- Jobs they're under-qualified for (<60% match)
- Jobs they're over-qualified for (flight risk)
- Jobs with red flags (high turnover, toxic culture)
- Applying to 50+ jobs blindly hoping something sticks

Better approach:
- Apply to 10-15 jobs strategically
- Target 70-90% match jobs
- Customize deeply for each
- Higher response rate, less burnout

## Analysis Process

### Step 1: Extract Requirements

Break job description into categories:

**Required (Must-Have)**: Education, years of experience, specific technical skills, certifications/licenses, industry experience.

**Preferred (Nice-to-Have)**: "Bonus" skills, advanced certifications, domain expertise, specific tool experience.

**Soft Skills/Culture**: Communication style, work environment, team structure, company values.

### Step 2: Keyword Extraction

Identify three types:
- **Hard Skills** (tools, methodologies, certifications)
- **Soft Skills** (leadership, collaboration, communication, problem-solving)
- **Industry/Domain Knowledge** (B2B SaaS, healthcare, fintech; enterprise vs SMB; regulatory: HIPAA, SOX, GDPR)

### Step 3: Calculate Match Score

```
MATCH CALCULATION:
Required Skills:  User has 8 out of 10 required = 80%
Preferred Skills: User has 3 out of 5 preferred = 60%
Overall Match: weight required 70%, preferred 30%
  (80% × 0.7) + (60% × 0.3) = 74%

INTERPRETATION:
90-100% = Overqualified (may be flight risk)
75-89%  = Excellent fit (apply immediately)
60-74%  = Good fit (apply with strong cover letter)
50-59%  = Stretch role (apply if passionate)
<50%    = Under-qualified (skip unless dream job)
```

### Step 4: Gap Analysis

For each missing requirement:
- **Critical gap**: Deal-breaker (don't apply)
- **Major gap**: Significant but addressable (mention in cover letter)
- **Minor gap**: Easy to learn (downplay or emphasize related skills)

### Step 5: Red Flag Detection

**Workload Red Flags:** "Wear many hats", "Fast-paced environment", "Hit the ground running", "Self-starter in ambiguous situations".

**Culture Red Flags:** "Rockstar/Ninja/Guru", "We work hard, play hard", "Unlimited vacation", "Like a family".

**Compensation Red Flags:** "Competitive salary" (no range), "Equity-heavy" (low cash), "Commission-based" (no base), "DOE" with no range.

## Match Score Output Format

```markdown
# JOB ANALYSIS REPORT
**Position / Company / Location / Salary Range**

## OVERALL MATCH SCORE: 78% ✅
**Recommendation:** STRONG FIT - Apply within 48 hours
**Application Priority / Estimated Competition / Time to Tailor**

## REQUIREMENTS BREAKDOWN
### Required Skills - 8/10 ✅   (list each ✅/❌ with "You have: ...")
### Preferred Skills - 4/6 ✅
### Soft Skills - 5/5 ✅

## STRENGTHS TO EMPHASIZE   (top 3 selling points)
## GAPS TO ADDRESS          (critical / major / minor + strategy for each)
## RESUME CUSTOMIZATION STRATEGY
  - Priority 1: Lead with most relevant experience (reorder roles)
  - Priority 2: Keyword integration (exact phrases from JD + where to add)
  - Priority 3: Quantify everything
## COVER LETTER TALKING POINTS (opening hook options + body match + gap handling)
## RED FLAGS ANALYSIS        (concerns, positive signals, company research needed)
## APPLICATION TIMELINE
## DECISION FACTORS          (reasons to apply / hesitate + overall recommendation)
```

(The full skill includes a complete worked example — see the source repo for the long-form template.)

## Requirement Classification Guide

**Language indicating REQUIRED:** "Must have...", "Required: X years of...", "Essential qualifications", listed under "Requirements", mentioned 3+ times.

**Language indicating PREFERRED:** "Nice to have...", "Bonus if you have...", "Preferred qualifications", "Ideally...", "A plus if...", mentioned only 1-2 times.

**Absolute dealbreakers (don't apply):** Required license you don't have, required clearance you can't get, years of experience 50%+ below requirement, required degree you don't have (when "required"), location you can't meet.

**Not dealbreakers (apply anyway):** Experience slightly below, "preferred" degree you don't have, nice-to-have tools you can learn, industry experience when you have transferable skills.

## Implementation Checklist

1. Extract all requirements (required vs preferred)
2. Identify all keywords (hard, soft, industry)
3. Calculate match score
4. Identify strengths to emphasize
5. Identify gaps and strategies to address
6. Detect red flags
7. Create resume customization plan
8. Generate cover letter talking points
9. Research company
10. Provide application recommendation and timeline

## Edge Cases
- **Vague JDs:** flag as potential red flag; extract what you can; recommend reaching out before applying.
- **Multiple roles in one JD:** identify core role vs "other duties"; flag scope creep.
- **Internal postings:** emphasize internal knowledge and cross-team relationships.
- **Reposted jobs:** research why (previous hire failed, role expanded); worth applying but check if requirements changed.
