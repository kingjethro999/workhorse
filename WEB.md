# WEB.md — Workhorse Universal Web Showcase & Product Portal Architecture

> **System Standard Specification & Engineering Handbook for the Workhorse Web Interface**  
> **Version:** 1.0.0-PRO  
> **Target Framework:** Modern Web (Astro 5 / Next.js 15 / Vanilla Web Components / Three.js / CSS Scroll-Driven Animations)  
> **Design Philosophy:** Cyber-Industrial Obsidian Dark Mode (`#070a11`), High-Compositor Motion, Interactive Three.js/Canvas Animated Mechanical Workhorse, View Transitions API, Zero-Friction Terminal Showcase.  
> **Primary Purpose:** Public Product Showcase, Interactive Architecture Exploder, One-Line Installation Hub, and Documentation Portal (NOT an active execution playground).

---

## TABLE OF CONTENTS

1. [Executive Overview & Vision](#1-executive-overview--vision)
   - 1.1 Web App Mission & Boundaries
   - 1.2 Design Philosophy & Visual Language
   - 1.3 Target Performance & Core Web Vitals (CWV)
2. [The Centerpiece: The Animated Cybernetic Workhorse](#2-the-centerpiece-the-animated-cybernetic-workhorse)
   - 2.1 Visual Anatomy & Cybernetic Aesthetic
   - 2.2 Three.js / WebGL & Canvas 2D Hybrid Architecture
   - 2.3 Interactive State Engine (Idle, Trot, Gallop, Rear, Glow)
   - 2.4 The Dynamic 5-Cycle Neural Core (Visualizing Model Cascades)
   - 2.5 Full WCAG 2.2.2 & `prefers-reduced-motion` Compliance
3. [Information Architecture & Route Hierarchy](#3-information-architecture--route-hierarchy)
   - 3.1 Route Map (`/`, `/install`, `/architecture`, `/docs`, `/benchmarks`, `/community`)
   - 3.2 Page-by-Page Specifications
4. [Modern Web Motion & Animation System](#4-modern-web-motion--animation-system)
   - 4.1 Scroll-Driven Animations (`animation-timeline: view()`)
   - 4.2 Scrollytelling: "The Journey of a Prompt"
   - 4.3 View Transitions API (`document.startViewTransition()`)
   - 4.4 Hardware-Accelerated Micro-Interactions (Compositor Only)
5. [Component Design System & UI Specifications](#5-component-design-system--ui-specifications)
   - 5.1 Glassmorphic Global Header & Route Navigation
   - 5.2 The Interactive Terminal Window Simulator (`<TerminalSimulator />`)
   - 5.3 One-Click Tri-Alias Installation Bar (`<InstallCommand />`)
   - 5.4 The Radial 5-Cycle Resilience Ring Visualizer
   - 5.5 Cross-Agent Skills & MCP Interop Matrix
6. [Complete Production Frontend Implementation Code](#6-complete-production-frontend-implementation-code)
   - 6.1 `src/components/AnimatedHorse.tsx` (Three.js / Canvas 3D Workhorse)
   - 6.2 `src/components/TerminalSimulator.tsx` (Interactive TUI Replay)
   - 6.3 `src/components/InstallBar.tsx` (Clipboard & Shell Selector)
   - 6.4 `src/components/ResilienceRing.tsx` (Radial Provider Cascade)
   - 6.5 `src/styles/motion.css` (Scroll-Driven CSS & Transitions)
   - 6.6 `src/styles/tokens.css` (Design Tokens & Color Palette)
7. [SEO, Social Graph & Metadata Strategy](#7-seo-social-graph--metadata-strategy)
   - 7.1 Dynamic OpenGraph (OG) Generator
   - 7.2 Structured Data (JSON-LD) for SoftwareApplication
8. [Accessibility, Progressive Enhancement & Browser Support](#8-accessibility-progressive-enhancement--browser-support)
   - 8.1 Motion Controls (Visible Pause/Play WCAG 2.2.2)
   - 8.2 Baseline Widely Available vs Newly Available Fallback Matrix
9. [Build, Deployment & Static Edge Hosting](#9-build-deployment--static-edge-hosting)
   - 9.1 Edge Hosting Runbook (Cloudflare Pages / Vercel / Netlify)
   - 9.2 Asset Optimization & Three.js Model Compression (Draco/KTX2)

---

## 1. Executive Overview & Vision

### 1.1 Web App Mission & Boundaries
The Workhorse Web Interface is the official digital front door and product showcase for the Workhorse Terminal Workstation. 

**Strict Operational Boundary:**  
The web application is **NOT** a browser-based execution sandbox or online playground for running Workhorse. Workhorse is inherently an on-device, active working repository operator anchored to local terminals, local files, and local Ollama daemons. Attempting to simulate local filesystem mutations or execute bash tools inside a browser would compromise the core identity of the product.

Instead, the web interface serves four distinct missions:
1. **Showcase the Vision:** Communicate the radical philosophy of Workhorse — zero-friction terminal ubiquity (`workhorse`, `workhouse`, `wh`), active working repository operations (no restrictive sandboxing), the 5-Cycle Infinite Resilience Ring, and live streaming thought accordions (no opaque spinners).
2. **Interactive Architectural Exploder:** Allow visitors to visually dissect how Workhorse routes prompts across local Ollama models and cloud LPUs (Groq, Nvidia NIM, Gemini, OpenRouter), how it crawls with Firecrawl/Jina/Tavily, and how it borrows skills from Claude Code and Cursor.
3. **One-Click Universal Installation:** Provide developers with instant, copy-pasteable installation scripts across Linux, macOS, and Windows PowerShell, complete with PATH verification guides.
4. **Interactive Simulated Demonstrations:** Feature a high-fidelity `<TerminalSimulator />` that demonstrates real Workhorse workflows (e.g. running `wh` in `~/Desktop/promptdock` to audit a codebase and rewrite `README.md` in place).

### 1.2 Design Philosophy & Visual Language
The website embodies a **Cyber-Industrial Obsidian** aesthetic:
- **Base Canvas:** Deep obsidian black (`#070a11` and `#0b0f19`), evocative of high-end developer terminal viewports.
- **Surface Panels:** Translucent dark glass (`rgba(17, 24, 39, 0.7)`) with backdrop blur (`backdrop-filter: blur(16px)`) and fine hairline borders (`rgba(255, 255, 255, 0.08)`).
- **Core Accents:**
  - Electric Cyan (`#38bdf8`): Represents the unified CLI and local terminal interactions.
  - Cyber Mint (`#10b981`): Represents Local Ollama execution, zero-cost compute, and passed tests.
  - Hyper Groq Violet (`#a855f7`): Represents high-throughput cloud reasoning and Groq LPU speed.
  - Solar Amber (`#f59e0b`): Represents live web research (Firecrawl, Jina, Tavily) and active thought accordions.
  - Crimson Warning (`#ef4444`): Represents 429 rate limits, network outages, and failover triggers.
- **Typography:**
  - Headings: `Geist Sans`, `Inter Display`, or `Cabinet Grotesk` (clean, geometric, futuristic).
  - Code & Command Prompts: `Geist Mono`, `JetBrains Mono`, or `Fira Code` with optical ligatures enabled.

### 1.3 Target Performance & Core Web Vitals (CWV)
Because developers judge developer tools by web speed, the showcase must achieve near-perfect performance scores:
- **Largest Contentful Paint (LCP):** < 1.0s (Critical hero typography rendered instantly; 3D canvas progressive enhancement).
- **Cumulative Layout Shift (CLS):** 0.00 (Pre-allocated canvas dimensions, aspect-ratio locked terminal frames).
- **Interaction to Next Paint (INP):** < 50ms (Compositor-only animations; 3D render loops decoupled from UI thread).
- **Page Payload:** < 180 KB initial HTML/CSS/JS (excluding 3D mesh assets loaded asynchronously).

---

## 2. The Centerpiece: The Animated Cybernetic Workhorse

A standout visual signature of the web interface is an **Actual Animated Cybernetic Workhorse** integrated directly into the hero experience.

```
+-----------------------------------------------------------------------------------------------------------------+
|                                         HERO INTERACTIVE STAGE                                                  |
+-----------------------------------------------------------------------------------------------------------------+
|                                                                                                                 |
|             +----------------------------------+        +-----------------------------------------------+       |
|             |        TYPOGRAPHIC HERO          |        |        THREE.JS / CANVAS 3D STAGE             |       |
|             |                                  |        |                                               |       |
|             |   THE TERMINAL AI WORKSTATION    |        |             _(\_/)                            |       |
|             |   THAT NEVER QUITS.              |        |           ,-"     "-.                         |       |
|             |                                  |        |          /  _     _  \     [CYBERNETIC HORSE] |       |
|             |   Local-First with Ollama.       |        |         /  (o)   (o)  \    - Glowing Core     |       |
|             |   5-Cycle Resilience Ring.       |        |        /      .-.      \   - Kinetic Trot     |       |
|             |   Active Repo Operator.          |        |       (      (   )      )  - Particle Trails  |       |
|             |                                  |        |        \      `-'      /   - Interactive      |       |
|             |   [ $ curl -fsSL get.wh | bash ] |        |         `-.__     __.-'                       |       |
|             |   [ View Architecture -> ]       |        |              `---'                            |       |
|             +----------------------------------+        +-----------------------------------------------+       |
|                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------+
| [|| Pause Motion]                 Scroll to Trot  |  Hover to Gallop  |  Click to Pulse Neural Core             |
+-----------------------------------------------------------------------------------------------------------------+
```

### 2.1 Visual Anatomy & Cybernetic Aesthetic
The Workhorse mascot is not a cartoon pony or generic stock graphic; it is an industrial, mechanical equine automaton built from faceted low-poly carbon fiber, exposed hydraulic pistons, and neon optical conduits:
1. **Chassis & Armor Plating:** Dark matte titanium (`#1a1f2c`) with bevelled geometric facets reflecting ambient rim lighting.
2. **The 5-Cycle Neural Core:** A faceted crystal chamber inside the horse's chest that visibly pulses and shifts colors as the user interacts:
   - Green pulse: Local Ollama mode active.
   - Violet pulse: Groq LPU tier engaged.
   - Blue pulse: Nvidia NIM reasoning.
   - Amber pulse: Live web intelligence scraping.
3. **Mane & Tail:** Flowing strands of luminescent fiber-optic data cables emitting subtle cyan/violet energy particles.
4. **Hooves:** Kinetic shock-absorbing pistons that strike the virtual ground plane, emitting subtle glowing ripples on each stride.

### 2.2 Three.js / WebGL & Canvas 2D Hybrid Architecture
To ensure silky 60fps performance across all devices (including mobile smartphones and low-power laptops):
- **Desktop / High-End Devices (WebGL 2.0 / WebGPU):** Renders a lightweight low-poly 3D mesh (~14,000 polygons, compressed to < 85 KB via Draco/KTX2) with procedural bone kinematics and PBR materials.
- **Mobile / Low-Power Devices (Canvas 2D / Vector SVG Fallback):** Renders an orthographic vector silhouette animated via 2D skeletal transformation matrices, requiring near-zero GPU memory.
- **Zero Motion Overhead:** The render loop automatically throttles to 1fps or pauses entirely when the hero section scrolls out of the viewport using `IntersectionObserver`.

### 2.3 Interactive State Engine (Idle, Trot, Gallop, Rear, Glow)
The horse reacts dynamically to user behavior across the page:
1. **Idle Breathing (Default):** Subtle vertical chest displacement (sinusoidal period: 3.2s) with hydraulic piston compression and soft glowing core dissipation.
2. **Trot on Scroll (Velocity-Bound):** As the visitor scrolls down the page, the horse breaks into a rhythmic trot. The animation playback speed is mathematically linked to the scroll velocity via `window.scrollY` delta or CSS Scroll-Driven Timelines.
3. **Gallop on CTA Hover:** When the user hovers over the installation command (`curl -fsSL ... | bash`) or primary download button, the horse charges into a full gallop, head lowered, particle vapor streaming from its exhausts.
4. **Rear Up on Copy:** When the visitor clicks the **Copy Command** button, the horse rears up on its hind legs in triumph, releasing an electric energy shockwave across the hero panel.
5. **Cursor Gaze Tracking:** The horse's head and neck subtly articulate (yaw: ±25°, pitch: ±15°) to follow the visitor's cursor across the screen.

### 2.4 The Dynamic 5-Cycle Neural Core (Visualizing Model Cascades)
Surrounding the animated horse is an orbiting orbital ring representing the 5 models in the resilience chain:
```
           [Local Ollama]
                 |
     +-----------+-----------+
     |                       |
[OpenRouter]             [Groq LPU]
     |                       |
     +-----------+-----------+
                 |
        [Gemini] - [Nvidia]
```
Clicking any node in the orbital ring triggers an instantaneous electrical surge from that node into the horse's core, changing its neon emissive shader color and displaying a micro-tooltip explaining that tier's latency and token economics.

### 2.5 Full WCAG 2.2.2 & `prefers-reduced-motion` Compliance
In strict adherence to modern web standards and accessibility guidelines:
- **Visible Pause/Play Control:** A prominent button labeled `[|| Pause Animation]` is anchored adjacent to the horse canvas. Clicking it halts all skeletal motion, keeps the horse in a dignified static resting stance, and toggles the label to `[▶ Play Animation]` (without ambiguous `aria-pressed` states).
- **Reduced Motion Detection:** When `@media (prefers-reduced-motion: reduce)` is detected:
  - All automated continuous skeletal trotting, galloping, and head tracking are disabled.
  - The horse is rendered in a static hero pose.
  - Lighting effects transition smoothly with gentle opacity shifts rather than kinetic motion.
- **No Rapid Flashing:** All glow pulses are clamped to frequencies strictly below 1.5 Hz, satisfying WCAG 2.3.1 (Three Flashes or Below Threshold).

---

## 3. Information Architecture & Route Hierarchy

```
                                      WORKHORSE WEB PORTAL
                                                |
        +---------------+---------------+-------+-------+---------------+---------------+
        |               |               |               |               |               |
        v               v               v               v               v               v
     / (Home)       /install      /architecture       /docs        /benchmarks      /skills-mcp
  - Hero & Horse  - 1-line curl  - 5-Cycle Ring   - Keybindings   - Latency vs     - Cross-Agent
  - TUI Replayer  - PowerShell   - Local vs Cloud - CLI Flags       Claude/Cursor    Skills Library
  - Core Tenets   - PATH Guide   - Web Cascade    - Config & Env  - Offline Test   - MCP Catalog
```

### 3.1 Route Map & Specifications

#### 1. Home Page (`/`)
- **Hero Stage:** Headline, value proposition, animated cybernetic horse, and quick-install copy button.
- **The Core Tenets Grid:** 4 cards explaining:
  1. *Tri-Alias Ubiquity:* `workhorse`, `workhouse`, `wh` anywhere on your machine.
  2. *Active Working Repo Operator:* No sandboxes. Real in-place modifications to code and READMEs.
  3. *5-Cycle Resilience Ring:* Zero premature failures across 5 model retry circles.
  4. *Live Thought Accordions:* No opaque spinners; complete transparency into reasoning.
- **Interactive Terminal Simulator:** Live replay of an actual session in `~/Desktop/promptdock`.
- **The Resilience Ring Exploder:** Radial interactive visualizer showing real-time 429 failover to Nvidia NIM and offline Ollama degradation.
- **Feature Comparison Matrix:** Workhorse vs Cursor vs Claude Code vs Generic CLI wrappers.

#### 2. Universal Installation Hub (`/install`)
- **OS Selector Tabs:** Linux (Ubuntu/Debian/Arch/Fedora), macOS (Homebrew / POSIX), Windows (PowerShell).
- **One-Line Copy Script:**
  ```bash
  curl -fsSL https://get.workhorse.sh | bash
  ```
- **Prerequisites Inspector:** Browser-based diagnostic checking if Python 3.10+ and Git are installed.
- **PATH Troubleshooting Guide:** Visual step-by-step for adding `~/.local/bin` to `~/.bashrc`, `~/.zshrc`, or `~/.config/fish/config.fish`.
- **Manual Git Installation Option:**
  ```bash
  git clone https://github.com/japheth/workhorse.git ~/.local/share/workhorse
  cd ~/.local/share/workhorse && ./install.sh
  ```

#### 3. Interactive Architecture Exploder (`/architecture`)
- **Scrollytelling Experience:** User scrolls through 5 distinct interactive layers:
  1. *Layer 1: Context Anchoring ($PWD)* — Demonstrating how `wh` captures the caller directory.
  2. *Layer 2: Local Ollama Discovery* — Auto-probing `localhost:11434` for 1B/4B models.
  3. *Layer 3: Cloud LPU Cluster* — Handing over to Groq and Nvidia NIM.
  4. *Layer 4: Multi-Engine Web Cascade* — Tavily -> Jina AI -> Firecrawl -> You.com.
  5. *Layer 5: Safe Atomic File Engine* — Chunked mutations and `.workhorse_backups/`.

#### 4. Documentation & Keybinding Reference (`/docs`)
- **Interactive TUI Keybinding Map:** Visual keyboard with interactive tooltips for `F1` (Help), `F2` (Mode), `F3` (Web), `F4` (Models), `F5` (Clear), `F6` (Skills & MCP Hub), `Ctrl+B` (Sidebar), and `Ctrl+Q` (Quit).
- **CLI Flag Index:** Complete documentation of `-m`, `-w`, `-f`, `-c` (CRUD), `--models`, `--tui`.
- **Environment Variables Reference:** Searchable table of all 25+ `.env` variables with demo placeholders.

#### 5. Cross-Agent Skills & Universal MCP Hub (`/skills-mcp`)
- **Skills Borrowing Directory:** Interactive visual library showing how skills from `.claude/skills/`, `.gemini/antigravity/skills/`, and `.cursor/skills/` are auto-harvested by Workhorse.
- **MCP Server Showcase:** Pre-built configurations for connecting PostgreSQL, GitHub, Filesystem, and Brave Search MCP servers.

---

## 4. Modern Web Motion & Animation System

Adhering strictly to modern web standards, Workhorse avoids heavy, outdated animation libraries like GSAP or bloated jQuery plugins. All motion is authored using native browser primitives.

### 4.1 Scroll-Driven Animations (`animation-timeline: view()`)
Page elements reveal and transform naturally as they enter the scrollport without triggering JavaScript scroll events:

```css
@media (prefers-reduced-motion: no-preference) {
  @supports ((animation-timeline: view()) and (animation-range: entry)) {
    @keyframes feature-reveal {
      entry 0% {
        opacity: 0;
        transform: translateY(40px) scale(0.96);
      }
      entry 100% {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }

    .scroll-reveal-card {
      animation: feature-reveal auto linear both;
      animation-timeline: view();
      animation-range: entry 10% entry 90%;
    }
  }
}
```

### 4.2 Scrollytelling: "The Journey of a Prompt"
In the `/architecture` route, a sticky terminal pane remains pinned on the left side of the screen while informative story cards scroll on the right. 
- As card 1 enters: The simulated terminal executes `wh` and shows context anchoring.
- As card 2 enters: The terminal shows local Ollama model auto-discovery.
- As card 3 enters: Groq LPU auto-handover streams tokens into a `ThoughtAccordion`.
- As card 4 enters: In-place file modification modifies `README.md` in real time.

### 4.3 View Transitions API (`document.startViewTransition()`)
When navigating between `/`, `/install`, and `/docs`:
- The header and animated horse seamlessly morph across routes.
- Code blocks smoothly resize to match the incoming page layout.
- Implementation:
  ```javascript
  function navigateWithTransition(targetUrl) {
    if (!document.startViewTransition) {
      window.location.href = targetUrl;
      return;
    }
    document.startViewTransition(async () => {
      const response = await fetch(targetUrl);
      const text = await response.text();
      const parser = new DOMParser();
      const newDoc = parser.parseFromString(text, 'text/html');
      document.body.innerHTML = newDoc.body.innerHTML;
      document.title = newDoc.title;
    });
  }
  ```

---

## 5. Component Design System & UI Specifications

### 5.1 Glassmorphic Global Header
```
+-----------------------------------------------------------------------------------------------------------------+
| [W] WORKHORSE  |  Overview  Architecture  Docs  Skills & MCP  Benchmarks  |  [ v3.1.0 ]  [ Install wh ] [GitHub]|
+-----------------------------------------------------------------------------------------------------------------+
```
- **Height:** 64px, fixed top with `backdrop-filter: blur(16px)` and `background: rgba(7, 10, 17, 0.8)`.
- **Brand Mark:** Stylized low-poly equine monogram with glowing cyan rim lighting.
- **Install CTA Pill:** High-contrast button with subtle radial gradient pulse on hover.

### 5.2 The Interactive Terminal Window Simulator (`<TerminalSimulator />`)
An authentic replication of the Workhorse Textual TUI rendered directly in CSS and React/Astro:
- Top status bar: `WORKHORSE WORKSTATION | auto:auto | [OLLAMA: UP] | [WEB: OFF] | promptdock`
- Split layout: Left sidebar directory tree with interactive file items (`README.md`, `package.json`, `src/`).
- Center conversation log: Animated typewriter playback showing the prompt `tell me about this repo and edit readme, make it more detailed`.
- Expandable `ThoughtAccordion`: Visitors can click the yellow `▼ Reasoning & Chunk Progress` disclosure box to toggle thought details on and off.

### 5.3 One-Click Tri-Alias Installation Bar (`<InstallCommand />`)
A high-visibility input banner featuring shell tabs (`curl`, `pnpm`, `brew`, `powershell`):
- Displays: `curl -fsSL https://get.workhorse.sh | bash`
- Right side: Magnetic **Copy** button with clipboard feedback and a particle burst animation.
- Sub-label: `Universal Tri-Alias: Automatically symlinks 'workhorse', 'workhouse', and 'wh' into ~/.local/bin`.

---

## 6. Complete Production Frontend Implementation Code

The following production code files form the foundation of the Workhorse web experience.

### 6.1 `src/components/AnimatedHorse.tsx` (Three.js / WebGL Cybernetic Mascot)
```tsx
import React, { useEffect, useRef, useState } from 'react';
import * as THREE from 'three';

interface HorseProps {
  interactive?: boolean;
}

export const AnimatedHorse: React.FC<HorseProps> = ({ interactive = true }) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [isPlaying, setIsPlaying] = useState<boolean>(true);
  const [reducedMotion, setReducedMotion] = useState<boolean>(false);
  const sceneRef = useRef<{
    renderer: THREE.WebGLRenderer;
    scene: THREE.Scene;
    camera: THREE.PerspectiveCamera;
    horseGroup: THREE.Group;
    coreLight: THREE.PointLight;
    clock: THREE.Clock;
    animFrameId: number;
  } | null>(null);

  useEffect(() => {
    // Check user reduced motion preference
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setReducedMotion(mediaQuery.matches);

    const handleMotionChange = (e: MediaQueryListEvent) => {
      setReducedMotion(e.matches);
      if (e.matches) setIsPlaying(false);
    };
    mediaQuery.addEventListener('change', handleMotionChange);

    if (!containerRef.current) return;

    // 1. Scene & Camera Initialization
    const width = containerRef.current.clientWidth;
    const height = containerRef.current.clientHeight || 480;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
    camera.position.set(0, 1.5, 5);

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    containerRef.current.appendChild(renderer.domElement);

    // 2. Lighting Setup
    const ambientLight = new THREE.AmbientLight(0x0f172a, 2.5);
    scene.add(ambientLight);

    const rimLight = new THREE.DirectionalLight(0x38bdf8, 4.0);
    rimLight.position.set(5, 5, -2);
    scene.add(rimLight);

    const fillLight = new THREE.DirectionalLight(0xa855f7, 2.0);
    fillLight.position.set(-4, 2, 3);
    scene.add(fillLight);

    // 3. Cybernetic Horse Group (Procedural Low-Poly Geometric Rig)
    const horseGroup = new THREE.Group();

    // Material definitions
    const titaniumMaterial = new THREE.MeshStandardMaterial({
      color: 0x111827,
      metalness: 0.85,
      roughness: 0.25,
      flatShading: true,
    });

    const neonChassisMaterial = new THREE.MeshStandardMaterial({
      color: 0x1e293b,
      metalness: 0.9,
      roughness: 0.1,
      flatShading: true,
    });

    // Horse Torso (Faceted Low-Poly Body)
    const bodyGeo = new THREE.BoxGeometry(0.9, 0.8, 1.8, 2, 2, 3);
    const bodyMesh = new THREE.Mesh(bodyGeo, titaniumMaterial);
    bodyMesh.position.y = 1.2;
    horseGroup.add(bodyMesh);

    // Neck & Head
    const neckGeo = new THREE.CylinderGeometry(0.22, 0.35, 1.0, 5);
    const neckMesh = new THREE.Mesh(neckGeo, titaniumMaterial);
    neckMesh.position.set(0, 1.8, 0.7);
    neckMesh.rotation.x = Math.PI / 4;
    horseGroup.add(neckMesh);

    const headGeo = new THREE.BoxGeometry(0.35, 0.4, 0.7, 2, 2, 2);
    const headMesh = new THREE.Mesh(headGeo, neonChassisMaterial);
    headMesh.position.set(0, 2.2, 1.1);
    horseGroup.add(headMesh);

    // 5-Cycle Neural Core (Pulsing Glowing Crystal)
    const coreGeo = new THREE.OctahedronGeometry(0.22, 0);
    const coreMat = new THREE.MeshStandardMaterial({
      color: 0x10b981,
      emissive: 0x10b981,
      emissiveIntensity: 2.5,
      wireframe: true,
    });
    const coreMesh = new THREE.Mesh(coreGeo, coreMat);
    coreMesh.position.set(0, 1.2, 0.3);
    horseGroup.add(coreMesh);

    const coreLight = new THREE.PointLight(0x10b981, 3.0, 4);
    coreLight.position.copy(coreMesh.position);
    horseGroup.add(coreLight);

    // Four Articulated Legs
    const legGeo = new THREE.CylinderGeometry(0.08, 0.06, 1.1, 4);
    const legPositions = [
      [-0.4, 0.55, 0.6],  // Front Left
      [0.4, 0.55, 0.6],   // Front Right
      [-0.4, 0.55, -0.6], // Back Left
      [0.4, 0.55, -0.6],  // Back Right
    ];

    const legs: THREE.Mesh[] = [];
    legPositions.forEach((pos) => {
      const leg = new THREE.Mesh(legGeo, titaniumMaterial);
      leg.position.set(pos[0], pos[1], pos[2]);
      horseGroup.add(leg);
      legs.push(leg);
    });

    scene.add(horseGroup);
    camera.lookAt(0, 1.2, 0);

    const clock = new THREE.Clock();

    // 4. Render & Animation Loop
    const animate = () => {
      const animFrameId = requestAnimationFrame(animate);
      const elapsedTime = clock.getElapsedTime();

      if (isPlaying && !reducedMotion) {
        // Idle breathing & dynamic gait
        const breathe = Math.sin(elapsedTime * 2.0) * 0.05;
        bodyMesh.position.y = 1.2 + breathe;
        coreMesh.rotation.y = elapsedTime * 1.5;
        coreMesh.rotation.z = elapsedTime * 0.8;

        // Subtle leg kinetics (Trot simulation)
        legs[0].rotation.x = Math.sin(elapsedTime * 3.5) * 0.3;
        legs[1].rotation.x = -Math.sin(elapsedTime * 3.5) * 0.3;
        legs[2].rotation.x = -Math.sin(elapsedTime * 3.5) * 0.3;
        legs[3].rotation.x = Math.sin(elapsedTime * 3.5) * 0.3;

        // Subtle horizontal rotation
        horseGroup.rotation.y = Math.sin(elapsedTime * 0.5) * 0.15 - 0.2;
      }

      renderer.render(scene, camera);
      if (sceneRef.current) {
        sceneRef.current.animFrameId = animFrameId;
      }
    };

    sceneRef.current = { renderer, scene, camera, horseGroup, coreLight, clock, animFrameId: 0 };
    animate();

    // Resize handler
    const handleResize = () => {
      if (!containerRef.current || !sceneRef.current) return;
      const newWidth = containerRef.current.clientWidth;
      const newHeight = containerRef.current.clientHeight || 480;
      sceneRef.current.camera.aspect = newWidth / newHeight;
      sceneRef.current.camera.updateProjectionMatrix();
      sceneRef.current.renderer.setSize(newWidth, newHeight);
    };
    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      mediaQuery.removeEventListener('change', handleMotionChange);
      if (sceneRef.current) {
        cancelAnimationFrame(sceneRef.current.animFrameId);
        renderer.dispose();
      }
      if (containerRef.current) {
        containerRef.current.innerHTML = '';
      }
    };
  }, [isPlaying, reducedMotion]);

  // Pause / Play toggle for WCAG 2.2.2 compliance
  const togglePlay = () => {
    setIsPlaying((prev) => !prev);
  };

  return (
    <div className="relative w-full h-[480px] flex items-center justify-center">
      <div ref={containerRef} className="w-full h-full cursor-grab active:cursor-grabbing" />
      
      {/* Accessible Pause/Play Control (WCAG 2.2.2 Pause, Stop, Hide) */}
      <button
        onClick={togglePlay}
        className="absolute bottom-4 left-4 z-20 px-3 py-1.5 text-xs font-mono font-medium tracking-wider uppercase bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-700/60 rounded-md backdrop-blur-md transition-colors"
      >
        {isPlaying ? '⏸ Pause Mascot' : '▶ Play Mascot'}
      </button>

      {/* Interactive Neural Core Badge */}
      <div className="absolute top-4 right-4 z-20 px-3 py-1.5 text-xs font-mono bg-emerald-950/60 border border-emerald-500/40 rounded-full text-emerald-300 flex items-center gap-2 backdrop-blur-md">
        <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
        5-Cycle Neural Core: Active
      </div>
    </div>
  );
};
```

### 6.2 `src/components/TerminalSimulator.tsx` (Interactive TUI Replay)
```tsx
import React, { useState } from 'react';

export const TerminalSimulator: React.FC = () => {
  const [accordionOpen, setAccordionOpen] = useState<boolean>(true);

  return (
    <div className="w-full max-w-4xl mx-auto rounded-xl overflow-hidden border border-slate-800 bg-[#0d1117] shadow-2xl font-mono text-sm">
      {/* Top Header Bar */}
      <div className="bg-[#161b22] px-4 py-2.5 border-b border-slate-800 flex items-center justify-between text-xs text-slate-400">
        <div className="flex items-center gap-2">
          <span className="w-3 h-3 rounded-full bg-red-500/80 inline-block" />
          <span className="w-3 h-3 rounded-full bg-yellow-500/80 inline-block" />
          <span className="w-3 h-3 rounded-full bg-green-500/80 inline-block" />
          <span className="ml-2 font-bold text-sky-400">WORKHORSE WORKSTATION</span>
        </div>
        <div className="flex items-center gap-3 text-[11px]">
          <span className="bg-sky-950/80 text-sky-300 px-2 py-0.5 rounded border border-sky-800/60">MODE: auto:auto</span>
          <span className="bg-emerald-950/80 text-emerald-300 px-2 py-0.5 rounded border border-emerald-800/60">OLLAMA: UP</span>
          <span className="text-slate-500">~/Desktop/promptdock</span>
        </div>
      </div>

      {/* Main Split Layout */}
      <div className="grid grid-cols-1 md:grid-cols-12 min-h-[380px]">
        {/* Left Sidebar: Workspace Explorer */}
        <div className="md:col-span-4 border-r border-slate-800/80 p-3 bg-[#0a0e14] text-xs">
          <div className="text-slate-400 font-bold mb-2 flex items-center justify-between">
            <span>📂 WORKSPACE</span>
            <div className="flex gap-1 text-[10px]">
              <span className="bg-blue-600 px-1.5 py-0.5 rounded text-white">New</span>
              <span className="bg-slate-700 px-1.5 py-0.5 rounded text-slate-200">Edit</span>
            </div>
          </div>
          <div className="space-y-1 text-slate-400">
            <div className="text-sky-300">v promptdock/</div>
            <div className="pl-3 text-slate-400">📁 src/</div>
            <div className="pl-6 text-slate-500">📄 index.ts</div>
            <div className="pl-6 text-slate-500">📄 routes.ts</div>
            <div className="pl-3 text-emerald-400 font-medium">📄 README.md (Modified)</div>
            <div className="pl-3 text-slate-500">⚙️ package.json</div>
            <div className="pl-3 text-slate-500">⚙️ tsconfig.json</div>
          </div>
        </div>

        {/* Center Main: Conversation Stream */}
        <div className="md:col-span-8 p-4 flex flex-col justify-between bg-[#0d1117]">
          <div className="space-y-4">
            {/* User Message */}
            <div className="bg-[#1f2937]/50 border-l-2 border-sky-400 p-2.5 rounded-r text-slate-200">
              <span className="text-sky-400 font-bold text-xs block mb-1">User</span>
              tell me about this repo and edit readme, make it more detailed
            </div>

            {/* Live Streaming ThoughtAccordion */}
            <div className="border border-yellow-500/40 bg-yellow-950/10 rounded overflow-hidden">
              <button
                onClick={() => setAccordionOpen(!accordionOpen)}
                className="w-full text-left px-3 py-1.5 bg-yellow-500/10 text-yellow-400 font-bold text-xs flex items-center justify-between hover:bg-yellow-500/20 transition-colors"
              >
                <span>{accordionOpen ? '▼' : '▶'} Reasoning & Chunk Progress (4 steps)</span>
                <span className="text-[10px] text-yellow-500/70 font-normal">Click to toggle</span>
              </button>
              
              {accordionOpen && (
                <div className="p-3 text-xs text-yellow-200/90 space-y-1 font-mono border-t border-yellow-500/20 bg-[#0a0d13]">
                  <div>[*] Scanning repository structure in ~/Desktop/promptdock...</div>
                  <div>[*] Ingested chunk 1/1: package.json (Detected Express & TypeScript)</div>
                  <div>[*] auto:auto Dispatcher: Promoted to [GROQ: openai/gpt-oss-120b]</div>
                  <div className="text-emerald-400">[OK] In-place write complete: README.md updated (148 lines).</div>
                </div>
              )}
            </div>

            {/* Agent Completion Card */}
            <div className="bg-[#131b26] border-l-2 border-emerald-400 p-2.5 rounded-r text-slate-300 text-xs">
              <span className="text-emerald-400 font-bold block mb-1">Agent (GROQ | gpt-oss-120b)</span>
              I analyzed <strong>promptdock</strong> and expanded `README.md` in place with detailed setup instructions, architecture breakdown, and REST API documentation.
            </div>
          </div>

          {/* Bottom Simulated Input */}
          <div className="mt-4 pt-2 border-t border-slate-800 flex items-center text-xs text-slate-400">
            <span className="text-sky-400 mr-2 font-bold">&gt;</span>
            <span className="text-slate-500">Ask Workhorse or edit files... (Enter to send)</span>
          </div>
        </div>
      </div>
    </div>
  );
};
```

### 6.3 `src/components/InstallBar.tsx` (One-Line Clipboard Command)
```tsx
import React, { useState } from 'react';

export const InstallBar: React.FC = () => {
  const [copied, setCopied] = useState(false);
  const command = 'curl -fsSL https://get.workhorse.sh | bash';

  const handleCopy = () => {
    navigator.clipboard.writeText(command);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  };

  return (
    <div className="flex flex-col items-center gap-2 max-w-xl mx-auto w-full">
      <div className="w-full flex items-center justify-between bg-slate-900/90 border border-slate-700/80 rounded-xl p-2 pl-4 backdrop-blur-xl shadow-2xl">
        <div className="flex items-center gap-2 font-mono text-sm text-sky-300 overflow-x-auto select-all">
          <span className="text-slate-500 select-none">$</span>
          <span>{command}</span>
        </div>
        <button
          onClick={handleCopy}
          className={`px-4 py-2 rounded-lg font-mono text-xs font-semibold uppercase tracking-wider transition-all duration-200 ${
            copied
              ? 'bg-emerald-500 text-slate-950 font-bold scale-105'
              : 'bg-sky-500 hover:bg-sky-400 text-slate-950 hover:shadow-lg hover:shadow-sky-500/25'
          }`}
        >
          {copied ? '✓ Copied' : 'Copy'}
        </button>
      </div>
      <p className="text-xs text-slate-400 font-mono">
        Universal Tri-Alias: Automatically installs <code className="text-sky-300">workhorse</code>, <code className="text-sky-300">workhouse</code>, and <code className="text-sky-300">wh</code> into <code className="text-slate-300">~/.local/bin</code>.
      </p>
    </div>
  );
};
```

### 6.4 `src/styles/motion.css` (Native Scroll-Driven Animations)
```css
/* =============================================================================
   Workhorse Native Modern Web Motion & Animation System
   ============================================================================= */

/* 1. Hardware-Accelerated Compositor Transitions */
.card-hover-fx {
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1),
              border-color 0.25s ease,
              box-shadow 0.25s ease;
  will-change: transform;
}

.card-hover-fx:hover {
  transform: translateY(-4px) scale(1.01);
  border-color: rgba(56, 189, 248, 0.4);
  box-shadow: 0 12px 30px -10px rgba(56, 189, 248, 0.15);
}

/* 2. Scroll-Driven Element Entry & Exit Animations */
@media (prefers-reduced-motion: no-preference) {
  @supports ((animation-timeline: view()) and (animation-range: entry)) {
    @keyframes section-fade-in {
      entry 0% {
        opacity: 0;
        transform: translateY(30px);
      }
      entry 100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .scroll-entry-reveal {
      animation: section-fade-in auto cubic-bezier(0.16, 1, 0.3, 1) both;
      animation-timeline: view();
      animation-range: entry 10% entry 70%;
    }

    /* Scroll progress bar anchored to page scroll */
    @keyframes scroll-progress-fill {
      from { transform: scaleX(0); }
      to { transform: scaleX(1); }
    }

    .scroll-progress-bar {
      transform-origin: 0 50%;
      animation: scroll-progress-fill auto linear both;
      animation-timeline: scroll();
    }
  }
}

/* 3. Reduced Motion Safety Overrides (WCAG Compliance) */
@media (prefers-reduced-motion: reduce) {
  .scroll-entry-reveal,
  .card-hover-fx {
    animation: none !important;
    transform: none !important;
    transition: opacity 0.2s ease !important;
  }
}
```

---

## 7. SEO, Social Graph & Metadata Strategy

### 7.1 Dynamic OpenGraph (OG) Generator
Every route generates an automated high-resolution OpenGraph card (1200x630px):
- Background: Obsidian gradient (`#070a11` -> `#0f172a`).
- Foreground: Rendered 3D Cybernetic Workhorse with glowing neon emerald core.
- Title: `Workhorse | Universal Hybrid AI Terminal Workstation`
- Subtitle: `Local-First with Ollama. 5-Cycle Resilience Ring. Real Repo Operator.`

### 7.2 Structured Data (JSON-LD)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Workhorse",
  "operatingSystem": "Linux, macOS, Windows",
  "applicationCategory": "DeveloperApplication",
  "offers": {
    "@type": "Offer",
    "price": "0.00",
    "priceCurrency": "USD"
  },
  "description": "Enterprise-grade local-first hybrid terminal workstation and autonomous agent runtime with 5-Cycle resilience ring and full workspace file CRUD.",
  "softwareVersion": "3.1.0"
}
</script>
```

---

## 8. Accessibility & Progressive Enhancement

### 8.1 Motion Controls (WCAG 2.2.2 Pause, Stop, Hide)
Any automated movement (such as the 3D horse rotation or particle systems) includes a visible `<button>` control enabling users to freeze motion immediately.

### 8.2 Baseline Compatibility Strategy
- **Baseline Widely Available:** CSS Grid, Flexbox, custom properties, `localStorage`, `IntersectionObserver`. Safe without polyfills.
- **Progressive Enhancement:** CSS Scroll-Driven Animations and the View Transitions API enhance modern browsers (Chrome/Edge 115+, Safari 18+), while gracefully falling back to standard static positioning on legacy browsers.

---

## 9. Build, Deployment & Static Edge Hosting

### 9.1 Edge Hosting Runbook (Cloudflare Pages / Vercel)
```bash
# 1. Build optimized static output
pnpm build

# 2. Deploy to Cloudflare Pages
npx wrangler pages deploy dist/ --project-name=workhorse-web

# 3. Verify Edge Cache Headers
curl -I https://workhorse.sh
# Expected: cf-cache-status: HIT, cache-control: public, max-age=31536000, immutable
```

---
*End of WEB.md — Workhorse Universal Web Showcase Specification 1.0.0-PRO*


---

## 10. Complete Component Implementations for the Web App

The following subsections provide the full production implementations for the key interactive components, visualizers, and pages of the Workhorse showcase site.

### 10.1 `src/components/ResilienceRingVisualizer.tsx` (Interactive 5-Cycle Ring)
```tsx
import React, { useState } from 'react';

interface ProviderNode {
  id: string;
  name: string;
  category: 'local' | 'cloud' | 'gateway';
  model: string;
  latency: string;
  cost: string;
  color: string;
  description: string;
}

const PROVIDERS: ProviderNode[] = [
  {
    id: 'ollama',
    name: 'Local Ollama',
    category: 'local',
    model: 'llama3.2:1b / deepseek-v4.1',
    latency: 'Sub-80ms TTFT',
    cost: '$0.00 (Zero Cloud Cost)',
    color: '#10b981', // Emerald
    description: 'Runs directly on local GPU/CPU. Handles micro-tasks, parsing, and offline fallback.'
  },
  {
    id: 'groq',
    name: 'Groq Cloud LPU',
    category: 'cloud',
    model: 'openai/gpt-oss-120b',
    latency: '450 tokens/sec',
    cost: 'Ultra-low cost LPU',
    color: '#a855f7', // Violet
    description: 'High-speed reasoning and deep code generation. Primary cloud tier for active development.'
  },
  {
    id: 'nvidia',
    name: 'Nvidia NIM',
    category: 'cloud',
    model: 'nemotron-3.5-super-vl-120b',
    latency: 'High Reasoning',
    cost: 'Enterprise Cloud',
    color: '#38bdf8', // Cyan
    description: 'Massive parameter reasoning, code graph analysis, and vision decompilation.'
  },
  {
    id: 'gemini',
    name: 'Google Gemini',
    category: 'cloud',
    model: 'gemini-2.5-flash',
    latency: '2M Token Window',
    cost: 'High Efficiency',
    color: '#f59e0b', // Amber
    description: 'Multi-file audits, complete repo ingestion, and multimodal image analysis.'
  },
  {
    id: 'openrouter',
    name: 'OpenRouter Gateway',
    category: 'gateway',
    model: 'z-ai/glm-5.3-prime',
    latency: 'High Resilience',
    cost: 'Dynamic Routing',
    color: '#ec4899', // Pink
    description: 'Universal failover gateway ensuring 100% operational uptime if vendor APIs drop.'
  }
];

export const ResilienceRingVisualizer: React.FC = () => {
  const [activeNode, setActiveNode] = useState<ProviderNode>(PROVIDERS[0]);
  const [isSimulatingFailover, setIsSimulatingFailover] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);

  const simulateFailover = () => {
    if (isSimulatingFailover) return;
    setIsSimulatingFailover(true);
    setCurrentStep(0);

    const interval = setInterval(() => {
      setCurrentStep((prev) => {
        const next = prev + 1;
        if (next >= PROVIDERS.length) {
          clearInterval(interval);
          setIsSimulatingFailover(false);
          return 0;
        }
        setActiveNode(PROVIDERS[next]);
        return next;
      });
    }, 1200);
  };

  return (
    <div className="w-full max-w-5xl mx-auto p-6 rounded-2xl bg-slate-950/70 border border-slate-800 backdrop-blur-xl shadow-2xl font-mono">
      <div className="flex flex-col md:flex-row items-center justify-between gap-6 mb-8">
        <div>
          <h3 className="text-xl font-bold text-white tracking-tight flex items-center gap-2">
            <span className="w-3 h-3 rounded-full bg-emerald-400 animate-ping" />
            The 5-Cycle Infinite Resilience Ring
          </h3>
          <p className="text-xs text-slate-400 mt-1">
            Workhorse traverses this circular ring up to 5 full times before declaring a failure.
          </p>
        </div>
        <button
          onClick={simulateFailover}
          disabled={isSimulatingFailover}
          className="px-4 py-2 rounded-lg text-xs font-bold uppercase tracking-wider bg-sky-500 hover:bg-sky-400 text-slate-950 transition-all disabled:opacity-50"
        >
          {isSimulatingFailover ? `Simulating Handover (Step ${currentStep + 1}/5)...` : '▶ Simulate 429 Failover'}
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        {/* SVG Orbital Circle */}
        <div className="lg:col-span-7 flex justify-center relative">
          <svg className="w-72 h-72 md:w-96 md:h-96" viewBox="0 0 400 400">
            {/* Background Orbital Track */}
            <circle cx="200" cy="200" r="140" fill="none" stroke="rgba(255,255,255,0.08)" strokeWidth="2" strokeDasharray="6 6" />

            {/* Glowing Active Ring Track */}
            <circle
              cx="200"
              cy="200"
              r="140"
              fill="none"
              stroke={activeNode.color}
              strokeWidth="4"
              className="transition-all duration-700 opacity-60"
            />

            {/* Central Mascot Hologram */}
            <circle cx="200" cy="200" r="48" fill="#0d1117" stroke={activeNode.color} strokeWidth="2" />
            <text x="200" y="196" textAnchor="middle" fill="#fff" fontSize="11" fontWeight="bold">WORKHORSE</text>
            <text x="200" y="214" textAnchor="middle" fill={activeNode.color} fontSize="9">auto:auto</text>

            {/* 5 Orbital Nodes */}
            {PROVIDERS.map((node, index) => {
              const angle = (index * (360 / PROVIDERS.length) - 90) * (Math.PI / 180);
              const x = 200 + 140 * Math.cos(angle);
              const y = 200 + 140 * Math.sin(angle);
              const isSelected = activeNode.id === node.id;

              return (
                <g
                  key={node.id}
                  className="cursor-pointer transition-transform duration-300 hover:scale-110"
                  onClick={() => setActiveNode(node)}
                >
                  <circle
                    cx={x}
                    cy={y}
                    r={isSelected ? 26 : 20}
                    fill="#0f172a"
                    stroke={isSelected ? node.color : 'rgba(255,255,255,0.2)'}
                    strokeWidth={isSelected ? 3 : 1.5}
                  />
                  {isSelected && (
                    <circle cx={x} cy={y} r="32" fill="none" stroke={node.color} strokeWidth="1" opacity="0.4" className="animate-pulse" />
                  )}
                  <text x={x} y={y + 3} textAnchor="middle" fill={isSelected ? '#fff' : 'rgba(255,255,255,0.6)'} fontSize="9" fontWeight="bold">
                    {index + 1}
                  </text>
                </g>
              );
            })}
          </svg>
        </div>

        {/* Selected Tier Inspector Card */}
        <div className="lg:col-span-5 bg-slate-900/90 border border-slate-700/60 p-5 rounded-xl text-xs space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <span className="text-[10px] uppercase font-bold tracking-wider text-slate-400 block">Tier Inspection</span>
              <h4 className="text-base font-bold text-white" style={{ color: activeNode.color }}>
                {activeNode.name}
              </h4>
            </div>
            <span className="px-2 py-0.5 rounded text-[10px] uppercase font-bold bg-slate-800 text-slate-300 border border-slate-700">
              {activeNode.category}
            </span>
          </div>

          <div className="space-y-2 text-slate-300">
            <div>
              <span className="text-slate-500 block text-[10px] uppercase">Default Model:</span>
              <span className="text-sky-300 font-bold">{activeNode.model}</span>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <div>
                <span className="text-slate-500 block text-[10px] uppercase">Latency Profile:</span>
                <span className="text-emerald-400">{activeNode.latency}</span>
              </div>
              <div>
                <span className="text-slate-500 block text-[10px] uppercase">Economics:</span>
                <span className="text-amber-400">{activeNode.cost}</span>
              </div>
            </div>
            <div>
              <span className="text-slate-500 block text-[10px] uppercase">Role in Resilience Ring:</span>
              <p className="text-slate-300 text-xs leading-relaxed mt-0.5">{activeNode.description}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
```

### 10.2 `src/components/SkillsMCPDirectory.tsx` (Cross-Agent Interop Showcase)
```tsx
import React, { useState } from 'react';

interface SkillItem {
  name: string;
  origin: 'Claude Code' | 'Antigravity' | 'Cursor' | 'Workhorse';
  description: string;
  category: 'Testing' | 'Database' | 'Refactoring' | 'DevOps';
}

const SAMPLE_SKILLS: SkillItem[] = [
  {
    name: 'playwright-e2e',
    origin: 'Antigravity',
    description: 'Automated headless browser end-to-end testing and visual snapshot comparisons.',
    category: 'Testing'
  },
  {
    name: 'git-squash-rebase',
    origin: 'Claude Code',
    description: 'Interactive branch history compression and conventional commit synthesis.',
    category: 'DevOps'
  },
  {
    name: 'sql-query-optimizer',
    origin: 'Cursor',
    description: 'Inspects query execution plans and generates composite B-tree index recommendations.',
    category: 'Database'
  },
  {
    name: 'fastapi-crud-scaffold',
    origin: 'Workhorse',
    description: 'Generates async SQLModel endpoints with Pydantic v2 validation and unit tests.',
    category: 'Refactoring'
  }
];

export const SkillsMCPDirectory: React.FC = () => {
  const [filter, setFilter] = useState<string>('All');

  const filteredSkills = filter === 'All'
    ? SAMPLE_SKILLS
    : SAMPLE_SKILLS.filter((s) => s.origin === filter || s.category === filter);

  return (
    <div className="w-full max-w-5xl mx-auto font-mono text-xs p-6 bg-slate-950/80 border border-slate-800 rounded-2xl backdrop-blur-xl">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
        <div>
          <h3 className="text-lg font-bold text-white flex items-center gap-2">
            <span>⚡</span> Universal Cross-Agent Skills & MCP Harvester
          </h3>
          <p className="text-slate-400 text-xs mt-0.5">
            Workhorse automatically discovers and executes skills from your Claude Code, Antigravity, and Cursor directories.
          </p>
        </div>
        <div className="flex gap-1.5 flex-wrap">
          {['All', 'Claude Code', 'Antigravity', 'Cursor'].map((cat) => (
            <button
              key={cat}
              onClick={() => setFilter(cat)}
              className={`px-2.5 py-1 rounded text-[11px] transition-colors ${
                filter === cat
                  ? 'bg-sky-500 text-slate-950 font-bold'
                  : 'bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filteredSkills.map((skill) => (
          <div
            key={skill.name}
            className="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80 hover:border-sky-500/40 transition-all card-hover-fx"
          >
            <div className="flex items-center justify-between mb-2">
              <span className="font-bold text-sky-300 text-sm">{skill.name}</span>
              <span className="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700/60">
                {skill.origin}
              </span>
            </div>
            <p className="text-slate-300 text-xs leading-relaxed">{skill.description}</p>
            <div className="mt-3 pt-2 border-t border-slate-800/60 flex items-center justify-between text-[10px] text-slate-500">
              <span>Category: {skill.category}</span>
              <span className="text-emerald-400">Ready to execute in wh</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
```

### 10.3 `src/components/ScrollyArchitecture.tsx` (Scrollytelling Deep Dive)
```tsx
import React, { useState } from 'react';

const STEPS = [
  {
    step: '01',
    title: 'Context Anchoring ($PWD)',
    description: 'When invoked anywhere on your machine via workhorse, workhouse, or wh, Workhorse dynamically captures the caller working directory. Dependencies resolve from the isolated .venv while operations anchor strictly to your current project.',
    code: 'export WORKHORSE_INVOCATION_CWD="$(pwd)"\nexec "$INSTALL_DIR/.venv/bin/python" "$MAIN_SCRIPT" "$@"'
  },
  {
    step: '02',
    title: 'Dynamic Local Ollama Auto-Discovery',
    description: 'On startup, Workhorse probes http://localhost:11434/api/tags without blocking. If llama3.2:1b, deepseek-v4.1, or qwen3-vl are present, they are harnessed for micro-tasks and offline fallback at zero token cost.',
    code: 'status = ollama.list()\n# Detected models: [llama3.2:1b, deepseek-v4.1-flash, qwen3-vl:4b]\n# Tier-0 Local Anchor: ONLINE'
  },
  {
    step: '03',
    title: '5-Cycle Resilience Ring & Cloud LPU',
    description: 'Complex reasoning tasks promote autonomously to Groq LPUs or Nvidia NIM. If rate limits occur, Workhorse traverses the circular model ring and repeats up to 5 full cycles before ever declaring a failure.',
    code: 'ring = [Local_Ollama -> Groq_LPU -> Nvidia_NIM -> Gemini_Flash -> OpenRouter]\n# Retries remaining: Cycle 2/5 (Zero fast-failures)'
  },
  {
    step: '04',
    title: 'Active Working Repo Operator (No Sandbox)',
    description: 'Workhorse is not isolated in a sandbox. It actively mutates files in place—reading large repositories in chunks and writing updates directly back to your project with automatic safety backups.',
    code: 'wh> tell me about this repo and edit readme, make it more detailed\n# Ingested README.md (lines 1-200)\n# Wrote in-place: README.md (Backup: .workhorse_backups/README.md.bak)'
  }
];

export const ScrollyArchitecture: React.FC = () => {
  const [activeStep, setActiveStep] = useState(0);

  return (
    <div className="w-full max-w-6xl mx-auto py-12 px-4 font-mono">
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* Sticky Code Panel */}
        <div className="lg:col-span-6 sticky top-24 rounded-xl overflow-hidden border border-slate-800 bg-[#0d1117] p-4 shadow-2xl">
          <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-800 text-xs text-slate-400">
            <span className="text-sky-400 font-bold">WORKHORSE INTERNAL KERNEL</span>
            <span className="text-emerald-400 font-bold">STEP {STEPS[activeStep].step} ACTIVE</span>
          </div>
          <pre className="text-xs text-sky-200 overflow-x-auto p-2 bg-[#090d14] rounded leading-relaxed">
            <code>{STEPS[activeStep].code}</code>
          </pre>
        </div>

        {/* Scrolling Narrative Steps */}
        <div className="lg:col-span-6 space-y-16 py-8">
          {STEPS.map((step, idx) => (
            <div
              key={step.step}
              onMouseEnter={() => setActiveStep(idx)}
              className={`p-6 rounded-xl border transition-all cursor-pointer ${
                activeStep === idx
                  ? 'bg-slate-900/90 border-sky-500/60 shadow-xl shadow-sky-500/10'
                  : 'bg-slate-950/40 border-slate-800/60 opacity-60 hover:opacity-100'
              }`}
            >
              <span className="text-sky-400 font-bold text-sm block mb-1">PHASE {step.step}</span>
              <h4 className="text-lg font-bold text-white mb-2">{step.title}</h4>
              <p className="text-slate-300 text-xs leading-relaxed">{step.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
```

---

## 11. Complete Web Project Scaffolding & Configuration

### 11.1 `package.json`
```json
{
  "name": "workhorse-showcase-web",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "astro dev",
    "build": "astro check && astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "@astrojs/react": "^4.2.0",
    "@astrojs/tailwind": "^5.1.0",
    "astro": "^5.0.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "three": "^0.170.0",
    "@types/three": "^0.170.0",
    "clsx": "^2.1.1",
    "tailwind-merge": "^2.5.4"
  },
  "devDependencies": {
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "tailwindcss": "^3.4.15",
    "typescript": "^5.6.3"
  }
}
```

### 11.2 `astro.config.mjs`
```javascript
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [
    react(),
    tailwind({
      applyBaseStyles: false,
    }),
  ],
  output: 'static',
  build: {
    format: 'file',
    inlineStylesheets: 'auto',
  },
});
```

### 11.3 `tailwind.config.mjs`
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        obsidian: '#070a11',
        panel: '#0d1117',
        cyber: {
          cyan: '#38bdf8',
          mint: '#10b981',
          violet: '#a855f7',
          amber: '#f59e0b',
        },
      },
      fontFamily: {
        mono: ['Geist Mono', 'JetBrains Mono', 'Fira Code', 'monospace'],
        sans: ['Geist Sans', 'Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
```

---

## 12. Complete Page Implementations

### 12.1 `src/pages/index.astro` (Main Landing Showcase)
```astro
---
import Layout from '../layouts/Layout.astro';
import { AnimatedHorse } from '../components/AnimatedHorse';
import { TerminalSimulator } from '../components/TerminalSimulator';
import { InstallBar } from '../components/InstallBar';
import { ResilienceRingVisualizer } from '../components/ResilienceRingVisualizer';
import { SkillsMCPDirectory } from '../components/SkillsMCPDirectory';
import { ScrollyArchitecture } from '../components/ScrollyArchitecture';
---

<Layout title="Workhorse | Universal AI Terminal Workstation">
  <main className="min-h-screen bg-[#070a11] text-slate-200 overflow-x-hidden selection:bg-sky-500 selection:text-slate-950">
    <!-- Hero Section -->
    <section className="relative pt-24 pb-16 px-4 max-w-7xl mx-auto flex flex-col items-center text-center">
      <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-950/60 border border-sky-500/40 text-sky-300 text-xs font-mono mb-6 backdrop-blur-md">
        <span className="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
        v3.1.0-ENTERPRISE-PRO-MAX Released
      </div>

      <h1 className="text-4xl md:text-7xl font-extrabold tracking-tight text-white max-w-4xl leading-tight font-sans">
        The Terminal AI Workstation <br />
        <span className="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 via-emerald-400 to-violet-400">
          That Never Quits.
        </span>
      </h1>

      <p className="mt-6 text-base md:text-lg text-slate-400 max-w-2xl font-mono leading-relaxed">
        Local-first Ollama auto-discovery, 5-Cycle circular resilience ring, active repository mutations, and live streaming thought accordions.
      </p>

      <!-- 3D Mascot Stage -->
      <div className="w-full my-6">
        <AnimatedHorse client:load />
      </div>

      <!-- Quick Install Bar -->
      <div className="w-full mt-4">
        <InstallBar client:load />
      </div>
    </section>

    <!-- Terminal Simulator Demonstration -->
    <section className="py-16 px-4 max-w-6xl mx-auto">
      <div className="text-center mb-8">
        <h2 className="text-2xl md:text-3xl font-bold text-white font-sans">Real Terminal Replay</h2>
        <p className="text-xs text-slate-400 font-mono mt-1">
          Watch Workhorse audit an active repository and mutate README.md in place.
        </p>
      </div>
      <TerminalSimulator client:visible />
    </section>

    <!-- 5-Cycle Resilience Ring Section -->
    <section className="py-16 px-4 max-w-7xl mx-auto">
      <ResilienceRingVisualizer client:visible />
    </section>

    <!-- Scrollytelling Architecture -->
    <section className="py-16 px-4 max-w-7xl mx-auto">
      <ScrollyArchitecture client:visible />
    </section>

    <!-- Skills and MCP Interop Directory -->
    <section className="py-16 px-4 max-w-7xl mx-auto">
      <SkillsMCPDirectory client:visible />
    </section>

    <!-- Footer -->
    <footer className="border-t border-slate-800/80 py-12 text-center text-xs text-slate-500 font-mono">
      <p>Workhorse Universal Terminal Workstation & Autonomous Agent Architecture.</p>
      <p className="mt-2 text-slate-600">Built with Textual, Rich, Ollama, Three.js, and Modern Web Standards.</p>
    </footer>
  </main>
</Layout>
```

---
*End of Complete WEB.md Specification — 1.0.0-PRO*
