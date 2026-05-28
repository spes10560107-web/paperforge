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

本研究以魚骨形狀 PLA 列印件為對象，建立涵蓋 A 至 F 共六等級拉絲嚴重程度之影像分類資料集，採用 MobileNetV3-Large 為骨幹進行遷移學習，並附加品質評分輔助頭以輸出 0 至 100 之連續品質分數；同時以 ResNet18、EfficientNet-B0 為對照基準，於原圖層級 Group Split 與五個 seed 重複實驗下評估模型穩定性，並補做 seed=7 單變因消融、模型校準、Grad-CAM 與外部影像檢查，以區分單次最佳結果與可重複之結論。

實驗在嚴格 Group Split 測試集（原圖零重疊）上，五個 seed 重複後，各模型 / 策略之平均 accuracy 約落在 80.1\% 至 81.2\%，accuracy 與 QWK 差異未達統計顯著，且以 Bonferroni 校正後 macro-F1 之探索性差異亦不再顯著；seed=7 單次案例中簡化設定達 86.31\%、完整設定達 89.88\%，但均不代表穩定表現，差異原因之一是完整設定因 WeightedRandomSampler 使每 epoch 訓練步數為簡化設定的約六倍。品質分數呈現 A 至 F 大致遞減，具輔助排序價值，但因僅由等級編號線性轉換而來，未經多人主觀評分校準，不宜視為絕對品質分。本研究貢獻在於提供 FDM 魚骨拉絲瑕疵於本研究條件下之內部評估基準與離線批量辨識原型，並指出受限於單一機型、單一材料、單一形狀、單一瑕疵類型與標注一致性未驗證等條件，現階段仍應定位為品質管控之輔助工具。

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

3D 列印技術（Three-Dimensional Printing），又稱積層製造（Additive Manufacturing, AM），係指透過電腦輔助設計（CAD）軟體建立三維數位模型後，依據切片軟體產生的路徑指令，將材料逐層堆積成形的製造技術[@ISOASTM52900]。自 Charles Hull 於 1984 年提出光固化成型技術（Stereolithography, SLA）相關專利，並由 3D Systems 推動早期商業化應用後，3D 列印技術歷經數十年的持續演進，應用範圍由工業快速原型製造逐漸擴展至航太、汽車、醫療、電子、建築及個人消費等多元應用領域[@gibsonAdditiveManufacturingTechnologies2021; @OurStory3D2017]。市場研究機構 MarketsandMarkets 於 2023 年估計，全球 3D 列印市場規模可能由 2023 年約 150 億美元成長至 2028 年約 345 億美元，年均複合成長率約為 18.1\%[@marketsandmarkets3DPrintingMarket]，顯示此一製造技術在全球產業中的應用前景持續擴展。

在眾多 3D 列印技術中，熔融沉積成型（Fused Deposition Modeling, FDM）因設備成本相對低廉、操作流程較為簡易，且可支援 PLA、PETG、ABS、TPU 等多種熱塑性材料，成為桌上型與教育應用場域中常見的 3D 列印技術之一[@gibsonAdditiveManufacturingTechnologies2021; @InventorFDM3D2017]。FDM 的基本工作原理是將熱塑性聚合物線材（Filament，直徑通常為 1.75 mm 或 2.85 mm）送入加熱腔，融化後由噴嘴（Nozzle）擠出，依照切片路徑在熱床（Heated Bed）上逐層堆積，冷卻固化後形成實體成品。由於 FDM 技術的普及，其列印品質管控的重要性日益受到業界與學術界的重視。

然而，FDM 列印的品質受到多項關鍵參數的交互影響，包括噴嘴溫度、熱床溫度、列印速度、回抽距離（Retraction Distance）與速度、層高（Layer Height）、填充密度（Infill Density）、冷卻風扇轉速及支撐結構設定等。任一參數設定不當，均可能引發不同類型的列印瑕疵，導致成品品質下降。目前業界對 FDM 列印品質的評估，仍多依賴操作人員的人工目視檢查，缺乏系統化、自動化的品質管控機制，難以滿足工業 4.0 背景下智慧製造的需求。

工業 4.0（Industry 4.0）一詞最早於 2011 年德國漢諾威工業展（Hannover Fair）中被提出，後續由德國工業 4.0 工作小組於 2013 年提出正式推動建議。其核心在於透過資訊通訊技術，使機器、製程與生產系統形成智慧化連網，進而提升製造流程的即時性、自動化與資訊整合能力[@WhatIndustry40; @WhatIndustrie40]。近年來，以卷積神經網路（CNN）為代表的深度學習影像辨識技術在工業視覺檢測領域取得顯著進展，為自動化品質管控提供了新的技術路徑；將此類技術導入 3D 列印列印後品質輔助辨識，既符合工業 4.0 的智慧製造方向，亦具有實際應用探索價值。

## 研究動機 {#sec:intro-motivation}

在實際的 3D 列印生產場景中，品質管控面臨以下幾項核心困難：其一，人工目視效率低落，當列印批量增加時，每件成品的逐一檢視耗時過長，成為生產流程的瓶頸；其二，主觀判斷標準不一，不同操作人員對同一件成品的品質評估可能存在差異，尤其在瑕疵程度接近等級邊界的案例中，判斷結果的不一致性會降低品質數據的可信度；其三，缺乏一致且可追溯的數值化紀錄，傳統目視評估不易形成可比較的品質分布；其四，難以建立品質歷史紀錄，人工評估結果不易系統性地留存，不利於品質趨勢分析與製程改善。

深度學習影像分類技術具備從大量樣本中自動學習視覺特徵的能力，能客觀量化瑕疵嚴重程度，恰能彌補上述人工目視的不足。然而，3D 列印拉絲瑕疵的嚴重程度判定具有明顯的序數特性：少量短絲仍屬可接受範圍，大範圍絲狀殘留則需重新列印，等級邊界常受光線、角度與標注者主觀判斷影響。此外，在小批量研究場景中，取得大量具多人一致性標注的資料往往成本高昂，資料集的類別不平衡問題亦難以避免。在上述挑戰條件下，如何建立一套嚴格且可重現的評估框架，以確認深度學習模型是否真正具備作為品質管控輔助工具的潛力，是本研究的核心動機。

## 研究目的與貢獻 {#sec:intro-purpose}

本研究的核心貢獻有以下四項：

1. **FDM 魚骨拉絲六等級資料集**：建立包含 1110 張魚骨影像、依目視估計拉絲覆蓋比例定義之六等級（A 至 F）資料集；雖目前由單一標注者完成尚待多人一致性驗證，但可作為本研究條件下之內部基準，供後續 FDM 拉絲瑕疵小樣本影像分類研究比較。
2. **嚴格分組切分與多 seed 泛化評估**：以原圖為單位進行 Group Split（原圖零重疊），避免同源樣本造成過度樂觀的評估，並透過多組 seed 重複實驗提供比單次切分更保守的小樣本工業視覺基準。
3. **模型策略比較、消融與不確定性分析**：系統比較 MobileNetV3-Large、ResNet18、EfficientNet-B0 三種骨幹，並消融 Focal Loss、Label Smoothing、Mixup、Weighted Random Sampler 等訓練策略，評估各因素對少數類別分類的實際貢獻；並進行模型校準分析，確認低置信度樣本可納入人工複核流程。
4. **離線批量辨識流程可行性**：整合自動裁切、批量推論、分級輸出與 HTML 可視化報告，於 RTX 3050 Laptop GPU 上達毫秒級單張模型推論（簡化設定約 6.90 ms、完整設定約 7.05 ms），驗證離線批量推論流程之可行性（詳細效能見 \ref{sec:results-batch} 節）。

附帶產出包含具明確判斷規則的六等級評分準則、各等級範例圖、Label Studio 標注流程與雙輸出（六分類 + 0 至 100 連續品質分）模型架構，作為後續研究擴充之共用工具。

## 研究範圍 {#sec:intro-scope}

本研究的研究範圍以 FDM 技術列印之魚骨形狀 PLA 材質列印件為主要研究對象。魚骨形狀因具有細長肋條、尖端與多個間隙結構，當噴嘴溫度、回抽設定或冷卻條件不穩定時，細絲通常優先出現於魚骨間隙與尖端區域，使拉絲現象易於觀察與等級判定，因此作為本研究拉絲嚴重程度分類的測試對象。本研究聚焦於拉絲瑕疵的嚴重程度分類，不包含翹曲及裂痕瑕疵的深入分析（因現有樣本中此兩類瑕疵數量不足）。實驗設備限定為 Bambu Lab A1 3D 印表機，耗材為標準 PLA 線材，拍攝環境為固定背景的室內自然光環境，因此模型的泛化能力主要針對此特定設備與材料條件。資料規模方面，本研究資料集共取得 1110 筆有效魚骨樣本，分屬六個品質等級，最多等級 546 張（A 級），最少等級 32 張（F 級）。

為使後續讀者與審查者能正確解讀本研究之結論，茲將本研究之適用範圍與已知限制條列如下：

1. **單一硬體條件**：僅使用 Bambu Lab A1 印表機與標準 PLA 線材，未驗證其他機型（如 Prusa、Creality）或材料（如 PETG、ABS、TPU）之表現。
2. **單一幾何條件**：僅使用魚骨形狀樣本，模型對其他幾何形狀（如盒體、齒輪、有機曲面）之泛化能力未經驗證。
3. **單一瑕疵類型**：僅針對拉絲（Stringing）嚴重程度分類；翹曲與裂痕雖於文獻回顧介紹，但因樣本不足未納入訓練與測試。
4. **資料相關性**：1110 張樣本係由 185 張原始照片裁切而來，同源樣本在光線、背景與列印批次上高度相關；評估時採原圖層級 Group Split 確保訓練與測試集原圖零重疊，詳見第 \ref{sec:method} 章。

上述邊界條件確立了本研究的適用範圍；其餘方法與實驗設計層面之限制，詳見第 \ref{sec:conclusion} 章結論。

## 研究流程 {#sec:intro-flow}

本研究的整體執行流程分為三大階段：第一階段為資料蒐集與前處理，包含 3D 列印樣本製作、影像拍攝、魚骨自動裁切及人工標注；第二階段為模型訓練與評估，包含資料集整理、模型訓練、效能評估、多 seed 重複與消融分析；第三階段為系統整合與應用，包含批量辨識系統開發、可視化報告產生及實際應用驗證。詳細流程如圖 \ref{fig:overall-flow} 所示。

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth,height=0.72\textheight,keepaspectratio]{images/research-overall-flow.png}
\caption{研究整體流程圖}
\label{fig:overall-flow}
\end{figure}

# 文獻回顧 {#sec:literature}

## 文獻回顧架構說明 {#sec:literature-source-quality}

本章按「FDM 製程與瑕疵類型 → 電腦視覺與深度學習方法 → 相關研究 → 模型架構 → 遷移學習與不平衡處理 → 研究缺口」的順序展開，逐步收斂至本研究的問題情境。

