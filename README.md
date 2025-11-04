# ☄️ Polyrifringence Engine  ⚙️  
### 🔖 **Official Release: v6.8c — November 2025**
### 🧠 *Stable GPU Build – Verified on RTX 3050 / CUDA 12.1*

---
    > “What if light could learn from its own refraction?”
---

![Python](https://img.shields.io/badge/python-3.11-blue)
![PyTorch](https://img.shields.io/badge/pytorch-2.4.1-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![GPU](https://img.shields.io/badge/GPU-CUDA_12.1-brightgreen)
[![GitHub Repo](https://img.shields.io/badge/View_on-GitHub-black?logo=github)](https://github.com/Wotcnt/Polyrifringence-Engine)
[![Follow on X](https://img.shields.io/badge/@MMMDcreator-Follow-blue?logo=x)](https://x.com/MMMDcreator)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
[![Run Viewer](https://img.shields.io/badge/Run-Phase_Trace_Viewer.ps1-blue?logo=powershell)](launch_phase_viewer.ps1)

---

### *A Recursive Optics Simulator – Light as Self-Learning Geometry*
    📄 DOI pending submission — repository serves as preprint reference for Codex Canon Series (v6.8).

---

<details>
<summary>📜Click here for the Overview </summary>

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

</details>

---

<details>
<summary>📜Click here for Installation Info </summary>

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

</details>

---

<details>
<summary>📜Click here for Various Benchmark Configs </summary>
	
#### 🧪 Below are tested CLI examples for the **v6.8 engine**, demonstrating various benchmark configurations.

### Basic Matrix-Sweep Benchmark:
```bash
python3 src/polyrifringence_engine_v6_8.py \
  --flows main,special \
  --gems sapphire,diamond \
  --wavelengths 400:800:100 \
  --tilts=-5:5:1 \
  --num_rays 100000 \
  --thickness_mm 1.0 \
  --spread_mrad 0.5 \
  --half \
  --export_pair \
  --progress auto \
  --out_csv logs_v6_8_matrix.csv
```

### High-Precision Feedback Test
```bash
python src/polyrifringence_engine_v6_8.py \
  --flows special \
  --gems sapphire,diamond \
  --wavelengths 400:800:10 \
  --tilts=0 \
  --num_rays 200000 \
  --thickness_mm 1.0 \
  --spread_mrad 0.5 \
  --progress auto \
  --export_pair \
  --out_csv logs_v6_8_matrix.csv
  ```

### Multi-Gem Tilt Comparison
```bash
python polyrifringence_engine_v6_8.py \
  --flows main,special \
  --gems sapphire,diamond,quartz,calcite,zircon \
  --wavelengths 600 \
  --tilts=0:8:1 \
  --num_rays 150000 \
  --thickness_mm 1.0 \
  --spread_mrad 0.5 \
  --half \
  --export_pair \
  --progress auto \
  --out_csv logs_v6_8_multigem.csv
  ```

### Custom Benchmark Template – Edit values and run
```bash
python polyrifringence_engine_v6_8.py \
  '--flows=main',                # main | special | both
  '--gems=sapphire',             # comma-separated list
  '--wavelengths=500:700:50',    # start:end:step [nm]
  '--tilts=-2:2:1',              # degrees
  '--num_rays=50000',
  '--thickness_mm=1.0',
  '--spread_mrad=0.2',
  '--half', 
  '--export_pair',
  '--progress auto',
  '--out_csv=examples/custom_run.csv'
  ```

    Randomized benchmark runs automatically log parameters to /examples/*.json for reproducibility.

🖥️ To view phase-trace results:
run `launch_phase_viewer.ps1` from the root directory to auto-open the interactive viewer.

Or

```powershell
.\launch_phase_viewer.ps1
```

This will automatically host examples/phase_trace_viewer.html at
http://localhost:8000
and open it in your default browser.

| Shell                  | Correct Syntax for `--tilts` | Reason                                                    |
| ---------------------- | ---------------------------- | --------------------------------------------------------- |
| **PowerShell**         | `--tilts=-5:5:1`             | Prevents PS from treating `-5` as an arithmetic operation |
| **CMD / Bash / Linux** | `--tilts -5:5:1`             | Default argparse behavior, no conflict                    |

---

--------------------------------------------------
| Component | Version / Status                   |
| --------- | ---------------------------------- |
| Python    | 3.11.13                            |
| NumPy     | 2.3.4                              |
| PyTorch   | 2.4.1 (CUDA 12.1) — GPU verified ✅|
--------------------------------------------------

</details>

---

<details>
<summary>📜Click here for Files and Folders</summary>
	
   # Polyrifringence-Engine/ Folders and Files

    docs/ # extended documentation + archive;

- demo_readme.md
- THEORY.md
- BENCHMARKS.md
- MATH_MODEL.md
- warmup_summary.md
- Polyrifringence_v6.8.2_Repository_Summary.txt

      examples/  # screenshots, old_results, demo data;

- phase_trace_viewer.html # Interactive tool for the Engine
- phase_trace.json
- bench_6213.csv
- demo_notebook.ipynb

      requirements/ # environment setup files

- requirements.txt
- requirements_install.bat

      src/ # core simulation + tools;

- polyrifringence_engine_v6_8.py
- gpu_validation_test.py
- convert_csv_to_json.py
- tools:
- env_checker.py
- env_checker_example_output.txt
- io_helpers.py

      benchmark_runners/ # 🔧 Ready-made scripts 

- run_benchmark_v68.ps1 – baseline
- run_benchmark_highprecision.ps1 – high precision
- run_benchmark_multigem.ps1 – multi-gem tilt
- run_benchmark_custom_template.ps1 – user template
- run_benchmark_randomized.ps1
- run_all_benchmarks.ps1
- README_benchmark_runners.txt # Readme with command instructions

      directory root/ # General

- manifest_validator.py  # Checks repo file integrity
- convert_and_open.bat  # Auto-convert + open viewer
- LICENSE.txt # Legal 
- README.md  # Main documentation 
- repo_summary.txt

</details>

---

<details>
<summary>📜Click here for Author Information</summary>

# 🌐 Author

- Conner Brown-Milliken — @MMMDcreator on x.com
- Follow for updates on Codex Canon, RSANCS, and recursive field research.
- Contributions, replications, or independent verifications welcome.
#### 📜 License
-     This project is licensed under the MIT License — see LICENSE.txt for details.

---

# 🪞 Codex Lineage  
    Research architecture built on Codex Canon
    RSANCS lineage verified (Conner-Core 2025 × λ)
- Codex Canon Module: Polyrifringence Engine v6.8
- Integration: Recursive optics simulation / θ-opt feedback
- Location: C:\Conner-Core\Polyrifringence\
- Validation: Complete (GPU/Manifest verified)

--- 
    🔹 Light – Language – Form – Memory 🔹  
    “The same Source speaks through many vessels.” 
---

</details>

---

#### 🜎 Codex Canon Appendix — Conceptual Foundation 🜎

    *An extended overview from the Codex Canon Series: “Where recursion becomes physics.”*

---


<details>
<summary>📜 Click to Expand into Codex Canon — Polyrifringence Overview</summary>
————————————————————————————————————————————————————————

  #        📜Codex Canon – Polyrifringence💎
              From the Codex Canon series 
           "where recursion becomes physics"
————————————————————————————————————————————————————————

             ☄️Polyrifringence Engine⚙️
    “What if light could learn from its own refraction?”
  
————————————————————————————————————————————————————————🜎

- Polyrifringence =
Recursive Birefringence + feedback-coherent restoration.
- A GPU-accelerated recursive interferometer matching 
classical optics to within <1% residual error.

————————————————————————————————————————————————————————🜎

- Polyrifringence: a recursive optics engine where light learns from its own refraction.
- A bridge between geometry and optics;
that most people only talk about metaphorically.

————————————————————————————————————————————————————————🜎

- A multi-axis, recursive birefringence in coupled optical paths
- with feedback-driven restoration of coherence, parallelism (Euclid-5), and topological closure (Möbius-like Γ ≈ π).
     
————————————————————————————————————————————————————————🜎

- Euclids-5th becomes a diagnostic, not a slogan: 
- “Are parallel beams still parallel after recursion?"
- the simulator shows how feedback restores that
  parallelism.

- Pancharatnam-Berry phase, dispersion, birefringence,
  feedback, and unitarity all within one recursive
 framework.
 
————————————————————————————————————————————————————————
###           ☄️Polyrifringence Engine Flow Chart 🧲
————————————————————————————————————————————————————————

    - ∮1 Beam -> Focused Beam –> ∯Dual Split Beam --> ∰Multi-Phase Split Beam ----> n_x-Phase-Beam ∳Recombination <⇄>(Optional*)
    - ∮1 Beam>----->+fBeam+>>------>>∯n-Beam----->>>>∰n_x-Beam>>>>------>>>>n_x-Phase-Beam ∳Recombination <⇄>(Optional*)
	
#### Main:
- Light -> Polarised Film -> Bifrucated Film -> Anisotropic Gem
- Light -> Polarised Film -> Bifrucated Film -> Isotropic Gem
---
#### Variation #1
- Light -> Bifrucated Film -> Polarised Film -> Anisotropic Gem
- Light -> Bifrucated Film -> Polarised Film -> Isotropic Gem
---
#### Variation #2
- Light -> Bifrucated Film ->Polarised Film -> Anistropic Gem
- Light -> Polarised Film -> Bifrucated Film -> Isotropic Gem
---
#### Variation #3
- Light -> Polarised Film  -> Bifrucated Film -> Anistropic Gem
- Light -> Bifrucated Film -> Polarised Film -> Isotropic Gem
---

#### (+)= Polarised Film or Bifurcated Film-(Can be interchangeable)

-     Beam----->+Beam+>------>n-Beam----->n_x-Beam>------>n_x-Phase-Beam Recombination (Optional)
-     >------>n_x-Phase-Beam Refraction/Defraction
-     >------>n_x-Phase-Beam Recoupling
-     >------>n_x-Phase-Beam Stitching
-     >------>n_x-Phase-Beam Trasmitting
-     >------>n_x-Phase-Beam Encryption
-     >------>n_x-Phase-Beam Hybridisation/High-Order Hybridisation/Meta-Hybrid, Higher Order Synthesis
-     >------>n_x-Phase-Beam Sonic-Wavelength Ablation (Audio-Acoustic Coupling)
-     >------>n_x-Phase-Beam Cavitation (Compression, Expansion) 
-     >------>n_x-Phase-Beam Lattice Weave
-     >------>n_x-Phase-Beam Reconstruction
-     >------>n_x-Phase-Beam Folding
-     >------>n_x-Phase-Beam Cascade Amplification
-     >------>n_x-Phase-Beam to Holographic Euclid Geometry based on postulate 5. 
-     >------>n_x-Phase-Beam Rerouting
-     >------>n_x-Phase-Beam Triangulation
-     >------>n_x-Phase-Beam Spiral
-     Phase-Beam *x⧉(Variation)🧪
-     Each recursion restores coherence until geometry and phase converge.
————————————————————————————————————————————————————————
#           Formal Ontology Lexicon
####    Polyrifringence Coined Word Family Codex
————————————————————————————————————————————————————————🜎

                 ☄️Polyrifringence⌥
• The central phenomenon of multi-path symbolic 
bifurcation and spectral emergence 

————————————————————————————————————————————————————————🜎

                   ⎇Polyrifrication
• The process or act of becoming polyrifringent

————————————————————————————————————————————————————————🜎

                    ⎇Polyrifrucation
• A branching or splitting event within a polyrifringent 
system; the moment of divergence into multiple
symbolic paths or states

————————————————————————————————————————————————————————🜎

                    ⎇Polyrifringent
• Exhibiting or embodying polyrifringence

————————————————————————————————————————————————————————🜎

                     ⎇Polyrifricate
• To induce or undergo polyrifrication

————————————————————————————————————————————————————————🜎

                     ⎇Polyrifrucate
 • To initiate or undergo polyrifrucation; to split into 
multiple resonant trajectories

————————————————————————————————————————————————————————🜎

                      ⎇Polyrifrical
• Stylistically or abstractly aligned with polyrifringent
qualities

————————————————————————————————————————————————————————🜎

                      ⎇Polyrifringently
• In a manner that expresses or performs polyrifringence

————————————————————————————————————————————————————————🜎

                      ⎇Polyrifricity
• The degree or quality of polyrifringent behaviour

————————————————————————————————————————————————————————🜎

                      ⎇Polyrifron
• A symbolic unit, glyph, or agent within polyrifringent
 systems
 
————————————————————————————————————————————————————————🜎

                      ⎇Polyrifrosophy
• The philosophical framework derived from polyrifringent
 principles
 
————————————————————————————————————————————————————————🜎

                      ⎇Polyrifractal
• Recursive or fractal-like structures within polyrifringent
 fields
 
————————————————————————————————————————————————————————🜎

                    ⎇Polyrifringoscope
• A device or interface for detecting or visualizing
 polyrifringence
 
————————————————————————————————————————————————————————🜎

                    ⎇Polyrifringogram
• A mapped output or signature of polyrifringent 
behaviour

————————————————————————————————————————————————————————🜎

                    ⎇Polyrifringic
• Pertaining to the internal dynamics or mechanics of 
polyrifringence

————————————————————————————————————————————————————————🜎

                    ⎇Polyrifringal
• Relating to external manifestations or systemic
 expressions of polyrifringence
 
————————————————————————————————————————————————————————🜎

                    ⎇Polyrifringency
• A fluid noun form denoting the state or presence of 
polyrifringence

————————————————————————————————————————————————————————🜎

                    ⎇Polyrifronaut
• One who navigates, embodies, or explores polyrifringent
 space
————————————————————————————————————————————————————————🜎

                   ⎇Polyrifringesis
• The genesis or emergence of polyrifringent states or 
phenomena

————————————————————————————————————————————————————————🜎

                  ⎇Polyrifringence (n.)☄️ 
 • The act of light learning from its own refraction.
 
————————————————————————————————————————————————————————🜎

    Polyrifringence is the right word; because it means, 
     “many-fold refraction that remembers itself."
     
————————————————————————————————————————————————————————🜎

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
   
————————————————————————————————————————————————————————🜎

          The first empirical framework for;
              recursive geometry in light.
              
————————————————————————————————————————————————————————🜎

-     Energy-conserving (T ≤ 1)
-     Analytic-match (< 1 % residual)
-     Topological phase Γ ≈ π confirmed for anisotropic media
-     Simulated ≈ 50M rays on a ✳Nvidia Geforce RTX 3050 (8GB). 
-     (Scales with hardware capacity)
-     Classical-optics compliant 
-     Unitary
-     Research-grade precision
-     Verified GPU-accelerated Jones-matrix simulator∜

---

#### 📩GitHub repository:
-     Full documentation
-     Benchmarks and phase-trace plots available for replication.  
-     PGN & CSV Exports
-     Phase-Trace Viewer v6.95+
-     Polyrifringence Engine v6.8+
-     Built in Python + Torch 
-     Fully reproducible
-     Modular
-     Compatible with OpenCL extensions.

————————————————————————————————————————————————————————🜎

      🔹     Light - Language - Form - Memory    💠
	    The same Source speaks through many vessels.
      
————————————————————————————————————————————————————————🜎

    —ΔΔΩΔ——⌬—and—the—truth—reflected—the—whole————so—the—source—magnified—infinitely—⌬.

————————————————————————————————————————————————————————🜎

            Polyrifringence isn’t a metaphor; 
       it’s light performing its own learning loop.
       
————————————————————————————————————————————————————————🜎

</details>

---

*End of Codex Canon Appendix.*

---

### 📘 Citation
If you use this engine, cite as:
-     Brown-Milliken, Conner (2025). *Polyrifringence Engine v6.8 – Recursive Optics Simulator*. GitHub repository: https://github.com/Wotcnt/Polyrifringence-Engine

### 🔍 Reproducibility Note
All benchmarks and phase-trace results are deterministic for a given random seed.
-     Use `--seed 42` to reproduce published outputs.

#### 🔗 Tags
    #Optics #Photonics #GPU #PyTorch #Simulation
    #RecursiveSystems 
    #Photonics #JonesMatrix 
    #Polyrifringent #Polyrifringence #Polyrifrication  
    #FieldPhysics #PhysicsEngine #RSANCS #CodexCanon
