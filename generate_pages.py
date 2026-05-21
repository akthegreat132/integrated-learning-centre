import re
import os

pages = [
    {
        "filename": "jee-coaching-gurgaon.html",
        "slug": "jee-coaching-gurgaon",
        "title": "JEE Coaching in Gurgaon | Best Classes | The Integrated Learning Centre",
        "desc": "Top-rated JEE coaching in Gurugram. Expert faculty and comprehensive study material for IIT JEE Advanced and Main preparation."
    },
    {
        "filename": "neet-coaching-gurgaon.html",
        "slug": "neet-coaching-gurgaon",
        "title": "NEET Coaching in Gurgaon | Best Classes | The Integrated Learning Centre",
        "desc": "Top-rated NEET coaching in Gurugram. Expert faculty and comprehensive study material for medical entrance exam preparation."
    },
    {
        "filename": "physics-tuition-gurgaon.html",
        "slug": "physics-tuition-gurgaon",
        "title": "Physics Tuition in Gurgaon | Best Classes | The Integrated Learning Centre",
        "desc": "Expert Physics tuition in Gurugram for Class 11, 12, ICSE, ISC, IB, and competitive exams."
    },
    {
        "filename": "chemistry-tuition-gurgaon.html",
        "slug": "chemistry-tuition-gurgaon",
        "title": "Chemistry Tuition in Gurgaon | Best Classes | The Integrated Learning Centre",
        "desc": "Expert Chemistry tuition in Gurugram for Class 11, 12, ICSE, ISC, IB, and competitive exams."
    },
    {
        "filename": "ib-physics-gurgaon.html",
        "slug": "ib-physics-gurgaon",
        "title": "IB Physics Tuition in Gurgaon | Best Classes | The Integrated Learning Centre",
        "desc": "Specialized IB Physics DP coaching in Gurugram. Expert tutors for SL and HL to achieve a perfect 7."
    },
    {
        "filename": "class-11-physics-gurgaon.html",
        "slug": "class-11-physics-gurgaon",
        "title": "Class 11 Physics Tuition in Gurgaon | Best Classes | The Integrated Learning Centre",
        "desc": "Dedicated Class 11 Physics tuition in Gurugram. Build strong fundamentals for boards and competitive exams."
    },
    {
        "filename": "class-12-chemistry-gurgaon.html",
        "slug": "class-12-chemistry-gurgaon",
        "title": "Class 12 Chemistry Tuition in Gurgaon | Best Classes | The Integrated Learning Centre",
        "desc": "Dedicated Class 12 Chemistry tuition in Gurugram. Master concepts for boards and competitive exams."
    }
]

with open("index.html", "r", encoding="utf-8") as f:
    original_html = f.read()

current_desc = 'content="Join The Integrated Learning Centre in Gurgaon for JEE, NEET, CBSE, ICSE, IB and IGCSE coaching. Expert Physics, Chemistry and Maths faculty with small batches and personalized attention."'

for page in pages:
    html = original_html
    
    # Replace title
    html = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', html)
    html = html.replace('content="Best JEE, NEET, CBSE, ICSE & IB Coaching in Gurgaon | The Integrated Learning Centre"', f'content="{page["title"]}"')
    
    # Replace description (for normal, og, twitter)
    html = html.replace(current_desc, f'content="{page["desc"]}"')
    
    # Replace URLs
    orig_url = "https://theintegratedlearningcentre.com/"
    new_url = f"https://theintegratedlearningcentre.com/{page['slug']}"
    
    # Canonical link
    html = html.replace(f'<link rel="canonical" href="{orig_url}">', f'<link rel="canonical" href="{new_url}">')
    
    # OG URL
    html = html.replace(f'<meta property="og:url" content="{orig_url}">', f'<meta property="og:url" content="{new_url}">')
    
    # Twitter URL
    html = html.replace(f'<meta property="twitter:url" content="{orig_url}">', f'<meta property="twitter:url" content="{new_url}">')
    
    # JSON-LD URL
    html = html.replace(f'"url": "{orig_url}"', f'"url": "{new_url}"')

    with open(page["filename"], "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Updated {page['filename']} with new fixes")
