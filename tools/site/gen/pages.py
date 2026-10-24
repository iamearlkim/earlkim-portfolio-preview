import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from tpl import *

SAM = 'CaseStudy-Samsung.dc.html'
FPA = 'CaseStudy-FPA.dc.html'
P = {}

# ---------------- SAMSUNG HUB ----------------
def mini_project(meta, title, desc):
    return (f'<article style="background: #FFFFFF; border: 1px solid {BORDER}; border-radius: 16px; padding: 24px; display: flex; flex-direction: column; gap: 10px">'
            f'<span style="font-size: 13px; color: {MUTED}">{e(meta)}</span>'
            f'<h3 style="margin: 0; font-size: 22px; font-weight: 600; letter-spacing: -0.015em; line-height: 1.3">{e(title)}</h3>'
            f'<p style="margin: 0; font-size: 16px; line-height: 1.55; color: {MUTED}">{e(desc)}</p></article>')

P[SAM] = page('Samsung enterprise platforms — Case study', [
    hero(['SAP × Samsung Electronics', 'Enterprise platforms', 'Multiple engagements'],
         "Unifying Samsung's enterprise platforms",
         "Over five years of SAP engagements, I shaped one platform UX approach across Samsung's divisions — procurement, ESG, logistics and cloud workspaces. Each project solved its own business problem; together they built a consistent, reusable way of working for Samsung's enterprise users.",
         [('Role', 'Lead UX designer / Design lead'), ('Client', 'Samsung Electronics (DX & DS divisions)'), ('Platforms', 'SAP BTP, SAP Analytics Cloud, SAP Fiori'), ('Scope', 'Procurement, ESG, cloud, analytics, logistics')]),
    cover('proc-hero.png', 'Samsung negotiation overview dashboard on a laptop'),
    stats([('42.5%', 'less process time in the end-to-end procurement workflow'),
           ('11.6%', 'year-over-year CO₂ reduction for Samsung Semiconductor, supported by the ESG platform'),
           ('2', 'follow-on contracts from the ESG proof of concept'),
           ('5+', 'engagements across the DX and DS divisions')]),
    split('The challenge', 'One company, many systems, many personas', top=112, paras=[
        "Samsung's operations run on many SAP and legacy systems, each serving different teams — buyers, ESG managers, plant operators, supply-chain planners and executives.",
        'Across engagements the recurring problem was the same: data lived in disconnected systems and spreadsheets, and the people who needed it worked in very different ways.']),
    cards('Platform UX strategy', 'Three principles that carried across every project', [
        ('One design language', 'Every module was built on SAP Fiori, so a buyer, an ESG manager and an executive meet the same patterns, components and behaviors — and new modules feel like part of one platform.'),
        ('Domain experts as co-designers', 'Design thinking workshops, interviews and usability tests put end users, process owners and specialists (procurement, EHS, supply chain) at the center of every decision.'),
        ('Reusable patterns across divisions', 'Overview dashboards, filterable work lists and calculate-then-review flows repeat across procurement, ESG and planning — designed once, adapted per domain.')], minw=300),
    section_title('Projects', 'Five engagements across the platform'),
    f'''<section style="{W}; padding: 16px 24px 32px"><div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); gap: 32px">
{project_link('Integrated material purchasing (N-ERP)', 'Turning Excel-based negotiation and price distribution into one automated purchasing process — designed with 50+ end users and up to 10 iterations, cutting process time by 42.5%.', 'proc-hero.png', 'Samsung negotiation overview dashboard', 'CaseStudy-SamsungProcurement.dc.html', 'Procurement · UI & UX designer')}
{project_link('Carbon footprint management (ESG)', 'A 4-week PoC for product-level Scope 3 emissions — from product master to emissions report. It converted into two follow-on contracts.', 'esg-hero.png', 'Carbon footprint management screen', 'CaseStudy-SamsungESG.dc.html', 'ESG · Design lead')}
{project_link_ph('DS cloud platform', 'An enterprise cloud workspace for the semiconductor division on SAP BTP and Work Zone, bringing tools and information into one entry point.', 'CaseStudy-SamsungDSCloud.dc.html', 'Cloud platform · DS division')}
{project_link_ph('DX risk management', 'Data analytics dashboard design for the device experience division — risk analytics and planning in SAP Analytics Cloud.', 'CaseStudy-SamsungDXRisk.dc.html', 'Data analytics · DX division')}
{project_link_ph('Shipment', 'Process redesign and application modernization for shipment operations.', 'CaseStudy-SamsungShipment.dc.html', 'Logistics · Process redesign')}
</div></section>''',
    split('What I learned', 'Designing a platform, not just projects', bullets=[
        'Consistency compounds: each project was faster to design and easier to adopt because it reused patterns users already knew.',
        'The deepest insights came from end users and domain experts in the room — workshops and usability tests changed the design more than any assumption.',
        'Enterprise UX is as much about how data moves between systems and roles as about the screens on top.']),
    nxt('Real-time manufacturing insight for Hanon Systems', 'CaseStudy-Hanon.dc.html'),
])

# ---------------- SAMSUNG ESG (sub) ----------------
P['CaseStudy-SamsungESG.dc.html'] = page('Samsung ESG — Case study', [
    hero(['SAP × Samsung Electronics', 'ESG', 'Sustainability'],
         'Carbon footprint management for Samsung Electronics',
         "Samsung committed to carbon neutrality by 2050 and asked SAP for a proof of concept to measure and manage its emissions. I led design of the product-level scenario: the emissions Samsung's products create while customers use them.",
         [('Role', 'Design lead, UI design'), ('Team', 'Solution experts, industry experts, 3 UX designers'), ('Tools', 'Figma, SAP Fiori'), ('Duration', '4 weeks · Proof of concept')],
         kicker='Samsung enterprise platforms · Project 2 of 5'),
    cover('esg-hero.png', 'The product consumption screen for a drum washing machine, shown on a laptop'),
    stats([('84%', 'of the footprint (Scope 3) previously calculated by hand'), ('4 weeks', 'from kickoff to a working PoC design'), ('6 steps', 'one end-to-end flow, from product master to business log'), ('2', 'follow-on contracts won from the PoC')]),
    split('01 — The challenge', 'A 2025 disclosure deadline, and no granular data', top=112, bottom=32, bullets=[
        'Samsung lacked granular climate and sustainability data across its operations, which made full reporting hard and kept environmental data apart from financial performance.',
        'A 2025 carbon-disclosure obligation required both a company-wide and a product-level measurement system.',
        'Scope 3 greenhouse-gas emissions had been calculated by hand and needed to be digitized.',
        'The PoC focused on one Scope 3 scenario: <strong style="color: #121316; font-weight: 600">use of sold products</strong> — products that consume energy directly while customers use them.']),
    figure(None, None, [('esg-ghg-scopes.png', 'GHG Protocol diagram of Scope 1, 2 and 3 emissions across the value chain, with use of sold products highlighted')], maxw=900,
           caption='Use of sold products sits in downstream Scope 3. Source: WRI/WBCSD Corporate Value Chain (Scope 3) Accounting and Reporting Standard, p. 5.'),
    split('02 — My role', 'Leading design with domain experts', paras=[
        "As design lead, I worked with environmental-solution, analytics and solution experts to design Samsung's carbon-emission management platform, at both the corporate and the product level.",
        "My focus was the use-of-sold-products scenario: defining how a product is registered, how its energy and water consumption is calculated, and how the resulting emissions are monitored and reported."]),
    cards('03 — The flow', 'Six steps from product to report', [(t, None) for t in ['Manage product master', 'Define consumption activity', 'Calculate product consumption', 'Calculate product footprint', 'Monitor product footprint', 'Monitor business log']], numbered=True, minw=170, dark_last=True),
    section_title('04 — The design', 'The solution, screen by screen'),
    figure('A. Manage product master', "Review new products in the product master, see which still need registering, and assign who enters each product's consumption — the system makes those assignments automatically.", [('esg-a-product-master.png', 'Product master list with filters, products, milestones and owners')]),
    figure('B. Define consumption activity', "The registration type for electricity use is mapped automatically to each country's energy regulations, with the formula shown — or chosen by hand. Users then fill each field the formula needs.", [('esg-b-consumption-activity.png', 'Drum washing machine detail page with usable life, unit consumption and total consumption')]),
    figure('C. Calculate product consumption', 'Confirm annual and lifetime electricity and water use, scale it by sales volume to a company-wide total, account for tap and sewage water, then validate the data and calculate total consumption.', [('esg-c-product-consumption.png', 'Product consumption calculation list')]),
    figure('D. Calculate product footprint', 'Map emission factors for electricity, water and filters, calculate greenhouse-gas emissions from templates for sold, manufactured and purchased products, and prepare the regulatory report.', [('esg-d-product-footprint.png', 'Footprint calculation screen with templates and settings')]),
    figure('E. Monitor product footprint and business log', 'Review emissions by model, region, country and corporate level, confirm results for reporting, and keep the history of every recalculation.', [('esg-e1-monitoring.png', 'Monthly emission results for a product across one year'), ('esg-e2-business-log.png', 'Emission detail by country with links to logs')]),
    split('05 — Outcome', 'Fully digital GHG management', white=True, top=96, bottom=96, bullets=[
        'Samsung can track emissions under the GHG Protocol at every location, and manage specification and substance data for every product it makes.',
        'Greenhouse-gas management moved from manual calculation to a fully digital system on SAP technology.',
        "We identified users' pain points and innovation opportunities, and prioritized use cases for the next phase.",
        'The proof of concept converted into two follow-on contracts.']),
    split('06 — What I learned', 'Reflections', paras=[
        'This project showed me how carbon-emission management works end to end as a business task: the key roles each step needs and how they collaborate, how companies break down and allocate reduction targets, and how emission data is collected and monitored to reach them.',
        'It also deepened my understanding of how enterprise software can help companies run a more sustainable business.',
        '<strong style="color: #121316; font-weight: 600">Next:</strong> multi-language support, and handling differences in units of measurement across countries.']),
    nxt('DS cloud platform', 'CaseStudy-SamsungDSCloud.dc.html', back_href=SAM, back_label='Samsung overview', kicker='Next Samsung project'),
], back_href=SAM, back_label='Samsung overview')

