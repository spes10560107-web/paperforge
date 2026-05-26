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

<!-- 待修正(學長標註B4)：品質評分頭(0–100)在本摘要與結論第5點被當成「研究成果」陳述，但它僅是等級編號的線性轉換 + MSE 輔助頭，且 D/E/F 系統性偏高（F 目標 0、預測平均 28.5），定位上更接近限制而非貢獻。建議將摘要與貢獻處的語氣降一格（明確標為「輔助排序指標、未經人工校準」）。屬語氣調整、不涉數據，學長暫不更動，待原作者修。 -->

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

3D 列印技術（Three-Dimensional Printing），又稱積層製造（Additive Manufacturing, AM），係指透過電腦輔助設計（CAD）軟體建立三維數位模型後，依據切片軟體產生的路徑指令，將材料逐層堆積成形的製造技術[@ISOASTM52900]。自 Charles Hull 於 1984 年提出光固化成型技術（Stereolithography, SLA）相關專利，並由 3D Systems 推動早期商業化應用後，3D 列印技術歷經數十年的持續演進，應用範圍由工業快速原型製造逐漸擴展至航太、汽車、醫療、電子、建築及個人消費等多元應用領域[@gibsonAdditiveManufacturingTechnologies2021; @OurStory3D2017]。市場研究機構 MarketsandMarkets 於 2023 年估計，全球 3D 列印市場規模可能由 2023 年約 150 億美元成長至 2028 年約 345 億美元，年均複合成長率約為 18.1\%[@marketsandmarkets3DPrintingMarket]；此數字僅作為產業應用動機與市場脈絡參考，實際市場規模仍可能因研究機構、估算口徑與年度更新而改變，不作為本文模型效能或方法有效性之證據。

在眾多 3D 列印技術中，熔融沉積成型（Fused Deposition Modeling, FDM）因設備成本相對低廉、操作流程較為簡易，且可支援 PLA、PETG、ABS、TPU 等多種熱塑性材料，成為桌上型與教育應用場域中常見的 3D 列印技術之一[@gibsonAdditiveManufacturingTechnologies2021; @InventorFDM3D2017]。FDM 的基本工作原理是將熱塑性聚合物線材（Filament，直徑通常為 1.75 mm 或 2.85 mm）送入加熱腔，融化後由噴嘴（Nozzle）擠出，依照切片路徑在熱床（Heated Bed）上逐層堆積，冷卻固化後形成實體成品。由於 FDM 技術的普及，其列印品質管控的重要性日益受到業界與學術界的重視。

然而，FDM 列印的品質受到多項關鍵參數的交互影響，包括噴嘴溫度、熱床溫度、列印速度、回抽距離（Retraction Distance）與速度、層高（Layer Height）、填充密度（Infill Density）、冷卻風扇轉速及支撐結構設定等。任一參數設定不當，均可能引發不同類型的列印瑕疵，導致成品品質下降。目前業界對 FDM 列印品質的評估，仍多依賴操作人員的人工目視檢查，缺乏系統化、自動化的品質管控機制，難以滿足工業 4.0 背景下智慧製造的需求。

工業 4.0（Industry 4.0）一詞最早於 2011 年德國漢諾威工業展（Hannover Fair）中被提出，後續由德國工業 4.0 工作小組於 2013 年提出正式推動建議。其核心在於透過資訊通訊技術，使機器、製程與生產系統形成智慧化連網，進而提升製造流程的即時性、自動化與資訊整合能力[@WhatIndustry40; @WhatIndustrie40]。在此背景下，將深度學習技術導入 3D 列印品質管控，建立自動化的瑕疵辨識與評分系統，既符合工業 4.0 的技術路線，也具有顯著的實際應用價值。

## 研究動機 {#sec:intro-motivation}

在實際的 3D 列印生產場景中，品質管控面臨以下幾項核心困難：其一，人工目視效率低落，當列印批量增加時，每件成品的逐一檢視耗時過長，成為生產流程的瓶頸；其二，主觀判斷標準不一，不同操作人員對同一件成品的品質評估可能存在差異，尤其在瑕疵程度接近等級邊界的案例中，判斷結果的不一致性會降低品質數據的可信度；其三，缺乏量化依據，傳統目視評估難以提供精確的數值品質分數，無法為列印參數的系統性優化提供回饋依據；其四，難以建立品質歷史紀錄，人工評估結果不易系統性地留存，不利於品質趨勢分析與製程改善。

有鑑於此，本研究的研究動機源自對以上痛點的深刻認識：若能以深度學習模型模擬有經驗品管人員的判斷邏輯，將瑕疵辨識與品質評分工作自動化，不僅可大幅提升檢測效率，更能確保評估標準的一致性與客觀性。此外，本研究的另一動機來自對「有限資料量下如何訓練高效能模型」此一挑戰的探索興趣。在實際應用場景中，取得充足的標注資料往往成本高昂，如何在樣本數受限的條件下（本研究最少的 F 等級為 32 張），透過遷移學習、資料增強及損失函數設計等技術手段，建立具可行性的分類模型，是本研究的核心技術課題。