本文在引用上採分級原則：名詞定義、製造流程、深度學習模型架構等內容優先引用國際標準、教科書與同儕審查論文[@ISOASTM52900; @gibsonAdditiveManufacturingTechnologies2021; @dengImageNetLargescaleHierarchical2009; @heDeepResidualLearning2016; @howardSearchingMobileNetV32019]；FDM 瑕疵現象與調參經驗則輔以廠商文件[@StringingOozing; @BambuStudioAdvanced; @WarpingPrusaKnowledge2025; @LayerSeparationSplitting2024]，此類來源反映實務經驗而非受控實驗結果；市場規模數字僅作緒論背景[@marketsandmarkets3DPrintingMarket]，不參與模型效能判斷。本文核心實證結論均來自本研究資料集、嚴格切分評估、多 seed 重複實驗與可重現程式輸出。

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

從影像辨識的角度而言，拉絲在影像中呈現細線狀、高頻率的局部紋理，通常以明亮細絲出現在較暗背景（如黑色熱床）或魚骨間隙中，形成與正常平滑表面明顯不同的對比特徵。此類特徵屬影像的高頻空間成分，對局部感受野敏感的卷積神經網路（CNN）比傳統全域描述子（如顏色直方圖）更適合捕捉；拉絲嚴重程度的差異則進一步反映在細絲密度與分布面積上，使得等級分類可藉由 CNN 對多尺度局部紋理的感知來實現。第四章 Grad-CAM 分析結果將驗證此推論：模型正確預測的案例中，熱力圖高亮區域集中於魚骨間隙的拉絲細絲區域；詳見 \ref{sec:results-supplemental-calibration} 節。

## 電腦視覺與深度學習於工業瑕疵檢測 {#sec:literature-cv-dl}

電腦視覺（Computer Vision）技術在工業品質檢測領域的應用已有數十年歷史，早期方法以傳統影像處理技術為主，包括邊緣偵測、閾值分割、形態學運算及特徵工程等，需要領域專家手動設計特徵提取規則。此類方法在受控環境下（固定光源、背景及目標位置）表現尚可，但對光線變化、姿態變化及背景干擾的魯棒性較差，且難以應對複雜的多類別瑕疵辨識任務。

深度學習技術的崛起從根本上改變了電腦視覺的研究範式[@DeepLearning; @lecunGradientbasedLearningApplied1998]。卷積神經網路（CNN）以端到端的方式自動學習影像的層次化特徵表示，從底層的邊緣和紋理特徵到高層的語義特徵，無需人工設計特徵，且在充足資料的支持下，其辨識精度通常優於傳統人工特徵方法[@dengImageNetLargescaleHierarchical2009; @heDeepResidualLearning2016]。近年來，CNN 已被廣泛應用於半導體晶圓瑕疵檢測、紡織品缺陷辨識、鋼板表面瑕疵分類、PCB 板焊接缺陷偵測等工業品質管控任務[@bhattImageBasedSurfaceDefect2021]，並在多項公開基準或受控資料集上取得高辨識率；在 3D 列印領域，亦已有研究將 CNN 應用於列印過程的即時錯誤偵測與校正[@brionGeneralisable3DPrinting2022]。

值得注意的是，工業瑕疵檢測文獻中另有一類基於**異常偵測（Anomaly Detection）**的無監督或半監督方法，如以自動編碼器（Autoencoder）的重建誤差判斷是否異常，或以正常樣本建立特徵分布、測試時以馬氏距離偵測偏離[@bhattImageBasedSurfaceDefect2021]。此類方法的優勢在於訓練時僅需正常樣本，不必對每種瑕疵類型逐一標注；但其輸出為「正常/異常」的二元判斷，無法直接輸出瑕疵嚴重程度等級。本研究的核心目標是對拉絲嚴重程度進行 A 至 F 六等級的**序數分級**，需要每張樣本帶有等級標籤才能訓練分類或迴歸模型，因此選擇有監督分類路線，而非無監督異常偵測。

## 相關文獻探討 {#sec:literature-related}

本節依「通用影像分類 → 小樣本遷移學習 → 類別不平衡處理 → 與本研究最相近之 FDM 領域研究」的順序，逐步收斂至本研究的問題情境。

CNN 以端到端方式自動學習影像的層次化特徵表示，在充足資料的支持下，其辨識精度通常優於傳統人工特徵方法---此為深度學習文獻中已建立的共識[@DeepLearning; @lecunGradientbasedLearningApplied1998]。Jogin 等人[@joginFeatureExtractionUsing2018]的 CIFAR-10 實驗（85.97\% 準確率，顯著優於 SVM 與隨機森林）提供了一個具體的多類別分類參照，說明 CNN 學得的深度特徵在非工業影像分類任務上的系統性優勢；惟此屬通用影像分類，與 FDM 表面瑕疵視覺特徵之關聯僅屬間接，主要用途是為本研究採用 CNN 骨幹提供方法論背景。

Varshni 等人[@varshniPneumoniaDetectionUsing2019]以 DenseNet-169、ResNet-50、VGG-16、Xception 等預訓練模型對 ChestX-ray14 肺炎 X 光影像做特徵提取並接 SVM 分類，其中 DenseNet-169+SVM 在 AUC 達 0.8002。需指出，醫學 X 光影像與工業表面拉絲影像在視覺頻譜與標注性質上差異甚大；本文引用此研究的意義在於其**方法論層面**的相似性：同樣在「標注樣本有限（約千張量級）」的條件下，以 ImageNet 預訓練模型進行特徵遷移並取得有效結果，為本研究採用 MobileNetV3-Large 遷移學習策略提供支持依據。

Lin 等人[@linFocalLossDense2017]提出之 Focal Loss 原用於**目標偵測**中前景與背景之極端類別不平衡（原始論文情境下比例可達 1000:1 以上），其在標準交叉熵的基礎上引入調焦因子 $(1-p_t)^\gamma$，降低模型已正確分類之高信心樣本的損失權重，使訓練聚焦於困難樣本（Hard Example）。需指出，本研究六個等級中最大不平衡比例約為 17:1（A 級 546 張對 F 級 32 張），屬相對溫和的失衡，與原論文情境有別；本研究引入 Focal Loss 是作為多重不平衡處理手段之一（配合 Weighted Sampler、Label Smoothing），而非針對極端比例失衡的主要解法（本研究實際採用之不平衡處理組合詳見 \ref{sec:method-model} 節）。

與本研究最直接相關者為 Brion 與 Pattinson[@brionGeneralisable3DPrinting2022]，其以多頭神經網路對 FDM 列印過程進行**即時**錯誤偵測與參數校正，並在多種印表機、材料與幾何形狀上展現泛化能力，屬「列印中（in-process）」的閉迴路監控。相較之下，本研究著眼於「列印後（post-print）」的成品表面品質評級：將拉絲瑕疵依嚴重度劃分為 A 至 F 六個**序數**等級並輸出連續品質分，且採用保留未來邊緣部署彈性的輕量模型，於小規模且不平衡的資料上以嚴格切分重複評估。兩者在偵測時機、輸出粒度與應用情境上互補，而後者正是本研究欲補足之處（詳見 \ref{sec:literature-gap} 節）。

## MobileNetV3 架構 {#sec:literature-mobilenetv3}

MobileNet 系列最早由 Howard 等人提出，其核心設計是以深度可分離卷積（Depthwise Separable Convolution）取代標準卷積：將其分解為深度卷積（Depthwise Conv）與逐點卷積（Pointwise Conv）兩步驟，在維持感受野的同時大幅降低參數量與計算量，使 CNN 更適合部署於行動端與邊緣裝置[@howardMobileNetsEfficientConvolutional2017]。MobileNetV3 則由 Google 以神經架構搜尋（NAS）自動搜尋最優配置，並在深度可分離卷積的基礎上再引入兩項關鍵技術[@howardSearchingMobileNetV32019]：（1）**壓縮激活（Squeeze-and-Excitation, SE）注意力機制**：對特徵圖各通道的重要性進行自適應加權，強化關鍵特徵的表達；（2）**Hard-Swish 激活函數**：以分段線性函數近似 Swish 激活，在效能損失極小的前提下大幅降低計算成本。

MobileNetV3-Large 的整體架構包含：初始卷積層（3 × 3 卷積，stride = 2）、15 個 Bottleneck 模組（其中部分模組含 SE 注意力機制）、1 × 1 卷積升維層（將通道從 160 升至 960）、自適應平均池化層（輸出 960 維向量），以及最終的分類頭（含 Linear(960→1280) + Hardswish + Dropout + Linear(1280→1000)）。其中，池化後的 1280 維中間特徵是本研究雙輸出頭的共用輸入（詳見 \ref{sec:method-model-dualhead} 節）。以 224 × 224 像素輸入為例，三個候選模型的效率指標比較如表 \ref{tab:model-complexity} 所示。

\begin{table}[H]
\centering
\caption{本研究三個候選模型效率指標比較（224 × 224 輸入）}
\label{tab:model-complexity}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{cccc}
\hline
\textbf{模型} & \textbf{參數量} & \textbf{計算量（FLOPs）} & \textbf{設計哲學} \\
\hline
MobileNetV3-Large & 5.4M & \textasciitilde{}219 MFLOPs & 行動端最佳化（NAS + SE） \\
EfficientNet-B0   & 5.3M & \textasciitilde{}390 MFLOPs & 複合縮放（寬度/深度/解析度） \\
ResNet18          & 11.7M & \textasciitilde{}1.8 GFLOPs & 殘差連接（深度基準） \\
\hline
\end{tabular}
\end{table}

MobileNetV3-Large 與 EfficientNet-B0 參數量相近，但 MobileNetV3-Large 計算量較低（219 MFLOPs 對 390 MFLOPs），SE 注意力機制亦有助於對通道重要性加權，對局部紋理（如細絲密度差異）的感知具一定優勢。本研究採用 torchvision 提供之 ImageNet V2 預訓練權重作為初始化，可利用大規模自然影像資料上學得的通用低階與中階視覺特徵，減少對本研究標注資料量的依賴。

## 遷移學習與資料不平衡處理 {#sec:literature-transfer}

遷移學習（Transfer Learning）在電腦視覺領域的核心假設是：在大規模資料集（如 ImageNet）上預訓練的模型，已學習到豐富的底層視覺特徵（邊緣、紋理、形狀等），這些特徵可以遷移至目標任務，即使目標任務的資料量遠少於預訓練資料集。常用的遷移學習策略包括：（a）**特徵提取（Feature Extraction）**：凍結預訓練模型的全部或大部分層，僅訓練新增的任務特定層；（b）**微調（Fine-tuning）**：以較小的學習率對全部或部分層進行更新，使模型特徵更好地適應目標任務。本研究兩組設定（簡化與完整）均採用全層微調（Full Fine-tuning）策略；兩者的差異主要在於損失函數、資料增強（有無 Mixup）與過採樣設定的組合，詳見 \ref{sec:method-model} 節。

