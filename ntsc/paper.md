---
# ============================================================
# === 國科會大專學生研究計畫成果報告基本資訊 ===
# ============================================================
thesis-title-zh: "3D 列印件瑕疵檢測與品質評分研究設計"
thesis-title-en: "Defect Detection and Quality Grading System for 3D-Printed Parts"
university-zh: "國立聯合大學"
department: "機械工程學系"
program: "大專學生研究計畫"
degree: "成果報告"
student: "劉哲銘"
advisor: "張致文 博士"
year: "115"
month: "4"

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

# ============================================================
# === 頁碼與標題設定 ===
# ============================================================
numbersections: true
secnumdepth: 4
toc: false

# ============================================================
# === LaTeX 標題格式、頁碼、超連結等進階設定 ===
# ============================================================
header-includes:
  - |
    ```{=latex}
    \usepackage{titlesec}
    \usepackage{titletoc}
    \usepackage{makecell}
    \usepackage{indentfirst}
    \usepackage{fancyhdr}
    \usepackage{graphicx}
    \usepackage{caption}
    \usepackage{hyperref}
    \usepackage{xcolor}
    \usepackage{float}
    \usepackage{longtable}
    \usepackage{colortbl}
    \usepackage{array}
    \usepackage{multirow}
    \usepackage{zhnumber}

    % === 圖表位置：偏好原位，允許少量浮動 ===
    \floatplacement{figure}{!htbp}
    \floatplacement{table}{!htbp}

    % === 圖表編號改用 章節-序號（例如 圖 3-2、表 4-1） ===
    \numberwithin{figure}{section}
    \numberwithin{table}{section}
    \renewcommand{\thefigure}{\arabic{section}-\arabic{figure}}
    \renewcommand{\thetable}{\arabic{section}-\arabic{table}}

    % === 公式：靠左 + 自動編號 (節號-公式號) ===
    \setlength{\mathindent}{0pt}
    \numberwithin{equation}{section}
    \renewcommand{\theequation}{\arabic{section}-\arabic{equation}}

    % === 超連結設定 ===
    \hypersetup{
      colorlinks=true,
      linkcolor=black,
      citecolor=blue,
      urlcolor=blue,
      breaklinks=true
    }

    % === 首行縮排 2 字元 ===
    \setlength{\parindent}{2em}

    % === 圖表標題置中、名稱中文化 ===
    \captionsetup{justification=centering}
    \captionsetup[figure]{name={圖},labelsep=space}
    \captionsetup[table]{name={表},labelsep=space}

    % === 目錄/圖目錄/表目錄標題 ===
    \renewcommand{\contentsname}{目錄}
    \renewcommand{\listfigurename}{圖目錄}
    \renewcommand{\listtablename}{表目錄}

    % === 章標題格式：與本文同字級、不粗體、左對齊縮排 2em（對齊 NSTC 大專生報告 Word 版） ===
    \titleformat{\section}
      {\normalsize}
      {第\zhnum{section}章}{1em}{}
    \titlespacing*{\section}{2em}{12pt}{6pt}

    % === 節標題格式：與本文同字級、不粗體 ===
    \titleformat{\subsection}
      {\normalsize}
      {\thesubsection}{1em}{}
    \titlespacing*{\subsection}{2em}{6pt}{6pt}

    % === 小節標題格式：與本文同字級、不粗體 ===
    \titleformat{\subsubsection}
      {\normalsize}
      {\arabic{section}.\arabic{subsection}.\arabic{subsubsection}}{1em}{}
    \titlespacing*{\subsubsection}{2em}{6pt}{6pt}

    % === 第四層標題格式：與本文同字級、不粗體 ===
    \titleformat{\paragraph}
      {\normalsize}
      {\arabic{section}.\arabic{subsection}.\arabic{subsubsection}.\arabic{paragraph}}{1em}{}
    \titlespacing*{\paragraph}{2em}{6pt}{6pt}

    % === 目錄／圖目錄／表目錄頁面標題：置中、大字、粗體（取代預設的 \section*） ===
    \makeatletter
    \renewcommand\tableofcontents{%
      \begin{center}{\Large\bfseries\contentsname}\end{center}%
      \vspace{1em}%
      \@starttoc{toc}%
    }
    \renewcommand\listoffigures{%
      \begin{center}{\Large\bfseries\listfigurename}\end{center}%
      \vspace{1em}%
      \@starttoc{lof}%
    }
    \renewcommand\listoftables{%
      \begin{center}{\Large\bfseries\listtablename}\end{center}%
      \vspace{1em}%
      \@starttoc{lot}%
    }
    \makeatother

    % === TOC 章節顯示「第X章」前綴；子節仍用阿拉伯數字（不繼承 \thesection） ===
    \renewcommand{\thesection}{第\zhnum{section}章}
    \renewcommand{\thesubsection}{\arabic{section}.\arabic{subsection}}
    \renewcommand{\thesubsubsection}{\arabic{section}.\arabic{subsection}.\arabic{subsubsection}}

    % === TOC 各層級寬度：第一層留 4.5em 給「第X章」，第二/三層依層級縮排 ===
    \makeatletter
    \renewcommand*\l@section{\@dottedtocline{1}{0em}{4.5em}}
    \renewcommand*\l@subsection{\@dottedtocline{2}{4.5em}{3em}}
    \renewcommand*\l@subsubsection{\@dottedtocline{3}{7.5em}{4em}}
    \makeatother

    % === 圖目錄／表目錄條目加「圖」「表」前綴 ===
    \titlecontents{figure}
      [0em]
      {}
      {\contentslabel[圖 \thecontentslabel]{4.5em}}
      {}
      {\titlerule*[0.5pc]{.}\contentspage}
    \titlecontents{table}
      [0em]
      {}
      {\contentslabel[表 \thecontentslabel]{4.5em}}
      {}
      {\titlerule*[0.5pc]{.}\contentspage}

    % === 頁碼樣式 ===
    \fancypagestyle{frontmatter}{
      \fancyhf{}
      \fancyfoot[C]{\thepage}
      \renewcommand{\headrulewidth}{0pt}
    }
    \fancypagestyle{mainmatter}{
      \fancyhf{}
      \fancyfoot[C]{\thepage}
      \renewcommand{\headrulewidth}{0pt}
    }

    % === 左右對齊 ===
    \usepackage{ragged2e}
    \justifying
    \setlength{\emergencystretch}{3em}

    % === 技術識別符允許在底線處換行 ===
    \let\paperforgeOrigUnderscore\_
    \renewcommand{\_}{\ifmmode\paperforgeOrigUnderscore\else\textunderscore\allowbreak\fi}

    ```
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

{\fontsize{14pt}{18pt}\selectfont 計\,畫\,名\,稱：3D 列印件瑕疵檢測與品質評分研究設計\par}

\vspace{0.3cm}

{\fontsize{16pt}{20pt}\selectfont ＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\,＊\par}

\end{center}

\vspace{1.2cm}

\noindent\hspace*{2cm}\begin{minipage}{0.8\textwidth}
\setlength{\parskip}{0.35cm}

執行計畫學生：劉哲銘

學生計畫編號：NSTC 114-2813-C-239-054-E

研\,究\,期\,間：114 年 07 月 01 日至 115 年 02 月 28 日止，計 8 個月

指\,導\,教\,授：張致文
\end{minipage}

\vfill

\begin{center}
\setlength{\parskip}{0.3cm}

處理方式：本計畫可公開查詢

執\,行\,單\,位：國立聯合大學機械工程學系

中\,華\,民\,國\,115 年 04 月 27 日
\end{center}

\vspace*{0.5cm}

\end{titlepage}

<!-- ============================================================ -->
<!-- 內封頁 -->
<!-- ============================================================ -->

\begin{titlepage}
\begin{center}

\vspace*{2cm}

{\bfseries\fontsize{18pt}{24pt}\selectfont 國科會\quad 大專學生專題研究計畫\par}

\vspace{2.5cm}

{\bfseries\fontsize{22pt}{30pt}\selectfont 3D 列印件瑕疵檢測與品質評分研究設計\par}

\vspace{1cm}

{\fontsize{14pt}{18pt}\selectfont NSTC 114-2813-C-239-054-E\par}

\vspace{3.5cm}

指導老師：張致文 老師

\vspace{1cm}

專題學生：劉哲銘

\vfill

中\,華\,民\,國\,115\,年\,4\,月

\vspace{1cm}

\end{center}
\end{titlepage}

<!-- ============================================================ -->
<!-- 摘要（羅馬數字頁碼 i, ii, iii ...） -->
<!-- ============================================================ -->

\pagenumbering{roman}
\pagestyle{frontmatter}

摘要

3D 列印技術近年來已廣泛應用於工業製造、醫療輔具、教育教具及個人創作等多元領域，然而熔融沉積成型（FDM）列印過程中常因噴嘴溫度、回抽設定或列印速度等參數控制不當，導致拉絲（Stringing）、翹曲（Warping）及裂痕（Cracking）等表面瑕疵，影響成品外觀品質與結構完整性。傳統目視檢測方式費時費力，且因操作人員主觀判斷標準不一，難以在大規模生產場景中維持品質評估的一致性與效率。

