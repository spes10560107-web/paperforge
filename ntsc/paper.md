---
profile: report-nstc-undergrad  # PaperForge 編譯時自動套用此 profile（ctrl+shift+b 不必再帶 --profile）

# ============================================================
# === 國科會大專學生研究計畫成果報告基本資訊 ===
# ============================================================
project-title-zh: "3D 列印件瑕疵檢測與品質評分研究設計"
project-title-en: "Defect Detection and Quality Grading System for 3D-Printed Parts"
project-id: "NSTC 114-2813-C-239-054-E"
project-type: "國科會\\quad 大專學生專題研究計畫"
student: "劉哲銘"
advisor: "張致文"
period-from: "114 年 07 月 01 日"
period-to: "115 年 02 月 28 日"
period-months: "計 8 個月"
affiliation: "國立聯合大學機械工程學系"
handling-method: "本計畫可公開查詢"
year: "115"
month: "04"
day: "27"

# ============================================================
# === 圖片子圖支援 ===
# ============================================================
subfigure: true

# ============================================================
# === 紙張與邊距（依 NCU 規範） ===
# ============================================================
geometry: "top=2.5cm, bottom=2.5cm, left=3cm, right=2cm"
papersize: a4
classoption: [fleqn]

# ============================================================
# === 字體設定 ===
# ============================================================
mainfont: "Times New Roman"
CJKmainfont: "標楷體"
CJKoptions:
  - AutoFakeBold=2.5
fontsize: 12pt
linestretch: 1.5

# ============================================================
# === 引用/參考文獻（biblatex + biber） ===
# ============================================================
bibliography: references.bib
biblatex: true
biblio-style: ieee
suppress-bibliography: true
header-includes:
  - \usepackage{float}
  - \usepackage{adjustbox}
  - \usepackage{array}
  - \usepackage{tabularx}
  - \usepackage{makecell}
  - \setlength{\tabcolsep}{3pt}
  - \setlength{\extrarowheight}{1pt}
  - \renewcommand{\arraystretch}{1.14}
  - '\renewcommand\cellset{\renewcommand\arraystretch{1.16}}'
  - \captionsetup[table]{font=small,justification=centering}
  - \captionsetup[figure]{font=small,skip=12pt}
  - \setlength{\floatsep}{12pt plus 2pt minus 2pt}
  - \setlength{\textfloatsep}{14pt plus 2pt minus 2pt}
  - \setlength{\intextsep}{12pt plus 2pt minus 2pt}
  - '\newcommand{\TableNote}[2][0.9\textwidth]{\par\vspace{0.3em}\begin{minipage}{#1}\centering\footnotesize\textit{#2}\end{minipage}\par}'

# ============================================================
# === 頁碼與標題設定 ===
# ============================================================
numbersections: true
secnumdepth: 4
toc: false
---

<!-- ============================================================ -->
<!-- 封面頁（國科會大專學生研究計畫成果報告） -->
<!-- ============================================================ -->

\begin{titlepage}

\begin{center}

\vspace*{1.5cm}

{\bfseries\fontsize{20pt}{28pt}\selectfont 國科會補助\par}

\vspace{0.5cm}

{\bfseries\fontsize{20pt}{28pt}\selectfont 大專學生研究計畫研究成果報告\par}

\vspace{1.5cm}

{\fontsize{16pt}{20pt}\selectfont ＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\par}

\vspace{0.3cm}

{\fontsize{14pt}{18pt}\selectfont 計\,畫\,名\,稱：\ProjectTitleZh\par}

\vspace{0.3cm}

{\fontsize{16pt}{20pt}\selectfont ＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\par}

\end{center}

\vspace{1.2cm}

\noindent\hspace*{2cm}\begin{minipage}{0.8\textwidth}
\setlength{\parskip}{0.35cm}

執行計畫學生：\StudentName

學生計畫編號：\ProjectId

研\,究\,期\,間：\PeriodFrom 至 \PeriodTo 止，\PeriodMonths

指\,導\,教\,授：\AdvisorName
\end{minipage}

\vfill

\begin{center}
\setlength{\parskip}{0.3cm}

處理方式：\HandlingMethod

執\,行\,單\,位：\Affiliation

中\,華\,民\,國\,\ROCYear\ 年\ \ROCMonth\ 月\ \ROCDay\ 日
\end{center}

\vspace*{0.5cm}

\end{titlepage}

<!-- ============================================================ -->
<!-- 內封頁 -->
<!-- ============================================================ -->

\begin{titlepage}
\begin{center}

\vspace*{2cm}

{\bfseries\fontsize{18pt}{24pt}\selectfont \ProjectType\par}

\vspace{2.5cm}

{\bfseries\fontsize{22pt}{30pt}\selectfont \ProjectTitleZh\par}

\vspace{1cm}

{\fontsize{14pt}{18pt}\selectfont \ProjectId\par}

\vspace{3.5cm}

指導老師：\AdvisorName\ 老師

\vspace{1cm}

專題學生：\StudentName

\vfill

中\,華\,民\,國\,\ROCYear\,年\,\ROCMonth\,月

\vspace{1cm}

\end{center}
\end{titlepage}

<!-- ============================================================ -->
<!-- 摘要（羅馬數字頁碼 i, ii, iii ...） -->
<!-- ============================================================ -->

\pagenumbering{Roman}
\pagestyle{frontmatter}

\begin{center}
{\Large\bfseries 摘要}
\end{center}

熔融沉積成型（FDM）為目前桌上型 3D 列印之主流製程，其列印品質受噴嘴溫度、回抽距離、列印速度等多項參數交互影響，容易產生拉絲（Stringing）、翹曲與裂痕等瑕疵。傳統人工目視檢查費時且判定標準因人而異，難以維持品質一致性，因此自動化瑕疵辨識成為導入工業 4.0 智慧製造之關鍵需求。

本研究以魚骨形狀 PLA 列印件為對象，建立涵蓋 A 至 F 共六等級拉絲嚴重程度之影像分類資料集，採用 MobileNetV3-Large 為骨幹進行遷移學習，並附加品質評分輔助頭以輸出 0 至 100 之連續品質分數；同時以 ResNet18、EfficientNet-B0 為對照基準，於原圖層級 Group Split 與多種子重複實驗下評估模型穩定性，並補做單變因消融、模型校準、Grad-CAM 與外部影像檢查，以區分單次最佳結果與可重複之結論。

實驗在嚴格 Group Split 測試集（原圖零重疊）上，主要設定之最佳種子達 86\% 之整體準確率，多種子重複後平均仍維持約 81\%，顯示在小樣本工業視覺任務下具一定可行性。本研究貢獻在於提供 FDM 魚骨拉絲瑕疵之可重現基準與端對端批量辨識原型，並指出受限於單一機型、單一材料、單一形狀、單一瑕疵類型與標注一致性未驗證等條件，現階段仍應定位為品質管控之輔助工具，後續需擴充至跨機型、跨材料與多人標注以提升泛化與客觀性。

\vspace{0.5cm}

\noindent\textbf{關鍵詞：3D 列印、熔融沉積成型（FDM）、瑕疵檢測、深度學習、MobileNetV3、品質評分、遷移學習、資料不平衡、分組切分（Group Split）、消融實驗、基準模型比較}

\newpage

<!-- ============================================================ -->
<!-- 目錄 -->
<!-- ============================================================ -->

\tableofcontents

\newpage

<!-- ============================================================ -->
<!-- 圖目錄 -->
<!-- ============================================================ -->

\listoffigures

\newpage

<!-- ============================================================ -->
<!-- 表目錄 -->
<!-- ============================================================ -->

\listoftables

\newpage

<!-- ============================================================ -->
<!-- 正文開始（阿拉伯數字頁碼） -->
<!-- ============================================================ -->

\pagenumbering{arabic}
\pagestyle{mainmatter}

# 緒論 {#sec:intro}

## 研究背景 {#sec:intro-background}

3D 列印技術（Three-Dimensional Printing），又稱積層製造（Additive Manufacturing, AM），係指透過電腦輔助設計（CAD）軟體建立三維數位模型後，依據切片軟體產生的路徑指令，將材料逐層堆積成形的製造技術[@ISOASTM52900]。自 1980 年代光固化成型（Stereolithography, SLA）等技術問世以來，積層製造歷經數十年演進，應用範圍由工業快速原型逐漸擴展至航太、汽車、醫療、電子、建築及個人消費等多元領域[@gibsonAdditiveManufacturingTechnologies2021; @OurStory3D2017]，相關市場規模亦持續成長，使列印品質管控的自動化需求日益受到重視[@marketsandmarkets3DPrintingMarket]。

在眾多 3D 列印技術中，熔融沉積成型（Fused Deposition Modeling, FDM）因設備成本相對低廉、操作流程較為簡易，且可支援 PLA、PETG、ABS、TPU 等多種熱塑性材料，成為桌上型與教育應用場域中常見的 3D 列印技術之一[@gibsonAdditiveManufacturingTechnologies2021; @InventorFDM3D2017]。FDM 的基本工作原理是將熱塑性聚合物線材（Filament，直徑通常為 1.75 mm 或 2.85 mm）送入加熱腔，融化後由噴嘴（Nozzle）擠出，依照切片路徑在熱床（Heated Bed）上逐層堆積，冷卻固化後形成實體成品。由於 FDM 技術的普及，其列印品質管控的重要性日益受到業界與學術界的重視。

然而，FDM 列印的品質受到多項關鍵參數的交互影響，包括噴嘴溫度、熱床溫度、列印速度、回抽距離（Retraction Distance）與速度、層高（Layer Height）、填充密度（Infill Density）、冷卻風扇轉速及支撐結構設定等。任一參數設定不當，均可能引發不同類型的列印瑕疵，導致成品品質下降。目前業界對 FDM 列印品質的評估，仍多依賴操作人員的人工目視檢查，缺乏系統化、自動化的品質管控機制，難以滿足工業 4.0 背景下智慧製造的需求。

在工業 4.0 透過資訊通訊技術使機器、製程與生產系統智慧化連網、提升製造自動化的趨勢下[@WhatIndustry40; @WhatIndustrie40]，將深度學習導入 3D 列印品質管控、建立自動化的瑕疵辨識與評分系統，既符合此技術路線，也具有顯著的實際應用價值。

## 研究動機 {#sec:intro-motivation}

在實際的 3D 列印生產場景中，品質管控面臨以下幾項核心困難：其一，人工目視效率低落，當列印批量增加時，每件成品的逐一檢視耗時過長，成為生產流程的瓶頸；其二，主觀判斷標準不一，不同操作人員對同一件成品的品質評估可能存在差異，尤其在瑕疵程度接近等級邊界的案例中，判斷結果的不一致性會降低品質數據的可信度；其三，缺乏量化依據，傳統目視評估難以提供精確的數值品質分數，無法為列印參數的系統性優化提供回饋依據；其四，難以建立品質歷史紀錄，人工評估結果不易系統性地留存，不利於品質趨勢分析與製程改善。

有鑑於此，本研究的研究動機源自對以上痛點的深刻認識：若能以深度學習模型模擬有經驗品管人員的判斷邏輯，將瑕疵辨識與品質評分工作自動化，不僅可大幅提升檢測效率，更能確保評估標準的一致性與客觀性。此外，本研究的另一動機來自對「有限資料量下如何訓練高效能模型」此一挑戰的探索興趣。在實際應用場景中，取得充足的標注資料往往成本高昂，如何在樣本數受限的條件下（本研究最少的 F 等級為 32 張），透過遷移學習、資料增強及損失函數設計等技術手段，建立具可行性的分類模型，是本研究的核心技術課題。

## 研究目的與貢獻 {#sec:intro-purpose}

本研究的核心貢獻有以下四項：

1. **FDM 魚骨拉絲六等級資料集**：建立包含 1110 張魚骨影像、依拉絲面積佔比定義之六等級（A 至 F）資料集；雖目前由單一標注者完成尚待多人一致性驗證，但就本研究目前蒐集之文獻範圍而言，可作為後續 FDM 拉絲瑕疵小樣本影像分類研究之可重現基準。
2. **嚴格分組切分與多 seed 泛化評估**：以原圖為單位進行 Group Split（原圖零重疊），避免同源樣本造成過度樂觀的評估；MobileNetV3-Large 在嚴格測試集達約 86\% 整體準確率，並以五個 seed 重複後平均仍維持約 81\%，提供比單次切分更保守的小樣本工業視覺基準（詳細數值見 \ref{sec:results-supplemental} 節）。
3. **模型策略比較、消融與不確定性分析**：本研究完成 MobileNetV3-Large、ResNet18、EfficientNet-B0 之完整 / 簡化策略比較，並補做 Focal Loss、Label Smoothing、Mixup、Weighted Random Sampler 之單變因消融。五 seed 結果顯示，各模型 accuracy 與 QWK 差異未達統計顯著；但 MobileNetV3-Large 完整與 ResNet18 完整之 macro-F1 顯著高於簡化設定。消融結果顯示移除 Weighted Sampler 對 QWK 與跨等級誤判傷害最大，模型校準則顯示低 confidence 樣本適合導入人工複核流程。
4. **端對端批量辨識系統可行性**：整合自動裁切、批量推論、分級輸出與 HTML 可視化報告，於桌上型 GPU 上達毫秒級單張推論（每秒可處理上百張），驗證離線批量部署之可行性（詳細效能見 \ref{sec:results-batch} 節）。

附帶產出包含可量化的六等級評分準則、各等級範例圖、Label Studio 標注流程與雙輸出（六分類 + 0 至 100 連續品質分）模型架構，作為後續研究擴充之共用工具。

## 研究範圍 {#sec:intro-scope}

本研究的研究範圍以 FDM 技術列印之魚骨形狀 PLA 材質列印件為主要研究對象，聚焦於拉絲瑕疵的嚴重程度分類，不包含翹曲及裂痕瑕疵的深入分析（因現有樣本中此兩類瑕疵數量不足）。實驗設備限定為 Bambu Lab A1 3D 印表機，耗材為標準 PLA 線材，拍攝環境為固定背景的室內自然光環境，因此模型的泛化能力主要針對此特定設備與材料條件。資料規模方面，本研究資料集共取得 1110 筆有效魚骨樣本，分屬六個品質等級，最多等級 546 張（A 級），最少等級 32 張（F 級）。

為使後續讀者與審查者能正確解讀本研究之結論，茲將本研究之適用範圍與已知限制條列如下：

1. **單一硬體條件**：僅使用 Bambu Lab A1 印表機與標準 PLA 線材，未驗證其他機型（如 Prusa、Creality）或材料（如 PETG、ABS、TPU）之表現。
2. **單一幾何條件**：僅使用魚骨形狀樣本，模型對其他幾何形狀（如盒體、齒輪、有機曲面）之泛化能力未經驗證。
3. **單一瑕疵類型**：僅針對拉絲（Stringing）嚴重程度分類；翹曲與裂痕雖於文獻回顧介紹，但因樣本不足未納入訓練與測試。
4. **資料相關性與分組切分**：1110 張樣本係由 185 張原始照片各裁切出約 6 支魚骨而來，同一原圖切出之多支樣本在光線、背景與列印批次上高度相關。為避免同源樣本造成過度樂觀的評估，本研究以原圖 ID 為分組鍵，採用分組隨機切分（Group Shuffle Split，seed=7），並在零原圖重疊之嚴格測試集（168 筆）上評估；惟 B、E、F 測試樣本數偏少（16、8、4 張），相關結果詳見 \ref{sec:results-supplemental} 節。

上述為本研究之主要邊界條件。其餘較技術性之限制，包含標注一致性未驗證（單一標注者，未做 Cohen's / Fleiss' Kappa）、品質分數未經多人主觀評分校準、基準模型比較與消融研究之範圍、ordinal 任務以 nominal classification 近似處理、模型可解釋性僅完成 Grad-CAM 定性檢查，以及外部影像僅完成未標注 sanity check、文獻與市場資料來源之準確性等；此類限制因需搭配方法與實驗結果方能完整說明，統一於 \ref{sec:results-supplemental-interpretation} 節與第 \ref{sec:conclusion} 章之結論中討論。

## 研究流程 {#sec:intro-flow}

本研究的整體執行流程分為三大階段：第一階段為資料蒐集與前處理，包含 3D 列印樣本製作、影像拍攝、魚骨自動裁切及人工標注；第二階段為模型訓練與評估，包含資料集整理、模型訓練、效能評估及新舊版本比較；第三階段為系統整合與應用，包含批量辨識系統開發、可視化報告產生及實際應用驗證。詳細流程如圖 \ref{fig:overall-flow} 所示。

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth,height=0.72\textheight,keepaspectratio]{images/research-overall-flow.png}
\caption{研究整體流程圖}
\label{fig:overall-flow}
\end{figure}

# 文獻回顧 {#sec:literature}

## 文獻與資料來源準確性說明 {#sec:literature-source-quality}

為避免將不同性質的資料來源等量解讀，本文在文獻回顧中採取分級引用原則。與名詞定義、製造流程、深度學習方法與模型架構相關之內容，優先引用國際標準、教科書、同儕審查論文與模型原始論文，例如 ISO/ASTM 52900[@ISOASTM52900]、additive manufacturing 教科書[@gibsonAdditiveManufacturingTechnologies2021]、ImageNet / ResNet / MobileNetV3 等文獻[@dengImageNetLargescaleHierarchical2009; @heDeepResidualLearning2016; @howardSearchingMobileNetV32019]。與 FDM 瑕疵現象、切片參數或設備操作經驗相關之內容，則輔以 Bambu Lab、Prusa 等廠商文件[@StringingOozing; @BambuStudioAdvanced; @WarpingPrusaKnowledge2025; @LayerSeparationSplitting2024]；此類來源反映實務經驗，但不等同於受控實驗證據，且部分線上文件未明確標示發佈年份，僅依其網址與存取日期保留可追溯性。市場規模數字則僅用於緒論背景與產業動機[@marketsandmarkets3DPrintingMarket]，並不參與模型效能或方法有效性判斷。

因此，本文的核心實證結論均來自本研究資料集、Group Split 評估、多 seed 重複實驗、消融研究、混淆矩陣、校準分析與可重現程式輸出；外部文獻主要提供研究脈絡與方法依據。若外部市場報告、公司歷史頁或廠商 troubleshooting 文件的內容日後更新，不影響本文對模型效能與系統限制的主要判斷。

## FDM 3D 列印技術概述 {#sec:literature-fdm}

