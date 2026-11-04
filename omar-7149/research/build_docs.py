# Generates the email-sequence and ad-script pages from one spine.
import html, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS='''<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--ink:#14261f;--ink2:#4c5f57;--em:#0f5c45;--gold:#b8892f;--paper:#f6efe2;--card:#fffdf8;--line:rgba(20,38,31,.1)}
*{box-sizing:border-box}html,body{max-width:100%;overflow-x:hidden}
body{margin:0;background:radial-gradient(60% 40% at 50% 0%,rgba(184,137,47,.14),transparent 70%),var(--paper);color:var(--ink);font:16px/1.65 Manrope,system-ui,sans-serif}
.wrap{max-width:820px;margin:0 auto;padding:64px 20px 80px}
.top{text-align:center;margin-bottom:40px}
.eb{font:800 12px/1 Manrope;letter-spacing:.22em;text-transform:uppercase;color:var(--gold)}
h1{font:600 clamp(32px,5vw,48px)/1.08 Fraunces,Georgia,serif;margin:14px 0 12px;letter-spacing:-.015em}
.top p{color:var(--ink2);max-width:56ch;margin:0 auto}
.tabs{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:26px 0 0}
.tabs span{font:700 12.5px Manrope;padding:8px 14px;border-radius:999px;background:#fff;border:1px solid var(--line);color:var(--ink2)}
.tabs span.on{background:var(--em);color:#fff;border-color:var(--em)}
.grp{font:800 12px/1 Manrope;letter-spacing:.18em;text-transform:uppercase;color:var(--em);margin:40px 0 14px;display:flex;align-items:center;gap:12px}
.grp::after{content:"";flex:1;height:1px;background:var(--line)}
.mail{background:var(--card);border:1px solid var(--line);border-radius:18px;margin-bottom:16px;overflow:hidden;box-shadow:0 18px 40px -30px rgba(20,38,31,.4)}
.mh{display:grid;grid-template-columns:46px 1fr auto;gap:14px;align-items:center;padding:18px 22px;border-bottom:1px solid var(--line);cursor:pointer}
.mh img{width:42px;height:42px;border-radius:50%;object-fit:cover}
.mh .n{font:800 12px Manrope;color:var(--gold);letter-spacing:.1em}
.mh b{display:block;font-size:16.5px;line-height:1.35}
.mh small{color:var(--ink2);font-size:13.5px}
.when{font:700 11.5px Manrope;padding:6px 10px;border-radius:999px;background:rgba(15,92,69,.08);color:var(--em);white-space:nowrap}
.mb{padding:20px 26px 24px 82px;color:#2b3a34}
.mb p{margin:0 0 12px}
.mail.closed .mb{display:none}
.tag{display:inline-block;font:700 11px Manrope;padding:3px 8px;border-radius:6px;background:rgba(184,137,47,.14);color:#7a5a17;margin-left:6px}
.ad{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px 26px;margin-bottom:16px}
.ad h3{font:600 22px/1.25 Fraunces,serif;margin:6px 0 14px}
.ad .row{display:grid;grid-template-columns:90px 1fr;gap:14px;padding:10px 0;border-top:1px solid var(--line)}
.ad .row b{font:800 11px/1.8 Manrope;letter-spacing:.14em;text-transform:uppercase;color:var(--em)}
.ad .row div p{margin:0 0 8px}
@media(max-width:600px){.mb{padding:18px 20px}.mh{grid-template-columns:40px 1fr}.when{grid-column:2;justify-self:start}.ad .row{grid-template-columns:1fr;gap:4px}}
</style>'''
def page(title,eb,lead,tabs,body,folder):
    t=''.join(f'<span class="{"on" if i==tabs[1] else ""}">{x}</span>' for i,x in enumerate(tabs[0])) if tabs else ''
    out=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>{html.escape(title)} · Unshakeable Method</title>{CSS}</head>
