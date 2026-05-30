---
profile: report-nstc-undergrad  # PaperForge 編譯時自動套用此 profile（ctrl+shift+b 不必再帶 --profile）

# ============================================================
# === 國科會大專學生研究計畫成果報告基本資訊 ===
# ============================================================
project-title-zh: "3D列印單面列印件瑕疵檢測與品質評分設計"
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

熔融沉積成型（FDM）為桌上型 3D 列印之主流製程，拉絲（Stringing）為其常見表面瑕疵之一。傳統人工目視檢查標準因人而異，難以維持一致性，自動化瑕疵嚴重程度分級具有實用價值。

本研究以魚骨形狀 PLA 列印件為標的，建立 1110 張、六等級（A 至 F）拉絲嚴重程度影像分類資料集（185 個原圖群組，單一標注者）。採 MobileNetV3-Large 為主要骨幹進行遷移學習，以 ResNet18、EfficientNet-B0 為對照；以原圖層級 Group Split 確保訓練、驗證與測試集原圖零重疊，並以五組 seed 重複實驗量化結果穩定性。

五 seed 結果顯示四組模型 / 策略平均 accuracy 80.12\%--81.19\%、平均 QWK 約 0.91，各項統計檢定（Bonferroni 校正後）均未達顯著差異，故本研究不宣稱任一設定為穩定最佳。A/B 邊界（B 級召回率 56.3\%）為最主要效能瓶頸；品質分提供等級內排序參考，非絕對量化指標。

本研究受限於單一機型、材料、幾何、瑕疵類型與標注者，定位為此條件下可重現的輔助辨識原型；外部應用前需補多人標注一致性與跨機型驗證。

\vspace{0.5cm}

\noindent\textbf{關鍵詞：3D 列印、熔融沉積成型（FDM）、拉絲瑕疵檢測、MobileNetV3、深度學習、遷移學習、序數分類、分組切分（Group Split）、多 seed 評估、模型校準}

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

3D 列印技術（Three-Dimensional Printing），又稱積層製造（Additive Manufacturing, AM），係指透過電腦輔助設計（CAD）軟體建立三維數位模型後，依據切片軟體產生的路徑指令，將材料逐層堆積成形的製造技術[@ISOASTM52900]。自 1980 年代問世以來，已從工業快速原型擴展至航太、汽車與醫療等領域[@gibsonAdditiveManufacturingTechnologies2021]。

在眾多 3D 列印技術中，FDM 因設備成本低廉、支援多種熱塑性材料而廣受桌上型與教育場域採用，其製程原理與主要影響參數詳見第 \ref{sec:literature-fdm} 節；FDM 品質管控目前仍多依賴人工目視，缺乏系統化自動化機制[@gibsonAdditiveManufacturingTechnologies2021; @InventorFDM3D2017]。

以卷積神經網路（CNN）為代表的深度學習影像辨識技術，已用於工業視覺檢測[@WhatIndustry40; @WhatIndustrie40]。本研究聚焦於列印完成後的離線辨識（成品分級與品質追溯），與工業 4.0 強調的即時連網監控互補；即時監控之延伸見 \ref{sec:conclusion-future} 節。

## 研究動機 {#sec:intro-motivation}

在實際的 3D 列印生產場景中，品質管控主要面臨三項困難。其一是效率：人工目視在列印批量增加時逐件檢視耗時過長，成為產線瓶頸。其二是一致性：不同操作人員對同一成品的評估常有差異，在瑕疵程度接近等級邊界時尤其明顯，降低品質數據的可信度。其三是可追溯性：傳統目視結果不易形成可比較、可留存的數值化紀錄，不利於品質趨勢分析與製程改善。

深度學習可從樣本中自動學習視覺特徵，在固定標注準則下提供一致的瑕疵嚴重度預測。然而，3D 列印拉絲瑕疵的嚴重程度判定具有明顯的序數特性：少量短絲仍屬可接受範圍，大範圍絲狀殘留則需重新列印，等級邊界常受光線、角度與標注者主觀判斷影響。此外，在小批量研究場景中，取得大量具多人一致性標注的資料往往成本高昂，資料集的類別不平衡問題亦難以避免。本研究的核心動機，是在上述限制下建立嚴格且可重現的評估框架，檢驗深度學習模型能否作為品質管控的輔助工具。

## 研究目的與貢獻 {#sec:intro-purpose}

本研究的核心貢獻有以下四項：

1. **FDM 魚骨拉絲六等級資料集**：建立包含 1110 張魚骨影像、依目視估計拉絲覆蓋比例定義之六等級（A 至 F）資料集，供後續 FDM 拉絲瑕疵小樣本影像分類研究比較（單一標注者之限制詳見 \ref{sec:method-grading} 節）。
2. **嚴格分組切分與多 seed 泛化評估**：以原圖為單位進行 Group Split（原圖零重疊），避免同源樣本造成過度樂觀的評估；並以五組 seed 重複實驗、報告 seed 間 std，提供比單次切分更保守的小樣本工業視覺基準。
3. **模型策略比較、診斷性消融與不確定性分析**：比較 MobileNetV3-Large、ResNet18、EfficientNet-B0 三種骨幹與簡化／完整兩組訓練策略，並以 seed=7 對 Focal Loss、Label Smoothing、Mixup、Weighted Random Sampler 做單變因消融，評估各因素對少數類別分類的影響趨勢；並進行模型校準分析，確認低置信度樣本可納入人工複核流程。
4. **整批照片自動處理流程**：整合自動裁切、逐張前向推論、分級輸出與 HTML 可視化報告，形成由原始照片到品質等級報告之離線處理流程；並於 RTX 3050 Laptop GPU 上量測純模型前向延遲作為部署參考基準（量測條件與端到端吞吐量限制詳見 \ref{sec:results-batch} 節）。

附帶產出包含具明確判斷規則的六等級評分準則、各等級範例圖、Label Studio 標注流程，以及雙輸出（六分類 + 0 至 100 連續品質分）模型架構（品質分之使用限制見 \ref{sec:method-model-dualhead} 節）。

## 研究範圍 {#sec:intro-scope}

本研究以 FDM 列印之魚骨形狀 PLA 件為研究對象（選用原因詳見第 \ref{sec:method-sample-design} 節）。研究題目中「單面」係指以**單一俯拍角度、單一 2D 影像**作為模型輸入，不涉及多視角影像、3D 掃描或點雲重建；完整 3D 幾何資訊的檢測屬互補方向，不在本研究範圍內。本研究聚焦於拉絲瑕疵的嚴重程度分類，不包含翹曲及裂痕瑕疵（現有樣本中此兩類數量不足）。

實驗設備限定為 Bambu Lab A1、耗材為標準 PLA 線材、拍攝環境為固定背景的室內自然光，模型泛化能力主要針對此特定設備與材料條件。資料集共 1110 筆有效魚骨樣本，分屬六個品質等級，各等級樣本數差異明顯（最多與最少約相差 17 倍，詳見 \ref{sec:results-dataset} 節）。完整邊界條件詳見第 \ref{sec:conclusion} 章結論。

## 研究流程 {#sec:intro-flow}

本研究的整體執行流程分為三大階段：第一階段為資料蒐集與前處理，包含 3D 列印樣本製作、影像拍攝、魚骨自動裁切及人工標注；第二階段為模型訓練與評估，包含資料集整理、模型訓練、效能評估、多 seed 重複與消融分析；第三階段為系統整合與應用，包含整批照片自動處理流程開發、可視化報告產生及實際應用驗證。各階段之時序順序如圖 \ref{fig:overall-flow} 所示；資料流與責任分工另見第 \ref{sec:method-architecture} 節。

\begin{figure}[H]
\centering
% TODO@學長：原 research-overall-flow.png 流程圖整體偏小，圖內方塊文字在 PDF 列印後字級過小、難以辨識，已暫時移除改為占位框。
% 重新生圖需求：
%   (1) 請放大整張圖或加大圖內字級，確保印出後每個流程方塊與箭頭標註（如「全數成品拍攝」「魚骨自動裁切」「7 ms/張」等）都清晰可讀；
%   (2) 圖的三階段內容請對照本節正文（資料蒐集與前處理 → 模型訓練與評估 → 系統整合與應用）；
%   (3) 命名為 images/research-overall-flow.png 覆蓋後，刪掉下方 \fbox 占位框、取消 \includegraphics 該行註解即可。
%\includegraphics[width=0.9\textwidth,height=0.72\textheight,keepaspectratio]{images/research-overall-flow.png}
\fbox{\parbox[c][4cm][c]{0.9\textwidth}{\centering\footnotesize 研究整體流程圖待重新繪製\\（TODO@學長，圖內文字過小須放大重生，詳見原始碼註解）}}
\caption{研究整體流程圖}
\label{fig:overall-flow}
\end{figure}

# 文獻回顧 {#sec:literature}

## FDM 3D 列印技術概述 {#sec:literature-fdm}

熔融沉積成型（Fused Deposition Modeling, FDM）由 Scott Crump 於 1989 年發明，並於 1992 年由 Stratasys 公司商業化推出[@InventorFDM3D2017]。其工作流程為：以 CAD 軟體建模並輸出 STL 或 3MF 格式，經切片軟體（如 Bambu Studio、PrusaSlicer）轉為逐層的噴嘴路徑指令（G-code），印表機再依指令逐層擠出熔融材料堆積成形，最後視需要拆除支撐並做表面處理。