# ---------------- SAMSUNG E-COMMERCE (sub) ----------------
P['CaseStudy-SamsungEcom.dc.html'] = page('Samsung e-commerce — Case study', [
    hero(['SAP × Samsung Electronics', 'E-commerce', 'Pricing management'],
         'Samsung e-commerce: one-stop pricing management',
         'Managing product pricing on Samsung.com is labor-intensive: huge data sets and variables like time periods, discount rates and customer segments. With two designers, a solution expert and three engineers, I found the key problems in the current tool and designed a new UI to solve them.',
         [('Role', 'Design lead, research, prototype & UI design'), ('Team', 'Solution expert, 2 UX designers, platform and operations engineers, SAP Fiori UI developers'), ('Tools', 'Claude Code, Cursor, Figma Design / Make'), ('Scope', 'Global rollout across 24 subsidiaries')],
         ),
    video('ecomlive-hero.mp4', 'Demo of the redesigned pricing management app', pad='0 24px 96px'),
    stats([('3.2×', 'faster product search'), ('2.2×', 'faster data editing'), ('2 → 0', 'screen transitions to find or edit an item'), ('45 → 82.5', 'mean SUS usability score, before and after')]),
    split('Overview', 'A $29.9B commerce platform', top=112, bottom=24, paras=[
        'Samsung.com is an integrated B2C, B2B and B2E commerce platform — USD 29.9B in revenue and 20–50% year-over-year growth in 2025.']),
    figure(None, None, [('ecomlive-storefront.jpg', 'Samsung.com storefront showing Galaxy phones')], maxw=1000),
    split('01 — The challenge', 'Costly operations on a tool that fought the workflow', paras=[
        'The goal was to fix operational inefficiencies, high costs and performance bottlenecks in product data management — improving UX and system performance, validating the move back to SAP Commerce Cloud, and preparing a global rollout across 24 subsidiaries.'],
        bullets=['<strong style="color: #121316; font-weight: 600">Business:</strong> high operational cost in time, effort, people and communication.',
                 '<strong style="color: #121316; font-weight: 600">Users:</strong> a complex process on a complex legacy system that did not match their workflow.']),
    gallery([('ecomlive-legacy-1.jpg', 'Legacy pricing tool list view', 'Legacy tool: long, attribute-poor lists'), ('ecomlive-legacy-2.jpg', 'Legacy pricing tool detail view', 'Legacy tool: editing one item at a time')], minw=420,
            title='02 — Stakeholder interviews and demos', desc='Interviews and demos of the current tool showed a UI that did not match business workflows, system limits that forced manual workarounds — and some parts of the previous tool that were genuinely useful.'),
    cards(None, None, [
        ('Missing features', 'No product search in price mode, no multi-SKU editing, no bulk operations.'),
        ('Forced workarounds', 'Users avoided the system for data edits and bulk-uploaded through Excel.'),
        ('Inefficient search', 'Users memorized item IDs and scrolled through useless lists of 1,000+ rows.'),
        ('Lack of information', 'No status, dates, validity or price type in the table — every product had to be opened one by one.')], minw=240),
    split('System vs. mental model', 'Users think product-first', paras=[
        'Users work in a simple loop — find, view, edit — starting from the product. The system offered multiple entry points, showed only a few attributes, and allowed one edit at a time on a separate page.']),
    cards('03 — Design strategy', 'Streamlining data management for speed and accuracy', [
        ('One single entry point', 'A single, product-centric search entry point.'),
        ('Quick search', 'Minimize the time spent searching for items.'),
        ('Data at a glance', 'Expose all attributes in the list to speed up work.'),
        ('Bulk action', 'Select and update multiple SKUs at once.'),
        ('Scalable UI patterns', 'Support ever-growing data volumes.'),
        ('Merge view and edit', 'Combine two applications to cut clicks.')], numbered=True, minw=260),
    gallery([('ecomlive-prev-1.jpg', 'Previous custom tool search screen', 'Previous system'), ('ecomlive-prev-2.jpg', 'Previous custom tool filter popup', 'Previous system'), ('ecomlive-iterations.jpg', 'Three design iterations side by side', 'Design iterations')], minw=300,
            title='04 — Design iterations', desc='Ideas did not start from scratch: I built on the previous system, keeping what users valued and iterating toward one product-centric screen.'),
    section_title('Design solution 1', '3.2× faster search — “Easier and faster product search”'),
    split('', 'Single-screen filtering', bottom=16, paras=['A combined filter of attributes, category and text prompt makes search much faster — no jumping between screens, pop-ups or scrolling.']),
    video('ecomlive-search.mp4', 'Demo of product search with the combined filter'),
    before_after([('ecomlive-search-before.jpg', 'Search in the legacy tool')], [('ecomlive-search-after.jpg', 'Search in the redesigned tool')],
                 [('Task time', '95 s → 29 s (−69.4%)'), ('Productivity', '37 → 124 tasks per hour (+227.6%)'), ('Screen transitions', '2 → 0, including pop-ups'), ('Method', 'Filter to item detail, experienced users, n = 5')]),
    section_title('Design solution 2', '2.2× faster editing — “Edit item properties quickly”'),
    split('', 'Edit many items in place', bottom=16, paras=['Frequently used controls sit next to editable fields to cut mouse travel, and users can select and update multiple items at once — without leaving the screen.']),
    video('ecomlive-edit.mp4', 'Demo of editing prices for multiple items'),
    before_after([('ecomlive-edit-before-1.jpg', 'Legacy edit flow, step 1'), ('ecomlive-edit-before-2.jpg', 'Legacy edit flow, step 2')], [('ecomlive-edit-after.jpg', 'Redesigned in-place editing')],
                 [('Task time', '34 s → 15 s (−55.8%)'), ('Productivity', '+126.6%'), ('Screen transitions', '1 → 0'), ('Method', 'Find price to edit, experienced users, n = 5')]),
    section_title('Design solution 3', 'Scalable UI patterns for data growth — “Make it scalable”'),
    split('', 'One expandable screen', bottom=16, paras=['The layout accommodates unbounded product growth without breaking, so users can manage pricing at scale.']),
    video('ecomlive-scale.mp4', 'Demo of expanding and collapsing product price lists'),
    before_after([('ecomlive-scale-before-1.jpg', 'Legacy flow across two applications'), ('ecomlive-scale-before-2.jpg', 'Legacy edit dialog')], [('ecomlive-scale-after.jpg', 'Redesigned single expandable screen')],
                 [('Process', '2 applications and 2 screens → 1 screen'), ('Scalability', 'Static screen area → expandable screen'), ('Benefit', 'Supports business and data growth without UI changes')]),
    split('05 — Results', 'Performance and usability', white=True, top=96, bottom=96, bullets=[
        'Mean SUS usability score rose from 45.0 to 82.5.',
        'Search 3.2× faster and editing 2.2× faster, with zero screen transitions.',
        'One product-centric screen replaced two applications.']),
    split('06 — Takeaways', 'Reflections', bottom=24, paras=[
        'E-commerce data is complex — thousands to millions of products, with attributes that vary by location and timing.',
        'Repetitive edits like price and discount updates pushed me to explore AI for productivity. The next question is how to connect this system with the CMS so it can identify needed edits on its own, leaving people to review the outcomes.']),
    figure('AI research analysis agent', 'An agent analyzed research recordings and summarized key findings — timestamps, speakers, insights, quotes, what each screen shows and what is missing — then clustered linked insights by importance.', [('ecomlive-ai-agent.jpg', 'AI research analysis agent output with timestamped insights and screenshots')]),
    nxt('Optimizing talent acquisition for Doosan', 'CaseStudy-Doosan.dc.html'),
])

# ---------------- DOOSAN ----------------
P['CaseStudy-Doosan.dc.html'] = page('Doosan AI recruitment — Case study', [
    hero(['SAP × Doosan Group', 'HR tech', 'Human–AI interaction'],
         'Optimizing talent acquisition with ML',
         'Doosan was losing experienced employees and overspending on external hiring. Built on SAP BTP and integrated with SAP SuccessFactors, this platform uses machine learning to boost internal mobility, streamline recruiter screening and support self-directed careers for millennial and Gen Z employees.',
         [('Role', 'Design lead, user research, UI/UX design'), ('Team', 'Project manager, solution expert, ML and front-end engineers, UX designer'), ('Platform & tools', 'Responsive web, SAP Fiori, Figma'), ('Client', 'Doosan — 43,000+ employees, 20 subsidiaries, 38 countries')]),
    cover('doosan-thumb.png', 'Recruitment management candidate list with job-fit scores'),
    stats([('5×', 'more internal transfers'), ('23%', 'lower employee turnover'), ('2.5×', 'recruiter screening productivity'), ('+26%', 'employee satisfaction with career development')]),
    split('01 — The challenge', 'A talent retention problem', top=112, paras=[
        '92% of employees who left did so for career development, and 37% left within three years of an internal transfer.'],
        bullets=['<strong style="color: #121316; font-weight: 600">High talent turnover</strong> — experienced employees were leaving.',
                 '<strong style="color: #121316; font-weight: 600">Rising recruitment costs</strong> — heavy spending on external hiring to fill gaps.',
                 '<strong style="color: #121316; font-weight: 600">Hiring bottlenecks</strong> — external candidates were harder and more competitive to find.']),
    split('02 — Exploring', 'Design thinking workshops as a kickoff', paras=[
        'I brought all stakeholders together to align on the as-is internal recruitment process, conceptualize the to-be screen flows, and draw up action plans — producing a use-case diagram, key screen flows and an action plan.']),
    cards('Empathizing with users', '6 interviews and thematic analysis', [
        ('Recruiters', 'Overwhelmed by manual screening and reporting; struggling to balance quality with limited time.'),
        ('Employees', 'Seeking career growth, clear role details and safe, anonymous communication channels.')], minw=320),
    cards('03 — Design goals', 'A healthy, sustainable internal hiring culture through technology', [
        ('Streamlined process', 'Replace Excel-based screening and reporting with a system that cuts recruiters\' manual work.'),
        ('Enhanced job visibility', 'Help employees find opportunities and detailed job information easily.'),
        ('Ensured data protection', 'Prevent exposure of application information that created workplace friction.')], minw=280),
    split('04 — Building the ML foundation', 'Designing with engineers and data scientists', paras=[
        'With the dev team, ML engineers, data scientists and the client\'s IT team, I framed the data questions: what data recruiters already use, where it lives in the HR system and in what format, how much history is realistic, and which data must be visible and explainable in the UI.',
        'Because there was not yet enough labeled data to justify every recommendation, the first model was built on legacy HR records, with an architecture integrating the legacy system, SAP SuccessFactors and SAP Data Intelligence on SAP BTP.'],
        bullets=['<strong style="color: #121316; font-weight: 600">Phase 1 — learn from the past:</strong> train on years of internal moves, evaluations and project records to learn what a successful internal placement looks like.',
                 '<strong style="color: #121316; font-weight: 600">Phase 2 — learn from the next year:</strong> run the model alongside existing HR processes, log every recommendation and capture how recruiters and managers respond.']),
    figure('05 — Design iterations', 'Sketches validated with users moved from an SAP SuccessFactors-based flow, to customizable applicant data entry, to ML insights that give recruiters a faster, insightful first screen.', [('doosan-proto.png', 'Low-fidelity candidate list with a screening-score explanation popup')]),
    figure('06 — Design solution: intelligent screening', 'An AI-enhanced candidate list built with SAP Fiori 3.0: switch between job requisitions, refine with a filter bar, read color-coded indicators for each criterion, compare in a table, and see each application\'s suitability at a glance.', [('doosan-ai-list.png', 'Candidate list with color-coded job-fit scores and evaluation columns')]),
    gallery([('doosan-job-posting.png', 'Internal job posting candidate list', 'Transparent internal job postings'), ('doosan-candidate-detail.png', 'Application detail with masked personal data', 'Confidential application details')], minw=320),
    split('07 — Result', 'Data-driven people management', white=True, top=96, bottom=96, bullets=[
        'Internal transfers increased 5×.', 'Turnover dropped by 23%, lowering external recruitment costs.', 'Screening productivity increased 2.5×, with data-driven hiring decisions.',
        'Satisfaction and engagement with career development rose 26%, through transparent job information and a trusted, confidential process.']),
    cards("What's next", 'Future direction', [
        ('Analytical dashboard', 'Spot trends, drill into root causes and get actionable insights, designed with SAP Fiori Horizon.'),
        ('Scalable AI explainability', 'Three levels — descriptive score, explanatory factors, and advanced explainability with suggested next steps.'),
        ('Predictive workforce planning', 'Connect recruitment with business strategy using LinkedIn data, internal talent pools, demand and budget forecasts.')], minw=280),
    split('Scaling', 'From project to product', paras=[
        'The project scaled into an independent service: Peoply, a cloud SaaS solution built on SAP BTP and SAP SuccessFactors.']),
    split('08 — Takeaways', 'What I learned about designing AI', bullets=[
        'AI products need end-to-end collaboration with data scientists, ML engineers and domain experts.',
        'Human–AI interaction patterns manage the trade-off between control and automation, and explainability reduces over-reliance.',
        'AI works best as an assistant, with transparency and the ability to override.',
        'Designing the data experience — input, processing and display — matters as much as the UI.']),
    quote("It was a great opportunity to experience the whole process of human-centered design, development and collaboration for an AI-powered HR product. It was a delightful experience as an SAP developer thanks to the strong backup of Earl's UX team.", 'Minchoul Jung, Project Manager, Doosan'),
    quote("In a global collaboration with Doosan, we developed a use case along SAP's Human-Centered Approach to Innovation. I really enjoyed working together with Earl's team and Doosan IT.", 'Kay Schmitteckert, ML Developer, SAP'),
    nxt('Self-aligned intelligence: Clerro', 'CaseStudy-Clerro.dc.html'),
])