資料不平衡（Class Imbalance）是小樣本瑕疵分類常見的難題，文獻上的處理手段大致可分為三類：（1）**資料採樣層面**的重採樣，如對少數類別過採樣（oversampling）或加權抽樣，平衡各類別在訓練過程中的曝光機會；（2）**損失函數層面**的成本敏感法，包括前述 Focal Loss[@linFocalLossDense2017]（對困難樣本加重懲罰）與 **Label Smoothing**（將分類目標由硬標籤替換為軟標籤，分配小量機率 $\epsilon$ 給非目標類），後者有助於避免模型對多數類別樣本產生過度自信，並在少數類別邊界保留更多梯度訊號；（3）**資料增強層面**的方法，如 Mixup[@zhangMixupEmpiricalRisk2018]在批次中對任意兩筆樣本進行線性混合，擴充訓練分布的多樣性並抑制模型對邊界樣本的過度自信。三類手段彼此正交、可組合使用；本研究完整設定採用 Focal Loss + Label Smoothing ($\epsilon=0.1$) + Mixup ($\alpha=0.3$) + Weighted Sampler 之組合，簡化設定僅保留標準 Cross Entropy，詳見 \ref{sec:method-model} 節。需特別指出的是，Mixup 應用於序數分類任務時存在一項潛在限制：若混合的兩張樣本跨越非相鄰等級（例如 A 級完美品與 F 級失敗品），所得的混合樣本在物理上並不存在，其混合標籤亦難以對應真實拉絲狀態；本研究仍採用 Mixup 作為正則化手段，主因是其邊界軟化效果有助於抑制過擬合，此簡化的方法論取捨已列入 \ref{sec:conclusion-future} 節後續研究方向。另一方面，本研究的完整設定同時啟用 Focal Loss 與 Mixup，形成 MixFocal 的組合：以混合比例 $\lambda$ 線性插值兩個樣本的交叉熵後再套用焦點加權；此組合偏離 Focal Loss 的原始硬標籤設計，屬方法論的實作取捨，詳細說明見 \ref{sec:method-model} 節。

此外，本研究的 A 至 F 等級並非彼此完全獨立的名目類別，而具有由良品到嚴重瑕疵的序數關係。若僅以一般多類別交叉熵訓練模型，仍需在評估階段額外檢查模型是否尊重等級距離，例如相鄰等級誤判與跨等級誤判的差異、加權 Kappa 指標是否維持穩定，以及低信心樣本是否應交由人工複核。序數分類文獻亦提出以排序一致性約束處理等級輸出的方法，例如 CORAL 與 CORN 將類別順序納入模型學習目標[@caoRankConsistentOrdinal2020; @shiDeepNeuralNetworks2023]；模型信心校準則可用於檢查 softmax confidence 是否能反映預測可靠度，temperature scaling 為常見的後處理方法之一[@guoCalibrationModern2017]。本文目前仍以 nominal classification 作為主要訓練方式，因此在結果章中特別回報 Quadratic Weighted Kappa（QWK）、跨等級誤判率（即預測等級與真實等級差距 $\geq 2$ 的樣本佔比，等效於「未達 $\pm 1$ 容忍」之比例）與校準分析，避免只用 accuracy 解讀序數分級任務。

## 研究缺口與本研究定位 {#sec:literature-gap}

綜合前述文獻，可歸納出三點現況與缺口。其一，CNN 與遷移學習在工業表面瑕疵檢測（半導體晶圓、鋼板、紡織品、PCB 等）已有成熟應用，並在多項公開基準或受控資料集上取得高辨識率[@bhattImageBasedSurfaceDefect2021]；但這些任務多屬「有無瑕疵」或「瑕疵種類」的名目分類，少有針對單一瑕疵之「嚴重程度分級」的序數評估。其二，在 FDM 領域，既有代表性研究（如 Brion 與 Pattinson[@brionGeneralisable3DPrinting2022]）聚焦於列印過程中的即時錯誤偵測與校正，著重「即時介入、避免廢件」，而非列印完成後對成品表面品質給出較細緻且可追溯的分級。其三，遷移學習雖已證實能緩解小樣本問題[@varshniPneumoniaDetectionUsing2019]，但各研究的資料規模、不平衡程度與評估切分方式差異甚大，少有在「小樣本、類別不平衡」條件下同時報告嚴格切分、多 seed 重複與校準分析的可重現評估。

據此，本研究的定位是補足「列印後、單一瑕疵（拉絲）、序數品質分級、輕量模型、嚴格可重現評估」這一交集情境：以 ImageNet 預訓練之 MobileNetV3-Large 為骨幹進行遷移學習，輸出 A 至 F 六等級分類並附加連續品質分；針對類別不平衡採用重採樣、成本敏感損失與資料增強的組合（見 \ref{sec:method-model} 節）；並以 Group Split 嚴格切分、多 seed 重複與校準分析建立可重現的效能基準（見 \ref{sec:results} 章）。目前文獻中與本研究完全相同之「列印後拉絲序數分級」情境仍相對有限，因此本文定位為此特定條件下的探索性基準。

# 研究方法 {#sec:method}

## 研究架構 {#sec:method-architecture}

本研究系統架構以資料流與責任分工為主軸呈現，如圖 \ref{fig:method-flow} 所示。整體流程由列印製樣與影像蒐集開始，經由裁切前處理與人工標注建立 A 至 F 六等級資料集，再以 MobileNetV3-Large 進行遷移學習訓練，最後輸出混淆矩陣、品質分數、批量分級資料夾與 HTML 統計報告。此呈現方式可直接對應資料來源、模型訓練與推論輸出三大環節。硬體端由 Bambu Lab A1 印表機、智慧型手機（用於拍攝）與配備 NVIDIA RTX 3050 Laptop GPU 之筆記型電腦（用於訓練與推論）組成，硬體規格詳見 \ref{sec:method-equipment-pc} 節。

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth,height=0.75\textheight,keepaspectratio]{images/method-system-flow.png}
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

本研究未將列印參數設為主動操控變因；正文依現有 Bambu Studio 截圖與實驗整理紀錄，將可追溯之代表性設定彙整於附錄。由於缺乏每一批次逐項匯出的完整列印設定檔，本文不宣稱已能逐批證明所有列印參數完全相同，而是將其視為本研究條件下的背景製程紀錄。參數控制重點分為五類：

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

本研究使用直徑 1.75 mm 之 PLA（聚乳酸）線材作為列印材料。PLA 具備列印門檻低、尺寸穩定與收縮率小等特性，適合用於建立 FDM 列印瑕疵影像資料集。本研究不將材料配方作為主要變因；現有紀錄可支持使用 PLA 與 Bambu Studio 代表性耗材設定，但不足以逐批驗證所有耗材與冷卻參數完全一致。

耗材與冷卻設定的正文重點在於三點：（一）說明目前可追溯之材料與耗材設定來源；（二）呈現噴嘴、熱床與風扇策略的代表性設定；（三）將此類設定視為實驗背景條件，而非本研究主動比較之變因。完整耗材與冷卻設定截圖移至附錄三，正文不再逐張呈現。

## 列印樣本製作與影像蒐集 {#sec:method-sample}

### 樣本設計與列印過程 {#sec:method-sample-design}

本研究以魚骨形狀列印件作為樣本，是因其具有細長肋條、尖端與多個間隙，對 FDM 拉絲瑕疵特別敏感。當噴嘴溫度、回抽設定、移動速度或冷卻條件不穩定時，細絲通常會出現在魚骨間隙與尖端區域，因此此幾何形狀適合作為拉絲嚴重程度分類的測試對象。

資料蒐集採分批列印方式進行，並另行補充少數等級與失敗件樣本，使各等級樣本更為完整。每組原始照片可裁切出 6 支魚骨樣本，最後整理為 1110 筆有效資料。正文保留資料蒐集流程與代表性設計說明，完整列印過程照片改列於附錄一，避免主文被連續照片切斷。

此安排的重點是讓正文回答三個問題：為何選擇魚骨件、資料如何分批取得，以及照片如何轉換為可訓練資料。至於每一張列印過程照片的時間與狀態，屬於實驗紀錄與佐證資料，放在附錄一更適合查核與保存。

### 影像拍攝規範 {#sec:method-sample-capture}

影像拍攝採用固定角度與固定背景的標準化規範：拍攝設備為智慧型手機相機，鏡頭以俯拍方式對準列印床，並盡量維持相同拍攝位置與室內環境，以降低批次間因視角、背景與反光造成的差異。背景為 Bambu Lab A1 原廠的黑色熱床表面，與各色 PLA 魚骨形成良好的明暗對比，有助於後續影像裁切與辨識。拍攝完成後，資料再依批次進行裁切、標注、模型訓練與辨識分析。各批次拍攝資料統計如表 \ref{tab:batch-stats} 所示。

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

本研究依列印與拍攝完成後整理之實驗照片進行魚骨樣本自動裁切。裁切採用固定網格方式：將每張照片等分為 2 欄 × 3 列，各格切出一支魚骨，並在後續訓練前統一縮放為 224 × 224 pixels 以符合預訓練模型輸入。本研究整理後共取得 1110 張有效單支魚骨樣本。

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

訓練階段對輸入影像施加表 \ref{tab:augmentation} 所列的多種隨機增強變換，以擴充有效訓練樣本多樣性，提升模型泛化能力；驗證與測試階段僅保留 Resize 與 Normalize 等確定性前處理，不施加隨機增強，確保評估流程一致。增強步驟的執行順序如表所示：Resize 至 RandomPerspective 皆在 PIL 影像空間執行；ToTensor 後進行 Normalize，最後的 RandomErasing 在 Tensor 空間執行（直接對張量數值作隨機遮蔽）。Mixup 屬批次層級增強，在 DataLoader 回傳 mini-batch 後才執行，與前述樣本層級增強互相獨立。

需特別說明 RandomVerticalFlip 的使用邏輯：魚骨樣本雖具有方向性（尾部在下），但本研究的拉絲嚴重程度標籤以覆蓋比例為準，與方向無關；且拍攝時偶有上下顛倒放置的情形。因此，以低機率（$p=0.3$）加入垂直翻轉，旨在增加方向多樣性、減少模型對固定方向的過度依賴，而非宣稱方向不影響等級判斷。

\begin{table}[H]
\centering
\caption{訓練資料增強方法彙整（Mixup 僅用於完整設定；簡化設定未啟用）}
\label{tab:augmentation}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
\hline
\textbf{增強方法} & \textbf{參數設定} & \textbf{目的說明} \\
\hline
Resize & 224$\times$224 px & \makecell{統一輸入尺寸以符合\\預訓練模型要求} \\
RandomHorizontalFlip & $p=0.5$ & 水平翻轉，增加方向多樣性 \\
RandomVerticalFlip & $p=0.3$ & \makecell{垂直翻轉；拉絲等級以覆蓋比例\\為準與方向無關，低機率使用} \\
RandomRotation & $\pm$30$^\circ$ & 應對拍攝角度偏差 \\
ColorJitter & \makecell{亮度 0.4、對比 0.4\\飽和 0.3、色相 0.1} & 應對光線與色調變化 \\
RandomGrayscale & $p=0.05$ & 強化紋理特徵，減少顏色依賴 \\
RandomPerspective & distortion=0.2, $p=0.3$ & 應對拍攝視角偏差 \\
ToTensor + Normalize & ImageNet mean/std & \makecell{轉為張量並對齊\\預訓練模型輸入分布} \\
RandomErasing & \makecell{$p=0.2$\\scale=(0.02, 0.15)} & \makecell{在 Tensor 空間執行；\\提升部分遮擋魯棒性} \\
Mixup（批次層級）& $\alpha=0.3$ & \makecell{線性混合兩筆樣本\\提升邊界辨識能力} \\
\hline
\end{tabular}
\end{table}

## 品質等級定義 {#sec:method-grading}