影響 FDM 列印品質的關鍵參數可分為溫度類、速度類及結構類三大類。溫度類包括噴嘴溫度（Nozzle Temperature）、熱床溫度（Bed Temperature）及環境溫度；速度類包括列印速度（Print Speed）、移位速度（Travel Speed）、回抽速度（Retraction Speed）；結構類包括層高（Layer Height）、填充密度（Infill Density）、填充圖案（Infill Pattern）、支撐結構類型及冷卻設定。這些參數之間存在複雜的交互作用，例如提高列印速度通常需要相應提高噴嘴溫度以確保材料充分熔融，但過高的溫度又會增加拉絲風險。

## 3D 列印常見瑕疵類型 {#sec:literature-defects}

根據現有 FDM 文獻與設備廠商 troubleshooting 文件，FDM 列印常見的表面瑕疵主要包含以下三類，如圖 \ref{fig:defects-overview} 所示。本文實驗僅將拉絲瑕疵納入模型訓練與測試，翹曲與裂痕因樣本不足僅作背景說明。

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.32\textwidth}
  \includegraphics[width=\textwidth]{images/defect-stringing.png}
  \subcaption{拉絲（Stringing）}
  \label{fig:defect-stringing}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.32\textwidth}
  \includegraphics[width=\textwidth]{images/defect-warping.png}
  \subcaption{翹曲（Warping）}
  \label{fig:defect-warping}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.32\textwidth}
  % TODO@學長：原 defect-cracking.png 解析度過低，且照片內嵌的紅色標註文字過小、無法辨識，已暫時移除。
  % 補圖需求：
  %   (1) 清晰度需與 (a) 拉絲、(b) 翹曲兩張子圖一致（同一拍攝距離、對焦清楚、無壓縮模糊）；
  %   (2) 請勿在照片內嵌紅色標註文字；若要指出裂痕位置，改用箭頭或於 \caption 文字說明；
  %   (3) 命名為 images/defect-cracking.png 覆蓋後，刪掉下方 \fbox 占位框、取消 \includegraphics 該行註解即可。
  %\includegraphics[width=\textwidth]{images/defect-cracking.png}
  \fbox{\parbox[c][3cm][c]{0.9\textwidth}{\centering\footnotesize 裂痕照片待補\\（TODO@學長，詳見原始碼註解）}}
  \subcaption{裂痕（Cracking）}
  \label{fig:defect-cracking}
\end{subfigure}
\caption{FDM 列印三種常見表面瑕疵（由左至右：拉絲、翹曲、裂痕）}
\label{fig:defects-overview}
\end{figure}

**拉絲（Stringing）**：係指噴嘴在非列印區域移動時，熔融材料因回抽不足、噴嘴溫度過高或材料流動性過大而持續滲出，進而在列印件表面形成細絲狀殘留的現象。其嚴重程度通常與回抽距離與速度、噴嘴溫度、移位速度及冷卻效率等參數交互影響有關[@StringingOozing; @BambuStudioAdvanced]。

**翹曲（Warping）**：列印件冷卻時因材料收縮與平台附著力不足，底層邊角上翹或脫離平台，通常與熱床溫度、第一層附著、環境溫度與材料熱收縮特性有關[@WarpingPrusaKnowledge2025]。

**裂痕（Cracking）或層間分離（Layer Separation）**：層與層之間因冷卻速率差異、黏結不足或翹曲應力過大而分離出裂縫，會降低列印件的結構完整性與機械強度[@LayerSeparationSplitting2024]。

從影像辨識的角度而言，拉絲在影像中呈現細線狀、高頻率的局部紋理，通常以明亮細絲出現在較暗背景（如黑色熱床）或魚骨間隙中，形成與正常平滑表面明顯不同的對比特徵。相較於顏色直方圖等全域描述子，CNN 的局部感受野更能捕捉拉絲的高頻細線紋理，其密度與分布面積正適合用以區分嚴重程度。此推論在第四章 Grad-CAM 分析中獲得部分佐證（詳見 \ref{sec:results-supplemental-calibration} 節）。

## 電腦視覺與深度學習於工業瑕疵檢測 {#sec:literature-cv-dl}

電腦視覺技術應用於工業品質檢測已有數十年歷史。早期方法以傳統影像處理為主（邊緣偵測、閾值分割、形態學運算、特徵工程等），需領域專家手動設計特徵；此類方法在受控環境下表現尚可，但對光線、姿態與背景干擾的魯棒性較差，也難以應對複雜的多類別瑕疵辨識。

深度學習則改變了電腦視覺的特徵設計方式[@DeepLearning; @lecunGradientbasedLearningApplied1998]。卷積神經網路（CNN）以端到端方式自動學習影像的層次化特徵，從底層邊緣、紋理到高層語義，無需人工設計特徵，在充足資料下辨識精度通常優於傳統人工特徵方法[@dengImageNetLargescaleHierarchical2009; @heDeepResidualLearning2016]，並已應用於半導體晶圓、鋼板、紡織品與 PCB 等工業瑕疵檢測[@bhattImageBasedSurfaceDefect2021]。在 3D 列印領域，已有研究將影像技術用於列印過程的即時瑕疵偵測[@holzmondSituRealTime2017]，以及以多頭神經網路進行即時錯誤偵測與跨機型校正[@brionGeneralisable3DPrinting2022]，多聚焦列印中（in-process）的逐層或即時監控。

工業瑕疵檢測文獻中另有一類基於**異常偵測（Anomaly Detection）**的無監督或半監督方法，如以自動編碼器（Autoencoder）的重建誤差判斷是否異常，或以正常樣本建立特徵分布、測試時以馬氏距離偵測偏離[@bhattImageBasedSurfaceDefect2021]。此類方法的優勢在於訓練時僅需正常樣本，不必對每種瑕疵類型逐一標注；但其輸出為「正常/異常」的二元判斷，無法直接輸出瑕疵嚴重程度等級。本研究的核心目標是對拉絲嚴重程度進行 A 至 F 六等級的**序數分級**，需要每張樣本帶有等級標籤才能訓練分類或迴歸模型，因此選擇有監督分類路線，而非無監督異常偵測。

語意分割（Semantic Segmentation）方法雖可逐像素標注拉絲細絲分布，理論上能直接量測覆蓋面積，但本研究未採用此路線，主要原因有三：（1）拉絲細絲邊界模糊、寬度僅數像素，逐像素標注成本高且一致性難以保證；（2）現階段研究目標為建立可行的分類基準，影像級標籤已足夠；（3）1110 張資料規模下，訓練語意分割模型的樣本密度可能不足。未來可在累積更多資料後導入分割模型，以像素級覆蓋面積取代目視估計，提升品質分數的物理可解釋性。

## 相關文獻探討 {#sec:literature-related}

Jogin 等人[@joginFeatureExtractionUsing2018]的 CIFAR-10 實驗（85.97\% 準確率，顯著優於 SVM 與隨機森林）說明 CNN 學得的深度特徵在多類別影像分類上的系統性優勢，為本研究採用 CNN 骨幹提供方法論背景。

Varshni 等人[@varshniPneumoniaDetectionUsing2019]以 DenseNet-169、ResNet-50、VGG-16、Xception 等預訓練模型對 ChestX-ray14 肺炎 X 光影像做特徵提取並接 SVM 分類，其中 DenseNet-169+SVM 之 AUC 達 0.8002。其價值在方法論層面：同樣在標注樣本有限（約千張量級）的條件下，以 ImageNet 預訓練模型遷移特徵即取得有效結果，支持本研究採用 MobileNetV3-Large 的遷移學習策略。

Lin 等人[@linFocalLossDense2017]提出之 Focal Loss 原用於目標偵測中前景與背景的極端不平衡（比例可達 1000:1 以上），以調焦因子 $(1-p_t)^\gamma$ 降低高信心樣本的損失權重，使訓練聚焦於困難樣本。本研究六等級最大不平衡約 17:1（A 級 546 張對 F 級 32 張）屬相對溫和，故將 Focal Loss 作為多重不平衡處理手段之一（配合 Weighted Sampler、Label Smoothing），而非主要解法（組合詳見 \ref{sec:method-model} 節）。

與本研究最直接相關者為 Brion 與 Pattinson[@brionGeneralisable3DPrinting2022]，其以多頭神經網路對 FDM 列印過程進行**即時**錯誤偵測與參數校正，並在多種印表機、材料與幾何形狀上展現泛化能力，屬「列印中（in-process）」的閉迴路監控。相較之下，本研究著眼於「列印後（post-print）」的成品表面品質評級：將拉絲瑕疵依嚴重度劃分為 A 至 F 六個**序數**等級並輸出連續品質分，且採用保留未來邊緣部署彈性的輕量模型，於小規模且不平衡的資料上以嚴格切分重複評估。兩者在偵測時機、輸出粒度與應用情境上互補（本研究對此缺口的定位見 \ref{sec:literature-gap} 節）。

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

MobileNetV3-Large 與 EfficientNet-B0 參數量相近，但 MobileNetV3-Large 計算量較低（219 MFLOPs 對 390 MFLOPs），其 SE 注意力機制對各通道重要性加權，理論上有利於凸顯細絲密度差異等局部紋理。本研究採用 torchvision 提供之 ImageNet V2 預訓練權重作為初始化，可利用大規模自然影像資料上學得的通用低階與中階視覺特徵，減少對本研究標注資料量的依賴。