# ---------------- HANON ----------------
P['CaseStudy-Hanon.dc.html'] = page('Hanon Systems — Case study', [
    hero(['SAP × Hanon Systems', 'Manufacturing', 'SAP Innovation Awards 2019 finalist'],
         'Real-time manufacturing insight',
         'Lack of visibility was holding back productivity at Hanon Systems. Working with manufacturing experts, a solution specialist, a project manager and another designer, I helped digitize their production system — from workshop to user test.',
         [('Role', 'User research, prototyping, UI design'), ('Team', 'Project manager, solution expert, 2 industry experts, 2 UX designers'), ('Tools', 'Axure, SAP Build'), ('Duration', '3 months')]),
    cover('hanon-thumb.png', 'Production insights dashboard and a mobile task alert'),
    stats([('10', 'in-depth user interviews at the pilot plant'), ('5', 'target user groups, each with its own app'), ('Real time', 'OEE visibility and downtime reasoning'), ('Finalist', 'SAP Innovation Awards 2019')]),
    split('01 — The challenge', 'No visibility, no prediction', top=112, bullets=[
        'The client wanted to evaluate equipment effectiveness digitally, for better insight into plant performance.',
        'They wanted predictive machine maintenance to improve scheduling and minimize downtime.']),
    figure('A human-centered process', 'I went through the whole process — Explore workshop, field research, synthesis, ideation, user validation and user testing.', [('hanon-process.jpg', 'Seven-step process diagram from Explore workshop to user test')]),
    gallery([('hanon-workshop.jpg', 'Workshop board visualizing the as-is production process', 'Current challenges and opportunities, visualized with SAP Scenes')], minw=320,
            title='02 — Explore workshop', desc='With the CIO, CHRO, VP of product group and operations leaders, I facilitated sessions to identify business challenges and priorities. Key insights: inaccurate data and human error, no real-time visibility of machine status, no way to predict breakdowns, and no maintenance knowledge process.'),
    figure('03 — Field research', 'I observed the pilot plant and ran ten interviews across operations, production, engineering, maintenance and IT.', [('hanon-field.png', 'Field observation photos of manual production and downtime management')]),
    cards('What were the real problems?', 'Three issues in the production process', [
        ('Lack of visibility', 'Workers monitored machines manually, which delayed maintenance.'),
        ('Less productivity', 'Without predicting downtime, production goals were hard to meet.'),
        ('Less data accuracy', 'Manual reports were slow to produce and often inaccurate.')], minw=280),
    split('Goals', 'Connect, visualize and trust the data', paras=['How might we increase manufacturing productivity and efficiency by integrating data?'], bullets=[
        'Connect live machining and production-order data from all production units.',
        'Visualize real-time line performance so employees can act on it.',
        'Ensure data accuracy and replace analog reports with dashboards.']),
    section_title('04 — The design solution', 'Five apps for five target users'),
    figure('A. Plant insights — for operation managers', 'Plant-level KPIs — OEE, volume performance, productivity, first-time-through and scrap — with trends by month and by cell.', [('hanon-plant.png', 'Plant insights dashboard with KPI tiles and charts')]),
    figure('B. Production insights — for production managers', 'Line KPIs and a downtime list with activity summaries, so managers can see which lines are inactive and why.', [('hanon-production.png', 'Production insights with line downtime list')]),
    figure('C. Machine insights — for operators', 'The current shift order, machine KPIs and a line-activity timeline, with quick actions to manage downtime and report production.', [('hanon-machine.png', 'Operator dashboard with shift order and activity timeline')]),
    figure('D. Maintenance management — for team leaders and engineers', 'Team leaders get downtime notifications and assign available engineers; engineers receive tasks and work through their action items on a tablet.', [('hanon-maintenance.png', 'Maintenance engineer home and action item list on tablets')]),
    split('05 — Outcome', 'Real-time decisions on the shop floor', white=True, top=96, bottom=96, bullets=[
        'Real-time OEE visualization and downtime reasoning.',
        'Increased overall productivity and efficiency, effectively meeting customer needs.',
        'Operators empowered to make real-time decisions to adjust production.',
        'Less desk work and fewer trips between shop floor and office.',
        'SAP Innovation Awards 2019 finalist.']),
    quote('With better data about the health of our equipment, we can improve the way we schedule our maintenance activities and minimize equipment downtime.', 'Zsolt Karikó, Managing Director of European Compressor Operations, Hanon Systems'),
    split('06 — What I learned', 'Reflections', paras=[
        "Through the manufacturer's digitalization, I understood the real concerns and barriers from business and stakeholder perspectives — how roles across the factory are interconnected and affect each other's work, and how the maturity of a production system shapes individual employees' quality of life."]),
    nxt('Financial planning and analysis', 'CaseStudy-FPA.dc.html'),
])

# ---------------- BHP ----------------
P['CaseStudy-BHP.dc.html'] = page('BHP financial planning — Case study', [
    hero(['SAP × BHP', 'Finance', 'SAP Analytics Cloud'],
         'Redesigning financial planning',
         "BHP, an Australian mining company, needed its financial planning in SAP Analytics Cloud to keep up with a changing process. Working with BHP's UX designer and the SAC product team, I simplified the experience and made it more enjoyable.",
         [('Role', 'User research, data visualization, UI design'), ('Team', 'Project manager, 2 UX designers'), ('Tools', 'SAP Analytics Cloud'), ('Duration', '4 weeks')],
         kicker='Financial planning and analysis · Project 1 of 2'),
    cover('bhp-hero.jpg', 'Total cost planning dashboard in SAP Analytics Cloud on a laptop'),
    stats([('10 → 4', 'tables, without losing any information'), ('5 → 2', 'screens for the core planning flow'), ('80%+', 'target reduction in pages to navigate'), ('3', 'clear steps: plan, review, report')]),
    figure('01 — User research', "I analyzed recorded remote interviews in which finance professionals shared their screens, showing their process and personal workarounds. I mapped pain points, opportunities and ideas onto the planning journey.", [('bhp-journey.png', 'Financial planning user journey map with pain points and opportunities')]),
    cards('Defining problems', 'Slow, clicky and complicated', [
        ('Slow', 'SAC loaded slowly compared with other tools; users expected Excel-like speed.'),
        ('Clicky', 'Too many buttons wore users out before tasks were done.'),
        ('Complicated', 'Users lost track of where they were and kept returning to the landing page.')], minw=280),
    split('Goals', 'Fast, intuitive and enjoyable', paras=['How might we make the financial planning experience in SAC fast, intuitive and enjoyable?'], bullets=[
        'Optimize the speed — a system that responds quickly and consistently.',
        'Create an intuitive experience — get the job done as quickly as possible.',
        'Make it enjoyable — intuitive and purpose-driven.']),
    figure('02 — The design solution', 'I split the process into two main sections — data input and review — combining 10 tables on 5 screens into 4 tables on 2 screens, with a landing page tying them together.', [('bhp-structure.png', 'Diagram of the landing page linking to an input page and a review page')], maxw=820),
    figure('Landing page', 'One place to reach every page and resource needed for planning, replacing scattered entry points: plan, review and report.', [('bhp-landing.png', 'Planning process landing page with plan, review and report links')]),
    figure('Input page', 'Tables arranged in sequential steps with optional steps set apart. Excel-like grid headers, editable versus read-only cells, totals and frozen headers build on what finance users already know.', [('bhp-input.jpg', 'Input page with step instructions and Excel-like tables')]),
    figure('Review page', 'Six scattered tables consolidated into one page: a five-year overview chart, year-over-year comparisons, and detailed tables — no need to jump between pages.', [('bhp-review.jpg', 'Review page with five-year comparison charts and detail tables')]),
    split('03 — What I learned', 'Lessons learned', bullets=[
        'Financial planners are rarely satisfied with a single tool — no tool has every capability they need.',
        'Excel is dated but still the most popular finance tool; SAC has to offer what Excel cannot.',
        'Fixed windows limit visibility of financial tasks; users need deeper control.']),
    quote('The design solutions provided by Earl and his colleague were of high quality and extremely useful. Always willing to listen and dive into the underlying problems, which led the team to propose new and innovative ways to resolve the problems we shared with them.', 'UX designer, BHP'),
    nxt('Enterprise financial planning for JG Summit', 'CaseStudy-JGSummit.dc.html', back_href=FPA, back_label='Financial planning overview', kicker='Next finance project'),
], back_href=FPA, back_label='Financial planning overview')

