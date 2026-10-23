import fitz, glob, os, re

doc = fitz.open(r"C:\Users\Misak\Desktop\NASA TT F-928.pdf")

# Map of extracted figures
extracted_info = {
    # Kibalchich
    "kibalchich-fig1.png": (15, "Figure 1", "Aeronautical Machine Diagram"),
    "kibalchich-fig2.png": (16, "Figure 2", "Thrust vector decomposition"),
    # Build
    "build-fig1.png": (23, "Figure 1", "First method flight path"),
    "build-fig2.png": (24, "Figure 2", "Second method flight path"),
    "build-fig3.png": (25, "Figure 3", "Prone position / bed for acceleration"),
    "build-fig4.png": (26, "Figure 4", "Wire recoil device"),
    "build-fig5.png": (28, "Figure 5", "Schematic section of vehicle with nested tanks"),
    "build-fig6.png": (30, "Figure 6", "Short tube thrust attachment"),
    "build-fig7.png": (30, "Figure 7", "Control stick / lever arm"),
    "build-fig8.png": (31, "Figure 8", "Concentric bodies gyroscope"),
    "build-fig9.png": (32, "Figure 9", "Co-axial counter-rotating gyroscopes"),
    "build-fig10.png": (32, "Figure 10", "Astatic gyroscope frames"),
    "build-fig11.png": (36, "Figure 11", "Combustion chamber and paraboloid exit tube"),
    "build-fig12.png": (39, "Figure 12", "Small angle of attack heating"),
    "build-fig13.png": (40, "Figure 13", "Elongated projectile vehicle cross-section"),
    "build-fig14.png": (42, "Figure 14", "Parabolic reflector and sun receptacle"),
    "build-fig15.png": (43, "Figure 15", "Water thermal dissociation and porous tubes"),
    "build-fig16.png": (44, "Figure 16", "Alternate reflector and heat receptacle"),
    "build-fig17.png": (44, "Figure 17", "Paraboloid of revolution (focus point)"),
    "build-fig18.png": (44, "Figure 18", "Cylindrical paraboloid (focal line)"),
    "build-fig19.png": (45, "Figure 19", "Cylinder focus"),
    "build-fig20.png": (45, "Figure 20", "Collapsible frame for reflector"),
    "build-fig21.png": (46, "Figure 21", "General view of frame with rods and cables"),
    "build-fig22.png": (49, "Figure 22", "Gravitational assist line of flight around planet"),
    "build-fig23.png": (49, "Figure 23", "Gravitational slingshot around two moving bodies"),
    "build-fig24.png": (49, "Figure 24", "Electric gun construction"),
    "build-fig25.png": (50, "Figure 25", "Multiple electric guns in sectional view"),
    "build-fig26.png": (51, "Figure 26", "Projectiles in series with nonmagnetic connector"),
    # Build Commentary
    "commentary-fig1.png": (53, "Figure 1", "Electrostatic dust propulsion scheme"),
    "commentary-fig2.png": (53, "Figure 2", "Charged particle flight through electrode"),
    "commentary-fig3.png": (57, "Figure 3", "Active agent transport vehicle construction"),
    "commentary-fig4.png": (57, "Figure 4", "Cross-section of vehicle in cannon"),
    # Space
    "space-fig1.png": (84, "Figure 1", "Tangential trajectory with multiple ellipses"),
    "space-fig2.png": (85, "Figure 2", "Hybrid type trajectory (spiral)"),
    "space-fig3.png": (92, "Figure 3", "J0 = F(h) curve for atmospheric resistance"),
    "space-fig4.png": (93, "Figure 4", "J0 = F(t) curve for k4 = 1/3"),
    "space-fig5.png": (99, "Figure 5", "Velocity loss Ld vs trajectory angle"),
    "space-fig6.png": (101, "Figure 6", "Temperature T = 0.09 Tv m^(1/4) vs velocity"),
    "space-fig7.png": (104, "Figure 7", "Atmospheric deceleration glider vehicle diagram"),
    "space-fig8.png": (105, "Figure 8", "Altitude vs velocity h = F(V1) during descent"),
    # Historical Outline
    "history-nezhdanovskiy-manuscript.png": (132, "Figure 1", "Nezhdanovskiy 1882-1884 manuscript facsimile"),
    "history-fedorov-pipe.png": (136, "Figure 2", "Fedorov reaction pipe / nozzle drawing"),
}

md_files = glob.glob("docs/zh/rocket-pioneers/**/*.md", recursive=True)

print("=== IMAGE USAGE IN MARKDOWN FILES ===")
for img_name, (pdf_page, fig_label, orig_desc) in extracted_info.items():
    found_in = []
    for md in md_files:
        content = open(md, "r", encoding="utf-8").read()
        if img_name in content:
            # find the line with this image
            for line in content.split("\n"):
                if img_name in line:
                    found_in.append((os.path.basename(md), line.strip()))
    if not found_in:
        print(f"[DROPPED / NOT IN MD] {img_name} (PDF p.{pdf_page}, {fig_label}: {orig_desc})")
    else:
        for md_name, line in found_in:
            print(f"[USED] {img_name} -> {md_name} (PDF p.{pdf_page}, {fig_label}): {orig_desc}")
