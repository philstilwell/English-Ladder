# English Ladder 🧗‍♂️

Welcome to the **English Ladder** project! This repository hosts a website that **automatically publishes a new, advanced ESL lesson every single day.**

The system is completely self-sustaining. Every morning, it pulls the latest breaking news headlines, uses state-of-the-art Gemini AI (Google AI Studio utilizing Nano Banana Pro) to shape that news into a complete curriculum, updates the website files, and deploys the changes live.

## How the Core Files Work Together (The Dynamic Cycle)

The system relies on five interconnected components, visualized in the project infographic.

### 1. The Schedule/Alarm Clock ⏰

**File:** `.github/workflows/cron.yml`

* **Simple Purpose:** This file contains the schedule for the entire operation. It is an automated command that tells GitHub: *"Wake up every single day at exactly 12:00 UTC (8:00 AM EST) and run our robot worker script."* It is the initial **"DAILY LAUNCH"**.

### 2. The Robot Worker (Automation Script) 🤖

**File:** `update_site.py`

* **Simple Purpose:** This Python script does all the heavy lifting in a sequential process.
* **Fetch:** It connects to the live BBC World News RSS feed and gets the very latest headlines.
* **Generate:** It sends those news summaries and a complex curriculum prompt to the Gemini AI in Google AI Studio.
* **Parse:** Once the AI generates the ESL content (News Brief, Vocabulary, and Quiz), this Python script takes that raw text and structures it perfectly for a website.

### 3. The Website (The Living Document) 🌐

**File:** `index.html`

* **Simple Purpose:** This **IS** the actual website. This file stores the current daily lesson and a rolling archive of the seven most recent lessons. When the `update_site.py` script finishes its work, it automatically **injects** the fresh lesson at the very top of this file and decomps (removes) any lessons that are older than 7 days, keeping the page lean and fast.

### 4. The Project Portrait (Visual Guide) 🗺️

**File:** `English-Ladder.png`

* **Simple Purpose:** This is the detailed **PNG infographic** that visualizes exactly how all these parts fit together and work dynamically in a circular, self-sustaining ecosystem. It maps out the journey from the daily launch to the automatic deployment on the web.

### 5. The System ID Card 🏷️

**File:** `.gitattributes`

* **Simple Purpose:** A behind-the-scenes system file. Its only job is to tell GitHub’s technical systems: *"Treat this repository as a Python project when you are running your internal calculations and statistics."