# ---------------- JG SUMMIT ----------------
P['CaseStudy-JGSummit.dc.html'] = page('JG Summit — Case study', [
    hero(['SAP × JG Summit', 'Finance', 'SAP Analytics Cloud'],
         'Enterprise financial planning',
         'JG Summit, one of the largest Filipino conglomerates, struggled to integrate production and sales data for its planning. As senior UX designer, I took the work from exploration and research through to dashboard design.',
         [('Role', 'User research, workshop facilitation, data visualization'), ('Team', 'Program manager, project manager, finance expert, engineer, 2 UX designers'), ('Tools', 'SAP Analytics Cloud'), ('Duration', '4 months')],
         kicker='Financial planning and analysis · Project 2 of 2'),
    cover('jg-urc-overview.png', 'URC sales overview dashboard with KPIs and charts'),
    stats([('2', 'Explore workshops across two business units'), ('3+ weeks', 'previously spent preparing reports in Excel'), ('3', 'priority areas: P&L planning, consolidation, reporting'), ('1', 'source of truth for planning and reporting')]),
    split('01 — The challenge', 'Manual planning in Excel', top=112, paras=[
        'Manual Excel budgeting and forecasting caused human errors, inaccurate data and slow reporting, keeping finance professionals stuck in operational tasks. Executives needed timelier decisions with better visibility.'],
        bullets=['Plan across the organization for more engagement and accuracy.', 'Link operational and financial planning.', 'Embed planning in the enterprise application as one source of truth.']),
    figure('02 — Explore workshops', 'I facilitated two Explore workshops — for URC\'s Branded Consumer Food Group and its packaging division — to find high-value planning use cases, build journey maps per persona, map stakeholders and prioritize the top problems.', [('jg-workshop.jpg', 'Workshop wall with sticky notes mapping a sales and costing process')]),
    split('03 — Discover', 'Interviews and a Discover workshop', paras=[
        'Before the Discover workshop, I interviewed finance stakeholders across the holding company and business units with role-specific questionnaires.',
        'Common needs: a unified view for budget consolidation, standardized planning across units, better forecasting and what-if simulation — and an end to Excel reporting that took over three weeks.']),
    gallery([('jg-journey-asis.png', 'As-is journey map wall', 'As-is journey'), ('jg-journey-tobe.png', 'To-be journey map wall', 'To-be journey')], minw=300,
            title='Journey maps and prioritization', desc='In co-creation sessions, stakeholders mapped current and ideal processes and voted on the most impactful ideas: profit and loss planning, consolidation, and reporting and dashboards.'),
    section_title('04 — The design solution', 'From data input to automatic reports'),
    split('Architecture', 'One flow for every role', paras=[
        'The application starts with data input, moves through five-year planning, and ends with dashboards shared automatically with decision-makers — no separate report creation. Financial planners, general managers, CEOs and CFOs each enter at their level.']),
    figure('Company-level sales overview', 'Financial elements for each business unit side by side. Every chart is interactive, so users drill down without leaving the page.', [('jg-urc-overview.png', 'URC sales overview dashboard')]),
    gallery([('jg-flour.png', 'Flour sales overview dashboard', 'Division-level sales overview — Flour, Pasta and Bread compared year over year'), ('jg-bcfg.jpg', 'BCFG sales report dashboard', 'Division-level sales report — by period, division, customer and region, budget versus actual')], minw=360),
    split('05 — What I learned', 'Reflections', paras=[
        'I learned how production, sales and budget data are interconnected across an enterprise, and how much data accuracy and timeliness matter.',
        'Repurposing financial data for different users also made me think about how terms like gross profit and EBITDA shape UI design.']),
    quote('This is exactly what we expected. I want to see the PoC outcome realized as soon as possible to cover more tasks in our financial planning process.', 'Kerwin Tan, Deputy CFO, Robinsons Land Corporation, JG Summit'),
    nxt('Redesigning financial planning for BHP', 'CaseStudy-BHP.dc.html', back_href=FPA, back_label='Financial planning overview', kicker='Previous finance project'),
], back_href=FPA, back_label='Financial planning overview')

# ---------------- FOOD DELIVERY ----------------
P['CaseStudy-FoodDelivery.dc.html'] = page('Eco-friendly food delivery — Case study', [
    hero(['Concept project', 'Mobile', 'Sustainability'],
         'Eco-friendly food delivery',
         "Food delivery in Korea has grown into a 10-billion-dollar industry — and a major source of plastic waste and carbon emissions. I designed an eco-friendly experience across the whole ordering flow, from choosing food to packaging and delivery.",
         [('Role', 'User research, interaction design, UI design'), ('Team', '2 UX designers'), ('Tools', 'Figma'), ('Duration', '2 weeks')]),
    cover('food-thumb.jpg', 'Food delivery app showing restaurants with eco-ratings, on a phone'),
    stats([('8.3M', 'disposable food containers thrown away every day in South Korea'), ('100K', 'delivery motorcycles on Seoul\'s roads every day'), ('76%', 'of Koreans feel guilty throwing away delivery packaging'), ('4', 'design ideas, from eco-ratings to feedback')]),
    figure('01 — The problem', 'Delivered food is convenient, but its packaging and transport are “out of sight, out of mind.” People have no information about environmental impact and no alternatives.', [('food-hmw.jpg', 'Delivery motorcycles and piles of disposable containers')]),
    split('Goals', 'Visibility and alternatives', paras=['How might we reduce plastic waste and carbon emissions while keeping the convenience of food delivery?'], bullets=[
        '<strong style="color: #121316; font-weight: 600">Data visibility</strong> — show sustainability data across the food supply chain to guide decisions.',
        '<strong style="color: #121316; font-weight: 600">Eco-friendly alternatives</strong> — make greener delivery and packaging options easy to choose.']),
    figure('02 — Prototyping and iterations', 'I mapped rapid prototypes onto the ordering journey. Users relied heavily on reviews, ratings and appealing images — so eco-information had to work the same way.', [('food-journey.png', 'Sketched prototypes mapped along the ordering user journey')]),
    figure('System architecture', "To show how eco-scores could be calculated, I proposed a system landscape on SAP Cloud Platform: CO₂ is calculated from raw materials and production steps (S/4HANA bills of materials and recipes) and from actual order quantities.", [('food-arch.png', 'Architecture from the mobile app through CO₂ calculation microservices to S/4HANA')], maxw=900),
    section_title('03 — The design', 'Eco-friendly choices at every step'),
    gallery([('food-list.jpg', 'Restaurant list sorted by eco-rating', 'Listing restaurants by eco-rating'),
             ('food-dish.png', 'Dish detail showing an 80% carbon reduction', 'Eco-rating for each dish'),
             ('food-delivery.png', 'Delivery options from walking to car', 'Alternative ways to deliver'),
             ('food-profile.png', 'Profile with CO₂, plastic and food waste saved', 'Feedback on your impact')], minw=220),
    split('04 — Impact', 'On users, business and society', white=True, top=96, bottom=96, bullets=[
        '<strong style="color: #121316; font-weight: 600">Users</strong> — transparent data supports better environmental decisions, and people get real alternatives.',
        '<strong style="color: #121316; font-weight: 600">Business</strong> — integrated CO₂ data across the platform informs ideation and strategy.',
        '<strong style="color: #121316; font-weight: 600">Society</strong> — eco-information in apps can become a market standard and shift consumption habits.']),
    split('05 — What I learned', 'Reflections', paras=[
        'Individual choices add up to a collective impact. With technology, it is possible to measure CO₂ from how ingredients are produced and distributed to how food is cooked and delivered.']),
    nxt('Design thinking for Gogoro', 'CaseStudy-Gogoro.dc.html', kicker='More use cases'),
])

# ---------------- GOGORO ----------------
P['CaseStudy-Gogoro.dc.html'] = page('Gogoro — Case study', [
    hero(['SAP AppHaus × Gogoro', 'Design thinking', 'Mobility'],
         'Sustainable mobility: design thinking with Gogoro',
         "Gogoro, Taiwan's electric-scooter company, wanted to improve the whole customer journey from pre-purchase to maintenance. I led field research and an Explore workshop to find and prioritize innovation opportunities.",
         [('Role', 'Design lead, researcher, workshop facilitator'), ('Platform', 'Web, mobile'), ('Duration', '12 weeks')]),
    cover('gogoro-hero.jpg', 'Paper prototypes of a scooter and phone from the Gogoro and SAP workshop'),
    split('01 — The challenge', "Rethinking every touchpoint", top=112, paras=[
        "Discover innovation opportunities across Gogoro's touchpoints — retail stores, maintenance, customer service and online and offline channels — to create a superior customer experience as the electric-scooter business grew."]),
    figure('02 — Field research', 'Gogoro and SAP met at SAP Taiwan for a one-day design thinking workshop. It began with empathy: a visit to a retail store the day before. Participants then ideated and rapid-prototyped from each persona\'s point of view, and narrowed down use cases for further engagement.', [('gogoro-field.jpg', 'Gogoro retail store, battery swap station and a customer with a scooter')]),
    section_title('03 — Prototyping', 'Four ideas from the workshop'),
    idea(1, 'Predict maintenance time and sign documents electronically', 'After booking, owners get a predicted maintenance time so they wait less in the store, and sign all related files digitally.', 'gogoro-idea1.png', 'Storyboard of booking maintenance on a phone'),
    idea(2, 'Quick, timely troubleshooting on the road', 'Owners scan a QR code on the scooter for a self-help guide built from feedback and past cases — fewer helpdesk calls and faster answers.', 'gogoro-idea2.png', 'Paper prototype of roadside troubleshooting'),
    idea(3, 'Charging and service at neighborhood convenience stores', 'Convenience stores host battery changes and basic maintenance, so owners get service while they shop and wait less at retail stores.', 'gogoro-idea3.png', 'Participant presenting the convenience-store concept'),
    idea(4, 'Better communication between customer service and stores', "Policies on electric-scooter sales change often. A dedicated channel, with communication tracked in sales managers' reviews, keeps salespeople up to date.", 'gogoro-idea4.png', 'Participants presenting a paper prototype'),
    split('04 — Outcome', 'What Gogoro gained', white=True, top=96, bottom=96, bullets=[
        "Users' pain points and innovation opportunities discovered, and use cases prioritized.",
        'A full experience of SAP design thinking with the AppHaus team.',
        'Use cases explored through visual storyboards, ready to become proofs of concept.']),
    quote('The design thinking workshop delivered by the SAP AppHaus team was far beyond my expectations! I believe all participants from Gogoro learned a lot through the practice and methodology.', 'Allen Huang, Head of Customer Engagement Solution, Gogoro'),
    nxt('Eco-friendly food delivery', 'CaseStudy-FoodDelivery.dc.html', kicker='More use cases'),
])