熔融沉積成型（Fused Deposition Modeling, FDM）由 Scott Crump 於 1989 年發明，並於 1992 年由 Stratasys 公司商業化推出[@InventorFDM3D2017]。FDM 的工作流程分為四個主要步驟：（1）數位建模：以 CAD 軟體（如 Autodesk Fusion 360、SolidWorks 等）建立三維數位模型並輸出 STL 或 3MF 格式；（2）切片處理：以切片軟體（如 Bambu Studio、PrusaSlicer 等）將模型切分為若干水平薄層，生成噴嘴移動路徑指令（G-code）；（3）列印成形：印表機依 G-code 指令逐層擠出熔融材料堆積成形；（4）後處理：拆除支撐結構、打磨或表面處理以達到所需品質。

影響 FDM 列印品質的關鍵參數可分為溫度類、速度類及結構類三大類。溫度類包括噴嘴溫度（Nozzle Temperature）、熱床溫度（Bed Temperature）及環境溫度；速度類包括列印速度（Print Speed）、移位速度（Travel Speed）、回抽速度（Retraction Speed）；結構類包括層高（Layer Height）、填充密度（Infill Density）、填充圖案（Infill Pattern）、支撐結構類型及冷卻設定。這些參數之間存在複雜的交互作用，例如提高列印速度通常需要相應提高噴嘴溫度以確保材料充分熔融，但過高的溫度又會增加拉絲風險，因此參數調校是一項需要豐富實驗經驗的技術工作。

## 3D 列印常見瑕疵類型 {#sec:literature-defects}

根據現有 FDM 文獻與設備廠商 troubleshooting 文件，FDM 列印常見的表面瑕疵主要包含以下三類，如圖 \ref{fig:defect-stringing} 至圖 \ref{fig:defect-cracking} 所示。需注意，廠商文件主要用於補充實務現象與調參經驗；本文實驗僅將拉絲瑕疵納入模型訓練與測試，翹曲與裂痕因樣本不足僅作背景說明。

\begin{figure}[H]
\centering
\includegraphics[width=0.65\textwidth,height=0.55\textheight,keepaspectratio]{images/defect-stringing.png}
\caption{拉絲（Stringing）瑕疵：噴嘴移位時殘留的細絲}
\label{fig:defect-stringing}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.65\textwidth,height=0.55\textheight,keepaspectratio]{images/defect-warping.png}
\caption{翹曲（Warping）瑕疵：底層因冷卻收縮而翹起}
\label{fig:defect-warping}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.65\textwidth,height=0.55\textheight,keepaspectratio]{images/defect-cracking.png}
\caption{裂痕（Cracking）瑕疵：層間結合不足導致的分層}
\label{fig:defect-cracking}
\end{figure}

**拉絲（Stringing）**：係指噴嘴在非列印區域移動時，熔融材料因回抽不足、噴嘴溫度過高或材料流動性過大而持續滲出，進而在列印件表面形成細絲狀殘留的現象。其嚴重程度通常與回抽距離與速度、噴嘴溫度、移位速度及冷卻效率等參數交互影響有關[@StringingOozing; @BambuStudioAdvanced]。

**翹曲（Warping）**：係指列印件於冷卻過程中因材料收縮與平台附著力不足，使底層邊角產生上翹或脫離列印平台的現象。此問題通常與熱床溫度、第一層附著、環境溫度變化、列印速度與材料熱收縮特性有關[@WarpingPrusaKnowledge2025]。

**裂痕（Cracking）或層間分離（Layer Separation）**：係指列印件不同層之間因冷卻速率差異、層間黏結不足或翹曲應力過大，導致層與層之間產生分離裂縫的現象。此類缺陷會降低列印件的結構完整性與機械強度[@LayerSeparationSplitting2024]。

## 電腦視覺與深度學習於工業瑕疵檢測 {#sec:literature-cv-dl}

電腦視覺（Computer Vision）技術在工業品質檢測領域的應用已有數十年歷史，早期方法以傳統影像處理技術為主，包括邊緣偵測、閾值分割、形態學運算及特徵工程等，需要領域專家手動設計特徵提取規則。此類方法在受控環境下（固定光源、背景及目標位置）表現尚可，但對光線變化、姿態變化及背景干擾的魯棒性較差，且難以應對複雜的多類別瑕疵辨識任務。

深度學習技術的崛起從根本上改變了電腦視覺的研究範式[@DeepLearning; @lecunGradientbasedLearningApplied1998]。卷積神經網路（CNN）以端到端的方式自動學習影像的層次化特徵表示，從底層的邊緣和紋理特徵到高層的語義特徵，無需人工設計特徵，且在充足資料的支持下，其辨識精度遠超傳統方法[@dengImageNetLargescaleHierarchical2009; @heDeepResidualLearning2016]。近年來，CNN 已被廣泛應用於半導體晶圓瑕疵檢測、紡織品缺陷辨識、鋼板表面瑕疵分類、PCB 板焊接缺陷偵測等工業品質管控任務[@bhattImageBasedSurfaceDefect2021]，並在多項基準測試中達到甚至超越人類水準；在 3D 列印領域，亦已有研究將 CNN 應用於列印過程的即時錯誤偵測與校正[@brionGeneralisable3DPrinting2022]。

## 相關文獻探討 {#sec:literature-related}

本節依「通用影像分類 → 小樣本遷移學習 → 類別不平衡處理 → 與本研究最相近之 FDM 領域研究」的順序，逐步收斂至本研究的問題情境。

Jogin 等人[@joginFeatureExtractionUsing2018]在 CIFAR-10 上以六層 Conv2D--ReLU--MaxPooling 架構對 10 類、50,000 張 32 × 32 像素彩色影像分類，達到 85.97\% 準確率，明顯優於同期的支援向量機（SVM）、決策樹與隨機森林等傳統方法。此結果說明 CNN 自動學得的深度特徵在多類別影像分類上具系統性優勢，為本研究以 CNN 取代人工特徵工程提供基本依據；惟此屬通用影像分類任務，與 FDM 表面瑕疵之關聯僅屬間接。

Varshni 等人[@varshniPneumoniaDetectionUsing2019]以 DenseNet-169、ResNet-50、VGG-16、Xception 等預訓練模型對 ChestX-ray14 肺炎 X 光影像做特徵提取並接 SVM 分類，其中 DenseNet-169+SVM 在 AUC 達 0.8002。此研究直接針對「標注樣本有限」之情境，證明遷移學習在小樣本醫學影像上的有效性，與本研究在約千張量級資料上採用 ImageNet 預訓練 MobileNetV3-Large 的處境高度吻合，為本研究的遷移學習策略提供方法論依據。

Lin 等人[@linFocalLossDense2017]提出之 Focal Loss 原用於目標偵測中前景（目標）與背景（非目標）的極端類別不平衡，其在標準交叉熵的基礎上引入調焦因子 $(1-p_t)^\gamma$，降低模型已正確分類之高信心樣本的損失權重，使訓練聚焦於困難樣本（Hard Example），在類別分布不均時仍能有效收斂。此思路適用於本研究各瑕疵等級樣本數差異懸殊的情形（本研究實際採用之不平衡處理組合詳見 \ref{sec:method-model} 節）。

與本研究最直接相關者為 Brion 與 Pattinson[@brionGeneralisable3DPrinting2022]，其以多頭神經網路對 FDM 列印過程進行**即時**錯誤偵測與參數校正，並在多種印表機、材料與幾何形狀上展現泛化能力，屬「列印中（in-process）」的閉迴路監控。相較之下，本研究著眼於「列印後（post-print）」的成品表面品質評級：將拉絲瑕疵依嚴重度劃分為 A 至 F 六個**序數**等級並輸出連續品質分，且刻意採用可部署於邊緣裝置的輕量模型，於小規模且不平衡的資料上以嚴格切分重複評估。兩者在偵測時機、輸出粒度與部署情境上互補，而後者正是本研究欲補足之處（詳見 \ref{sec:literature-gap} 節）。

## MobileNetV3 架構 {#sec:literature-mobilenetv3}

MobileNet 系列最早由 Howard 等人提出，其核心設計是以深度可分離卷積（Depthwise Separable Convolution）取代標準卷積：將其分解為深度卷積（Depthwise Conv）與逐點卷積（Pointwise Conv）兩步驟，在維持感受野的同時大幅降低參數量與計算量，使 CNN 更適合部署於行動端與邊緣裝置[@howardMobileNetsEfficientConvolutional2017]。MobileNetV3 則由 Google 以神經架構搜尋（NAS）自動搜尋最優配置，並在深度可分離卷積的基礎上再引入兩項關鍵技術[@howardSearchingMobileNetV32019]：（1）**壓縮激活（Squeeze-and-Excitation, SE）注意力機制**：對特徵圖各通道的重要性進行自適應加權，強化關鍵特徵的表達；（2）**Hard-Swish 激活函數**：以分段線性函數近似 Swish 激活，在效能損失極小的前提下大幅降低計算成本。

MobileNetV3-Large 的整體架構包含：初始卷積層（3 × 3 卷積，stride = 2）、15 個 Bottleneck 模組（其中部分模組含 SE 注意力機制）、1 × 1 卷積升維層、自適應平均池化層，以及最終的分類頭。以 224 × 224 像素輸入為例，模型參數量約 5.4M，計算量約 219 MFLOPs；在本研究使用的預訓練模型中，較新版本（V2）之 ImageNet-1K 預訓練權重 Top-1 指標高於前一版本（V1），因此以較新版本作為本研究初始化權重。本研究採用 ImageNet V2 預訓練權重，可充分利用模型在 1.28M 張大規模影像上學習到的通用視覺特徵，顯著減少對標注資料量的依賴。

## 遷移學習與資料不平衡處理 {#sec:literature-transfer}

遷移學習（Transfer Learning）在電腦視覺領域的核心假設是：在大規模資料集（如 ImageNet）上預訓練的模型，已學習到豐富的底層視覺特徵（邊緣、紋理、形狀等），這些特徵可以遷移至目標任務，即使目標任務的資料量遠少於預訓練資料集。常用的遷移學習策略包括：（a）**特徵提取（Feature Extraction）**：凍結預訓練模型的全部或大部分層，僅訓練新增的任務特定層；（b）**微調（Fine-tuning）**：以較小的學習率對全部或部分層進行更新，使模型特徵更好地適應目標任務。

資料不平衡（Class Imbalance）是小樣本瑕疵分類常見的難題，文獻上的處理手段大致可分為三類：（1）**資料採樣層面**的重採樣，如對少數類別過採樣（oversampling）或加權抽樣，平衡各類別在訓練過程中的曝光機會；（2）**損失函數層面**的成本敏感法，如前述 Focal Loss[@linFocalLossDense2017]，對困難樣本或少數類別加重懲罰；（3）**資料增強層面**的方法，如 Mixup[@zhangMixupEmpiricalRisk2018]在批次中對任意兩筆樣本進行線性混合，擴充訓練分布的多樣性並抑制模型對邊界樣本的過度自信。三類手段彼此正交、可組合使用；本研究實際採用之組合與超參數設定詳見 \ref{sec:method-model} 節。

## 研究缺口與本研究定位 {#sec:literature-gap}

綜合前述文獻，可歸納出三點現況與缺口。其一，CNN 與遷移學習在工業表面瑕疵檢測（半導體晶圓、鋼板、紡織品、PCB 等）已有成熟應用，並在多項基準上達到甚至超越人類水準[@bhattImageBasedSurfaceDefect2021]；但這些任務多屬「有無瑕疵」或「瑕疵種類」的名目分類，少有針對單一瑕疵之「嚴重程度分級」的序數評估。其二，在 FDM 領域，既有代表性研究（如 Brion 與 Pattinson[@brionGeneralisable3DPrinting2022]）聚焦於列印過程中的即時錯誤偵測與校正，著重「即時介入、避免廢件」，而非列印完成後對成品表面品質給出細緻且可量化的分級。其三，遷移學習雖已證實能緩解小樣本問題[@varshniPneumoniaDetectionUsing2019]，但各研究的資料規模、不平衡程度與評估切分方式差異甚大，少有在「小樣本、類別不平衡」條件下同時報告嚴格切分、多 seed 重複與校準分析的可重現評估。

據此，本研究的定位是補足「列印後、單一瑕疵（拉絲）、序數品質分級、輕量可部署、嚴格可重現評估」這一交集情境：以 ImageNet 預訓練之 MobileNetV3-Large 為骨幹進行遷移學習，輸出 A 至 F 六等級分類並附加連續品質分；針對類別不平衡採用重採樣、成本敏感損失與資料增強的組合（見 \ref{sec:method-model} 節）；並以 Group Split 嚴格切分、多 seed 重複與校準分析建立可重現的效能基準（見 \ref{sec:results} 章）。此情境在現有文獻中著墨相對有限，亦是本研究的主要貢獻所在。

# 研究方法 {#sec:method}

## 研究架構 {#sec:method-architecture}

本研究系統架構以資料流與責任分工為主軸呈現，如圖 \ref{fig:method-flow} 所示。整體流程由列印製樣與影像蒐集開始，經由裁切前處理與人工標注建立 A 至 F 六等級資料集，再以 MobileNetV3-Large 進行遷移學習訓練，最後輸出混淆矩陣、品質分數、批量分級資料夾與 HTML 統計報告。此呈現方式可直接對應資料來源、模型訓練與推論輸出三大環節。硬體端由 Bambu Lab A1 印表機、智慧型手機（用於拍攝）與配備 NVIDIA RTX 3050 Laptop GPU 之筆記型電腦（用於訓練與推論）組成，硬體規格詳見 \ref{sec:method-equipment-pc} 節。

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth,keepaspectratio]{images/method-system-flow.png}
\caption{研究流程與資料流關係圖}
\label{fig:method-flow}
\end{figure}

## 實驗設備 {#sec:method-equipment}

### 3D 列印設備規格 {#sec:method-equipment-printer}

本研究使用 Bambu Lab A1 桌上型 3D 印表機作為列印設備，該機型採用床式平台移動（Bed Slinger）機械結構，具備高精度列印能力與穩定性。Bambu Lab A1 的主要技術規格整理如表 \ref{tab:printer-spec} 所示。

\begin{table}[H]
\centering
\caption{Bambu Lab A1 主要技術規格}
\label{tab:printer-spec}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{cc}
\hline
\textbf{規格項目} & \textbf{規格值} \\
\hline
最大列印尺寸 & 256 $\times$ 256 $\times$ 256 mm \\
最高列印速度 & 500 mm/s（正常模式 250 mm/s）\\
噴嘴直徑 & 0.4 mm（標準）\\
噴嘴最高溫度 & 280 $^\circ$C \\
熱床最高溫度 & 100 $^\circ$C \\
層高範圍 & 0.05 $\sim$ 0.35 mm \\
定位精度 & XY 軸 $\pm$0.05 mm \\
支援材料 & PLA、PETG、TPU、PVA 等 \\
自動調平 & 支援（ABL 自動調床）\\
震動補償 & 支援（Input Shaping）\\
內建攝影機 & 支援遠端查看 \\
\hline
\end{tabular}
\end{table}

### 列印參數設定截圖 {#sec:method-equipment-params}

本研究的列印參數以「全研究期間統一固定」為原則，避免引入不必要變因，使後續模型訓練可專注於拉絲嚴重程度差異。參數控制重點分為五類：

1. **品質設定**：固定層高、線寬與外殼品質，使拉絲差異主要來自列印狀態而非幾何尺寸變動。
2. **強度設定**：控制填充密度與壁厚，避免樣本因結構強度不足而產生非拉絲類破壞。
3. **速度設定**：維持列印與移動速度的一致性，降低批次間因噴嘴移動條件不同造成的額外變異。
4. **支撐設定**：在魚骨件列印中保持固定，避免支撐拆除痕跡被誤判為瑕疵特徵。
5. **其他進階設定**：作為固定環境條件，不作為本研究主要變因。

完整 Bambu Studio 參數設定彙整於附錄二表 \ref{tab:param-summary}，作為實驗重現之查核依據。

### 電腦硬體與軟體環境 {#sec:method-equipment-pc}

模型訓練所使用的電腦硬體與軟體規格如表 \ref{tab:pc-spec} 所示。本研究利用 NVIDIA RTX 3050 Laptop GPU 進行深度學習模型訓練，搭配 PyTorch 2.6.0+CUDA 12.4 環境，開啟 FP16 混合精度訓練以提升運算效率[@falconPyTorchLightning2019]。

\begin{table}[H]
\centering
\caption{電腦硬體與軟體環境}
\label{tab:pc-spec}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{cc}
\hline
\textbf{項目} & \textbf{規格} \\
\hline
處理器 & AMD Ryzen 7 4800H with Radeon Graphics 2.90 GHz \\
GPU & NVIDIA GeForce RTX 3050 Laptop（4 GB VRAM）\\
記憶體 & 32.0 GB DDR4 \\
作業系統 & Windows 10 Home 64 位元 \\
CUDA / cuDNN & CUDA 12.4 \\
Python & 3.11 \\
PyTorch & 2.6.0+cu124 \\
訓練框架 & PyTorch Lightning 2.x \\
標注工具 & Label Studio \\
開發工具 & Visual Studio Code \\
\hline
\end{tabular}
\end{table}

## 耗材規格與設定 {#sec:method-material}

本研究使用直徑 1.75 mm 之 PLA（聚乳酸）線材作為列印材料。PLA 具備列印門檻低、尺寸穩定與收縮率小等特性，適合用於建立可重複的 FDM 列印瑕疵資料集。本研究不將材料配方作為主要變因，而是固定耗材種類與冷卻條件，使後續模型學習重點集中於拉絲程度與品質等級差異。

耗材與冷卻設定的正文重點在於三點：（一）使用相同材料來源以降低批次差異；（二）維持固定噴嘴與熱床相關條件，避免溫度差異擴大成不可控變因；（三）將冷卻模式固定，避免風扇策略改變造成表面狀態差異。完整耗材與冷卻設定截圖移至附錄三，正文不再逐張呈現。

## 列印樣本製作與影像蒐集 {#sec:method-sample}

### 樣本設計與列印過程 {#sec:method-sample-design}

本研究以魚骨形狀列印件作為樣本，是因其具有細長肋條、尖端與多個間隙，對 FDM 拉絲瑕疵特別敏感。當噴嘴溫度、回抽設定、移動速度或冷卻條件不穩定時，細絲通常會出現在魚骨間隙與尖端區域，因此此幾何形狀適合作為拉絲嚴重程度分類的測試對象。

資料蒐集採分批列印方式進行，並另行補充少數等級與失敗件樣本，使各等級樣本更為完整。每組原始照片可裁切出 6 支魚骨樣本，最後整理為 1110 筆有效資料。正文保留資料蒐集流程與代表性設計說明，完整列印過程照片改列於附錄一，避免主文被連續照片切斷。