## 研究目的與貢獻 {#sec:intro-purpose}

本研究的核心貢獻有以下四項：

1. **FDM 魚骨拉絲六等級資料集**：建立包含 1110 張魚骨影像、依拉絲面積佔比定義之六等級（A 至 F）資料集；雖目前由單一標注者完成尚待多人一致性驗證，但就本研究目前蒐集之文獻範圍而言，可作為後續 FDM 拉絲瑕疵小樣本影像分類研究之可重現基準。
2. **嚴格分組切分與多 seed 泛化評估**：以原圖為單位進行 Group Split（原圖零重疊），避免同源樣本造成過度樂觀的評估；MobileNetV3-Large 在嚴格測試集達約 86\% 整體準確率，並以五個 seed 重複後平均仍維持約 81\%，提供比單次切分更保守的小樣本工業視覺基準（詳細數值見 \ref{sec:results-supplemental} 節）。
3. **模型策略比較、消融與不確定性分析**：本研究完成 MobileNetV3-Large、ResNet18、EfficientNet-B0 之完整 / 簡化策略比較，並補做 Focal Loss、Label Smoothing、Mixup、Weighted Random Sampler 之單變因消融。五 seed 結果顯示，各模型 accuracy 與 QWK 差異未達統計顯著；但 MobileNetV3-Large 完整與 ResNet18 完整之 macro-F1 顯著高於簡化設定。消融結果顯示移除 Weighted Sampler 對 QWK 與跨等級誤判傷害最大，模型校準則顯示低 confidence 樣本適合導入人工複核流程。
4. **端對端批量辨識系統可行性**：整合自動裁切、批量推論、分級輸出與 HTML 可視化報告，於桌上型 GPU（RTX 3050 Laptop）上達毫秒級單張推論（約 6.90 ms、每秒約 145 張），驗證離線批量部署之可行性（詳細效能見 \ref{sec:results-batch} 節）。

附帶產出包含可量化的六等級評分準則、各等級範例圖、Label Studio 標注流程與雙輸出（六分類 + 0 至 100 連續品質分）模型架構，作為後續研究擴充之共用工具。

## 研究範圍 {#sec:intro-scope}

本研究的研究範圍以 FDM 技術列印之魚骨形狀 PLA 材質列印件為主要研究對象，聚焦於拉絲瑕疵的嚴重程度分類，不包含翹曲及裂痕瑕疵的深入分析（因現有樣本中此兩類瑕疵數量不足）。實驗設備限定為 Bambu Lab A1 3D 印表機，耗材為標準 PLA 線材，拍攝環境為固定背景的室內自然光環境，因此模型的泛化能力主要針對此特定設備與材料條件。資料規模方面，本研究資料集共取得 1110 筆有效魚骨樣本，分屬六個品質等級，最多等級 546 張（A 級），最少等級 32 張（F 級）。

為使後續讀者與審查者能正確解讀本研究之結論，茲將本研究之適用範圍與已知限制條列如下：

1. **單一硬體條件**：僅使用 Bambu Lab A1 印表機與標準 PLA 線材，未驗證其他機型（如 Prusa、Creality）或材料（如 PETG、ABS、TPU）之表現。
2. **單一幾何條件**：僅使用魚骨形狀樣本，模型對其他幾何形狀（如盒體、齒輪、有機曲面）之泛化能力未經驗證。
3. **單一瑕疵類型**：僅針對拉絲（Stringing）嚴重程度分類；翹曲與裂痕雖於文獻回顧介紹，但因樣本不足未納入訓練與測試。
4. **資料相關性與分組切分**：1110 張樣本係由 185 張原始照片各裁切出 6 支魚骨而來，同一原圖切出之多支樣本在光線、背景與列印批次上高度相關。為避免同源樣本造成過度樂觀的評估，本研究以原圖 ID 為分組鍵，採用分組隨機切分（Group Shuffle Split，seed=7），並在零原圖重疊之嚴格測試集（168 筆）上評估；惟 B、E、F 測試樣本數偏少（16、8、4 張），相關結果詳見 \ref{sec:results-supplemental} 節。

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

本節依「通用影像分類 $\rightarrow$ 小樣本遷移學習 $\rightarrow$ 類別不平衡處理 $\rightarrow$ 與本研究最相近之 FDM 領域研究」的順序，逐步收斂至本研究的問題情境。

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