## 遷移學習與資料不平衡處理 {#sec:literature-transfer}

遷移學習（Transfer Learning）在電腦視覺領域的核心假設是：在大規模資料集（如 ImageNet）上預訓練的模型，已學習到豐富的底層視覺特徵（邊緣、紋理、形狀等），這些特徵可以遷移至目標任務，即使目標任務的資料量遠少於預訓練資料集。常用的遷移學習策略包括：（a）**特徵提取（Feature Extraction）**：凍結預訓練模型的全部或大部分層，僅訓練新增的任務特定層；（b）**微調（Fine-tuning）**：以較小的學習率對全部或部分層進行更新，使模型特徵更好地適應目標任務。本研究兩組設定（簡化與完整）均採用全層微調（Full Fine-tuning）策略；兩者的差異主要在於損失函數、資料增強（有無 Mixup）與過採樣設定的組合，詳見 \ref{sec:method-model} 節。

資料不平衡（Class Imbalance）是小樣本瑕疵分類常見的難題，文獻上的處理手段大致可分為三類：（1）**資料採樣層面**的重採樣，如對少數類別過採樣（oversampling）或加權抽樣，平衡各類別在訓練過程中的曝光機會；（2）**損失函數層面**的成本敏感法，包括前述 Focal Loss[@linFocalLossDense2017]（對困難樣本加重懲罰）與 **Label Smoothing**（將分類目標由硬標籤替換為軟標籤，分配小量機率 $\epsilon$ 給非目標類），後者有助於避免模型對多數類別樣本產生過度自信，並在少數類別邊界保留更多梯度訊號；（3）**資料增強層面**的方法，如 Mixup[@zhangMixupEmpiricalRisk2018]在批次中對任意兩筆樣本進行線性混合，擴充訓練分布的多樣性並抑制模型對邊界樣本的過度自信。三類手段彼此正交、可組合使用。本研究完整設定採用 Focal Loss + Label Smoothing（$\epsilon=0.1$）+ Mixup（$\alpha=0.3$）+ Weighted Sampler 之組合，簡化設定僅保留標準 Cross Entropy；此組合的實作取捨詳見 \ref{sec:method-model} 節。

此外，本研究的 A 至 F 等級並非彼此獨立的名目類別，而具有由良品到嚴重瑕疵的序數關係。序數分類文獻提出以排序一致性約束處理等級輸出，例如 CORAL 與 CORN 將類別順序納入學習目標[@caoRankConsistentOrdinal2020; @shiDeepNeuralNetworks2023]；模型信心校準則可檢查 softmax confidence 是否反映預測可靠度，temperature scaling 為常見後處理方法[@guoCalibrationModernNeural2017]。本文仍以名目分類（nominal classification）為主要訓練方式，故在結果章額外回報 Quadratic Weighted Kappa（QWK）、跨等級誤判率（預測與真實等級差距 $\geq 2$ 的樣本佔比）與校準分析，避免只用 accuracy 解讀序數分級任務。

## 研究缺口與本研究定位 {#sec:literature-gap}

綜合前述文獻，可歸納出三點缺口。第一，CNN 與遷移學習在工業表面瑕疵檢測（半導體晶圓、鋼板、紡織品、PCB 等）已有成熟應用[@bhattImageBasedSurfaceDefect2021]，但多屬「有無瑕疵」或「瑕疵種類」的名目分類，少有針對單一瑕疵的「嚴重程度分級」之序數評估。第二，FDM 領域的代表性研究（如 Brion 與 Pattinson[@brionGeneralisable3DPrinting2022]）聚焦列印過程中的即時錯誤偵測與校正，而非列印完成後對成品表面品質給出可追溯的細緻分級。第三，遷移學習雖已證實能緩解小樣本問題[@varshniPneumoniaDetectionUsing2019]，但各研究的資料規模、不平衡程度與切分方式差異甚大，少有在「小樣本、類別不平衡」條件下同時報告嚴格切分、多 seed 重複與校準分析的可重現評估。

據此，本研究的定位是補足「列印後、單一瑕疵（拉絲）、序數品質分級、輕量模型、嚴格可重現評估」這一交集情境：以 ImageNet 預訓練之 MobileNetV3-Large 為骨幹進行遷移學習，輸出 A 至 F 六等級分類並附加連續品質分；針對類別不平衡採用重採樣、成本敏感損失與資料增強的組合（見 \ref{sec:method-model} 節）；並以 Group Split 嚴格切分、多 seed 重複與校準分析建立可重現的效能基準（見 \ref{sec:results} 章）。

# 研究方法 {#sec:method}

## 研究架構 {#sec:method-architecture}

本研究系統架構如圖 \ref{fig:method-flow} 所示。整體流程由列印製樣與影像蒐集開始，經裁切前處理與人工標注建立 A 至 F 六等級資料集，再以 MobileNetV3-Large 進行遷移學習訓練，最後輸出混淆矩陣、品質分數、分級資料夾與 HTML 統計報告。硬體與軟體環境詳見 \ref{sec:method-equipment} 節。

\begin{figure}[H]
\centering
% TODO@學長：原 method-system-flow.png 流程圖整體偏小，圖內方塊文字與底部「※雙輸出頭…」註解在 PDF 列印後字級過小、閱讀吃力，已暫時移除改為占位框。
% 重新生圖需求：
%   (1) 請放大整張圖或加大圖內字級，特別是底部的小字註解，確保印出後每個方塊與資料流箭頭都清晰可讀；
%   (2) 圖的內容請對照本節正文（列印製樣與影像蒐集 → 裁切前處理與人工標注 → MobileNetV3-Large 遷移學習 → 輸出混淆矩陣/品質分數/分級資料夾/HTML 報告）；
%   (3) 命名為 images/method-system-flow.png 覆蓋後，刪掉下方 \fbox 占位框、取消 \includegraphics 該行註解即可。
%\includegraphics[width=\textwidth,height=0.75\textheight,keepaspectratio]{images/method-system-flow.png}
\fbox{\parbox[c][4cm][c]{0.9\textwidth}{\centering\footnotesize 研究流程與資料流關係圖待重新繪製\\（TODO@學長，圖內文字過小須放大重生，詳見原始碼註解）}}
\caption{研究流程與資料流關係圖}
\label{fig:method-flow}
\end{figure}

## 實驗設備 {#sec:method-equipment}

### 3D 列印設備規格 {#sec:method-equipment-printer}

本研究使用 Bambu Lab A1 桌上型 3D 印表機作為列印設備，該機型採用床式平台移動（Bed Slinger）機械結構。主要技術規格整理如表 \ref{tab:printer-spec} 所示。

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

### 列印參數設定 {#sec:method-equipment-params}

列印參數非本研究的操控變因，全程固定採用 Bambu Studio 預設值；惟未逐批匯出完整設定檔，無法保證各批次完全一致。預設值在以下四個面向維持固定，使樣本間的拉絲差異主要來自列印狀態而非參數變動：

1. **品質設定**：固定層高、線寬與外殼品質，使拉絲差異主要來自列印狀態而非幾何尺寸變動。
2. **強度設定**：固定填充密度與壁厚，避免樣本因結構強度不足而產生非拉絲類破壞。
3. **速度設定**：維持列印與移動速度一致，降低批次間因噴嘴移動條件不同造成的額外變異。
4. **支撐設定**：在魚骨件列印中保持固定，避免支撐拆除痕跡被誤判為瑕疵特徵。

耗材使用直徑 1.75 mm 之 Polymaker PolyTerra PLA 線材，噴嘴溫度 220 $^\circ$C、熱床溫度 65 $^\circ$C（紋理 PEI）。完整 Bambu Studio 參數與耗材冷卻設定分別彙整於附錄二表 \ref{tab:param-summary} 與附錄三。

### 電腦硬體與軟體環境 {#sec:method-equipment-pc}

模型訓練所使用的電腦硬體與軟體規格如表 \ref{tab:pc-spec} 所示。本研究利用 NVIDIA RTX 3050 Laptop GPU 進行深度學習模型訓練，搭配 PyTorch 2.6.0+CUDA 12.4 環境，並開啟 FP16 混合精度訓練[@falconPyTorchLightning2019]。

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

## 列印樣本製作與影像蒐集 {#sec:method-sample}

### 樣本設計與列印過程 {#sec:method-sample-design}

本研究以魚骨形狀列印件作為樣本，是因其具有細長肋條、尖端與多個間隙，對 FDM 拉絲瑕疵特別敏感。當噴嘴溫度、回抽設定、移動速度或冷卻條件不穩定時，細絲通常會出現在魚骨間隙與尖端區域，因此此幾何形狀適合作為拉絲嚴重程度分類的測試對象。魚骨件幾何規格如表 \ref{tab:fishbone-spec} 所示，列印方向為底面貼熱床平放。