本研究旨在建立一套以深度學習影像辨識為核心的 3D 列印件自動瑕疵辨識與品質評分系統，以魚骨形狀 PLA 列印件為研究標的，聚焦於拉絲瑕疵嚴重程度的六等級分類（A 至 F）。本研究之流程依序為列印實驗、影像拍攝、影像裁切與模型訓練；資料蒐集期間為 2025/11/22 至 2026/02/07，其中主要列印紀錄集中於 2025/11/22 至 2025/12/10，並於 2026/02/05 至 2026/02/07 補充少數類別與失敗件樣本；影像拍攝於列印完成後進行，並於 2026/02/10 前完成資料裁切、標注、模型訓練與辨識分析。最新資料集共取得 1110 筆有效魚骨樣本，最終整理出 A 級 546 張、B 級 87 張、C 級 213 張、D 級 160 張、E 級 72 張、F 級 32 張。

模型架構選用 MobileNetV3-Large（ImageNet V2 預訓練權重），以遷移學習方式進行六分類微調，並附加品質評分輔助頭同時輸出 0 至 100 的連續品質分數。訓練策略整合 Focal Loss（$\gamma = 2.0$）結合 Label Smoothing（0.1）、批次層級 Mixup 資料增強（$\alpha=0.3$）、Weighted Random Sampler 過採樣、Cosine Annealing Warm Restarts 學習率排程及 Early Stopping 機制（patience=35），以全面應對資料不平衡與小樣本過擬合問題。實驗結果顯示，最新改良版模型（MobileNetV3-Large）在全資料集整體準確率達 95.86\%（1064/1110），各等級準確率分別為：A 級 98.7\%、B 級 92.0\%、C 級 96.7\%、D 級 90.6\%、E 級 88.9\%、F 級 93.8\%。獨立測試集共 167 筆，測試準確率為 83.23\%（139/167），各等級測試準確率分別為 A 級 98.8\%、B 級 53.8\%、C 級 87.5\%、D 級 54.2\%、E 級 54.5\%、F 級 80.0\%。相較於初版模型（MobileNetV3-Small，86.9\%），最新模型全資料集準確率提升約 9.0 個百分點，且 C、D、F 等瑕疵等級的辨識能力明顯改善；惟 B、D、E 等少數或邊界類別於獨立測試集仍有改善空間。本系統已完整整合自動裁切、批量辨識、分級輸出與 HTML 可視化報告等功能，具備作為生產端品質管控輔助原型的應用可行性。

關鍵詞：3D 列印、熔融沉積成型（FDM）、瑕疵檢測、深度學習、MobileNetV3、品質評分、遷移學習、Focal Loss、資料不平衡

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

3D 列印技術（Three-Dimensional Printing），又稱積層製造（Additive Manufacturing, AM），係指透過電腦輔助設計（CAD）軟體建立三維數位模型後，依據切片軟體產生的路徑指令，將材料逐層堆積成形的製造技術[@iso52900]。自 Charles Hull 於 1984 年提出光固化成型技術（Stereolithography, SLA）相關專利，並由 3D Systems 推動早期商業化應用後，3D 列印技術歷經數十年的持續演進，應用範圍由工業快速原型製造逐漸擴展至航太、汽車、醫療、電子、建築及個人消費等多元應用領域[@gibson2021additive; @3dsystems-history]。根據 MarketsandMarkets 於 2023 年發布之市場研究報告，全球 3D 列印市場規模預估將由 2023 年約 150 億美元成長至 2028 年約 345 億美元，年均複合成長率約為 18.1\%，顯示此技術在全球製造業中的戰略地位日益重要[@marketsandmarkets2023-3dprint]。

在眾多 3D 列印技術中，熔融沉積成型（Fused Deposition Modeling, FDM）因設備成本相對低廉、操作流程較為簡易，且可支援 PLA、PETG、ABS、TPU 等多種熱塑性材料，成為桌上型與教育應用場域中常見的 3D 列印技術之一[@gibson2021additive; @stratasys-fdm]。FDM 的基本工作原理是將熱塑性聚合物線材（Filament，直徑通常為 1.75 mm 或 2.85 mm）送入加熱腔，融化後由噴嘴（Nozzle）擠出，依照切片路徑在熱床（Heated Bed）上逐層堆積，冷卻固化後形成實體成品。由於 FDM 技術的普及，其列印品質管控的重要性日益受到業界與學術界的重視。

然而，FDM 列印的品質受到多項關鍵參數的交互影響，包括噴嘴溫度、熱床溫度、列印速度、回抽距離（Retraction Distance）與速度、層高（Layer Height）、填充密度（Infill Density）、冷卻風扇轉速及支撐結構設定等。任一參數設定不當，均可能引發不同類型的列印瑕疵，導致成品品質下降。目前業界對 FDM 列印品質的評估，仍多依賴操作人員的人工目視檢查，缺乏系統化、自動化的品質管控機制，難以滿足工業 4.0 背景下智慧製造的需求。

工業 4.0（Industry 4.0）一詞最早於 2011 年德國漢諾威工業展（Hannover Fair）中被提出，後續由德國工業 4.0 工作小組於 2013 年提出正式推動建議。其核心在於透過資訊通訊技術，使機器、製程與生產系統形成智慧化連網，進而提升製造流程的即時性、自動化與資訊整合能力[@din-industry40; @plattform-industrie40]。在此背景下，將深度學習技術導入 3D 列印品質管控，建立自動化的瑕疵辨識與評分系統，既符合工業 4.0 的技術路線，也具有顯著的實際應用價值。

## 研究動機 {#sec:intro-motivation}

在實際的 3D 列印生產場景中，品質管控面臨以下幾項核心困難：其一，人工目視效率低落，當列印批量增加時，每件成品的逐一檢視耗時過長，成為生產流程的瓶頸；其二，主觀判斷標準不一，不同操作人員對同一件成品的品質評估可能存在差異，尤其在瑕疵程度接近等級邊界的案例中，判斷結果的不一致性會降低品質數據的可信度；其三，缺乏量化依據，傳統目視評估難以提供精確的數值品質分數，無法為列印參數的系統性優化提供回饋依據；其四，難以建立品質歷史紀錄，人工評估結果不易系統性地留存，不利於品質趨勢分析與製程改善。

有鑑於此，本研究的研究動機源自對以上痛點的深刻認識：若能以深度學習模型模擬有經驗品管人員的判斷邏輯，將瑕疵辨識與品質評分工作自動化，不僅可大幅提升檢測效率，更能確保評估標準的一致性與客觀性。此外，本研究的另一動機來自對「有限資料量下如何訓練高效能模型」此一挑戰的探索興趣。在實際應用場景中，取得充足的標注資料往往成本高昂，如何在樣本數受限的條件下（本研究最少的 F 等級為 32 張），透過遷移學習、資料增強及損失函數設計等技術手段，建立具可行性的分類模型，是本研究的核心技術課題。

## 研究目的 {#sec:intro-purpose}

本研究之主要研究目的如下：（一）制定客觀可量化的六等級品質評分標準（A 至 F），以拉絲面積佔比為主要依據，並製作各等級範例圖，建立標注與評分的參考基準；（二）系統性地建立涵蓋各品質等級的 3D 列印魚骨件影像資料集，以 Label Studio 工具完成精確人工標注；（三）以 MobileNetV3-Large 預訓練模型為基礎，透過遷移學習與多項訓練優化策略，在有限樣本量條件下達到全資料集整體準確率 95\% 以上；（四）實現同時輸出六分類標籤與 0 至 100 品質分數的雙輸出模型，提供更細緻的品質量化依據；（五）開發端對端自動化批量辨識系統，整合影像裁切、推論、分級輸出與報告產生功能。

## 研究範圍 {#sec:intro-scope}

本研究的研究範圍以 FDM 技術列印之魚骨形狀 PLA 材質列印件為主要研究對象，聚焦於拉絲瑕疵的嚴重程度分類，不包含翹曲及裂痕瑕疵的深入分析（因現有樣本中此兩類瑕疵數量不足）。實驗設備限定為 Bambu Lab A1 3D 印表機，耗材為標準 PLA 線材，拍攝環境為固定背景的室內自然光環境，因此模型的泛化能力主要針對此特定設備與材料條件。資料規模方面，最新資料集共取得 1110 筆有效魚骨樣本，分屬六個品質等級，最多等級 546 張（A 級），最少等級 32 張（F 級）。

## 研究流程 {#sec:intro-flow}

本研究的整體執行流程分為三大階段：第一階段為資料蒐集與前處理，包含 3D 列印樣本製作、影像拍攝、魚骨自動裁切及人工標注；第二階段為模型訓練與評估，包含資料集整理、模型訓練、效能評估及新舊版本比較；第三階段為系統整合與應用，包含批量辨識系統開發、可視化報告產生及實際應用驗證。詳細流程如圖 \ref{fig:overall-flow} 所示。

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.6\textwidth,keepaspectratio]{images/image1.png}
\caption{研究整體流程圖}
\label{fig:overall-flow}
\end{figure}

# 文獻回顧 {#sec:literature}

## FDM 3D 列印技術概述 {#sec:literature-fdm}

熔融沉積成型（Fused Deposition Modeling, FDM）由 Scott Crump 於 1989 年發明，並於 1992 年由 Stratasys 公司商業化推出[@stratasys-fdm]。FDM 的工作流程分為四個主要步驟：（1）數位建模：以 CAD 軟體（如 Autodesk Fusion 360、SolidWorks 等）建立三維數位模型並輸出 STL 或 3MF 格式；（2）切片處理：以切片軟體（如 Bambu Studio、PrusaSlicer 等）將模型切分為若干水平薄層，生成噴嘴移動路徑指令（G-code）；（3）列印成形：印表機依 G-code 指令逐層擠出熔融材料堆積成形；（4）後處理：拆除支撐結構、打磨或表面處理以達到所需品質。