# ---------------- CLERRO ----------------
P['CaseStudy-Clerro.dc.html'] = page('Clerro — Case study', [
    hero(['Clerro', 'Consumer AI', '0-to-1'],
         'Self-aligned intelligence: Clerro',
         "People don't need more AI tools — they need systems that know who they are and how they think. As the sole designer on a 0-to-1 AI decision-intelligence product, I turned an abstract idea into an investor-ready prototype: screenshot a product, get a clear, personal verdict you can trust.",
         [('Role', 'AI product designer (contract), sole designer'), ('Timeline', 'Sep – Dec 2025'), ('Approach', 'AI-native design process, mobile-first'), ('Deliverables', 'Investor-demo prototype, design system, engineering handoff')]),
    figure(None, None, [('clerro-hero.png', 'Clerro Clarity Card on a phone: Aligned, a great fit for your specific needs, score 91')], maxw=340),
    stats([('2 weeks', 'to an investor-ready clickable prototype'), ('3', 'AI UX layers: Insight, Proof and Personal CQ'), ('50%', 'of Gen Z already screenshot products before buying'), ('$50B+', 'AI analytics market opportunity')]),
    split('01 — Context and opportunity', 'Decision fatigue and an AI trust gap', top=112, bullets=[
        '<strong style="color: #121316; font-weight: 600">Problem:</strong> decision fatigue as a cognitive burden, and an AI trust gap — 65% of organizations adopt AI, but personalization and trust stay low.',
        '<strong style="color: #121316; font-weight: 600">Behavioral signal:</strong> half of Gen Z save product screenshots — an unmet need hiding in plain sight.',
        '<strong style="color: #121316; font-weight: 600">Users:</strong> consumers at moments of decision friction first; enterprises later, through a decision-intelligence API.']),
    cards('02 — AI-native workflow', 'Designing with AI, end to end', [
        ('Problem framing', 'AI-assisted synthesis of decision fatigue, the trust gap and screenshot behavior.'),
        ('Insight extraction', 'User journeys and behavioral patterns: zero-friction entry, progressive disclosure.'),
        ('Rapid prototyping', 'AI-generated variations and testing, leading to an interactive Clarity Card prototype.'),
        ('System design', 'A three-layer system, design specs and a mobile-first design system.')], numbered=True, minw=240),
    cards('03 — Solution architecture', 'Three layers of trust', [
        ('Insight — the default view', 'Builds confidence and context: the CQ score and confidence level, why Clerro recommends it, and how it fits you.'),
        ('Proof — evidence on demand', 'Enables transparency and auditability: verification sources, a data-consistency check, and the insight model used.'),
        ('Personal CQ — an evolving profile', 'Builds learning and trust over time: how your clarity evolves, decision patterns and suggestions to improve.')], minw=300),
    section_title('04 — Interaction flow', 'From screenshot to clarity'),
    gallery([('clerro-1-product.png', 'Product page on a shopping app', 'On any shopping app'),
             ('clerro-2-share.png', 'Share sheet for the product', 'Share or screenshot'),
             ('clerro-3-share-to-clerro.png', 'Share sheet with the Clerro app', 'Send to Clerro')], minw=200, colmax=280,
            title='Step 1 — Zero-friction entry', desc='On Amazon, TikTok or any store, the user takes a screenshot or shares a link to Clerro. Analysis starts immediately — no login, no onboarding.'),
    gallery([('clerro-4-analyzing.png', 'Clerro analyzing the product', 'Analyzing'),
             ('clerro-5-clarity-card.png', 'Clarity Card with score 91', 'Clarity Card'),
             ('clerro-6-insight.png', 'Why Clerro gave that rating', 'Why this rating')], minw=200, colmax=280,
            title='Step 2 — The Clarity Card', desc='A moment of friction becomes a moment of confidence: the verdict and CQ score appear at once, with the reasons one tap away.'),
    gallery([('clerro-7-proof.png', 'Proof View with verification sources', 'Proof View'),
             ('clerro-8-personal-cq.png', 'Personal CQ profile and insights', 'Personal CQ')], minw=200, colmax=280,
            title='Step 3 — Transparency on demand', desc='Users can see exactly how a verdict was verified, then explore how their own clarity profile is evolving.'),
    figure(None, None, [('clerro-9-proof-detail.png', 'Data consistency check and insight model details')], maxw=640, caption='Proof details: data-consistency check and the insight model used.'),
    cards('05 — Key design decisions', 'Built around how people already behave', [
        ('Zero-friction entry', 'Users see value before any commitment; Personal CQ learns quietly through use.'),
        ('Screenshot as primary input', 'Half of Gen Z already screenshot products — no app-switching, and it works across any platform, online or offline.'),
        ('Mobile-first architecture', '“People already use screenshots to share things they are looking at on their phones.”')], minw=280),
    split('Future expansion', 'From consumer to enterprise', paras=[
        'The same behavioral learning engine can power a different application layer: a ClerroLayer API offering decision logic as a service, and Team CQ for organizational decision patterns — for procurement, vendor selection and compliance decisions.']),
    split('06 — Key contributions', 'What I brought', white=True, top=96, bottom=96, bullets=[
        '<strong style="color: #121316; font-weight: 600">Abstract to tangible:</strong> translated ambiguous business ideas into concrete screen flows and logical structures.',
        '<strong style="color: #121316; font-weight: 600">AI-driven UX:</strong> established interaction principles for AI uncertainty that build user confidence.',
        '<strong style="color: #121316; font-weight: 600">Rapid prototyping:</strong> high-fidelity prototypes to align engineering and validate concepts.',
        '<strong style="color: #121316; font-weight: 600">Scalable design system:</strong> tokens, components and patterns documented for handoff and future growth.']),
    nxt('Agent Skills for Documentation', 'CaseStudy-GoogleCloud.dc.html'),
])


# ---------------- GOOGLE CLOUD DOCS (UW HCDE capstone) ----------------
B = 'style="color: #121316; font-weight: 600"'
PROTO = 'https://jimnidev.github.io/google-cloud-docs-capstone/pages/home.html'
def ext_link(label, desc, href, cta):
    return f'''<section style="{W}; padding: 32px 24px"><div style="background: #FFFFFF; border: 1px solid #E2E2DC; border-radius: 16px; padding: 28px; display: flex; flex-wrap: wrap; gap: 20px; align-items: center; justify-content: space-between">
<div style="display: flex; flex-direction: column; gap: 6px; max-width: 44rem"><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.015em">{e(label)}</span><span style="font-size: 16px; line-height: 1.55; color: #4A4C53">{e(desc)}</span></div>
<a href="{href}" target="_blank" rel="noopener" style="text-decoration: none; background: #121316; color: #F6F6F3; font-weight: 500; font-size: 16px; padding: 14px 24px; border-radius: 999px">{e(cta)} ↗</a>
</div></section>'''

def evidence(items, minw=260):
    out = []
    for title, big, note in items:
        bg = f'<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.015em; line-height: 1.3; color: {{{{accent}}}}">{e(big)}</span>' if big else ''
        out.append(f'<li style="background: #FFFFFF; border: 1px solid #E2E2DC; border-radius: 16px; padding: 24px; display: flex; flex-direction: column; gap: 12px"><span style="font-size: 16px; font-weight: 600; line-height: 1.4">{e(title)}</span>{bg}<span style="font-size: 13px; line-height: 1.5; color: #4A4C53; margin-top: auto">{e(note)}</span></li>')
    return f'<section style="{W}; padding: 16px 24px 48px"><ol style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, {minw}px), 1fr)); gap: 16px">{"".join(out)}</ol></section>'

def pull(text, pad='48px 24px 80px'):
    return f'<section style="{W}; padding: {pad}"><p style="margin: 0; font-size: clamp(2rem, 3.6vw, 2.75rem); line-height: 1.2; letter-spacing: -0.02em; font-weight: 500; max-width: 26ch">“{e(text)}”</p></section>'

def insight(label, text):
    return f'<section style="{W}; padding: 32px 24px"><div style="border-left: 3px solid {{{{accent}}}}; padding: 8px 0 8px 24px; display: flex; flex-direction: column; gap: 10px; max-width: 52rem"><span style="{LBL}">{e(label)}</span><p style="margin: 0; font-size: 22px; line-height: 1.5">{text}</p></div></section>'

P['CaseStudy-GoogleCloud.dc.html'] = page('Agent Skills for Documentation — Case study', [
    hero(['UW HCDE × Google Cloud', 'AI documentation', 'Agent Skills'],
         'Agent Skills for Documentation',
         'AI changed how developers find answers before technical documentation could catch up. I led research and design on Skills — task-oriented, agent-readable workflows built on official docs — to close the trust gap between fast AI answers and verified technical truth for human users.',
         [('Role', 'UX designer & researcher in a team of four'), ('Partner', 'Google Cloud Documentation team'), ('Program', 'UW HCDE capstone · 2026'), ('Methods', 'Friction logs, contextual inquiry, design sprint, usability testing')]),
    pull("When developers stopped reading docs and started prompting AI, Google Cloud's documentation had to learn a new language."),
    cover('gcd-home-slash.jpg', 'Prototype home page: typing / in the AI prompt box lists Documentation Skills such as gcloud Commands Quick Reference and Onboarding to Google Cloud'),
    split('01 — Context', 'The docs are no longer the first stop', top=64, paras=[
        "Google Cloud's documentation supports more than 100 cloud services, but people increasingly reach it through AI rather than reading it directly. The documentation team put the shift plainly:",
        '<span style="font-size: 22px; line-height: 1.5; color: #121316">“AI has fundamentally reshaped how people seek, explore, and consume information.”</span>']),
    evidence([
        ('AI agents are reading documentation.', '48% of doc views by AI', 'Source: Write the Docs 2026 Conference'),
        ('AI-generated code is increasing.', '50% → 75% in 6 months', 'Fall 2025 to April 2026 · Source: Google Cloud Next 2026'),
        ('Documentation is becoming infrastructure for AI agents.', None, 'Source: Write the Docs 2026 Conference')]),
    split('02 — Challenge', 'Accurate, but not there at the point of failure', paras=[
        "I began by auditing Google Cloud's documentation directly, from onboarding through a free trial. The documentation was accurate; it wasn't built to meet someone at the point of failure.",
        'The “Get started” page read as an overview, not a starting point, and build errors led to pages that explained concepts but never addressed the specific error.']),
    split('03 — Research', 'Watching developers solve real tasks', paras=[
        "To test what I'd seen in the documentation, I ran contextual inquiry sessions with 9 participants across three segments — builders, entry-level developers and experienced developers — observing how they actually solved real Google Cloud tasks: prototyping in Vertex AI Studio, troubleshooting a permissions error, and exploring documentation under pressure."]),
    insight('Key insight', 'Developers rarely read documentation sequentially or proactively. They consult it <strong style="font-weight: 600">reactively, as a precision anchor</strong> when things break — and prioritize interactive, actionable, visually clear steps.'),
    evidence([
        ('AI is the new front door.', '70% of participants used AI before documentation', '“AI, then human experience, and then last thing, documentation. Because documentation is very long, it could take like hours just reading nonstop until you find the answer.” — P7'),
        ('Action over concept.', '100% of participants reached for tools beyond documentation to finish a task', '“Documentation is fine. It’s just that it should have been guiding me to the console or UI that allows me to add or remove permissions.” — P6'),
        ('Tasks cut across products.', '0% of participants completed a task using a single doc page', '“I got the information that I needed, but I feel like it wasn’t enough to continue as a person who first got introduced to this problem or assignment.” — P5')], minw=280),
    section_title('04 — The pivot', 'Information seeking → execution'),
    cards(None, None, [
        ('The assumption', '“Redesign documentation in the AI era” — but January’s segmentation was all human: builders, entry-level, experienced. AI was a tool people used. Not yet a reader.'),
        ('The evidence', 'Same findings, read differently: ~70% reaching for AI first, zero finishing on a single page. Not just how people searched — proof of who’s actually reading.'),
        ('The correction', 'The reader changes too. Documentation was written for a human who seeks, then acts. Increasingly, the one executing is the agent, and the human’s role shifts to approving what it does.')], numbered=True, minw=280),
    split('05 — Solution', 'Documentation Skills', paras=[
        'Skills transform static documentation into actionable workflows that help users move from problem to resolution faster. Each Skill is a SKILL.md an AI agent can follow, grounded in official Google Cloud documentation. Skills enable AI agents to:'], bullets=[
        f'<strong {B}>Follow structured instructions</strong> — accelerate task completion',
        f'<strong {B}>Reduce ambiguity</strong> — reduce cognitive load',
        f'<strong {B}>Execute repeatable workflows</strong> — improve workflow consistency',
        f'<strong {B}>Deliver consistent outcomes</strong> — grounded in official docs']),
    figure(None, None, [('gcd-detail.jpg', 'Fix 403 Forbidden Access Skill page with overview, Execute button and a command for different coding agents')]),
    cards(None, None, [
        ('Overview', 'Every Skill opens with what it does, not how — the problem it solves, its category, and what changes on your system if you run it. Before “Execute” ever appears, a user already knows whether this is the right fix.'),
        ('Execution', 'One Execute action, plus a copyable command for the agent the user already works in — Antigravity, Claude Code, Codex, Cursor or Gemini CLI.'),
        ('Instruction', 'Clarifying questions, prerequisites, numbered steps and validation logic, each tied back to the documentation source behind it.')], numbered=True, minw=280),
    split('06 — Solution', 'Multiple entry points', paras=[
        'Skills are still new to many users, including people who use AI tools every day. So we placed entry points where people already are: search in the prompt box, onboarding, an introduction page, the Skill library, and the original documentation pages.']),
    gallery([('gcd-home-slash.jpg', 'Typing / in the home prompt box lists Skills', 'Home — type / for Skills'),
             ('gcd-skills.jpg', 'Skills introduction page', 'Skills introduction')], minw=420,
            title=None, desc=None),
    gallery([('gcd-library.jpg', 'Skill library filtered by goals, products and types', 'Skill library'),
             ('gcd-on-doc.jpg', 'IAM documentation page with an embedded Skill', 'Skills on a documentation page')], minw=420),
    ext_link('Try the prototype', 'Home, Skills introduction, Skill library, Skill detail and Skills on a documentation page.', PROTO, 'Open prototype'),
    cards('07 — Usability testing', 'Five patterns from testing', [
        ('Skills concept confusion', 'AI familiarity predicted understanding: engineers who used AI daily got it; others struggled.'),
        ('Execute button opacity', 'Two of three participants were unsure what Execute would actually do.'),
        ('Context over standalone docs', 'Everyone preferred Skills inside the environment where they were already working.'),
        ('Search over browse', 'Two of three skipped the home page and library and went straight to search.'),
        ('Trust through context fit', 'Trust came from the Google source and a close match to their situation — not from reading the code.')], numbered=True, minw=220),
    quote('If I trust Google, and this is on the Google Doc, then I don’t really care what it’s running.', 'U1, usability study'),
    split('08 — Iteration', 'One recommendation per finding', paras=[
        'Each pattern became a recommendation for the next iteration. The highest priorities: a “What is a Skill?” explainer, an Execute button that states its outcome, a preview of the execution mode, trust signals such as source attribution, and a Skills flow embedded in the console.'], bullets=[
        'Lead with search; deprioritize browsing the library.',
        'Separate what people read from what the AI agent executes.',
        'Test alternative command names, and use progressive disclosure for the full documentation.']),
    split('09 — Outcome', 'What we learned', white=True, top=96, bottom=96, bullets=[
        f'<strong {B}>Developers are execution-first.</strong> They run first and read the docs only when something fails.',
        f'<strong {B}>“AI as navigator, docs as anchor” held up</strong> from formative research through usability testing.',
        f'<strong {B}>Trust and outcome clarity are the critical gaps</strong> — where the next version most needs to improve.',
        f'<strong {B}>People stay in control.</strong> No meaningful cloud action runs without the user’s review and approval.']),
    nxt("Unifying Samsung's enterprise platforms", SAM),
])


