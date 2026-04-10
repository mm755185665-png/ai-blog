---
title: "How to Use Midjourney: Complete Guide (2026) — 10 Steps from Zero to First Image, with Error Fixes"
date: 2026-04-10
tags: ["how to use Midjourney", "Midjourney tutorial", "AI image generation", "Midjourney prompts"]
difficulty: "Beginner"
summary: "Step-by-step Midjourney tutorial for beginners: account setup, subscription, prompts, parameters, image-to-image, and common error fixes."
cover: "/ai-blog/covers/midjourney.png"
---

title: "How to Use Midjourney: Complete Guide (2026) — 10 Steps from Zero to First Image, with Error Fixes"
summary: "Step-by-step Midjourney tutorial for beginners: account setup, subscription, prompts, parameters, image-to-image, and common error fixes."
tags: ["how to use Midjourney", "Midjourney tutorial", "AI image generation", "Midjourney prompts"]
---

First time opening Midjourney and completely lost by the all-English interface and Discord's unfamiliar layout?

This guide is written for you. I'll walk through **how to use Midjourney** from scratch, in the exact order you'll actually do things — registration, payment, writing prompts, tweaking parameters, and image-to-image. Every step has concrete instructions, and if you hit an error, you can cross-reference the troubleshooting section. Follow along once and you'll have your first image by the end of the day.

---

**TL;DR:** Register on Discord → link your Midjourney account → pick a subscription plan → type `/imagine` + your prompt → wait for the image. The whole flow takes under 20 minutes. The two biggest hurdles are your network setup and payment method.

---

## 1. Before You Start: What You Need

A lot of people get stuck at step one — not because it's hard, but because they didn't set up their environment first. Get these three things sorted and everything else goes much smoother.

### 1.1 Network Requirements

Both midjourney.com and Discord are blocked in mainland China, so **you'll need a reliable VPN for the entire process**.

A few practical notes:

- When registering on Discord, use a global proxy — browser-only proxies tend to fail
- US, Japan, or Singapore nodes are recommended for low latency and stability
- If your connection drops mid-generation, the job won't be cancelled — just re-enter the channel to find your results

If your network is unstable, test that you can open discord.com normally before starting the registration process.

### 1.2 Which Email to Use

Discord requires email verification. Use **Gmail or Outlook** — domestic Chinese email providers (QQ, 163) sometimes don't receive verification emails or get flagged as suspicious accounts.

After registering, it's worth binding a phone number right away to reduce the chance of your account getting suspended. Discord supports mainland China numbers (+86), though some carriers may not receive the SMS. Fallback options include Google Voice or another international number.

### 1.3 Two Ways In: Web App vs. Discord

Midjourney launched a standalone web app in late 2023. **Beginners should start with the web app** — the interface is more intuitive and you don't need to memorize any commands.

| Entry Point | URL | Best For |
|-------------|-----|----------|
| Web app | midjourney.com | Beginners, everyday use |
| Discord | discord.com/invite/midjourney | Batch operations, community |

Both share the same account and subscription — image credits are pooled, so use whichever you prefer.

---

## 2. Creating Your Account: Discord + Midjourney Setup

Midjourney doesn't have its own account system — you log in by authorizing your Discord account. So the first step is registering on Discord, then using it to sign into Midjourney.

### 2.1 Register on Discord