\begin{table}[H]
\centering
\caption{魚骨樣本幾何規格（由 STL 模型解析，Rhino 建模匯出）}
\label{tab:fishbone-spec}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
\hline
\textbf{項目} & \textbf{數值} & \textbf{備注} \\
\hline
總長度（含吊頭） & 86.41 mm & X 軸方向 Bounding Box \\
最大寬度（含雙側肋條） & 30.09 mm & Y 軸方向，最寬肋條處 \\
高度 & 9.00 mm & Z 軸方向 \\
肋條數量 & 7 根 & 對稱雙側 \\
相鄰肋條中心間距 & 7--9 mm（平均 7.8 mm） & 由尾至頭漸寬後漸窄 \\
列印方向 & 底面貼熱床（平放） & 不使用支撐 \\
\hline
\end{tabular}
\end{table}

資料蒐集採分批列印方式進行：以 Bambu Lab A1 分批列印魚骨件後集中拍攝（各批張數見表 \ref{tab:batch-stats}）。標準批次以 2 欄 × 3 列拍攝，**每支列印件均納入資料集**、不遺漏，每張原始照片裁切出 6 筆有效樣本（拍攝與裁切規範詳見 \ref{sec:method-sample-capture} 節）。同一列印批次的魚骨件共享相同列印條件（溫度、速度、材料批號），批次內樣本之間具高階相關性（其對切分的影響詳見 \ref{sec:method-model} 節 Group Split 說明）。

此外，另行補充少數等級樣本，使各等級資料更為完整；此批補樣以單支或少量方式個別拍攝，每張原圖裁切數不一定為標準批次的 6 筆，其中 E 級來自 61 組獨立拍攝原圖（共 72 張裁切），F 級來自 28 組獨立拍攝原圖（共 32 張裁切），且 F 級樣本皆與其他等級同板拍攝（非單獨成板）。最後整理為 1110 筆有效資料，完整列印過程照片改列於附錄一。

### 影像拍攝規範 {#sec:method-sample-capture}

影像拍攝採固定角度與固定背景：從累積的列印成品中每次取 6 支，平鋪於**黑色背景板**上排列成 2 欄 $\times$ 3 列，以 Redmi Note 14 5G 智慧型手機（搭載 MediaTek Camera Application）俯拍一張原始照片，重複此流程直至全部成品完成拍攝。相機採全自動曝光，AE、AWB、ISO 與快門均未鎖定，室內光源與拍攝距離亦未紀錄，僅盡量維持拍攝位置與環境一致。黑色背景板與各色 PLA 魚骨形成良好明暗對比，有助於後續裁切與辨識。上述未鎖定使各批次亮度與色調略有差異，部分由 ColorJitter 吸收（見 \ref{sec:method-preprocessing-aug} 節），但不能取代拍攝端的嚴格控制。各批次拍攝資料統計如表 \ref{tab:batch-stats} 所示。

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

本研究依列印與拍攝完成後整理之實驗照片進行魚骨樣本自動裁切。裁切採用固定網格方式：將每張照片等分為 2 欄 × 3 列，各格切出一支魚骨，並在後續訓練前統一縮放為 224 × 224 pixels 以符合預訓練模型輸入。由於拍攝時維持相近角度與位置，固定網格裁切的錯位風險偏低；惟未逐張人工 QC，個別批次仍可能因拍攝偏移出現邊界不齊。

圖 \ref{fig:crop-fish01} 至圖 \ref{fig:crop-fish03} 為自動裁切輸出的範例，每支魚骨被完整切割、背景一致。

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.31\textwidth}
  \includegraphics[width=\textwidth]{images/crop-fish-example-01.jpg}
  \subcaption{fish01}
  \label{fig:crop-fish01}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.31\textwidth}
  \includegraphics[width=\textwidth]{images/crop-fish-example-02.jpg}
  \subcaption{fish02}
  \label{fig:crop-fish02}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.31\textwidth}
  \includegraphics[width=\textwidth]{images/crop-fish-example-03.jpg}
  \subcaption{fish03}
  \label{fig:crop-fish03}
\end{subfigure}
\caption{自動裁切輸出之魚骨裁切結果範例（每支魚骨完整切割、背景一致）}
\label{fig:crop-fish-examples}
\end{figure}

### 資料增強策略 {#sec:method-preprocessing-aug}

訓練階段對輸入影像施加表 \ref{tab:augmentation} 所列的多種隨機增強，以擴充樣本多樣性、提升泛化能力；驗證與測試階段僅保留 Resize 與 Normalize 等確定性前處理，不施加隨機增強，確保評估流程一致。表中除 Mixup 屬批次層級增強（在 DataLoader 回傳 mini-batch 後才執行）外，其餘皆為樣本層級增強，依表列順序在 PIL 影像或 Tensor 空間執行。

垂直翻轉以低機率（$p=0.3$）使用，因拍攝時偶有上下顛倒放置；低機率翻轉可增加方向多樣性而不過度偏離魚骨原始方向。

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

本研究雖以 ColorJitter 與 RandomGrayscale 增加色彩變化、降低對材料顏色的依賴，仍無法完全排除模型利用材料顏色或拍攝批次作為捷徑特徵（Shortcut Feature）：若某批次的 PLA 顏色恰好對應特定等級，模型可能學到「顏色→等級」而非「拉絲紋理→等級」。此風險在缺乏跨批次驗證集時無法量化（參見 \ref{sec:method-model} 節 Group Split 之批次相關性限制）。

## 品質等級定義 {#sec:method-grading}

本研究依目視估計之拉絲覆蓋比例與魚骨結構可辨識程度，制定六個品質等級（A 至 F），如表 \ref{tab:grading-criteria} 所示。等級定義以覆蓋比例區間作為標注準則，而非透過影像分割演算法量測實際面積；並配合各等級範例圖（圖 \ref{fig:grade-a} 至圖 \ref{fig:grade-f}），以提升單一標注者在整批資料中的前後一致性。

本研究現階段僅單一標注者，無法計算標注者間一致性（如 Cohen's、Fleiss' Kappa）或人類基準；故所有準確率均應理解為相對此固定標注準則，而非多人共識標準。模型能重現此套準則以降低批量檢查負擔、輔助人工複核，但尚未消除人工主觀差異。

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
B & 良好品 & \makecell{極少量細絲，$1 \sim 2$ 根短絲\\面積可忽略} & 80 分 & 一般用途可接受 \\
C & 輕微拉絲 & \makecell{少量細絲\\目視覆蓋 $<$ 魚身 1/4} & 60 分 & \makecell{外觀要求低時\\可接受} \\
D & 中度拉絲 & \makecell{明顯細絲\\目視覆蓋約魚身 $1/4 \sim 1/2$} & 40 分 & \makecell{需重新列印\\或後處理} \\
E & 嚴重拉絲 & \makecell{大量細絲\\目視覆蓋 $>$ 魚身 1/2} & 20 分 & 品質不合格 \\
F & 失敗品 & \makecell{極度拉絲\\幾乎看不出魚骨結構} & 0 分 & 廢品 \\
\hline
\end{tabular}
\end{table}

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.30\textwidth}
  \includegraphics[width=\textwidth]{images/grade-a-sample.jpg}
  \subcaption{A 完美品}
  \label{fig:grade-a}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.30\textwidth}
  \includegraphics[width=\textwidth]{images/grade-b-sample.jpg}
  \subcaption{B 良好品}
  \label{fig:grade-b}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.30\textwidth}
  \includegraphics[width=\textwidth]{images/grade-c-sample.jpg}
  \subcaption{C 輕微拉絲}
  \label{fig:grade-c}
\end{subfigure}

\vspace{0.5em}

\begin{subfigure}[b]{0.30\textwidth}
  \includegraphics[width=\textwidth]{images/grade-d-sample.jpg}
  \subcaption{D 中度拉絲}
  \label{fig:grade-d}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.30\textwidth}
  \includegraphics[width=\textwidth]{images/grade-e-sample.jpg}
  \subcaption{E 嚴重拉絲}
  \label{fig:grade-e}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.30\textwidth}
  % TODO@學長：原 grade-f-sample.jpg 右上角殘留標註工具的紅色「F 90%」UI 標籤，與其他五張乾淨樣本不一致，已暫時移除。
  % 補圖需求：
  %   (1) 重新裁切一張乾淨的 F 級（失敗品）魚骨樣本，畫面內不可有任何標註框、文字或浮水印；
  %   (2) 拍攝/裁切條件與 A～E 五張一致（黑底俯拍、單支魚骨置中）；
  %   (3) 命名為 images/grade-f-sample.jpg 覆蓋後，刪掉下方 \fbox 占位框、取消 \includegraphics 該行註解即可。
  %\includegraphics[width=\textwidth]{images/grade-f-sample.jpg}
  \fbox{\parbox[c][3cm][c]{0.9\textwidth}{\centering\footnotesize F 級樣本待補\\（TODO@學長，詳見原始碼註解）}}
  \subcaption{F 失敗品}
  \label{fig:grade-f}
\end{subfigure}
\caption{A 至 F 六等級代表性樣本（上列：A/B/C；下列：D/E/F）}
\label{fig:grade-samples}
\end{figure}

## 資料標注流程 {#sec:method-labeling}

本研究使用 Label Studio（開源標注平台）[@OpenSourceData]完成全部裁切圖的人工標注，採用**圖片級分類標籤**（image-level classification label）作為訓練監督信號，而非物件偵測的邊界框標籤。標注流程為：