影響 FDM 列印品質的關鍵參數可分為溫度類、速度類及結構類三大類。溫度類包括噴嘴溫度（Nozzle Temperature）、熱床溫度（Bed Temperature）及環境溫度；速度類包括列印速度（Print Speed）、移位速度（Travel Speed）、回抽速度（Retraction Speed）；結構類包括層高（Layer Height）、填充密度（Infill Density）、填充圖案（Infill Pattern）、支撐結構類型及冷卻設定。這些參數之間存在複雜的交互作用，例如提高列印速度通常需要相應提高噴嘴溫度以確保材料充分熔融，但過高的溫度又會增加拉絲風險，因此參數調校是一項需要豐富實驗經驗的技術工作。

## 3D 列印常見瑕疵類型 {#sec:literature-defects}

根據本研究的計畫書及現有文獻，FDM 列印常見的表面瑕疵主要包含以下三類，如圖 \ref{fig:defect-stringing} 至圖 \ref{fig:defect-cracking} 所示。

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.65\textwidth,keepaspectratio]{images/image2.png}
\caption{拉絲（Stringing）瑕疵：噴嘴移位時殘留的細絲}
\label{fig:defect-stringing}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.65\textwidth,keepaspectratio]{images/image3.png}
\caption{翹曲（Warping）瑕疵：底層因冷卻收縮而翹起}
\label{fig:defect-warping}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.65\textwidth,keepaspectratio]{images/image4.png}
\caption{裂痕（Cracking）瑕疵：層間結合不足導致的分層}
\label{fig:defect-cracking}
\end{figure}

**拉絲（Stringing）**：係指噴嘴在非列印區域移動時，熔融材料因回抽不足、噴嘴溫度過高或材料流動性過大而持續滲出，進而在列印件表面形成細絲狀殘留的現象。其嚴重程度通常與回抽距離與速度、噴嘴溫度、移位速度及冷卻效率等參數交互影響有關[@bambulab-stringing; @bambulab-quality]。

**翹曲（Warping）**：係指列印件於冷卻過程中因材料收縮與平台附著力不足，使底層邊角產生上翹或脫離列印平台的現象。此問題通常與熱床溫度、第一層附著、環境溫度變化、列印速度與材料熱收縮特性有關[@prusa-warping]。

**裂痕（Cracking）或層間分離（Layer Separation）**：係指列印件不同層之間因冷卻速率差異、層間黏結不足或翹曲應力過大，導致層與層之間產生分離裂縫的現象。此類缺陷會降低列印件的結構完整性與機械強度[@prusa-layer-separation]。

## 電腦視覺與深度學習於工業瑕疵檢測 {#sec:literature-cv-dl}

電腦視覺（Computer Vision）技術在工業品質檢測領域的應用已有數十年歷史，早期方法以傳統影像處理技術為主，包括邊緣偵測、閾值分割、形態學運算及特徵工程等，需要領域專家手動設計特徵提取規則。此類方法在受控環境下（固定光源、背景及目標位置）表現尚可，但對光線變化、姿態變化及背景干擾的魯棒性較差，且難以應對複雜的多類別瑕疵辨識任務。

深度學習技術的崛起從根本上改變了電腦視覺的研究範式[@goodfellow2016deeplearning; @lecun1998gradient]。卷積神經網路（CNN）以端到端的方式自動學習影像的層次化特徵表示，從底層的邊緣和紋理特徵到高層的語義特徵，無需人工設計特徵，且在充足資料的支持下，其辨識精度遠超傳統方法[@deng2009imagenet; @he2016resnet]。近年來，CNN 已被廣泛應用於半導體晶圓瑕疵檢測、紡織品缺陷辨識、鋼板表面瑕疵分類、PCB 板焊接缺陷偵測等工業品質管控任務[@huang2021surface; @lin2020realtime]，並在多項基準測試中達到甚至超越人類水準。

## 相關文獻探討 {#sec:literature-related}

Jogin 等人[@jogin2018cnn]對卷積神經網路在 CIFAR-10 影像分類任務上進行系統性研究，採用 6 層 Conv2D--ReLU--MaxPooling 模組架構，搭配全連接層與 Softmax 分類頭，對 10 類 50,000 張 32$\times$32 像素彩色影像進行分類，最終達到 85.97\% 的準確率，顯著優於同期的支援向量機（SVM）、決策樹及隨機森林等傳統機器學習方法。此研究奠定了 CNN 在中等規模影像分類任務中的效能基準，並論證了 CNN 深度特徵在多類別辨識中的優越性，為本研究採用 CNN 架構提供了重要參考依據。

Scarpa 等人[@scarpa2018cnn-sentinel]提出基於三層 CNN 的多源衛星影像融合方法，將 Sentinel-1（SAR 雷達）與 Sentinel-2（光學）影像進行跨模態特徵融合，以估算 NDVI（歸一化植被指數）。實驗在非洲 Burkina Faso 農業區進行，結果顯示融合模型的相關係數達 0.907，PSNR 達 25.33 dB，優於傳統插值法與回歸法。此研究展現了 CNN 在處理不同來源、不同模態資料時的強大表徵學習能力，間接支持了將 CNN 應用於多種拍攝條件下的列印件品質辨識的可行性。

Varshni 等人[@varshni2019pneumonia]採用多種預訓練 CNN 模型（包括 DenseNet-169、ResNet-50、VGG-16 及 Xception）對 ChestX-ray14 資料集中的肺炎 X 光影像進行特徵提取，並搭配 SVM（RBF 核）分類器進行二分類。DenseNet-169+SVM 的組合在 AUC 指標上達到 0.8002，優於其他模型。此研究證明，預訓練模型的遷移學習在醫學影像等小樣本任務中的有效性，對本研究在有限標注樣本條件下採用預訓練 MobileNetV3-Large 提供了充分的方法論依據。

Lin 等人[@lin2017focal]提出的 Focal Loss 最初設計用於解決目標偵測任務中前景（目標）與背景（非目標）的極端類別不平衡問題。其核心思想是在標準交叉熵損失的基礎上，引入調焦因子 $(1-p_t)^\gamma$，對模型已正確分類的高信心樣本降低損失權重，使訓練過程更專注於困難樣本（Hard Example），從而在類別分布極端不均的情況下仍能有效訓練。本研究中，A 等級與 F 等級樣本比例達 25:1，直接應用 Focal Loss 可有效緩解多數類別主導訓練梯度的問題。

## MobileNetV3 架構 {#sec:literature-mobilenetv3}

MobileNet 系列最早由 Howard 等人提出，其核心設計是以深度可分離卷積降低模型參數量與計算量，使 CNN 更適合部署於行動端與邊緣裝置[@howard2017mobilenets]。MobileNetV3 則進一步結合神經架構搜尋、Squeeze-and-Excitation 模組與 Hard-Swish 激活函數，以提升精度與推論效率[@howard2019mobilenetv3]。MobileNetV3-Large 是 Google 針對移動端與邊緣計算場景設計的高效深度學習模型，其架構通過神經架構搜索（NAS）技術自動搜尋最優配置，並融合以下三項核心技術：（1）**深度可分離卷積（Depthwise Separable Convolution）**：將標準卷積分解為深度卷積（Depthwise Conv）與逐點卷積（Pointwise Conv）兩步驟，在保持感受野的同時大幅降低計算量；（2）**壓縮激活（Squeeze-and-Excitation, SE）注意力機制**：對特徵圖的各通道重要性進行自適應加權，強化關鍵特徵的表達；（3）**Hard-Swish 激活函數**：以分段線性函數近似 Swish 激活，在效能損失極小的前提下大幅降低計算成本。

MobileNetV3-Large 的整體架構包含：初始卷積層（3$\times$3, stride 2）、15 個 Bottleneck 模組（其中部分含 SE 模組）、1$\times$1 卷積升維層、自適應平均池化層及分類頭。以 224$\times$224 像素輸入為例，模型參數量約 5.4M，計算量約 219 MFLOPs，在 ImageNet-1K 驗證集上的 Top-1 準確率達 75.2\%（ImageNet V2 權重可達 76.7\%），速度效能比優於 EfficientNet-B0 及 ResNet-50 等同等精度的模型。本研究採用 ImageNet V2 預訓練權重，可充分利用模型在 1.28M 張大規模影像上學習到的通用視覺特徵，顯著減少對標注資料量的依賴。

## 遷移學習與資料不平衡處理 {#sec:literature-transfer}

遷移學習（Transfer Learning）在電腦視覺領域的核心假設是：在大規模資料集（如 ImageNet）上預訓練的模型，已學習到豐富的底層視覺特徵（邊緣、紋理、形狀等），這些特徵可以遷移至目標任務，即使目標任務的資料量遠少於預訓練資料集。常用的遷移學習策略包括：（a）**特徵提取（Feature Extraction）**：凍結預訓練模型的全部或大部分層，僅訓練新增的任務特定層；（b）**微調（Fine-tuning）**：以較小的學習率對全部或部分層進行更新，使模型特徵更好地適應目標任務。