本研究依目視估計之拉絲覆蓋比例與魚骨結構可辨識程度，制定六個品質等級（A 至 F），如表 \ref{tab:grading-criteria} 所示。等級定義以覆蓋比例區間作為標注準則，而非透過影像分割演算法量測實際面積；並配合各等級範例圖（圖 \ref{fig:grade-a} 至圖 \ref{fig:grade-f}），以提升單一標注者在整批資料中的前後一致性。

需特別說明的是，本研究現階段無法取得第二位以上標注者重新標注資料，因此無法計算 Cohen's Kappa、Fleiss' Kappa 或人類基準表現。故本文所有模型準確率皆應解讀為「相對於本研究固定標注準則與單一標注者標籤之表現」，而非「相對多人共識品質標準之表現」。本研究可主張的是：模型能學習並重現此套固定分級準則，用於降低批量檢查負擔與提供人工複核輔助；但不宣稱已完全消除人工主觀差異。

\begin{table}[H]
\centering
\caption{六等級品質定義}
\label{tab:grading-criteria}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccccc}
\hline
\textbf{等級} & \textbf{名稱} & \textbf{拉絲覆蓋判斷標準} & \textbf{目標分數} & \textbf{應用建議} \\
\hline
A & 完美品 & \makecell{完全無拉絲細絲\\表面乾淨} & 100 分 & 可直接使用 \\
B & 良好品 & \makecell{極少量細絲，1$\sim$2 根短絲\\面積可忽略} & 80 分 & 一般用途可接受 \\
C & 輕微拉絲 & \makecell{少量細絲\\目視覆蓋 $<$ 魚身 1/4} & 60 分 & \makecell{外觀要求低時\\可接受} \\
D & 中度拉絲 & \makecell{明顯細絲\\目視覆蓋約魚身 1/4$\sim$1/2} & 40 分 & \makecell{需重新列印\\或後處理} \\
E & 嚴重拉絲 & \makecell{大量細絲\\目視覆蓋 $>$ 魚身 1/2} & 20 分 & 品質不合格 \\
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
\caption{C 等級（輕微拉絲）：目視拉絲覆蓋小於魚身四分之一}
\label{fig:grade-c}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.62\textheight,keepaspectratio]{images/grade-d-sample.jpg}
\caption{D 等級（中度拉絲）：目視拉絲覆蓋約為魚身四分之一至二分之一}
\label{fig:grade-d}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.62\textheight,keepaspectratio]{images/grade-e-sample.jpg}
\caption{E 等級（嚴重拉絲）：目視拉絲覆蓋大於魚身二分之一}
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

**C 與 D 等級的差異**在於目視拉絲覆蓋是否跨越局部區域並形成連續分布。C 級通常仍屬輕微拉絲，魚骨主體結構清楚；D 級則已出現較大範圍的絲狀殘留，可能遮蔽部分魚骨間隙。這是本研究模型較容易出現邊界誤判的區間，原因在於兩者都保留可辨識的主體輪廓，但拉絲覆蓋比例不同。

**E 與 F 等級**則代表嚴重瑕疵與失敗件。E 級仍可辨識魚骨結構，但拉絲覆蓋比例已明顯偏高；F 級則接近列印失敗或結構難以辨識。由於 F 級樣本數僅 32 張，未來仍需補充更多失敗件，以提升模型對極端瑕疵的泛化能力。

## 資料標注流程 {#sec:method-labeling}

本研究使用 Label Studio（開源標注平台）[@OpenSourceData]完成全部裁切圖的人工標注。本研究採用**圖片級分類標籤**（image-level classification label）作為訓練監督信號，而非物件偵測的邊界框標籤。標注流程為：

1. 將裁切圖匯入 Label Studio 專案。
2. A 等級直接標記為合格，無需畫框。
3. 有拉絲的樣本，先以邊界框（bounding box）於拉絲區域做視覺輔助圈選（供標注者確認覆蓋範圍），再選擇對應的圖片級嚴重程度標籤（A 至 F）。
4. 完成後匯出標注結果（JSON 格式）。
5. 解析匯出結果，僅擷取每張裁切圖的圖片級等級標籤，忽略邊界框座標，將各樣本依標籤歸入 A 至 F 對應等級的子目錄，建立可供 ImageFolder 讀取的資料集。

需說明的是，邊界框僅作為標注者的視覺確認輔助，並未進入模型訓練；本研究之模型訓練與測試全程使用圖片級等級標籤，不涉及目標偵測任務。

標注完成後，A 級 546 張、B 級 87 張、C 級 213 張、D 級 160 張、E 級 72 張、F 級 32 張，共 1110 張有效資料。

## 模型架構與訓練設計 {#sec:method-model}

### 模型架構 {#sec:method-model-arch}

#### 骨幹網路選擇之考量 {#sec:method-model-rationale}

本研究選用 MobileNetV3-Large 作為主要骨幹，並以 ResNet18、EfficientNet-B0 為對照基準，主要考量如下：

1. **參數量與小樣本過擬合風險**：1110 張資料規模偏小，過大模型容易過擬合。三個候選模型之參數量與計算量詳見第二章表 \ref{tab:model-complexity}，皆屬輕量級。相較之下 ResNet50（25.6M）或 ViT-Base（86M）參數量過大，在此資料規模下需更強之資料增強與正則化策略才能避免過擬合。
2. **推論效率與未來部署彈性**：MobileNetV3 系列原為行動端與邊緣裝置設計，其 219 MFLOPs 計算量明顯低於 ResNet18（約 1.8 GFLOPs）；本研究於配備 RTX 3050 Laptop GPU 之筆記型電腦上訓練與推論，未來若需離線現場部署，可再評估工業電腦、Raspberry Pi 或 Jetson 系列等邊緣裝置。實測單張推論時間 6.90 ms 亦支持批量處理需求。
3. **ImageNet 預訓練權重可用性**：MobileNetV3-Large 可直接載入 torchvision 提供之 ImageNet 預訓練權重，遷移學習成本低。
4. **與相近研究之可比較性**：ResNet18 為小資料瑕疵檢測之常用基準，EfficientNet-B0 為近年主流輕量模型代表，三者並列可同時涵蓋「移動端最佳化」「殘差網路經典」「複合縮放最佳化」三條設計哲學，為後續研究者提供可比較之基準模型。方法路線（有監督分類 vs. 異常偵測）之選擇依據詳見第二章 \ref{sec:literature-cv-dl} 節。

本研究兩組設定（簡化與完整）均採用**全層微調（Full Fine-tuning）**策略---骨幹所有層均參與梯度更新，而非僅訓練新增的分類頭。在 1110 張資料規模下，全層微調的過擬合風險主要透過 Dropout、資料增強與正則化損失控制；特徵提取（Feature Extraction，凍結骨幹）策略未在本研究探索，列為後續比較方向。

選擇之 trade-off 在於：未涵蓋 Vision Transformer 系列（如 ViT-Tiny、DeiT-Tiny）、ConvNeXt 系列等新架構，亦未探討 self-supervised pre-training（如 DINO、MAE）對小樣本任務之助益，此屬本研究範圍限制，列為後續研究方向。

#### 雙輸出架構 {#sec:method-model-dualhead}

本研究採用 MobileNetV3-Large[@howardSearchingMobileNetV32019]（ImageNet V2 預訓練）作為骨幹網路，以遷移學習方式進行六分類微調。模型的特徵提取路徑為：backbone features 模組 → AdaptiveAvgPool → Flatten → classifier[:3]（Linear(960→1280) + Hardswish + Dropout(0.2)），輸出 1280 維特徵向量。在此 1280 維特徵向量之上接兩個並行輸出頭：

**分類頭**：Dropout（$p = 0.4$）→ Linear(1280→6)，輸出六類 logits。

**品質評分輔助頭**：Dropout（$p = 0.2$）→ Linear(1280→64) → ReLU → Linear(64→1) → Sigmoid，輸出範圍 0 至 1 的連續品質分，乘以 100 即得 0 至 100 分。

訓練時分類頭與評分頭同步優化。需特別說明的是，現行品質分輔助頭以「等級編號之線性轉換」（A=1.0, B=0.8, \ldots, F=0.0）作為迴歸目標（$\text{score\_gt} = 1 - \text{label} / 5$），**隱含假設等級間距相等且 ordinal 關係由 MSE loss 隱式建模**；然而此等距假設在感知品質層面未必成立---A→B（幾乎無拉絲至 1～2 根短絲）的感知品質差異，未必等同於 E→F（大量拉絲至結構幾乎難以辨識）的差異，實際主觀品質曲線在嚴重端（D/E/F）可能較為陡峭，而在輕微端（A/B/C）較為平緩，但在缺乏多人連續評分校準資料的條件下無法量化此偏差（詳見 \ref{sec:conclusion-future} 節第七項建議）。此外，Mixup 啟用時，評分監督目標 $\text{score\_gt}$ 僅以混合前第一個樣本的標籤（$y_a$）計算，未對第二個樣本標籤（$y_b$）做線性插值；此為實作層面的簡化，可能在跨等級混合樣本上引入輕微監督不一致，列入後續改進項目。嚴格而言，本研究將 ordinal classification 任務以「nominal classification + auxiliary regression」近似處理，未採用 ordinal-aware loss（如 CORAL [@caoRankConsistentOrdinal2020]、CORN [@shiDeepNeuralNetworks2023]）或 ordinal regularization。此為方法層級之簡化，列入 \ref{sec:conclusion-future} 節後續研究方向。

本研究依不同的資料切分與策略組合進行多組訓練（如表 \ref{tab:training-scripts} 所示）。需特別區分的是，「多 seed」在本文中僅指同一份 1110 張資料、相同 Group Split 流程與相同模型 / 設定下，更換\textbf{亂數種子值（seed，即隨機數生成器的初始化數值）}後重複訓練與測試；資料逐步擴充時產生的歷史版本不列入多 seed 統計。本文使用之五個種子值依序為 \textbf{7、42、123、1234、2024}；「seed=X」在本文中均表示亂數種子值等於 X，與訓練執行的先後順序無關。

\begin{table}[H]
\centering
\caption{本研究各訓練紀錄之角色對照}
\label{tab:training-scripts}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
\hline
\textbf{紀錄類型} & \textbf{實際完成內容} & \textbf{在本研究之角色} \\
\hline
\makecell[c]{歷史訓練版本} & \makecell[c]{資料量與設定隨研究進程改變} & \makecell[c]{觀察資料擴充與模型演進\\不列入多 seed 統計} \\
\makecell[c]{Group Split\\seed=7 詳細案例} & \makecell[c]{同一 168 筆嚴格測試集\\比較 MobileNet 簡化 / 完整\\與兩個完整基準模型} & \makecell[c]{混淆矩陣、品質分、校準\\與視覺化分析案例} \\
\makecell[c]{正式五 seed 比較} & \makecell[c]{4 組模型 / 設定 $\times$ 5 seeds\\共 20 筆訓練紀錄} & \makecell[c]{判斷模型 / 策略差異\\是否穩定} \\
\makecell[c]{seed=7 診斷實驗} & \makecell[c]{4 組單變因消融\\+ 1 組 100 epoch 檢查} & \makecell[c]{診斷訓練元件影響\\不作多 seed 結論} \\
\hline
\end{tabular}
\end{table}

