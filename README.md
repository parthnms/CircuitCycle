# CircuitCycle — E-Waste Collection & Recycling Business Website

A business website for an authorized e-waste collection, IT asset disposal, and enterprise carbon credits business, modeled after [green-stream-dispose.lovable.app](https://green-stream-dispose.lovable.app).

## 🌟 Key Features

- **Pixel-Accurate Design & Typography**: Built using the exact styling design system, OKLCH color palettes (emerald green `#236f4d`, electric lime `#c2f53b`, and dark forest `#14231b`), and Google Fonts (`Sora` for headings, `Inter` for body).
- **Responsive Layout**: Designed for mobile, tablet, and desktop screens with a mobile navigation drawer and sticky blurred header.
- **Complete Multi-Page Structure**:
  - `index.html`: Homepage featuring hero metrics, "Who We Serve", "How It Works" 4-step workflow, environmental impact stats, and compliance callout.
  - `services.html`: Comprehensive breakdown of Household Pickup, Corporate ITAD, Industrial E-Waste, Certified Data Destruction, Material Recovery, and EPR Compliance.
  - `pricing.html`: Buyback price matrix (what we pay you) and certified disposal service tiers (Household ₹199, Corporate ₹12/kg, Industrial Custom).
  - `partners.html`: **Integrated Partner Network** featuring:
    - **E-Commerce Trade-In & Exchange Fulfillment**: Reverse logistics, AI grading, and EPR compliance for platforms like Amazon, Flipkart, and electronics retailers.
    - **Developer REST API Showcase**: Interactive cURL & JSON request/response documentation (`POST /v1/exchange/quote`).
    - **Salvaged Tested OEM Spare Parts Marketplace**: B2B circular parts inventory for independent repair shops and refurbishers (Logic boards, FHD/OLED displays, server PSUs, camera modules).
    - **Interactive Parts Filter & Application Form**: Live brand/category filtering, one-click inquiry batch pre-fill, and partner onboarding application modal with tracking IDs (`CC-PTNR-XXXX`).
  - `carbon-credits.html`: Enterprise managed forests, carbon sequestration quantification, credit generation, and trading desk.
  - `about.html`: Origin story, mission, the 4 core driving values, and a dedicated spotlight on visionary young founder **Parth Saxena** and his commitment to societal impact.
  - `contact.html`: Doorstep pickup scheduling form with instant feedback and reference tracking ID generation.
- **Leadership & Vision Spotlight**:
  - Highlights founder **Parth Saxena**: a young entrepreneur dedicating his venture to societal welfare, preventing toxic contamination of groundwater, upskilling youth with dignified green jobs, and pioneering high-integrity carbon offsets.
- **Interactive Tools**:
  - **Live E-Waste Estimate Calculator**: Select device category (laptops, phones, servers, scrap PCBs), quantity, and condition to view real-time buyback payout or disposal fee estimates.
  - **Enterprise Carbon Simulator**: Slide emissions from 50 to 5,000 tonnes of CO₂ to calculate native trees needed and forest hectares under management.
  - **Spare Parts Inventory Filter**: Filter genuine extracted components by brand (Apple, Dell, Lenovo, HP, Samsung) and component category in real time.
  - **Pickup & Partner Booking Modals**: Submits requests, assigns reference IDs (e.g., `#CC-84920` or `#CC-PTNR-7291`), and persists records in browser local storage.

---

## 🚀 How to Run Locally

### Option 1: Run with Python (Recommended)
You can run the included Python server which serves all pages and automatically launches your browser:
```powershell
python serve.py
```
Or with standard Python command:
```powershell
python -m http.server 8000
```
Then visit: [http://localhost:8000](http://localhost:8000)

### Option 2: Open Directly
Because all CSS, JS, and SVG icons are self-contained with no heavy compilation dependencies, you can also double-click `index.html` to open it directly in any browser.

---

## 📁 Project Structure

```
d:\Parth1c\SustainabiityBusiness\
├── index.html           # Homepage & Founder Spotlight
├── services.html        # Services overview & deliverables
├── partners.html        # E-Commerce exchange fulfillment & OEM spare parts
├── pricing.html         # Buyback matrix, disposal plans & interactive calculator
├── carbon-credits.html  # Managed forestry & carbon offset simulator
├── about.html           # Founder Parth Saxena bio, story, values & impact
├── contact.html         # Pickup booking form & contact details
├── css/
│   └── styles.css       # Complete responsive CSS design system
├── js/
│   └── main.js          # Calculators, parts filters, partner forms & modals
├── assets/
│   └── favicon.svg      # CircuitCycle SVG brand favicon
├── serve.py             # Local development server runner
└── README.md            # Documentation
```

---

## 🌐 Deployment Options

This website is ready for static deployment to any hosting provider:
- **GitHub Pages**: Push this repository and activate GitHub Pages on the `main` branch.
- **Vercel / Netlify**: Drag-and-drop the project folder or connect via Git.
- **Firebase Hosting**: Run `firebase deploy` after initializing.
