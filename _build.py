import os, html
BASE="https://meltckr.github.io/zubin-ai"
CSS="""*{box-sizing:border-box}body{margin:0;font:17px/1.65 -apple-system,Segoe UI,Inter,sans-serif;color:#1b1d21;background:#fbfaf7}
a{color:#0b5fff}header,footer{max-width:820px;margin:auto;padding:18px 20px}header{display:flex;flex-wrap:wrap;gap:14px;align-items:center;border-bottom:1px solid #e6e3dc}
header .brand{font-weight:800;text-decoration:none;color:#111;margin-right:auto}header nav a{margin-left:14px;text-decoration:none;color:#444;font-size:15px}
main{max-width:820px;margin:auto;padding:24px 20px 60px}h1{font-size:2.1em;line-height:1.15;margin:.4em 0}h2{margin-top:1.8em}
.lede{font-size:1.15em;color:#444}.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;margin:18px 0}
.card{background:#fff;border:1px solid #e6e3dc;border-radius:10px;padding:16px;text-decoration:none;color:inherit}.card b{display:block;margin-bottom:4px}
.card span{color:#555;font-size:15px}.box{background:#fff;border:1px solid #e6e3dc;border-left:4px solid #0b5fff;border-radius:8px;padding:14px 18px;margin:18px 0}
code,pre{background:#f0eee8;border-radius:5px;padding:2px 5px;font-size:.92em}pre{padding:12px;overflow:auto;white-space:pre-wrap}
input,button{font:inherit;padding:10px 12px;border-radius:8px;border:1px solid #ccc}button{background:#111;color:#fff;border:0;cursor:pointer}button:disabled{opacity:.6}
footer{color:#777;font-size:14px;border-top:1px solid #e6e3dc}"""
NAV=[("Start here","start-here/"),("Guides","guides/"),("Use cases","use-cases/"),("Newsletter","newsletter/"),("Sponsor","sponsor/")]
pages=[]
def page(path,title,desc,body):
    depth=path.count("/")
    root="../"*depth
    nav="".join(f'<a href="{root}{u}">{n}</a>' for n,u in NAV)
    url=BASE+"/"+path
    doc=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | Zubin AI</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary"><link rel="stylesheet" href="{root}style.css"></head><body>