<body><div class="wrap"><div class="top"><span class="eb">{eb}</span><h1>{title}</h1><p>{lead}</p><div class="tabs">{t}</div></div>{body}</div>
<script>document.querySelectorAll('.mh').forEach(function(h){{h.onclick=function(){{h.parentNode.classList.toggle('closed')}}}})</script></body></html>'''
    open(os.path.join(ROOT,folder,'index.html'),'w').write(out)
def mails(seq,start=1,grp=None):
    o=f'<div class="grp">{grp}</div>' if grp else ''
    for i,(when,subj,prev,body) in enumerate(seq,start):
        ps=''.join(f'<p>{p}</p>' for p in body.strip().split('\n'))
        o+=f'''<article class="mail{" closed" if i>start else ""}"><div class="mh"><img src="../assets/img/omar-avatar.jpg" alt=""><div><span class="n">EMAIL {i:02d}</span><b>{subj}</b><small>{prev}</small></div><span class="when">{when}</span></div><div class="mb">{ps}</div></article>'''
    return o
P1="The Officeless Agency: sell a service you don't deliver and sign your first client in 30 days"
P2="The 6-step hiring system that gets the work done in under an hour a day, so your 9-to-5 stays safe"
P3="The 3-ETF halal portfolio behind Omar's $1.6M, and how to auto-invest your agency profit into it"
LIVE="Tuesday 17 November at 7pm Dubai (3pm London)"
SIG="Omar"
pre=[
("Instantly","Action required: reply YES to confirm your spot","Salam {FIRST NAME}, one quick thing before Tuesday",f"""Salam {{FIRST NAME}},
You're registered for the Halal Freedom Masterclass, {LIVE}.
Can you do one thing for me? Hit reply and type YES. It tells your inbox my emails are wanted, so the live link doesn't end up in spam.
Then join the WhatsApp group: [WHATSAPP LINK]. Your Halal Freedom Number Calculator is waiting in there.
See you Tuesday,
{SIG}"""),
("Day 1 · 6pm","I didn't have a skill. I still made $2M.","How my first agency started with someone else's talent","""Salam {FIRST NAME},
In 2017 I was employed in Europe and trying every business model I could find. All of them failed.
Then I paid a mentor who freelanced remotely. I couldn't do what he did, so I asked if I could find him clients and resell his work. He said yes.
That was my first agency. Over the next five years it made more than $2M in profit, and I ran it in under an hour a day.
On Tuesday I'll show you the exact model, and why you don't need a skill of your own to start it.
Omar"""),
("Day 2 · 6pm","Is this actually halal?","The question I get more than any other","""Salam {FIRST NAME},
It's the first thing people ask me, and it's the right question.
You're selling a real service to a real business. The client knows what they're paying for, the freelancer is paid fairly for their work, and you're paid for finding the client and managing the project. No interest, no gharar, nothing hidden.
I'll walk through it properly on Tuesday, including the services I'd stay away from.
Omar"""),
("Day 3 · 6pm","\"I don't have the time\"","Your job takes everything. I know.","""Salam {FIRST NAME},
If your job already takes ten hours a day, the last thing you need is a second job.
That's why the agency only works if other people do the work. On Tuesday I'll show you the 6-step hiring system I use so freelancers deliver on time and don't ghost, and how the whole thing fits into about an hour a day.
Omar"""),
("Day 4 · 6pm","Where I actually keep my money","The 3 funds behind my portfolio","""Salam {FIRST NAME},
Income is half of it. The other half is what happens to the money once it lands.
Most of my wealth sits in three Shariah-screened funds and five properties. No riba, no gambling stocks, nothing I'd be uncomfortable explaining.
On Tuesday I'll show you the three ETFs, and how to make your agency profit flow into them every month without thinking about it. Open your Freedom Number Calculator before then, so you know your starting point.
Omar"""),
("Day before · 10am","Tomorrow: the three things I'll teach you","Bring a notebook",f"""Salam {{FIRST NAME}},
Tomorrow, {LIVE}, here's what we'll cover:
1. {P1}
2. {P2}
3. {P3}
Stay to the end. There's a second gift for everyone who does.
Omar"""),
("Day of · 9am","Tonight at 7pm Dubai","The link goes in the WhatsApp group","""Salam {FIRST NAME},
It's today. 7pm Dubai, 3pm London.
I'll post the link in the WhatsApp group an hour before, and here too. Find somewhere quiet for 90 minutes. Your future self will thank you.
Omar"""),
("1 hour before","We start in one hour","Here's your link","""Salam {FIRST NAME},
One hour to go. Here's your link: [LIVE LINK]
Come with one question you want answered. I'll stay after for Q&A.
Omar"""),
("Live now","We're live","Join now: [LIVE LINK]","""We're live, {FIRST NAME}.
Join here: [LIVE LINK]
I'm starting with a quick quiz, so don't miss the first five minutes.
Omar"""),
]
post_a=[
("+1 hour","The replay (and your next step)","Thank you for staying, {FIRST NAME}","""Salam {FIRST NAME},
JazakAllah khair for staying tonight. Here's the replay if you want to go over anything again: [REPLAY LINK]
If you'd like help doing this properly, answer four questions under the replay and book a call with my team. We'll map your agency and your freedom date with you.
Omar"""),
("+1 day","The question that came up most","\"Can I really do this next to my job?\"","""Salam {FIRST NAME},
Most of the questions last night were a version of the same one: can I really do this next to my job?
Yes, if you build it the way I showed you. Outreach in the first 30 days, freelancers doing the delivery after that, about an hour a day. The people who struggle are the ones who try to do the work themselves.
If you want us to build it with you, book here: [APPLY LINK]
Omar"""),
("+2 days","What 90 days actually looks like","Day 1 to day 90, step by step","""Salam {FIRST NAME},
In the Unshakeable Method, days 1 to 30 are about one thing: your first paying client. Days 31 to 60, handing the work to the Freelancer Bench and adding clients. Days 61 to 90, setting up your halal portfolio and the auto-invest.
You get a coach, a weekly call with me and the do the work guarantee.
15 places this cohort: [APPLY LINK]
Omar"""),
("+3 days","The replay comes down tonight","Last chance to watch it","""Salam {FIRST NAME},
The replay comes down at midnight. If there's one part you wanted to rewatch, now's the time: [REPLAY LINK]
And if you already know you want help, book your call: [APPLY LINK]
Omar"""),
]
post_n=[
("+1 hour","You missed it, here's the replay","90 minutes, worth it","""Salam {FIRST NAME},
Life happens. Here's the replay of the Halal Freedom Masterclass: [REPLAY LINK]
Watch it before Friday, it comes down after that.
Omar"""),
("+1 day","The three secrets in three minutes","If you only read one email this week","""Salam {FIRST NAME},
Short version of what you missed:
1. You don't need a skill. You need clients, and freelancers already have the skill.
2. A paid test before you hire anyone is what keeps it to an hour a day.
3. Three halal ETFs and an auto-invest on the 1st of every month.
The full thing is here, with the application under it: [REPLAY LINK]
Omar"""),
("+3 days","Coming down tonight","The replay disappears at midnight","""Salam {FIRST NAME},
Last reminder. The replay is gone at midnight: [REPLAY LINK]
Omar"""),
]
pc=[
("On booking","You're booked. Here's how to prepare","Two minutes of prep makes the call twice as useful","""Salam {FIRST NAME},
Your call with my team is booked for {CALL TIME}.
Before it, open your Halal Freedom Number Calculator and write down three numbers: your monthly take-home, what you save, and your freedom number. We'll build your plan from those.
Omar"""),
("+1 day","Watch this before your call","8 minutes on how the agency works","""Salam {FIRST NAME},
If you only watch one video before your call, make it this one: [VIDEO LINK]
It's the model from start to finish, so we can spend the call on your plan, not the basics.
Omar"""),
("+2 days","What happens on the call","No pressure, no script","""Salam {FIRST NAME},
Here's how the call works. My team will ask about your job, your time and your goals, then sketch your first 90 days: which service, which clients, and when your portfolio starts.
If the Unshakeable Method isn't the right fit, they'll tell you. Honestly.
Omar"""),
("+3 days","\"Is this for someone like me?\"","The honest answer","""Salam {FIRST NAME},
Almost everyone asks this before their call.
The people who get results aren't the ones with the most skill or the most spare time. They're the ones who do the outreach in the first 30 days.
{{SWAP: 1 to 3 real student stories}}
Omar"""),
("Day of · 9am","Your call is today","{CALL TIME}","""Salam {FIRST NAME},
Your call is today at {CALL TIME}. Join from a laptop if you can, somewhere quiet, with your three numbers to hand.
Omar"""),
("1 hour before","See you in an hour","Here's the link","""Salam {FIRST NAME},
One hour. Here's the link: [CALL LINK]
Omar"""),
]
page('Pre-webinar','Email sequence · 9 emails','Registration to live. Each email answers one real question before Tuesday: is it halal, do I have the time, where does the money go.',None,mails(pre),'pre-webinar')
page('Post-webinar','Email sequence · 7 emails','Split by who showed up. Attendees get the next step, no-shows get the replay in short form.',None,mails(post_a,1,'Attended · 4 emails')+mails(post_n,5,'Didn\'t attend · 3 emails'),'post-webinar')
page('Pre-call','Email sequence · 6 emails','Booked to call. Walks the applicant in prepared, with their numbers and the model already understood.',None,mails(pc),'pre-call')
ads=[
("01 · The quiz","Belief: you need a skill","\"True or false: to make halal money online, you need a skill to sell. False. I made $2M+ without one.\"","Talking head, Omar at the desk. Quick cut to the agency flow graphic (client pays $1,500 → freelancer paid $600 → you keep $900).","\"I'll show you the exact model live, free, on Tuesday. Link below.\""),
("02 · The calculator","Years to freedom","\"If you have $500 a month to invest, it takes about 31 years to replace your salary. Here's how to cut that to nine.\"","Screen recording of the Freedom Number Calculator. Bars shrink: 31 yrs → 17 yrs → 9 yrs as agency income is added.","\"Get the calculator free when you register for my live training.\""),
("03 · The 9-to-5","Time objection","\"You don't need to quit your job to start a business. I'd actually tell you not to.\"","Omar walks through his one hour: 15 minutes client messages, 30 reviewing delivery, 15 outreach. B-roll of laptop at a café.","\"I'll show you the hiring system that makes this possible. Free, Tuesday.\""),
("04 · The portfolio","Halal investing","\"This is my exact halal portfolio. Three ETFs. No interest, no haram stocks.\"","Reuse the pinned-reel format. Portfolio screen blurred, three fund types labelled. Then: 'but you need income to feed it first.'","\"I'll show you how to fund it from an agency you run on the side. Save your seat.\""),
("05 · The tier list","Ranking where to put money","\"Where to put your money, ranked.\" (S tier reveal: a business that pays you, invested halal.)","Use the 160K-view tier-list format that already works on his page. D: savings account. C: crypto. B: property. A: halal ETFs. S: an agency feeding halal ETFs.","\"I'm teaching the S tier live on Tuesday. Link in bio.\""),
]
o=''
for k,ang,hook,body,cta in ads:
    o+=f'<article class="ad"><span class="eb">{k}</span><h3>{hook}</h3><div class="row"><b>Angle</b><div><p>{ang}</p></div></div><div class="row"><b>Body</b><div><p>{body}</p></div></div><div class="row"><b>CTA</b><div><p>{cta}</p></div></div></article>'
page('Ad creative scripts','5 angles · one live session','Five hooks, one angle each, every one pointing at the same Tuesday masterclass. Two reuse formats that already work on his Instagram.',None,o,'ad-scripts')
print('ok')