資料不平衡（Class Imbalance）的處理是本研究的重要技術課題之一。本研究同時採用三種互補的策略：（1）**WeightedRandomSampler**：在資料載入階段，對少數類別樣本以更高的機率抽取，確保每個批次中各等級樣本均有充分的學習機會；（2）**Focal Loss**：在損失函數層面對困難樣本（含少數類別）加重懲罰[@lin2017focal]；（3）**Mixup 資料增強**[@zhang2018mixup]：在批次層面對任意兩筆樣本進行線性混合，擴充訓練分布的多樣性，並正則化模型對邊界樣本的預測信心。三種策略從資料採樣、損失計算及資料擴充三個角度協同應對不平衡問題，效果優於單一策略。

# 研究方法 {#sec:method}

## 研究架構 {#sec:method-architecture}

本研究系統架構如圖 \ref{fig:method-flow} 所示，修訂後以資料流與責任分工為主軸呈現。整體流程由列印製樣與影像蒐集開始，經由裁切前處理與人工標注建立 A 至 F 六等級資料集，再以 MobileNetV3-Large 進行遷移學習訓練，最後輸出混淆矩陣、品質分數、批量分級資料夾與 HTML 統計報告。此種呈現方式可直接對應資料來源、模型訓練與推論輸出，避免原流程圖僅堆疊模組而未說明關係。硬體端仍由 Bambu Lab A1、拍攝設備與訓練電腦組成，如圖 \ref{fig:method-hardware} 所示。

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.95\textwidth,keepaspectratio]{images/image5.png}
\caption{修訂後研究流程與資料流關係圖}
\label{fig:method-flow}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.6\textwidth,keepaspectratio]{images/image6.jpeg}
\caption{系統硬體架構圖}
\label{fig:method-hardware}
\end{figure}

## 實驗設備 {#sec:method-equipment}

### 3D 列印設備規格 {#sec:method-equipment-printer}

本研究使用 Bambu Lab A1 桌上型 3D 印表機作為列印設備，該機型採用床式平台移動（Bed Slinger）機械結構，具備高精度列印能力與穩定性。Bambu Lab A1 的主要技術規格整理如表 \ref{tab:printer-spec} 所示。

\begin{table}[!htbp]
\centering
\caption{Bambu Lab A1 主要技術規格}
\label{tab:printer-spec}
\small
\begin{tabular}{ll}
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

本節原先逐張列出列印參數設定截圖，雖然完整，但會使正文被截圖切割，讀者反而難以掌握哪些參數真正影響資料集的一致性。因此修訂後將正文改為說明參數選擇理由，完整設定畫面移至附錄二保存，作為實驗重現時的查核來源。

本研究的列印參數控制重點可分為五類。**第一**，品質設定用於固定層高、線寬與外殼品質，使拉絲差異主要來自列印狀態而非幾何尺寸變動。**第二**，強度設定用於控制填充密度與壁厚，避免樣本因結構強度不足而產生非拉絲類破壞。**第三**，速度設定用於維持列印與移動速度的一致性，降低批次間因噴嘴移動條件不同造成的額外變異。**第四**，支撐設定在魚骨件列印中保持固定，避免支撐拆除痕跡被誤當成瑕疵特徵。**第五**，其他進階設定僅作為固定環境條件，不作為本研究主要變因。

正文保留上述原則即可支撐研究方法；若需逐項核對 Bambu Studio 設定畫面，可參考附錄二之完整截圖。這樣安排能同時保留實驗可重複性與正文閱讀性。

### 電腦硬體與軟體環境 {#sec:method-equipment-pc}

模型訓練所使用的電腦硬體與軟體規格如表 \ref{tab:pc-spec} 所示。本研究利用 NVIDIA RTX 3050 Laptop GPU 進行深度學習模型訓練，搭配 PyTorch 2.6.0+CUDA 12.4 環境，開啟 FP16 混合精度訓練以提升運算效率[@falcon2019lightning]。

\begin{table}[!htbp]
\centering
\caption{電腦硬體與軟體環境}
\label{tab:pc-spec}
\small
\begin{tabular}{ll}
\hline
\textbf{項目} & \textbf{規格} \\
\hline
處理器 & AMD Ryzen 7 4800H with Radeon Graphics 2.90 GHz \\
GPU & NVIDIA GeForce RTX 3050 Laptop（4 GB VRAM）\\
記憶體 & 32.0 GB DDR4 \\
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

資料蒐集採分批列印方式進行，主要紀錄集中於 2025/11/22 至 2025/12/10，並於 2026/02/05 至 2026/02/07 補充少數等級與失敗件樣本。每組原始照片可裁切出 6 支魚骨樣本，最後整理為 1110 筆有效資料。正文保留資料蒐集流程與代表性設計說明，完整列印過程照片改列於附錄一，避免主文被連續照片切斷。

此安排的重點是讓正文回答三個問題：為何選擇魚骨件、資料如何分批取得，以及照片如何轉換為可訓練資料。至於每一張列印過程照片的時間與狀態，屬於實驗紀錄與佐證資料，放在附錄一更適合查核與保存。

### 影像拍攝規範 {#sec:method-sample-capture}

影像拍攝採用固定距離、固定背景的標準化規範：拍攝設備為智慧型手機相機（解析度約 12 MP），鏡頭垂直俯拍列印床，拍攝距離固定於熱床正上方約 30 cm，室內自然光環境，避免陽光直射造成反光。背景為 Bambu Lab A1 原廠的黑色熱床表面，與各色 PLA 魚骨形成良好的明暗對比，有助於後續影像裁切與辨識。拍攝完成後，資料再依批次進行裁切、標注、模型訓練與辨識分析。各批次拍攝資料統計如表 \ref{tab:batch-stats} 所示。

\begin{table}[!htbp]
\centering
\caption{各批次拍攝資料統計}
\label{tab:batch-stats}
\small
\begin{tabular}{lllp{5cm}}
\hline
\textbf{批次} & \textbf{日期} & \textbf{張數} & \textbf{裁切後樣本數} \\
\hline
第 1 批 & 2025/11/22 & 3 & 18 \\
第 2 批 & 2025/11/25 & 20 & 120 \\
第 3 批 & 2025/11/26 & 14 & 84 \\
第 4 批 & 2025/12/04 & 17 & 102 \\
第 5 批 & 2025/12/06 & 51 & 306 \\
第 6 批 & 2025/12/08 & 30 & 180 \\
第 7 批 & 2025/12/09 & 30 & 180 \\
第 8 批 & 2025/12/10 & 20 & 120 \\
\hline
\textbf{合計} & --- & \textbf{185} & \textbf{1110} \\
\hline
\end{tabular}
\end{table}

## 影像前處理 {#sec:method-preprocessing}

### 魚骨自動裁切 {#sec:method-preprocessing-crop}

本研究依列印與拍攝完成後整理之實驗照片進行魚骨樣本裁切，並於 2026/02/10 前完成模型訓練與辨識分析，使用自行開發的 \texttt{crop\_fish.py} 腳本進行自動切割。裁切採用固定網格方式：將每張照片等分為 2 欄 $\times$ 3 列，各格切出一支魚骨，裁切後尺寸約 700$\times$900 pixels，保留足夠細節供後續辨識。為處理路徑含中文字元的問題，程式改用 PIL \texttt{Image.open()} 或 numpy \texttt{fromfile()}+cv2.\texttt{imdecode()} 組合讀取，確保跨平台相容性。最新整理後共取得 1110 張有效單支魚骨樣本。

以下圖 \ref{fig:crop-fish01} 至圖 \ref{fig:crop-fish03} 為裁切腳本輸出的魚骨裁切結果範例，可清楚看到每支魚骨被完整切割、背景一致，裁切品質良好。

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.6\textwidth,keepaspectratio]{images/image7.jpg}
\caption{魚骨裁切結果範例（fish01）}
\label{fig:crop-fish01}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.6\textwidth,keepaspectratio]{images/image8.jpg}
\caption{魚骨裁切結果範例（fish02）}
\label{fig:crop-fish02}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.6\textwidth,keepaspectratio]{images/image9.jpg}
\caption{魚骨裁切結果範例（fish03）}
\label{fig:crop-fish03}
\end{figure}

### 資料增強策略 {#sec:method-preprocessing-aug}

訓練階段對輸入影像施加表 \ref{tab:augmentation} 所列的多種隨機增強變換，以擴充有效訓練樣本多樣性，提升模型泛化能力；驗證與測試階段不施加增強，確保評估結果客觀。

\begin{table}[!htbp]
\centering
\caption{訓練資料增強方法彙整}
\label{tab:augmentation}
\small
\begin{tabular}{lll}
\hline
\textbf{增強方法} & \textbf{參數設定} & \textbf{目的說明} \\
\hline
Resize & 224$\times$224 px & 統一輸入尺寸以符合預訓練模型要求 \\
RandomHorizontalFlip & $p=0.5$ & 水平翻轉，增加方向多樣性 \\
RandomVerticalFlip & $p=0.3$ & 垂直翻轉 \\
RandomRotation & $\pm$30$^\circ$ & 應對拍攝角度偏差 \\
ColorJitter & 亮度 0.4、對比 0.4、飽和 0.3、色相 0.1 & 應對光線與色調變化 \\
RandomGrayscale & $p=0.05$ & 強化紋理特徵，減少顏色依賴 \\
RandomPerspective & distortion=0.2, $p=0.3$ & 應對拍攝視角偏差 \\
RandomErasing & $p=0.2$, scale=(0.02, 0.15) & 提升部分遮擋魯棒性 \\
Normalize & ImageNet mean/std & 對齊預訓練模型輸入分布 \\
Mixup（批次層級）& $\alpha=0.3$ & 線性混合兩筆樣本，提升邊界辨識能力 \\
\hline
\end{tabular}
\end{table}

