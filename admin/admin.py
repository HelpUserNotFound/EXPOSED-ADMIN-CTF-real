from flask import Flask, request, redirect, url_for
# from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

USERS = {
    'admin': "admin",
    "user": "password"
}


@app.route("/")
def login():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Quality Learing Center | Admin Portal</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #1f2937, #111827);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
        }

        .login-box {
            background-color: #1f2937;
            padding: 40px;
            border-radius: 8px;
            width: 320px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        }

        .login-box h2 {
            margin-top: 0;
            text-align: center;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
            border: none;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #10b981;
            border: none;
            color: white;
            font-weight: bold;
            cursor: pointer;
            border-radius: 4px;
        }

        button:hover {
            background-color: #059669;
        }

        .note {
            text-align: center;
            font-size: 12px;
            margin-top: 15px;
            color: #9ca3af;
        }
    </style>
</head>
<body>

<!-- 
Don't forget to delete page before publishing!!
thats not right!

Username: admin
Password: admin
 -->

<div class="login-box">
    <h2>Admin Development Portal</h2>
    <form method="POST" action="/login">
        <input name="username" placeholder="Username">
        <input name="password" type="password" placeholder="Password"> 
        <button type="submit">Login</button>
    </form>
    <div class="note">
        Internal Use Only - Dev Environment
    </div>
</div>

</body>
</html>
"""

@app.route("/login", methods=["POST"])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in USERS and USERS[username] == password:
        return redirect(url_for("dashboard"))
    return "<h3> Invalid credentials </h3>"
    

@app.route("/dashboard")
def dashboard():
    return"""
<!DOCTYPE html>
<html>
<head>
<title>Quality Learing Center | Infrastructure Admin</title>

<style>
body {
margin:0;
font-family: "Segoe UI", Tahoma, sans-serif;
background:#f5f7fb;
}

.topbar {
height:60px;
background:#0f172a;
color:white;
display:flex;
align-items:center;
justify-content:space-between;
padding:0 20px;
box-shadow:0 2px 4px rgba(0,0,0,0.1);
}

.logo {
font-weight:600;
font-size:18px;
}

.topbar-right {
font-size:14px;
color:#cbd5e1;
}

.layout {
display:flex;
}

.sidebar {
width:240px;
background:white;
height:calc(100vh - 60px);
border-right:1px solid #e5e7eb;
padding-top:20px;
}

.sidebar a {
display:block;
padding:12px 24px;
color:#374151;
text-decoration:none;
font-size:14px;
}

.sidebar a:hover {
background:#f1f5f9;
}

.sidebar-title {
padding:10px 24px;
font-size:12px;
color:#9ca3af;
text-transform:uppercase;
}

.content {
flex:1;
padding:30px;
}

.page-title {
font-size:24px;
margin-bottom:20px;
}

.cards {
display:grid;
grid-template-columns: repeat(4, 1fr);
gap:20px;
margin-bottom:20px;
}

.card {
background:white;
padding:20px;
border-radius:8px;
box-shadow:0 1px 3px rgba(0,0,0,0.05);
}

.card-title {
font-size:12px;
color:#6b7280;
margin-bottom:10px;
}

.card-value {
font-size:22px;
font-weight:600;
}

.grid {
display:grid;
grid-template-columns: 2fr 1fr;
gap:20px;
}

.table {
width:100%;
border-collapse:collapse;
}

.table th {
text-align:left;
font-size:12px;
color:#6b7280;
padding-bottom:10px;
}

.table td {
padding:10px 0;
border-top:1px solid #eee;
font-size:14px;
}