本研究採用 MobileNetV3-Large[@howardSearchingMobileNetV32019]（ImageNet V2 預訓練）作為骨幹網路，以遷移學習方式進行六分類微調。模型修改如下：將分類頭最後一個全連接層（原 1000 類輸出）替換為含 Dropout（p = 0.4）的六分類線性層；同時在 pooling 後的特徵向量上接品質評分輔助頭，其結構為 Dropout（p = 0.2）$\rightarrow$ Linear $\rightarrow$ ReLU $\rightarrow$ Linear $\rightarrow$ Sigmoid，輸出範圍 0 至 1 的連續品質分，乘以 100 即得 0 至 100 分。訓練時分類頭與評分頭同步優化。

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

# 結論與建議 {#sec:conclusion}

## 結論 {#sec:conclusion-summary}

本研究建立了一套以深度學習影像辨識為核心的 3D 列印件瑕疵自動辨識與品質評分系統，以 FDM 列印魚骨件的拉絲瑕疵為研究標的，實現六等級（A 至 F）自動分類與品質評分輸出。主要研究成果總結如下：

1. **單一標注者下之可重複品質等級制度**：以拉絲面積佔比為主要判斷依據，建立六個明確的品質等級定義並配合 A 至 F 範例圖。本研究主張的是「模型可學習並重現此套固定標注準則」，可降低批量檢查負擔並提供人工複核輔助；惟全部樣本由單一標注者完成、尚未進行多人一致性測試，故不宣稱已建立多人共識下的客觀品質標準（標注一致性限制詳見 \ref{sec:results-supplemental-interpretation} 節）。
2. **系統性資料蒐集與標注**：透過多批次列印與拍攝，配合 Label Studio 工具完成全部樣本的人工標注，建立含 1110 張有效樣本的六等級分類資料集。從 214 張嚴重不平衡的舊資料擴充至 1110 張後，**隨機切分獨立測試集整體準確率由 78.79\% 提升至 83.23\%**；進一步以 Group Split 嚴格切分重新訓練，seed=7 詳細案例可達 **86.31\%（145/168）**，五 seed 平均約 80\% 至 81\%，顯示模型已具備初步輔助分級能力，但單次切分結果不應過度外推。
3. **深度學習模型效能與不確定性**：以 MobileNetV3-Large（ImageNet V2 預訓練）為主，並補做完整 / 簡化策略、ResNet18 與 EfficientNet-B0 對照。五 seed 重複後，各模型平均 accuracy 均落在 80\% 至 81\%，accuracy 與 QWK 之 paired t-test 未達顯著差異；惟完整策略與 ResNet18 之 macro-F1 顯著高於簡化設定（詳見 \ref{sec:results-supplemental-multiseed} 節）。單變因消融顯示 Weighted Random Sampler 對 QWK 與跨等級誤判控制最關鍵；模型校準後低 confidence 子集準確率明顯偏低，適合作為人工複核門檻（詳見 \ref{sec:results-supplemental-calibration} 節）。故系統定位為「品質管控輔助原型」，而非可獨立判定之自動分級系統。
4. **端對端自動化流程**：整合自動裁切、批量辨識、分級輸出與 HTML 可視化報告，形成由原始照片到品質等級報告的離線批量處理流程；主要簡化模型於 RTX 3050 Laptop GPU 單張推論約 6.90 ms（約 144.9 張/秒），原完整 Group Split 模型約 7.05 ms（約 141.8 張/秒），驗證離線批量部署之可行性。惟此為單機離線量測，產線部署前仍需補做完整吞吐量、人工複核成本與現場穩定性評估。
5. **品質評分量化（未經人工校準）**：模型同時輸出 0 至 100 的連續品質分數。各等級平均分在 Group Split 測試集與全資料回測下均呈 A $>$ B $>$ C $>$ D $>$ E $>$ F 之單調遞減（數值詳見表 \ref{tab:plain-quality-score}），具輔助排序價值；惟目標分數採等級編號之線性轉換、未經多人主觀評分校準，B、D、E、F 等級之預測平均偏高，現階段僅作為分類結果之輔助連續指標，不宜作為絕對品質量化依據。

\vspace{0.5em}

**主要貢獻陳述（Take-home Message）**：

> 重寫

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
\TableNote[0.96\textwidth]{註：以上數值為 Bambu Studio「耗材絲設置」頁 Polymaker PolyTerra PLA \texttt{@BBL A1} 預設值，全研究期間未做調整。此設計使噴嘴溫度、熱床溫度、冷卻風扇策略等可能影響拉絲嚴重程度之變因全部固定，使列印件之拉絲差異主要反映 FDM 過程之自然變動，而非人為參數差異。}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.7\textheight,keepaspectratio]{images/bambu-studio-cooling-mode.png}
\caption{冷卻模式設定代表截圖（風扇 60\%$\sim$80\%、最小列印速度 20 mm/s、懸垂強制冷卻）}
\label{fig:cooling-representative}
\end{figure}
