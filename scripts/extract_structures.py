import pymupdf
import os

pdf_path = r'C:\Users\AnyNeko\Desktop\Controlled substances  a chemical and legal guide to the federal drug laws (Shulgin, Alexander T. (Alexander Theodore) etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf'
out_dir = r'C:\Users\AnyNeko\Desktop\amayalab-library\public\images\controlled-substances'
os.makedirs(out_dir, exist_ok=True)

doc = pymupdf.open(pdf_path)

plate_mapping = [
    (270, '01-opiate-progression.png', '阿片类母核经环简化衍变的结构序列'),
    (271, '02-phenylpiperidines-fentanyl.png', '苯基哌啶类、芬太尼修饰物与开环类似物'),
    (272, '03-pharmacological-groups-overview-1.png', '主要药理与结构族谱概览（苯二氮䓬、苯丙胺、吲哚、巴比妥等）'),
    (273, '04-pharmacological-groups-overview-2.png', '同化类固醇、镇静剂与植物天然成分概览'),
    (274, '05-morphine-ring-skeleton.png', 'Structure A：经典吗啡环骨架及其取代基'),
    (275, '06-dihydromorphine-skeleton.png', 'Structure A：二氢吗啡母核骨架及衍生物'),
    (276, '07-other-morphine-derivatives.png', 'Structure A：其他吗啡环骨架修饰物（含C环修饰）'),
    (277, '08-diels-alder-oripavine.png', 'Structure B：狄尔斯-阿尔德桥环加成物（埃托啡等奥利帕文衍生物）'),
    (278, '09-morphinan-and-benzomorphan.png', 'Structure C & D：吗啡喃骨架与苯并吗烷骨架'),
    (279, '10-ethyl-4-piperidinecarboxylate.png', 'Structure E1：4-哌啶羧酸乙酯类（哌替啶/杜冷丁家族）'),
    (280, '11-4-propionyloxy-piperidines.png', 'Structure E2：4-丙酰氧基哌啶类（反向哌替啶/MPPP等）'),
    (281, '12-fentanyl-skeleton.png', 'Structure F：芬太尼母核化学结构式'),
    (282, '13-fentanyl-analogues.png', 'Structure F：芬太尼类似物取代基分配表'),
    (283, '14-methadone-skeleton.png', 'Structure G1：美沙酮母核化学骨架'),
    (284, '15-methadone-optical-isomers.png', 'Structure G2：美沙酮光学异构体与异美沙酮'),
    (285, '16-methadone-analogues-propoxyphene.png', 'Structure G3：美沙酮开环类似物（右丙氧芬等）'),
    (286, '17-benzodiazepine-skeleton.png', 'Structure H：经典1,4-苯二氮䓬母核骨架'),
    (287, '18-benzodiazepines-table.png', 'Structure H：苯二氮䓬类受控药物取代基代码表'),
    (288, '19-benzo-analogues-of-benzodiazepines.png', 'Structure H1：苯并杂环类似物（氯巴占等）'),
    (289, '20-triazolo-imidazo-benzodiazepines.png', 'Structure H2：稠合三唑并与咪唑并苯二氮䓬（阿普唑仑、三唑仑等）'),
    (290, '21-substituted-amphetamines.png', 'Structure I：取代苯丙胺/安非他命类结构骨架与取代基详表'),
    (291, '22-unusual-amphetamine-relatives.png', 'Structure I：侧链异化苯丙胺类似物（卡西酮、麻黄碱等）'),
    (292, '23-indoles-and-tryptamines.png', 'Structure J：吲哚、色胺与麦角酰胺类（DMT、裸盖菇素、LSD等）'),
    (293, '24-barbituric-acid-derivatives-1.png', 'Structure K：巴比妥酸母核衍生物表（5,5-双取代）'),
    (294, '25-barbituric-acid-derivatives-2.png', 'Structure K：巴比妥酸衍生物续表与硫代巴比妥类'),
    (295, '26-methyl-barbiturates.png', 'Structure K：N-甲基巴比妥类'),
    (296, '27-phencyclidine-pcp-analogues.png', 'Structure L：苯环利定（PCP）与芳基环己胺类似物'),
    (297, '28-anabolic-steroids-testosterone.png', 'Structure M：同化雄激素类固醇（睾酮与双氢睾酮骨架）'),
    (298, '29-anabolic-steroids-nandrolone.png', 'Structure M：同化雄激素类固醇（诺龙与环修饰骨架）'),
    (299, '30-sulfones-and-sedatives.png', 'Structure N1：砜类与其他合成中枢神经镇静剂'),
    (300, '31-cannabis-components.png', 'Structure N2：大麻天然活性成分骨架（THC各异构体、CBN、CBD）'),
    (301, '32-benzimidazole-analgesics.png', 'Structure N3：苯并咪唑类强效镇痛剂（依託尼秦等）与格鲁米特'),
    (302, '33-one-of-a-kind-compounds.png', 'Structure N4：独立特殊架构化合物（甲喹酮、芬乙茶碱、氨雷司等）'),
]

print(f'Starting extraction of {len(plate_mapping)} structure plates...')
for page_num, filename, desc in plate_mapping:
    page = doc[page_num - 1]
    pix = page.get_pixmap(dpi=160)
    out_path = os.path.join(out_dir, filename)
    pix.save(out_path)
    print(f'Saved: {filename} ({desc})')

print('All chemical structure diagrams extracted successfully!')