1. 將裁切圖匯入 Label Studio 專案。
2. A 等級直接標記為合格，無需畫框。
3. 有拉絲的樣本，先以邊界框（bounding box）於拉絲區域做視覺輔助圈選（供標注者確認覆蓋範圍），再選擇對應的圖片級嚴重程度標籤（A 至 F）。
4. 完成後匯出標注結果（JSON 格式）。
5. 解析匯出結果，僅擷取每張裁切圖的圖片級等級標籤，忽略邊界框座標，將各樣本依標籤歸入 A 至 F 對應等級的子目錄，建立可供 ImageFolder 讀取的資料集。

標注完成後，A 級 546 張、B 級 87 張、C 級 213 張、D 級 160 張、E 級 72 張、F 級 32 張，共 1110 張有效資料。

## 模型架構與訓練設計 {#sec:method-model}

### 模型架構 {#sec:method-model-arch}

#### 骨幹網路選擇之考量 {#sec:method-model-rationale}

本研究選用 MobileNetV3-Large 作為主要骨幹，並以 ResNet18、EfficientNet-B0 為對照基準，主要考量如下：

1. **參數量與小樣本過擬合風險**：1110 張資料規模偏小，過大模型容易過擬合。三個候選模型之參數量與計算量詳見第二章表 \ref{tab:model-complexity}，皆屬輕量級。相較之下 ResNet50（25.6M）或 ViT-Base（86M）參數量過大，在此資料規模下需更強之資料增強與正則化策略才能避免過擬合。
2. **推論效率與未來部署彈性**：MobileNetV3 系列原為行動端與邊緣裝置設計，其 219 MFLOPs 計算量明顯低於 ResNet18（約 1.8 GFLOPs）；本研究於配備 RTX 3050 Laptop GPU 之筆記型電腦上訓練與推論，未來若需離線現場部署，可再評估工業電腦、Raspberry Pi 或 Jetson 系列等邊緣裝置。實測單張推論時間 6.90 ms 亦支持批量處理需求。
3. **ImageNet 預訓練權重可用性**：MobileNetV3-Large 可直接載入 torchvision 提供之 ImageNet 預訓練權重，遷移學習成本低。
4. **與相近研究之可比較性**：ResNet18 為小資料瑕疵檢測之常用基準，EfficientNet-B0 為近年主流輕量模型代表，三者並列可涵蓋移動端最佳化、殘差網路與複合縮放三種代表性設計，便於後續研究比較。方法路線（有監督分類 vs. 異常偵測）之選擇依據詳見第二章 \ref{sec:literature-cv-dl} 節。

本研究兩組設定（簡化與完整）均採用**全層微調（Full Fine-tuning）**策略，即骨幹所有層均參與梯度更新，而非僅訓練新增的分類頭。在 1110 張資料規模下，全層微調的過擬合風險主要透過 Dropout、資料增強與正則化損失控制；特徵提取（Feature Extraction，凍結骨幹）策略未在本研究探索。

選擇之 trade-off 在於：未涵蓋 Vision Transformer 系列（如 ViT-Tiny、DeiT-Tiny）、ConvNeXt 系列等新架構，亦未探討 self-supervised pre-training（如 DINO、MAE）對小樣本任務之助益，此屬本研究範圍限制。

#### 雙輸出架構 {#sec:method-model-dualhead}

本研究採用 MobileNetV3-Large[@howardSearchingMobileNetV32019]（ImageNet V2 預訓練）作為骨幹網路，以遷移學習方式進行六分類微調。模型的特徵提取路徑為：backbone features 模組 → AdaptiveAvgPool → Flatten → classifier[:3]（Linear(960→1280) + Hardswish + Dropout(0.2)），輸出 1280 維特徵向量。在此 1280 維特徵向量之上接兩個並行輸出頭：

**分類頭**：Dropout（$p = 0.4$）→ Linear(1280→6)，輸出六類 logits。

**品質評分輔助頭**：Dropout（$p = 0.2$）→ Linear(1280→64) → ReLU → Linear(64→1) → Sigmoid，輸出範圍 0 至 1 的連續品質分，乘以 100 即得 0 至 100 分。

訓練時分類頭與評分頭同步優化。品質分輔助頭以「等級編號的線性轉換」（A=1.0, B=0.8, \ldots, F=0.0）作為迴歸目標（$\text{score\_gt} = 1 - \text{label} / 5$），**隱含假設等級間距相等、ordinal 關係由 MSE loss 隱式建模**。

此等距假設在感知品質層面未必成立：A→B（幾乎無拉絲至 1～2 根短絲）的差異，未必等同於 E→F（大量拉絲至結構幾乎難以辨識）的差異，主觀品質曲線在嚴重端（D/E/F）可能較陡、在輕微端（A/B/C）較平緩；惟缺乏多人連續評分校準資料，此偏差暫無法量化。

此外，Mixup 啟用時評分目標 $\text{score\_gt}$ 僅以混合前第一個樣本的標籤（$y_a$）計算，未對第二個樣本標籤（$y_b$）做線性插值，在跨等級混合樣本上會引入輕微的監督不一致。整體而言，本研究以「名目分類＋輔助迴歸」近似序數分類（ordinal classification），未採用序數感知損失（如 CORAL [@caoRankConsistentOrdinal2020]、CORN [@shiDeepNeuralNetworks2023]）。

本研究依不同的資料切分與策略組合進行多組訓練（如表 \ref{tab:training-scripts} 所示）。本文的「多 seed」指在同一份 1110 張資料、相同 Group Split 流程與相同模型／設定下，更換亂數種子值後重複訓練與測試；資料逐步擴充產生的歷史版本不列入多 seed 統計。五個種子值為 7、42、123、1234、2024。

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

\noindent 如表 \ref{tab:training-scripts}，四組正式比較（MobileNetV3-Large 簡化／完整、ResNet18 完整、EfficientNet-B0 完整）跑滿五 seed，而單變因消融與 100 epoch 檢查僅在 seed=7 完成，故定位為診斷實驗而非穩定性結論。

**Group Split 切分比例**：以 GroupShuffleSplit 兩步切割，先取 15\% 原圖群組為測試集，再從其餘樣本以 test\_size $\approx 0.176$ 切出驗證集（$0.176\times85\%\approx15\%$），最終近似 70/15/15。seed=7 案例的切分結果為訓練 774 張、驗證 168 張、測試 168 張，三者原圖群組零重疊；另以 seed=42、123、1234、2024 依相同流程各重複一次，以評估小樣本切分與模型初始化對結果的影響。Group Split 可避免同一原圖的裁切樣本同時落入訓練與測試集，但**尚未排除列印批次、材料顏色與拍攝條件造成的高階相關性**：若特定批次的 PLA 顏色或列印條件在各 split 中分布不均，仍可能使測試集結果偏樂觀。

MobileNetV3-Large 兩組策略（完整 vs 簡化）使用相同骨幹、輸入尺寸、批次大小與輔助頭結構，主要差在分類損失、Mixup 與資料採樣方式：

\begin{equation}
\begin{aligned}
L_{\text{full}}  &= L_{\text{Focal}}(\gamma=2.0,\,\text{LS}=0.1) + 0.3 \times L_{\text{MSE}} \\
L_{\text{plain}} &= L_{\text{CE}} + 0.3 \times L_{\text{MSE}}
\end{aligned}
\label{eq:total-loss}
\end{equation}

\noindent 其中 $L_{\text{full}}$ 對應完整設定，$L_{\text{plain}}$ 對應簡化設定。係數 0.3 為經驗設定：初步實驗中 $L_{\text{Focal}}$ 與 $L_{\text{MSE}}$ 在訓練初期量級相近（均在 $0.5 \sim 2.0$ 區間），取 0.3 可使評分輔助頭提供穩定梯度而不壓過分類損失。

Mixup 啟用時，Focal Loss 以混合比例 $\lambda$ 線性組合兩個硬標籤的 CE，再套用焦點加權 $(1-p_t)^\gamma$，其中 $p_t = \exp(-(\lambda \cdot \text{CE}_a + (1-\lambda) \cdot \text{CE}_b))$。此做法等效於 MixFocal，技術上偏離 Focal Loss 針對固定硬標籤的原始設計，屬本研究的簡化取捨。

完整設定同時啟用 Focal Loss 與 Label Smoothing 有一處衝突。Focal Loss 的加權因子 $(1-p_t)^\gamma$ 依賴模型對正確類別的預測機率 $p_t$：$p_t$ 愈高代表樣本愈「容易」、損失權重愈低，訓練因而聚焦於困難樣本。但 Label Smoothing 將目標由硬標籤 1.0 軟化至 $1-\epsilon=0.9$，人為限制 $p_t$ 上限，使模型即便對多數類別「幾乎確定」也無法觸發 Focal Loss 的強降權，削弱了困難樣本挖掘的效果。本研究未對「僅 FL」「僅 LS」與「FL+LS」做單獨消融，無法量化此組合是否優於單獨使用。