此安排的重點是讓正文回答三個問題：為何選擇魚骨件、資料如何分批取得，以及照片如何轉換為可訓練資料。至於每一張列印過程照片的時間與狀態，屬於實驗紀錄與佐證資料，放在附錄一更適合查核與保存。

### 影像拍攝規範 {#sec:method-sample-capture}

影像拍攝採用固定距離、固定背景的標準化規範：拍攝設備為智慧型手機相機（解析度約 12 MP），鏡頭垂直俯拍列印床，拍攝距離固定於熱床正上方約 30 cm，室內自然光環境，避免陽光直射造成反光。背景為 Bambu Lab A1 原廠的黑色熱床表面，與各色 PLA 魚骨形成良好的明暗對比，有助於後續影像裁切與辨識。拍攝完成後，資料再依批次進行裁切、標注、模型訓練與辨識分析。各批次拍攝資料統計如表 \ref{tab:batch-stats} 所示。

\begin{table}[H]
\centering
\caption{各批次拍攝資料統計}
\label{tab:batch-stats}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
\hline
\textbf{批次} & \textbf{張數} & \textbf{裁切後樣本數} \\
\hline
第 1 批 & 3 & 18 \\
第 2 批 & 20 & 120 \\
第 3 批 & 14 & 84 \\
第 4 批 & 17 & 102 \\
第 5 批 & 51 & 306 \\
第 6 批 & 30 & 180 \\
第 7 批 & 30 & 180 \\
第 8 批 & 20 & 120 \\
\hline
\textbf{合計} & \textbf{185} & \textbf{1110} \\
\hline
\end{tabular}
\end{table}

## 影像前處理 {#sec:method-preprocessing}

### 魚骨自動裁切 {#sec:method-preprocessing-crop}

本研究依列印與拍攝完成後整理之實驗照片進行魚骨樣本自動裁切。裁切採用固定網格方式：將每張照片等分為 2 欄 × 3 列，各格切出一支魚骨，裁切後尺寸約 700 × 900 pixels，保留足夠細節供後續辨識。本研究整理後共取得 1110 張有效單支魚骨樣本。

以下圖 \ref{fig:crop-fish01} 至圖 \ref{fig:crop-fish03} 為自動裁切輸出的魚骨裁切結果範例，可清楚看到每支魚骨被完整切割、背景一致，裁切品質良好。

\begin{figure}[H]
\centering
\includegraphics[width=0.6\textwidth,height=0.58\textheight,keepaspectratio]{images/crop-fish-example-01.jpg}
\caption{魚骨裁切結果範例（fish01）}
\label{fig:crop-fish01}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.6\textwidth,height=0.58\textheight,keepaspectratio]{images/crop-fish-example-02.jpg}
\caption{魚骨裁切結果範例（fish02）}
\label{fig:crop-fish02}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.6\textwidth,height=0.58\textheight,keepaspectratio]{images/crop-fish-example-03.jpg}
\caption{魚骨裁切結果範例（fish03）}
\label{fig:crop-fish03}
\end{figure}

### 資料增強策略 {#sec:method-preprocessing-aug}

訓練階段對輸入影像施加表 \ref{tab:augmentation} 所列的多種隨機增強變換，以擴充有效訓練樣本多樣性，提升模型泛化能力；驗證與測試階段不施加增強，確保評估結果客觀。

\begin{table}[H]
\centering
\caption{訓練資料增強方法彙整（Mixup 僅用於原完整候選設定；簡化設定未啟用）}
\label{tab:augmentation}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
\hline
\textbf{增強方法} & \textbf{參數設定} & \textbf{目的說明} \\
\hline
Resize & 224$\times$224 px & \makecell{統一輸入尺寸以符合\\預訓練模型要求} \\
RandomHorizontalFlip & $p=0.5$ & 水平翻轉，增加方向多樣性 \\
RandomVerticalFlip & $p=0.3$ & 垂直翻轉 \\
RandomRotation & $\pm$30$^\circ$ & 應對拍攝角度偏差 \\
ColorJitter & \makecell{亮度 0.4、對比 0.4\\飽和 0.3、色相 0.1} & 應對光線與色調變化 \\
RandomGrayscale & $p=0.05$ & 強化紋理特徵，減少顏色依賴 \\
RandomPerspective & distortion=0.2, $p=0.3$ & 應對拍攝視角偏差 \\
RandomErasing & \makecell{$p=0.2$\\scale=(0.02, 0.15)} & 提升部分遮擋魯棒性 \\
Normalize & ImageNet mean/std & 對齊預訓練模型輸入分布 \\
Mixup（批次層級）& $\alpha=0.3$ & \makecell{線性混合兩筆樣本\\提升邊界辨識能力} \\
\hline
\end{tabular}
\end{table}

## 品質等級定義 {#sec:method-grading}

本研究依拉絲瑕疵面積佔魚骨本體的比例，制定六個品質等級（A 至 F），如表 \ref{tab:grading-criteria} 所示。等級定義以客觀可量化的面積比例為主要依據，並配合各等級範例圖（圖 \ref{fig:grade-a} 至圖 \ref{fig:grade-f}），以提升單一標注者在整批資料中的前後一致性。

需特別說明的是，本研究現階段無法取得第二位以上標注者重新標注資料，因此無法計算 Cohen's Kappa、Fleiss' Kappa 或人類 baseline。故本文所有模型準確率皆應解讀為「相對於本研究固定標注準則與單一標注者標籤之表現」，而非「相對多人共識品質標準之客觀準確率」。本研究可主張的是：模型能學習並重現此套固定分級準則，用於降低批量檢查負擔與提供人工複核輔助；但不宣稱已完全消除人工主觀差異。

\begin{table}[H]
\centering
\caption{六等級品質定義}
\label{tab:grading-criteria}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccc}
\hline
\textbf{等級} & \textbf{名稱} & \textbf{拉絲面積判斷標準} & \textbf{目標分數} & \textbf{應用建議} \\
\hline
A & 完美品 & \makecell{完全無拉絲細絲\\表面乾淨} & 100 分 & 可直接使用 \\
B & 良好品 & \makecell{極少量細絲，1$\sim$2 根短絲\\面積可忽略} & 80 分 & 一般用途可接受 \\
C & 輕微拉絲 & \makecell{少量細絲\\拉絲面積 $<$ 魚身 1/4} & 60 分 & \makecell{外觀要求低時\\可接受} \\
D & 中度拉絲 & \makecell{明顯細絲\\拉絲面積佔魚身 1/4$\sim$1/2} & 40 分 & \makecell{需重新列印\\或後處理} \\
E & 嚴重拉絲 & \makecell{大量細絲\\拉絲面積 $>$ 魚身 1/2} & 20 分 & 品質不合格 \\
F & 失敗品 & \makecell{極度拉絲\\幾乎看不出魚骨結構} & 0 分 & 廢品 \\
\hline
\end{tabular}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.62\textheight,keepaspectratio]{images/grade-a-sample.jpg}
\caption{A 等級（完美品）：完全無細絲，表面乾淨}
\label{fig:grade-a}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.62\textheight,keepaspectratio]{images/grade-b-sample.jpg}
\caption{B 等級（良好品）：極少量細絲，1$\sim$2 根短絲}
\label{fig:grade-b}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.62\textheight,keepaspectratio]{images/grade-c-sample.jpg}
\caption{C 等級（輕微拉絲）：拉絲面積小於魚身四分之一}
\label{fig:grade-c}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.62\textheight,keepaspectratio]{images/grade-d-sample.jpg}
\caption{D 等級（中度拉絲）：拉絲面積約佔魚身四分之一至二分之一}
\label{fig:grade-d}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.62\textheight,keepaspectratio]{images/grade-e-sample.jpg}
\caption{E 等級（嚴重拉絲）：拉絲面積大於魚身二分之一}
\label{fig:grade-e}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.62\textheight,keepaspectratio]{images/grade-f-sample.jpg}
\caption{F 等級（失敗品）：結構幾乎難以辨識}
\label{fig:grade-f}
\end{figure}

### 各等級邊界判斷邏輯 {#sec:method-grading-boundary}

前一節已以圖 \ref{fig:grade-a} 至圖 \ref{fig:grade-f} 呈現 A 至 F 六等級的代表性樣本，本節進一步補充各等級之邊界判斷邏輯，作為標注時的判斷依據。

**A 與 B 等級的差異**在於是否可見極少量短細絲。A 級要求表面乾淨且無明顯拉絲；B 級雖仍可接受，但可能在魚骨細刺或局部轉角處出現少量短絲。這兩級容易混淆的原因，是短絲在拍攝角度與光線變化下可能被弱化或放大，因此標注時必須以整體面積與可見程度共同判斷。

**C 與 D 等級的差異**在於拉絲面積是否跨越局部區域並形成連續分布。C 級通常仍屬輕微拉絲，魚骨主體結構清楚；D 級則已出現較大範圍的絲狀殘留，可能遮蔽部分魚骨間隙。這是本研究模型較容易出現邊界誤判的區間，原因在於兩者都保留可辨識的主體輪廓，但拉絲覆蓋比例不同。

**E 與 F 等級**則代表嚴重瑕疵與失敗件。E 級仍可辨識魚骨結構，但拉絲覆蓋比例已明顯偏高；F 級則接近列印失敗或結構難以辨識。由於 F 級樣本數僅 32 張，未來仍需補充更多失敗件，以提升模型對極端瑕疵的泛化能力。

## 資料標注流程 {#sec:method-labeling}

本研究使用 Label Studio（開源標注平台）[@OpenSourceData]完成全部裁切圖的人工標注。標注流程為：

1. 將裁切圖匯入 Label Studio 專案。
2. A 等級直接標記為合格，不畫框。
3. 有拉絲的樣本，以邊界框框住拉絲區域，並選擇對應的嚴重程度標籤。
4. 完成後匯出標注結果。
5. 解析標注結果，將各樣本依標籤歸入 A 至 F 對應等級的資料集。

標注完成後，A 級 546 張、B 級 87 張、C 級 213 張、D 級 160 張、E 級 72 張、F 級 32 張，共 1110 張有效資料。

## 模型架構與訓練設計 {#sec:method-model}

### 模型架構 {#sec:method-model-arch}

#### 骨幹網路選擇之考量 {#sec:method-model-rationale}

本研究選用 MobileNetV3-Large 作為主要骨幹，並以 ResNet18、EfficientNet-B0 為對照基準，主要考量如下：

1. **參數量與小樣本過擬合風險**：1110 張資料規模偏小，過大模型容易過擬合。MobileNetV3-Large 約 5.4M 參數、ResNet18 約 11.7M、EfficientNet-B0 約 5.3M，皆屬輕量級。相較之下 ResNet50（25.6M）或 ViT-Base（86M）參數量過大，在此資料規模下需更強之資料增強與正則化策略才能避免過擬合。
2. **推論效率與未來部署彈性**：MobileNetV3 系列原為行動端與邊緣裝置設計，雖本研究在 RTX 3050 桌上型 GPU 部署，但保留未來轉移至 Bambu Lab A1 內建 SoC、Raspberry Pi 或 Jetson Nano 等邊緣裝置之選項。實測單張推論時間 6.90 ms 亦支持即時批量處理需求。
3. **ImageNet 預訓練權重可用性**：MobileNetV3-Large 之較新版本（V2）ImageNet 預訓練權重優於前一版本（V1），且可直接載入，遷移學習成本低。
4. **與相近研究之可比較性**：ResNet18 為小資料瑕疵檢測之常用基準，EfficientNet-B0 為近年主流輕量模型代表，三者並列可同時涵蓋「移動端最佳化」「殘差網路經典」「複合縮放最佳化」三條設計哲學，為後續研究者提供可比較之 baseline。

選擇之 trade-off 在於：未涵蓋 Vision Transformer 系列（如 ViT-Tiny、DeiT-Tiny）、ConvNeXt 系列等新架構，亦未探討 self-supervised pre-training（如 DINO、MAE）對小樣本任務之助益，此屬本研究範圍限制，列為後續研究方向。

#### 雙輸出架構 {#sec:method-model-dualhead}

本研究採用 MobileNetV3-Large[@howardSearchingMobileNetV32019]（ImageNet V2 預訓練）作為骨幹網路，以遷移學習方式進行六分類微調。模型修改如下：將分類頭最後一個全連接層（原 1000 類輸出）替換為含 Dropout（p = 0.4）的六分類線性層；同時在 pooling 後的特徵向量上接品質評分輔助頭，其結構為 Dropout（p = 0.2）→ Linear → ReLU → Linear → Sigmoid，輸出範圍 0 至 1 的連續品質分，乘以 100 即得 0 至 100 分。訓練時分類頭與評分頭同步優化。

需特別說明的是，現行品質分輔助頭以「等級編號之線性轉換」（A=100, B=80, ..., F=0）作為迴歸目標，**隱含假設等級間距相等且 ordinal 關係由 MSE loss 隱式建模**。嚴格而言，本研究將 ordinal classification 任務以「nominal classification + auxiliary regression」近似處理，未採用 ordinal-aware loss（如 CORAL [@caoRankConsistentOrdinal2020]、CORN [@shiDeepNeuralNetworks2023]）或 ordinal regularization。此為方法層級之簡化，列入 \ref{sec:conclusion-future} 節後續研究方向。

本研究依不同的資料切分與策略組合進行多組訓練（如表 \ref{tab:training-scripts} 所示）。其中採用分組切分（Group Split）的簡化設定（MobileNetV3-Large）為本研究之主要結果來源，其餘為對照與歷史紀錄。

\begin{table}[H]
\centering
\caption{本研究各訓練設定之角色對照}
\label{tab:training-scripts}
\begingroup
\small
\setlength{\tabcolsep}{8pt}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{ccc}
\hline
\textbf{訓練設定} & \textbf{資料切分} & \textbf{在本研究之角色} \\
\hline
\makecell[c]{原完整\\候選策略} & \makecell[c]{隨機切分\\seed=7} & \makecell[c]{早期\\歷史對照} \\
\makecell[c]{原完整\\候選策略} & \makecell[c]{分組切分\\seed=7} & \makecell[c]{完整策略\\對照} \\
\makecell[c]{簡化\\策略} & \makecell[c]{分組切分\\多 seed} & \makecell[c]{主要結果\\與補充分析} \\
\hline
\end{tabular}
\endgroup
\end{table}

\noindent 表 \ref{tab:training-scripts} 中，隨機切分設定對應早期歷史結果；分組切分（Group Split）完整策略為完整候選策略之嚴格切分對照；分組切分多 seed 之簡化設定則負責多 seed、單變因消融、校準、Grad-CAM、PR/ROC、t-SNE 與外部未標注檢查等補充分析，並為本研究主要結果來源。

兩組策略（原完整 vs 簡化）使用相同骨幹、輸入尺寸、批次大小與輔助頭結構，僅差在分類損失與資料採樣方式：

\begin{equation}
\begin{aligned}
L_{\text{full}}  &= L_{\text{Focal}}(\gamma=2.0,\,\text{LS}=0.1) + 0.3 \times L_{\text{MSE}} \\
L_{\text{plain}} &= L_{\text{CE}} + 0.3 \times L_{\text{MSE}}
\end{aligned}
\label{eq:total-loss}
\end{equation}

\noindent 其中 $L_{\text{full}}$ 對應完整候選設定，$L_{\text{plain}}$ 對應簡化設定。

seed=7 詳細分析中，簡化設定於同一 Group Split 測試集取得 86.31\%（145/168），可作為後續混淆矩陣、校準與可視化的代表案例；但五 seed 重複後，簡化設定與完整設定在 accuracy / QWK 上未呈現顯著差異，因此本文不再將單次 86.31\% 解讀為策略穩定勝出，而是將其定位為可重現的嚴格切分基準。兩組設定之超參數整理於表 \ref{tab:hyperparameters}。

\begin{table}[H]
\centering
\caption{模型訓練超參數設定（兩組設定共用骨幹，差異標示於下方）}
\label{tab:hyperparameters}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
\hline
\textbf{超參數} & \textbf{設定值} & \textbf{說明} \\
\hline
骨幹模型 & \makecell{MobileNetV3-Large\\(ImageNet V2)} & 預訓練權重 \\
輸入尺寸 & 224$\times$224 px & --- \\
批次大小 & 32 & GPU 記憶體限制 \\
學習率 & $2\times10^{-4}$ & AdamW 初始值 \\
Weight Decay & $3\times10^{-4}$ & --- \\
學習率排程 & \makecell{CosineAnnealing\\WarmRestarts} & \makecell{$T_0=20$, $T_{\text{mult}}=2$\\$\eta_{\min}=10^{-6}$} \\
Dropout & \makecell{分類頭 $p=0.4$\\評分頭 $p=0.2$} & \makecell{兩組\\共用} \\
訓練精度 & FP16 Mixed Precision & GPU 加速 \\
\hline
\multicolumn{3}{c}{\textit{＝＝ 兩組設定之差異 ＝＝}} \\
\hline
分類損失 & \makecell{原完整：Focal $\gamma=2.0$\\＋LS 0.1} & 候選策略 \\
         & 簡化：Cross Entropy            & 目前主要設定 \\
Mixup Alpha & \makecell{原完整：0.3\\簡化：0.0} & 批次層級線性混合 \\
過採樣 & \makecell{原完整：WeightedRandomSampler\\（0.75 次方反比）} & --- \\
       & 簡化：無加權，隨機洗牌 & --- \\
最大輪數 & \makecell{原完整：100\\簡化補充：25} & --- \\
EarlyStopping Patience & \makecell{原完整：35\\簡化補充：7} & 監控驗證準確率 \\
\hline
\end{tabular}

\TableNote{註：簡化補充實驗以較低訓練預算（25 epoch、patience=7）於同一 Group Split 評估，因此本文不將不同預算下的結果歸因於單一超參數差異。}
\end{table}

# 實驗結果與分析 {#sec:results}

## 資料集統計分析 {#sec:results-dataset}

本研究有效樣本共 1110 張，依品質等級分布如表 \ref{tab:dataset-dist} 及圖 \ref{fig:dataset-dist} 所示。A 等級（完美品）佔比最高，共 546 張；B 級 87 張、C 級 213 張、D 級 160 張、E 級 72 張、F 級 32 張。相較早期 214 張嚴重不平衡資料，本資料集已顯著補足 B、C、D、E、F 等瑕疵等級，使模型能學習較完整的輕微至嚴重拉絲特徵。