## 品質等級定義 {#sec:method-grading}

本研究依拉絲瑕疵面積佔魚骨本體的比例，制定六個品質等級（A 至 F），如表 \ref{tab:grading-criteria} 所示。等級定義以客觀可量化的面積比例為主要依據，並配合各等級範例圖（圖 \ref{fig:grade-a} 至圖 \ref{fig:grade-f}），確保標注一致性。

\begin{table}[!htbp]
\centering
\caption{六等級品質定義}
\label{tab:grading-criteria}
\small
\begin{tabular}{cllcl}
\hline
\textbf{等級} & \textbf{名稱} & \textbf{拉絲面積判斷標準} & \textbf{目標分數} & \textbf{應用建議} \\
\hline
A & 完美品 & 完全無拉絲細絲，表面乾淨 & 100 分 & 可直接使用 \\
B & 良好品 & 極少量細絲，1$\sim$2 根短絲，面積可忽略 & 80 分 & 一般用途可接受 \\
C & 輕微拉絲 & 少量細絲，拉絲面積 $<$ 魚身 1/4 & 60 分 & 外觀要求低時可接受 \\
D & 中度拉絲 & 明顯細絲，拉絲面積佔魚身 1/4$\sim$1/2 & 40 分 & 需重新列印或後處理 \\
E & 嚴重拉絲 & 大量細絲，拉絲面積 $>$ 魚身 1/2 & 20 分 & 品質不合格 \\
F & 失敗品 & 極度拉絲，幾乎看不出魚骨結構 & 0 分 & 廢品 \\
\hline
\end{tabular}
\end{table}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image10.jpg}
\caption{A 等級（完美品）：完全無細絲，表面乾淨}
\label{fig:grade-a}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image11.jpg}
\caption{B 等級（良好品）：極少量細絲，1$\sim$2 根短絲}
\label{fig:grade-b}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image12.jpg}
\caption{C 等級（輕微拉絲）：拉絲面積小於魚身四分之一}
\label{fig:grade-c}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image13.jpg}
\caption{D 等級（中度拉絲）：拉絲面積約佔魚身四分之一至二分之一}
\label{fig:grade-d}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image14.jpg}
\caption{E 等級（嚴重拉絲）：拉絲面積大於魚身二分之一}
\label{fig:grade-e}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image15.jpg}
\caption{F 等級（失敗品）：結構幾乎難以辨識}
\label{fig:grade-f}
\end{figure}

### 各等級邊界判斷邏輯 {#sec:method-grading-boundary}

前一節已以圖 \ref{fig:grade-a} 至圖 \ref{fig:grade-f} 呈現 A 至 F 六等級的代表性樣本，因此本節修訂後不再逐張堆疊所有樣本，而改為補充各等級的邊界判斷邏輯。這種寫法能保留標注依據，也能避免正文被大量相似圖片中斷。

**A 與 B 等級的差異**在於是否可見極少量短細絲。A 級要求表面乾淨且無明顯拉絲；B 級雖仍可接受，但可能在魚骨細刺或局部轉角處出現少量短絲。這兩級容易混淆的原因，是短絲在拍攝角度與光線變化下可能被弱化或放大，因此標注時必須以整體面積與可見程度共同判斷。

**C 與 D 等級的差異**在於拉絲面積是否跨越局部區域並形成連續分布。C 級通常仍屬輕微拉絲，魚骨主體結構清楚；D 級則已出現較大範圍的絲狀殘留，可能遮蔽部分魚骨間隙。這是本研究模型較容易出現邊界誤判的區間，原因在於兩者都保留可辨識的主體輪廓，但拉絲覆蓋比例不同。

**E 與 F 等級**則代表嚴重瑕疵與失敗件。E 級仍可辨識魚骨結構，但拉絲覆蓋比例已明顯偏高；F 級則接近列印失敗或結構難以辨識。由於 F 級樣本數僅 32 張，未來仍需補充更多失敗件，以提升模型對極端瑕疵的泛化能力。

## 資料標注流程 {#sec:method-labeling}

本研究使用 Label Studio（開源標注平台）[@labelstudio]完成全部裁切圖的人工標注。標注流程為：

1. 將裁切圖匯入 Label Studio 專案。
2. A 等級直接 Submit 不畫框。
3. 有拉絲的樣本，以邊界框框住拉絲區域，並從下拉選單選擇對應嚴重程度標籤。
4. 完成後從 Label Studio 匯出 CSV。
5. 執行 \texttt{parse\_labelstudio.py} 解析 CSV，將各樣本複製至對應等級資料夾 \texttt{data/raw/A\textasciitilde F/}。

最新標注完成後，A 級 546 張、B 級 87 張、C 級 213 張、D 級 160 張、E 級 72 張、F 級 32 張，共 1110 張有效資料。

## 模型架構與訓練設計 {#sec:method-model}

### 模型架構 {#sec:method-model-arch}

本研究採用 MobileNetV3-Large[@howard2019mobilenetv3]（ImageNet V2 預訓練）作為骨幹網路，以遷移學習方式進行六分類微調。模型修改如下：將分類頭最後一個全連接層（原 1000 類輸出）替換為含 Dropout（$p=0.4$）的六分類線性層；同時在 pooling 後的特徵向量上接品質評分輔助頭（Dropout($p=0.2$)$\to$Linear$\to$ReLU$\to$Linear$\to$Sigmoid），輸出 0 至 1 的連續品質分（$\times$100 即 0 至 100 分）。訓練時分類頭與評分頭同步優化，損失函數為 Focal Loss[@lin2017focal]與 MSE Loss 的加權組合：

\begin{equation}
L = L_{\text{Focal}} + 0.3 \times L_{\text{MSE}}
\label{eq:total-loss}
\end{equation}

模型訓練超參數設定整理於表 \ref{tab:hyperparameters}。

\begin{table}[!htbp]
\centering
\caption{模型訓練超參數設定}
\label{tab:hyperparameters}
\small
\begin{tabular}{lll}
\hline
\textbf{超參數} & \textbf{設定值} & \textbf{說明} \\
\hline
骨幹模型 & MobileNetV3-Large (ImageNet V2) & 預訓練權重 \\
輸入尺寸 & 224$\times$224 px & --- \\
批次大小 & 32 & GPU 記憶體限制 \\
最大輪數 & 100 輪 & 含 EarlyStopping \\
EarlyStopping Patience & 35 輪 & 監控 val/acc \\
學習率 & $2\times10^{-4}$ & AdamW 初始值 \\
Weight Decay & $3\times10^{-4}$ & --- \\
學習率排程 & CosineAnnealingWarmRestarts & $T_0=20$, $T_{\text{mult}}=2$, $\eta_{\min}=10^{-6}$ \\
Dropout & 分類頭 $p=0.4$；評分頭 $p=0.2$ & 依 \texttt{train\_and\_report.py} 設定 \\
Label Smoothing & 0.1 & 於 Focal Loss 中 \\
Mixup Alpha & 0.3 & 批次層級 \\
Focal Loss $\gamma$ & 2.0 & --- \\
過採樣 & WeightedRandomSampler（0.75 次方反比）& --- \\
訓練精度 & FP16 Mixed Precision & GPU 加速 \\
\hline
\end{tabular}
\end{table}

# 實驗結果與分析 {#sec:results}

## 資料集統計分析 {#sec:results-dataset}

本研究最新有效樣本共 1110 張，依品質等級分布如表 \ref{tab:dataset-dist} 及圖 \ref{fig:dataset-dist} 所示。A 等級（完美品）佔比最高，共 546 張；B 級 87 張、C 級 213 張、D 級 160 張、E 級 72 張、F 級 32 張。相較早期 214 張嚴重不平衡資料，最新資料集已顯著補足 B、C、D、E、F 等瑕疵等級，使模型能學習較完整的輕微至嚴重拉絲特徵。

\begin{table}[!htbp]
\centering
\caption{訓練資料集各等級分布}
\label{tab:dataset-dist}
\small
\begin{tabular}{cllrp{4.5cm}}
\hline
\textbf{等級} & \textbf{名稱} & \textbf{張數} & \textbf{佔比(\%)} & \textbf{資料集內比例} \\
\hline
A & 完美品 & 546 & 49.2\% & 樣本數最多，作為正常列印品質基準 \\
B & 良好品 & 87 & 7.8\% & 輕微邊界樣本 \\
C & 輕微拉絲 & 213 & 19.2\% & 拉絲開始明顯的主要過渡類別 \\
D & 中度拉絲 & 160 & 14.4\% & 中度瑕疵樣本已補足 \\
E & 嚴重拉絲 & 72 & 6.5\% & 嚴重瑕疵樣本 \\
F & 失敗品 & 32 & 2.9\% & 樣本基數最小，仍建議持續補充 \\
\hline
\textbf{合計} & --- & \textbf{1110} & \textbf{100\%} & 最新有效資料集 \\
\hline
\end{tabular}
\end{table}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.95\textwidth,keepaspectratio]{images/image16.png}
\caption{資料集各等級樣本分布（左：張數，右：佔比圓餅圖）}
\label{fig:dataset-dist}
\end{figure}