seed=7 詳細分析中，簡化設定於同一 Group Split 測試集取得 86.31\%（145/168），可作為後續混淆矩陣、校準與可視化的代表案例；但五 seed 重複後，簡化設定與完整設定在 accuracy / QWK 上未呈現顯著差異，因此本文不再將單次 86.31\% 解讀為策略穩定勝出，而是將其定位為可重現的嚴格切分基準。兩組設定之超參數整理於表 \ref{tab:hyperparameters}。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 訓練超參數設定（完整設定 vs 簡化設定；「共用」欄兩組相同）}
\label{tab:hyperparameters}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{lccc}
\hline
\textbf{超參數} & \textbf{完整設定} & \textbf{簡化設定} & \textbf{說明} \\
\hline
骨幹模型 & \multicolumn{2}{c}{MobileNetV3-Large (ImageNet V2)} & 共用 \\
輸入尺寸 & \multicolumn{2}{c}{224$\times$224 px} & 共用 \\
批次大小 & \multicolumn{2}{c}{32} & GPU 記憶體限制 \\
學習率 & \multicolumn{2}{c}{$2\times10^{-4}$} & AdamW 初始值 \\
Weight Decay & \multicolumn{2}{c}{$3\times10^{-4}$} & 共用 \\
學習率排程 & \multicolumn{2}{c}{\makecell{CosineAnnealingWarmRestarts\\$T_0=20$, $T_{\text{mult}}=2$, $\eta_{\min}=10^{-6}$}} & 共用 \\
Dropout & \multicolumn{2}{c}{\makecell{分類頭 $p=0.4$；評分頭 $p=0.2$}} & 共用 \\
訓練精度 & \multicolumn{2}{c}{FP16 Mixed Precision} & 共用 \\
最大輪數 & \multicolumn{2}{c}{25（另做 100 epoch 檢查）} & patience=7（檢查：35） \\
\hline
分類損失 & Focal $\gamma=2.0$ + LS 0.1 & Cross Entropy & --- \\
Mixup Alpha & 0.3 & 0.0 & 批次層級線性混合 \\
過採樣 & \makecell{WeightedRandomSampler\\（0.75 次方反比）} & 隨機洗牌 & \makecell{每 epoch 抽 4644 次\\vs 不加權} \\
\hline
\end{tabular}
\end{table}

\par\noindent\small\textit{100 epoch 檢查僅針對 MobileNetV3-Large 簡化設定，用來觀察較長訓練預算下結果是否改變。}

# 實驗結果與分析 {#sec:results}

## 資料集統計分析 {#sec:results-dataset}

本研究有效樣本共 1110 張，各等級分布如表 \ref{tab:dataset-dist} 及圖 \ref{fig:dataset-dist} 所示：A 等級（完美品）佔近半（546 張），B、E、F 三級樣本數偏少（87/72/32 張），類別不平衡明顯。故後續以 macro-F1、QWK、跨等級誤判與各等級 support 等多指標綜合評估，不單看整體 accuracy。

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
\caption{資料集各等級樣本分布長條圖（n = 1110；各柱標注樣本數與佔比）}
\label{fig:dataset-dist}
\end{figure}

## seed=7 詳細案例：同一測試集下的模型比較 {#sec:results-seed7}

本章採用 25 筆訓練紀錄（正式五 seed 共 20 筆 + seed=7 單變因消融 4 筆 + 100 epoch 檢查 1 筆），均以原始照片 ID 為分組單位進行 Group Split，確保訓練、驗證與測試集原圖零重疊。seed=7 案例之切分結果如表 \ref{tab:gs-split-summary} 所示。本節 seed=7 一律作為混淆矩陣、校準與視覺化的診斷案例；所有穩定性與模型排序結論皆以 \ref{sec:results-supplemental-multiseed} 節之五 seed 統計為準。

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

表 \ref{tab:seed7-results} 整理 seed=7、同一 Group Split 測試集下四組主要模型／設定之結果。最佳單次結果為 MobileNetV3-Large 完整設定，accuracy 89.88\%（151/168）。但完整與簡化設定的差距（89.88\% vs 86.31\%）同時含策略差異與約 6 倍訓練量差異，無法單獨歸因（詳見 \ref{sec:results-supplemental-ablation} 節）。

由於 seed=7 測試集中 B、E、F 等級分別只有 16、8、4 張，少數類別的 precision、recall 與 macro-F1 易受少量樣本變動影響。

\begin{table}[H]
\centering
\caption{seed=7 主要模型／設定於同一 Group Split 測試集之結果（單次案例，穩定性見表 \ref{tab:multiseed-results} 五 seed）}
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

表 \ref{tab:seed7-perclass} 為 MobileNetV3-Large 簡化設定於 seed=7 測試集之各等級精確率、召回率與 F1 分數。**B 等級召回率僅 56.3\%（9/16），為六等級中最低**：5 張 B 等級樣本被誤判為 A 等級（良品誤判為完美品）。此方向誤判在「合格/不合格篩選」情境下風險相對較低（漏判輕微瑕疵影響有限）；但若用於細粒度品質評分，B 被誤判為 A 將導致品質分系統性偏高，仍屬需注意的失效模式。上述誤判顯示 A/B 邊界為本系統最薄弱環節（品質分佐證見 \ref{sec:results-quality-score} 節）。

C/D 邊界混淆同樣顯著（C→D 有 7/35、D→C 有 2/28）；D→A 出現 2 次跨等級誤判（詳見後段 Grad-CAM 回溯分析）。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 簡化設定 seed=7 各等級精確率、召回率與 F1（測試集 168 張；標 $^{\dagger}$ 之列 Support $<$ 10，P/R/F1 無統計意義，僅供觀察）}
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
E（嚴重拉絲）$^{\dagger}$ & 0.750 & 0.750 & 0.750 & 8 \\
F（失敗品）$^{\dagger}$   & 0.750 & 0.750 & 0.750 & 4 \\
\hline
Macro avg     & 0.823 & 0.776 & 0.791 & 168 \\
\hline
\end{tabular}
\end{table}

\par\noindent\small\textit{\textbf{$^{\dagger}$ E、F 兩列樣本數過小，F 等級任一張誤判即造成 Recall 變動 25\%。}}

圖 \ref{fig:confusion-matrix} 為 seed=7 MobileNetV3-Large 簡化設定之混淆矩陣。對角線代表正確分類；非對角線誤判集中於相鄰等級（A/B、C/D、E/F），符合序數分類的預期行為；D→A 的 2 次跨等級誤判為本研究最需注意的誤判模式。

進一步回溯定位：2 筆 D→A 誤判均來自同一張原始照片（`IMG_20251206_163641_1`），對應裁切圖 fish02 與 fish04。其中 fish02 之模型信心度高達 0.941（品質分 96.7），屬**高信心誤判**；fish04 信心度為 0.565（品質分 85.0），處於分類邊界。兩筆均來自同一批次同一原圖，可能與該次拍攝角度使 D 級樣本的拉絲對比度降低有關，導致模型以高信心誤判為無拉絲的 A 級。

圖 \ref{fig:gradcam-da} 為此兩筆 D→A 誤判樣本之 Grad-CAM 可視化。fish02（信心度 0.941）之熱力圖高亮區域集中於魚骨結構而非拉絲間隙，顯示模型激活點偏離瑕疵區域；fish04（信心度 0.565）熱力圖較分散，反映模型在邊界樣本上的激活不確定性。

\begin{figure}[H]
\centering
\includegraphics[width=0.96\textwidth,height=0.52\textheight,keepaspectratio]{images/gradcam-DA-misclassified.png}
\caption{D→A 跨等級誤判 Grad-CAM 分析（上：fish02，信心度 0.941；下：fish04，信心度 0.565）。左欄為原始影像（真實等級 D），中欄為熱力圖，右欄為疊加結果；兩者熱力圖激活均偏離拉絲細絲區域。}
\label{fig:gradcam-da}
\end{figure}

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

表 \ref{tab:multiseed-results} 中，MobileNetV3-Large 完整設定的 accuracy std（5.98\%）為四組最大，約為其餘兩者的 2.6 倍，macro-F1 與 QWK 的 std 也同步偏高。在 1110 張小樣本規模下，對 seed（Group Split 切分與權重初始化）較敏感的設定，其單次結果的外推性遠不如方差小的設定。

完整設定雖在 seed=7 達 89.88\%（該 seed 最高），五 seed 平均卻是四組最低（80.12\%）且方差最大，可見其高分屬該次切分之利而非策略穩定優越；由於實際部署只看單次訓練結果，此高方差應視為負面訊號。簡化設定亦然（seed=7 86.31\% 高於平均 81.19\%），可見 seed=7 對兩種設定都偏寬鬆，單一 seed 結果均不宜外推。

以 MobileNetV3-Large 簡化設定作為比較基準之 paired t-test 如表 \ref{tab:paired-ttest} 所示。五 seed 結果顯示，其他模型／設定相對簡化設定的 accuracy 與 QWK 差異皆未達統計顯著；MobileNetV3-Large 完整與 ResNet18 完整在 macro-F1 上較高，且探索性檢定達 \(p<0.05\)，表面上意味完整策略或 ResNet18 對少數類別與類別邊界可能較有幫助。

然而此推論有兩點警語。其一，檢定 power 偏低：n=5 的 paired t-test 對中等效應量的 power 通常低於 0.4，「未達顯著」不可解讀為「兩設定等效」，僅表示在此樣本量下無法區分。其二，多重比較應涵蓋全部 9 個比較（3 個模型 × Accuracy／Macro-F1／QWK），而非僅 macro-F1 的 3 個；以 9 個比較的 Bonferroni 校正（$\alpha \approx 0.0056$），macro-F1 的兩個 p 值（0.0246、0.0363）均超出門檻，即使僅以 3 個比較校正（$\alpha \approx 0.0167$）亦不顯著。