<header><a class="brand" href="{root}">Zubin AI</a><nav>{nav}</nav></header><main>{body}</main>
<footer>Zubin AI: plain-English guides to using and deploying AI agents. Independent; not affiliated with any tool mentioned. <a href="{root}sponsor/">Sponsor</a> · <a href="{root}llms.txt">llms.txt</a></footer></body></html>"""
    fp=os.path.join("site_new",path,"index.html"); os.makedirs(os.path.dirname(fp),exist_ok=True); open(fp,"w").write(doc); pages.append((path,title,desc))

G=[
("first-agent","Set up your first agent in one afternoon","Pick one tool, one job, and one folder. Get a real result before you get clever.","""
<p>Most people stall because they try to set up "an AI assistant for everything." Don't. Give your first agent one boring, repeatable job you already do by hand.</p>
<h2>1. Pick the tool by where the work lives</h2>
<ul><li><b>Work lives in code or files on your computer:</b> a coding agent like Claude Code, Codex, or Antigravity.</li>
<li><b>Work lives in email, calendar, Slack, docs:</b> a hosted assistant with connectors, like Grok Bot.</li>
<li><b>Not sure:</b> start hosted. Less setup, fewer ways to break your machine.</li></ul>
<h2>2. Write a one-page brief</h2><p>Every serious agent tool reads a standing instruction file (names vary: <code>CLAUDE.md</code>, <code>AGENTS.md</code>, a "memory" or "instructions" panel). Put in it: who you are, what the job is, what "done" looks like, and what it must never do.</p>
<pre>Job: Every weekday, summarize new emails from vendors into 5 bullets.
Done looks like: one message to me, under 120 words, links included.
Never: reply to anyone, delete anything, or spend money.</pre>
<h2>3. Run it by hand three times</h2><p>Before you automate anything, run the job manually and fix the brief after each run. Three clean runs in a row means it's ready for a schedule.</p>
<div class="box">Rule of thumb: if you can't describe "done" in one sentence, the agent can't hit it either.</div>"""),
("write-a-brief","Write instructions an agent actually follows","Short, specific, testable. How to write a brief that survives contact with real work.","""
<p>Agents don't fail because they're dumb. They fail because the instructions were a vibe.</p>
<h2>The four-part brief</h2><ol><li><b>Goal:</b> one sentence.</li><li><b>Inputs:</b> where to look, and where not to.</li><li><b>Output:</b> format, length, destination.</li><li><b>Limits:</b> what needs your approval, what's off limits forever.</li></ol>
<h2>Show, don't describe</h2><p>Five great examples beat a page of adjectives. Paste in your best past work and say "match this." It's the single biggest quality upgrade available.</p>
<h2>Ask for labeled guesses</h2><p>Tell the agent to mark each claim as <i>seen</i> (it checked), <i>inferred</i>, or <i>unknown</i>. You'll instantly know what to verify.</p>
<h2>Keep it current</h2><p>When the agent gets something wrong twice, that's a missing line in the brief. Add it. Briefs are living documents, not contracts.</p>"""),
("routines","Routines and schedules: make an agent show up on time","Turn a one-off task into a daily or weekly routine without it going off the rails.","""
<p>A routine is just a brief plus a clock. The hard part isn't the clock; it's making the output safe to receive while you're not watching.</p>
<h2>Start with a report, not an action</h2><p>Your first routine should only <b>read and summarize</b>: a morning digest, a weekly metrics roundup, a "what changed" check on a web page. Reports can be wrong without hurting anyone.</p>
<h2>Pick times you'll actually read</h2><p>Schedule it 15 minutes before you normally look. A 6:45a report you read at 7:00 builds the habit; a 3:00a report gets buried.</p>
<h2>Make silence meaningful</h2><p>Tell it: "If nothing changed, say so in one line." A routine that always writes an essay trains you to skip it.</p>
<h2>Review weekly</h2><p>Once a week, skim the last five runs. Kill routines you stopped reading. Fewer, sharper routines beat a noisy pile.</p>"""),
("connectors","Connectors: giving an agent access without giving it the keys","How to hook agents up to email, calendar, Slack, Drive, and GitHub safely.","""
<p>Connectors are what turn a chatbot into an assistant. They're also where the risk lives.</p>
<h2>Connect read-first</h2><p>Add one connector at a time. For the first week, use it only for reading: search, summarize, find. Writes (sending, editing, deleting) come later, behind approval.</p>
<h2>Use the official route</h2><p>Prefer the tool's built-in sign-in (OAuth) over pasting passwords or API keys into chat. If you must use a key, keep it in a config file the agent can use but never prints.</p>
<h2>Scope it down</h2><p>One folder, not the whole drive. One channel, not the whole workspace. One repo, not the whole account. You can always widen later.</p>
<h2>Know how to unplug</h2><p>Before connecting anything, find the "disconnect" or "revoke access" button. If you can't find it, don't connect it.</p>"""),
("approval-gates","Approval gates: let agents draft, keep the send button","The single most important safety habit: agents prepare, humans approve anything irreversible.","""
<p>The best setup we know: the agent does 95% of the work and stops one click short of anything you can't take back.</p>
<h2>What always needs a yes</h2><ul><li>Sending email, texts, or messages as you</li><li>Posting publicly</li><li>Spending money or starting a subscription</li><li>Deleting things or sharing files outside your account</li><li>Pushing code to production</li></ul>
<h2>Make approvals fast</h2><p>A gate only works if it's painless. Ask for drafts in a fixed format: who, what, why, and the exact text. You should be able to approve in ten seconds.</p>
<h2>Beware "auto-approve everything" modes</h2><p>Many coding agents offer a turbo or "full access" mode that skips prompts. It's fine in a throwaway sandbox. On a machine with your real files and keys, your written limits become the only guardrail. Use it knowingly, and switch back when the job's done.</p>
<div class="box">Write your yes/no rules down once, in the brief. Then you're approving actions, not re-litigating policy.</div>"""),
("multi-agent-desks","Multi-agent desks: when one assistant isn't enough","Split work into desks with clear lanes so agents stop stepping on each other.","""
<p>Once you have more than a handful of routines, one agent juggling everything gets sloppy. Split it into desks.</p>
<h2>One desk, one lane</h2><p>Examples: an Email desk (triage, drafts), a Research desk (briefings), a Build desk (code and sites), a Calendar desk (scheduling). Each has its own brief and its own connectors.</p>
<h2>One coordinator</h2><p>Have a single "front desk" agent you talk to. It hands work to the right desk and brings back results. You manage one conversation, not five.</p>
<h2>Shared notes, not shared chaos</h2><p>Give desks a shared folder for reference facts (your preferences, standing decisions). Keep each desk's working files separate.</p>
<h2>Different models for different jobs</h2><p>It's normal to use Claude Code for one build, Codex or Antigravity for another, and a hosted assistant for inbox work. Pick per job; don't marry a tool.</p>"""),
("cost-control","Cost control: keep agents from quietly burning money","Where agent costs come from and five habits that keep the bill boring.","""
<h2>Where the money goes</h2><ul><li>Subscriptions (the flat monthly plan)</li><li>Usage-based APIs that agents call (search, data, voice, image)</li><li>Hosting and "starter" plans you forgot you opened</li></ul>
<h2>Five habits</h2><ol><li><b>No new paid service without a yes.</b> Put it in the brief.</li><li><b>Cap usage-based keys</b> with the provider's spending limit, before you hand them over.</li><li><b>Test with fake data.</b> Tell build agents "no live API calls" until the logic works.</li><li><b>Monthly subscription sweep.</b> Have an agent list every recurring charge it can find; you cancel.</li><li><b>Use the smaller model for routine work.</b> Save the heavy model for hard problems.</li></ol>"""),
("coding-agents","Claude Code, Codex, Antigravity: a working comparison","How the main coding agents differ in practice, and how to pick for a given job.","""
<p>All of them can read a project, edit files, run commands, and fix their own errors. The differences are workflow, not magic.</p>
<h2>Claude Code</h2><p>Terminal and desktop app. Strong at exploring a messy codebase and multi-file changes. Reads <code>CLAUDE.md</code> for standing instructions.</p>
<h2>Codex</h2><p>CLI, editor, and a cloud mode that works in the background and opens a pull request for review. Reads <code>AGENTS.md</code>.</p>
<h2>Antigravity</h2><p>Google's agent-first editor. Lets you pick model and effort level, and has permission presets that control how often it stops to ask.</p>
<h2>How to pick</h2><ul><li>Want to watch every change? Terminal or editor agent.</li><li>Want to hand it off and review later? A background/cloud mode that opens a PR.</li><li>Second opinion? Give the same brief to two tools and compare.</li></ul>
<div class="box">Tools change monthly. Check each one's current docs for pricing and model names before committing.</div>"""),
("deploy-a-site","Deploy your first agent-built site for free","From prompt to a live public URL using GitHub Pages, without touching a server.","""
<ol><li>Ask your coding agent for a <b>static</b> site: plain HTML and CSS, no build step, mobile-friendly.</li>
<li>Have it create a GitHub repository and push the files.</li><li>In the repo's Settings &rarr; Pages, publish from the main branch. You get a <code>username.github.io/repo</code> URL.</li>
<li>Ask the agent to verify: every page returns status 200 and looks right on a phone.</li><li>Add the basics: page titles and descriptions, <code>sitemap.xml</code>, <code>robots.txt</code>, and <code>llms.txt</code> so AI tools can read your site cleanly.</li></ol>
<p>This site was built exactly that way.</p>"""),
("when-it-goes-wrong","When your agent goes wrong: a calm debugging checklist","Stalled, looping, confidently wrong, or did something you didn't ask for. What to check first.","""
<ol><li><b>Read what it actually did,</b> not what it said it did. Check the file, the sent folder, the log.</li>
<li><b>Find the missing instruction.</b> Most mistakes trace to a gap in the brief.</li><li><b>Shrink the task.</b> Split one big ask into three small ones.</li>
<li><b>Check access.</b> "I couldn't find it" often means a connector expired.</li><li><b>Start a fresh session</b> when it starts looping. Long conversations drift.</li>
<li><b>Tighten the gate.</b> If it did something irreversible, that action goes behind approval today.</li></ol>"""),
("finding-agent-tools","Finding agent tools worth your time","How to scout new agent tools and apps, and how to judge them before you hand over access.","""
<p>New agent tools launch every week. Names you'll run into include hosted assistants like Grok Bot, coding agents like Claude Code, Codex, and Antigravity, open agent projects like Hermes, and newer apps such as Muse, Dots, and Instinct. Features and pricing change fast, so treat this as a map, not a review, and <b>always check each tool's current docs</b> before you commit.</p>
<h2>Where to find them</h2><ul><li>Official changelogs and launch posts from the companies themselves</li><li>GitHub trending and the README of open-source projects</li><li>Practitioners on X and YouTube who show real setups, not just demos</li><li>App store listings, for consumer apps (read the privacy section)</li></ul>
<h2>Sort before you try</h2><ul><li><b>Hosted assistant:</b> lives in the cloud, connects to your apps.</li><li><b>Coding agent:</b> works in files and a terminal.</li><li><b>Open-source agent:</b> you run it yourself; more control, more setup.</li><li><b>Single-purpose app:</b> does one job well; easy to try, hard to extend.</li></ul>
<h2>Five-question test</h2><ol><li>Does it solve a job I already do every week?</li><li>What exactly can it read, and what can it send or change?</li><li>Can I require my approval before anything irreversible?</li><li>What does it cost at real usage, not the trial?</li><li>How do I export my data and disconnect it?</li></ol>
<div class="box">Try new tools on a low-stakes job with read-only access. Promote them only after a clean week.</div>"""),
("new-model-releases","How to take advantage of new model releases","A simple playbook for testing a new AI model against your real work instead of the hype.","""
<p>Every release comes with charts. Your work isn't a chart. Here's how to find out in an hour whether a new model actually helps you.</p>
<h2>1. Keep a personal test set</h2><p>Save 5 to 10 real tasks you care about with a known good answer: a brief you wrote, a bug you fixed, an email you'd send. This is your benchmark.</p>
<h2>2. Run old vs new side by side</h2><p>Same brief, same inputs, both models. Compare results blind if you can. Note speed and cost too.</p>
<h2>3. Look for new abilities, not just better scores</h2><p>Longer context, better tool use, cheaper speed tiers, or a new effort setting can unlock jobs that weren't worth automating before.</p>
<h2>4. Switch one routine at a time</h2><p>Move a single low-risk routine to the new model for a week. Keep the old one ready to switch back.</p>
<h2>5. Re-check your briefs</h2><p>Newer models often follow instructions more literally. Lines you added to work around an old model's quirks may now cause problems. Trim them.</p>
<div class="box">Model names, prices, and limits change constantly. Confirm details in the provider's current docs before you rely on them.</div>"""),
]
for slug,t,d,b in G: page(f"guides/{slug}/",t,d,f"<p><a href='../'>&larr; All guides</a></p><h1>{t}</h1><p class='lede'>{d}</p>{b}")
cards=lambda items,pre: '<div class="cards">'+"".join(f'<a class="card" href="{pre}{s}/"><b>{t}</b><span>{d}</span></a>' for s,t,d,_ in items)+'</div>'
page("guides/","Guides","Practical how-to guides for using and deploying AI agents.","<h1>Guides</h1><p class='lede'>Practical, tested, plain English. Pick the one that matches what you're stuck on.</p>"+cards(G,""))
page("start-here/","Start here","A beginner's path to getting real work out of AI agents in your first week.","""<h1>Start here</h1><p class="lede">An agent is an AI that can take steps for you: read your files, use your apps, and come back with finished work. Here's the shortest path from curious to useful.</p>
<h2>Your first week</h2><ol><li><b>Day 1:</b> <a href="../guides/first-agent/">Set up one agent for one job.</a></li><li><b>Day 2:</b> <a href="../guides/write-a-brief/">Write a brief it can follow.</a></li>
<li><b>Day 3:</b> <a href="../guides/approval-gates/">Decide what needs your yes.</a></li><li><b>Day 4:</b> <a href="../guides/connectors/">Connect one app, read-only.</a></li><li><b>Day 5:</b> <a href="../guides/routines/">Put it on a schedule.</a></li></ol>
<h2>Three beliefs that save you time</h2><ul><li>Specific beats smart. A clear brief beats a better model.</li><li>Drafts are free; sends are forever. Keep the send button.</li><li>One job done every day beats ten jobs done once.</li></ul>""")
U=[("Morning briefing","Calendar, important email, and today's top three priorities in one message before 7am."),("Inbox triage","Sort, label, archive the noise, and draft replies you approve."),("Meeting prep","A one-page brief on who you're meeting and what's open between you."),("Meeting follow-up","Turn a recorded call into decisions, owners, and draft follow-ups."),("Subscription sweep","Find every recurring charge so you can cancel what you forgot."),("Web page watcher","Tell me when a price, policy, or competitor page changes."),("Content repurposing","Turn one long piece into a short post, an email, and an audio version."),("Personal dashboard","A private web page that shows your projects and daily priorities."),("Code maintenance","Fix small bugs, update dependencies, and open a pull request for review."),("Research digest","A weekly roundup on one topic with sources and labeled guesses."),("Reminders that matter","Renewals, appointments, and deadlines put on your calendar with the link attached."),("Team pulse","Post a quick survey in a team channel and tally the answers for you.")]
page("use-cases/","Use-case library","Real, everyday jobs people hand to AI agents, with where to start.","<h1>Use-case library</h1><p class='lede'>Jobs that work well today. Each one starts read-only and keeps sends behind your approval.</p><div class='cards'>"+"".join(f"<div class='card'><b>{a}</b><span>{b}</span></div>" for a,b in U)+"</div><p>Not sure how to start one? <a href='../guides/first-agent/'>Set up your first agent.</a></p>")
page("newsletter/","Newsletter","A short weekly email with one useful agent setup you can copy.","""<h1>The Zubin AI newsletter</h1><p class="lede">One practical agent setup a week. Five minutes to read, copy-paste ready.</p>
<form onsubmit="event.preventDefault();this.querySelector('p').hidden=false"><input type="email" placeholder="you@example.com" required aria-label="Email"> <button type="submit">Join the list</button>
<p hidden><b>Thanks!</b> Signups open soon. Nothing was sent or saved yet.</p></form><p style="color:#777;font-size:14px">Coming soon. This form doesn't collect or store emails yet.</p>""")
page("sponsor/","Sponsor Zubin AI","Reach people who are actually setting up and running AI agents.","""<h1>Sponsor Zubin AI</h1><p class="lede">Our readers are builders and operators putting agents to work. Sponsorships are opening soon.</p>
<ul><li>One sponsor per newsletter issue, clearly labeled</li><li>We only accept tools we'd recommend to a friend</li><li>Sponsors never edit guide content</li></ul><p>Sponsorship details and booking are coming soon.</p>""")
page("","Zubin AI: plain-English guides to using AI agents","Learn to set up, run, and safely deploy AI agents like Grok Bot, Claude Code, Codex, Antigravity, and more. Practical guides, no jargon.",
"""<h1>Put AI agents to work. Keep your hand on the wheel.</h1><p class="lede">Plain-English guides to setting up, scheduling, connecting, and safely running AI agents, from people who run them every day.</p>
<p><a class="card" style="display:inline-block" href="start-here/"><b>New here? Start here &rarr;</b><span>Your first useful agent in a week.</span></a></p>
<h2>Popular guides</h2>"""+cards(G[:6],"guides/")+"""<p><a href="guides/">See all guides &rarr;</a> · <a href="use-cases/">Browse use cases &rarr;</a></p>""")
open("site_new/style.css","w").write(CSS); open("site_new/.nojekyll","w").write("")
open("site_new/robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open("site_new/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{BASE}/{p}</loc><lastmod>2026-10-13</lastmod></url>\n" for p,_,_ in pages)+"</urlset>\n")
open("site_new/llms.txt","w").write("# Zubin AI\n\n> Plain-English guides to using and deploying AI agents (Grok Bot, Claude Code, Codex, Antigravity and more).\n\n## Pages\n"+"".join(f"- [{t}]({BASE}/{p}): {d}\n" for p,t,d in pages))
open("site_new/404.html","w").write('<!doctype html><meta charset="utf-8"><title>Not found | Zubin AI</title><p>Page not found. <a href="/zubin-ai/">Go home</a>.</p>')