\begin{table}[H]
\centering
\caption{訓練資料集各等級分布}
\label{tab:dataset-dist}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccc}
\hline
\textbf{等級} & \textbf{名稱} & \textbf{張數} & \textbf{佔比(\%)} & \textbf{資料集內比例} \\
\hline
A & 完美品 & 546 & 49.2\% & \makecell{樣本數最多\\作為正常列印品質基準} \\
B & 良好品 & 87 & 7.8\% & 輕微邊界樣本 \\
C & 輕微拉絲 & 213 & 19.2\% & \makecell{拉絲開始明顯\\的主要過渡類別} \\
D & 中度拉絲 & 160 & 14.4\% & 中度瑕疵樣本已補足 \\
E & 嚴重拉絲 & 72 & 6.5\% & 嚴重瑕疵樣本 \\
F & 失敗品 & 32 & 2.9\% & \makecell{樣本基數最小\\仍建議持續補充} \\
\hline
\textbf{合計} & --- & \textbf{1110} & \textbf{100\%} & 本研究有效資料集 \\
\hline
\end{tabular}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.88\textwidth,height=0.7\textheight,keepaspectratio]{images/dataset-distribution.png}
\caption{資料集各等級樣本分布（左：張數，右：佔比圓餅圖）}
\label{fig:dataset-dist}
\end{figure}

## 主要結果一覽 {#sec:results-overview}

為方便讀者快速掌握本研究最關鍵之泛化指標，茲將主要結果集中呈現於表 \ref{tab:results-overview}。本論文之主要結果分為兩層：seed=7 嚴格 Group Split 作為詳細分析案例；五 seed mean $\pm$ std 則作為策略比較之穩定性判斷依據。

\clearpage

\begin{table}[H]
\centering
\caption{本研究主要結果一覽（seed=7 詳細案例與五 seed 穩定性對照）}
\label{tab:results-overview}
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{2.5cm}
                >{\centering\arraybackslash}p{1.75cm}
                >{\centering\arraybackslash}p{1.75cm}
                >{\centering\arraybackslash}p{2.35cm}
                >{\centering\arraybackslash}p{3.2cm}@{}}
\hline
\textbf{模型 / 設定} & \textbf{Acc} & \textbf{Macro-F1} & \makecell[c]{\textbf{QWK}\\\textbf{跨等級}} & \textbf{角色 / 成本} \\
\hline
\makecell[c]{\textbf{MobileNetV3-Large}\\\textbf{簡化}\\\textbf{(seed=7)}} & \textbf{86.31\%} & 0.791 & \makecell[c]{0.932\\3.0\%} & \makecell[c]{詳細案例\\混淆矩陣/校準/Grad-CAM\\6.90 ms} \\
\makecell[c]{MobileNetV3-Large\\簡化\\(5 seeds)} & 81.19 $\pm$ 3.71\% & 0.661 $\pm$ 0.079 & \makecell[c]{\textbf{0.921} $\pm$ 0.009\\\textbf{3.10} $\pm$ 0.27\%} & \makecell[c]{accuracy 並列最高\\6.6 min} \\
\makecell[c]{MobileNetV3-Large\\完整\\(5 seeds)} & 80.12 $\pm$ 5.98\% & \textbf{0.713} $\pm$ 0.070 & \makecell[c]{0.909 $\pm$ 0.039\\3.45 $\pm$ 1.70\%} & \makecell[c]{macro-F1 較高\\$p=0.0246$\\20.0 min} \\
\makecell[c]{ResNet18\\完整\\(5 seeds)} & 80.83 $\pm$ 2.16\% & 0.712 $\pm$ 0.057 & \makecell[c]{0.914 $\pm$ 0.032\\3.33 $\pm$ 1.91\%} & \makecell[c]{macro-F1 較高\\$p=0.0363$\\23.9 min} \\
\makecell[c]{EfficientNet-B0\\完整\\(5 seeds)} & \textbf{81.19} $\pm$ 2.25\% & 0.698 $\pm$ 0.031 & \makecell[c]{0.910 $\pm$ 0.039\\3.57 $\pm$ 2.10\%} & \makecell[c]{accuracy 與簡化相同\\差異不顯著\\24.3 min} \\
\makecell[c]{MobileNetV3-Large\\完整\\隨機切分基準} & 83.23\% & --- & --- & \makecell[c]{歷史對照\\不作為 Group Split\\策略優劣依據} \\
\hline
\end{tabular}
\end{adjustbox}
\TableNote[0.96\textwidth]{註：5 seeds 使用 seed = 7, 42, 123, 1234, 2024；成本欄為單次訓練平均時間（NVIDIA GeForce RTX 3050 Laptop GPU）。paired t-test 顯示相對 MobileNetV3-Large 簡化，其他模型在 accuracy 與 QWK 皆未達顯著差異；MobileNetV3-Large 完整與 ResNet18 完整在 macro-F1 上顯著較高。}
\end{table}

詳細各等級結果、混淆矩陣、品質分校準、模型校準、Grad-CAM 與外部未標注檢查見後續各節。本論文後續呈現順序為：先以 §\ref{sec:results-tensorboard} 至 \ref{sec:results-batch} 鋪陳訓練監控、舊版基準與隨機切分歷史對照，再於 \ref{sec:results-supplemental} 節完整展開主要結果之 Group Split、多 seed、消融與可視化分析，最後於 \ref{sec:results-comparison} 節做多版本綜合對照。**急於了解主要結果之讀者可直接跳至 \ref{sec:results-supplemental} 節**。

## TensorBoard 訓練過程監控 {#sec:results-tensorboard}

本研究以 TensorBoard 記錄訓練、驗證與測試過程，但正文不再逐張放置所有監控畫面，而改以關鍵數據與趨勢說明呈現。完整截圖可作為實驗查核資料保存，不必全部置於正文。

隨機切分基準模型最高驗證準確率為 90.96\%，獨立測試集準確率為 83.23\%，全資料集回測準確率為 95.86\%（1064/1110）。其中，全資料集回測用於確認模型對已標注資料的整體擬合與批量辨識能力；獨立測試集準確率則用於觀察模型在未參與訓練樣本上的泛化表現。兩者目的不同，不能混為同一個效能指標。

訓練階段使用 Mixup 資料增強，因此訓練準確率會在混合樣本與軟標籤條件下計算，不能直接與未混合的驗證準確率作等值比較。本研究以驗證集、測試集與全資料集回測三種角度交叉檢視模型表現，避免只依單一曲線判斷模型好壞。

### 訓練曲線趨勢說明 {#sec:results-tensorboard-trend}

訓練曲線的重點不是截圖數量，而是收斂趨勢與泛化落差。從紀錄可知，模型在訓練後期仍維持約 89\% 至 91\% 的驗證表現，顯示資料擴充與正則化策略對少數類別辨識有幫助。然而訓練準確率偏低並不代表模型未學習，因為 Mixup 會使訓練標籤成為軟標籤，準確率指標本身會被混合比例影響。

因此，本研究後續分析以混淆矩陣、各等級召回率、測試集準確率與全資料集回測結果作為主要依據。TensorBoard 截圖僅作為實驗紀錄來源，不再於正文逐張展示。

### Group Split 補充實驗訓練曲線 {#sec:results-tensorboard-supplemental}

本研究之三組補充實驗（MobileNetV3-Large 簡化、ResNet18 完整、EfficientNet-B0 完整）使用相同 Group Split 切分、25 epoch 上限與 patience=7 之 Early Stopping。三模型之驗證集收斂曲線匯出後並排呈現如圖 \ref{fig:gs-training-curves} 所示。

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth,height=0.7\textheight,keepaspectratio]{images/gs-training-curves.png}
\caption{Group Split 補充實驗驗證集收斂曲線（左：驗證準確率；右：驗證損失）}
\label{fig:gs-training-curves}
\end{figure}

由曲線可觀察到三項細節：(1) **三模型皆在 5 至 10 epoch 內驗證準確率即衝至 80\% 以上**，顯示 ImageNet 預訓練權重對小樣本任務之遷移學習效果顯著；(2) **EfficientNet-B0 完整最早收斂**（第 4 個 logging step 即達最佳 86.31\% 驗證準確率，總計 12 epoch 後 Early Stopping），而 MobileNet 簡化於第 9 step 達最佳 85.12\%（17 epoch 後停止）、ResNet18 完整於第 11 step 達最佳 86.31\%（19 epoch 後停止）；(3) **三模型於收斂後期皆出現驗證準確率小幅波動**（如 ResNet18 從 86.31\% 回落至 83.33\%、MobileNet 簡化從 85.12\% 回落至 83.93\%），反映 batch size 32 下小資料集驗證準確率本身之 noise level。三者最佳驗證準確率僅相差約 1 個百分點，與測試集準確率差距（86.31\% 至 82.14\%）方向一致，但**所有差距皆落在驗證準確率波動幅度之內**。此再次支持 \ref{sec:results-supplemental-interpretation} 節之保守解讀。

## 舊版模型評估（MobileNetV3-Small，214 張不平衡資料） {#sec:results-old-model}

在完成全部樣本的重新標注前，本研究先以初版 MobileNetV3-Small 模型對早期的 214 張嚴重不平衡資料（A 級 181 張，B 至 F 級各 4 至 9 張）進行訓練，作為新版模型之歷史對照（**註：此處 214 張之整體準確率 86.9\% 為驗證/回測表現，舊版獨立測試集準確率為 78.79\%，詳見 \ref{sec:results-comparison} 節之多版本比較表 \ref{tab:multi-versions}**）。即使如此，舊版模型最致命的問題並非整體數字，而是少數類別之嚴重失能：D 等級 Precision 僅 0.304，整體 Macro F1 僅 0.708，顯示模型幾乎只會預測 A 等級，對 B 至 F 等級的辨識能力極為有限。詳細評估結果如表 \ref{tab:old-model} 所示。

\begin{table}[H]
\centering
\caption{舊版模型（MobileNetV3-Small，214 張）評估結果}
\label{tab:old-model}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccc}
\hline
\textbf{等級} & \textbf{樣本數} & \textbf{Precision} & \textbf{Recall} & \textbf{F1-score} \\
\hline
A 完美品 & 181 & 0.982 & 0.884 & 0.930 \\
B 良好品 & 5 & 0.500 & 0.800 & 0.615 \\
C 輕微拉絲 & 4 & 0.600 & 0.750 & 0.667 \\
D 中度拉絲 & 9 & 0.304 & 0.778 & 0.438 \\
E 嚴重拉絲 & 9 & 0.727 & 0.889 & 0.800 \\
F 失敗品 & 6 & 1.000 & 0.667 & 0.800 \\
\hline
macro avg & 214 & 0.686 & 0.795 & 0.708 \\
weighted avg & 214 & 0.925 & 0.869 & 0.888 \\
\hline
\end{tabular}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.7\textheight,keepaspectratio]{images/old-model-confusion-matrix.png}
\caption{舊版模型混淆矩陣（A$\to$D 誤判 16 張為主要問題）}
\label{fig:old-confusion}
\end{figure}

舊版模型之完整混淆矩陣數字如表 \ref{tab:old-confusion-matrix} 所示。

\begin{table}[H]
\centering
\caption{舊版模型（MobileNetV3-Small，214 張）混淆矩陣（列為真實標籤，欄為預測標籤）}
\label{tab:old-confusion-matrix}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{cccccccc}
\hline
\textbf{真實 \textbackslash 預測} & A & B & C & D & E & F & 樣本數 \\
\hline
A 完美品   & \textbf{160} & 3 & 2 & \underline{\textbf{16}} & 0 & 0 & 181 \\
B 良好品   & 1 & \textbf{4} & 0 & 0 & 0 & 0 & 5 \\
C 輕微拉絲 & 0 & 0 & \textbf{3} & 0 & 1 & 0 & 4 \\
D 中度拉絲 & 2 & 0 & 0 & \textbf{7} & 0 & 0 & 9 \\
E 嚴重拉絲 & 0 & 1 & 0 & 0 & \textbf{8} & 0 & 9 \\
F 失敗品   & 0 & 0 & 0 & 0 & 2 & \textbf{4} & 6 \\
\hline
\textbf{合計} & 163 & 8 & 5 & 23 & 11 & 4 & \textbf{214} \\
\hline
\end{tabular}

\TableNote{註：對角線為正確分類數（粗體），底線標示主要錯誤（A→D 16 張，佔 A 級 8.8\%）。整體準確率 86.9\%（186/214），但 D 級 23 筆預測中僅 7 筆正確（Precision 0.304）；模型實質上將 16 張 A 級樣本誤判為 D 級，導致 D 級預測膨脹。}
\end{table}

由表 \ref{tab:old-confusion-matrix} 與圖 \ref{fig:old-confusion} 可看出，舊版混淆矩陣中 A 等級有 16 張（8.8\%）被誤判為 D 等級，是最主要的錯誤來源。分析其根本原因：D 等級的訓練樣本僅 9 張，模型無法從如此有限的樣本中學習到 D 等級的穩定特徵表示，導致模型將 D 等級的高置信度預測閾值設定得極低，許多 A 等級樣本因特徵向量與 D 等級過度重疊而被誤分。此外，B 等級（5 張）和 C 等級（4 張）的樣本數同樣嚴重不足，其 F1-score 分別僅 0.615 和 0.667。這些結果明確說明：在嚴重資料不平衡的條件下，即使採用 WeightedRandomSampler 等過採樣技術，若少數類別的樣本數低於臨界值（本研究估計約 20 至 30 張），模型效能仍無法有效提升，補充實際樣本才是根本解決之道。

## 改良版模型評估（MobileNetV3-Large，1110 張資料，隨機切分原完整策略） {#sec:results-new-model}

> **讀者提示**：本節為**隨機切分版本**之結果，作為歷史對照與資料擬合度觀察用途；本研究之策略比較以 \ref{sec:results-supplemental} 節之 Group Split、多 seed 與消融結果為準，seed=7 簡化設定 86.31\% 則作為詳細混淆矩陣與校準分析案例。

完成 1110 張有效樣本的重新整理並採用升級的 MobileNetV3-Large 模型後，**隨機切分獨立測試集（167 筆）整體準確率為 83.23\%（139/167）**，詳細各等級表現見 \ref{sec:results-new-model-testset} 節。作為訓練擬合度參考，全資料集回測整體準確率為 95.86\%（1064/1110），各等級全資料集辨識正確率分別為 A 級 98.7\%、B 級 92.0\%、C 級 96.7\%、D 級 90.6\%、E 級 88.9\%、F 級 93.8\%；但因此回測包含已參與訓練的樣本，**不能視為模型於未見過資料上的真實表現，僅供觀察模型對已標注資料的整體擬合與批量辨識完成度**。全資料集詳細結果如表 \ref{tab:new-model} 所示，獨立測試集結果見表 \ref{tab:new-model-testset}。

\begin{table}[H]
\centering
\caption{隨機切分原完整策略模型（MobileNetV3-Large）全資料集回測各等級表現（含訓練資料，僅供擬合度參考，非泛化指標）}
\label{tab:new-model}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccccc}
\hline
\textbf{等級} & \textbf{樣本數} & \textbf{正確數} & \textbf{Recall} & \textbf{預測平均} & \textbf{目標分數} & \textbf{誤差} \\
\hline
A 完美品 & 546 & 539 & 98.7\% & 79.4 分 & 100 分 & $-20.6$ 分 \\
B 良好品 & 87 & 80 & 92.0\% & 69.7 分 & 80 分 & $-10.3$ 分 \\
C 輕微拉絲 & 213 & 206 & 96.7\% & 57.5 分 & 60 分 & $-2.5$ 分 \\
D 中度拉絲 & 160 & 145 & 90.6\% & 49.8 分 & 40 分 & $+9.8$ 分 \\
E 嚴重拉絲 & 72 & 64 & 88.9\% & 37.4 分 & 20 分 & $+17.4$ 分 \\
F 失敗品 & 32 & 30 & 93.8\% & 28.5 分 & 0 分 & $+28.5$ 分 \\
\hline
\textbf{整體} & \textbf{1110} & \textbf{1064} & \textbf{95.86\%} & \makecell{66.0 分\\（weighted）}& --- & --- \\
\hline
\end{tabular}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth,height=0.7\textheight,keepaspectratio]{images/new-model-accuracy-comparison.png}
\caption{改良版模型各等級準確率（左）及新舊版對比（右）}
\label{fig:new-model-acc}
\end{figure}

### 獨立測試集表現（泛化能力主要指標） {#sec:results-new-model-testset}

獨立測試集共 167 筆未參與訓練之樣本，整體準確率 83.23\%（139/167）。**此為本研究評估模型泛化能力之主要量化指標**，相對於全資料集回測 95.86\%（表 \ref{tab:new-model}），可看出兩者落差約 12.6 個百分點，且少數類別之落差更為顯著。詳細結果如表 \ref{tab:new-model-testset} 所示。

\begin{table}[H]
\centering
\caption{隨機切分原完整策略模型（MobileNetV3-Large）獨立測試集各等級表現}
\label{tab:new-model-testset}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccc}
\hline
\textbf{等級} & \textbf{測試樣本數} & \textbf{測試準確率} & \makecell{\textbf{全資料集}\\\textbf{回測 Recall}} & \textbf{落差（pp）} \\
\hline
A 完美品   & 82 & 98.8\%（81/82）& 98.7\% & $-0.1$（穩定）\\
B 良好品   & 13 & 53.8\%（7/13） & 92.0\% & $-38.2$（嚴重）\\
C 輕微拉絲 & 32 & 87.5\%（28/32）& 96.7\% & $-9.2$ \\
D 中度拉絲 & 24 & 54.2\%（13/24）& 90.6\% & $-36.4$（嚴重）\\
E 嚴重拉絲 & 11 & 54.5\%（6/11） & 88.9\% & $-34.4$（嚴重）\\
F 失敗品   & 5  & 80.0\%（4/5）  & 93.8\% & $-13.8$ \\
\hline
\textbf{整體} & \textbf{167} & \textbf{83.23\%（139/167）} & \textbf{95.86\%（1064/1110）} & $-12.6$ \\
\hline
\end{tabular}

\TableNote{註：落差以百分比點（pp）計算 = 測試準確率 − 全資料集回測 Recall。各等級測試樣本數依資料切分比例隨機分配，B、E、F 三類基數僅 5 至 13 張，單一誤判即可造成顯著百分比變化，解讀時須與樣本數一併考量。}
\end{table}

**重要解讀**：