## TensorBoard 訓練過程監控 {#sec:results-tensorboard}

本研究以 TensorBoard 記錄訓練、驗證與測試過程，但正文不再逐張放置所有監控畫面，而改以關鍵數據與趨勢說明呈現。完整截圖可作為實驗查核資料保存，不必全部置於正文。

version\_21 模型最高驗證準確率為 90.96\%，獨立測試集準確率為 83.23\%，全資料集回測準確率為 95.86\%（1064/1110）。其中，全資料集回測用於確認模型對已標注資料的整體擬合與批量辨識能力；獨立測試集準確率則用於觀察模型在未參與訓練樣本上的泛化表現。兩者目的不同，不能混為同一個效能指標。

訓練階段使用 Mixup 資料增強，因此 \texttt{train/acc} 會在混合樣本與軟標籤條件下計算，不能直接與未混合的 \texttt{val/acc} 作等值比較。本研究以驗證集、測試集與全資料集回測三種角度交叉檢視模型表現，避免只依單一曲線判斷模型好壞。

### 訓練曲線趨勢說明 {#sec:results-tensorboard-trend}

訓練曲線的重點不是截圖數量，而是收斂趨勢與泛化落差。從紀錄可知，模型在訓練後期仍維持約 89\% 至 91\% 的驗證表現，顯示資料擴充與正則化策略對少數類別辨識有幫助。然而 \texttt{train/acc} 偏低並不代表模型未學習，因為 Mixup 會使訓練標籤成為軟標籤，準確率指標本身會被混合比例影響。

因此，本研究後續分析以混淆矩陣、各等級召回率、測試集準確率與全資料集回測結果作為主要依據。TensorBoard 截圖僅作為實驗紀錄來源，不再於正文逐張展示。

## 舊版模型評估（MobileNetV3-Small，214 張不平衡資料）{#sec:results-old-model}

在完成全部樣本的重新標注前，本研究先以初版 MobileNetV3-Small 模型對早期的 214 張嚴重不平衡資料（A=181 張，B$\sim$F 各 4$\sim$9 張）進行訓練，作為基準對照（Baseline）。初版模型的整體準確率雖達 86.9\%，但此數字主要是由 A 等級（約 85\% 佔比）貢獻，D 等級的 Precision 僅 0.304，說明模型幾乎只會預測 A 等級，對 B 至 F 等級的辨識能力極為有限，整體 Macro F1 僅 0.708。詳細評估結果如表 \ref{tab:old-model} 所示。

\begin{table}[!htbp]
\centering
\caption{舊版模型（MobileNetV3-Small，214 張）評估結果}
\label{tab:old-model}
\small
\begin{tabular}{lcccc}
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

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image17.png}
\caption{舊版模型混淆矩陣（A$\to$D 誤判 16 張為主要問題）}
\label{fig:old-confusion}
\end{figure}

由圖 \ref{fig:old-confusion} 可看出，舊版混淆矩陣中 A 等級有 16 張（8.8\%）被誤判為 D 等級，是最主要的錯誤來源。分析其根本原因：D 等級的訓練樣本僅 9 張，模型無法從如此有限的樣本中學習到 D 等級的穩定特徵表示，導致模型將 D 等級的高置信度預測閾值設定得極低，許多 A 等級樣本因特徵向量與 D 等級過度重疊而被誤分。此外，B 等級（5 張）和 C 等級（4 張）的樣本數同樣嚴重不足，其 F1-score 分別僅 0.615 和 0.667。這些結果明確說明：在嚴重資料不平衡的條件下，即使採用 WeightedRandomSampler 等過採樣技術，若少數類別的樣本數低於臨界值（本研究估計約 20$\sim$30 張），模型效能仍無法有效提升，補充實際樣本才是根本解決之道。

## 改良版模型評估（MobileNetV3-Large，1110 張最新資料）{#sec:results-new-model}

完成最新 1110 張有效樣本的重新整理並採用升級的 MobileNetV3-Large 模型後，全資料集回測整體準確率提升至 95.86\%（1064/1110），相較舊版 MobileNetV3-Small 的 86.9\% 提升約 9.0 個百分點。各等級全資料集辨識正確率分別為 A 級 98.7\%、B 級 92.0\%、C 級 96.7\%、D 級 90.6\%、E 級 88.9\%、F 級 93.8\%，其中 C 級與 D 級較前版有明顯改善。此處全資料集結果用於檢視模型對已標注資料的整體擬合與批量辨識能力，獨立測試集結果另以 \texttt{test/accuracy} 呈現。詳細評估結果如表 \ref{tab:new-model} 所示。

\begin{table}[!htbp]
\centering
\caption{最新模型（MobileNetV3-Large，1110 張）各等級評估結果}
\label{tab:new-model}
\small
\begin{tabular}{lcccccc}
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
\textbf{整體} & \textbf{1110} & \textbf{1064} & \textbf{95.86\%} & 66.0 分（weighted）& --- & --- \\
\hline
\end{tabular}
\end{table}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.95\textwidth,keepaspectratio]{images/image18.png}
\caption{改良版模型各等級準確率（左）及新舊版對比（右）}
\label{fig:new-model-acc}
\end{figure}

### 評估結果整體討論 {#sec:results-new-model-discussion}

本節原先放置分類報告、混淆矩陣與多張 TensorBoard 測試截圖。修訂後正文改以表 \ref{tab:new-model}、圖 \ref{fig:new-model-acc} 與下一節混淆矩陣分析作為主要證據，避免相同資訊重複出現。完整輸出仍保留於實驗資料夾與 TensorBoard/HTML 報告中，可供後續查核。

從評估結果看，改良版 MobileNetV3-Large 在全資料集回測中達 95.86\%，但獨立測試集為 83.23\%。這個落差表示模型已能有效擬合目前資料集，但在少數等級與邊界樣本上仍有泛化限制。因此，本研究不將 95.86\% 解讀為實際部署時的保證準確率，而是將其定位為目前標注資料上的回測表現。

## 混淆矩陣深度分析 {#sec:results-confusion}

以下以最新模型混淆矩陣作為主要分析依據，說明各品質等級的辨識穩定性與主要混淆來源。

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image19.png}
\caption{最新模型混淆矩陣（1110 張）}
\label{fig:new-confusion}
\end{figure}

由圖 \ref{fig:new-confusion} 之最新 version\_21 評估結果可觀察到以下趨勢：

1. A 等級共 546 張，準確率 98.7\%，完美品辨識最穩定。
2. B 等級共 87 張，準確率 92.0\%，與 A/C 邊界仍為主要混淆來源。
3. C 等級共 213 張，準確率 96.7\%，已具備穩定辨識能力。
4. D 等級共 160 張，準確率 90.6\%，較前版 77.8\% 明顯改善。
5. E 等級共 72 張，準確率 88.9\%。
6. F 等級共 32 張，準確率 93.8\%，但樣本數仍偏少，未來仍建議持續補充嚴重失敗樣本。

### 誤判案例類型分析 {#sec:results-confusion-error}

誤判案例修訂後改以類型分析為主，而非逐張排列。主要錯誤可分為三類。

**第一**，A 級與 B 級之間的混淆，多發生在魚骨細刺附近有極短細絲時；模型可能將光線、陰影或短絲解讀為輕微瑕疵。

**第二**，C 級與 D 級之間的混淆，主要來自拉絲面積比例接近臨界值，尤其當拉絲集中於局部區域時，模型對整體嚴重程度的判定會產生偏差。

**第三**，E 級與 F 級之間的混淆，與嚴重失敗樣本數不足有關，模型較難穩定學習結構崩壞與嚴重拉絲的邊界。

這些誤判顯示，本研究的主要瓶頸不只在模型架構，也在標注準則與邊界樣本數量。後續若要提升 B/C、C/D 與 E/F 邊界辨識能力，應優先補充邊界樣本，並建立更明確的複核規則，而不是單純增加訓練輪數。

### 正確辨識案例特徵歸納 {#sec:results-confusion-correct}

正確辨識案例的功能是說明模型在典型樣本上的判斷能力。修訂後不再逐張展示所有正確案例，而改以文字歸納：A 級樣本通常具有乾淨輪廓與清楚魚骨間隙；B 級樣本可能存在少量短絲但不影響整體品質；C 與 D 級樣本的差異主要在拉絲覆蓋比例與連續性；E 與 F 級樣本則呈現大範圍拉絲或結構難以辨識。

從正確案例可看出，模型對典型 A、C、D 與 F 級具有較明確的特徵反應；較不穩定的區域仍集中在相鄰等級的邊界樣本。這與前述混淆矩陣分析一致，也支持後續以邊界樣本補充與標注一致性檢查作為改善方向。

## 品質評分系統分析 {#sec:results-quality-score}

品質評分輔助頭的輸出如表 \ref{tab:new-model} 所示。表 \ref{tab:grading-criteria} 中的目標分數為人工定義之等級基準，表 \ref{tab:new-model} 則為模型回歸頭輸出的預測平均分，兩者尚未經校準，因此數值不必完全相同。最新全資料集平均品質分為 66.0 分；各等級平均分依 A 至 F 呈現遞減趨勢，分別為 A 級 79.4 分、B 級 69.7 分、C 級 57.5 分、D 級 49.8 分、E 級 37.4 分、F 級 28.5 分。預測平均分可作為比六等級分類更細緻的品質量化工具，例如以品質分 65 分為門檻，低於此值的列印件建議重新列印或進行後處理。比較結果如圖 \ref{fig:quality-score} 所示。

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.85\textwidth,keepaspectratio]{images/image20.png}
\caption{各等級目標品質分與模型輸出平均分比較}
\label{fig:quality-score}
\end{figure}