P['CaseStudy-GoogleCloud-v1.dc.html'] = page('Google Cloud documentation — Case study (v1)', [
    hero(['Google Cloud × UW HCDE', 'AI documentation', 'Agent-ready content'],
         'Google Cloud documentation for the AI era',
         'Developers now ask AI first and open the docs only to check the answer. With the Google Cloud Documentation team, we asked how documentation should change when AI, not the human, is the first reader — and answered with Skills: task-oriented workflows, grounded in official docs, that people and AI agents can both follow.',
         [('Role', 'UX designer in a team of four'), ('Sponsor', 'Google Cloud Documentation team'), ('Timeline', '20 weeks · Winter – Spring 2026'), ('Methods', 'Friction logs, contextual inquiry, design sprint, usability testing')]),
    cover('gcd-home.jpg', 'Prototype home page: Google Cloud Documentation with an AI prompt box to build, scale and optimize with Documentation Skills'),
    stats([('7 of 9', 'participants started their tasks with AI before any docs'), ('11', 'research themes synthesized from contextual inquiry'), ('30', 'Skills defined across a three-axis taxonomy'), ('1.2M', 'human users of Google Cloud documentation')]),
    split('01 — The challenge', 'The docs are no longer the first stop', top=112, paras=[
        'Google Cloud documentation supports more than 100 cloud services and is organized by product. It is an authoritative reference — but people reach for it differently now. They move between AI tools, search, community answers and the official docs, and the docs often come last.',
        'The project started as docs.cloud.google.com launched as a dedicated home for technical documentation. Our guiding question: how should the documentation experience evolve when AI is increasingly the first reader?']),
    cards('02 — Discover', 'Mapping the friction first', [
        ('Friction logs', 'Each of us onboarded, deployed to Cloud Run and followed a BigQuery ML tutorial, logging every moment of hesitation.'),
        ('Competitive analysis', 'Five documentation platforms — Google Cloud, AWS, Microsoft Learn, OpenAI and Vercel — compared on how they support AI-assisted work.'),
        ('SWOT and literature review', 'Information-seeking is non-linear, and interactive, code-centered formats reduce cognitive load.'),
        ('User segmentation', 'Builders as the primary segment, plus entry-level and experienced developers.')], numbered=True, minw=240),
    split('03 — Contextual inquiry', 'AI first, docs last', paras=[
        'Nine participants — builders, engineers and future developers — completed four realistic Google Cloud tasks: building an app, fixing a permission error, troubleshooting BigQuery and exploring models in Vertex AI. Finishing the task was not the point; we studied how, when and why they switched between AI, documentation and search.',
        'We clustered what we saw into eleven themes. Three mattered most:'], bullets=[
        f'<strong {B}>AI is the default entry point.</strong> Seven of nine started with AI before touching any other source.',
        f'<strong {B}>Action over concepts.</strong> Participants wanted step-by-step instructions and abandoned concept-heavy pages.',
        f'<strong {B}>Product-centered structure breaks continuity.</strong> Docs organized by product forced people to rebuild a workflow across many pages — one task took five tool switches.']),
    quote('AI first, then human experience, and then last thing, documentation. Because documentation is very long.', 'P7, contextual inquiry'),
    cards('04 — Design direction', 'AI as the navigator, documentation as the anchor', [
        ('Put AI at the center of the workflow', 'Documentation treats the AI agent as the primary reader, not the human.'),
        ('Accuracy through context recognition', 'Documentation reads user signals and brings back the same trusted content in the order the user needs it.'),
        ('Bridge reading and doing', 'Documentation packages its own content into workflows that can be executed.')], numbered=True, minw=280),
    split('05 — The solution', 'Skills: documentation that can be executed', paras=[
        'A Skill is a task-oriented, agent-readable workflow grounded in official Google Cloud documentation. It is written as a SKILL.md file an AI agent can follow, while the Skill page gives people the same steps in a form they can read, check and run.',
        'We ran a design-sprint week to get from problem to a testable prototype: map the problem, sketch competing solutions, decide on Skills, build a high-fidelity prototype, and test it with people.']),
    figure('Skills, explained', 'An introduction page explains what a Skill is, what is inside one and how it helps both humans and AI agents.', [('gcd-skills.jpg', 'Skills introduction page explaining that Skills turn static documentation into actionable, reusable workflows')]),
    figure('Skill library', 'Thirty Skills, filterable by seven user goals, fifteen product categories and four Skill types. Each card shows steps, time and the outcome at a glance.', [('gcd-library.jpg', 'Skill library with filters for goals, products and types, and cards such as Fix 403 Forbidden Access')]),
    figure('Skill detail', 'Each Skill answers the questions a user asks in order: what problem is this, what do I need, what will the steps do, and what should I check before I execute. A copyable command runs it in the agent of their choice.', [('gcd-detail.jpg', 'Fix 403 Forbidden Access Skill page with overview, Execute button and a command for different coding agents')]),
    figure('Skills on a documentation page', 'The right Skill appears inside the documentation page the user is already reading, connecting the explanation directly to a workflow they can run.', [('gcd-on-doc.jpg', 'IAM access-control documentation page with an embedded Fix 403 Forbidden Access Skill')]),
    ext_link('Try the prototype', 'Home, Skills introduction, Skill library, Skill detail and Skills on a documentation page.', PROTO, 'Open prototype'),
    cards('06 — Usability testing', 'Five patterns from testing', [
        ('Skills concept confusion', 'AI familiarity predicted understanding: engineers who used AI daily got it; others struggled.'),
        ('Execute button opacity', 'Two of three participants were unsure what Execute would actually do.'),
        ('Context over standalone docs', 'Everyone preferred Skills inside the environment where they were already working.'),
        ('Search over browse', 'Two of three skipped the home page and library and went straight to search.'),
        ('Trust through context fit', 'Trust came from the Google source and a close match to their situation — not from reading the code.')], numbered=True, minw=220),
    quote('If I trust Google, and this is on the Google Doc, then I don’t really care what it’s running.', 'U1, usability study'),
    split('07 — Iteration', 'One recommendation per finding', paras=[
        'Each pattern became a recommendation for the next iteration. The highest priorities: a “What is a Skill?” explainer, an Execute button that states its outcome, a preview of the execution mode, trust signals such as source attribution, and a Skills flow embedded in the console.'], bullets=[
        'Lead with search; deprioritize browsing the library.',
        'Separate what people read from what the AI agent executes.',
        'Test alternative command names, and use progressive disclosure for the full documentation.']),
    split('08 — Responsible AI', 'People stay in control', paras=[
        'Skills touch real cloud resources, so we used a Responsible AI impact assessment to set the guardrails: no meaningful action without the user’s review and approval, a clear preview of what a Skill will do, links back to the documentation behind every step, and extra checks for production and security-sensitive work.']),
    split('09 — Outcome', 'What we learned', white=True, top=96, bottom=96, bullets=[
        f'<strong {B}>Developers are execution-first.</strong> They run first and read the docs only when something fails.',
        f'<strong {B}>“AI as navigator, docs as anchor” held up</strong> from formative research through usability testing.',
        f'<strong {B}>Trust and outcome clarity are the critical gaps</strong> — where the next version of the prototype most needs to improve.',
        'Final readout and process book delivered to the Google Cloud Documentation team.']),
    nxt("Unifying Samsung's enterprise platforms", SAM),
])


def score_dots(v):
    if v is None:
        return '<span style="font-size: 13px; color: #8A8C93">Not scored</span>'
    lo, hi, label = v
    d = ''
    for i in range(1, 8):
        col = '{{accent}}' if i <= lo else ('#9DAAF0' if i <= hi else '#E2E2DC')
        d += f'<span style="width: 12px; height: 12px; border-radius: 50%; background: {col}; display: inline-block"></span>'
    return f'<span style="display: inline-flex; align-items: center; gap: 4px">{d}<span style="font-size: 16px; font-weight: 600; margin-left: 8px; font-variant-numeric: tabular-nums">{label}</span></span>'