1. **A 級辨識穩定**（98.8\%，落差僅 −0.1 pp），代表正常列印品在實際部署可被穩定辨識。
2. **B、D、E 三個少數類別於獨立測試集準確率全部跌至 50\% 左右**，落差超過 30 個百分點。這顯示模型在這些等級上**有嚴重過擬合**：全資料集回測時看似 88 至 92\%，但實際部署到未見樣本時近乎隨機猜測。
3. **C、F 等級落差中等**（−9 至 −14 pp），仍可作為輔助分級，但需以人工複核補強。
4. **此落差來源**綜合包含：(a) F 級樣本基數過小（32 張），(b) 同一原圖切出之多支魚骨在訓練/測試間相關性高（此為隨機切分情境下之資料洩漏風險，Group Split 重訓結果詳見 \ref{sec:results-supplemental} 節），(c) 標注一致性未驗證可能引入雜訊。後續補強方向詳見 \ref{sec:conclusion-future} 節。

### 評估結果整體討論 {#sec:results-new-model-discussion}

本節以表 \ref{tab:new-model}、圖 \ref{fig:new-model-acc} 與下一節混淆矩陣分析作為主要證據。完整分類報告與 TensorBoard 測試截圖保留於實驗資料夾與 HTML 報告中，可供後續查核。

從評估結果看，改良版 MobileNetV3-Large **在獨立測試集（167 筆未參與訓練之樣本）準確率為 83.23\%，此為本研究評估泛化能力之主要指標**。全資料集回測準確率 95.86\% 雖然數字較高，但因樣本已參與訓練，僅能反映模型對已標注資料之擬合度，**不可解讀為實際部署時的保證準確率**。83.23\% 與 95.86\% 之間約 12.6 個百分點的落差，顯示模型在少數等級與邊界樣本上仍存在泛化限制；尤其 B、D、E 三個少數類別於獨立測試集準確率僅 53.8\%、54.2\%、54.5\%（詳見 \ref{sec:results-new-model-testset} 節），代表這些等級在實際部署時的可靠性與全資料集回測呈現之表象存在巨大落差，後續研究應優先補強。

## 混淆矩陣深度分析 {#sec:results-confusion}

以下以隨機切分基準模型之混淆矩陣作為主要分析依據，說明各品質等級的辨識穩定性與主要混淆來源（Group Split 嚴格切分之簡化設定混淆矩陣詳見 \ref{sec:results-supplemental-classes} 節）。

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.7\textheight,keepaspectratio]{images/new-model-confusion-matrix.png}
\caption{隨機切分基準模型混淆矩陣（1110 張全資料集回測，含訓練樣本）}
\label{fig:new-confusion}
\end{figure}

由圖 \ref{fig:new-confusion} 之評估結果可觀察到以下趨勢：

1. A 等級共 546 張，準確率 98.7\%，完美品辨識最穩定。
2. B 等級共 87 張，準確率 92.0\%，與 A/C 邊界仍為主要混淆來源。
3. C 等級共 213 張，準確率 96.7\%，已具備穩定辨識能力。
4. D 等級共 160 張，準確率 90.6\%，較前版 77.8\% 明顯改善。
5. E 等級共 72 張，準確率 88.9\%。
6. F 等級共 32 張，準確率 93.8\%，但樣本數仍偏少，未來仍建議持續補充嚴重失敗樣本。

### 誤判案例類型分析 {#sec:results-confusion-error}

誤判案例以類型分析為主，主要錯誤可分為三類。

**第一**，A 級與 B 級之間的混淆，多發生在魚骨細刺附近有極短細絲時；模型可能將光線、陰影或短絲解讀為輕微瑕疵。

**第二**，C 級與 D 級之間的混淆，主要來自拉絲面積比例接近臨界值，尤其當拉絲集中於局部區域時，模型對整體嚴重程度的判定會產生偏差。

**第三**，E 級與 F 級之間的混淆，與嚴重失敗樣本數不足有關，模型較難穩定學習結構崩壞與嚴重拉絲的邊界。

這些誤判顯示，本研究的主要瓶頸不只在模型架構，也在標注準則與邊界樣本數量。後續若要提升 B/C、C/D 與 E/F 邊界辨識能力，應優先補充邊界樣本，並建立更明確的複核規則，而不是單純增加訓練輪數。

### 正確辨識案例特徵歸納 {#sec:results-confusion-correct}

正確辨識案例的功能是說明模型在典型樣本上的判斷能力，以下以文字歸納各等級正確辨識的特徵：A 級樣本通常具有乾淨輪廓與清楚魚骨間隙；B 級樣本可能存在少量短絲但不影響整體品質；C 與 D 級樣本的差異主要在拉絲覆蓋比例與連續性；E 與 F 級樣本則呈現大範圍拉絲或結構難以辨識。

從正確案例可看出，模型對典型 A、C、D 與 F 級具有較明確的特徵反應；較不穩定的區域仍集中在相鄰等級的邊界樣本。這與前述混淆矩陣分析一致，也支持後續以邊界樣本補充與標注一致性檢查作為改善方向。

## 品質評分系統分析 {#sec:results-quality-score}

品質評分輔助頭的輸出如表 \ref{tab:new-model} 所示（隨機切分基準之全資料集回測；簡化設定品質分校準另見表 \ref{tab:plain-quality-score}）。表 \ref{tab:grading-criteria} 中的目標分數為人工定義之等級基準，表 \ref{tab:new-model} 則為模型回歸頭輸出的預測平均分，兩者尚未經校準，因此數值不必完全相同。隨機切分基準全資料集平均品質分為 66.0 分；各等級平均分依 A 至 F 呈現遞減趨勢，分別為 A 級 79.4 分、B 級 69.7 分、C 級 57.5 分、D 級 49.8 分、E 級 37.4 分、F 級 28.5 分。預測平均分可作為比六等級分類更細緻的品質量化工具，例如以品質分 65 分為門檻，低於此值的列印件建議重新列印或進行後處理。比較結果如圖 \ref{fig:quality-score} 所示。

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth,height=0.7\textheight,keepaspectratio]{images/quality-score-comparison.png}
\caption{各等級目標品質分與模型輸出平均分比較}
\label{fig:quality-score}
\end{figure}

## 批量辨識系統實測 {#sec:results-batch}

本研究將訓練完成的隨機切分基準模型整合至批量辨識流程，對 1110 支魚骨樣本進行自動辨識，結果如表 \ref{tab:batch-result} 及圖 \ref{fig:batch-result} 所示。此次批量辨識的輸入為既有的已標注資料集（未納入 105 張外部未標注照片），系統將辨識結果依等級分類整理，並在每張裁切圖右上角標示等級，同時產生統計圖。本批量辨識輸出分布為 A 級 544 張、B 級 89 張、C 級 215 張、D 級 156 張、E 級 72 張、F 級 34 張；該流程以原圖 2 欄 $\times$ 3 列裁切後再推論，故與 \ref{sec:results-new-model} 節之全資料集回測（已標注樣本逐張輸入）流程不同，預測分布略有差異。

\begin{table}[H]
\centering
\caption{批量辨識 1110 支魚骨結果統計}
\label{tab:batch-result}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccc}
\hline
\textbf{等級} & \textbf{名稱} & \textbf{辨識支數} & \textbf{佔比(\%)} & \textbf{說明} \\
\hline
A & 完美品 & 544 & 49.0\% & 多數列印件品質良好 \\
B & 良好品 & 89 & 8.0\% & \makecell{A/B 邊界樣本\\略有混淆} \\
C & 輕微拉絲 & 215 & 19.4\% & \makecell{輕微瑕疵\\主要輸出類別} \\
D & 中度拉絲 & 156 & 14.1\% & \makecell{中度拉絲樣本\\穩定辨識} \\
E & 嚴重拉絲 & 72 & 6.5\% & 嚴重瑕疵樣本 \\
F & 失敗品 & 34 & 3.1\% & 失敗品樣本數較少 \\
\hline
\textbf{合計} & --- & \textbf{1110} & \textbf{100\%} & 本批量辨識結果 \\
\hline
\end{tabular}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth,height=0.7\textheight,keepaspectratio]{images/batch-result-distribution.png}
\caption{批量辨識各等級支數分布統計圖}
\label{fig:batch-result}
\end{figure}

### 端對端辨識流程的實際意義 {#sec:results-batch-pipeline}

本節說明端對端流程之實際意義：系統將 1110 支魚骨樣本依模型預測結果分入 A 至 F 資料夾，並產生統計圖與 HTML 報告。此流程之價值在於快速提供批次品質概況，讓使用者先掌握異常等級分布，再針對低品質或邊界樣本進行人工複核。

本批量輸出分布為 A 級 544 張、B 級 89 張、C 級 215 張、D 級 156 張、E 級 72 張、F 級 34 張。需特別說明：此批量辨識的 1110 張輸入即為訓練/驗證集，故輸出分布與人工標注資料集分布相近實屬必然，**此結果僅能驗證系統可正常完成端對端流程，不能視為對模型泛化能力的獨立驗證**。對泛化能力的真實評估仍應以 \ref{sec:results-supplemental} 節之 Group Split 嚴格測試集結果為主，\ref{sec:results-new-model-testset} 節之隨機切分結果則作為歷史對照。

## Group Split 與補充消融、基準模型實驗 {#sec:results-supplemental}

### 實驗設計動機 {#sec:results-supplemental-design}

\ref{sec:results-new-model-testset} 節指出 B、D、E 三個少數類別於隨機切分測試集準確率僅 50\% 左右，並懷疑同源樣本相關性使模型藉由共享背景／光線取得偏高分數。為驗證此風險並補強審查上常被質疑的 baseline 與 ablation 缺口，本研究以分組隨機切分（Group Shuffle Split，以原圖為分組鍵，seed=7）重新切分資料，並補做三組對照實驗。共識別 185 個獨立原圖組，切分結果如表 \ref{tab:group-split-dist} 所示。

\begin{table}[H]
\centering
\caption{Group Split 測試集各等級分布（與隨機切分對照）}
\label{tab:group-split-dist}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccc}
\hline
\textbf{等級} & \textbf{名稱} & \makecell{\textbf{Group Split}\\\textbf{測試集}} & \makecell{\textbf{隨機切分}\\\textbf{測試集}} & \textbf{差異} \\
\hline
A & 完美品 & 77 & 82 & $-5$ \\
B & 良好品 & 16 & 13 & $+3$ \\
C & 輕微拉絲 & 35 & 32 & $+3$ \\
D & 中度拉絲 & 28 & 24 & $+4$ \\
E & 嚴重拉絲 & 8  & 11 & $-3$ \\
F & 失敗品   & 4  & 5  & $-1$ \\
\hline
\textbf{合計} & --- & \textbf{168} & \textbf{167} & $+1$ \\
\hline
\end{tabular}

\TableNote{註：Group Split 後訓練 774／驗證 168／測試 168，三集之原圖 ID 完全不重疊（已通過程式 assertion 驗證）。}
\end{table}

補充實驗共用 Group Split 切分、相同測試集（168 筆）、25 epoch 上限與 patience=7 之 Early Stopping，設定如表 \ref{tab:supplemental-experiment-design} 所示。所有實驗均保留品質分 MSE 輔助頭，差異集中在骨幹網路、損失函數、Mixup 與採樣策略；本節先呈現 seed=7 詳細結果，再以五個 seed 檢查差異是否穩定。seed=7 各模型訓練成本對照如表 \ref{tab:supplemental-train-cost} 所示。

\begin{table}[H]
\centering
\caption{seed=7 補充實驗之訓練成本對照（NVIDIA RTX 3050 Laptop GPU）}
\label{tab:supplemental-train-cost}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccc}
\hline
\textbf{模型 / 設定} & \makecell{\textbf{總訓練}\\\textbf{時間}} & \makecell{\textbf{平均每}\\\textbf{epoch}} & \makecell{\textbf{骨幹}\\\textbf{參數量}} & \textbf{相對成本} \\
\hline
\makecell{MobileNetV3-Large\\簡化} & 6.2 分鐘 & $\sim$14.9 秒 & $\sim$5.4M & \makecell{1.0$\times$\\（基準）}\\
\makecell{EfficientNet-B0\\完整} & 21.2 分鐘 & $\sim$50.9 秒 & $\sim$5.3M & 3.4$\times$ \\
\makecell{MobileNetV3-Large\\完整} & 27.5 分鐘 & $\sim$66.0 秒 & $\sim$5.4M & 4.4$\times$ \\
\makecell{ResNet18\\完整} & 31.2 分鐘 & $\sim$74.9 秒 & $\sim$11.7M & 5.0$\times$ \\
\hline
\end{tabular}

\TableNote{註：訓練時間含資料載入與 Early Stopping。完整策略主要額外成本來自 Weighted Random Sampler、Mixup 與較重的資料增強。}
\end{table}

\begin{table}[H]
\centering
\caption{補充消融與 baseline 實驗設計}
\label{tab:supplemental-experiment-design}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
\hline
\textbf{實驗} & \textbf{模型架構} & \textbf{訓練設定} \\
\hline
\shortstack{MobileNetV3-Large\\簡化設定} & \shortstack{MobileNetV3\\Large} & \shortstack{Cross Entropy +\\品質分 MSE 輔助頭\\未啟用 Focal Loss\\未啟用 Label Smoothing\\未啟用 Mixup\\未啟用 Weighted Random\\Sampler} \\
\shortstack{MobileNetV3-Large\\完整設定} & \shortstack{MobileNetV3\\Large} & \shortstack{Focal Loss\\Label Smoothing\\Mixup\\Weighted Random\\Sampler\\保留品質分 MSE 輔助頭} \\
\shortstack{ResNet18\\完整設定} & ResNet18 & \shortstack{Focal Loss\\Label Smoothing\\Mixup\\Weighted Random\\Sampler\\保留品質分 MSE 輔助頭} \\
\shortstack{EfficientNet-B0\\完整設定} & \shortstack{EfficientNet\\B0} & \shortstack{Focal Loss\\Label Smoothing\\Mixup\\Weighted Random\\Sampler\\保留品質分 MSE 輔助頭} \\
\hline
\end{tabular}
\end{table}

### Group Split 測試結果 {#sec:results-supplemental-results}

seed=7 之 Group Split 測試結果整理於表 \ref{tab:supplemental-experiment-results}。其中「MobileNetV3-Large 原完整」對應先前完整策略 Group Split 所得之歷史模型；其餘列在同一 Group Split 切分與 25 epoch 預算下重新訓練取得。

\begin{table}[H]
\centering
\caption{seed=7 補充消融與 baseline 在同一 Group Split 測試集之結果}
\label{tab:supplemental-experiment-results}
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{3.1cm}cccccc@{}}
\hline
\textbf{模型} & \textbf{Acc} & \textbf{Macro-F1} & \textbf{Weighted-F1} & \textbf{QWK} & \textbf{跨等級} & \textbf{時間} \\
\hline
\makecell[c]{MobileNetV3-Large\\完整設定（等預算）} & \textbf{89.88\%} (151/168) & \textbf{0.834} & \textbf{0.901} & \textbf{0.967} & \textbf{1.2\%} & 27.5 分 \\
\makecell[c]{MobileNetV3-Large\\簡化設定} & 86.31\% (145/168) & 0.791 & 0.859 & 0.932 & 3.0\% & 6.2 分 \\
\makecell[c]{ResNet18\\完整設定} & 84.52\% (142/168) & 0.783 & 0.851 & 0.954 & \textbf{1.2\%} & 31.2 分 \\
\makecell[c]{EfficientNet-B0\\完整設定} & 82.14\% (138/168) & 0.729 & 0.832 & 0.951 & \textbf{1.2\%} & 21.2 分 \\
\makecell[c]{MobileNetV3-Large\\原完整 checkpoint} & 82.74\% (139/168) & 0.740 & 0.830 & --- & --- & 100 epoch 歷史 \\
\hline
\end{tabular}
\end{adjustbox}

\TableNote[0.96\textwidth]{註：等預算完整設定與簡化設定為同一批補充實驗產生。MobileNetV3-Large 原完整模型保留為歷史對照，因訓練流程與 early stopping 設定不同，不納入策略優劣判定。}
\end{table}

以二項分布近似估計（Wilson 信賴區間），四組模型之測試準確率與 95\% 信賴區間如表 \ref{tab:ci-wilson} 所示。

\begin{table}[H]
\centering
\caption{Group Split 測試集準確率之 95\% Wilson 信賴區間}
\label{tab:ci-wilson}
\scriptsize
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.96\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{3.3cm}ccc@{}}
\hline
\textbf{模型} & \textbf{準確率} & \textbf{95\% Wilson CI} & \textbf{寬度} \\
\hline
\makecell[c]{MobileNetV3-Large\\完整（等預算）} & 89.88\% (151/168) & [84.4\%, 93.6\%] & 9.2 pp \\
\makecell[c]{MobileNetV3-Large\\簡化} & 86.31\% (145/168) & [80.3\%, 90.7\%] & 10.4 pp \\
ResNet18 完整 & 84.52\% (142/168) & [78.3\%, 89.2\%] & 10.9 pp \\
\makecell[c]{MobileNetV3-Large\\原完整 (best\_gs-v1)} & 82.74\% (139/168) & [76.4\%, 87.6\%] & 11.2 pp \\
EfficientNet-B0 完整 & 82.14\% (138/168) & [75.7\%, 87.2\%] & 11.5 pp \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

**值得特別注意的是，各模型之 95\% 信賴區間互相高度重疊**。因此單純就 seed=7 準確率而言，MobileNetV3-Large 完整 89.88\%、簡化 86.31\%、ResNet18 84.52\% 與 EfficientNet-B0 82.14\% 之排序仍可能受到切分與訓練隨機性影響；穩定性需以 \ref{sec:results-supplemental-multiseed} 節之多 seed 結果判斷。

#### Ordinal-aware 指標下之結論轉變 {#sec:results-supplemental-ordinal}

由於本研究為**有序等級分類任務**（A 至 F 為 ordinal label），accuracy 與 macro-F1 將「A→B」與「A→F」誤判視為等價懲罰，不反映 ordinal 任務本質。為補強此缺口，本研究從各模型混淆矩陣計算 Quadratic Weighted Kappa（QWK）、Cohen's Kappa 與「±1 等級容差」三項 ordinal-aware 指標，整理於表 \ref{tab:ordinal-metrics}。