## 批量辨識系統實測 {#sec:results-batch}

將訓練完成的最佳模型整合至批量辨識腳本，對最新 1110 支魚骨樣本進行自動辨識，結果如表 \ref{tab:batch-result} 及圖 \ref{fig:batch-result} 所示。系統自動將辨識結果依等級分類存入 \texttt{results/graded/A\textasciitilde F/}，並在每張裁切圖右上角標示等級，同時產生統計圖。最新批量辨識輸出分布為 A 級 544 張、B 級 89 張、C 級 216 張、D 級 156 張、E 級 71 張、F 級 34 張。

\begin{table}[!htbp]
\centering
\caption{批量辨識 1110 支魚骨結果統計}
\label{tab:batch-result}
\small
\begin{tabular}{cllrp{4.5cm}}
\hline
\textbf{等級} & \textbf{名稱} & \textbf{辨識支數} & \textbf{佔比(\%)} & \textbf{說明} \\
\hline
A & 完美品 & 544 & 49.0\% & 多數列印件品質良好 \\
B & 良好品 & 89 & 8.0\% & A/B 邊界樣本略有混淆 \\
C & 輕微拉絲 & 216 & 19.5\% & 輕微瑕疵主要輸出類別 \\
D & 中度拉絲 & 156 & 14.1\% & 中度拉絲樣本穩定辨識 \\
E & 嚴重拉絲 & 71 & 6.4\% & 嚴重瑕疵樣本 \\
F & 失敗品 & 34 & 3.1\% & 失敗品樣本數較少 \\
\hline
\textbf{合計} & --- & \textbf{1110} & \textbf{100\%} & 最新批量辨識結果 \\
\hline
\end{tabular}
\end{table}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image21.png}
\caption{批量辨識各等級支數分布統計圖}
\label{fig:batch-result}
\end{figure}

### 端對端辨識流程的實際意義 {#sec:results-batch-pipeline}

批量辨識結果範例修訂後不再逐張排列各等級輸出圖，而改為說明端對端流程的實際意義。系統會將 1110 支魚骨樣本依模型預測結果分入 A 至 F 資料夾，並產生統計圖與 HTML 報告。這個流程的價值在於快速提供批次品質概況，讓使用者先掌握異常等級分布，再針對低品質或邊界樣本進行人工複核。

最新批量輸出分布為 A 級 544 張、B 級 89 張、C 級 216 張、D 級 156 張、E 級 71 張、F 級 34 張。此分布與人工標注資料集的整體趨勢相近，表示系統可作為初步分級工具；但由於 C/E 等級與資料夾現況曾出現 1 張差異，本研究仍以 TensorBoard/HTML 輸出作為正式表格來源，並建議未來在批量輸出後加入版本化紀錄與自動檢查表。

## 新舊版模型綜合比較 {#sec:results-comparison}

本研究於資料蒐集、標注與模型調整過程中進行多次訓練。為呈現模型效能隨資料量與訓練版本演進的變化，整理具完整全資料集評估紀錄之代表版本如表 \ref{tab:multi-versions} 所示；未完成或重複輸出的版本未列入比較。

\begin{table}[!htbp]
\centering
\caption{多次訓練結果比較}
\label{tab:multi-versions}
\small
\begin{tabular}{llcccp{4.8cm}}
\hline
\textbf{版本} & \textbf{資料量} & \textbf{全資料準確率} & \textbf{測試準確率} & \textbf{驗證最高} & \textbf{說明} \\
\hline
version\_4 & 214 & 98.60\% & 93.94\% & 96.88\% & 早期二元分類器訓練紀錄（非六分類），資料量小，結果易受資料切分影響 \\
version\_5 & 214 & 86.9\% & 78.79\% & 84.38\% & 舊版基準結果，對應初期 214 張資料階段 \\
version\_9 & 624 & 89.90\% & 79.79\% & 80.85\% & 資料擴充至 624 張後的早期訓練結果 \\
version\_10 & 624 & 93.75\% & 82.98\% & 84.04\% & 624 張資料階段，整體準確率明顯提升 \\
version\_11 & 624 & 94.39\% & 86.17\% & 82.98\% & 624 張資料階段最佳完整紀錄之一 \\
version\_13 & 984 & 92.38\% & 82.43\% & 72.97\% & 984 張資料初期訓練，驗證表現仍不穩定 \\
version\_17 & 984 & 95.02\% & 87.16\% & 87.84\% & 984 張資料階段最佳紀錄 \\
version\_18 & 1110 & 92.07\% & 87.16\% & 87.84\% & 資料擴充至 1110 張後的過渡版本 \\
version\_19 & 1110 & 91.44\% & 82.63\% & 86.14\% & 1110 張資料階段中期訓練紀錄 \\
version\_21 & 1110 & 95.86\% & 83.23\% & 90.96\% & 目前最新版本，全資料集準確率最高 \\
\hline
\end{tabular}
\end{table}

由表 \ref{tab:multi-versions} 可知，資料集由 214 張逐步擴充至 1110 張後，模型在不同版本間呈現整體改善趨勢。早期 version\_4 雖有較高數值，但屬二元分類器（非六分類）階段，資料量僅 214 張，結果易受切分方式與樣本分布影響，不宜與最新完整資料集直接等量比較；在 1110 張資料版本中，version\_21 的全資料集回測準確率 95.86\% 為最高，最高驗證準確率亦提升至 90.96\%。雖然測試集準確率仍會受少數類別樣本數影響而波動，但資料補充與訓練策略調整對模型穩定性具有正面效果。

\begin{table}[!htbp]
\centering
\caption{新舊版模型綜合比較}
\label{tab:model-comparison}
\small
\begin{tabular}{lp{5cm}p{6cm}}
\hline
\textbf{比較項目} & \textbf{舊版（MobileNetV3-Small）} & \textbf{改良版（MobileNetV3-Large）} \\
\hline
訓練樣本 & 214 張（嚴重不平衡）& 1110 張（重新標注）\\
模型架構 & MobileNetV3-Small & MobileNetV3-Large（ImageNet V2）\\
損失函數 & CrossEntropy & Focal Loss（$\gamma=2.0$）+Label Smoothing（0.1）+MSE \\
資料增強 & 基礎翻轉旋轉 & 全套增強+Mixup（$\alpha=0.3$）\\
過採樣 & WeightedRandomSampler & WeightedRandomSampler（0.75 次方反比）\\
整體準確率 & 86.9\%（186/214）& 95.86\%（1064/1110）\\
D 等級 Recall & 77.8\%（Precision 僅 30.4\%）& 90.6\%（145/160）\\
Macro F1（估算）& 0.708 & 約 0.94 \\
主要問題 & A$\to$D 誤判 16 張 & B/D/E 邊界仍需補充樣本 \\
\hline
\end{tabular}
\end{table}

# 結論與建議 {#sec:conclusion}

## 結論 {#sec:conclusion-summary}

本研究成功建立了一套以深度學習影像辨識為核心的 3D 列印件瑕疵自動辨識與品質評分系統，以 FDM 列印魚骨件的拉絲瑕疵為研究標的，實現六等級（A 至 F）自動分類與品質評分輸出。主要研究成果總結如下：

1. **標準化品質等級制度**：以拉絲面積佔比為客觀量化依據，建立了六個明確、可重複的品質等級定義，並配合 A 至 F 六張範例圖，確保不同標注人員間的一致性，有效解決了傳統目視檢測主觀性強的核心問題。
2. **系統性資料蒐集與標注**：透過多批次列印與拍攝，配合 Label Studio 工具完成全部樣本的精確人工標注，建立含 1110 張有效樣本的六等級分類資料集。本研究的實踐驗證了高品質標注資料對深度學習效能的根本性影響：從 214 張嚴重不平衡的舊資料逐步擴充至 1110 張重新標注資料後，全資料集整體準確率提升至 95.86\%。
3. **高效能深度學習模型**：採用 MobileNetV3-Large（ImageNet V2 預訓練）進行遷移學習，結合 Focal Loss、Label Smoothing、Mixup、WeightedRandomSampler 等多項訓練優化策略，在有限樣本量的條件下達到全資料集整體準確率 95.86\% 的高效能，其中 A、B、C、D、E、F 六個等級全資料集 Recall 均達 88\% 以上，顯示本系統具備品質管控輔助原型可行性，但 B、D、E 等邊界或少數類別仍需持續補充資料以提升泛化能力。
4. **端對端自動化系統**：整合自動裁切（\texttt{crop\_fish.py}）、批量辨識（\texttt{辨識資料夾.py}）、分級輸出及 HTML 可視化報告等功能，形成由原始照片輸入到品質等級報告輸出的離線批量處理流程。本研究未保留獨立硬體計時紀錄，因此不將單張推論時間作為正式效能指標；系統定位為品質管控輔助原型，後續仍需在固定硬體與批次條件下補做推論時間、吞吐量與人工複核成本評估。
5. **品質評分量化**：模型同時輸出 0 至 100 的連續品質分數。以 A=100、B=80、C=60、D=40、E=20、F=0 作為目標分數時，各等級預測平均分與目標分數的絕對誤差分別為 A 級 20.6 分、B 級 10.3 分、C 級 2.5 分、D 級 9.8 分、E 級 17.4 分、F 級 28.5 分。此結果顯示品質分已呈現由 A 至 F 遞減的趨勢，但 A、B、E、F 等級仍需進一步校準，才能作為更精準的品質量化依據。