def scorecard(title, desc, cols, rows, note):
    th = ''.join(f'<th scope="col" style="text-align: left; font-weight: 500; font-size: 13px; color: #4A4C53; padding: 0 16px 12px 0">{e(c)}</th>' for c in cols)
    tr = ''
    for who, vals in rows:
        tds = ''.join(f'<td style="padding: 14px 16px 14px 0; border-top: 1px solid #ECECE6; white-space: nowrap">{score_dots(v)}</td>' for v in vals)
        tr += f'<tr><th scope="row" style="text-align: left; font-weight: 600; font-size: 16px; padding: 14px 16px 14px 0; border-top: 1px solid #ECECE6">{e(who)}</th>{tds}</tr>'
    return f"""<section style="{W}; padding: 32px 24px"><div style="background: #FFFFFF; border: 1px solid #E2E2DC; border-radius: 16px; padding: 28px; display: flex; flex-direction: column; gap: 20px">
<div style="display: flex; flex-direction: column; gap: 8px; max-width: 48rem"><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.015em">{e(title)}</span><p style="margin: 0; font-size: 16px; line-height: 1.6; color: #4A4C53">{desc}</p></div>
<div style="overflow-x: auto"><table style="border-collapse: collapse; min-width: 560px"><thead><tr><th style="padding: 0 16px 12px 0"></th>{th}</tr></thead><tbody>{tr}</tbody></table></div>
<p style="margin: 0; font-size: 13px; line-height: 1.5; color: #4A4C53">{e(note)}</p></div></section>"""

P['CaseStudy-GoogleCloud-v3.dc.html'] = page('Agent Skills for Documentation — Case study (v3)', [
    hero(['UW HCDE × Google Cloud', 'AI documentation', 'Agent Skills'],
         'Agent Skills for Documentation',
         'Developers now ask AI first and open the docs only to check the answer. With the Google Cloud Documentation team, I led research and design on Skills — workflows grounded in official docs that people and AI agents can both follow.',
         [('Role', 'UX designer & researcher in a team of four'), ('Partner', 'Google Cloud Documentation team'), ('Program', 'UW HCDE capstone · 2026'), ('Methods', 'Friction logs, contextual inquiry, design sprint, usability testing')]),
    pull("When developers stopped reading docs and started prompting AI, Google Cloud's documentation had to learn a new language."),
    cover('gcd-home-slash.jpg', 'Prototype home page: typing / in the AI prompt box lists Documentation Skills such as gcloud Commands Quick Reference and Onboarding to Google Cloud'),
    split('01 — Context', 'AI is becoming the first reader', top=64, paras=[
        "Google Cloud's documentation supports more than 100 cloud services, but people increasingly reach it through AI rather than reading it directly. The documentation team put the shift plainly:",
        '<span style="font-size: 22px; line-height: 1.5; color: #121316">“AI has fundamentally reshaped how people seek, explore, and consume information.”</span>']),
    evidence([
        ('AI agents are reading documentation.', '48% of doc views by AI', 'Source: Write the Docs 2026 Conference'),
        ('AI-generated code is increasing.', '50% → 75% in 6 months', 'Fall 2025 to April 2026 · Source: Google Cloud Next 2026'),
        ('Documentation is becoming infrastructure for AI agents.', None, 'Source: Write the Docs 2026 Conference')]),
    split('02 — The challenge', 'The docs are no longer the first stop', paras=[
        'Google Cloud documentation is organized by product. It is an authoritative reference — but people reach for it differently now. They move between AI tools, search, community answers and the official docs, and the docs often come last.',
        'The project started as docs.cloud.google.com launched as a dedicated home for technical documentation. Our guiding question: how should the documentation experience evolve when AI is increasingly the first reader?']),
    cards('03 — Discover', 'Mapping the friction first', [
        ('Friction logs', 'Each of us onboarded, deployed to Cloud Run and followed a BigQuery ML tutorial, logging every moment of hesitation.'),
        ('Competitive analysis', 'Five documentation platforms — Google Cloud, AWS, Microsoft Learn, OpenAI and Vercel — compared on how they support AI-assisted work.'),
        ('SWOT and literature review', 'Information-seeking is non-linear, and interactive, code-centered formats reduce cognitive load.'),
        ('User segmentation', 'Builders as the primary segment, plus entry-level and experienced developers.')], numbered=True, minw=240),
    split('04 — Research', 'Watching developers solve real tasks', paras=[
        "To test what I'd seen in the documentation, I ran contextual inquiry sessions with 9 participants across three segments — builders, entry-level developers and experienced developers — observing how they actually solved real Google Cloud tasks: prototyping in Vertex AI Studio, troubleshooting a permissions error, and exploring documentation under pressure."]),
    insight('Key insight', 'Developers rarely read documentation sequentially or proactively. They consult it <strong style="font-weight: 600">reactively, as a precision anchor</strong> when things break — and prioritize interactive, actionable, visually clear steps.'),
    evidence([
        ('AI is the new front door.', '7 of 9 (78%) participants used AI before documentation', 'Contextual inquiry · 9 participants'),
        ('Action over concept.', '100% of participants reached for tools beyond documentation to finish a task', '“Documentation is fine. It’s just that it should have been guiding me to the console or UI that allows me to add or remove permissions.” — P6'),
        ('Tasks cut across products.', '0% of participants completed a task using a single doc page', '“I got the information that I needed, but I feel like it wasn’t enough to continue as a person who first got introduced to this problem or assignment.” — P5')], minw=280),
    quote('AI first, then human experience, and then last thing, documentation. Because documentation is very long.', 'P7, contextual inquiry'),
    section_title('05 — The pivot', 'Information seeking → execution'),
    cards(None, None, [
        ('The assumption', '“Redesign documentation in the AI era” — but January’s segmentation was all human: builders, entry-level, experienced. AI was a tool people used. Not yet a reader.'),
        ('The evidence', 'Same findings, read differently: 7 of 9 reaching for AI first, zero finishing on a single page. Not just how people searched — proof of who’s actually reading.'),
        ('The correction', 'The reader changes too. Documentation was written for a human who seeks, then acts. Increasingly, the one executing is the agent, and the human’s role shifts to approving what it does.')], numbered=True, minw=280),
    split('06 — Solution', 'Documentation Skills', paras=[
        'Skills transform static documentation into actionable workflows that help users move from problem to resolution faster. Each Skill is a SKILL.md an AI agent can follow, grounded in official Google Cloud documentation. Skills enable AI agents to:'], bullets=[
        f'<strong {B}>Follow structured instructions</strong> — accelerate task completion',
        f'<strong {B}>Reduce ambiguity</strong> — reduce cognitive load',
        f'<strong {B}>Execute repeatable workflows</strong> — improve workflow consistency',
        f'<strong {B}>Deliver consistent outcomes</strong> — grounded in official docs']),
    figure(None, None, [('gcd-detail.jpg', 'Fix 403 Forbidden Access Skill page with overview, Execute button and a command for different coding agents')]),
    cards(None, None, [
        ('Overview', 'Every Skill opens with what it does, not how — the problem it solves, its category, and what changes on your system if you run it. Before “Execute” ever appears, a user already knows whether this is the right fix.'),
        ('Execution', 'One Execute action, plus a copyable command for the agent the user already works in — Antigravity, Claude Code, Codex, Cursor or Gemini CLI.'),
        ('Instruction', 'Clarifying questions, prerequisites, numbered steps and validation logic, each tied back to the documentation source behind it.')], numbered=True, minw=280),
    split('07 — Solution', 'Multiple entry points', paras=[
        'Skills are still new to many users, including people who use AI tools every day. So we placed entry points where people already are: search in the prompt box, onboarding, an introduction page, the Skill library, and the original documentation pages.']),
    gallery([('gcd-home-slash.jpg', 'Typing / in the home prompt box lists Skills', 'Home — type / for Skills'),
             ('gcd-skills.jpg', 'Skills introduction page', 'Skills introduction')], minw=420),
    gallery([('gcd-library.jpg', 'Skill library filtered by goals, products and types', 'Skill library'),
             ('gcd-on-doc.jpg', 'IAM documentation page with an embedded Skill', 'Skills on a documentation page')], minw=420),
    section_title('08 — Outcomes', 'What we delivered, and how to measure it'),
    stats([('30', 'Skills defined across 7 goals, 15 products and 4 types'), ('5', 'entry points, from the prompt box to the doc page'), ('5', 'developers in usability testing'), ('9', 'design recommendations for the next iteration')]),
    scorecard('Measured in usability testing', 'UMUX-Lite and the Single Ease Question (SEQ), each on a 7-point scale. U2 marked ease down to 5 because the Execute button was unclear — the gap the CTA redesign targets.',
        ['Features met my requirements', 'Easy to use', 'Task ease (SEQ)'],
        [('U1', [(7, 7, '7/7'), (7, 7, '7/7'), (7, 7, '7/7')]),
         ('U2', [(5, 6, '5–6/7'), (5, 5, '5/7'), None]),
         ('U3', [None, None, (5, 5, '≈5/7')])],
        'Three valid sessions; scores are read alongside what participants said, not as statistics. U2 rated usefulness 5–6 depending on whether the docs were their starting point; U3 called the task easy because there were few options, not because the concept was clear.'),
    f'<section style="{W}; padding: 48px 24px 0"><p style="margin: 0; font-size: 16px; line-height: 1.6; color: #4A4C53; max-width: 48rem"><strong style="color: #121316; font-weight: 600">Proposed success metrics.</strong> Metrics follow Google’s HEART framework (Happiness, Engagement, Adoption, Retention, Task success), with safe execution added as a guardrail metric. These are proposed for a next phase and were not measured during the capstone; usability findings were shared with Google as qualitative feedback.</p></section>',
    cards(None, None, [
        ('Task success', 'Share of tasks finished without leaving the docs for an outside AI tool. Baseline: 0 of 9 participants finished on a single doc page.'),
        ('Efficiency', 'Tool switches and time to resolution per task. Baseline: one research task took five tool switches.'),
        ('Adoption', 'Skill runs per entry point — prompt box, library, introduction page and documentation pages.'),
        ('Happiness and trust', 'UMUX-Lite and SEQ after a Skill run, and how confident users feel before they press Execute.'),
        ('Retention', 'Users who run a Skill again within 30 days.'),
        ('Safe execution', 'Share of runs reviewed and approved before execution, and how often a change is rolled back.')], minw=300),
    ext_link('Try the prototype', 'Home, Skills introduction, Skill library, Skill detail and Skills on a documentation page.', PROTO, 'Open prototype'),
    cards('09 — Usability testing', 'Five patterns from testing', [
        ('Skills concept confusion', 'AI familiarity predicted understanding: engineers who used AI daily got it; others struggled.'),
        ('Execute button opacity', 'Two of three participants were unsure what Execute would actually do.'),
        ('Context over standalone docs', 'Everyone preferred Skills inside the environment where they were already working.'),
        ('Search over browse', 'Two of three skipped the home page and library and went straight to search.'),
        ('Trust through context fit', 'Trust came from the Google source and a close match to their situation — not from reading the code.')], numbered=True, minw=220),
    quote('If I trust Google, and this is on the Google Doc, then I don’t really care what it’s running.', 'U1, usability study'),
    split('10 — Iteration', 'A fix for every finding', white=True, top=96, bottom=96, paras=[
        'Each pattern became a recommendation for the next iteration. The highest priorities: a “What is a Skill?” explainer, an Execute button that states its outcome, a preview of the execution mode, trust signals such as source attribution, and a Skills flow embedded in the console.'], bullets=[
        'Lead with search; deprioritize browsing the library.',
        'Separate what people read from what the AI agent executes.',
        'Test alternative command names, and use progressive disclosure for the full documentation.']),
    nxt("Unifying Samsung's enterprise platforms", SAM),
])