\begin{table}[H]
\centering
\caption{seed=7 ordinal-aware 評估指標（同一 Group Split 168 筆測試集）}
\label{tab:ordinal-metrics}
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{3.0cm}cccccc@{}}
\hline
\textbf{模型} & \textbf{Acc} & \textbf{Macro-F1} & \textbf{QWK} & \textbf{Cohen's $\kappa$} & \textbf{相鄰誤判} & \textbf{跨等級誤判} \\
\hline
\makecell[c]{MobileNetV3-Large\\完整（等預算）} & \textbf{89.88\%} & \textbf{0.834} & \textbf{0.967} & \textbf{0.858} & 8.9\% & \textbf{1.2\%} \\
\makecell[c]{MobileNetV3-Large\\簡化} & 86.31\% & 0.791 & 0.932 & 0.803 & 10.7\% & 3.0\% \\
ResNet18 完整 & 84.52\% & 0.783 & 0.954 & 0.787 & 14.3\% & \textbf{1.2\%} \\
EfficientNet-B0 完整 & 82.14\% & 0.729 & 0.951 & 0.755 & 16.7\% & \textbf{1.2\%} \\
\hline
\multicolumn{7}{c}{\textit{參考：簡化設定全資料 1110 張回測（含訓練資料，僅供擬合度比較）}} \\
MobileNetV3-Large 簡化 (full) & 87.30\% & 0.779 & 0.953 & 0.812 & 11.2\% & 1.5\% \\
\hline
\end{tabular}
\end{adjustbox}

\TableNote[0.96\textwidth]{註：QWK（Quadratic Weighted Kappa）為 ordinal 任務之標準指標，將相鄰等級誤判懲罰減輕、跨等級誤判懲罰加重，1.0 為完美、0 為隨機。相鄰誤判定義為 $|i-j|=1$（如 A 預測為 B、C 預測為 B），跨等級誤判定義為 $|i-j| \geq 2$（如 A 預測為 D、F 預測為 C）。}
\end{table}

\noindent**關鍵觀察：seed=7 下，等預算完整策略同時提高 accuracy、macro-F1 與 QWK；但此排序仍需多 seed 檢查穩定性**。

* **Accuracy 排序**：MobileNetV3-Large 完整等預算 (89.88\%) > 簡化 (86.31\%) > ResNet18 完整 (84.52\%) > EfficientNet-B0 完整 (82.14\%)
* **QWK 排序**：MobileNetV3-Large 完整等預算 (0.967) > ResNet18 完整 (0.954) $\approx$ EfficientNet-B0 完整 (0.951) > 簡化 (0.932)
* **跨等級誤判排序**：MobileNetV3-Large 完整等預算、ResNet18 完整、EfficientNet-B0 完整皆為 1.2\%，低於簡化設定的 3.0\%

具體而言：**簡化策略 23 筆誤判中有 5 筆為跨等級誤判**（其中 D→A 屬於「將中度拉絲誤判為完美品」之高成本錯誤），而三組完整策略之跨等級誤判皆為 2 筆。這顯示完整正則化策略（Focal Loss + Label Smoothing + Mixup + Weighted Sampler）在 seed=7 下較能抑制「跨大幅度誤判」；此特性對品質管控應用尤為重要，因為將 D 級（建議重印）誤判為 A 級（直接使用）的成本，遠高於將 D 級誤判為 C 級的成本。

**因此，本研究之主要泛化結論需修正為**：早期「簡化勝過完整」來自特定 checkpoint 與單一 seed，經等預算與多 seed 補強後不宜再作為定論。較穩健的說法是：完整策略在 seed=7 與 macro-F1 上顯示價值，但五 seed accuracy / QWK 差異未達顯著；最終模型選擇仍應依下游應用對「整體正確率」、「少數類別 macro-F1」與「跨等級誤判成本」之權衡決定。

### 簡化設定各等級結果 {#sec:results-supplemental-classes}

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 簡化設定 Group Split 測試集各等級結果}
\label{tab:plain-class-results}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{cccccc}
\hline
\textbf{等級} & \textbf{正確數 / 樣本數} & \textbf{準確率} & \textbf{Precision} & \textbf{Recall} & \textbf{F1-score} \\
\hline
A 完美品   & 77/77 & 100.0\% & 0.917 & 1.000 & 0.957 \\
B 良好品   & 9/16  & 56.3\%  & 0.900 & 0.563 & 0.692 \\
C 輕微拉絲 & 27/35 & 77.1\%  & 0.900 & 0.771 & 0.831 \\
D 中度拉絲 & 23/28 & 82.1\%  & 0.719 & 0.821 & 0.767 \\
E 嚴重拉絲 & 6/8   & 75.0\%  & 0.750 & 0.750 & 0.750 \\
F 失敗品   & 3/4   & 75.0\%  & 0.750 & 0.750 & 0.750 \\
\hline
\end{tabular}
\end{table}

A 級於 Group Split 測試集達 100.0\%（77/77），相較隨機切分 98.8\% 略升，且未受同源樣本影響；D 級由隨機切分的 54.2\% 大幅提升至 82.1\%（23/28），E 級由 54.5\% 升至 75.0\%（6/8），E 與 D 之間的混淆明顯緩解。但 B 級僅 9/16（56.3\%），與隨機切分的 53.8\% 相近，仍為主要弱點；C 級由 87.5\% 降至 77.1\%，反映 C/D 邊界仍不穩定。E、F 類測試樣本各僅 8 與 4 張，單一樣本誤判即會造成顯著百分比變化，故百分比應與樣本數共同解讀。

#### 三模型各等級 F1-score 對照

\begin{table}[H]
\centering
\caption{三模型 Group Split 測試集各等級 F1-score 對照}
\label{tab:three-model-class-f1}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccc}
\hline
\textbf{等級} & \textbf{樣本} & \textbf{MobileNet 簡化} & \textbf{ResNet18 完整} & \textbf{EfficientNet-B0 完整} \\
\hline
A 完美品   & 77 & \textbf{0.957} & 0.945          & 0.952          \\
B 良好品   & 16 & 0.692          & 0.718          & \textbf{0.757} \\
C 輕微拉絲 & 35 & \textbf{0.831} & 0.829          & 0.831          \\
D 中度拉絲 & 28 & \textbf{0.767} & 0.755          & 0.667          \\
E 嚴重拉絲 & 8  & \textbf{0.750} & 0.700          & 0.500          \\
F 失敗品   & 4  & \textbf{0.750} & 0.750          & 0.667          \\
\hline
Macro-F1   & 168 & \textbf{0.791} & 0.783         & 0.729          \\
\hline
\end{tabular}
\end{table}

由表 \ref{tab:three-model-class-f1} 可觀察三項細節：(1) 在列入混淆矩陣細節的三組模型中，**MobileNet 簡化在多數等級（A、C、D、E、F）F1 最高**，但 B 級則由 EfficientNet-B0 完整領先（0.757 vs 簡化 0.692），反映完整策略之 Weighted Random Sampler 與 Focal Loss 對 B 類少數樣本提供額外幫助；(2) **EfficientNet-B0 完整於 E 級僅 0.500、D 級僅 0.667**，顯示其對中重度瑕疵之辨識能力較弱，可能與 compound scaling 對小樣本任務不利有關；(3) 結合表 \ref{tab:ordinal-metrics} 可知，完整策略對「跨等級誤判」更穩健，不能只依單一 accuracy 或 macro-F1 判斷最佳模型。

#### 三模型混淆矩陣對照

\begin{table}[H]
\centering
\caption{三模型 Group Split 測試集混淆矩陣（一）：MobileNetV3-Large 簡化（列為真實標籤，欄為預測標籤）}
\label{tab:three-model-confusion}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccccc}
\hline
真實 \textbackslash 預測 & A & B & C & D & E & F \\
\hline
A & \textbf{77} & 0 & 0 & 0 & 0 & 0 \\
B & 5 & \textbf{9} & 1 & 1 & 0 & 0 \\
C & 0 & 0 & \textbf{27} & 7 & 1 & 0 \\
D & \underline{2} & 1 & 2 & \textbf{23} & 0 & 0 \\
E & 0 & 0 & 0 & 1 & \textbf{6} & 1 \\
F & 0 & 0 & 0 & 0 & 1 & \textbf{3} \\
\hline
\end{tabular}
\TableNote{註：accuracy = 86.31\%，QWK = 0.932，跨等級誤判 5 筆；底線標示「D→A」之高成本跨等級誤判。}
\end{table}

\begin{table}[H]
\centering
\caption{三模型 Group Split 測試集混淆矩陣（二）：ResNet18 完整（列為真實標籤，欄為預測標籤）}
\label{tab:three-model-confusion-resnet}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccccc}
\hline
真實 \textbackslash 預測 & A & B & C & D & E & F \\
\hline
A & \textbf{69} & 8 & 0 & 0 & 0 & 0 \\
B & 0 & \textbf{14} & 1 & 1 & 0 & 0 \\
C & 0 & 1 & \textbf{29} & 4 & 1 & 0 \\
D & 0 & 0 & 5 & \textbf{20} & 3 & 0 \\
E & 0 & 0 & 0 & 0 & \textbf{7} & 1 \\
F & 0 & 0 & 0 & 0 & 1 & \textbf{3} \\
\hline
\end{tabular}
\TableNote{註：accuracy = 84.52\%，QWK = 0.954，跨等級誤判 2 筆。}
\end{table}

\begin{table}[H]
\centering
\caption{三模型 Group Split 測試集混淆矩陣（三）：EfficientNet-B0 完整（列為真實標籤，欄為預測標籤）}
\label{tab:three-model-confusion-efficientnet}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccccc}
\hline
真實 \textbackslash 預測 & A & B & C & D & E & F \\
\hline
A & \textbf{70} & 7 & 0 & 0 & 0 & 0 \\
B & 0 & \textbf{14} & 1 & 1 & 0 & 0 \\
C & 0 & 0 & \textbf{27} & 7 & 1 & 0 \\
D & 0 & 0 & 2 & \textbf{18} & 8 & 0 \\
E & 0 & 0 & 0 & 0 & \textbf{6} & 2 \\
F & 0 & 0 & 0 & 0 & 1 & \textbf{3} \\
\hline
\end{tabular}

\TableNote{註：對角線為正確分類數（粗體）；底線標示 MobileNet 簡化「D→A」之高成本跨等級誤判（將中度拉絲誤判為完美品 2 筆），此類錯誤在 ResNet18 / EfficientNet 完整策略中完全消失，是 QWK 反轉的主要原因。}
\end{table}

\noindent**跨模型誤判模式比較**：

* **MobileNet 簡化**：誤判集中於「B→A」5 筆、「C→D」7 筆、「D→A」2 筆。**D→A 為跨等級高成本錯誤**（將需重印之中度拉絲誤判為可直接使用之完美品），共 2 筆。
* **ResNet18 完整**：誤判集中於「A→B」8 筆、「D→C」5 筆、「D→E」3 筆，皆為相鄰等級誤判。**「A→B」反映 Label Smoothing 與 Mixup 使模型對完美品也保留一定的「可能稍有瑕疵」機率**，是完整策略 accuracy 略低之主因，但此類「過度保守」之誤判**不會造成嚴重品質決策錯誤**。
* **EfficientNet-B0 完整**：誤判模式類似 ResNet18，但「D→E」誤判增加為 8 筆（將中度拉絲誤判為嚴重拉絲），顯示其對中重度等級邊界較不穩定。

**結論**：在上述三組混淆矩陣中，簡化策略在「正確分類數」最多，但**犧牲了完整策略對「A 級嚴格性」的保守判定**。從品質管控觀點，「將 A 級誤判為 B 級」（建議用於略低品質要求）的成本，遠低於「將 D 級誤判為 A 級」（直接使用瑕疵品）的成本；因此完整策略的誤判分布更貼近實務需求。等預算 MobileNetV3-Large 完整設定之彙總指標另見表 \ref{tab:supplemental-experiment-results} 與 \ref{tab:ordinal-metrics}。

### 品質分校準（簡化設定） {#sec:results-supplemental-quality}

簡化設定品質分輔助頭之輸出，與目標分數的對應整理於表 \ref{tab:plain-quality-score}。Group Split 測試集平均與全資料集回測平均皆呈現 A $>$ B $>$ C $>$ D $>$ E $>$ F 的單調排序，因此具備輔助排序價值；但 D、E、F 等較差等級的平均分仍高於目標分數，B 級則出現品質分接近 89 而分類 recall 僅 0.563 之不一致，反映以「等級編號之線性轉換」作為連續監督目標時，回歸頭難以充分學習極端失敗特徵。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 簡化設定品質分對照}
\label{tab:plain-quality-score}
\scriptsize
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.96\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{1.8cm}
                >{\centering\arraybackslash}p{1.8cm}
                >{\centering\arraybackslash}p{1.9cm}
                >{\centering\arraybackslash}p{1.9cm}
                >{\centering\arraybackslash}p{3.5cm}@{}}
\hline
\textbf{等級} & \textbf{目標分數} & \textbf{Group Split} & \textbf{全資料回測} & \textbf{解讀} \\
\hline
A 完美品   & 100 分 & 99.6 分 & 99.5 分 & 接近目標，排序穩定 \\
B 良好品   & 80 分  & 89.0 分 & 88.3 分 & 略高估，且 B 類 recall 偏低 \\
C 輕微拉絲 & 60 分  & 58.8 分 & 60.5 分 & 接近目標 \\
D 中度拉絲 & 40 分  & 54.5 分 & 50.9 分 & 系統性偏高 \\
E 嚴重拉絲 & 20 分  & 23.5 分 & 30.8 分 & 樣本少，分數偏高 \\
F 失敗品   & 0 分   & 12.5 分 & 16.2 分 & 極端失敗樣本仍被高估 \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

### 簡化設定全資料回測 {#sec:results-supplemental-fullretest}

對 1110 張全資料以簡化設定 checkpoint 重新評估，整體準確率為 87.30\%（969/1110）、macro-F1 = 0.779、QWK = 0.953、Cohen's $\kappa$ = 0.812，各等級詳細指標如表 \ref{tab:plain-full-retest-class} 所示。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 簡化設定全資料回測各等級表現（1110 張，含訓練資料）}
\label{tab:plain-full-retest-class}
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{1.7cm}
                >{\centering\arraybackslash}p{1.8cm}ccccc@{}}
\hline
\textbf{等級} & \textbf{正確 / 樣本} & \textbf{Recall} & \textbf{Precision} & \textbf{F1-score} & \textbf{均分} & \textbf{目標} \\
\hline
A 完美品   & 546/546 & 1.000 & 0.937 & 0.967 & 99.5 & 100 \\
B 良好品   & 47/87   & 0.540 & 0.922 & 0.681 & 88.3 & 80 \\
C 輕微拉絲 & 177/213 & 0.831 & 0.894 & 0.861 & 60.5 & 60 \\
D 中度拉絲 & 138/160 & 0.863 & 0.687 & 0.765 & 50.9 & 40 \\
E 嚴重拉絲 & 39/72   & 0.542 & 0.750 & 0.629 & 30.8 & 20 \\
F 失敗品   & 22/32   & 0.688 & 0.880 & 0.772 & 16.2 & 0 \\
\hline
\textbf{整體} & \textbf{969/1110} & \textbf{0.873} & \textbf{0.877}\textsuperscript{*} & \textbf{0.868}\textsuperscript{*} & 66.5 & --- \\
\hline
\end{tabular}
\end{adjustbox}

\TableNote[0.96\textwidth]{$^*$ weighted average。註：B、E 兩等級 recall 較低（54.0\%、54.2\%）顯示「精度高、召回低」之模式 — 模型在預測為 B 或 E 時通常正確，但實際 B / E 樣本常被誤判為相鄰等級（B 多誤判為 A、E 多誤判為 D）。141 筆誤判中相鄰誤判 124 筆（11.2\%）、跨等級誤判僅 17 筆（1.5\%），QWK 0.953 高於 accuracy 87.30\% 即反映此分布。}
\end{table}

需特別強調：此回測包含已參與訓練的樣本，**不可解讀為部署準確率**；其與 95.86\%（隨機切分基準）、94.50\%（原完整 Group Split）並列時，**三者並非「同條件下的策略優劣比較」**。三者僅作擬合度量級比較，真正可比較泛化能力之指標仍須來自同一 Group Split 測試集與相同訓練預算下的實驗。

### 多 seed 穩定性與顯著性檢定 {#sec:results-supplemental-multiseed}

為檢查 seed=7 的模型排序是否穩定，本研究以 seed = 7, 42, 123, 1234, 2024 重複 Group Split、訓練與測試，並彙整 mean $\pm$ std 如表 \ref{tab:multiseed-results}。此表是本文判斷「策略是否穩定優於另一策略」的主要依據。

\begin{table}[H]
\centering
\caption{五個 seed 之 Group Split 測試表現（mean $\pm$ std, n=5）}
\label{tab:multiseed-results}
\scriptsize
\setlength{\tabcolsep}{2pt}
\renewcommand{\arraystretch}{1.12}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{2.35cm}ccccccc@{}}
\hline
\textbf{模型 / 設定} & \textbf{Acc} & \textbf{Macro-F1} & \textbf{Weighted-F1} & \textbf{QWK} & \textbf{$\pm 1$ 容差} & \textbf{跨等級} & \textbf{時間} \\
\hline
\makecell[c]{MobileNetV3-Large\\簡化} & 81.19 $\pm$ 3.71 & 0.661 $\pm$ 0.079 & 0.806 $\pm$ 0.038 & \textbf{0.921} $\pm$ 0.009 & \textbf{96.90} $\pm$ 0.27 & \textbf{3.10} $\pm$ 0.27 & \textbf{6.6} $\pm$ 1.0 \\
\makecell[c]{MobileNetV3-Large\\完整} & 80.12 $\pm$ 5.98 & \textbf{0.713} $\pm$ 0.070 & 0.806 $\pm$ 0.057 & 0.909 $\pm$ 0.039 & 96.55 $\pm$ 1.70 & 3.45 $\pm$ 1.70 & 20.0 $\pm$ 5.6 \\
ResNet18 完整 & 80.83 $\pm$ 2.16 & 0.712 $\pm$ 0.057 & 0.813 $\pm$ 0.022 & 0.914 $\pm$ 0.032 & 96.67 $\pm$ 1.91 & 3.33 $\pm$ 1.91 & 23.9 $\pm$ 4.8 \\
\makecell[c]{EfficientNet-B0\\完整} & \textbf{81.19} $\pm$ 2.25 & 0.698 $\pm$ 0.031 & \textbf{0.814} $\pm$ 0.025 & 0.910 $\pm$ 0.039 & 96.43 $\pm$ 2.10 & 3.57 $\pm$ 2.10 & 24.3 $\pm$ 3.3 \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

\begin{table}[H]
\centering
\caption{相對 MobileNetV3-Large 簡化之 paired t-test（n=5）}
\label{tab:paired-ttest}
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{2.8cm}cccccc@{}}
\hline
\textbf{比較模型} & \textbf{Acc 差異} & \textbf{Acc $p$} & \textbf{Macro-F1 差異} & \textbf{Macro-F1 $p$} & \textbf{QWK 差異} & \textbf{QWK $p$} \\
\hline
EfficientNet-B0 完整 & 0.00 pp & 1.000 & +0.038 & 0.295 & -0.011 & 0.540 \\
MobileNetV3-Large 完整 & -1.07 pp & 0.621 & +0.052 & \textbf{0.0246} & -0.011 & 0.502 \\
ResNet18 完整 & -0.36 pp & 0.745 & +0.052 & \textbf{0.0363} & -0.006 & 0.604 \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

