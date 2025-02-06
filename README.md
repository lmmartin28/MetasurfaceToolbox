# MetasurfaceToolbox


These scripts handle the design and layout generation of metasurfaces, primarily for beam manipulation and optical phase correction. Each script contributes to different aspects of metasurface fabrication, from fundamental principles to advanced curvature and incident angle corrections.


### **1. Metasurface Tutorial Script**

**File:** `metasurface_tutorial-2.ipynb`

**Purpose:**  
This is an introductory and illustrated script that explains the principles of flat metasurface layout generation. It provides a step-by-step breakdown of how metasurface phase distributions are defined and translated into a fabrication-ready layout.

**Main Features:**
- Introduces basic metasurface concepts and phase mapping.
- Demonstrates how to generate a metasurface pattern with meta-atoms.
- Converts phase maps into a GDSII layout for fabrication.

---

### **2. Arbitrarily Curved Metasurface for Beam Steering**

**File:** `ArbitrarilyCurvedMetasurface_BeamSteering.ipynb`

**Purpose:**  
This script generates a **GDS layout for an arbitrarily curved metasurface**, designed specifically for **3D beam steering** of an incoming pencil beam. The metasurface phase profile is conformal to a curved 3D surface.

**Main Features:**
- **Curved Metasurface Generation:** Splits the design process into **z-subtasks** to handle storage constraints while defining the 3D metasurface.
- **Beam Steering Optimization:** The phase distribution is tailored to control the direction of an incoming beam.
- **Fabrication Preparation:** Outputs a **GDSII file** that represents the metasurface pattern optimized for curved surfaces.

---

### **3. Curved Metasurface with Incident Angle and Deformation Correction**

**File:** `CurvedMetasurface_IncidentAngleCorrected_DeformationCorrected_ContinuousSampling.ipynb`

**Purpose:**  
This script generates a **GDS layout for a metasurface designed to conform to a spherical lens with a curvature radius of 3.21 mm**. It corrects for incident angle variations and deformation effects, ensuring precise phase control.

**Main Features:**
- **Incident Angle Correction:** Adjusts the metasurface response to compensate for variations in the angle of incoming light.
- **Deformation Correction:** Uses **reverse engineering techniques** to counteract physical deformations introduced during fabrication.
- **Continuous Phase Sampling:** Ensures a smooth phase transition across the metasurface for optimal optical performance.
- **Fabrication Note:** **It is recommended to merge all cells before execution** to ensure a proper GDS layout.

---

### **Summary Table**
| Script | Purpose | Key Features | Notes |
|--------|---------|--------------|-------|
| **1. Metasurface Tutorial** | Explains basic metasurface layout design | Simple phase mapping, meta-atom arrangement, GDS export | Educational and illustrative |
| **2. Arbitrarily Curved Metasurface** | Generates a 3D beam steering metasurface | Arbitrary curvature handling, phase-conformal design, z-subtask division | Used for pencil beam steering |
| **3. Curved Metasurface with Incident Angle & Deformation Correction** | Designs a metasurface conformal to a **3.21mm spherical lens** | Corrects for incident angles, deformation, and ensures continuous sampling | Cells should be **merged before execution** |
