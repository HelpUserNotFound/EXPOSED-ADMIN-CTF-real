from flask import Flask, Response

app = Flask(__name__)


@app.after_request
def add_header(resp):
    resp.headers["X-Environment"] = "QLC-DEV"
    return resp


def layout(title, content):

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Quality Learing Center</title>

<style>

body {{
margin:0;
font-family:Segoe UI, sans-serif;
background:#f5f7fb;
color:#374151;
}}

.header {{
background:#4A3F35;
color:white;
padding:18px 40px;
display:flex;
justify-content:space-between;
align-items:center;
}}

.logo {{
font-size:20px;
font-weight:600;
}}

.logo span {{
color:#9BC53D;
}}

.nav a {{
color:white;
margin-left:25px;
text-decoration:none;
font-size:14px;
}}

.hero {{
background:#5FB3A5;
color:white;
padding:70px 40px;
}}

.section {{
padding:50px 40px;
}}

.cards {{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:20px;
margin-top:20px;
}}

.card {{
background:white;
padding:20px;
border-radius:8px;
box-shadow:0 1px 3px rgba(0,0,0,0.05);
border-top:4px solid #9BC53D;
}}

.footer {{
background:#2F7F7B;
color:white;
padding:30px 40px;
margin-top:40px;
}}

.btn {{
background:#9BC53D;
color:white;
padding:10px 18px;
text-decoration:none;
border-radius:4px;
display:inline-block;
margin-top:10px;
}}

.hero{{
background-image:url("/assets/naughty.jpg");
background-size:cover;
background-position:center;
padding:120px 40px;
position:relative;
color:white;
}}

.hero-overlay{{
background:rgba(0,0,0,0.35);
padding:40px;
border-radius:6px;
max-width:600px;
}}

</style>

</head>

<body>

<div class="header">
<div class="logo">Quality <span>Learing</span> Center</div>

<div class="nav">
<a href="/">Home</a>
<a href="/programs">Programs</a>
<a href="/about">About</a>
<a href="/contact">Contact</a>
</div>
</div>

{content}

<div class="footer">
Quality Learing Center 2026<br>
Professional tutoring and academic success programs
</div>

</body>
</html>
"""


# HOME
@app.route("/")
def home():

    content = """
<div class="hero">
<div class="hero-overlay">
<h1>Helping Students Succeed</h1>
<p>Professional tutoring for math, reading, and technology.</p>
</div>
</div>

<div class="section">
<h2>Our Services</h2>

<div class="cards">

<div class="card">
<h3>Math Tutoring</h3>
<p>Algebra, calculus, and exam prep.</p>
</div>

<div class="card">
<h3>Reading Programs</h3>
<p>Improve comprehension and fluency.</p>
</div>

<div class="card">
<h3>STEM Prep</h3>
<p>Technology and science instruction.</p>
</div>

</div>
</div>
"""

    return layout("Home", content)


# PROGRAMS
@app.route("/programs")
def programs():

    content = """
<div class="section">

<h2>Available Programs</h2>

<div class="cards">

<div class="card">
<h3>Elementary Support</h3>
<p>Foundational reading and math skills.</p>
<img src="/static/classroom.avif" width="100%">
</div>

<div class="card">
<h3>High School Prep</h3>
<p>ACT, SAT, and college readiness.</p>
<img src="/static/naughty.jpg" width="100%">
</div>

<div class="card">
<h3>Technology Track</h3>
<p>Programming and computer literacy.</p>
<img src="/static/bad-class.jpg" width="100%">

<!-- dev cluster moved -->
<!-- qlc-learing-dev -->

</div>

</div>

</div>
"""

    return layout("Programs", content)


# ABOUT
@app.route("/about")
def about():

    content = """
<div class="section">

<h2>About Quality Learing Center</h2>

<div class="card">
<p>
Quality Learing Center has helped students succeed for over 10 years.
Our instructors provide personalized academic guidance in a professional
learning environment.
</p>

<p>
We specialize in math, reading, and technology instruction
for students of all ages.
</p>
<img src="/assets/dev/classroom.png" width="100%">
</div>

</div>

"""

    return layout("About", content)


# CONTACT
@app.route("/contact")
def contact():

    content = """
<div class="section">

<h2>Contact Us</h2>

<div class="cards">

<div class="card">
<h3>Phone</h3>
<p>1-800-FRAUD</p>
</div>

<div class="card">
<h3>Email</h3>
<p>info@qlc-learing.edu</p>
</div>

<div class="card">
<h3>Location</h3>
<p>123 Education Way<br>Provo, UT</p>
</div>

</div>

</div>

<script src="/static/app.js"></script>
"""

    return layout("Contact", content)


# JS CLUE
@app.route("/static/app.js")
def js():
    return Response(
"""
// TODO remove before production
// admin dashboard moved
// dev-admin
""",
        mimetype="application/javascript"
    )


# ROBOTS CLUE
@app.route("/robots.txt")
def robots():
    return Response(
"""User-agent: *
Disallow: /admin
Disallow: /dev
Disallow: /internal
Disallow: /staging
""",
        mimetype="text/plain"
    )


# SITEMAP CLUE
@app.route("/sitemap.xml")
def sitemap():
    return Response(
"""<?xml version="1.0" encoding="UTF-8"?>
<urlset>
<url><loc>/</loc></url>
<url><loc>/programs</loc></url>
<url><loc>/contact</loc></url>
<url><loc>/admin</loc></url>
</urlset>
""",
        mimetype="application/xml"
    )


# fake asset path clue
@app.route("/assets/dev/classroom.png")
def fake_img():
    return "", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)