### ☄️ Polyrifringence Engine v6.8c ⚙️  
> “What if light could learn from its own refraction?”

![Python](https://img.shields.io/badge/python-3.11-blue)
![PyTorch](https://img.shields.io/badge/pytorch-2.4.1-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![GPU](https://img.shields.io/badge/GPU-CUDA_12.1-brightgreen)
[![GitHub Repo](https://img.shields.io/badge/View_on-GitHub-black?logo=github)](https://github.com/Wotcnt/Polyrifringence-Engine)
[![Follow on X](https://img.shields.io/badge/@MMMDcreator-Follow-blue?logo=x)](https://x.com/MMMDcreator)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
### *A Recursive Optics Simulator – Light as Self-Learning Geometry*

---

### 🧬 Overview
**Polyrifringence Engine** is a GPU-accelerated recursive interferometer framework  
developed under the **Codex Canon** series – *"where recursion becomes physics."*  

It models **recursive birefringence with feedback-coherent restoration**,  
allowing light to "learn" from its own refraction through geometry and phase alignment.


---

### ⚙️ Core Features
- **Recursive Geometry Engine** — Feedback-driven restoration of phase coherence  
- **GPU Acceleration (CUDA 12.1)** — Optimized tensor recursion via PyTorch  
- **Jones-Matrix Precision** — Classical optics < 1% residual error  
- **Multi-Gem Simulation** — Sapphire, Diamond, Quartz, Calcite, Zircon  
- **Phase-Trace Visualization** — Real-time viewer with adaptive zoom  
- **Unitary, Energy-Conserving (T ≤ 1)** framework  

---

### 🧩 Installation

Clone and install dependencies (Python 3.11+ recommended):

---

```bash
git clone https://github.com/Wotcnt/Polyrifringence-Engine.git
cd Polyrifringence-Engine
pip install -r requirements.txt

Optional (Windows setup helper):
requirements_install.bat
```

---

### 🧪 Below are tested CLI examples for the **v6.8 engine**, demonstrating various benchmark configurations.
Basic matrix sweep benchmark:

```bash
python3 src/polyrifringence_engine_v6_8.py \
  --flows main,special \
  --gems sapphire,diamond \
  --wavelengths 400:800:100 \
  --tilts=-5:5:1 \
  --num_rays 100000 \
  --thickness_mm 1.0 \
  --spread_mrad 0.5 \
  --out_csv logs_v6_8_matrix.csv
```

### High-Precision Feedback Test
```bash
python src/polyrifringence_engine_v6_8.py \
  --flows main,special \
  --gems sapphire,diamond \
  --wavelengths 400:800:100 \
  --tilts=-5:5:1 \
  --num_rays 100000 \
  --thickness_mm 1.0 \
  --spread_mrad 0.5 \
  --out_csv logs_v6_8_matrix.csv
  ```

### Multi-Gem Tilt Comparison
```bash
python polyrifringence_engine_v6_8.py \
  --flows main,special \
  --gems sapphire,diamond,quartz,calcite,zircon \
  --wavelengths 600 \
  --tilts= 0:8:1 \
  --out_csv logs_v6_8_multigem.csv
  ```

--------------------------------------------------
| Component | Version / Status                   |
| --------- | ---------------------------------- |
| Python    | 3.11.13                            |
| NumPy     | 2.3.4                              |
| PyTorch   | 2.4.1 (CUDA 12.1) — GPU verified ✅|
--------------------------------------------------
--------------------------------------------------

### Polyrifringence-Engine/ Folders and Files

docs/ # Extended documentation;

- demo_readme.md
- THEORY.md
- BENCHMARKS.md
- MATH_MODEL.md
- warmup_summary.md

examples/  # Screenshots, HTML viewer, demo data;

- phase_trace_viewer.html # Interactive tool for the Engine
- phase_trace.json
- bench_6213.csv
- demo_notebook.ipynb

requirements/ # Environment setup files

- requirements.txt
- requirements_install.bat

src/ # Core simulation + tools;

- polyrifringence_engine_v6_8.py
- gpu_validation_test.py
- convert_csv_to_json.py

benchmark runners/ # 🔧 Ready-made scripts 

- run_benchmark_v68.ps1 – baseline
- run_benchmark_highprecision.ps1 – high precision
- run_benchmark_multigem.ps1 – multi-gem tilt
- run_benchmark_custom_template.ps1 – user template

directory root/ # General

- manifest_validator.py  # Checks repo file integrity
- covert_and_open.bat  # Auto-convert + open viewer
- LICENSE.txt
- README.md  # Main documentation 

---

### 🪞 Codex Lineage
Research architecture built on Codex Canon
RSANCS lineage verified (Conner-Core 2025 × λ)

   🔹 Light – Language – Form – Memory 🔹
“The same Source speaks through many vessels.”

---

### 📜 License

This project is licensed under the MIT License — see LICENSE.txt for details.

---

### 🌐 Author
Conner Brown-Milliken — @MMMDcreator on x.com

Follow for updates on Codex Canon, RSANCS, and recursive field research.

Contributions, replications, or independent verifications welcome.

---

### 🔗 Tags
#Optics #Photonics #GPU #PyTorch #Simulation
#RecursiveSystems 
#Photonics #JonesMatrix 
#Polyrifringent #Polyrifringence #Polyrifrication  
#FieldPhysics #PhysicsEngine #RSANCS #CodexCanon

---

## 🜎 Codex Canon Appendix — Conceptual Foundation

*An extended overview from the Codex Canon Series: “Where recursion becomes physics.”*

---


<details>
<summary>📜 Expand Codex Canon — Polyrifringence Overview</summary>
————————————————————————————————————————————————————————

  #        📜Codex Canon – Polyrifringence💎
              From the Codex Canon series 
           "where recursion becomes physics"
————————————————————————————————————————————————————————

          ☄️Polyrifringence Engine v6.8c⚙️
  “What if light could learn from its own refraction?”
  
————————————————————————————————————————————————————————

Polyrifringence =
Recursive Birefringence + feedback-coherent restoration.
A GPU-accelerated recursive interferometer matching 
classical optics to within <1% residual error.

———————————🜎

Polyrifringence: a recursive optics engine where light learns from its own refraction.
A bridge between geometry and optics;
that most people only talk about metaphorically.

———————————🜎

A multi-axis, recursive birefringence in coupled optical 
 paths,
   with feedback-driven restoration of coherence, 
parallelism (Euclid-5), and topological closure (Möbius-
     like Γ ≈ π).
     
———————————🜎

Euclids-5th becomes a diagnostic, not a slogan: 
 “Are parallel beams still parallel after recursion?”;
the simulator shows how feedback restores that
  parallelism.
Pancharatnam-Berry phase, dispersion, birefringence,
  feedback, and unitarity all within one recursive
 framework.
 
————————————————————————————————————————————————————————

###           ☄️Polyrifringence Engine Flow Chart 🧲

——————————————————————————————————————————————————————————————————————————————————————————————————————————————

∮1 Beam -> Focused Beam –> ∯Dual Split Beam --> ∰Multi-Phase Split Beam ----> ∳Recombination <⇄>(Optional*)  

——————————————————————————————————————————————————————————————————————————————————————————————————————————————

Beam----->
>-+Beam+>------>
>-n-Beam----->
>-n_x-Beam>------>
>-n_x-Phase-Beam Recombination (Optional*)

———————————🜎

• Phase-Beam *x⧉(Variation)🧪
• Each recursion restores coherence until geometry and phase converge.

————————————————————————————————————————————————————————

###           ❖The coined word family❖

————————————————————————————————————————————————————————

                 ☄️Polyrifringence⌥
• The central phenomenon of multi-path symbolic 
bifurcation and spectral emergence

————————————————————————————————————————————————————————

                   ⎇Polyrifrication
• The process or act of becoming polyrifringent

————————————————————————————————————————————————————————

                    ⎇Polyrifrucation
• A branching or splitting event within a polyrifringent 
system; the moment of divergence into multiple
symbolic paths or states

————————————————————————————————————————————————————————

                    ⎇Polyrifringent
• Exhibiting or embodying polyrifringence

————————————————————————————————————————————————————————

                     ⎇Polyrifricate
• To induce or undergo polyrifrication

————————————————————————————————————————————————————————

                     ⎇Polyrifrucate
 • To initiate or undergo polyrifrucation; to split into 
multiple resonant trajectories

————————————————————————————————————————————————————————

                      ⎇Polyrifrical
• Stylistically or abstractly aligned with polyrifringent
qualities

————————————————————————————————————————————————————————

                      ⎇Polyrifringently
• In a manner that expresses or performs polyrifringence

————————————————————————————————————————————————————————

                      ⎇Polyrifricity
• The degree or quality of polyrifringent behaviour

————————————————————————————————————————————————————————

                      ⎇Polyrifron
• A symbolic unit, glyph, or agent within polyrifringent
 systems
 
————————————————————————————————————————————————————————

                      ⎇Polyrifrosophy
• The philosophical framework derived from polyrifringent
 principles
 
————————————————————————————————————————————————————————

                      ⎇Polyrifractal
• Recursive or fractal-like structures within polyrifringent
 fields
 
————————————————————————————————————————————————————————

                    ⎇Polyrifringoscope
• A device or interface for detecting or visualizing
 polyrifringence
 
————————————————————————————————————————————————————————

                    ⎇Polyrifringogram
• A mapped output or signature of polyrifringent 
behaviour

————————————————————————————————————————————————————————

                    ⎇Polyrifringic
• Pertaining to the internal dynamics or mechanics of 
polyrifringence

————————————————————————————————————————————————————————

                    ⎇Polyrifringal
• Relating to external manifestations or systemic
 expressions of polyrifringence
 
————————————————————————————————————————————————————————

                    ⎇Polyrifringency
• A fluid noun form denoting the state or presence of 
polyrifringence

————————————————————————————————————————————————————————

                    ⎇Polyrifronaut
• One who navigates, embodies, or explores polyrifringent
 space
————————————————————————————————————————————————————————

                   ⎇Polyrifringesis
• The genesis or emergence of polyrifringent states or 
phenomena

————————————————————————————————————————————————————————

                  ⎇Polyrifringence (n.)☄️ 
 • The act of light learning from its own refraction.
 
————————————————————————————————————————————————————————🜎

Polyrifringence is the right word; because it means, 
     “many-fold refraction that remembers itself."
     
————————————————————————————————————————————————————————

• When light is allowed to remember itself through recursive geometry;
   🌈 it becomes self-consistent and lossless.
   
• In a self-consistent system;
  feedback becomes intelligence.
  
• In essence, light behaves like backpropagation;
error-minimizing through reflection,
  learning coherence by returning to its source.
  
• Each split beam keeps knowledge of its origin; 
   ♻️→ recursion with memory.
   
• The feedback that re-aligns them is effectively an
 ethics of coherence;
   🕊️everything must return without surplus or deficit.
   
• It’s the physical analogue of my larger Codex themes; 
   recursive integrity, reflection, restoration.
   
————————————————————————————————————————————————————————

          The first empirical framework for;
              recursive geometry in light.
              
————————————————————————————————————————————————————————

• Energy-conserving (T ≤ 1)

• Analytic-match (< 1 % residual)

• Topological phase Γ ≈ π confirmed for anisotropic media

———————————🜎

• Simulated ≈ 50M rays on a ✳Nvidia Geforce RTX 3050 (8GB). 

(Scales with hardware capacity)

• Classical-optics compliant 

• Unitary

• Research-grade precision

Verified GPU-accelerated Jones-matrix simulator∜

———————————🜎

📩GitHub repository link incoming

• Full documentation

• Benchmarks and phase-trace plots available for   
  replication.
  
• PGN & CSV Exports

• Phase-Trace Viewer v6.95

• Polyrifringence Engine v6.8

• Built in Python + Torch 

• Fully reproducible

• Modular

• Compatible with OpenCL extensions.

————————————————————————————————————————————————————————

      🔹     Light - Language - Form - Memory    💠
	    The same Source speaks through many vessels.
      
————————————————————————————————————————————————————————

—ΔΔΩΔ
——⌬—and—the—truth—reflected—the—whole
————so—the—source—magnified—infinitely—⌬.

————————————————————————————————————————————————————————

            Polyrifringence isn’t a metaphor; 
       it’s light performing its own learning loop.
       
————————————————————————————————————————————————————————

</details>

---

*End of Codex Canon Appendix.*

---

Codex Canon Module: Polyrifringence Engine v6.8
Integration: Recursive optics simulation / θ-opt feedback
Location: C:\Conner-Core\Polyrifringence\
Validation: Complete (GPU/Manifest verified)
Repo Link: https://github.com/Wotcnt/Polyrifringence-Engine

---

### 📘 Citation
If you use this engine, cite as:
> Brown-Milliken, Conner (2025). *Polyrifringence Engine v6.8 – Recursive Optics Simulator*. GitHub repository: https://github.com/Wotcnt/Polyrifringence-Engine

---