.status-green { color:#10b981; }
.status-yellow { color:#f59e0b; }
.status-red { color:#ef4444; }

.activity {
font-size:14px;
}

.activity div {
padding:8px 0;
border-bottom:1px solid #eee;
}

</style>
</head>

<body>

<div class="topbar">
<div class="logo">Quality Learing Center Infrastructure</div>
<div class="topbar-right">
dev-admin-01 • Development Environment
</div>
</div>

<div class="layout">

<div class="sidebar">

<div class="sidebar-title">Overview</div>
<a href="/dashboard">Dashboard</a>
<a href="/deployments">Deployments</a>
<a href="/services">Services</a>

<div class="sidebar-title">Management</div>
<a href="/users">Users</a>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">Configuration</a>
<a href="/logs">System Logs</a>


</div>

<div class="content">

<div class="page-title">Infrastructure Dashboard</div>

<div class="cards">

<div class="card">
<div class="card-title">Active Services</div>
<div class="card-value">12</div>
</div>

<div class="card">
<div class="card-title">Running Containers</div>
<div class="card-value">28</div>
</div>

<div class="card">
<div class="card-title">Deployments Today</div>
<div class="card-value">5</div>
</div>

<div class="card">
<div class="card-title">Cluster Nodes</div>
<div class="card-value">3</div>
</div>

</div>

<div class="grid">

<div class="card">
<h3>Service Status</h3>

<table class="table">
<tr>
<th>Service</th>
<th>Status</th>
<th>Version</th>
</tr>

<tr>
<td>web-api</td>
<td class="status-green">Running</td>
<td>v1.3-dev</td>
</tr>

<tr>
<td>auth-service</td>
<td class="status-green">Running</td>
<td>v2.1</td>
</tr>

<tr>
<td>worker</td>
<td class="status-yellow">Degraded</td>
<td>v0.9-beta</td>
</tr>

<tr>
<td>internal-admin</td>
<td class="status-green">Running</td>
<td>v1.0</td>
</tr>

</table>

</div>

<div class="card">
<h3>Recent Activity</h3>

<div class="activity">
<div>✔ Deployment completed: web-api</div>
<div>✔ Config reload triggered</div>
<div>✔ User admin logged in</div>
<div>⚠ Worker container restarted</div>
<div>✔ Registry sync complete</div>
</div>

</div>

</div>

<div class="card" style="margin-top:20px;">
<h3>System Information</h3>

<table class="table">
<tr>
<td>Hostname</td>
<td>dev-admin-01</td>
</tr>

<tr>
<td>Environment</td>
<td>Development</td>
</tr>

<tr>
<td>Docker Version</td>
<td>24.0.5</td>
</tr>

<tr>
<td>Kubernetes</td>
<td>Disabled (local cluster)</td>
</tr>

<tr>
<td>Internal Network</td>
<td>learing-dev-net</td>
</tr>

<tr>
<td>Registry</td>
<td>registry.internal.learing.local</td>
</tr>

</table>

</div>

</div>
</div>

</body>
</html>
"""


# USERS PAGE

@app.route("/users")
def users():
    return """
<html>
<head>
<style>
body{margin:0;font-family:Segoe UI;background:#f5f7fb;}
.topbar{height:60px;background:#0f172a;color:white;display:flex;align-items:center;padding:0 20px;}
.layout{display:flex;}

.sidebar {
width:240px;
background:white;
height:calc(100vh - 60px);
border-right:1px solid #e5e7eb;
padding-top:20px;
}

.sidebar a {
display:block;
padding:12px 24px;
color:#374151;
text-decoration:none;
font-size:14px;
}

.sidebar a:hover {
background:#f1f5f9;
}

.sidebar-title {
padding:10px 24px;
font-size:12px;
color:#9ca3af;
text-transform:uppercase;
}
.content{flex:1;padding:30px;}
.card{background:white;padding:20px;border-radius:8px;}
.table{width:100%;border-collapse:collapse;}
.table td,.table th{padding:12px;border-top:1px solid #eee;}
</style>
</head>

<body>

<div class="topbar">Quality Learing Center Infrastructure</div>

<div class="layout">

<div class="sidebar">

<div class="sidebar-title">Overview</div>
<a href="/dashboard">Dashboard</a>
<a href="/deployments">Deployments</a>
<a href="/services">Services</a>

<div class="sidebar-title">Management</div>
<a href="/users">Users</a>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">Configuration</a>
<a href="/logs">System Logs</a>


</div>

<div class="content">

<h2>Users</h2>

<div class="card">

<table class="table">
<tr>
<th>Username</th>
<th>Role</th>
<th>Status</th>
<th>Last Login</th>
</tr>

<tr>
<td>admin</td>
<td>Administrator</td>
<td>Active</td>
<td>2 minutes ago</td>
</tr>

<tr>
<td>deploy-bot</td>
<td>Service Account</td>
<td>Active</td>
<td>1 hour ago</td>
</tr>

<tr>
<td>dev-user</td>
<td>Developer</td>
<td>Active</td>
<td>Yesterday</td>
</tr>

</table>

</div>

</div>
</div>

</body>
</html>
"""


# SERVICES PAGE
@app.route("/services")
def services():
    return """
<html>
<head>
<style>
body{margin:0;font-family:Segoe UI;background:#f5f7fb;}
.topbar{height:60px;background:#0f172a;color:white;display:flex;align-items:center;padding:0 20px;}
.layout{display:flex;}
.sidebar {
width:240px;
background:white;
height:calc(100vh - 60px);
border-right:1px solid #e5e7eb;
padding-top:20px;
}

.sidebar a {
display:block;
padding:12px 24px;
color:#374151;
text-decoration:none;
font-size:14px;
}

.sidebar a:hover {
background:#f1f5f9;
}

.sidebar-title {
padding:10px 24px;
font-size:12px;
color:#9ca3af;
text-transform:uppercase;
}}
.content{flex:1;padding:30px;}
.card{background:white;padding:20px;border-radius:8px;}
.table{width:100%;border-collapse:collapse;}
.table td{padding:10px;border-top:1px solid #eee;}
.status-green{color:#10b981;}
.status-red{color:#ef4444;}
</style>
</head>

<body>

<div class="topbar">Quality Learing Center Infrastructure</div>

<div class="layout">

<div class="sidebar">

<div class="sidebar-title">Overview</div>
<a href="/dashboard">Dashboard</a>
<a href="/deployments">Deployments</a>
<a href="/services">Services</a>

<div class="sidebar-title">Management</div>
<a href="/users">Users</a>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">Configuration</a>
<a href="/logs">System Logs</a>


</div>

<div class="content">

<h2>Services</h2>

<div class="card">

<table class="table">
<tr>
<td>web-api</td>
<td class="status-green">Running</td>
<td>Port 5000</td>
</tr>

<tr>
<td>auth-service</td>
<td class="status-green">Running</td>
<td>Port 5002</td>
</tr>

<tr>
<td>internal-admin</td>
<td class="status-green">Running</td>
<td>Port 5001</td>
</tr>

<tr>
<td>worker</td>
<td class="status-red">Stopped</td>
<td>N/A</td>
</tr>

</table>

</div>

</div>
</div>

</body>
</html>
"""

# DEPLOYMENTS PAGE

@app.route("/deployments")
def deployments():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Deployments</title>
<style>
body{margin:0;font-family:Segoe UI;background:#f5f7fb;}
.topbar{height:60px;background:#0f172a;color:white;display:flex;align-items:center;justify-content:space-between;padding:0 20px;}
.layout{display:flex;}
.sidebar {
width:240px;
background:white;
height:calc(100vh - 60px);
border-right:1px solid #e5e7eb;
padding-top:20px;
}

.sidebar a {
display:block;
padding:12px 24px;
color:#374151;
text-decoration:none;
font-size:14px;
}

.sidebar a:hover {
background:#f1f5f9;
}

.sidebar-title {
padding:10px 24px;
font-size:12px;
color:#9ca3af;
text-transform:uppercase;
}
.content{flex:1;padding:30px;}
.card{background:white;padding:20px;border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,0.05);}
.table{width:100%;border-collapse:collapse;}
.table th{font-size:12px;color:#6b7280;text-align:left;padding-bottom:10px;}
.table td{padding:12px 0;border-top:1px solid #eee;}
.status-green{color:#10b981;}
.status-yellow{color:#f59e0b;}
</style>
</head>

<body>

<div class="topbar">
<div>Quality Learing Center Infrastructure</div>
<div>Deployment Manager</div>
</div>

<div class="layout">

<div class="sidebar">

<div class="sidebar-title">Overview</div>
<a href="/dashboard">Dashboard</a>
<a href="/deployments">Deployments</a>
<a href="/services">Services</a>

<div class="sidebar-title">Management</div>
<a href="/users">Users</a>
<a href="https://www.youtube.com/watch?v=xvFZjo5PgG0">Configuration</a>
<a href="/logs">System Logs</a>


</div>

<div class="content">

<h2>Deployments</h2>

<div class="card">

<table class="table">
<tr>
<th>Service</th>
<th>Version</th>
<th>Environment</th>
<th>Status</th>
<th>Deployed By</th>
<th>Time</th>
</tr>

<tr>
<td>web-api</td>
<td>v1.3-dev</td>
<td>development</td>
<td class="status-green">Running</td>
<td>deploy-bot</td>
<td>2 min ago</td>
</tr>

<tr>
<td>auth-service</td>
<td>v2.1</td>
<td>development</td>
<td class="status-green">Running</td>
<td>ci-pipeline</td>
<td>15 min ago</td>
</tr>

<tr>
<td>worker</td>
<td>v0.9-beta</td>
<td>development</td>
<td class="status-yellow">Restarting</td>
<td>admin</td>
<td>1 hour ago</td>
</tr>

</table>

</div>

</div>
</div>

</body>
</html>
"""

# logs page

@app.route("/logs")
def logs():
    return """
<!DOCTYPE html>
<html>
<head>
<title>System Logs</title>

<style>
body{
margin:0;
font-family:monospace;
background:#0b1220;
color:#e5e7eb;
}

.topbar{
height:60px;
background:#020617;
color:white;
display:flex;
align-items:center;
justify-content:space-between;
padding:0 20px;
border-bottom:1px solid #111827;
}

.logs{
height:calc(100vh - 60px);
overflow-y:auto;
padding:20px;
font-size:13px;
line-height:1.6;
}

.line{ padding:2px 0; }

.info{ color:#93c5fd; }
.warn{ color:#f59e0b; }
.error{ color:#ef4444; }
.success{ color:#10b981; }
.dim{ color:#6b7280; }

</style>
</head>

<body>

<div class="topbar">
<div>Quality Learing Center Infrastructure Logs</div>
<div>dev-admin-01 • /var/log/internal-admin.log</div>
</div>

<div class="logs" id="logs"></div>

<script>

const logLines = [

{t:"dim",m:"[2026-03-28 09:12:01] Booting internal admin service"},
{t:"info",m:"[INFO] Loading environment configuration"},
{t:"info",m:"[INFO] Environment: development"},
{t:"info",m:"[INFO] Loading service manifest"},
{t:"info",m:"[INFO] Checking container runtime"},
{t:"success",m:"[OK] Docker runtime detected"},
{t:"info",m:"[INFO] Connecting to registry.internal.learing.local"},
{t:"success",m:"[OK] Registry connection established"},
{t:"info",m:"[INFO] Starting container monitor"},
{t:"info",m:"[INFO] Starting metrics collector"},
{t:"success",m:"[OK] Metrics collector ready"},
{t:"info",m:"[INFO] Initializing auth service"},
{t:"success",m:"[OK] auth-service container running"},
{t:"info",m:"[INFO] Initializing web-api"},
{t:"success",m:"[OK] web-api container running"},
{t:"warn",m:"[WARN] worker container unhealthy"},
{t:"info",m:"[INFO] Restarting worker container"},
{t:"success",m:"[OK] worker container restarted"},
{t:"info",m:"[INFO] Loading deployment history"},
{t:"success",m:"[OK] Deployment cache loaded"},

{t:"dim",m:"---------------------------------------------"},

{t:"info",m:"[INFO] Syncing container state"},
{t:"info",m:"[INFO] Node: dev-node-01"},
{t:"info",m:"[INFO] CPU usage: 12%"},
{t:"info",m:"[INFO] Memory usage: 48%"},
{t:"info",m:"[INFO] Disk usage: 63%"},
{t:"success",m:"[OK] Node healthy"},
{t:"info",m:"[INFO] Checking internal network"},
{t:"success",m:"[OK] learing-dev-net reachable"},
{t:"info",m:"[INFO] Validating service routes"},
{t:"success",m:"[OK] All routes active"},

{t:"dim",m:"---------------------------------------------"},

{t:"info",m:"[INFO] Deployment triggered: web-api"},
{t:"info",m:"[INFO] Pulling image learing/web-api:v1.3-dev"},
{t:"info",m:"[INFO] Downloading layer 1/4"},
{t:"info",m:"[INFO] Downloading layer 2/4"},
{t:"info",m:"[INFO] Downloading layer 3/4"},
{t:"info",m:"[INFO] Downloading layer 4/4"},
{t:"success",m:"[OK] Image pulled successfully"},
{t:"info",m:"[INFO] Replacing running container"},
{t:"success",m:"[OK] Deployment completed"},
{t:"info",m:"[INFO] Running post-deploy checks"},
{t:"success",m:"[OK] Health checks passed"},

{t:"dim",m:"---------------------------------------------"},

{t:"info",m:"[INFO] User authentication request"},
{t:"success",m:"[OK] User admin authenticated"},
{t:"info",m:"[INFO] Session created: 9f2a31ab3"},
{t:"info",m:"[INFO] Loading user permissions"},
{t:"success",m:"[OK] Permissions loaded"},
{t:"info",m:"[INFO] Fetching dashboard metrics"},
{t:"success",m:"[OK] Metrics loaded"},

{t:"dim",m:"---------------------------------------------"},

{t:"warn",m:"[WARN] Using development deployment token"},
{t:"dim",m:"[DEBUG] dev_deploy_token=FLAG{exposed_admin_port}"},

{t:"dim",m:"---------------------------------------------"},

{t:"info",m:"[INFO] Syncing container metrics"},
{t:"info",m:"[INFO] Node status: healthy"},
{t:"success",m:"[OK] Metrics updated"},
{t:"info",m:"[INFO] Polling service health"},
{t:"success",m:"[OK] web-api healthy"},
{t:"success",m:"[OK] auth-service healthy"},
{t:"success",m:"[OK] worker healthy"},
{t:"info",m:"[INFO] Writing runtime state"},
{t:"success",m:"[OK] State saved"},
{t:"info",m:"[INFO] Admin service ready"}

];

let i = 0;

function streamLogs() {
    if (i >= logLines.length) return;

    const log = logLines[i];
    const div = document.createElement("div");

    div.className = "line " + log.t;
    div.textContent = log.m;

    document.getElementById("logs").appendChild(div);

    document.getElementById("logs").scrollTop =
        document.getElementById("logs").scrollHeight;

    i++;

    setTimeout(streamLogs, 100);   // slower
}

window.onload = streamLogs;

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)