\noindent 表 \ref{tab:training-scripts} 中，正式五 seed 比較僅包含 MobileNetV3-Large 簡化、MobileNetV3-Large 完整、ResNet18 完整與 EfficientNet-B0 完整四組；單變因消融與 100 epoch 檢查僅在 seed=7 下完成，因此本文將其定位為診斷實驗，而非穩定性結論。

**Group Split 切分比例**：以 GroupShuffleSplit 兩步切割。第一刀從全資料取 15\% 原圖群組為測試集；第二刀從剩餘 85\% 中取 17.6\% 為驗證集（$17.6\% \times 85\% \approx 15\%$），最終三分法近似 70/15/15。seed=7（亂數種子值為 7）詳細案例之切分結果為訓練 774 張、驗證 168 張、測試 168 張，且訓練、驗證、測試三者之原圖群組零重疊；另以 seed = 42、123、1234、2024 依完全相同流程各重複一次，共五個不同種子值、同一份 1110 張資料，以評估小樣本切分與模型初始化對結果的影響。

MobileNetV3-Large 兩組策略（完整 vs 簡化）使用相同骨幹、輸入尺寸、批次大小與輔助頭結構，主要差在分類損失、Mixup 與資料採樣方式：

\begin{equation}
\begin{aligned}
L_{\text{full}}  &= L_{\text{Focal}}(\gamma=2.0,\,\text{LS}=0.1) + 0.3 \times L_{\text{MSE}} \\
L_{\text{plain}} &= L_{\text{CE}} + 0.3 \times L_{\text{MSE}}
\end{aligned}
\label{eq:total-loss}
\end{equation}

\noindent 其中 $L_{\text{full}}$ 對應完整設定，$L_{\text{plain}}$ 對應簡化設定。係數 0.3 為經驗設定：初步實驗中 $L_{\text{Focal}}$ 與 $L_{\text{MSE}}$ 在訓練初期量級相近（均在 0.5$\sim$2.0 區間），0.3 使評分輔助頭提供穩定梯度而不壓過分類損失；若兩損失量級差異較大，此係數應重新調整。Mixup 啟用時，Focal Loss 以混合比例 $\lambda$ 線性組合兩個硬標籤的 CE，再套用焦點加權 $(1-p_t)^\gamma$，其中 $p_t = \exp(-(\lambda \cdot \text{CE}_a + (1-\lambda) \cdot \text{CE}_b))$；此做法等效於 MixFocal，在技術上偏離 Focal Loss 的原始設計（針對固定硬標籤），屬本研究之簡化取捨。另需說明，完整設定同時啟用 Focal Loss 與 Label Smoothing 存在一項理論張力：Focal Loss 的加權因子 $(1-p_t)^\gamma$ 依賴模型對正確類別的預測機率 $p_t$---$p_t$ 愈高代表該樣本愈「容易」，Focal Loss 降低其損失權重，使訓練聚焦於困難樣本；但 Label Smoothing 將目標由硬標籤 1.0 軟化至 $1-\epsilon=0.9$，在訓練過程中人為限制了 $p_t$ 的上限，使模型即便對多數類別預測「幾乎確定」時，也因目標被軟化而無法觸發 Focal Loss 應有的強降權，實質上削弱了 Hard Example Mining 的效果。本研究未對「FL only」、「LS only」與「FL+LS」進行單獨消融，無法量化此組合是否優於單獨使用任一機制，此組合屬方法論簡化取捨，列為後續改進項目。

seed=7 詳細分析中，簡化設定於同一 Group Split 測試集取得 86.31\%（145/168），可作為後續混淆矩陣、校準與可視化的代表案例；但五 seed 重複後，簡化設定與完整設定在 accuracy / QWK 上未呈現顯著差異，因此本文不再將單次 86.31\% 解讀為策略穩定勝出，而是將其定位為可重現的嚴格切分基準。兩組設定之超參數整理於表 \ref{tab:hyperparameters}。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 訓練超參數設定（共用設定）}
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
學習率排程 & \makecell{CosineAnnealing\\WarmRestarts} & \makecell{$T_0=20$, $T_{\text{mult}}=2$\\$\eta_{\min}=10^{-6}$；\\25 epoch 內僅完成\\首次餘弦衰減與\\epoch 20 的 warm restart} \\
Dropout & \makecell{分類頭 $p=0.4$\\評分頭 $p=0.2$} & \makecell{兩組\\共用} \\
訓練精度 & FP16 Mixed Precision & GPU 加速 \\
\hline
\end{tabular}
\end{table}

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 訓練超參數設定（兩組策略差異）}
\label{tab:hyperparameters-diff}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
\hline
\textbf{超參數} & \textbf{設定值} & \textbf{說明} \\
\hline
分類損失 & \makecell{完整：Focal $\gamma=2.0$\\＋LS 0.1} & 候選策略 \\
         & 簡化：Cross Entropy            & 目前主要設定 \\
Mixup Alpha & \makecell{完整：0.3\\簡化：0.0} & 批次層級線性混合 \\
過採樣 & \makecell{完整：WeightedRandomSampler\\（0.75 次方反比；每 epoch\\抽 774×6=4644 次）} & \makecell{0.75 次方介於不加權（0）\\與完全反比（1.0）之間，\\避免少數類過度放大} \\
       & 簡化：無加權，隨機洗牌 & --- \\
最大輪數 & \makecell{正式補充實驗：25\\100 epoch 檢查：100} & --- \\
EarlyStopping Patience & \makecell{正式補充實驗：7\\100 epoch 檢查：35} & 監控驗證準確率 \\
\hline
\end{tabular}
\end{table}

\par\noindent\small\textit{正式五 seed 比較與 seed=7 單變因消融皆依實驗計畫使用 25 epoch、patience=7；僅 MobileNetV3-Large 簡化設定另做 100 epoch、patience=35 檢查，用來觀察較長訓練預算下結果是否改變。}

# 實驗結果與分析 {#sec:results}

## 資料集統計分析 {#sec:results-dataset}

本研究有效樣本共 1110 張，依品質等級分布如表 \ref{tab:dataset-dist} 及圖 \ref{fig:dataset-dist} 所示。A 等級（完美品）佔比最高，共 546 張；B 級 87 張、C 級 213 張、D 級 160 張、E 級 72 張、F 級 32 張。此分布反映資料仍具明顯類別不平衡，尤其 B、E、F 等級樣本數偏少，因此後續結果需同時參照 macro-F1、QWK、跨等級誤判與各等級 support，而不能只看整體 accuracy。

\begin{table}[H]
\centering
\caption{全資料集各等級分布}
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
D & 中度拉絲 & 160 & 14.4\% & 中度瑕疵樣本 \\
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

## 實驗紀錄口徑與 Group Split 切分 {#sec:results-record-scope}

本章僅採用實驗資料夾中已完成且可追溯之紀錄進行分析。正式多 seed 比較包含 4 組模型 / 設定、5 個 seed，共 20 筆訓練紀錄；另有 seed=7 下的 4 組單變因消融與 1 組 100 epoch 檢查，共 5 筆診斷紀錄。換言之，本研究實際用於本章的補充訓練紀錄為 25 筆，並非 9 組設定皆完成 5 seed。

Group Split 以原始照片 ID 為分組單位。seed=7 詳細分析案例之資料切分如表 \ref{tab:gs-split-summary} 所示；訓練、驗證與測試之間沒有原圖群組重疊，因此可降低同一張原圖裁切出的魚骨同時出現在訓練與測試中的資料洩漏風險。

\begin{table}[H]
\centering
\caption{seed=7 Group Split 切分與測試集分布（切分比例近似 70/15/15；B、E、F 類樣本數偏少，解讀百分比時須考量基數）}
\label{tab:gs-split-summary}
\small
\setlength{\tabcolsep}{3pt}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{ccccccc}
\hline
\textbf{總樣本} & \textbf{原圖群組} & \textbf{訓練集} & \textbf{驗證集} & \textbf{測試集} & \makecell{\textbf{測試集}\\\textbf{A/B/C}} & \makecell{\textbf{測試集}\\\textbf{D/E/F}} \\
\hline
1110 & 185 & 774 & 168 & 168 & 77 / 16 / 35 & 28 / 8 / 4 \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

## seed=7 詳細案例：同一測試集下的模型比較 {#sec:results-seed7}

表 \ref{tab:seed7-results} 整理 seed=7、同一 Group Split 測試集下四組主要模型 / 設定之結果。此處的最佳單次結果為 MobileNetV3-Large 完整設定，accuracy 為 89.88\%（151/168）；但此僅代表單一 seed 與單一切分下的結果，不能直接視為穩定最佳模型。此外，完整設定因 WeightedRandomSampler 每 epoch 訓練步數（145 步）約為簡化設定（24 步）的六倍，兩者在 seed=7 上的差距（89.88\% vs 86.31\%）同時反映訓練策略差異與累積計算量差異，無法單獨歸因於策略優劣；相關說明詳見 \ref{sec:results-supplemental-ablation} 節。

由於 seed=7 測試集中 B、E、F 等級分別只有 16、8、4 張，少數類別的 precision、recall 與 macro-F1 容易受到少量樣本變動影響。因此，本節將 seed=7 視為可檢查混淆矩陣、校準與視覺化的詳細案例；真正的模型 / 策略排序仍以五 seed 平均與配對檢定為主要依據。

\begin{table}[H]
\centering
\caption{seed=7 主要模型 / 設定於同一 Group Split 測試集之結果（seed=7 單次案例；穩定性判斷以表 \ref{tab:multiseed-results} 五 seed 結果為準）}
\label{tab:seed7-results}
\small
\setlength{\tabcolsep}{3pt}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{lccccc}
\hline
\textbf{模型 / 設定} & \textbf{Accuracy} & \textbf{Macro-F1} & \textbf{QWK} & \makecell{\textbf{跨等級}\\\textbf{誤判}} & \textbf{訓練時間} \\
\hline
\makecell[l]{MobileNetV3-Large\\簡化} & 86.31\% & 0.791 & 0.932 & 2.98\% & 6.2 分 \\
\makecell[l]{MobileNetV3-Large\\完整} & \textbf{89.88\%} & \textbf{0.834} & \textbf{0.967} & 1.19\% & 27.5 分 \\
ResNet18 完整 & 84.52\% & 0.783 & 0.954 & 1.19\% & 31.2 分 \\
EfficientNet-B0 完整 & 82.14\% & 0.729 & 0.951 & 1.19\% & 21.2 分 \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

表 \ref{tab:seed7-perclass} 為 MobileNetV3-Large 簡化設定於 seed=7 測試集之各等級精確率、召回率與 F1 分數。**B 等級召回率僅 56.3\%（9/16），為六等級中最低**：5 張 B 等級樣本被誤判為 A 等級（良品誤判為完美品）。此方向誤判在工業應用上相對可接受（漏判瑕疵影響較小），但亦反映 A/B 邊界在少量細絲辨識上存在困難，與 \ref{sec:results-quality-score} 節 B 等級品質分偏高（89.0 分 vs 目標 80 分）的觀察相互印證，說明 A/B 邊界是本系統最薄弱環節。C/D 邊界混淆同樣顯著（C→D 有 7/35、D→C 有 2/28）；D→A 出現 2 次跨等級誤判，可能與特定拍攝角度下拉絲特徵被遮蔽有關。E、F 各 8、4 張，統計解讀須謹慎。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 簡化設定 seed=7 各等級精確率、召回率與 F1（測試集 168 張）}
\label{tab:seed7-perclass}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{lcccc}
\hline
\textbf{等級（名稱）} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} & \textbf{Support} \\
\hline
A（完美品）   & 0.917 & 1.000 & 0.957 & 77 \\
B（良好品）   & 0.900 & 0.563 & 0.692 & 16 \\
C（輕微拉絲） & 0.900 & 0.771 & 0.831 & 35 \\
D（中度拉絲） & 0.719 & 0.821 & 0.767 & 28 \\
E（嚴重拉絲） & 0.750 & 0.750 & 0.750 & 8 \\
F（失敗品）   & 0.750 & 0.750 & 0.750 & 4 \\
\hline
Macro avg     & 0.823 & 0.776 & 0.791 & 168 \\
\hline
\end{tabular}
\end{table}