多 seed 結果顯示，MobileNetV3-Large 簡化與 EfficientNet-B0 完整的平均 accuracy 皆為 81.19\%，且所有模型相對簡化設定之 accuracy / QWK 差異皆未達統計顯著。相較之下，MobileNetV3-Large 完整與 ResNet18 完整在 macro-F1 上顯著高於簡化設定，表示完整策略對少數類別或類別邊界較有幫助。換言之，**本文不再將「簡化策略最佳」視為穩定結論**；較合理的結論是：簡化策略成本最低且 QWK 平均略高，完整策略與 ResNet18 則在 macro-F1 上較佳。

### 單變因消融與等預算檢查 {#sec:results-supplemental-ablation}

為拆解完整策略中各技術的影響，本研究在 seed=7、同一 Group Split、25 epoch 預算下逐項移除 Focal Loss、Label Smoothing、Mixup 與 Weighted Random Sampler，結果如表 \ref{tab:single-factor-ablation}。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large seed=7 單變因消融結果}
\label{tab:single-factor-ablation}
\scriptsize
\setlength{\tabcolsep}{2pt}
\renewcommand{\arraystretch}{1.12}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{2.05cm}ccccccccc@{}}
\hline
\textbf{設定} & \textbf{Focal} & \textbf{LS} & \textbf{Mixup} & \textbf{Sampler} & \textbf{Acc} & \textbf{Macro-F1} & \textbf{QWK} & \textbf{跨等級} & \textbf{時間} \\
\hline
完整策略 & 有 & 有 & 有 & 有 & \textbf{89.88} & 0.834 & \textbf{0.967} & \textbf{1.19} & 27.5 分 \\
移除 Focal & 無 & 有 & 有 & 有 & 86.31 & 0.775 & 0.958 & \textbf{1.19} & 34.0 分 \\
移除 Label\newline Smoothing & 有 & 無 & 有 & 有 & 88.10 & \textbf{0.837} & 0.963 & \textbf{1.19} & 28.3 分 \\
移除 Mixup & 有 & 有 & 無 & 有 & 85.71 & 0.776 & 0.958 & \textbf{1.19} & 19.0 分 \\
移除 Sampler & 有 & 有 & 有 & 無 & 83.33 & 0.737 & 0.910 & 4.17 & 7.8 分 \\
簡化策略 & 無 & 無 & 無 & 無 & 86.31 & 0.791 & 0.932 & 2.98 & \textbf{6.2} 分 \\
簡化策略（100 epoch） & 無 & 無 & 無 & 無 & 86.31 & 0.791 & 0.932 & 2.98 & 13.8 分 \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

消融結果顯示，Weighted Random Sampler 是完整策略中對 ordinal 穩健性最關鍵的元件：移除 sampler 後 accuracy 降至 83.33\%、QWK 降至 0.910、跨等級誤判升至 4.17\%。移除 Label Smoothing 反而得到最高 macro-F1（0.837），表示 label smoothing 在此 seed 下可能略微壓抑少數類別的判別邊界。簡化策略延長至 100 epoch 並未改善 best checkpoint，支持 25 epoch 對簡化設定已足以達到本次訓練的最佳驗證點。

### 模型校準與不確定性 {#sec:results-supplemental-calibration}

對 seed=7 簡化 MobileNetV3-Large 進行 confidence calibration 後，未校準 ECE 為 0.0576；以 temperature scaling（$T=1.525$）校準後 ECE 降至 0.0435。高信心樣本（confidence $>0.9$）共有 112/168 張，準確率 95.5\%；低信心樣本（confidence $<0.7$）共有 28/168 張，準確率僅 46.4\%。這代表 confidence 可作為人機協作流程的實用訊號：高 confidence 結果可優先自動通過，低 confidence 結果則應進入人工複核。

\begin{figure}[H]
\centering
\begin{minipage}{0.48\textwidth}
\centering
\includegraphics[width=\textwidth,height=0.36\textheight,keepaspectratio]{images/calibration-reliability.png}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
\centering
\includegraphics[width=\textwidth,height=0.36\textheight,keepaspectratio]{images/calibration-confidence-hist.png}
\end{minipage}
\caption{seed=7 簡化模型之可靠度圖與 confidence 分布}
\label{fig:calibration-reliability}
\end{figure}

### PR / ROC 曲線與特徵分布 {#sec:results-supplemental-curves}

圖 \ref{fig:curves-pr-roc} 顯示 one-vs-rest PR 與 ROC 曲線。A 級與 C 級分離度較高（A 級 AP 0.997、C 級 AP 0.960），D、E、F 之 AP 較低（D 0.840、E 0.797、F 0.788），與少數類別及邊界瑕疵較難辨識的觀察一致。圖 \ref{fig:tsne-test-features} 則以 t-SNE 呈現測試集 penultimate features，可作為 A 至 F 類別在特徵空間中是否形成連續排序與局部混疊的輔助視覺化。

\begin{figure}[H]
\centering
\begin{minipage}{0.48\textwidth}
\centering
\includegraphics[width=\textwidth,height=0.36\textheight,keepaspectratio]{images/curves-pr.png}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
\centering
\includegraphics[width=\textwidth,height=0.36\textheight,keepaspectratio]{images/curves-roc.png}
\end{minipage}
\caption{seed=7 簡化模型之 PR 與 ROC 曲線}
\label{fig:curves-pr-roc}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.78\textwidth,height=0.7\textheight,keepaspectratio]{images/tsne-test-features.png}
\caption{Group Split 測試集特徵之 t-SNE 視覺化}
\label{fig:tsne-test-features}
\end{figure}

### Grad-CAM 定性檢查 {#sec:results-supplemental-gradcam}

為檢查模型是否可能依賴背景或光線 shortcut，本研究對 seed=7 簡化模型產生正確樣本與誤判樣本之 Grad-CAM 視覺化，如圖 \ref{fig:gradcam-correct} 與圖 \ref{fig:gradcam-wrong}。此分析僅屬定性檢查；由於本研究尚無像素級拉絲標註，不能將 heatmap 解讀為嚴格的因果或定位準確率。不過，Grad-CAM 可協助後續人工審查模型是否主要關注魚骨主體、拉絲區域或背景紋理。

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth,height=0.7\textheight,keepaspectratio]{images/gradcam-correct-grid.png}
\caption{正確分類樣本之 Grad-CAM 視覺化}
\label{fig:gradcam-correct}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth,height=0.7\textheight,keepaspectratio]{images/gradcam-wrong-grid.png}
\caption{誤判樣本之 Grad-CAM 視覺化}
\label{fig:gradcam-wrong}
\end{figure}

### 外部未標注影像 sanity check {#sec:results-supplemental-ood}

本研究另蒐集 105 張外部照片，將其切成 630 支魚骨後，以 seed=7 簡化模型推論並統計預測分布，如圖 \ref{fig:external-unlabeled-distribution}。預測數量為 A/B/C/D/E/F = 417/14/82/75/30/12，平均 confidence 為 0.920，其中 confidence $<0.7$ 者有 74 支。由於此批資料沒有人工標籤，**不能**據此計算 OOD accuracy；它的用途是檢查外部未標注照片是否出現大量低信心或異常輸出分布，並作為未來建立具標注 OOD 測試集的前置檢查。

\begin{figure}[H]
\centering
\includegraphics[width=0.78\textwidth,height=0.7\textheight,keepaspectratio]{images/external-unlabeled-distribution.png}
\caption{外部未標注照片推論分布與 confidence 檢查}
\label{fig:external-unlabeled-distribution}
\end{figure}

### 補充實驗的更新後解讀邊界 {#sec:results-supplemental-interpretation}

本節結果支持以下保守結論：

1. **同源樣本相關性並非本研究整體準確率的唯一來源**：Group Split 嚴格測試集在 seed=7 仍可達 86.31\%，且五 seed 平均約 80\% 至 81\%，顯示模型並非只靠同源背景記憶。
2. **單次 seed=7 排名不可直接推論為穩定最佳模型**：等預算 seed=7 下 MobileNetV3-Large 完整為最高，但五 seed 後 accuracy / QWK 未達顯著差異；因此本文只保留「完整策略較有利於 macro-F1」與「簡化策略成本最低」兩項較穩健觀察。
3. **Weighted Random Sampler 對跨等級錯誤控制最重要**：移除 sampler 後 QWK 與跨等級誤判明顯惡化，代表少數類別採樣仍是此資料集的核心問題。
4. **校準與 confidence 可轉化為實務流程**：低 confidence 子集準確率明顯較低，適合設計人工複核門檻。

仍未完成的關鍵限制包括：具人工標籤的 OOD 測試集、多位標注者一致性、ordinal-aware loss（如 CORAL [@caoRankConsistentOrdinal2020]、CORN [@shiDeepNeuralNetworks2023]）、以及 ResNet18 / EfficientNet-B0 在簡化策略下的全因子比較。換言之，本研究目前足以作為可重現基準與輔助原型，但仍不應宣稱可在跨機型、跨材料或跨拍攝條件下直接部署。

## 新舊版模型綜合比較 {#sec:results-comparison}

本研究於資料蒐集、標注與模型調整過程中進行多次訓練。為呈現模型效能隨資料量與訓練版本演進的變化，整理具完整全資料集評估紀錄之代表版本如表 \ref{tab:multi-versions} 所示；未完成或重複輸出的版本未列入比較。

