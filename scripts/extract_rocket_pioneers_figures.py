import os
import pymupdf

def crop_and_save(page, rect, output_path, zoom=3.0):
    mat = pymupdf.Matrix(zoom, zoom)
    # 限制在页面范围内
    crop_rect = rect & page.rect
    pix = page.get_pixmap(matrix=mat, clip=crop_rect)
    pix.save(output_path)
    print(f"Saved: {output_path} ({pix.width}x{pix.height})")

def main():
    pdf_path = r"C:\Users\Misak\Desktop\NASA TT F-928.pdf"
    out_dir = r"docs/public/images/rocket-pioneers"
    os.makedirs(out_dir, exist_ok=True)
    
    doc = pymupdf.open(pdf_path)
    
    # 1. 基巴利契奇篇
    # Page 15: Figure 1
    p15 = doc[14]
    crop_and_save(p15, pymupdf.Rect(180, 80, 420, 310), os.path.join(out_dir, "kibalchich-fig1.png"))
    
    # Page 16: Figure 2
    p16 = doc[15]
    crop_and_save(p16, pymupdf.Rect(200, 240, 360, 360), os.path.join(out_dir, "kibalchich-fig2.png"))
    
    # 2. 孔德拉秋克《致读此书以建造者》
    # Page 23: Figure 1
    p23 = doc[22]
    crop_and_save(p23, pymupdf.Rect(180, 160, 380, 240), os.path.join(out_dir, "build-fig1.png"))
    
    # Page 24: Figure 2
    p24 = doc[23]
    crop_and_save(p24, pymupdf.Rect(160, 100, 400, 470), os.path.join(out_dir, "build-fig2.png"))
    
    # Page 25: Figure 3 (仰卧椅)
    p25 = doc[24]
    crop_and_save(p25, pymupdf.Rect(140, 530, 440, 680), os.path.join(out_dir, "build-fig3.png"))
    
    # Page 26: Figure 4 (钢丝旋转反冲)
    p26 = doc[25]
    crop_and_save(p26, pymupdf.Rect(170, 400, 400, 530), os.path.join(out_dir, "build-fig4.png"))
    
    # Page 28: Figure 5 (多层锥形贮箱航天器总体)
    p28 = doc[27]
    crop_and_save(p28, pymupdf.Rect(100, 110, 480, 480), os.path.join(out_dir, "build-fig5.png"))
    
    # Page 30: Figure 6 (万向节推力偏转短管) & Figure 7 (连杆与四向滑轮)
    p30 = doc[29]
    crop_and_save(p30, pymupdf.Rect(180, 110, 400, 420), os.path.join(out_dir, "build-fig6.png"))
    crop_and_save(p30, pymupdf.Rect(160, 440, 430, 720), os.path.join(out_dir, "build-fig7.png"))
    
    # Page 31: Figure 8 (双同心旋转体陀螺仪)
    p31 = doc[30]
    crop_and_save(p31, pymupdf.Rect(160, 380, 360, 520), os.path.join(out_dir, "build-fig8.png"))
    
    # Page 32: Figure 9 (双同轴反转陀螺) & Figure 10 (双轴无定陀螺截面 a, b)
    p32 = doc[31]
    crop_and_save(p32, pymupdf.Rect(100, 100, 440, 290), os.path.join(out_dir, "build-fig9.png"))
    crop_and_save(p32, pymupdf.Rect(120, 310, 440, 650), os.path.join(out_dir, "build-fig10.png"))
    
    # Page 36: Figure 11 (喷管与燃烧室)
    p36 = doc[35]
    crop_and_save(p36, pymupdf.Rect(100, 270, 460, 400), os.path.join(out_dir, "build-fig11.png"))
    
    # Page 39: Figure 12 (迎角与气流)
    p39 = doc[38]
    crop_and_save(p39, pymupdf.Rect(160, 500, 400, 610), os.path.join(out_dir, "build-fig12.png"))
    
    # Page 40: Figure 13 (细长弹体滑翔减速外形)
    p40 = doc[39]
    crop_and_save(p40, pymupdf.Rect(110, 270, 440, 480), os.path.join(out_dir, "build-fig13.png"))
    
    # Page 42: Figure 14 (太阳能抛物面反射镜集热)
    p42 = doc[41]
    crop_and_save(p42, pymupdf.Rect(120, 430, 420, 750), os.path.join(out_dir, "build-fig14.png"))
    
    # Page 43: Figure 15 (水热分解与多孔管分离器)
    p43 = doc[42]
    crop_and_save(p43, pymupdf.Rect(100, 230, 500, 410), os.path.join(out_dir, "build-fig15.png"))
    
    # Page 44: Figure 16 (共轴双反射镜) & Fig 17, 18 (旋转/柱面抛物面)
    p44 = doc[43]
    crop_and_save(p44, pymupdf.Rect(130, 90, 440, 450), os.path.join(out_dir, "build-fig16.png"))
    crop_and_save(p44, pymupdf.Rect(200, 510, 380, 640), os.path.join(out_dir, "build-fig17.png"))
    crop_and_save(p44, pymupdf.Rect(200, 650, 380, 770), os.path.join(out_dir, "build-fig18.png"))
    
    # Page 45: Figure 19 (柱面聚焦) & Figure 20 (折叠反射镜)
    p45 = doc[44]
    crop_and_save(p45, pymupdf.Rect(200, 90, 430, 250), os.path.join(out_dir, "build-fig19.png"))
    crop_and_save(p45, pymupdf.Rect(140, 510, 500, 700), os.path.join(out_dir, "build-fig20.png"))
    
    # Page 46: Figure 21 (整体线缆支架图)
    p46 = doc[45]
    crop_and_save(p46, pymupdf.Rect(170, 300, 390, 460), os.path.join(out_dir, "build-fig21.png"))
    
    # Page 49: Figure 22 (卫星借力引力助推) & Figure 23 (双星运动借力) & Figure 24 (电磁炮)
    p49 = doc[48]
    crop_and_save(p49, pymupdf.Rect(180, 80, 420, 240), os.path.join(out_dir, "build-fig22.png"))
    crop_and_save(p49, pymupdf.Rect(210, 340, 390, 450), os.path.join(out_dir, "build-fig23.png"))
    crop_and_save(p49, pymupdf.Rect(140, 550, 450, 720), os.path.join(out_dir, "build-fig24.png"))
    
    # Page 50: Figure 25 (多炮并联发射客运舱)
    p50 = doc[49]
    crop_and_save(p50, pymupdf.Rect(180, 500, 400, 660), os.path.join(out_dir, "build-fig25.png"))
    
    # Page 51: Figure 26 (串联非磁性弹头)
    p51 = doc[50]
    crop_and_save(p51, pymupdf.Rect(180, 80, 400, 160), os.path.join(out_dir, "build-fig26.png"))
    
    # Page 53 (编注): Figure 1 (静电喷射微粒推进) & Figure 2 (带电粒子电荷转移)
    p53 = doc[52]
    crop_and_save(p53, pymupdf.Rect(130, 240, 450, 430), os.path.join(out_dir, "commentary-fig1.png"))
    crop_and_save(p53, pymupdf.Rect(140, 540, 440, 650), os.path.join(out_dir, "commentary-fig2.png"))
    
    # Page 57 (编注): Figure 3 (液压抗冲击货运炮弹) & Figure 4 (炮弹横截面)
    p57 = doc[56]
    crop_and_save(p57, pymupdf.Rect(130, 90, 450, 520), os.path.join(out_dir, "commentary-fig3.png"))
    crop_and_save(p57, pymupdf.Rect(240, 630, 360, 770), os.path.join(out_dir, "commentary-fig4.png"))
    
    # 3. 孔德拉秋克《征服星际空间》
    # Page 84: Figure 1 (切向多椭圆入轨)
    p84 = doc[83]
    crop_and_save(p84, pymupdf.Rect(130, 90, 450, 360), os.path.join(out_dir, "space-fig1.png"))
    
    # Page 85: Figure 2 (混合螺旋轨道)
    p85 = doc[84]
    crop_and_save(p85, pymupdf.Rect(200, 360, 420, 630), os.path.join(out_dir, "space-fig2.png"))
    
    # Page 92: Figure 3 (高度-大气阻力曲线)
    p92 = doc[91]
    crop_and_save(p92, pymupdf.Rect(150, 200, 420, 370), os.path.join(out_dir, "space-fig3.png"))
    
    # Page 93: Figure 4 (时间-加速度曲线)
    p93 = doc[92]
    crop_and_save(p93, pymupdf.Rect(160, 230, 420, 450), os.path.join(out_dir, "space-fig4.png"))
    
    # Page 99: Figure 5 (速度损失关系图)
    p99 = doc[98]
    crop_and_save(p99, pymupdf.Rect(130, 280, 480, 560), os.path.join(out_dir, "space-fig5.png"))
    
    # Page 101: Figure 6 (绝热压缩激波加热温度图)
    p101 = doc[100]
    crop_and_save(p101, pymupdf.Rect(120, 360, 480, 660), os.path.join(out_dir, "space-fig6.png"))
    
    # Page 104: Figure 7 (大气减速滑翔航天器示意图)
    p104 = doc[103]
    crop_and_save(p104, pymupdf.Rect(100, 150, 440, 530), os.path.join(out_dir, "space-fig7.png"))
    
    # Page 105: Figure 8 (滑翔减速高度-速度曲线)
    p105 = doc[104]
    crop_and_save(p105, pymupdf.Rect(150, 500, 450, 750), os.path.join(out_dir, "space-fig8.png"))
    
    # 4. 索科尔斯基历史纲要
    # Page 132: Figure 1 (涅日达诺夫斯基 1882-1884 手稿照片)
    p132 = doc[131]
    crop_and_save(p132, pymupdf.Rect(90, 260, 480, 780), os.path.join(out_dir, "history-nezhdanovskiy-manuscript.png"))
    
    # Page 136: Figure 2 (费奥多罗夫反作用喷气管)
    p136 = doc[135]
    crop_and_save(p136, pymupdf.Rect(180, 90, 380, 350), os.path.join(out_dir, "history-fedorov-pipe.png"))

if __name__ == "__main__":
    main()