\par\noindent\small\textit{B 等級召回率（56.3\%）為六等級最低，5 張誤判均流向 A 等級；D 等級有 2 張跳至 A（跨等級大跳）；\textbf{E（8 張）與 F（4 張）等級樣本數過少，F 等級一張誤判即造成 Recall 變動 25\%，表中 P/R/F1 無統計意義，僅供觀察，不應作為此兩等級效能之穩定估計。}}

圖 \ref{fig:confusion-matrix} 為 seed=7 MobileNetV3-Large 簡化設定之混淆矩陣。對角線代表正確分類；非對角線誤判集中於相鄰等級（A/B、C/D、E/F），符合序數分類的預期行為；D→A 的 2 次跨等級誤判為本研究最需注意的誤判模式。

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth,height=0.62\textheight,keepaspectratio]{images/new-model-confusion-matrix.png}
\caption{seed=7 MobileNetV3-Large 簡化設定混淆矩陣（測試集 168 張，Group Split 原圖零重疊）}
\label{fig:confusion-matrix}
\end{figure}

## 五 seed 穩定性與顯著性檢定 {#sec:results-supplemental-multiseed}

為檢查 seed=7 的排序是否穩定，本研究對 MobileNetV3-Large 簡化、MobileNetV3-Large 完整、ResNet18 完整與 EfficientNet-B0 完整四組模型 / 設定，以 seed = 7, 42, 123, 1234, 2024 重複 Group Split、訓練與測試。五 seed 平均結果如表 \ref{tab:multiseed-results} 所示。

\begin{table}[H]
\centering
\caption{五個 seed 之 Group Split 測試表現（mean $\pm$ std, n=5）}
\label{tab:multiseed-results}
\small
\setlength{\tabcolsep}{3pt}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{lccccc}
\hline
\textbf{模型 / 設定} & \textbf{Accuracy} & \textbf{Macro-F1} & \textbf{QWK} & \makecell{\textbf{跨等級}\\\textbf{誤判}} & \textbf{平均時間} \\
\hline
\makecell[l]{MobileNetV3-Large\\簡化} & 81.19 $\pm$ 3.71\% & 0.661 $\pm$ 0.079 & 0.921 $\pm$ 0.009 & 3.10 $\pm$ 0.27\% & 6.6 $\pm$ 1.0 分 \\
\makecell[l]{MobileNetV3-Large\\完整} & 80.12 $\pm$ 5.98\% & \textbf{0.713 $\pm$ 0.070} & 0.909 $\pm$ 0.039 & 3.45 $\pm$ 1.70\% & 20.0 $\pm$ 5.6 分 \\
ResNet18 完整 & 80.83 $\pm$ 2.16\% & 0.712 $\pm$ 0.057 & 0.914 $\pm$ 0.032 & 3.33 $\pm$ 1.91\% & 23.9 $\pm$ 4.8 分 \\
EfficientNet-B0 完整 & 81.19 $\pm$ 2.25\% & 0.698 $\pm$ 0.031 & 0.910 $\pm$ 0.039 & 3.57 $\pm$ 2.10\% & 24.3 $\pm$ 3.3 分 \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

以 MobileNetV3-Large 簡化設定作為比較基準之 paired t-test 如表 \ref{tab:paired-ttest} 所示。五 seed 結果顯示，其他模型 / 設定相對於簡化設定之 accuracy 與 QWK 差異皆未達統計顯著；MobileNetV3-Large 完整與 ResNet18 完整在 macro-F1 上較高，且探索性檢定達 \(p<0.05\)，表示完整策略或 ResNet18 對少數類別與類別邊界可能較有幫助。然而，這些檢定僅有五組 paired observations，且未進行多重比較校正；若以 Bonferroni 校正三個比較（$\alpha_{\text{corrected}} = 0.05/3 \approx 0.0167$），MobileNetV3-Large 完整之 macro-F1（$p=0.0246$）與 ResNet18 完整之 macro-F1（$p=0.0363$）均不達顯著，結論應進一步保守解讀為「探索性趨勢，不排除機會誤差」；再加上 accuracy 與 QWK 未同步顯著提升，本文不宣稱任何單一設定為穩定最佳模型。

\begin{table}[H]
\centering
\caption{相對 MobileNetV3-Large 簡化之 paired t-test（n=5）}
\label{tab:paired-ttest}
\footnotesize
\setlength{\tabcolsep}{3pt}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{lcccccc}
\hline
\textbf{比較模型} & \makecell{\textbf{Acc}\\\textbf{差異}} & \makecell{\textbf{Acc}\\$p$} & \makecell{\textbf{Macro-F1}\\\textbf{差異}} & \makecell{\textbf{Macro-F1}\\$p$} & \makecell{\textbf{QWK}\\\textbf{差異}} & \makecell{\textbf{QWK}\\$p$} \\
\hline
EfficientNet-B0 完整 & 0.00 pp & 1.000 & +0.038 & 0.295 & -0.011 & 0.540 \\
\makecell[l]{MobileNetV3-Large\\完整} & -1.07 pp & 0.621 & +0.052 & \textbf{0.0246} & -0.011 & 0.502 \\
ResNet18 完整 & -0.36 pp & 0.745 & +0.052 & \textbf{0.0363} & -0.006 & 0.604 \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

## seed=7 單變因消融與 100 epoch 檢查 {#sec:results-supplemental-ablation}

表 \ref{tab:ablation-results} 整理 seed=7 下之消融與 100 epoch 檢查。每列「移除 X」代表**僅移除 X，其餘訓練元件（Focal Loss、Label Smoothing、Mixup、Weighted Sampler）均保留**；例如「移除 Focal Loss」仍保有 Label Smoothing、Mixup 與 Weighted Sampler。此表用來診斷完整策略中各訓練元件的影響，但因僅有單一 seed，不能作為穩定性結論。從此單次結果看，移除 Weighted Random Sampler 時 accuracy 為 83.33\%，QWK 為 0.910，跨等級誤判為 4.17\%；相較之下，移除 label smoothing 在此 seed 下得到 88.10\% accuracy。此現象只能說明 seed=7 下 label smoothing 未帶來改善，不能推論所有 seed 皆如此。

訓練時間欄位有兩點須特別注意：

**（1）WeightedRandomSampler 造成步數差異**：完整設定（27.5 分）與簡化設定（6.2 分）差距的主因是 `num_samples=774×6=4644`，使完整設定每 epoch 執行 $4644 \div 32 \approx 145$ 步，而簡化設定每 epoch 僅 $774 \div 32 \approx 24$ 步。名義上同為 25 epoch，但完整設定等效訓練步數約為簡化設定的 6 倍；移除 Weighted Sampler（7.8 分）因此回歸正常步數，訓練時間接近簡化設定。

**（2）EarlyStopping 造成實際 epoch 數差異**：「移除 Focal Loss」（34.0 分）比「完整設定」（27.5 分）更長，**原因是驗證準確率在 patience=7 窗口內未觸發 Early Stopping，實際跑到更多 epoch**（而完整設定在更早 epoch 達到峰值後觸發停止）。因此消融表中的訓練時間反映的是「該設定在 seed=7 下實際訓練的總 epoch $\times$ 步數」，而非純粹的每步計算成本差異，不能直接用訓練時間比較各設定的計算效率。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large seed=7 單變因消融與 100 epoch 檢查}
\label{tab:ablation-results}
\small
\setlength{\tabcolsep}{3pt}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{lccccc}
\hline
\textbf{實驗} & \textbf{Accuracy} & \textbf{Macro-F1} & \textbf{QWK} & \makecell{\textbf{跨等級}\\\textbf{誤判}} & \textbf{訓練時間} \\
\hline
完整設定 & \textbf{89.88\%} & 0.834 & \textbf{0.967} & 1.19\% & 27.5 分 \\
移除 Focal Loss & 86.31\% & 0.775 & 0.958 & 1.19\% & 34.0 分 \\
移除 Label Smoothing & 88.10\% & \textbf{0.837} & 0.963 & 1.19\% & 28.3 分 \\
移除 Mixup & 85.71\% & 0.776 & 0.958 & 1.19\% & 19.0 分 \\
移除 Weighted Sampler & 83.33\% & 0.737 & 0.910 & 4.17\% & 7.8 分 \\
簡化設定 & 86.31\% & 0.791 & 0.932 & 2.98\% & \textbf{6.2 分} \\
簡化設定（100 epoch） & 86.31\% & 0.791 & 0.932 & 2.98\% & 13.8 分 \\
\hline
\end{tabular}
\end{adjustbox}
\end{table}

## 品質分數與全資料回測 {#sec:results-quality-score}

MobileNetV3-Large 簡化設定之品質分輔助頭以 A=100、B=80、C=60、D=40、E=20、F=0 作為監督目標。表 \ref{tab:plain-quality-score} 依實驗紀錄整理 seed=7 Group Split 測試集與全資料回測之各等級平均分。測試集與全資料回測皆呈 A \(>\) B \(>\) C \(>\) D \(>\) E \(>\) F 的排序，因此可作為分類結果之外的輔助排序訊號；但 B、D、E、F 等級平均分與目標分數仍有偏差，且全資料回測包含訓練樣本，不能視為泛化能力證據。其中偏差較大者為：B 等級測試集均分 89.0 分（目標 80 分，偏高 9.0 分）、D 等級 54.5 分（目標 40 分，偏高 14.5 分）、F 等級 12.5 分（目標 0 分，偏高 12.5 分）。這些偏差並非隨機分散，而呈現有方向性的系統偏高：B 等級偏高與其低召回率（56.3\%）直接相關---被誤判為 A 的樣本以接近 100 分的高品質分輸出，拉高 B 的預測均分；D 等級偏高則對應 C/D 邊界混淆，部分 D 等級樣本被誤判為 C 而輸出 60 分附近的評分，使 D 的均分上移。此分析間接印證等間距假設的侷限：品質分偏差既反映邊界分類不確定性，也可能反映各等級感知差距並非線性等距。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 簡化設定品質分對照}
\label{tab:plain-quality-score}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{lcccc}
\hline
\textbf{等級} & \textbf{目標分數} & \makecell{\textbf{測試集}\\\textbf{平均分}} & \makecell{\textbf{全資料回測}\\\textbf{平均分}} & \makecell{\textbf{全資料回測}\\Recall} \\
\hline
A 完美品 & 100 & 99.6 & 99.5 & 1.000 \\
B 良好品 & 80 & 89.0 & 88.3 & 0.540 \\
C 輕微拉絲 & 60 & 58.8 & 60.5 & 0.831 \\
D 中度拉絲 & 40 & 54.5 & 50.9 & 0.863 \\
E 嚴重拉絲 & 20 & 23.5 & 30.8 & 0.542 \\
F 失敗品 & 0 & 12.5 & 16.2 & 0.688 \\
\hline
\end{tabular}
\end{table}