## 建議 {#sec:conclusion-future}

根據本研究執行過程中的觀察與系統評估結果，提出以下五點建議供後續研究參考：

1. **持續補充少數等級訓練資料**。雖然最新資料集中 D 級已達 160 張、E 級 72 張，但 F 級仍僅 32 張，且 B 級 87 張相較 A 級仍偏少，未來建議優先補充 B 級邊界樣本與 F 級失敗樣本，並將 F 等級資料補充至 50 張以上，使各等級樣本分布更平均，進一步降低 B/C 與 E/F 邊界的誤判，提高結果的統計可信度。
2. **擴充至翹曲與裂痕瑕疵的辨識**。本研究因翹曲和裂痕的現有樣本不足，聚焦於拉絲瑕疵的六等級分類。未來可系統性地蒐集翹曲及裂痕樣本，建立涵蓋三種瑕疵類型的多標籤分類系統（Multi-label Classification），更全面地反映 FDM 列印件的品質狀態，提升系統的應用廣度。
3. **開發即時列印監控系統**。目前系統為列印完成後的離線批量辨識模式，未來可整合 Bambu Lab A1 的內建攝影機或外接 USB 相機串流，在列印進行中進行即時逐層品質監控，一旦偵測到嚴重拉絲（D 等級以上）即觸發警告並自動暫停列印，實現真正的閉環品質管控。
4. **優化品質評分模型的準確性**。目前品質分採用等級編號的線性轉換作為監督目標，較為粗糙。未來可邀請 5 至 10 名有經驗的操作人員對全部樣本進行主觀評分（連續值 0 至 100），以人工評分作為監督標籤，採用迴歸方式訓練更精確的評分頭，並計算模型輸出分數與人工評分的 ICC（組內相關係數）作為系統可信度的量化指標。
5. **模型輕量化與邊緣部署**。MobileNetV3-Large 模型大小約 21 MB，適合部署於桌上型電腦或工業電腦。若未來需部署於計算資源有限的邊緣裝置（如 Raspberry Pi 或 NVIDIA Jetson 系列），可進一步評估知識蒸餾、模型剪枝或 INT8 量化等壓縮方法；但任何壓縮方案都必須在相同資料切分下重新測試混淆矩陣、各等級召回率、品質分校準與推論時間，不能僅依模型大小推論精度與速度。

<!-- ============================================================ -->
<!-- 參考文獻（Pandoc + biblatex 自動產生） -->
<!-- ============================================================ -->

\newpage
\nocite{*}
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

# 列印過程照片完整紀錄 {#sec:appendix-photos}

以下為本研究資料蒐集期間的完整紀錄：列印過程照片主要紀錄於 2025/11/22 至 2025/12/10。附圖中之拍攝時間依原始圖檔日期與整理後圖說呈現。

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image22.jpg}
\caption{拍攝時間：2025/11/22 灰色魚骨列印中，結構完整}
\label{fig:photo-01}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image23.jpg}
\caption{拍攝時間：2025/11/25 灰色魚骨列印完成，輕微翹曲}
\label{fig:photo-02}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image24.jpg}
\caption{拍攝時間：2025/11/25 參數測試件列印中，暗光}
\label{fig:photo-03}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image25.jpg}
\caption{拍攝時間：2025/11/26 空列印床，列印結束後}
\label{fig:photo-04}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image26.jpg}
\caption{拍攝時間：2025/11/26 藍綠色魚骨列印完成，整齊}
\label{fig:photo-05}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image27.jpg}
\caption{拍攝時間：2025/12/04 魚骨列印中，曝光不足}
\label{fig:photo-06}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image28.jpg}
\caption{拍攝時間：2025/12/06 藍色魚骨列印中，正常}
\label{fig:photo-07}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image29.jpg}
\caption{拍攝時間：2025/12/06 藍色魚骨列印完成，稍暗}
\label{fig:photo-08}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image30.jpg}
\caption{拍攝時間：2025/12/06 藍色魚骨列印完成，整齊}
\label{fig:photo-09}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image31.jpg}
\caption{拍攝時間：2025/12/06 藍色魚骨列印中，輕微拉絲}
\label{fig:photo-10}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image32.jpg}
\caption{拍攝時間：2025/12/08 藍色魚骨列印中，過曝}
\label{fig:photo-11}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image33.jpg}
\caption{拍攝時間：2025/12/09 藍綠魚骨列印中，少量拉絲}
\label{fig:photo-12}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image34.jpg}
\caption{拍攝時間：2025/12/09 藍色魚骨嚴重拉絲}
\label{fig:photo-13}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image35.jpg}
\caption{拍攝時間：2025/12/10 藍色魚骨列印中，輕微拉絲}
\label{fig:photo-14}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image36.jpg}
\caption{拍攝時間：2025/12/10 黃綠色魚骨嚴重拉絲，列印失敗}
\label{fig:photo-15}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image37.jpg}
\caption{空列印床狀態}
\label{fig:photo-16}
\end{figure}

# Bambu Lab A1 完整列印參數設定 {#sec:appendix-params}

以下為 Bambu Lab A1 印表機於本研究列印實驗中所使用的完整參數設定截圖，涵蓋品質、強度、速度、支撐及其他進階選項，作為實驗重現的完整參數紀錄。

## 品質（層高、線寬）設定 {#sec:appendix-params-quality}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.85\textwidth,keepaspectratio]{images/image38.PNG}
\caption{質量 1 設定畫面}
\label{fig:param-q1}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image39.PNG}
\caption{質量 2 設定畫面}
\label{fig:param-q2}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image40.PNG}
\caption{質量 3 設定畫面}
\label{fig:param-q3}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image41.PNG}
\caption{質量 4 設定畫面}
\label{fig:param-q4}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image42.PNG}
\caption{質量 5 設定畫面}
\label{fig:param-q5}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image43.PNG}
\caption{質量 6 設定畫面}
\label{fig:param-q6}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image44.PNG}
\caption{質量 7 設定畫面}
\label{fig:param-q7}
\end{figure}

## 強度（填充、壁厚）設定 {#sec:appendix-params-strength}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image45.PNG}
\caption{強度 1 設定畫面}
\label{fig:param-s1}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image46.PNG}
\caption{強度 2 設定畫面}
\label{fig:param-s2}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image47.PNG}
\caption{強度 3 設定畫面}
\label{fig:param-s3}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image48.PNG}
\caption{強度 4 設定畫面}
\label{fig:param-s4}
\end{figure}

## 速度（列印、移位）設定 {#sec:appendix-params-speed}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image49.PNG}
\caption{速度 1 設定畫面}
\label{fig:param-v1}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image50.PNG}
\caption{速度 2 設定畫面}
\label{fig:param-v2}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image51.PNG}
\caption{速度 3 設定畫面}
\label{fig:param-v3}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image52.PNG}
\caption{速度 4 設定畫面}
\label{fig:param-v4}
\end{figure}

## 支撐結構設定 {#sec:appendix-params-support}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image53.PNG}
\caption{支撐 1 設定畫面}
\label{fig:param-sp1}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image54.PNG}
\caption{支撐 2 設定畫面}
\label{fig:param-sp2}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image55.PNG}
\caption{支撐 3 設定畫面}
\label{fig:param-sp3}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image56.PNG}
\caption{支撐 4 設定畫面}
\label{fig:param-sp4}
\end{figure}

## 其他進階設定 {#sec:appendix-params-other}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image57.PNG}
\caption{其他 1 設定畫面}
\label{fig:param-o1}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image58.PNG}
\caption{其他 2 設定畫面}
\label{fig:param-o2}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image59.PNG}
\caption{其他 3 設定畫面}
\label{fig:param-o3}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image60.PNG}
\caption{其他 4 設定畫面}
\label{fig:param-o4}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\textwidth,keepaspectratio]{images/image61.PNG}
\caption{其他 5 設定畫面}
\label{fig:param-o5}
\end{figure}

# PLA 耗材及冷卻設定截圖 {#sec:appendix-material}

以下為本研究使用 PLA 耗材的相關設定截圖，包含耗材絲徑、溫度曲線及冷卻模式設定，作為列印材料條件的完整紀錄。

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.85\textwidth,keepaspectratio]{images/image62.PNG}
\caption{冷卻模式 1 設定畫面}
\label{fig:cooling-1}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.85\textwidth,keepaspectratio]{images/image63.PNG}
\caption{冷卻模式 2 設定畫面}
\label{fig:cooling-2}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.85\textwidth,keepaspectratio]{images/image64.PNG}
\caption{耗材絲 1 設定畫面}
\label{fig:filament-1}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.85\textwidth,keepaspectratio]{images/image65.PNG}
\caption{耗材絲 2 設定畫面}
\label{fig:filament-2}
\end{figure}

\begin{figure}[!htbp]
\centering
\includegraphics[width=0.85\textwidth,keepaspectratio]{images/image66.PNG}
\caption{耗材絲 3 設定畫面}
\label{fig:filament-3}
\end{figure}