# ---------------- SAMSUNG PROCUREMENT (sub) ----------------
P['CaseStudy-SamsungProcurement.dc.html'] = page('Samsung procurement — Case study', [
    hero(['SAP × Samsung', 'N-ERP', 'Procurement'],
         'Integrated material purchasing process',
         "Samsung's buyers negotiated prices and distributed volumes in Excel, across seven different material codes and four systems. As part of Samsung's next-generation ERP (N-ERP), we turned that manual work into an automated purchasing process — with end users shaping every phase.",
         [('Role', 'UI & UX designer, with two design colleagues'), ('Responsibility', 'Design thinking workshop, research, interviews, UI design, usability tests'), ('Tools', 'SAP Fiori, SAP Build, Axure'), ('Client', 'Samsung Electronics · N-ERP')],
         kicker='Samsung enterprise platforms · Project 1 of 5'),
    cover('proc-hero.png', 'Negotiation overview dashboard with savings, spend trend and category spend'),
    stats([('42.5%', 'less process time across the procurement workflow'), ('50+', 'end users involved across workshops, interviews and tests'), ('10', 'design iterations driven by user feedback'), ('5 weeks', 'from planning to validated high-fidelity design')]),
    split('01 — The challenge', 'Negotiation by spreadsheet', top=112, paras=[
        'Negotiation preparation and price distribution were done by hand in Excel. Buyers worked with seven different material codes globally and four separate systems to gather data and communicate — a process prone to human error.',
        'Our design direction: improve efficiency, shorten processing and decision time, simplify complex work, make data visible, and minimize manual tasks through process automation.']),
    figure('02 — A user-centered process', 'From design thinking workshops to final user tests, end users were key stakeholders. We uncovered pain points and hidden problems with them, had them generate the first ideas for the new process, and iterated up to ten times on their feedback.', [('proc-process.png', 'Five-week process from planning through design thinking workshop, interviews, feedback sessions and usability tests')]),
    cards(None, None, [
        ('Discover · W2–W3', 'Design thinking workshop (12 end users, 8 project owners), user interviews (13 end users) and a feedback session (11 end users).'),
        ('Design · W4–W5', 'Two online usability tests in SAP Build (32 and 23 user responses), a knowledge session, and an offline test and survey.'),
        ('Outcomes', 'As-is process and journey maps, stakeholder map, key UX values, then lo-fi prototypes refined into high-fidelity Fiori designs.')], minw=280),
    figure('03 — From as-is to to-be', 'Storyboards contrasted the manual process with an automated one where users understand current conditions at a glance.', [('proc-storyboard.png', 'As-is and to-be storyboards for the purchasing process')]),
    cards(None, None, [
        ('Negotiation dashboard', 'Was: quarterly Excel data gathering, hard to track afterward. Now: a negotiation-specific dashboard shows current work and progress at a glance.'),
        ('Automated RFQ and simulation', 'Was: per-vendor price and allocation negotiated by hand, with little history. Now: RPA filters RFQ errors and users simulate prices and allocations.'),
        ('Automatic reporting', 'Was: repeated report-making before, during and after negotiation. Now: reports are visualized automatically, with views for buyers and part or group leaders.'),
        ('Standardized work', 'Was: non-standard, person-dependent work. Now: standardized, efficient processes that support strategic decisions.')], minw=260),
    figure('04 — Rapid prototyping', 'We sketched the flows by hand and tested them with users before moving to high fidelity.', [('proc-lofi.jpg', 'Hand-drawn prototypes of negotiation screens and a team workshop photo')]),
    figure('05 — High-fidelity design', 'Clickable high-fidelity prototypes in Axure, built on the SAP Fiori design system and refined through online usability tests.', [('proc-hifi.jpg', 'Grid of high-fidelity negotiation, savings and RFQ screens')]),
    split('06 — Outcome', 'A faster, automated purchasing process', white=True, top=96, bottom=96, bullets=[
        'Total procurement process time reduced by 42.5%.',
        'Negotiation, RFQ, simulation and reporting brought into one connected flow.',
        'A design validated by end users at every phase, through up to ten iterations.']),
    nxt('Carbon footprint management (ESG)', 'CaseStudy-SamsungESG.dc.html', back_href=SAM, back_label='Samsung overview', kicker='Next Samsung project'),
], back_href=SAM, back_label='Samsung overview')


# ---------------- SAMSUNG STUB SUB-PAGES ----------------
def placeholder(label, h=420):
    return f'<section style="{W}; padding: 32px 24px"><div role="img" aria-label="Image placeholder" style="height: {h}px; border-radius: 16px; background: #E6ECEE; display: flex; align-items: center; justify-content: center; color: #4A4C53; font-size: 13px; text-align: center; padding: 0 24px">{e(label)}</div></section>'

def samsung_stub(fname, n, tags, title, lead, meta, next_title, next_href):
    P[fname] = page(f'{title} — Samsung case study', [
        hero(tags, title, lead, meta, kicker=f'Samsung enterprise platforms · Project {n} of 5'),
        placeholder('[Project cover image]', 520),
        stats([('[ADD]', '[Key result 1]'), ('[ADD]', '[Key result 2]'), ('[ADD]', '[Key result 3]')]),
        split('01 — The challenge', '[ADD challenge headline]', top=112, paras=['[ADD — the business problem, who was affected, and what was slow, manual or fragmented.]']),
        split('02 — My role and process', '[ADD process headline]', paras=['[ADD — research, workshops, collaboration with domain experts, iterations.]']),
        section_title('03 — The design', 'Key screens'),
        placeholder('[Screen 1]'), placeholder('[Screen 2]'),
        split('04 — Outcome', '[ADD outcome headline]', white=True, top=96, bottom=96, bullets=['[ADD result]', '[ADD result]']),
        split('05 — What I learned', 'Reflections', paras=['[ADD reflection]']),
        nxt(next_title, next_href, back_href=SAM, back_label='Samsung overview', kicker='Next Samsung project'),
    ], back_href=SAM, back_label='Samsung overview')

samsung_stub('CaseStudy-SamsungDSCloud.dc.html', 3, ['SAP × Samsung', 'DS division', 'Cloud platform'], 'DS cloud platform',
    'An enterprise cloud workspace for the semiconductor division on SAP BTP and Work Zone. [ADD one-sentence summary of the problem and what changed.]',
    [('Role', '[ADD ROLE]'), ('Team', '[ADD TEAM]'), ('Platform', 'SAP BTP, SAP Work Zone'), ('Client', 'Samsung Electronics · DS division')],
    'DX risk management', 'CaseStudy-SamsungDXRisk.dc.html')
samsung_stub('CaseStudy-SamsungDXRisk.dc.html', 4, ['SAP × Samsung', 'DX division', 'Data analytics'], 'DX risk management',
    'Data analytics dashboard design for the device experience division in SAP Analytics Cloud. [ADD one-sentence summary of the problem and what changed.]',
    [('Role', '[ADD ROLE]'), ('Team', '[ADD TEAM]'), ('Platform', 'SAP Analytics Cloud'), ('Client', 'Samsung Electronics · DX division')],
    'Shipment', 'CaseStudy-SamsungShipment.dc.html')
samsung_stub('CaseStudy-SamsungShipment.dc.html', 5, ['SAP × Samsung', 'Logistics', 'Process redesign'], 'Shipment',
    'Process redesign and application modernization for shipment operations. [ADD one-sentence summary of the problem and what changed.]',
    [('Role', '[ADD ROLE]'), ('Team', '[ADD TEAM]'), ('Platform', '[ADD PLATFORM]'), ('Client', 'Samsung Electronics')],
    'Integrated material purchasing (N-ERP)', 'CaseStudy-SamsungProcurement.dc.html')

# ---------------- FINANCIAL PLANNING HUB ----------------
P[FPA] = page('Financial planning and analysis — Case study', [
    hero(['SAP Analytics Cloud', 'Finance', 'Two engagements'],
         'Financial planning and analysis',
         'Finance teams at two global companies were planning in spreadsheets and fighting their tools. For BHP and JG Summit, I redesigned planning, review and reporting in SAP Analytics Cloud — fewer screens, Excel-like input and dashboards that reach decision-makers automatically.',
         [('Role', 'User research, workshop facilitation, data visualization, UI design'), ('Clients', 'BHP (mining, Australia) · JG Summit (conglomerate, Philippines)'), ('Platform', 'SAP Analytics Cloud'), ('Duration', '4 weeks · 4 months')]),
    cover('bhp-hero.jpg', 'Total cost planning dashboard in SAP Analytics Cloud on a laptop'),
    stats([('10 → 4', 'planning tables for BHP, without losing information'), ('5 → 2', 'screens in the BHP planning flow'), ('3+ weeks', 'of Excel reporting replaced for JG Summit'), ('1', 'source of truth from input to executive dashboard')]),
    split('The shared challenge', 'Planning trapped in Excel', top=112, paras=[
        'In both companies, budgeting and forecasting relied on manual Excel work and workarounds — slow tools, too many steps, human error and reports that took weeks, leaving finance professionals stuck in operational tasks instead of analysis.']),
    section_title('Featured projects', 'Two engagements in depth'),
    f'''<section style="{W}; padding: 16px 24px 32px"><div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); gap: 32px">
{project_link('Redesigning financial planning for BHP', 'A faster, simpler planning flow in SAC for a global mining company — 10 tables on 5 screens consolidated into 4 tables on 2, with Excel-like input.', 'bhp-thumb.png', 'BHP total cost dashboard', 'CaseStudy-BHP.dc.html', 'BHP · 4 weeks · Data visualization')}
{project_link('Enterprise financial planning for JG Summit', 'Explore and Discover workshops across business units, then one planning flow with dashboards shared automatically with executives.', 'jg-thumb.png', 'Flour sales overview dashboard', 'CaseStudy-JGSummit.dc.html', 'JG Summit · 4 months · Workshop facilitation')}
</div></section>''',
    split('What connects them', 'Lessons from finance UX', bullets=[
        'Financial planners are rarely satisfied with one tool; to win over Excel, a planning tool has to offer what Excel cannot.',
        'Data accuracy and timeliness matter as much as the interface — production, sales and budget data are deeply interconnected.',
        'Financial terms like gross profit and EBITDA shape how numbers should be structured and visualized.']),
    nxt('Samsung e-commerce: one-stop pricing management', 'CaseStudy-SamsungEcom.dc.html'),
])

if __name__ == '__main__':
    out = sys.argv[1]
    for name, html_ in P.items():
        open(os.path.join(out, name), 'w', encoding='utf-8').write(html_)
        print(name, len(html_))
