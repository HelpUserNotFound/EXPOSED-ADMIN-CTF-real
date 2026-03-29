# EXPOSED-ADMIN-CTF-real
Read up on the capec 121 if you want a clue.

If not, more clues will be provided below:
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
You sure you want clues?
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Okay, you must be desprate...
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Exploit-Non-Production-Interfaces WALKTHROUGH (use at your own risk)
CAPEC-121

## Objective
Exploit an exposed non-production admin interface that was unintentionally left accessible. This demonstrates **CAPEC-121: Exploit Non-Production Interfaces**.

---

## Step 1 — Download the CTF

Clone the repository from GitHub and unzip the files:

```bash
git clone https://github.com/BYU-ECE-Software/Cyber-266-Vulnerability-Walkthroughs/tree/main/Exploit-Non-Production-Interfaces
cd exposed-admin-ctf
```

---

## Step 2 — Start the Docker Environment

From inside the project directory, build and start the containers:

```bash
docker compose up --build
```

Docker will:

- Build the web container  
- Build the admin container  
- Install Flask  
- Start both applications  

You should see logs begin streaming in the terminal.

---

## Step 3 — Access the Target Website

Open your browser and navigate to:

```
http://localhost:8000
```

This is the public-facing web application. We will now begin looking for additional exposed services.

---

## Step 4 — Scan for Open Ports Using Nmap

Install Nmap if needed.

### Mac
```bash
brew install nmap
```

### Linux
```bash
sudo apt install nmap
```

### Windows
Download from: https://nmap.org/

Now scan localhost:

```bash
nmap localhost
```

Example output:

```
PORT     STATE SERVICE
8000/tcp open  http
8080/tcp open  http-proxy
8090/tcp open  http-proxy
```

From this screen, we can see all the other ports and services that are open and potentially vulnerable. This could define how we continue our attack. Here, we see that port **8080** is also open. This is commonly used for admin or internal services and shouldn't be publicly accessible. 

Navigate to:

```
http://localhost:8080
```

You should now see an admin login page that was not intended to be public.

---

## Step 5 — Access the Admin Interface

Because this is a non-production interface, it often uses weak or default credentials.

Try common combinations such as:

```
admin / admin
admin / password
admin / admin123
administrator / password
```

Once authenticated, you will gain access to the exposed admin panel, completing the exploit. From here any number of attacks could be performed. As we saw in the metasploit CTF, all were missing here is a payload now that were in the system.

---


## Attack Flow Summary

1. Start the application  
2. Access public site (port 8000)  
3. Scan for open ports  
4. Discover admin interface (port 8080)  
5. Guess weak credentials  
6. Gain admin access  