1. Go to [discord.com](https://discord.com), click "Login" → "Register" in the top right
2. Fill in your username, email, password, and date of birth (must be 18+)
3. Complete the CAPTCHA (puzzle or image click)
4. Click the verification link in your email to activate your account
5. Return to Discord, finish the onboarding flow, and you're in

Once registered, go to "User Settings → My Account" and bind your phone number. This improves account security and reduces how often you'll be asked for two-factor verification.

### 2.2 Link Your Midjourney Account

1. Go to [midjourney.com](https://www.midjourney.com)
2. Click "Sign In" in the bottom right
3. Select "Continue with Discord"
4. Discord will show an authorization prompt — click "Authorize"
5. You'll be redirected back to the Midjourney web app, now logged in

If the authorization page keeps loading, check that your proxy is set to global mode.

### 2.3 Choosing a Subscription Plan

**Midjourney no longer has a free tier** — you need a subscription to generate images. Here are the 2026 prices:

| Plan | Monthly | Annual (per month) | Fast GPU Hours | Best For |
|------|---------|-------------------|----------------|----------|
| Basic | $10/mo | $8/mo | 3.3 hrs | Light use |
| Standard | $30/mo | $24/mo | 15 hrs + unlimited Relax | Daily use |
| Pro | $60/mo | $48/mo | 30 hrs + Stealth mode | Commercial use |
| Mega | $120/mo | $96/mo | 60 hrs | Heavy users |

**Beginners: start with Basic ($10/mo).** Get comfortable with the workflow first, then upgrade to Standard if you need more.

Payment: Visa/Mastercard are accepted. Some users report that Chinese dual-currency cards fail intermittently — virtual cards like Depay or Wise tend to have higher success rates. Alipay and WeChat Pay are not supported.

To subscribe: click your avatar in the bottom left of the Midjourney web app → "Manage Subscription" → choose a plan → enter payment details.

---

## 3. Your First Image: Using the /imagine Command

Once your account and subscription are set up, you're ready to generate your first image.

### 3.1 Generating Images in the Web App (Recommended for Beginners)

1. Log into midjourney.com and go to the main interface
2. There's an input box at the bottom of the page — type your description directly into it
3. Press Enter or click the send button
4. Wait about 30–60 seconds — the page will show 4 candidate images
5. Click an image to enlarge it, then choose U1–U4 (upscale a single image) or V1–V4 (generate variations)

The web app doesn't require `/imagine` — just type your description directly. That's one of the main advantages over Discord.

### 3.2 Generating Images in Discord

1. Join the official Midjourney Discord server, or add the Midjourney Bot to your own server
2. In any channel, type `/imagine` and wait for the command prompt to appear
3. Enter your description in the `prompt` field
4. Press Enter and wait for the bot to reply with your images

**Common beginner mistake:** typing directly in the channel without triggering `/imagine` first. The bot won't respond unless you use the slash command.

### 3.3 Writing Your First Prompt

For your first image, a simple English description is all you need — no complex parameters required. For example:

```
a cat sitting on a wooden table, soft morning light, photorealistic
```

Midjourney can understand Chinese prompts, but results are less consistent than with English. It's worth getting into the habit of writing prompts in English.

If you're not comfortable with English, just translate your Chinese description with a translation tool and paste it in.

---

## 4. How to Write Prompts

Prompts are the single biggest factor in image quality. With the same tool, a well-written prompt versus a vague one can produce dramatically different results.

### 4.1 Basic Structure

The basic structure of a Midjourney prompt is:

```
[subject] + [scene/environment] + [style/mood] + [parameters]
```

Example:

```
a young woman reading a book, cozy coffee shop interior, warm golden hour lighting, film photography style --ar 3:4 --v 6.1
```

Breaking it down:
- Subject: `a young woman reading a book`
- Scene: `cozy coffee shop interior`
- Style: `warm golden hour lighting, film photography style`
- Parameters: `--ar 3:4 --v 6.1`

The more specific your description, the more predictable the output. Vague words like `beautiful` or `nice` have very little effect — replace them with concrete visual descriptions like `soft diffused light` or `shallow depth of field`.

If you want to systematically improve your prompting skills, check out this [Complete Guide to AI Prompt Techniques](https://mm755185665-png.github.io/ai-blog/zh/posts/2026-03-31-ai-09f249/) — it covers cross-tool prompt strategies in depth.

### 4.2 Style Keywords Quick Reference

| Style | Common Keywords |
|-------|----------------|
| Photorealistic | photorealistic, DSLR photo, 35mm film, shot on Canon |
| Illustration | digital illustration, flat design, vector art |
| Anime | anime style, Studio Ghibli, manga |
| Oil painting | oil painting, impressionist, brushstroke texture |
| Cyberpunk | cyberpunk, neon lights, futuristic city |
| Minimalist | minimalist, clean background, white space |
| Watercolor | watercolor, soft edges, pastel colors |
| 3D render | 3D render, Blender, octane render, CGI |

### 4.3 Controlling Element Weight

When your prompt has multiple elements and you want to emphasize one, use double colons `::` followed by a number:

```
red rose::2 blue sky::1
```

This gives the red rose twice the weight of the blue sky, so it'll be more prominent in the output.

Higher numbers increase an element's presence in the image. Negative weights (`::−1`) effectively exclude an element, though the `--no` parameter is usually more straightforward for that.

---

## 5. Essential Parameters Quick Reference (The 6 You'll Use Most)

Parameters go at the end of your prompt, prefixed with `--`. Master these 6 and you'll cover 90% of use cases.

| Parameter | What It Does | Common Values | Example |
|-----------|-------------|---------------|---------|
| `--ar` | Sets the aspect ratio | 1:1 / 16:9 / 3:4 / 9:16 | `--ar 16:9` |
| `--v` | Specifies the model version | 6.1 (current main version) | `--v 6.1` |
| `--stylize` | Artistic intensity — higher = more stylized | 0–1000, default 100 | `--stylize 300` |
| `--chaos` | Output variety — higher = more random | 0–100, default 0 | `--chaos 30` |
| `--seed` | Fixes the random seed to reproduce similar results | Any integer | `--seed 12345` |
| `--no` | Excludes unwanted elements | Any word or phrase | `--no text, watermark` |

**Practical use cases:**

- Phone wallpaper → `--ar 9:16`
- Landscape banner/cover → `--ar 16:9`
- Want more creative results → `--chaos 50` or higher
- Found a good image and want to fine-tune it → use `/show` to get the seed, then lock it with `--seed`
- Text or watermarks keep appearing → add `--no text, watermark, logo`

---

## 6. Advanced: Image-to-Image (Using a Reference Image)

### 6.1 What Is Image-to-Image?

Image-to-image (sometimes called "image prompting" or "img2img") means feeding a reference photo as input so Midjourney generates something based on it. Common uses:

- Keep the composition or color palette of an existing image, but change the style
- Use a product photo to generate lifestyle/scene mockups
- Reference a character's appearance to generate different poses or outfits

### 6.2 How to Do It

**Web app:**
1. Click the image upload icon to the left of the input box
2. Upload your local image and wait for it to finish uploading
3. The image URL will be automatically inserted into the input box
4. Continue typing your prompt after the link and send

**Discord:**
1. Drag an image into the channel input box, or click "+" to upload
2. Send the image and wait for it to upload
3. Right-click the uploaded image and select "Copy Link" to get the URL
4. Type `/imagine`, then in the prompt field paste the image URL, add a space, and write your description

Format example:
```
https://cdn.discordapp.com/xxx.jpg a woman in a red dress, studio lighting --iw 0.8
```

### 6.3 The `--iw` Parameter

`--iw` (Image Weight) controls how much the reference image influences the final output. Range is 0–3, default is 1.

- `--iw 0.5`: Reference image has less influence; your text prompt leads
- `--iw 1`: Default balance between reference image and text prompt
- `--iw 2`: Reference image has strong influence; output will closely follow the original composition and colors

**Practical tip:** On your first try, leave out `--iw` and use the default. If the result feels too different from your reference, increase it. If it feels too similar with no real change, decrease it.

---

## 7. Common Issues & Error Troubleshooting FAQ

### Q1: I sent a prompt but the bot didn't respond at all. What's wrong?

**The most common cause is sending in the wrong channel, or not triggering the `/imagine` command.**

Check these:
1. Confirm you're in a channel where the Midjourney Bot is present (Discord)
2. Confirm you typed `/imagine` first — not just plain text
3. If using the web app, refresh the page and try again
4. Check that your network and proxy are working

If all of the above look fine, Midjourney's servers may be temporarily congested. Wait a few minutes and try again.

---

### Q2: My images look blurry or distorted. How do I improve quality?

**The main culprit is usually a prompt that's too short or too vague.** Try:

1. Add specific visual details — lighting, materials, composition
2. Add `--v 6.1` to make sure you're using the latest model
3. Increase `--stylize` (e.g., `--stylize 200`)
4. For distorted figures, add `--no deformed, ugly, bad anatomy`

---

### Q3: Image upload keeps spinning and never finishes. How do I fix it?

**Almost always a network issue.** Try:

1. Check that your proxy is stable — switch nodes and retry
2. Compress the image (keep it under 5MB)
3. Convert to JPG format (PNG can be slower to upload)
4. In Discord, try uploading the image to another channel first, then copy the link

---

### Q4: I can't access the Midjourney Discord server — it says I need to verify. What do I do?

**Discord has security verification for new accounts.** Steps to resolve:

1. Complete email verification and bind your phone number
2. After joining the server, confirm the rules in the "Rules" channel
3. If it says to wait, it usually unlocks within 10 minutes automatically
4. Accounts less than 24 hours old may also trigger restrictions — wait a day and try again

---

### Q5: My payment keeps failing and my credit card is being declined. What should I do?

**Chinese credit cards (including dual-currency cards) have inconsistent success rates on Midjourney.** Recommended options:

1. Use a virtual card like Depay, Wise, or OneKey Card — much higher success rate
2. Make sure your card has enough balance (leave a $2–3 buffer)
3. Use a US billing address (any US address works)
4. If it keeps failing, try a different browser or clear your cookies and retry

---

### Q6: How do I check how many image credits I have left?

**In Discord, type `/info`** and the bot will reply with your account details, including:

- Current subscription plan
- Remaining Fast GPU hours
- Relax mode status
- Usage so far this month

In the web app, click your avatar in the bottom left → "Manage Subscription" to see detailed usage stats.

---

## 8. Quick-Start Checklist (10 Steps)

Check these off in order — make sure each step is done before moving to the next:

- [ ] **Step 1:** Confirm your VPN is working and you can open discord.com
- [ ] **Step 2:** Register a Discord account using Gmail or Outlook
- [ ] **Step 3:** Complete email verification and bind your phone number
- [ ] **Step 4:** Go to midjourney.com, click "Sign In with Discord," and authorize
- [ ] **Step 5:** Go to "Manage Subscription," select the Basic plan ($10/mo), and complete payment
- [ ] **Step 6:** Return to the Midjourney web app and type your first prompt in the bottom input box
- [ ] **Step 7:** Wait for your images (about 30–60 seconds) and review the 4 candidates
- [ ] **Step 8:** Click an image you like and choose U (upscale) or V (variation) for further refinement
- [ ] **Step 9:** Try adding `--ar 16:9 --v 6.1` to the end of a prompt to see how parameters work
- [ ] **Step 10:** Try uploading a reference image and use it as an image prompt

Once you've completed all 10 steps, you've got the core Midjourney workflow down.

---

## Summary

**How to use Midjourney** comes down to this: set up your network → register on Discord → link Midjourney and subscribe → generate images with `/imagine` or the web app input box → refine results with parameters and better prompts.

The two places people most commonly get stuck are the network setup and payment. Everything else in this guide should go smoothly if you follow the steps in order. If you hit an error, check Section 7's FAQ first — it covers 90% of common issues.

If you want to see how Midjourney stacks up against other AI image tools, this [2026 Comprehensive Review of the Best AI Image Generators: 8 Tools Compared](https://mm755185665-png.github.io/ai-blog/zh/posts/2026-03-30-ai-54628f/) can help you decide whether Midjourney is the right fit for you.

If this guide was helpful, feel free to bookmark it. Got questions or experience with other tools to share? Drop a comment below.