\par\noindent\small\textit{測試集平均分來自 seed=7 Group Split 測試紀錄；全資料回測為 1110 張樣本回測，包含訓練資料，僅供觀察模型對已標注資料的擬合與品質分排序。}

全資料回測整體準確率為 87.30\%（969/1110），macro-F1 為 0.779。由於此結果包含訓練資料，本文僅將其作為擬合度與批量流程檢查，不作為未見資料泛化能力的主要指標。

## 校準分析與視覺化診斷 {#sec:results-supplemental-calibration}

**模型校準**：以 seed=7 MobileNetV3-Large 簡化模型進行 confidence calibration。未校準 ECE 為 0.0576；temperature scaling[@guoCalibrationModern2017]（\(T=1.525\)）後 ECE 降至 0.0435。圖 \ref{fig:calibration-reliability} 為校準前後之 reliability diagram：校準後信心分布更接近對角線（理想校準），尤其在高信心區間的過信問題有所改善。高信心樣本（confidence \(>0.9\)）共有 112/168 張，準確率 95.5\%；低信心樣本（confidence \(<0.7\)）共有 28/168 張，準確率 46.4\%，落差顯著。因此，confidence 可作為人工複核流程的分流門檻：低信心預測不宜直接自動通過，建議進入人工確認。

\begin{figure}[H]
\centering
\includegraphics[width=0.88\textwidth,height=0.5\textheight,keepaspectratio]{images/calibration-reliability.png}
\caption{模型校準前後 reliability diagram（seed=7 MobileNetV3-Large 簡化設定；temperature scaling $T=1.525$）}
\label{fig:calibration-reliability}
\end{figure}

**PR 曲線分析**：One-vs-rest PR 曲線如圖 \ref{fig:pr-curves}。各等級 AP 如下：A 級 0.997、B 級 0.863、C 級 0.959、D 級 0.840、E 級 0.797、F 級 0.788。B、D、E、F 等少數類別或邊界類別 AP 均低於 0.90，其中 E、F AP 最低（分別為 0.797、0.788），反映樣本稀少與等級邊界模糊的雙重挑戰。One-vs-rest ROC 分析中，各等級 AUC 均超過 0.96（A：0.998、B：0.968、C：0.986、D：0.963、E：0.987、F：0.989），顯示模型在二元區分上的整體辨識力良好，但精確率與召回率之間的取捨仍是少數類別的主要瓶頸。此類曲線分析用於診斷模型行為，不取代正式五 seed 統計。

\begin{figure}[H]
\centering
\includegraphics[width=0.92\textwidth,height=0.55\textheight,keepaspectratio]{images/curves-pr.png}
\caption{One-vs-rest PR 曲線（seed=7 MobileNetV3-Large 簡化設定；各等級 AP 標示於圖例）}
\label{fig:pr-curves}
\end{figure}

**Grad-CAM 視覺解釋**：圖 \ref{fig:gradcam-correct} 與圖 \ref{fig:gradcam-wrong} 分別為預測正確與預測錯誤樣本的 Grad-CAM 熱力圖。本研究以手動掛載 forward/backward hook 的方式，對 MobileNetV3-Large \texttt{feature\_net[0][-1]}（features 模組末段最後一個 InvertedResidual block）之卷積輸出執行 Grad-CAM；熱力圖以 Jet colormap 生成後依 $0.55 \times \text{原圖} + 0.45 \times \text{熱力圖}$ 疊加顯示。展示樣本取各等級中「第一個」正確或錯誤預測樣本（依資料集索引順序，非隨機抽樣或人工精選），讀者解讀時應注意樣本選取並非追求最佳視覺效果。正確預測案例中，熱力圖高亮區域主要集中於魚骨間隙的拉絲細絲區域，顯示模型已學習從拉絲密度與分布特徵進行等級判斷，而非依賴樣本背景顏色或外輪廓。錯誤預測案例中（多為 A/B 或 C/D 邊界樣本），熱力圖出現分散或集中於非拉絲區域的情形，提示邊界樣本的特徵歧義性是誤判的主因，與 \ref{sec:results-seed7} 節 B 等級低召回率的觀察一致：B 等級中被誤判為 A 的樣本，模型對拉絲細絲的激活強度明顯偏低。

\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth,height=0.55\textheight,keepaspectratio]{images/gradcam-correct-grid.png}
\caption{預測正確樣本 Grad-CAM 熱力圖（熱力集中於拉絲細絲與魚骨間隙區域）}
\label{fig:gradcam-correct}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth,height=0.55\textheight,keepaspectratio]{images/gradcam-wrong-grid.png}
\caption{預測錯誤樣本 Grad-CAM 熱力圖（熱力分散或偏向非關鍵區域，多為相鄰等級邊界樣本）}
\label{fig:gradcam-wrong}
\end{figure}