綜上，本文將 macro-F1 的差異定位為**探索性趨勢**；加上 accuracy 與 QWK 未同步顯著、完整設定 std 偏大，本文**不宣稱任何單一設定為穩定最佳模型**。

**骨幹選擇之取捨**：五 seed 中 ResNet18 與 MobileNetV3-Large 完整之 macro-F1（0.712／0.713）略高於簡化（0.661），但兩點理由使本研究仍選 MobileNetV3-Large：（1）ResNet18 之 macro-F1 探索性 p 值（0.0363）經 Bonferroni 校正後不顯著，差異強度有限；（2）ResNet18 之 FLOPs（約 1.8 GFLOPs）為 MobileNetV3-Large（約 219 MFLOPs）的 8 倍以上，部署成本顯著較高，與本研究「未來邊緣部署彈性」之骨幹考量（見 \ref{sec:method-model-rationale} 節）相衝突。若後續以「最大化 macro-F1」為單一目標且不受部署成本限制，ResNet18 值得以更大樣本與多 seed 進一步驗證。

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

表 \ref{tab:ablation-results} 整理 seed=7 下之消融與 100 epoch 檢查。每列「移除 X」代表**僅移除 X，其餘訓練元件（Focal Loss、Label Smoothing、Mixup、Weighted Sampler）均保留**。此表用來診斷各訓練元件的影響，但僅單一 seed，不能作為穩定性結論。此單次結果中，移除 Weighted Sampler 使跨等級誤判升至 4.17\%（表中最高），移除 Label Smoothing 反而 accuracy 較高（88.10\%）。

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

## 品質分數與已標注資料擬合檢查 {#sec:results-quality-score}

品質分輔助頭之設計原則與等距假設限制詳見第 \ref{sec:method-model-dualhead} 節。表 \ref{tab:plain-quality-score} 整理 seed=7 測試集與全資料回測之各等級平均分；兩者均呈 A $>$ B $>$ C $>$ D $>$ E $>$ F 的單調遞減排序，可作為分類之外的輔助排序訊號（全資料回測含訓練集，僅供觀察）。其中 B、D、F 三級系統性偏高（最大偏差 D 級 +14.5 分），且非隨機分散：B 偏高與其低召回率（56.3\%）直接相關，被誤判為 A 的樣本以接近 100 分輸出，拉高 B 的均分；D 偏高則對應 C/D 邊界混淆，部分 D 被誤判為 C 而輸出 60 分附近。可見品質分偏差主要來自邊界分類的不確定性。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 簡化設定品質分對照（測試集 168 張 vs 已標注資料擬合檢查 1110 張之平均品質分）}
\label{tab:plain-quality-score}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{lccc}
\hline
\textbf{等級} & \textbf{目標分數} & \makecell{\textbf{測試集}\\\textbf{平均分}} & \makecell{\textbf{全資料回測}\\\textbf{平均分}\textsuperscript{$\ddagger$}} \\
\hline
A 完美品 & 100 & 99.6 & 99.5 \\
B 良好品 & 80 & 89.0 & 88.3 \\
C 輕微拉絲 & 60 & 58.8 & 60.5 \\
D 中度拉絲 & 40 & 54.5 & 50.9 \\
E 嚴重拉絲 & 20 & 23.5 & 30.8 \\
F 失敗品 & 0 & 12.5 & 16.2 \\
\hline
\end{tabular}
\end{table}

\par\noindent\small\textit{測試集平均分來自 seed=7 Group Split 測試紀錄（無原圖洩漏）；\textsuperscript{$\ddagger$} 全資料回測為 1110 張樣本（**包含 774 張訓練集樣本**）之回測平均分，僅供觀察模型對已標注資料之擬合與品質分排序，不可作為泛化能力指標。}

已標注資料擬合檢查之整體準確率為 87.30\%（969/1110），macro-F1 為 0.779；此結果含訓練資料，僅作擬合度與批量流程檢查。品質分雖維持單調排序，但 B、D、F 類存在系統性偏高，現階段不適合作為絕對品質門檻。

## 校準分析與視覺化診斷 {#sec:results-supplemental-calibration}

本節之校準、PR/ROC、Grad-CAM 與 t-SNE 均為 seed=7 單次之診斷工具，用於理解模型行為，不取代 \ref{sec:results-supplemental-multiseed} 節五 seed 統計。

**模型校準**：以 seed=7 MobileNetV3-Large 簡化模型進行 confidence calibration。溫度縮放（Temperature Scaling）的溫度參數 $T$ 以**驗證集**（168 張，與訓練集原圖零重疊）最小化 NLL 損失方式擬合，ECE 計算採用 15 個等距 confidence bins。未校準 ECE 為 0.0576；temperature scaling[@guoCalibrationModernNeural2017]（\(T=1.525\)）後 ECE 降至 0.0435。圖 \ref{fig:calibration-reliability} 為校準前後之 reliability diagram：校準後信心分布更接近對角線（理想校準），尤其在高信心區間的過信問題有所改善。高信心樣本（confidence \(>0.9\)）共有 112/168 張，準確率 95.5\%；低信心樣本（confidence \(<0.7\)）共有 28/168 張，準確率 46.4\%，落差顯著。因此，confidence 可作為人工複核流程的分流門檻：低信心預測不宜直接自動通過，建議進入人工確認。

\begin{figure}[H]
\centering
\includegraphics[width=0.88\textwidth,height=0.5\textheight,keepaspectratio]{images/calibration-reliability.png}
\caption{模型校準前後 reliability diagram（seed=7 MobileNetV3-Large 簡化設定；temperature scaling $T=1.525$）}
\label{fig:calibration-reliability}
\end{figure}

**PR 曲線分析**：One-vs-rest PR 曲線如圖 \ref{fig:pr-curves}。少數或邊界類別（B、D、E、F）AP 均低於 0.90，其中 E、F 最低（0.797、0.788），反映樣本稀少與等級邊界模糊的雙重挑戰；各等級 ROC AUC 則均超過 0.96，顯示二元區分的整體辨識力良好，但精確率與召回率的取捨仍是少數類別的主要瓶頸。

\begin{figure}[H]
\centering
\includegraphics[width=0.92\textwidth,height=0.55\textheight,keepaspectratio]{images/curves-pr.png}
\caption{One-vs-rest PR 曲線（seed=7 MobileNetV3-Large 簡化設定；各等級 AP 標示於圖例）}
\label{fig:pr-curves}
\end{figure}

**Grad-CAM 視覺解釋**：圖 \ref{fig:gradcam-correct} 與圖 \ref{fig:gradcam-wrong} 分別為預測正確與錯誤樣本的 Grad-CAM 熱力圖。本研究以手動掛載 forward/backward hook，對 MobileNetV3-Large \texttt{feature\_net[0][-1]}（features 模組末段最後一個 InvertedResidual block）之卷積輸出執行 Grad-CAM，熱力圖以 Jet colormap 生成後依 $0.55 \times \text{原圖} + 0.45 \times \text{熱力圖}$ 疊加。展示樣本取各等級中「第一個」正確或錯誤預測樣本（依資料集索引順序，非隨機或人工精選），解讀時應注意樣本選取並非追求最佳視覺效果。

正確預測案例中，部分樣本之熱力圖高亮集中於魚骨間隙的拉絲細絲區域，顯示模型可能以拉絲密度與分布作為判斷依據；惟 Grad-CAM 屬事後解釋工具，不能排除模型同時利用背景顏色、邊緣等非拉絲特徵。錯誤案例（多為 A/B 或 C/D 邊界樣本）熱力圖分散或集中於非拉絲區域，提示邊界樣本的特徵歧義為誤判主因之一，與 \ref{sec:results-seed7} 節 B 等級低召回的觀察一致。

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