\begin{center}
\begingroup
\small
\setlength{\tabcolsep}{3pt}
\setlength{\extrarowheight}{3pt}
\renewcommand{\arraystretch}{1.20}
\setlength{\LTleft}{\fill}
\setlength{\LTright}{\fill}
\newcommand{\mvcell}[1]{\parbox[c]{8.3cm}{\vspace{2pt}\centering\linespread{1.18}\selectfont #1\par\vspace{2pt}}}
\begin{longtable}{@{}cc@{}}
\caption{多次訓練結果比較}
\label{tab:multi-versions}\\
\hline
\textbf{訓練紀錄} & \mvcell{\textbf{指標與說明}} \\
\hline
\endfirsthead
\multicolumn{2}{c}{\textit{表 \ref{tab:multi-versions}（續）}} \\
\hline
\textbf{訓練紀錄} & \mvcell{\textbf{指標與說明}} \\
\hline
\endhead
\noalign{\vskip 6pt}
\hline
\endfoot
\makecell{二元分類\\（早期）} & \mvcell{資料量 214\\全資料 98.60\%\\測試 93.94\%\\驗證 96.88\%\\說明：早期二元分類器訓練紀錄\\（非六分類），資料量小\\結果易受資料切分影響} \\[3pt]
舊版基準 & \mvcell{資料量 214\\全資料 86.9\%\\測試 78.79\%\\驗證 84.38\%\\說明：舊版基準結果\\對應初期 214 張資料階段} \\[3pt]
擴充早期 & \mvcell{資料量 624\\全資料 89.90\%\\測試 79.79\%\\驗證 80.85\%\\說明：資料擴充至 624 張後\\早期訓練結果} \\[3pt]
擴充提升 & \mvcell{資料量 624\\全資料 93.75\%\\測試 82.98\%\\驗證 84.04\%\\說明：624 張資料階段\\整體準確率明顯提升} \\[3pt]
擴充最佳 & \mvcell{資料量 624\\全資料 94.39\%\\測試 86.17\%\\驗證 82.98\%\\說明：624 張資料階段\\最佳完整紀錄之一} \\[3pt]
中量初期 & \mvcell{資料量 984\\全資料 92.38\%\\測試 82.43\%\\驗證 72.97\%\\說明：984 張資料初期訓練\\驗證表現仍不穩定} \\[3pt]
中量最佳 & \mvcell{資料量 984\\全資料 95.02\%\\測試 87.16\%\\驗證 87.84\%\\說明：984 張資料階段最佳紀錄} \\[3pt]
全量過渡 & \mvcell{資料量 1110\\全資料 92.07\%\\測試 87.16\%\\驗證 87.84\%\\說明：資料擴充至 1110 張後\\過渡版本} \\[3pt]
全量中期 & \mvcell{資料量 1110\\全資料 91.44\%\\測試 82.63\%\\驗證 86.14\%\\說明：1110 張資料階段\\中期訓練紀錄} \\[3pt]
\makecell{隨機切分\\基準} & \mvcell{資料量 1110\\全資料 95.86\%\\測試 83.23\%\\驗證 90.96\%\\說明：隨機切分正式基準\\全資料集回測最高} \\[3pt]
\hline
\multicolumn{2}{>{\centering\arraybackslash}p{10.6cm}}{\textit{＝＝ Group Split 補充實驗\newline（測試集 168 筆，與訓練集零原圖重疊）＝＝}} \\
\hline
\makecell{分組切分\\完整首輪} & \mvcell{資料量 1110\\全資料 95.59\%\\測試 84.52\%\\驗證 86.9\%\\說明：完整策略首輪結果\\測試集 142/168} \\[3pt]
\makecell{分組切分\\完整對照} & \mvcell{資料量 1110\\全資料 94.50\%\\測試 82.74\%\\驗證 87.5\%\\說明：完整策略後續結果（同 seed）\\原完整策略主要對照\\測試集 139/168} \\[3pt]
\makecell{分組切分\\簡化（主要）} & \mvcell{資料量 1110\\全資料 87.30\%\\測試 \textbf{86.31\%}\\驗證 85.12\%\\說明：MobileNetV3-Large 簡化設定\\測試集 145/168} \\[3pt]
\makecell{分組切分\\完整等預算} & \mvcell{資料量 1110\\全資料 ---\\測試 \textbf{89.88\%}\\驗證 ---\\說明：MobileNetV3-Large 完整設定\\等預算重跑，seed=7\\測試集 151/168\\五 seed 後 accuracy 差異不顯著} \\[3pt]
\makecell{分組切分\\ResNet18} & \mvcell{資料量 1110\\全資料 ---\\測試 84.52\%\\驗證 86.31\%\\說明：ResNet18 完整設定 baseline\\測試集 142/168} \\[3pt]
\makecell{分組切分\\EfficientNet} & \mvcell{資料量 1110\\全資料 ---\\測試 82.14\%\\驗證 86.31\%\\說明：EfficientNet-B0 完整設定 baseline\\測試集 138/168} \\[3pt]
\hline
\end{longtable}
\TableNote{註：上半部各列為原隨機切分結果，其「測試準確率」為隨機切分獨立測試集；下半部分組切分各列為補充實驗結果，其「測試準確率」為 168 筆嚴格測試集。兩類測試集之原圖切分方式不同，不可直接視為同一指標。}
\endgroup
\end{center}

由表 \ref{tab:multi-versions} 可知，資料集由 214 張逐步擴充至 1110 張後，模型在不同訓練紀錄間呈現整體改善趨勢。早期 214 張之二元分類紀錄雖有較高數值，但屬二元分類（非六分類）階段，資料量小，結果易受切分方式與樣本分布影響，不宜與 1110 張完整資料集直接等量比較；在隨機切分各紀錄中，隨機切分基準的全資料集回測準確率 95.86\% 為最高，最高驗證準確率亦提升至 90.96\%。Group Split 補充實驗進一步顯示，seed=7 的模型排序會隨訓練預算與模型來源而改變，因此本文不再以單一列作為策略優劣定論，而是以 \ref{tab:multiseed-results} 之五 seed 結果作為穩定性判斷。

\begin{center}
\begingroup
\small
\setlength{\tabcolsep}{5pt}
\setlength{\extrarowheight}{3pt}
\renewcommand{\arraystretch}{1.22}
\setlength{\LTleft}{\fill}
\setlength{\LTright}{\fill}
\newcommand{\mccell}[1]{\parbox[c]{7.8cm}{\vspace{2pt}\centering\linespread{1.18}\selectfont #1\par\vspace{2pt}}}
\begin{longtable}{@{}cc@{}}
\caption{新舊版模型綜合比較}
\label{tab:model-comparison}\\
\hline
\textbf{比較項目} & \mccell{\textbf{舊版 / 改良版}} \\
\hline
\endfirsthead
\multicolumn{2}{c}{\textit{表 \ref{tab:model-comparison}（續）}} \\
\hline
\textbf{比較項目} & \mccell{\textbf{舊版 / 改良版}} \\
\hline
\endhead
\noalign{\vskip 6pt}
\hline
\endfoot
訓練樣本 & \mccell{舊版：214 張（嚴重不平衡）\\改良版：1110 張（重新標注）} \\[3pt]
模型架構 & \mccell{舊版：MobileNetV3-Small\\改良版：MobileNetV3-Large（ImageNet V2）} \\[3pt]
損失函數 & \mccell{舊版：CrossEntropy\\改良版簡化：Cross Entropy + 0.3 MSE（主要結果）\\改良版原完整：Focal $\gamma=2.0$ + LS 0.1 + 0.3 MSE} \\[3pt]
資料增強 & \mccell{舊版：基礎翻轉旋轉\\改良版簡化：標準增強，無 Mixup\\改良版原完整：標準增強 + Mixup $\alpha=0.3$} \\[3pt]
過採樣 & \mccell{舊版：Weighted Random Sampler\\改良版簡化：無\\改良版原完整：Weighted Random Sampler（0.75 次方反比）} \\[3pt]
\textbf{Group Split 測試集} & \mccell{舊版：---（舊版未做 Group Split）\\改良版 seed=7：86.31\%（145/168，簡化）\\改良版五 seed 平均：81.19\%（簡化 / EfficientNet-B0 並列）} \\[3pt]
隨機切分測試集 & \mccell{舊版：78.79\%（舊版基準）\\改良版：83.23\%（139/167，隨機切分基準歷史對照）} \\[3pt]
全資料集回測 & \mccell{舊版：86.9\%（186/214，含訓練樣本）\\改良版：95.86\%（1064/1110，隨機切分基準）\\改良版簡化：87.30\%（969/1110）} \\[3pt]
D 等級表現 & \mccell{舊版：Recall 77.8\%（Precision 僅 30.4\%）\\改良版：Group Split 測試集 82.1\%（23/28）} \\[3pt]
Macro F1 & \mccell{舊版：0.708（全資料估算）\\改良版：seed=7 簡化 0.791\\改良版五 seed：完整 MobileNet / ResNet18 較高} \\[3pt]
主要問題 & \mccell{舊版：A$\to$D 誤判 16 張\\改良版：B、E、F 測試樣本仍少（16、8、4 張）\\改良版：跨條件 OOD 尚缺人工標籤} \\[3pt]
\hline
\end{longtable}
\TableNote{註：Group Split 測試集為與訓練集零原圖重疊的嚴格測試集（168 筆）；隨機切分測試集為隨機切分基準歷史對照；全資料集回測包含訓練樣本，僅作為擬合度參考。三者不可互換解讀。}
\endgroup
\end{center}

# 結論與建議 {#sec:conclusion}

## 結論 {#sec:conclusion-summary}

本研究建立了一套以深度學習影像辨識為核心的 3D 列印件瑕疵自動辨識與品質評分系統，以 FDM 列印魚骨件的拉絲瑕疵為研究標的，實現六等級（A 至 F）自動分類與品質評分輸出。主要研究成果總結如下：

1. **單一標注者下之可重複品質等級制度**：以拉絲面積佔比為主要判斷依據，建立六個明確的品質等級定義並配合 A 至 F 範例圖。本研究主張的是「模型可學習並重現此套固定標注準則」，可降低批量檢查負擔並提供人工複核輔助；惟全部樣本由單一標注者完成、尚未進行多人一致性測試，故不宣稱已建立多人共識下的客觀品質標準（標注一致性限制詳見 \ref{sec:results-supplemental-interpretation} 節）。
2. **系統性資料蒐集與標注**：透過多批次列印與拍攝，配合 Label Studio 工具完成全部樣本的人工標注，建立含 1110 張有效樣本的六等級分類資料集。從 214 張嚴重不平衡的舊資料擴充至 1110 張後，**隨機切分獨立測試集整體準確率由 78.79\% 提升至 83.23\%**；進一步以 Group Split 嚴格切分重新訓練，seed=7 詳細案例可達 **86.31\%（145/168）**，五 seed 平均約 80\% 至 81\%，顯示模型已具備初步輔助分級能力，但單次切分結果不應過度外推。
3. **深度學習模型效能與不確定性**：以 MobileNetV3-Large（ImageNet V2 預訓練）為主，並補做完整 / 簡化策略、ResNet18 與 EfficientNet-B0 對照。五 seed 重複後，各模型平均 accuracy 均落在 80\% 至 81\%，accuracy 與 QWK 之 paired t-test 未達顯著差異；惟完整策略與 ResNet18 之 macro-F1 顯著高於簡化設定（詳見 \ref{sec:results-supplemental-multiseed} 節）。單變因消融顯示 Weighted Random Sampler 對 QWK 與跨等級誤判控制最關鍵；模型校準後低 confidence 子集準確率明顯偏低，適合作為人工複核門檻（詳見 \ref{sec:results-supplemental-calibration} 節）。故系統定位為「品質管控輔助原型」，而非可獨立判定之自動分級系統。
4. **端對端自動化流程**：整合自動裁切、批量辨識、分級輸出與 HTML 可視化報告，形成由原始照片到品質等級報告的離線批量處理流程；主要簡化模型於 RTX 3050 Laptop GPU 單張推論約 6.90 ms，驗證離線批量部署之可行性。惟此為單機離線量測，產線部署前仍需補做完整吞吐量、人工複核成本與現場穩定性評估。
5. **品質評分量化（未經人工校準）**：模型同時輸出 0 至 100 的連續品質分數。各等級平均分在 Group Split 測試集與全資料回測下均呈 A $>$ B $>$ C $>$ D $>$ E $>$ F 之單調遞減（數值詳見表 \ref{tab:plain-quality-score}），具輔助排序價值；惟目標分數採等級編號之線性轉換、未經多人主觀評分校準，B、D、E、F 等級之預測平均偏高，現階段僅作為分類結果之輔助連續指標，不宜作為絕對品質量化依據。

\vspace{0.5em}

**主要貢獻陳述（Take-home Message）**：

> 本研究為 FDM 魚骨拉絲瑕疵之小樣本影像分類提供可重現基準資料集（1110 張、A 至 F 六等級、Group Split 切分），並完成多 seed、單變因消融、模型校準、PR/ROC、t-SNE、Grad-CAM 與外部未標注照片 sanity check。核心結論是：單次 seed=7 的模型排序不足以宣稱某策略穩定最佳；五 seed 後，各模型 accuracy / QWK 差異未達顯著，而完整策略與 ResNet18 在 macro-F1 較有優勢。系統 6.90 ms/張之推論效率與端對端 pipeline 已驗證離線批量部署可行性，但在具標注 OOD、多人標注一致性與跨機型 / 跨材料驗證完成前，仍應定位為「品質管控輔助原型」。

## 建議 {#sec:conclusion-future}

根據本研究執行過程中的觀察與系統評估結果，提出以下建議供後續研究參考。其中第一項聚焦於尚未完成、且最直接影響部署可信度的驗證。

1. **【最高優先級】補齊部署可信度驗證**。本研究已完成 Group Split、多 seed、單變因消融、等預算比較、模型校準、PR/ROC、t-SNE、Grad-CAM 與外部未標注 sanity check；後續最需要補強的是下列四項：

   * **【未完成】具人工標籤的 OOD 測試集**：目前外部 105 張照片僅完成未標注推論分布與 confidence 檢查，不能計算 OOD accuracy。建議補拍並人工標注不同光源、背景、角度、相機之 30 至 50 張照片，量化模型對未見拍攝條件的退化幅度。
   * **【目前受限，保留為未來工作】標注一致性 Cohen's Kappa**：由於現階段無法取得第二位以上標注者重新標注，本文不計算也不推估 $\kappa$。若未來具備人力，建議重新標注 100 張涵蓋 A 至 F 之樣本並計算 Cohen's $\kappa$ / Fleiss' $\kappa$；若 $\kappa < 0.7$，需重新檢視標注準則並補充邊界判斷規則。
   * **【未完成】Ordinal-aware loss 對照**：本研究已補充 QWK、Cohen's $\kappa$ 與跨等級誤判率，但訓練目標仍是 nominal classification + MSE auxiliary regression。建議補做 CORAL [@caoRankConsistentOrdinal2020]、CORN [@shiDeepNeuralNetworks2023] 等 ordinal-aware loss，並以 QWK 與跨等級誤判率作為主要評估指標。
   * **【未完成】Baseline 架構 × 策略全因子設計**：目前尚缺 ResNet18 簡化、EfficientNet-B0 簡化等組合；若要分離「架構差異」與「訓練策略差異」，仍需完整 3 $\times$ 2 因子設計。
2. **持續補充少數等級訓練資料**。雖然本研究資料集中 D 級已達 160 張、E 級 72 張，但 F 級仍僅 32 張，且 B 級 87 張相較 A 級仍偏少，未來建議優先補充 B 級邊界樣本與 F 級失敗樣本，並將 F 等級資料補充至 50 張以上，使各等級樣本分布更平均，進一步降低 B/C 與 E/F 邊界的誤判，提高結果的統計可信度。
3. **擴充至翹曲與裂痕瑕疵的辨識**。本研究因翹曲和裂痕的現有樣本不足，聚焦於拉絲瑕疵的六等級分類。未來可系統性地蒐集翹曲及裂痕樣本，建立涵蓋三種瑕疵類型的多標籤分類系統（Multi-label Classification），更全面地反映 FDM 列印件的品質狀態。
4. **跨機型 / 跨材料 / 跨幾何泛化能力驗證**。本研究僅於 Bambu Lab A1 + PLA + 魚骨形狀條件下訓練與測試。建議蒐集：(a) 其他桌上型印表機（如 Prusa MK4、Creality K1）；(b) 其他材料（PETG、ABS、TPU）；(c) 其他幾何形狀（盒體、齒輪、有機曲面）之樣本，組成跨域測試集，量化模型於不同硬體 / 材料 / 幾何下之效能退化幅度。此項與第 1 項之 OOD 拍攝條件驗證互補，前者聚焦「列印物本身之變異」，後者聚焦「影像獲取條件之變異」，兩者皆為評估本系統作為通用品質管控工具之必要驗證。
5. **開發即時列印監控系統**。目前系統為列印完成後的離線批量辨識模式，未來可整合 Bambu Lab A1 的內建攝影機或外接 USB 相機串流，在列印進行中進行即時逐層品質監控，一旦偵測到嚴重拉絲（D 等級以上）即觸發警告並自動暫停列印，實現真正的閉環品質管控。
6. **優化品質評分模型的準確性**。目前品質分採用等級編號的線性轉換作為監督目標，較為粗糙。未來可邀請 5 至 10 名有經驗的操作人員對全部樣本進行主觀評分（連續值 0 至 100），以人工評分作為監督標籤，採用迴歸方式訓練更精確的評分頭，並計算模型輸出分數與人工評分的 ICC（組內相關係數）作為系統可信度的量化指標。
7. **模型輕量化與邊緣部署**。MobileNetV3-Large 模型大小約 21 MB，適合部署於桌上型電腦或工業電腦。若未來需部署於計算資源有限的邊緣裝置（如 Raspberry Pi 或 NVIDIA Jetson 系列），可進一步評估知識蒸餾、模型剪枝或 INT8 量化等壓縮方法；但任何壓縮方案都必須在相同資料切分下重新測試混淆矩陣、各等級召回率、品質分校準與推論時間，不能僅依模型大小推論精度與速度。

<!-- ============================================================ -->
<!-- 參考文獻（Pandoc + biblatex 自動產生） -->
<!-- ============================================================ -->

\newpage
\printbibliography[title=參考文獻]

<!-- ============================================================ -->
<!-- 附錄一　列印過程照片完整紀錄 -->
<!-- ============================================================ -->

\newpage

\appendix
\renewcommand{\thesection}{附錄\zhnum{section}}
\renewcommand{\thesubsection}{附\arabic{section}.\arabic{subsection}}
\renewcommand{\thesubsubsection}{附\arabic{section}.\arabic{subsection}.\arabic{subsubsection}}
\renewcommand{\thefigure}{附\arabic{section}-\arabic{figure}}
\renewcommand{\thetable}{附\arabic{section}-\arabic{table}}
\setcounter{figure}{0}
\setcounter{table}{0}

\titleformat{\section}{\normalsize}{\thesection}{1em}{}
\titlespacing*{\section}{2em}{12pt}{6pt}

# 列印過程代表性照片 {#sec:appendix-photos}

本附錄保留列印過程中四張代表性照片，分別對應「正常列印中」、「正常列印完成」、「輕微拉絲」、「列印失敗」四種典型狀態，作為前文等級定義之列印現場佐證。原始完整紀錄（共 16 張）一併保存於專案附件中供需要時查閱。

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.65\textheight,keepaspectratio]{images/print-process-01-normal.jpg}
\caption{典型「列印中、結構完整」狀態（灰色 PLA 魚骨）}
\label{fig:photo-print-normal}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.65\textheight,keepaspectratio]{images/print-process-05-good.jpg}
\caption{典型「列印完成、整齊」狀態（藍綠色 PLA 魚骨，對應 A 級樣本來源）}
\label{fig:photo-print-good}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.65\textheight,keepaspectratio]{images/print-process-10-light-stringing.jpg}
\caption{典型「列印中、輕微拉絲」狀態（藍色 PLA 魚骨，對應 C 級樣本來源）}
\label{fig:photo-print-light-stringing}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.65\textheight,keepaspectratio]{images/print-process-15-failed.jpg}
\caption{典型「列印失敗、嚴重拉絲」狀態（黃綠色 PLA 魚骨，對應 F 級樣本來源）}
\label{fig:photo-print-failed}
\end{figure}

# Bambu Lab A1 列印參數彙整 {#sec:appendix-params}

本研究全程使用同一組 Bambu Studio 列印參數設定（基於 PolyTerra PLA 0.08 mm 預設設定檔，未針對個別批次調整）。表 \ref{tab:param-summary} 彙整影響列印品質之關鍵參數值，圖 \ref{fig:param-quality-representative} 為品質頁籤之代表畫面。

\begin{table}[H]
\centering
\caption{Bambu Lab A1 列印參數彙整（全研究期間固定）}
\label{tab:param-summary}
\footnotesize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{1.4cm}
                >{\centering\arraybackslash}p{3.8cm}
                >{\centering\arraybackslash}p{2.4cm}
                >{\centering\arraybackslash}p{3.2cm}@{}}
\hline
\textbf{分類} & \textbf{參數項目} & \textbf{設定值} & \textbf{備註} \\
\hline
\multirow{6}{*}{品質} & 層高 & 0.08 mm & PolyTerra 預設 \\
                     & 首層層高 & 0.16 mm & \\
                     & 線寬（預設） & 0.42 mm & \\
                     & 線寬（首層） & 0.50 mm & \\
                     & 線寬（外牆/頂面/實心填充） & 0.42 mm & \\
                     & 線寬（內牆/稀疏填充/支撐） & 0.45 mm & \\
\hline
\multirow{2}{*}{接縫} & 接縫位置 & 背面 & 啟用智能斜拼接縫 \\
                     & 斜拼角度閾值 & 155$^\circ$ & 接縫間隔 15\% \\
\hline
\multirow{6}{*}{強度} & 牆層數 & 2 層 & 檢查薄壁啟用 \\
                     & 頂部殼體層數 / 厚度 & 9 層 / 0.8 mm & 頂面圖案：單調線 \\
                     & 底部殼體層數 & 7 層 & 底面圖案：單調 \\
                     & 內部實心填充圖案 & 直線 & 100\% 密度 \\
                     & 稀疏填充密度 / 圖案 & 5\% / 螺旋體 & 填充方向 45$^\circ$ \\
                     & 填充/牆重疊 & 15\% & \\
\hline
\end{tabular}
\end{adjustbox}
\TableNote[0.96\textwidth]{註：本表列出品質、接縫與強度設定；速度、支撐與其他設定續列於表 \ref{tab:param-summary-cont}。}
\end{table}

\begin{table}[H]
\centering
\caption{Bambu Lab A1 列印參數彙整（續）}
\label{tab:param-summary-cont}
\footnotesize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{1.4cm}
                >{\centering\arraybackslash}p{3.8cm}
                >{\centering\arraybackslash}p{2.4cm}
                >{\centering\arraybackslash}p{3.2cm}@{}}
\hline
\textbf{分類} & \textbf{參數項目} & \textbf{設定值} & \textbf{備註} \\
\hline
\multirow{8}{*}{速度} & 首層 / 首層填充 & 40 / 45 mm/s & \\
                     & 外牆 / 內牆 & 90 / 150 mm/s & \\
                     & 稀疏填充 & 225 mm/s & \\
                     & 內部實心填充 & 175 mm/s & \\
                     & 頂面 / 橋接 & 100 / 10 mm/s & 啟用懸垂降速 \\
                     & 支撐 / 支撐面 & 75 / 40 mm/s & \\
                     & 空駛速度 & 700 mm/s & \\
                     & 加速度（普通／空駛） & 6000 / 10000 mm/s$^2$ & \\
\hline
\multirow{2}{*}{支撐} & 開啟支撐 & 否 & 魚骨件全數不啟用支撐 \\
                     & 類型 / 筏層 & 普通（手動）/ 0 層 & 閾值角度 15$^\circ$ \\
\hline
\multirow{2}{*}{其他} & Skirt / Brim & 0 圈 / 無 brim & 擦料塔啟用 \\
                     & 耗材 & PolyTerra PLA & 直徑 1.75 mm \\
\hline
\end{tabular}
\end{adjustbox}
\TableNote[0.96\textwidth]{註：以上數值為 Bambu Studio「全局工藝」頁面 PolyTerra PLA 0.08 mm 預設檔之實際設定，全研究期間未做調整，使後續模型訓練可專注於拉絲嚴重程度差異。}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth,height=0.7\textheight,keepaspectratio]{images/bambu-studio-quality-tab.png}
\caption{Bambu Studio 品質頁籤代表截圖（層高 0.08 mm、線寬 0.42 mm）}
\label{fig:param-quality-representative}
\end{figure}

# PLA 耗材與冷卻設定彙整 {#sec:appendix-material}

本研究使用 Polymaker PolyTerra PLA 1.75 mm 線材，耗材物性、列印溫度與冷卻風扇策略於全研究期間固定。表 \ref{tab:material-summary} 彙整關鍵設定值，圖 \ref{fig:cooling-representative} 為冷卻模式設定代表畫面。

\begin{table}[H]
\centering
\caption{PolyTerra PLA 耗材與冷卻設定彙整（全研究期間固定）}
\label{tab:material-summary}
\footnotesize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.14}
\begin{adjustbox}{max width=0.98\textwidth,center}
\begin{tabular}{@{}>{\centering\arraybackslash}p{2.8cm}
                >{\centering\arraybackslash}p{2.8cm}
                >{\centering\arraybackslash}p{5.2cm}@{}}
\hline
\textbf{項目} & \textbf{設定值} & \textbf{備註} \\
\hline
耗材類型 / 供應商 & PLA / Polymaker & 配方 PolyTerra PLA \\
線材直徑 & 1.75 mm & --- \\
密度 / 流量比例 & 1.31 g/cm$^3$ / 0.98 & 預設值 \\
噴嘴溫度（首層 / 其它層）& 220 $^\circ$C / 220 $^\circ$C & 建議區間 190$\sim$240 $^\circ$C \\
熱床溫度（紋理 PEI）& 65 $^\circ$C & 首層與其它層相同 \\
最大體積速度 & 22 mm$^3$/s & 流量上限 \\
最小風扇速度閾值 & 60\%（層時間 80 秒）& 部件冷卻風扇 \\
最大風扇速度閾值 & 80\%（層時間 8 秒）& \\
風扇常開 & 啟用 & 全程保持冷卻 \\
冷卻減速邏輯 & 均勻冷卻 & 最小列印速度 20 mm/s \\
懸垂/橋接強制冷卻 & 啟用（風扇 100\%）& 冷卻懸空閾值 50\% \\
\hline
\end{tabular}
\end{adjustbox}
\TableNote[0.96\textwidth]{註：以上數值為 Bambu Studio「耗材絲設置」頁 Polymaker PolyTerra PLA \@BBL A1 預設值，全研究期間未做調整。此設計使噴嘴溫度、熱床溫度、冷卻風扇策略等可能影響拉絲嚴重程度之變因全部固定，使列印件之拉絲差異主要反映 FDM 過程之自然變動，而非人為參數差異。}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.7\textheight,keepaspectratio]{images/bambu-studio-cooling-mode.png}
\caption{冷卻模式設定代表截圖（風扇 60\%$\sim$80\%、最小列印速度 20 mm/s、懸垂強制冷卻）}
\label{fig:cooling-representative}
\end{figure}