**t-SNE 特徵可視化**：圖 \ref{fig:tsne} 為 seed=7 測試集（168 張）之 1280 維特徵向量以 t-SNE（perplexity=30，random\_state=7，\texttt{init=`pca'}）降維後的散佈圖。A 等級（無拉絲）形成緊密且獨立的聚落；C/D 等級部分樣本邊界相互滲透，與混淆矩陣中 C/D 誤判率較高的現象一致；B 等級聚落與 A 等級部分重疊，解釋了 5 張 B 等級樣本被誤判為 A 的現象。E/F 等級因樣本數過少（各 8/4 張），聚落位置解讀需謹慎。整體而言，特徵空間已形成具意義的等級區隔，但相鄰等級存在相互滲透的邊界區域，符合序數分類任務中等級邊界天然模糊的特性。

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth,height=0.62\textheight,keepaspectratio]{images/tsne-test-features.png}
\caption{seed=7 測試集 1280 維特徵之 t-SNE 視覺化（perplexity=30，168 個樣本，顏色對應 A 至 F 等級）}
\label{fig:tsne}
\end{figure}

## 外部未標注影像診斷 {#sec:results-supplemental-ood}

外部未標注資料共 105 張照片，裁切為 630 支魚骨後進行推論。預測分布如圖 \ref{fig:external-dist} 所示：A/B/C/D/E/F = 417/14/82/75/30/12，A 等級佔比 66.2\%，整體分布偏向良品側，與訓練集 A 等級 49.2\% 佔比相比更為集中，可能反映外部照片中良品比例較高或光線條件使拉絲特徵不易被偵測。平均 confidence 為 0.919，其中 confidence \(<0.7\) 者有 74 支（11.7\%）；相較測試集中低信心比例（28/168 = 16.7\%），外部資料低信心比例偏低，顯示模型整體輸出分布正常，未出現明顯崩潰或全部集中單一類別的異常現象。由於此批資料沒有人工標籤，本文不計算也不宣稱 OOD accuracy；其用途僅是確認模型對外部照片不會產生明顯異常輸出，並作為未來建立具人工標籤 OOD 測試集之前置檢查。需特別說明：預測分布偏向良品側（A 等級 66.2\%，高於訓練集 49.2\%）有兩種可能解釋：（1）外部照片中良品比例確實較高；（2）模型在拍攝條件略有不同的樣本上傾向以高信心輸出 A 等級（即高信心誤判）。兩者在缺乏人工標籤的情況下無法區分。「預測分布正常、未崩潰」是模型可用性的\textbf{必要條件而非充分條件}---高信心誤判不會表現為分布崩潰，卻是工業應用中更危險的失效模式（系統誤判為通過但實際為瑕疵品）；因此本節結果不能推論為模型在外部拍攝條件下具備泛化能力，建議後續優先取得此批資料的人工標籤以區分兩種解釋。

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth,height=0.5\textheight,keepaspectratio]{images/external-unlabeled-distribution.png}
\caption{外部未標注 630 支魚骨推論之等級分布（無人工標籤，僅作 sanity check；A 等級佔 66.2\%）}
\label{fig:external-dist}
\end{figure}

## 補充實驗的解讀邊界 {#sec:results-supplemental-interpretation}

綜合上述實驗紀錄，本文採取以下解讀邊界：

1. seed=7 的 89.88\% 最高單次 accuracy 僅能作為單次案例，不代表穩定最佳模型。
2. 五 seed 後，各模型 / 設定 accuracy 與 QWK 差異未達顯著，因此不能宣稱某一策略在整體辨識率上穩定勝出。
3. MobileNetV3-Large 完整與 ResNet18 完整在 macro-F1 上之探索性檢定達 \(p<0.05\)，較合理的說法是完整策略或 ResNet18 對少數類別 / 邊界樣本可能較有幫助。
4. seed=7 消融只提供訓練元件診斷；在該次實驗中，Weighted Sampler 與較低跨等級誤判同時出現，但仍需更多 seed 才能作穩定結論。
5. 品質分與外部未標注檢查皆屬輔助分析。品質分未經人工連續評分校準，外部照片未標注，兩者皆不能取代嚴格測試集指標。

## 批量推論效能 {#sec:results-batch}

以 seed=7 MobileNetV3-Large 簡化模型於 168 張測試樣本量測，平均單張模型推論時間為 6.90 ms，約 144.9 張/秒；完整 Group Split 模型約 7.05 ms，約 141.8 張/秒。需特別說明量測條件：推論以 \textbf{batch\_size=1} 逐張送入 GPU，影像張量\textbf{預先載入記憶體}（量測時不含磁碟讀取、裁切、resize/normalize 等前處理耗時），並以 20 張 warm-up 後計時 168 張；所呈現數字為\textbf{純模型前向傳播延遲}，不代表含完整前處理的端到端吞吐量。實際部署場景中，前處理（影像讀取、裁切）與後處理（分級排序、報告生成）的耗時可能與推論本身相當，評估系統吞吐量時應一併納入。此結果顯示離線批量推論流程具初步可行性，但不等同於完整產線吞吐量；實際部署仍需額外評估資料讀取、裁切、人工複核與現場設備整合成本。

# 結論與建議 {#sec:conclusion}

## 結論 {#sec:conclusion-summary}

本研究建立了一套以深度學習影像辨識為核心的 3D 列印件拉絲瑕疵輔助辨識與品質評分原型，以 FDM 列印魚骨件為研究標的，完成六等級（A 至 F）分類與品質評分輸出流程。主要研究成果總結如下：

1. **單一標注者下之可重複品質等級制度**：以目視估計拉絲覆蓋比例為主要判斷依據，建立六個品質等級定義並配合 A 至 F 範例圖。本研究主張的是「模型在嚴格測試集上可部分逼近此套固定標注準則」，可降低批量檢查負擔並提供人工複核輔助；惟全部樣本由單一標注者完成、尚未進行多人一致性測試，故不宣稱已建立多人共識下的品質標準（標注一致性限制詳見 \ref{sec:results-supplemental-interpretation} 節）。
2. **系統性資料蒐集與標注**：透過多批次列印與拍攝，配合 Label Studio 工具完成全部樣本的人工標注，建立含 1110 張有效樣本、185 個原圖群組的六等級分類資料集；以原圖層級 Group Split 確保訓練、驗證與測試集之原圖零重疊，為後續模型效能評估提供無洩漏基準。
3. **深度學習模型效能與不確定性**：正式多 seed 比較包含 4 組模型 / 設定 $\times$ 5 seeds，共 20 筆紀錄。seed=7 詳細案例中，MobileNetV3-Large 簡化設定達 **86.31\%（145/168）**，完整設定在同一測試集達 **89.88\%（151/168）**；上述為單一 seed 案例，穩定性仍須以五 seed 統計判斷。各等級分析顯示 B 等級召回率僅 56.3\%（9/16），為六等級中最低，A/B 邊界辨識為本系統最薄弱環節（詳見表 \ref{tab:seed7-perclass} 與 \ref{sec:results-seed7} 節）。五 seed 重複後，各模型平均 accuracy 均落在 80.1\% 至 81.2\%，accuracy 與 QWK 之 paired t-test 未達顯著差異；惟 MobileNetV3-Large 完整與 ResNet18 完整之 macro-F1 在探索性檢定中達 \(p<0.05\)（詳見 \ref{sec:results-supplemental-multiseed} 節）。seed=7 單變因消融觀察到移除 Weighted Random Sampler 時跨等級誤判較高，但該消融僅為單次診斷，不作多 seed 穩定結論。模型校準後低 confidence 子集準確率明顯偏低（46.4\%），適合作為人工複核門檻；Grad-CAM 可視化確認模型正確預測時熱力圖集中於魚骨間隙的拉絲細絲區域（詳見 \ref{sec:results-supplemental-calibration} 節）。故系統定位為「品質管控輔助原型」，而非可獨立判定之自動分級系統。
4. **離線批量處理流程**：整合自動裁切、批量辨識、分級輸出與 HTML 可視化報告，形成由原始照片到品質等級報告的離線批量處理流程；主要簡化模型於 RTX 3050 Laptop GPU 單張模型推論約 6.90 ms（約 144.9 張/秒），完整設定模型約 7.05 ms（約 141.8 張/秒），驗證離線批量推論流程可行。惟此為單機模型推論量測，產線部署前仍需補做完整吞吐量、人工複核成本與現場穩定性評估。
5. **品質評分量化（未經人工校準）**：模型同時輸出 0 至 100 的連續品質分數。各等級平均分在 Group Split 測試集與全資料回測下均呈 A $>$ B $>$ C $>$ D $>$ E $>$ F 之單調遞減（數值詳見表 \ref{tab:plain-quality-score}），具輔助排序價值；惟目標分數採等級編號之線性轉換、未經多人主觀評分校準，B、D、E、F 等級之預測平均偏高，現階段僅作為分類結果之輔助連續指標，不宜作為絕對品質量化依據。

\vspace{0.5em}

**主要貢獻陳述（Take-home Message）**：

> 本研究可支持的核心結論是：在同一份 1110 張資料與原圖層級 Group Split 下，模型已具備輔助辨識 FDM 魚骨拉絲等級的可行性；但五 seed 結果不足以宣稱某一模型或訓練策略在 accuracy / QWK 上穩定最佳，且 A/B 邊界召回率（B 等級 56.3\%）為最主要的效能瓶頸。品質分、校準、Grad-CAM 與外部未標注檢查可協助理解模型行為，但仍需完成人工標注一致性驗證、建立具標籤 OOD 測試集與進行跨機型 / 跨材料驗證後，才能提高應用可信度。

## 建議 {#sec:conclusion-future}

根據本研究執行過程中的觀察與系統評估結果，提出以下建議供後續研究參考。其中第一項聚焦於尚未完成、且最直接影響應用可信度的驗證。

1. **優先補齊應用可信度驗證**。本研究已完成 Group Split、多 seed、單變因消融、100 epoch 檢查、模型校準、PR/ROC、t-SNE、Grad-CAM 與外部未標注 sanity check。後續最需要補強的是下列三項：

   * **【未完成】具人工標籤的 OOD 測試集**：目前外部 105 張照片僅完成未標注推論分布與 confidence 檢查，不能計算 OOD accuracy。建議補拍並人工標注涵蓋不同光源、背景、角度與相機條件的測試集，先確認各等級皆有代表樣本，再擴充至足以穩定估計各等級召回率與整體退化幅度的規模。
   * **【目前受限，保留為未來工作】標注一致性 Cohen's Kappa**：由於現階段無法取得第二位以上標注者重新標注，本文不計算也不推估 $\kappa$。若未來具備人力，建議重新標注 100 張涵蓋 A 至 F 之樣本並計算 Cohen's $\kappa$ / Fleiss' $\kappa$；若 $\kappa < 0.7$，需重新檢視標注準則並補充邊界判斷規則。
   * **【未完成】Ordinal-aware loss 對照**：本研究已補充 QWK、Cohen's $\kappa$ 與跨等級誤判率，但訓練目標仍是 nominal classification + MSE auxiliary regression。建議補做 CORAL [@caoRankConsistentOrdinal2020]、CORN [@shiDeepNeuralNetworks2023] 等 ordinal-aware loss，並以 QWK 與跨等級誤判率作為主要評估指標。

2. **完善基準模型比較之因子設計**。目前正式多 seed 比較包含 MobileNetV3-Large 簡化 / 完整、ResNet18 完整與 EfficientNet-B0 完整四組，尚缺 ResNet18 簡化與 EfficientNet-B0 簡化之組合；若要分離「架構差異」與「訓練策略差異」的獨立效果，仍需完整 3 架構 $\times$ 2 策略的因子設計，並以五 seed 統計判斷各因素之主效果。
3. **持續補充少數等級訓練資料**。雖然本研究資料集中 D 級已達 160 張，但 E 級僅 72 張、F 級僅 32 張，B 級 87 張相較 A 級亦偏少，未來建議優先補充 B 級邊界樣本、E 級嚴重拉絲樣本與 F 級失敗樣本，並以「足以支撐穩定估計與多 seed 分析」為目標逐步擴充，使各等級樣本分布更平均，進一步降低 B/C、D/E 與 E/F 邊界的誤判，提高結果的統計可信度。
4. **擴充至翹曲與裂痕瑕疵的辨識**。本研究因翹曲和裂痕的現有樣本不足，聚焦於拉絲瑕疵的六等級分類。未來可系統性地蒐集翹曲及裂痕樣本，建立涵蓋三種瑕疵類型的多標籤分類系統（Multi-label Classification），更全面地反映 FDM 列印件的品質狀態。
5. **跨機型 / 跨材料 / 跨幾何泛化能力驗證**。本研究僅於 Bambu Lab A1 + PLA + 魚骨形狀條件下訓練與測試。建議蒐集：(a) 其他桌上型印表機（如 Prusa MK4、Creality K1）；(b) 其他材料（PETG、ABS、TPU）；(c) 其他幾何形狀（盒體、齒輪、有機曲面）之樣本，組成跨域測試集，量化模型於不同硬體 / 材料 / 幾何下之效能退化幅度。此項與第 1 項之 OOD 拍攝條件驗證互補，前者聚焦「列印物本身之變異」，後者聚焦「影像獲取條件之變異」，兩者皆為評估本系統作為通用品質管控工具之必要驗證。
6. **評估即時列印監控系統**。目前系統為列印完成後的離線批量辨識模式。若設備串流與控制介面允許，未來可評估整合 Bambu Lab A1 內建攝影機或外接 USB 相機串流，在列印進行中進行即時品質監控；當模型偵測到疑似達 E 或 F 等級之嚴重拉絲時，先以警示與人工確認為主，再進一步研究是否適合連動暫停列印。此方向需另行驗證即時影像品質、延遲、誤報成本與設備控制安全性。
7. **優化品質評分模型的準確性**。目前品質分採用等級編號的線性轉換作為監督目標，較為粗糙。未來可邀請 5 至 10 名有經驗的操作人員對全部樣本進行主觀評分（連續值 0 至 100），以人工評分作為監督標籤，採用迴歸方式訓練更精確的評分頭，並計算模型輸出分數與人工評分的 ICC（組內相關係數）作為系統可信度的量化指標。
8. **模型輕量化與邊緣部署**。MobileNetV3-Large 約 5.4M 參數，若以 FP32 權重估算約為 21 MB，適合先於桌上型電腦或工業電腦進行離線測試。若未來需部署於計算資源有限的邊緣裝置（如 Raspberry Pi 或 NVIDIA Jetson 系列），可進一步評估知識蒸餾、模型剪枝或 INT8 量化等壓縮方法；但任何壓縮方案都必須在相同資料切分下重新測試混淆矩陣、各等級召回率、品質分校準與推論時間，不能僅依模型大小推論精度與速度。

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

\setcounter{figure}{0}
\setcounter{table}{0}

# Bambu Lab A1 列印參數彙整 {#sec:appendix-params}

本附錄依現有 Bambu Studio 截圖整理本研究可追溯之代表性列印參數設定（基於 PolyTerra PLA 0.08 mm 預設設定檔）。由於缺乏每一批次逐項匯出的完整設定檔，以下數值應解讀為代表性背景設定，而非逐批完全一致性的證明。表 \ref{tab:param-summary} 彙整影響列印品質之關鍵參數值，圖 \ref{fig:param-quality-representative} 為品質頁籤之代表畫面。

\begin{table}[H]
\centering
\caption{Bambu Lab A1 代表性列印參數彙整}
\label{tab:param-summary}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{cccc}
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
\end{table}

\begin{table}[H]
\centering
\caption{Bambu Lab A1 列印參數彙整（續）}
\label{tab:param-summary-cont}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{cccc}
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
                     & 加速度（普通 / 空駛） & 6000 / 10000 mm/s$^2$ & \\
\hline
\multirow{2}{*}{支撐} & 開啟支撐 & 否 & 魚骨件全數不啟用支撐 \\
                     & 類型 / 筏層 & 普通（手動）/ 0 層 & 閾值角度 15$^\circ$ \\
\hline
\multirow{2}{*}{其他} & Skirt / Brim & 0 圈 / 無 brim & 擦料塔啟用 \\
                     & 耗材 & PolyTerra PLA & 直徑 1.75 mm \\
\hline
\end{tabular}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth,height=0.7\textheight,keepaspectratio]{images/bambu-studio-quality-tab.png}
\caption{Bambu Studio 品質頁籤代表截圖（層高 0.08 mm、線寬 0.42 mm）}
\label{fig:param-quality-representative}
\end{figure}

\setcounter{figure}{0}
\setcounter{table}{0}

# PLA 耗材與冷卻設定彙整 {#sec:appendix-material}

本研究使用 Polymaker PolyTerra PLA 1.75 mm 線材；耗材物性、列印溫度與冷卻風扇策略依現有 Bambu Studio 截圖整理為代表性設定。表 \ref{tab:material-summary} 彙整關鍵設定值，圖 \ref{fig:cooling-representative} 為冷卻模式設定代表畫面。

\begin{table}[H]
\centering
\caption{PolyTerra PLA 代表性耗材與冷卻設定彙整}
\label{tab:material-summary}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
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
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth,height=0.7\textheight,keepaspectratio]{images/bambu-studio-cooling-mode.png}
\caption{冷卻模式設定代表截圖（風扇 60\%$\sim$80\%、最小列印速度 20 mm/s、懸垂強制冷卻）}
\label{fig:cooling-representative}
\end{figure}