**t-SNE 特徵可視化**：圖 \ref{fig:tsne} 為 seed=7 測試集（168 張）之 1280 維特徵向量以 t-SNE（perplexity=30，random\_state=7，\texttt{init=`pca'}）降維後的散佈圖。A 等級（無拉絲）形成緊密且獨立的聚落；C/D 等級部分樣本邊界相互滲透，與混淆矩陣中 C/D 誤判率較高的現象一致；B 等級聚落與 A 等級部分重疊，解釋了 5 張 B 等級樣本被誤判為 A 的現象。E/F 等級因樣本數過少（各 8/4 張），聚落位置解讀需謹慎。t-SNE 僅作探索性視覺化，其二維投影結果受 perplexity 與隨機初始化影響，不可作為等級可分性的定量依據。

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth,height=0.62\textheight,keepaspectratio]{images/tsne-test-features.png}
\caption{seed=7 測試集 1280 維特徵之 t-SNE 視覺化（perplexity=30，168 個樣本，顏色對應 A 至 F 等級）}
\label{fig:tsne}
\end{figure}

## 外部未標注影像診斷 {#sec:results-supplemental-ood}

外部未標注資料共 105 張照片，裁切為 630 支魚骨後進行推論，預測分布如圖 \ref{fig:external-dist} 所示。A 等級佔 66.2\%，較訓練集（49.2\%）更偏向良品側。平均 confidence 為 0.919，其中 confidence \(<0.7\) 者 11.7\%，低於測試集的低信心比例（16.7\%），顯示模型輸出分布正常，未出現崩潰或集中單一類別的異常。

由於此批資料沒有人工標籤，本文不計算也不宣稱 OOD accuracy；其用途僅是確認模型對外部照片不會產生明顯異常輸出，並作為未來建立具人工標籤 OOD 測試集的前置檢查。預測偏向良品側有兩種可能：外部良品比例確實較高，或模型在拍攝條件略有差異的樣本上傾向以高信心輸出 A 等級（即高信心誤判），缺乏人工標籤時無法區分。

「分布正常、未崩潰」只是模型可用的\textbf{必要而非充分條件}：高信心誤判不會表現為分布崩潰，卻是工業應用中更危險的失效模式（誤判為通過但實際為瑕疵品）。故本節結果不能推論外部拍攝條件下的泛化能力，建議後續優先取得人工標籤以區分上述兩種解釋。

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth,height=0.5\textheight,keepaspectratio]{images/external-unlabeled-distribution.png}
\caption{外部未標注 630 支魚骨推論之等級分布（無人工標籤，僅作 sanity check；A 等級佔 66.2\%）}
\label{fig:external-dist}
\end{figure}

## 整批處理流程之推論延遲量測 {#sec:results-batch}

以 seed=7 MobileNetV3-Large 簡化模型於 168 張測試樣本量測，平均單張模型推論時間為 6.90 ms，約 144.9 張/秒；完整 Group Split 模型約 7.05 ms，約 141.8 張/秒（兩者 0.15 ms 差異在量測雜訊範圍內）。量測條件為：推論以 \textbf{batch\_size=1} 逐張送入 GPU，影像張量\textbf{預先載入記憶體}（不含磁碟讀取、裁切、resize/normalize 等前處理），並以 20 張 warm-up 後計時 168 張，所得為\textbf{純模型前向傳播延遲}。實際部署時，前處理（影像讀取、裁切）與後處理（分級排序、報告生成）的耗時可能與推論本身相當；此數字僅代表單機 GPU 的純前向延遲屬毫秒級，不等同於整批流程的產線吞吐量。

# 結論與建議 {#sec:conclusion}

## 結論 {#sec:conclusion-summary}

本研究以 FDM 列印魚骨件為標的，建立一套基於深度學習影像辨識的拉絲瑕疵輔助辨識與品質評分原型，完成六等級（A 至 F）分類與評分輸出流程。主要研究成果總結如下：

1. **單一標注者下的可重複品質等級制度**：以目視估計拉絲覆蓋比例為判斷依據，建立六個品質等級定義並配合 A 至 F 範例圖；模型在嚴格測試集上可部分重現此套固定準則，能降低批量檢查負擔並輔助人工複核（單一標注者之限制詳見 \ref{sec:method-grading} 節）。
2. **系統性資料蒐集與標注**：透過多批次列印與拍攝，配合 Label Studio 工具完成全部樣本的人工標注，建立含 1110 張有效樣本、185 個原圖群組的六等級分類資料集；以原圖層級 Group Split 確保訓練、驗證與測試集之原圖零重疊，為後續模型效能評估提供無洩漏基準。
3. **深度學習模型效能與不確定性**：五 seed 正式比較顯示四組模型／策略平均 accuracy 80.12\%–81.19\%、平均 QWK 約 0.91，各項統計檢定（Bonferroni 校正後）均未達顯著差異，故不宣稱任一設定為穩定最佳；A/B 邊界（B 等級召回率 56.3\%）為最薄弱環節（詳見第 \ref{sec:results-supplemental-multiseed} 節）。
4. **整批照片自動處理流程**：整合自動裁切、逐張前向推論、分級輸出與 HTML 可視化報告，形成由原始照片到品質等級報告之離線處理流程；於 RTX 3050 Laptop GPU 上量測純模型前向延遲約為 7 ms（量測條件詳見 \ref{sec:results-batch} 節），屬部署參考基準而非端到端產線吞吐量。
5. **品質評分輸出**：模型同時輸出 0 至 100 的連續品質分，各等級平均分呈單調遞減（表 \ref{tab:plain-quality-score}），可作等級內排序參考（使用限制詳見 \ref{sec:method-model-dualhead} 節）。

\vspace{0.5em}

**核心結論**：

> 本系統作為拉絲瑕疵輔助辨識工具具初步可行性（五 seed 平均 accuracy 約 80–81\%、QWK 約 0.91）。**最主要的效能瓶頸在 A/B 邊界**（B 等級召回率 56.3\%），且與「單一標注者、未驗證一致性」的資料侷限彼此交織，無法僅靠更換模型解決。在完成標注一致性驗證、具標籤 OOD 測試集與跨機型／跨材料驗證之前，本系統不宜部署於訓練條件以外的拍攝環境或硬體／材料組合。

## 建議 {#sec:conclusion-future}

以下建議依其對「應用可信度」的影響由高到低排列，前三項為本系統部署前必須補齊的條件。

\noindent\textbf{第一優先（應用可信度前提）}

1. **標注一致性驗證**：邀請第二位以上標注者重新標注 100 張涵蓋 A 至 F 之樣本，計算 Cohen's $\kappa$ / Fleiss' $\kappa$；若 $\kappa < 0.7$，需重新檢視標注準則並補充邊界判斷規則，再重新訓練評估。
2. **固定拍攝條件**：目前採半標準化拍攝（AE/AWB 未鎖定）；建議補拍涵蓋固定光源、固定曝光條件之標準化測試集，以量化拍攝條件變異對模型效能的影響。
3. **具人工標籤的 OOD 測試集**：現有外部 105 張照片僅完成未標注推論的分布合理性檢查（sanity check），建議補充人工標籤，計算 OOD accuracy 與各等級召回率退化幅度，再評估是否具備部署條件。

\noindent\textbf{第二優先（提升實驗嚴謹性）}

4. **補充少數等級資料**：優先補充 B 級邊界樣本、E 級與 F 級失敗樣本，使各等級支撐穩定的多 seed 估計。
5. **完整因子設計與批次切分**：補充 ResNet18 簡化與 EfficientNet-B0 簡化，完成 3 架構 $\times$ 2 策略之完整因子設計以分離架構與訓練策略的效果；並補做以列印批次為單位的 Batch Split，量化批次內相關性對效能估計的影響。
6. **Ordinal-aware loss**：補做 CORAL [@caoRankConsistentOrdinal2020]、CORN [@shiDeepNeuralNetworks2023] 等序數感知損失函數之對照，以 QWK 與跨等級誤判率為主要評估指標。

\noindent\textbf{第三優先（擴展應用範圍）}

7. **跨機型 / 跨材料 / 跨幾何泛化驗證**：蒐集其他印表機（Prusa MK4、Creality K1）、材料（PETG、ABS）與幾何（盒體、齒輪）之樣本，量化域外退化幅度。
8. **即時列印監控**：評估整合 Bambu Lab A1 內建攝影機進行列印中即時監控，並評估即時影像品質與誤報成本。
9. **品質評分校準**：邀請有經驗操作人員對樣本進行主觀連續評分（0 至 100），以人工共識分數作為監督標籤，計算 ICC 量化系統可信度。
10. **模型輕量化與邊緣部署**：評估知識蒸餾、剪枝或 INT8 量化，向 Raspberry Pi 或 NVIDIA Jetson 等邊緣裝置部署；任何壓縮方案須在相同資料切分下重新驗證分類效能與推論時間。

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

本附錄保留列印過程中四張代表性照片，分別對應「正常列印中」、「正常列印完成」、「輕微拉絲」、「列印失敗」四種狀態。

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

本附錄依現有 Bambu Studio 截圖整理本研究可追溯之列印參數設定（基於 PolyTerra PLA 0.08 mm 預設設定檔）。表 \ref{tab:param-summary} 彙整影響列印品質之關鍵參數值，圖 \ref{fig:param-quality-representative} 為品質頁籤畫面。

\begin{table}[H]
\centering
\caption{Bambu Lab A1 列印參數彙整}
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
\caption{Bambu Studio 品質頁籤截圖（層高 0.08 mm、線寬 0.42 mm）}
\label{fig:param-quality-representative}
\end{figure}

\setcounter{figure}{0}
\setcounter{table}{0}

# PLA 耗材與冷卻設定彙整 {#sec:appendix-material}

本研究使用 Polymaker PolyTerra PLA 1.75 mm 線材；耗材物性、列印溫度與冷卻風扇策略依現有 Bambu Studio 截圖整理。表 \ref{tab:material-summary} 彙整關鍵設定值，圖 \ref{fig:cooling-representative} 為冷卻模式設定畫面。

\begin{table}[H]
\centering
\caption{PolyTerra PLA 耗材與冷卻設定彙整}
\label{tab:material-summary}
\small
\setlength{\tabcolsep}{3pt}
\begin{tabular}{ccc}
\hline
\textbf{項目} & \textbf{設定值} & \textbf{備註} \\
\hline
耗材類型 / 供應商 & PLA / Polymaker & 配方 PolyTerra PLA \\
線材直徑 & 1.75 mm &  \\
密度 / 流量比例 & 1.31 g/cm$^3$ / 0.98 & 預設值 \\
噴嘴溫度 & 220 $^\circ$C & 首層與其它層相同；建議區間 $190 \sim 240\,^\circ$C \\
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
\caption{冷卻模式設定截圖（風扇 60\%$\sim$80\%、最小列印速度 20 mm/s、懸垂強制冷卻）}
\label{fig:cooling-representative}
\end{figure}
