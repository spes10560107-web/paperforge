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

熔融沉積成型（FDM）為目前桌上型 3D 列印之主流製程，其列印品質受噴嘴溫度、回抽距離、列印速度等多項參數交互影響，容易產生拉絲（Stringing）、翹曲與裂痕等瑕疵。傳統人工目視檢查費時且判定標準因人而異，難以維持品質一致性，因此自動化瑕疵辨識成為品質管控之關鍵需求。

本研究以魚骨形狀 PLA 列印件為對象，建立涵蓋 A 至 F 共六等級拉絲嚴重程度之影像分類資料集（共 1110 張、185 個原圖群組，單一標注者完成），採用 MobileNetV3-Large 為骨幹進行遷移學習，並以 ResNet18、EfficientNet-B0 為對照基準。為避免同源樣本造成評估過度樂觀，本研究採原圖層級 Group Split（訓練、驗證、測試集原圖零重疊），並以五個 seed 重複實驗評估模型穩定性，並於其中 seed=7 一例下追加單變因消融、模型校準、Grad-CAM 與外部未標注影像檢查，以區分單次案例與可重現之穩定結論。

主要結論如下：(1) 五 seed 重複後，四組模型 / 策略之平均 accuracy 落在 80.12\%–81.19\%，較多數類別基準（恆預測 A 等級 ≈ 49.2\%）高出約 31 個百分點，顯示模型習得超越多數類別猜測的辨識能力；因 n=5 之統計效力嚴重不足（中等效應量之 power 低於 0.3），各設定差異無法透過統計檢定可靠區分，本研究\textbf{不宣稱任何單一模型 / 策略為穩定最佳}，所有模型 / 策略差異均定位為待更大樣本研究確認的探索性現象。(2) MobileNetV3-Large 完整設定 accuracy 之 std 為 5.98\%（四組中最大），對 seed 較敏感；且完整設定因 WeightedRandomSampler 使每 epoch 訓練步數約為簡化設定六倍，兩設定比較本身存在根本性設計缺陷（梯度更新量不對等），任何觀察到的差異無法歸因於策略本身，完整設定不應被視為穩定優於簡化設定。(3) seed=7 詳細案例中簡化設定達 86.31\%、完整設定達 89.88\%，僅作為混淆矩陣、校準與可視化之觀察案例，不可外推為穩定效能。(4) 各等級分析顯示 A/B 邊界（B 級召回率 56.3\%）為本系統最薄弱環節。(5) 品質分輔助頭因監督目標為等級編號之線性轉換、未經多人主觀評分校準，僅可作為分類結果以外之排序輔助訊號，不宜視為絕對品質分。

本研究於 FDM 魚骨拉絲瑕疵此一特定條件下提供內部評估基準與整批照片自動處理流程原型，並指出受限於單一機型、單一材料、單一形狀、單一瑕疵類型、標注一致性未驗證、PLA 顏色批次間未受控以及拍攝條件未標準化等條件，現階段定位為品質管控之輔助工具，而非可獨立判定之自動分級系統；**本研究所報告之效能數字均為內部基準，無法與任何現有方法在相同條件下進行直接比較**。需特別說明，本文所報告之模型準確率（80–81\%）係相對於單一標注者之固定標注準則，而非相對於多人共識品質標準；在多人一致性驗證完成前，上述數字反映的是「模型複製一人判斷之能力」，不等同於「正確辨識客觀品質之能力」。

\vspace{0.5cm}

\noindent\textbf{關鍵詞：3D 列印、熔融沉積成型（FDM）、瑕疵檢測、深度學習、MobileNetV3、遷移學習、序數分類、資料不平衡、分組切分（Group Split）、多 seed 評估、模型校準}

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

3D 列印技術（Three-Dimensional Printing），又稱積層製造（Additive Manufacturing, AM），係指透過電腦輔助設計（CAD）軟體建立三維數位模型後，依據切片軟體產生的路徑指令，將材料逐層堆積成形的製造技術[@ISOASTM52900]。自 Charles Hull 於 1984 年提出光固化成型技術（Stereolithography, SLA）相關專利，並由 3D Systems 推動早期商業化應用後，3D 列印技術歷經數十年的持續演進，應用範圍由工業快速原型製造逐漸擴展至航太、汽車、醫療、電子、建築及個人消費等多元應用領域[@gibsonAdditiveManufacturingTechnologies2021; @OurStory3D2017]。市場研究機構 MarketsandMarkets 於 2023 年估計，全球 3D 列印市場規模可能由 2023 年約 150 億美元成長至 2028 年約 345 億美元，年均複合成長率約為 18.1\%[@marketsandmarkets3DPrintingMarket]（此數字來自商業調查機構付費報告，非同儕審查文獻，僅作緒論趨勢背景使用，不參與本研究任何技術論證），顯示此一製造技術在全球產業中的應用前景持續擴展。

在眾多 3D 列印技術中，熔融沉積成型（Fused Deposition Modeling, FDM）因設備成本相對低廉、操作流程較為簡易，且可支援 PLA、PETG、ABS、TPU 等多種熱塑性材料，成為桌上型與教育應用場域中常見的 3D 列印技術之一[@gibsonAdditiveManufacturingTechnologies2021; @InventorFDM3D2017]。FDM 的基本工作原理是將熱塑性聚合物線材（Filament，直徑通常為 1.75 mm 或 2.85 mm）送入加熱腔，融化後由噴嘴（Nozzle）擠出，依照切片路徑在熱床（Heated Bed）上逐層堆積，冷卻固化後形成實體成品。由於 FDM 技術的普及，其列印品質管控的重要性日益受到業界與學術界的重視。

然而，FDM 列印的品質受到多項關鍵參數的交互影響，包括噴嘴溫度、熱床溫度、列印速度、回抽距離（Retraction Distance）與速度、層高（Layer Height）、填充密度（Infill Density）、冷卻風扇轉速及支撐結構設定等。任一參數設定不當，均可能引發不同類型的列印瑕疵，導致成品品質下降。目前業界對 FDM 列印品質的評估，仍多依賴操作人員的人工目視檢查，缺乏系統化、自動化的品質管控機制，難以滿足工業 4.0 背景下智慧製造的需求。

近年來，以卷積神經網路（CNN）為代表的深度學習影像辨識技術在工業視覺檢測領域取得顯著進展[@WhatIndustry40; @WhatIndustrie40]，為自動化品質管控提供了新的技術路徑；將此類技術導入 FDM 列印後成品之品質輔助辨識，具有實際應用探索價值。需特別說明的是，本研究聚焦於列印**完成後**之離線辨識，與工業 4.0 所強調之即時連網監控屬互補方向：前者著重列印後成品分級與品質追溯，後者著重列印過程之即時介入；本研究選擇前者，因其資料蒐集、標注與評估流程在實驗室規模下較為可行，亦能作為日後即時監控之離線基準（即時監控之延伸見第 \ref{sec:conclusion-future} 節）。

## 研究動機 {#sec:intro-motivation}

在實際的 3D 列印生產場景中，品質管控面臨以下幾項核心困難：其一，人工目視效率低落，當列印批量增加時，每件成品的逐一檢視耗時過長，成為生產流程的瓶頸；其二，主觀判斷標準不一，不同操作人員對同一件成品的品質評估可能存在差異，尤其在瑕疵程度接近等級邊界的案例中，判斷結果的不一致性會降低品質數據的可信度；其三，缺乏一致且可追溯的數值化紀錄，傳統目視評估不易形成可比較的品質分布；其四，難以建立品質歷史紀錄，人工評估結果不易系統性地留存，不利於品質趨勢分析與製程改善。

深度學習影像分類技術具備從大量樣本中自動學習視覺特徵的能力，能客觀量化瑕疵嚴重程度，恰能彌補上述人工目視的不足。然而，3D 列印拉絲瑕疵的嚴重程度判定具有明顯的序數特性：少量短絲仍屬可接受範圍，大範圍絲狀殘留則需重新列印，等級邊界常受光線、角度與標注者主觀判斷影響。此外，在小批量研究場景中，取得大量具多人一致性標注的資料往往成本高昂，資料集的類別不平衡問題亦難以避免。在上述挑戰條件下，如何建立一套嚴格且可重現的評估框架，以確認深度學習模型是否真正具備作為品質管控輔助工具的潛力，是本研究的核心動機。

## 研究目的與貢獻 {#sec:intro-purpose}

本研究的核心貢獻有以下四項：

1. **FDM 魚骨拉絲六等級資料集**：建立包含 1110 張魚骨影像、依目視估計拉絲覆蓋比例定義之六等級（A 至 F）分類資料集，以原圖層級 Group Split 確保訓練與測試集原圖零重疊，提供本研究條件下之可重現內部評估基準，供後續 FDM 拉絲瑕疵小樣本影像分類研究比較。
2. **可重現的嚴格評估協定**：以原圖為單位進行 Group Split（原圖零重疊），避免同源樣本造成過度樂觀的評估；以多數類別分類器（恆預測 A 等級，accuracy ≈ 49.2%）作為效能基準下限，所有模型結果必須明顯超越此基準線才具備學習意義；透過五組 seed 重複實驗報告平均值與標準差，並明確說明 n=5 之統計效力限制，以提供比單次切分更保守且可重現的小樣本工業視覺評估基準。
3. **模型策略比較、消融與不確定性分析**：系統比較 MobileNetV3-Large、ResNet18、EfficientNet-B0 三種骨幹，並消融 Focal Loss、Label Smoothing、Mixup、Weighted Random Sampler 等訓練策略，評估各因素對少數類別分類的實際貢獻；並進行模型校準分析，確認低置信度樣本可納入人工複核流程。
4. **整批照片自動處理流程（工程整合原型）**：整合自動裁切、逐張前向推論、分級輸出與 HTML 可視化報告，形成由原始照片到品質等級報告之離線處理流程；並於 RTX 3050 Laptop GPU 上量測純模型前向延遲作為部署參考基準（量測條件與端到端吞吐量限制詳見第 \ref{sec:results-batch} 節）。需說明，此項屬工程整合產出，而非方法論層面的研究貢獻；其科學意義在於驗證完整推論管線可實際執行，並提供離線部署所需的延遲量測基準，而非提出新的方法或理論。

附帶產出包含具明確判斷規則的六等級評分準則、各等級範例圖、Label Studio 標注流程，以及雙輸出（六分類 + 0 至 100 連續品質分）模型架構；其中品質分輔助頭因監督目標為等級編號之線性轉換、未經多人主觀評分校準，僅可作為分類結果以外之排序輔助訊號，不宜視為獨立的絕對品質量化指標。

**本研究的核心研究問題**有二：（1）在小樣本（1,110 張）、類別不平衡（最大比例 17:1）、嚴格 Group Split 切分與五 seed 重複評估之條件下，MobileNetV3-Large 遷移學習可達到何種效能水準（accuracy、B 等級召回率、QWK 與信心校準），以及高信心子集是否具備足以支持「高信心 A 等級自動標記、低信心與非 A 等級移交人工複核」分流策略的初步可行性？多數類別基準分類器（恆預測 A 等級 accuracy ≈ 49.2%）作為效能下限，超越此基準是必要條件而非充分條件；本研究的核心判斷標準在於模型是否能在 B 等級等邊界類別達到對品質管控有實際意義的召回率門檻，而非僅僅超越多數類別猜測。（2）加入 Focal Loss、Label Smoothing、Mixup 與 Weighted Sampler 的完整不平衡處理組合，在五 seed 重複評估中呈現何種趨勢？需特別說明，此比較因 WeightedRandomSampler 導致完整設定每 epoch 訓練步數約為簡化設定六倍（詳見第 \ref{sec:method-model} 節），兩設定訓練量根本不對等，此缺陷在研究結束後才完整識別；因此此問題定位為**探索性觀察而非有效策略評比**，不能由此得出任何設定優劣的可靠結論。基於文獻對溫和不平衡（約 17:1）場景中複雜損失組合可能因理論張力而效益有限之觀察（詳見第 \ref{sec:method-model} 節），本研究的先驗預期為兩設定差異有限，而非預設完整設定必然優勝。

**本研究各項貢獻均在以下條件範圍內成立**：全部樣本由單一標注者完成，多人標注一致性（Cohen's Kappa）尚待驗證；模型效能指標係相對於此固定標注準則之複現能力，而非相對於多人共識品質標準——換言之，本文所報告的 accuracy 數字反映的是「模型複製一位標注者判斷的能力」，不等同於「正確辨識客觀品質等級的能力」；在多人一致性驗證完成前，上述區分至關重要，不應省略。所有結果限定於本研究之特定硬體、材料與幾何條件（詳見第 \ref{sec:intro-scope} 節）；此外，本研究 PLA 顏色批次間未受控、拍攝條件（曝光、白平衡、距離）未固定，模型是否確實學習拉絲紋理而非顏色或光線偽特徵，目前僅有定性 Grad-CAM 排查，尚無量化驗證。

## 研究範圍 {#sec:intro-scope}

本研究的研究範圍以 FDM 技術列印之魚骨形狀 PLA 材質列印件為主要研究對象。魚骨形狀具有細長肋條、尖端與多個固定間隙，依本研究前導列印觀察：當噴嘴溫度偏高或回抽設定不足時，拉絲細絲最先出現於肋條間隙與尖端，且不同批次的嚴重程度差異在視覺上可清楚區別；加以每件間隙數量固定（六個肋條間隙）、黑色熱床背景與 PLA 本體色對比明確、裁切邊界規則，使影像上的拉絲覆蓋程度能依面積比例進行分級，適合作為本研究拉絲嚴重程度分類的標準測試件。本研究聚焦於拉絲瑕疵的嚴重程度分類，不包含翹曲及裂痕瑕疵的深入分析（因現有樣本中此兩類瑕疵數量不足）。實驗設備限定為 Bambu Lab A1 3D 印表機，耗材為標準 PLA 線材，拍攝環境為固定背景的室內自然光環境，因此模型的泛化能力主要針對此特定設備與材料條件。資料規模方面，本研究資料集共取得 1110 筆有效魚骨樣本，分屬六個品質等級，最多等級 546 張（A 級），最少等級 32 張（F 級）。

為使後續讀者與審查者能正確解讀本研究之結論，茲將本研究之適用範圍與已知限制條列如下：

1. **單一硬體條件**：僅使用 Bambu Lab A1 印表機與標準 PLA 線材，未驗證其他機型（如 Prusa、Creality）或材料（如 PETG、ABS、TPU）之表現。
2. **單一幾何條件**：僅使用魚骨形狀樣本，模型對其他幾何形狀（如盒體、齒輪、有機曲面）之泛化能力未經驗證。
3. **單一瑕疵類型**：僅針對拉絲（Stringing）嚴重程度分類；翹曲與裂痕雖於文獻回顧介紹，但因樣本不足未納入訓練與測試。
4. **資料相關性**：1110 張樣本係由 185 張原始照片裁切而來，同源樣本在光線、背景與列印批次上高度相關；評估時採原圖層級 Group Split 確保訓練與測試集原圖零重疊，詳見第 \ref{sec:method} 章。
5. **列印參數文件不完整**：回抽距離（Retraction Distance）與回抽速度（Retraction Speed）係拉絲最直接相關的參數，但因未進行逐批截圖留存，無法逐批驗證兩參數之一致性，相關細節詳見附錄二表 \ref{tab:param-summary}。
6. **PLA 顏色未受控**：本研究不同批次使用多種顏色之 PLA（包含灰色、藍綠色、藍色、黃綠色等），顏色差異為未受控變因。若某顏色批次與特定等級存在系統性共現，模型可能學習顏色特徵而非拉絲紋理，產生虛假高準確率。資料增強中之 ColorJitter 雖可部分吸收亮度與色調變異，但無法取代嚴格的顏色控制；此風險已由 Grad-CAM 定性排查（第 \ref{sec:results-supplemental-calibration} 節），但定性觀察不等同於量化排除。

上述邊界條件確立了本研究的適用範圍；其餘方法與實驗設計層面之限制，詳見第 \ref{sec:conclusion} 章結論。

## 研究流程 {#sec:intro-flow}

本研究的整體執行流程分為三大階段：第一階段為資料蒐集與前處理，包含 3D 列印樣本製作、影像拍攝、魚骨自動裁切及人工標注；第二階段為模型訓練與評估，包含資料集整理、模型訓練、效能評估、多 seed 重複與消融分析；第三階段為系統整合與應用，包含整批照片自動處理流程開發、可視化報告產生及實際應用驗證。各階段之時序順序如圖 \ref{fig:overall-flow} 所示；資料流與責任分工另見第 \ref{sec:method-architecture} 節。

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

從影像辨識的角度而言，拉絲在影像中呈現細線狀、高頻率的局部紋理，通常以明亮細絲出現在較暗背景（如黑色熱床）或魚骨間隙中，形成與正常平滑表面明顯不同的對比特徵。此類特徵屬影像的高頻空間成分，對局部感受野敏感的卷積神經網路（CNN）比傳統全域描述子（如顏色直方圖）更適合捕捉；拉絲嚴重程度的差異則進一步反映在細絲密度與分布面積上，使得等級分類可藉由 CNN 對多尺度局部紋理的感知來實現。第四章 Grad-CAM 定性觀察將就此推論提供初步個案參考：部分正確預測案例之熱力圖高亮區域看似集中於魚骨間隙附近，但由於本研究未進行 IoU 量化分析，此觀察僅為定性探索，不能作為「模型確實依賴拉絲紋理」的量化驗證；詳見第 \ref{sec:results-supplemental-calibration} 節之 Grad-CAM 部分。

## 電腦視覺與深度學習於工業瑕疵檢測 {#sec:literature-cv-dl}

電腦視覺（Computer Vision）技術在工業品質檢測領域的應用已有數十年歷史，早期方法以傳統影像處理技術為主，包括邊緣偵測、閾值分割、形態學運算及特徵工程等，需要領域專家手動設計特徵提取規則。此類方法在受控環境下（固定光源、背景及目標位置）表現尚可，但對光線變化、姿態變化及背景干擾的魯棒性較差，且難以應對複雜的多類別瑕疵辨識任務。

深度學習技術的崛起從根本上改變了電腦視覺的研究範式[@DeepLearning; @lecunGradientbasedLearningApplied1998]。卷積神經網路（CNN）以端到端的方式自動學習影像的層次化特徵表示，從底層的邊緣和紋理特徵到高層的語義特徵，無需人工設計特徵，且在充足資料的支持下，其辨識精度通常優於傳統人工特徵方法[@dengImageNetLargescaleHierarchical2009; @heDeepResidualLearning2016]。近年來，CNN 已被廣泛應用於半導體晶圓瑕疵檢測、紡織品缺陷辨識、鋼板表面瑕疵分類、PCB 板焊接缺陷偵測等工業品質管控任務[@bhattImageBasedSurfaceDefect2021]，並在多項公開基準或受控資料集上取得高辨識率；在 3D 列印領域，亦已有研究將 CNN 應用於列印過程的即時錯誤偵測與校正[@brionGeneralisable3DPrinting2022]。

值得注意的是，工業瑕疵檢測文獻中另有一類基於**異常偵測（Anomaly Detection）**的無監督或半監督方法，如以自動編碼器（Autoencoder）的重建誤差判斷是否異常，或以正常樣本建立特徵分布、測試時以馬氏距離偵測偏離[@bhattImageBasedSurfaceDefect2021]。此類方法的優勢在於訓練時僅需正常樣本，不必對每種瑕疵類型逐一標注；但其輸出為「正常/異常」的二元判斷，無法直接輸出瑕疵嚴重程度等級。本研究的核心目標是對拉絲嚴重程度進行 A 至 F 六等級的**序數分級**，需要每張樣本帶有等級標籤才能訓練分類或迴歸模型，因此選擇有監督分類路線，而非無監督異常偵測。需承認，本研究未對兩種路線進行實驗比較；在本研究的資料條件下（A 等級佔 49.2\%，可視為「正常品」），半監督異常偵測（以 A 等級樣本建立正常特徵分布，測試時偵測偏離）在理論上具可行性，但其輸出為「正常/異常」二元判定，無法直接提供 A 至 F 六等級之序數分級輸出，此為本研究不採用此路線的核心業務需求考量；若後續研究以「有無瑕疵」的粗粒度判定為目標，異常偵測路線值得另行探索比較。

## 相關文獻探討 {#sec:literature-related}

本節依「通用影像分類 → 小樣本遷移學習 → 類別不平衡處理 → 與本研究最相近之 FDM 領域研究」的順序，逐步收斂至本研究的問題情境。

CNN 以端到端方式自動學習影像的層次化特徵表示，在充足資料的支持下，其辨識精度通常優於傳統人工特徵方法---此為深度學習文獻中已建立的共識[@DeepLearning; @lecunGradientbasedLearningApplied1998]。Jogin 等人[@joginFeatureExtractionUsing2018]的 CIFAR-10 實驗（85.97\% 準確率，顯著優於 SVM 與隨機森林）提供了一個具體的多類別分類參照，說明 CNN 學得的深度特徵在非工業影像分類任務上的系統性優勢；惟此屬通用影像分類，與 FDM 表面瑕疵視覺特徵之關聯僅屬間接，主要用途是為本研究採用 CNN 骨幹提供方法論背景。

在工業視覺領域，Bhatt 等人[@bhattImageBasedSurfaceDefect2021]系統性回顧了 CNN 於表面瑕疵偵測的應用現況，指出在標注樣本有限（通常千張量級）的工業場景中，以 ImageNet 預訓練模型進行特徵遷移已成為標準做法，並在半導體晶圓、鋼板、紡織品等任務上取得優於傳統特徵工程的結果。此工業視覺同域文獻直接支持本研究採用 MobileNetV3-Large ImageNet 預訓練權重遷移至 FDM 拉絲影像的策略選擇，其方法論基礎比跨領域類比（如醫學影像）更為可靠。Varshni 等人[@varshniPneumoniaDetectionUsing2019]的胸腔 X 光遷移學習實驗（DenseNet-169+SVM，AUC 0.8002）因醫學 X 光與工業表面紋理在視覺特性與標注性質上差異甚大，與本研究之關聯極為間接，不具備遷移學習可行性的直接支持效力，此後不再引用，建議後續研究以工業視覺同域文獻（如 Bhatt 等人[@bhattImageBasedSurfaceDefect2021]）為主要遷移學習方法論依據。

Lin 等人[@linFocalLossDense2017]提出之 Focal Loss 原用於**目標偵測**中前景與背景之極端類別不平衡（原始論文情境下比例可達 1000:1 以上），其在標準交叉熵的基礎上引入調焦因子 $(1-p_t)^\gamma$，降低模型已正確分類之高信心樣本的損失權重，使訓練聚焦於困難樣本（Hard Example）。需指出，本研究六個等級中最大不平衡比例約為 17:1（A 級 546 張對 F 級 32 張），屬相對溫和的失衡，與原論文情境有別。在溫和不平衡的多類別分類場景中，Focal Loss 的主要作用是強迫模型對邊界樣本持續更新梯度，而非解決比例極端失衡；其能否在此條件下穩定優於標準 Cross Entropy 目前仍無定論，且與 Label Smoothing 同時使用時存在理論張力（詳見第 \ref{sec:method-model} 節）。本研究引入 Focal Loss 是作為探索性的多重不平衡處理手段之一（配合 Weighted Sampler、Label Smoothing），而非針對極端比例失衡的主要解法；其實際效益以第 \ref{sec:results-supplemental-ablation} 節之消融實驗結果為準。**需特別指出**，目前文獻中缺乏 Focal Loss 在 10:1 至 20:1 這類溫和多類別失衡分類任務（非目標偵測）中相對於標準 Cross Entropy 的系統性比較，本研究採用 Focal Loss 的理論基礎較弱；加以本研究消融實驗僅有 seed=7 單次結果，其效益方向不具統計意義，後續研究引用此結果時應謹慎。

與本研究最直接相關者為 Brion 與 Pattinson[@brionGeneralisable3DPrinting2022]，其以多頭神經網路對 FDM 列印過程進行**即時**錯誤偵測與參數校正，並在多種印表機、材料與幾何形狀上展現泛化能力，屬「列印中（in-process）」的閉迴路監控。相較之下，本研究著眼於「列印後（post-print）」的成品表面品質評級：將拉絲瑕疵依嚴重度劃分為 A 至 F 六個**序數**等級並輸出連續品質分，且採用保留未來邊緣部署彈性的輕量模型，於小規模且不平衡的資料上以嚴格切分重複評估。兩者在偵測時機、輸出粒度與應用情境上互補，而後者正是本研究欲補足之處（詳見第 \ref{sec:literature-gap} 節）。

需特別說明本研究之文獻涵蓋範圍：本章所引用之 FDM 列印後成品表面品質影像分類文獻以 Brion 與 Pattinson[@brionGeneralisable3DPrinting2022] 為主，主因此方向之受同儕審查論文目前仍相對有限——既有工業視覺文獻多聚焦於半導體、鋼板、紡織品等傳統製造場景，而 FDM 領域之深度學習研究偏向「列印中即時監控」而非「列印後序數品質分級」。本研究認知到此文獻基礎之侷限，並於第 \ref{sec:literature-gap} 節明確說明研究缺口；後續若有更多同域文獻出現，本研究之方法論比較基礎可進一步擴充。

## MobileNetV3 架構 {#sec:literature-mobilenetv3}

MobileNet 系列最早由 Howard 等人提出，其核心設計是以深度可分離卷積（Depthwise Separable Convolution）取代標準卷積：將其分解為深度卷積（Depthwise Conv）與逐點卷積（Pointwise Conv）兩步驟，在維持感受野的同時大幅降低參數量與計算量，使 CNN 更適合部署於行動端與邊緣裝置[@howardMobileNetsEfficientConvolutional2017]。MobileNetV3 則由 Google 以神經架構搜尋（NAS）自動搜尋最優配置，並在深度可分離卷積的基礎上再引入兩項關鍵技術[@howardSearchingMobileNetV32019]：（1）**壓縮激活（Squeeze-and-Excitation, SE）注意力機制**：對特徵圖各通道的重要性進行自適應加權，強化關鍵特徵的表達；（2）**Hard-Swish 激活函數**：以分段線性函數近似 Swish 激活，在效能損失極小的前提下大幅降低計算成本。

MobileNetV3-Large 的整體架構包含：初始卷積層（3 × 3 卷積，stride = 2）、15 個 Bottleneck 模組（其中部分模組含 SE 注意力機制）、1 × 1 卷積升維層（將通道從 160 升至 960）、自適應平均池化層（輸出 960 維向量），以及最終的分類頭（含 Linear(960→1280) + Hardswish + Dropout + Linear(1280→1000)）。其中，池化後的 1280 維中間特徵是本研究雙輸出頭的共用輸入（詳見第 \ref{sec:method-model-dualhead} 節）。以 224 × 224 像素輸入為例，三個候選模型的效率指標比較如表 \ref{tab:model-complexity} 所示。

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

遷移學習（Transfer Learning）在電腦視覺領域的核心假設是：在大規模資料集（如 ImageNet）上預訓練的模型，已學習到豐富的底層視覺特徵（邊緣、紋理、形狀等），這些特徵可以遷移至目標任務，即使目標任務的資料量遠少於預訓練資料集。常用的遷移學習策略包括：（a）**特徵提取（Feature Extraction）**：凍結預訓練模型的全部或大部分層，僅訓練新增的任務特定層；（b）**微調（Fine-tuning）**：以較小的學習率對全部或部分層進行更新，使模型特徵更好地適應目標任務。本研究兩組設定（簡化與完整）均採用全層微調（Full Fine-tuning）策略；兩者的差異主要在於損失函數、資料增強（有無 Mixup）與過採樣設定的組合，詳見第 \ref{sec:method-model} 節。

資料不平衡（Class Imbalance）是小樣本瑕疵分類常見的難題，文獻上的處理手段大致可分為三類：（1）**資料採樣層面**的重採樣，如對少數類別過採樣（oversampling）或加權抽樣，平衡各類別在訓練過程中的曝光機會；（2）**損失函數層面**的成本敏感法，包括前述 Focal Loss[@linFocalLossDense2017]（對困難樣本加重懲罰）與 **Label Smoothing**（將分類目標由硬標籤替換為軟標籤，分配小量機率 $\epsilon$ 給非目標類），後者有助於避免模型對多數類別樣本產生過度自信，並在少數類別邊界保留更多梯度訊號；（3）**資料增強層面**的方法，如 Mixup[@zhangMixupEmpiricalRisk2018]在批次中對任意兩筆樣本進行線性混合，擴充訓練分布的多樣性並抑制模型對邊界樣本的過度自信。三類手段彼此正交、可組合使用。本研究完整設定採用 Focal Loss + Label Smoothing ($\epsilon=0.1$) + Mixup ($\alpha=0.3$) + Weighted Sampler 之組合，簡化設定僅保留標準 Cross Entropy；同時啟用 Focal Loss 與 Label Smoothing 之理論張力、Mixup 應用於序數分類之物理意義限制以及 MixFocal 偏離原設計等實作取捨，詳見第 \ref{sec:method-model} 節。

此外，本研究的 A 至 F 等級並非彼此完全獨立的名目類別，而具有由良品到嚴重瑕疵的序數關係。序數分類（Ordinal Classification）與名目分類的根本差異在於：相鄰等級間的誤判（如 B 誤判為 A）比跨等級誤判（如 D 誤判為 A）代價更低，因此評估指標應能反映此等級距離懲罰。**Quadratic Weighted Kappa（QWK）** 是序數分類任務的常用評估指標，其對誤判距離的懲罰以等級差距的平方加權，使跨等級誤判受到更大的懲罰；相較之下，accuracy 對所有誤判一視同仁，不適合作為序數分類的唯一指標[@CohenKappaStatistic]。就 QWK 的解讀基準而言，文獻通常以 0.81 以上為「幾乎完美一致（Almost Perfect）」、0.61–0.80 為「實質一致（Substantial）」；本研究最終報告之 QWK 約 0.91，從數值上落於「幾乎完美一致」區間，但需注意此數字係相對於單一標注者標籤，在多人標注一致性驗證完成前，此 QWK 值反映的是「模型複製一人序數判斷之能力」，不等同於「相對客觀序數品質標準的一致程度」。

序數分類文獻提出多種以排序一致性約束處理等級輸出的方法：CORAL（Consistent Rank Logits）將等級順序直接編碼至模型輸出層，透過共享權重的多個二元分類器確保輸出的等級一致性[@caoRankConsistentOrdinal2020]；CORN（Conditional Ordinal Regression for Neural Networks）則以條件機率鏈確保等級機率單調性[@shiDeepNeuralNetworks2023]。這兩種方法直接作用於訓練目標，理論上比本研究採用的「名目分類 + MSE 輔助頭」架構更適合序數分級任務；然而本研究受限於研究規模與時程，未能在主實驗中納入 CORAL 或 CORN，此為本研究方法設計的一項重要不足，相關缺口詳見第 \ref{sec:conclusion-future} 節建議 1。模型信心校準可用於檢查 softmax confidence 是否能反映預測可靠度，temperature scaling 為常見的後處理方法之一[@guoCalibrationModern2017]。本文目前以 nominal classification 作為主要訓練方式，因此在結果章中特別回報 QWK、跨等級誤判率（即預測等級與真實等級差距 $\geq 2$ 的樣本佔比）與校準分析，避免只用 accuracy 解讀序數分級任務。

## 研究缺口與本研究定位 {#sec:literature-gap}

綜合前述文獻，可歸納出三點現況與缺口。其一，CNN 與遷移學習在工業表面瑕疵檢測（半導體晶圓、鋼板、紡織品、PCB 等）已有成熟應用，並在多項公開基準或受控資料集上取得高辨識率[@bhattImageBasedSurfaceDefect2021]；但這些任務多屬「有無瑕疵」或「瑕疵種類」的名目分類，少有針對單一瑕疵之「嚴重程度分級」的序數評估。其二，在 FDM 領域，既有代表性研究（如 Brion 與 Pattinson[@brionGeneralisable3DPrinting2022]）聚焦於列印過程中的即時錯誤偵測與校正，著重「即時介入、避免廢件」，而非列印完成後對成品表面品質給出較細緻且可追溯的分級。其三，遷移學習雖已證實能緩解小樣本問題[@varshniPneumoniaDetectionUsing2019]，但各研究的資料規模、不平衡程度與評估切分方式差異甚大，少有在「小樣本、類別不平衡」條件下同時報告嚴格切分、多 seed 重複與校準分析的可重現評估。

據此，本研究的定位是補足「列印後、單一瑕疵（拉絲）、序數品質分級、輕量模型、嚴格可重現評估」這一交集情境：以 ImageNet 預訓練之 MobileNetV3-Large 為骨幹進行遷移學習，輸出 A 至 F 六等級分類並附加連續品質分；針對類別不平衡採用重採樣、成本敏感損失與資料增強的組合（見第 \ref{sec:method-model} 節）；並以 Group Split 嚴格切分、多 seed 重複與校準分析建立可重現的效能基準（見第 \ref{sec:results} 章）。目前文獻中與本研究完全相同之「列印後拉絲序數分級」情境仍相對有限，因此本文定位為此特定條件下的探索性基準。

# 研究方法 {#sec:method}

## 研究架構 {#sec:method-architecture}

本研究系統架構以**資料流與責任分工**為主軸呈現（相較於緒論圖 \ref{fig:overall-flow} 著重三階段時序，本圖補充各模組之輸入輸出關係），如圖 \ref{fig:method-flow} 所示。整體流程由列印製樣與影像蒐集開始，經由裁切前處理與人工標注建立 A 至 F 六等級資料集，再以 MobileNetV3-Large 進行遷移學習訓練，最後輸出混淆矩陣、品質分數、分級資料夾與 HTML 統計報告。此呈現方式可直接對應資料來源、模型訓練與推論輸出三大環節。硬體端由 Bambu Lab A1 印表機、智慧型手機（用於拍攝）與配備 NVIDIA RTX 3050 Laptop GPU 之筆記型電腦（用於訓練與推論）組成，硬體規格詳見第 \ref{sec:method-equipment-pc} 節。

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

完整 Bambu Studio 參數設定彙整於附錄二（表 \ref{tab:param-summary}），作為實驗重現之查核依據。

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
CUDA & 12.4 \\
cuDNN & 未紀錄 \\
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

噴嘴溫度、熱床溫度與風扇冷卻策略均視為本研究之背景製程條件，而非主動操控變因；完整設定值整理於附錄三。

## 列印樣本製作與影像蒐集 {#sec:method-sample}

### 樣本設計與列印過程 {#sec:method-sample-design}

本研究以魚骨形狀列印件作為樣本，是因其具有細長肋條、尖端與多個間隙，對 FDM 拉絲瑕疵特別敏感。當噴嘴溫度、回抽設定、移動速度或冷卻條件不穩定時，細絲通常會出現在魚骨間隙與尖端區域，因此此幾何形狀適合作為拉絲嚴重程度分類的測試對象。

資料蒐集採分批列印方式進行，並另行補充少數等級與失敗件樣本，使各等級樣本更為完整（B、E、F 少數等級之補充樣本中，詳細製作條件---包含是否刻意調差列印參數、具體調整項目及各等級之原圖群組數---未逐批留存紀錄，此為本研究資料文件之已知限制；讀者解讀模型對 E、F 等級之表現時，應考量樣本取得方式未明確記錄可能影響其代表性）。每組原始照片可裁切出 6 支魚骨樣本，最後整理為 1110 筆有效資料。正文保留資料蒐集流程與代表性設計說明，完整列印過程照片改列於附錄一，避免主文被連續照片切斷。

### 影像拍攝規範 {#sec:method-sample-capture}

影像拍攝採用固定角度與固定背景的標準化規範。拍攝設備為智慧型手機相機，鏡頭以俯拍方式對準列印床，並盡量維持相同拍攝位置與室內環境，以降低批次間因視角、背景與反光造成的差異。由於拍攝作業缺乏系統性文件化，手機型號、主鏡頭等效焦距、鏡頭距列印床垂直距離及室內光源條件均未紀錄；是否全程同一支手機亦未確認；相機 App 以自動曝光（AE-Lock 未鎖定）與自動白平衡（AWB-Lock 未鎖定）模式拍攝，ISO、快門與光圈均為自動設定。**這些拍攝條件的未受控是本研究最根本的資料品質問題之一**：工業視覺檢測的標準實作要求固定光源（方向、色溫、亮度）、固定拍攝距離與固定相機設定（ISO、快門、光圈），缺乏這些控制時，不同批次的影像在亮度、對比和色彩上的系統性差異可能與等級標籤部分相關，讓模型學到「拍攝批次特徵」而非「拉絲特徵」。本研究資料已無法補救，後續研究應以固定燈箱、固定架距與手動鎖定曝光為最低拍攝標準。上述拍攝條件未受控為本研究資料文件之已知限制，讀者解讀跨批次泛化邊界時應一併考量。此外，本研究不同批次使用多種顏色之 PLA（灰色、藍綠色、藍色、黃綠色等），顏色差異為**嚴重的未受控混淆變因**。若某顏色批次在資料蒐集中與特定等級高度共現（例如，若大部分 F 等級樣本恰好來自黃綠色 PLA 批次），模型可能學習到顏色特徵而非拉絲紋理，在測試集上仍呈現高準確率，但其實際運作機制是顏色分類而非品質分級，部署到其他顏色條件時將完全失效。**此問題無法以 ColorJitter 資料增強或 Grad-CAM 定性排查解決**：ColorJitter 只能增加顏色擾動的訓練多樣性，但若不同等級本身就以不同顏色 PLA 呈現，增強並不能消除這個混淆；Grad-CAM 的定性觀察存在確認性偏誤風險（見第 \ref{sec:results-supplemental-calibration} 節）。根本解決方案是在資料蒐集時使用統一顏色的 PLA（或至少確保每種顏色在各等級均有代表樣本）；本研究受限於既成條件無法補救，讀者解讀本研究所有效能數字時，應考量部分準確率可能來自顏色識別而非拉絲辨識。背景為 Bambu Lab A1 原廠的黑色熱床表面，與各色 PLA 魚骨形成良好的明暗對比，有助於後續影像裁切與辨識。由於本研究未強制鎖定曝光、白平衡與 ISO，不同批次間之亮度與色調可能存在輕微差異；此項拍攝條件變異性已於資料增強中以 ColorJitter（亮度 0.4、對比 0.4、飽和 0.3、色相 0.1）部分吸收，但不能取代固定拍攝條件下之嚴格控制（詳見第 \ref{sec:method-preprocessing-aug} 節）。拍攝完成後，資料再依批次進行裁切、標注、模型訓練與辨識分析。各批次拍攝資料統計如表 \ref{tab:batch-stats} 所示。

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

以下圖 \ref{fig:crop-fish01} 至圖 \ref{fig:crop-fish03} 為自動裁切輸出的魚骨裁切結果範例，可目視確認每支魚骨被完整切割、背景一致。需說明的是，本研究對裁切品質僅進行目視抽查，未以魚骨主體佔裁切圖面積比例或魚骨是否完整出現等定量指標系統驗證全部 1110 張；若特定批次放置位置有系統性偏移，固定網格裁切可能截到背景而非完整魚骨，此為本研究資料前處理的已知限制。**此問題的嚴重性在於**：若有一定比例的裁切圖包含不完整的魚骨或背景區域，對應的等級標籤將與實際影像內容不符，成為帶雜訊的訓練樣本，進而降低模型的學習效率與評估結果的可信度。正確的做法是以自動化方式（如魚骨邊界框偵測或輪廓偵測）驗證每張裁切圖的魚骨完整性，並剔除裁切失敗的樣本；本研究受限於實驗設計未能執行此步驟，後續研究應將此列為資料品管的優先改進項。

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

本研究依目視估計之拉絲覆蓋比例與魚骨結構可辨識程度，制定六個品質等級（A 至 F），如表 \ref{tab:grading-criteria} 所示。採用六等級而非二元（合格/不合格）的設計考量如下：（1）工業品管實務中需區分「可直接使用」、「低要求場合可接受」、「需後處理」與「廢品」四種行動決策，二元判定提供的決策粒度不足；（2）拉絲嚴重程度在視覺上呈現連續分布，六個區間能較均勻地涵蓋從「無拉絲」到「結構失敗」的完整範圍；（3）六等級亦能與品質分輔助頭的連續數值輸出建立對應關係，提供排序訊號。需說明，六等級的邊界設定（如「目視覆蓋 1/4」）係人眼估計而非像素分割量測，存在標注者間的主觀差異，此限制已在第 \ref{sec:method-labeling} 節進一步討論。等級定義以覆蓋比例區間作為**目視經驗準則**，而非透過影像分割演算法實際量測面積佔比；「目視覆蓋 $<$ 魚身 1/4」等數字係人眼估計的參考分界，而非可重現的像素級量測。配合各等級範例圖（圖 \ref{fig:grade-a} 至圖 \ref{fig:grade-f}），可提升單一標注者在整批資料中的前後一致性；但這僅為內部一致性（intra-rater reliability）之緩解措施，無法取代多人標注的人際一致性（inter-rater reliability）驗證。

需特別說明的是，本研究現階段無法取得第二位以上標注者重新標注資料，因此無法計算 Cohen's Kappa、Fleiss' Kappa 或人類基準表現。故本文所有模型準確率皆應解讀為「相對於本研究固定標注準則與單一標注者標籤之表現」，而非「相對多人共識品質標準之表現」。本研究可主張的是：模型能學習並重現此套固定分級準則，用於降低批量檢查負擔與提供人工複核輔助；但不宣稱已完全消除人工主觀差異。

為降低單一標注者帶來的系統性偏差，本研究採取以下最低限度緩解措施：（1）標注前制定含量化覆蓋比例區間的書面評分準則（第 \ref{sec:method-grading} 節），並配合各等級實體範例圖，提升標注前後一致性；（2）標注中對邊界樣本（尤其 A/B 與 C/D 邊界）先以邊界框輔助確認覆蓋範圍，再決定等級；（3）標注完成後進行全批次回視，對與準則不一致者重新標注。上述措施雖能提升單一標注者的內部一致性（intra-rater reliability），但無法取代多人標注所能提供的人際一致性（inter-rater reliability）驗證；後者列為後續研究之優先任務（詳見第 \ref{sec:conclusion-future} 節）。

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
4. **與相近研究之可比較性**：ResNet18 為小資料瑕疵檢測之常用基準，EfficientNet-B0 為近年主流輕量模型代表，三者並列可同時涵蓋「移動端最佳化」「殘差網路經典」「複合縮放最佳化」三條設計哲學，為後續研究者提供可比較之基準模型。方法路線（有監督分類 vs. 異常偵測）之選擇依據詳見第 \ref{sec:literature-cv-dl} 節。

本研究兩組設定（簡化與完整）均採用**全層微調（Full Fine-tuning）**策略---骨幹所有層均參與梯度更新，而非僅訓練新增的分類頭。在 1110 張資料規模下，全層微調的過擬合風險主要透過 Dropout、資料增強與正則化損失控制；特徵提取（Feature Extraction，凍結骨幹）策略未在本研究探索。**此為一項重要的方法論空缺**：在小樣本遷移學習場景中，凍結骨幹只訓練分類頭（特徵提取）是更保守的起始策略，可減少過擬合風險並加快訓練；理想的實驗設計應比較「全層微調」與「特徵提取」乃至「漸進解凍（Progressive Unfreezing）」三種策略，本研究僅探索全層微調，使得遷移學習策略選擇缺乏對照依據。後續研究建議補充此比較，尤其在資料量擴充之前，特徵提取策略可能提供更穩定的基準。

選擇之 trade-off 在於：未涵蓋 Vision Transformer 系列（如 ViT-Tiny、DeiT-Tiny）、ConvNeXt 系列等新架構，亦未探討 self-supervised pre-training（如 DINO、MAE）對小樣本任務之助益，此屬本研究範圍限制。

#### 雙輸出架構 {#sec:method-model-dualhead}

本研究採用 MobileNetV3-Large[@howardSearchingMobileNetV32019]（ImageNet V2 預訓練）作為骨幹網路，以遷移學習方式進行六分類微調。模型的特徵提取路徑為：backbone features 模組 → AdaptiveAvgPool → Flatten → classifier 前三層（Linear(960→1280) + Hardswish + Dropout(0.2)），輸出 1280 維特徵向量。在此 1280 維特徵向量之上接兩個並行輸出頭：

**分類頭**：Dropout（$p = 0.4$）→ Linear(1280→6)，輸出六類 logits。

**品質評分輔助頭**：Dropout（$p = 0.2$）→ Linear(1280→64) → ReLU → Linear(64→1) → Sigmoid，輸出範圍 0 至 1 的連續品質分，乘以 100 即得 0 至 100 分。

訓練時分類頭與評分頭同步優化。需特別說明的是，現行品質分輔助頭以「等級編號之線性轉換」（A=1.0, B=0.8, \ldots, F=0.0）作為迴歸目標（$\text{score\_gt} = 1 - \text{label} / 5$），**隱含假設等級間距相等且 ordinal 關係由 MSE loss 隱式建模**；然而此等距假設在感知品質層面已知不成立且偏差方向可預測：A→B（幾乎無拉絲至 1～2 根短絲）的感知品質差異，未必等同於 E→F（大量拉絲至結構幾乎難以辨識）的差異；主觀品質曲線在嚴重端（D/E/F）通常較為陡峭，在輕微端（A/B/C）較為平緩，因此等距假設將系統性低估嚴重端的相對品質退化。此偏差在缺乏多人連續評分校準資料的條件下無法量化，但結果章中 B 等級品質分偏高（89.0 vs 目標 80）、D 等級偏高（54.5 vs 目標 40）的現象將部分反映此設計局限（詳見第 \ref{sec:results-quality-score} 節）。**更根本的問題是**：品質分輔助頭的輸出幾乎是分類頭 softmax 結果的線性重映射，並不具備獨立於分類頭的品質評估能力——模型的「品質分」只是分類決策的另一種呈現方式，而非從品質本身學習得出的獨立數值。若研究目標包含輸出具有絕對意義的品質分數，應招募多位有經驗的操作人員對全部樣本進行主觀連續評分，以此作為監督目標重新訓練評分頭；本研究的品質分僅能作為分類結果的輔助排序工具，不宜賦予超出此範疇的解讀。此外，Mixup 啟用時，評分監督目標 $\text{score\_gt}$ 僅以混合前第一個樣本的標籤（$y_a$）計算，未對第二個樣本標籤（$y_b$）做線性插值，可能在跨等級混合樣本上引入輕微監督不一致。嚴格而言，本研究將 ordinal classification 任務以「nominal classification + auxiliary regression」近似處理，未採用 ordinal-aware loss（如 CORAL [@caoRankConsistentOrdinal2020]、CORN [@shiDeepNeuralNetworks2023]）或 ordinal regularization。

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

\noindent 其中 $L_{\text{full}}$ 對應完整設定，$L_{\text{plain}}$ 對應簡化設定。係數 0.3 為經驗設定：初步實驗中 $L_{\text{Focal}}$ 與 $L_{\text{MSE}}$ 在訓練初期量級相近（均在 0.5$\sim$2.0 區間），0.3 使評分輔助頭提供穩定梯度而不壓過分類損失；若兩損失量級差異較大，此係數應重新調整。Mixup 啟用時，Focal Loss 以混合比例 $\lambda$ 線性組合兩個硬標籤的 CE，再套用焦點加權 $(1-p_t)^\gamma$，其中 $p_t = \exp(-(\lambda \cdot \text{CE}_a + (1-\lambda) \cdot \text{CE}_b))$；此做法等效於 MixFocal，在技術上偏離 Focal Loss 的原始設計（針對固定硬標籤），屬本研究之簡化取捨。此外，Mixup 應用於序數分類任務存在一項**物理意義問題**：將 A 等級（無拉絲）與 F 等級（廢品）以 $\lambda=0.5$ 線性混合，產生的混合標籤 0.5（即名目上的「中等拉絲」）在視覺上並不對應任何真實的拉絲狀態，因為兩張影像的像素均值並不等同於中度拉絲的影像紋理；在名目分類設定下，此混合標籤對模型施加的是「同時學習 A 和 F 特徵的混淆信號」，可能干擾相鄰等級邊界（如 B/C、D/E）的學習。Mixup 的設計初衷是針對名目分類任務的 over-confidence 問題，並非針對序數等級分布的平滑；在序數分類場景下使用 Mixup，效益有限且潛在副作用不可預測，此為本研究完整設定的已知方法取捨，相關效果以第 \ref{sec:results-supplemental-ablation} 節消融（移除 Mixup 後 accuracy 降 4.17 pp，但為 seed=7 單次診斷）作為參考。另需說明，完整設定同時啟用 Focal Loss 與 Label Smoothing 存在一項理論張力：Focal Loss 的加權因子 $(1-p_t)^\gamma$ 依賴模型對正確類別的預測機率 $p_t$---$p_t$ 愈高代表該樣本愈「容易」，Focal Loss 降低其損失權重，使訓練聚焦於困難樣本；但 Label Smoothing 將目標由硬標籤 1.0 軟化至 $1-\epsilon=0.9$，在訓練過程中人為限制了 $p_t$ 的上限，使模型即便對多數類別預測「幾乎確定」時，也因目標被軟化而無法觸發 Focal Loss 應有的強降權，實質上削弱了 Hard Example Mining 的效果。本研究未對「FL only」、「LS only」與「FL+LS」進行單獨消融，無法量化此組合是否優於單獨使用任一機制。理想的實驗設計應事先設計「3 策略 × 2 架構」的完整因子消融，以分離各損失元件的獨立效果；此設計層面之不足為本研究的已知方法局限，後續研究建議補足此項因子消融（見第 \ref{sec:conclusion-future} 節建議 2）。

**重要警示——兩設定之比較在研究設計層面即已失效**：完整設定啟用 WeightedRandomSampler（`num_samples=774×6=4644`），每 epoch 執行約 145 步；簡化設定未啟用，每 epoch 僅約 24 步。名義上同為 25 epoch 訓練，完整設定等效梯度更新步數約為簡化設定的 **6 倍**。此意味本研究的「完整設定 vs 簡化設定」消融比較存在根本性的設計缺陷：兩設定之間任何觀察到的效能差異，同時混入「損失函數與增強策略差異」與「累積訓練量 6 倍差異」兩個無法分離的因素，**任何差異均無法單獨歸因於策略優劣**。正確的消融設計應固定等效 gradient steps 而非 epoch 數，使兩設定在相同計算預算下比較；本研究受限於研究資源未能重新設計此比較，讀者解讀第 \ref{sec:results-supplemental-ablation} 節消融結果時，應將此設計缺陷列為首要保留，所有觀察到的差異方向均不可視為策略本身的效果。**此缺陷的實質後果是**：本研究呈現的「完整設定 vs 簡化設定」比較在策略評比意義上是空的——結果數字是真實量測值，但任何差異均可完全由訓練量差異解釋，無法支持任何策略優劣結論。第 \ref{sec:results-supplemental-ablation} 節呈現此比較，僅作為完整實驗紀錄與「差異確實可觀察到」的事實記錄，不應引申為策略評估依據。相關結論以五 seed 統計而非單次結果為準（詳見第 \ref{sec:results-supplemental-multiseed} 節）。

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
學習率排程 & \makecell{CosineAnnealing\\WarmRestarts} & \makecell{$T_0=20$, $T_{\text{mult}}=2$\\$\eta_{\min}=10^{-6}$；\\25 epoch 內僅完成\\首次餘弦衰減與\\epoch 20 的 warm restart\\（第二個週期需 epoch 60\\完成，訓練上限 25 epoch\\使其未發揮多次重啟設計）} \\
Dropout & \makecell{分類頭 $p=0.4$\\評分頭 $p=0.2$} & \makecell{兩組\\共用} \\
訓練精度 & FP16 Mixed Precision & GPU 加速 \\
\hline
\end{tabular}
\end{table}

各項共用超參數之設定依據說明如下：初始學習率 $2\times10^{-4}$ 參考 MobileNetV3 在小樣本遷移學習場景下常用的 AdamW 範圍（$10^{-4}$ 至 $5\times10^{-4}$），並透過前導訓練確認驗證損失穩定下降；Weight Decay $3\times10^{-4}$ 為 AdamW 常用預設值；批次大小 32 受限於 4 GB VRAM；Dropout（分類頭 0.4、評分頭 0.2）以前導實驗中驗證損失趨勢確認未出現明顯過擬合。MSE 損失係數 0.3 依初步實驗中 $L_{\text{Focal}}$ 與 $L_{\text{MSE}}$ 在訓練初期量級相近（均約 0.5–2.0）而設定，使評分頭提供穩定梯度而不壓過分類損失。需說明的是，本研究未進行系統性超參數搜索（如 grid search 或 Bayesian optimization），上述設定以可重現的前導觀察為依據，但最優值未經嚴格驗證；此為本研究方法設計之已知局限。

**CosineAnnealingWarmRestarts 設定錯誤**：表 \ref{tab:hyperparameters} 中 $T_0=20$, $T_\text{mult}=2$ 的設置意味第二個重啟週期需等到 epoch 40–60 才能完成，而本研究訓練上限為 25 epoch，因此 25 epoch 內僅完成首次餘弦衰減與 epoch 20 的一次重啟，多週期重啟的設計意圖從未發揮。正確的選擇應為適合 25 epoch 的單週期排程（如 $T_0=25$ 的單次餘弦衰減，或固定 LR + step decay）。此設定錯誤使得學習率在 25 epoch 內的衰減行為等同於「$T_0=25$ 單週期餘弦」而非「多次重啟」，雖對訓練有效性的影響有限（單次餘弦衰減本身是合理策略），但應明確記錄為設計失誤而非有意選擇，避免後續研究者誤以為多次重啟是本研究的有效做法。

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

## 整批自動化處理流程設計 {#sec:method-batch-pipeline}

本研究以 Python 腳本實作由原始照片到品質等級報告的端對端離線處理流程，整體分為三個模組：

1. **影像裁切模組**：讀取拍攝完成的原始照片，依固定 2$\times$3 網格對每張照片自動裁切出 6 支魚骨，並統一縮放為 224$\times$224 pixels 存入暫存目錄，作為推論輸入。
2. **批次推論模組**：載入訓練完成之 MobileNetV3-Large 模型權重，依序讀取裁切圖，以 batch\_size=1 逐張送入 GPU 進行前向推論，輸出各等級 softmax 機率、argmax 預測等級（A–F）及品質分輔助頭數值（0–100 分），並依等級分別存入對應子目錄。
3. **報告輸出模組**：彙整推論結果，產生 HTML 可視化報告，內含各等級樣本縮圖、整批分級分布統計圖與低 confidence 樣本清單（confidence $< 0.7$ 者標示為建議人工複核），供操作人員快速瀏覽整批品質狀態。

模型前向延遲量測結果詳見第 \ref{sec:results-batch} 節。需特別指出，上述量測數字為純模型推論時間，不含影像讀取與 HTML 報告生成等前後處理耗時；評估實際端到端吞吐量時應一併計入前後處理。

# 實驗結果與分析 {#sec:results}

## 結果解讀框架：三項根本限制的優先聲明 {#sec:results-framework}

在呈現任何數字之前，需先確立三項根本限制，以確保讀者在正確的前提下解讀所有結果：

**限制一（標注效度）**：全部 1110 張樣本由單一標注者完成，多人標注一致性（Cohen's Kappa）未驗證。本章所有 accuracy、F1 與 QWK 數字，反映的是「模型複製一位標注者判斷的能力」，不代表「正確辨識客觀品質等級的能力」；兩者可能存在顯著差距，且在驗證完成前無法量化。

**限制二（統計效力）**：正式多 seed 比較共 n=5，對中等效應量（Cohen's d ≈ 0.5）的統計效力低於 0.3，任何「p 值」均無法可靠反映真實效應。本章不報告具體 p 值，所有模型間差異均定位為探索性觀察，不作為確定結論。

**限制三（混淆變因）**：PLA 顏色批次間未受控、拍攝條件未固定，模型是否確實依賴拉絲紋理特徵目前僅有定性 Grad-CAM 排查，無量化驗證；部分效能數字可能反映顏色或光線特徵而非拉絲辨識能力。

以上三項限制在本章每一個數字解讀時均隱含成立，不再逐一重複標注。

## 資料集統計分析 {#sec:results-dataset}

本研究有效樣本共 1110 張，依品質等級分布如表 \ref{tab:dataset-dist} 及圖 \ref{fig:dataset-dist} 所示。A 等級（完美品）佔比最高，共 546 張；B 級 87 張、C 級 213 張、D 級 160 張、E 級 72 張、F 級 32 張。此分布反映資料仍具明顯類別不平衡，尤其 B、E、F 等級樣本數偏少，因此後續結果需同時參照 macro-F1、QWK、跨等級誤判與各等級 support，而不能只看整體 accuracy。需特別指出，**多數類別基準分類器**（恆預測 A 等級，無需任何學習）在本研究資料分布下之整體 accuracy 約為 **49.2\%**（A 等級樣本佔比）；本研究所有模型的五 seed 平均 accuracy 約 80–81\%，較此基準高出約 **31 個百分點**，顯示模型確實學習到超越多數類別猜測的辨識能力。然而，多數類別基準之 macro-F1 約為 0.11（僅 A 等級有非零 F1），而本研究模型之 macro-F1 約 0.66–0.71，兩者差距在少數類別辨識上更為顯著。所有模型效能比較均應在此基準脈絡下解讀。

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

表 \ref{tab:seed7-results} 整理 seed=7、同一 Group Split 測試集下四組主要模型 / 設定之結果。此處的最佳單次結果為 MobileNetV3-Large 完整設定，accuracy 為 89.88\%（151/168）；但此僅代表單一 seed 與單一切分下的結果，不能直接視為穩定最佳模型。此外，完整設定因 WeightedRandomSampler 每 epoch 訓練步數（145 步）約為簡化設定（24 步）的六倍，兩者在 seed=7 上的差距（89.88\% vs 86.31\%）同時反映訓練策略差異與累積計算量差異，無法單獨歸因於策略優劣；相關說明詳見第 \ref{sec:results-supplemental-ablation} 節。

由於 seed=7 測試集中 B、E、F 等級分別只有 16、8、4 張，少數類別的 precision、recall 與 macro-F1 容易受到少量樣本變動影響。因此，本節將 seed=7 視為可檢查混淆矩陣、校準與視覺化的詳細案例；真正的模型 / 策略排序仍以五 seed 平均與配對檢定為主要依據。

\begin{table}[H]
\centering
\caption{seed=7 主要模型 / 設定於同一 Group Split 測試集之結果（seed=7 單次案例；MobileNetV3-Large 完整 vs 簡化之差異同時包含「策略差異」與「累積訓練量約 6 倍差異」兩項因素，無法單獨歸因；穩定性判斷以表 \ref{tab:multiseed-results} 五 seed 結果為準）}
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
多數類別基準$^{\ddagger}$ & $\approx$49.2\% & $\approx$0.11 & — & — & — \\
\hline
\end{tabular}
\end{adjustbox}
\TableNote{$^{\ddagger}$ 多數類別基準：恆預測 A 等級（多數類別），無需任何學習；accuracy = A 等級佔比 ≈ 49.2\%，macro-F1 ≈ 0.11（僅 A 等級有非零 F1，其餘等級 F1 = 0），QWK 與跨等級誤判率在此設定下無意義（以「—」標示）。所有模型效能均須在超越此基準的脈絡下解讀。}
\end{table}

表 \ref{tab:seed7-perclass} 為 MobileNetV3-Large 簡化設定於 seed=7 測試集之各等級精確率、召回率與 F1 分數。需先說明，此各等級分析**僅來自 seed=7 單次切分**，不同 seed 下 B/E/F 等少數類別的 support 差異可能使各等級 P/R/F1 數值大幅波動，本研究未補充五 seed 平均之各等級統計；讀者解讀以下數值時，應視為「seed=7 一例之觀察」而非跨 seed 穩定結論。

**\textcolor{red}{【關鍵瓶頸】B 等級召回率僅 56.3\%（9/16），為六等級中最低，亦是本系統最重要的實用限制}**：5 張 B 等級樣本被誤判為 A 等級（有輕微瑕疵的良好品被誤標為完美品）。從品質管控的風險角度評估：約 44\% 的 B 等級產品（有 1～2 根短細絲的輕微瑕疵品）會被系統自動標為完美品，在對外觀有要求的應用場合，這意味近半數輕微瑕疵品可能流入後續工序而未被攔截。此方向誤判（漏判瑕疵）在品質管控中通常比誤報（將良品標為瑕疵品）的代價更高，因為漏判的後果是瑕疵品到達終端使用者。這一瓶頸與第 \ref{sec:results-quality-score} 節 B 等級品質分偏高（89.0 分 vs 目標 80 分）的觀察相互印證，且不能僅靠更換模型解決——其根本原因是 A/B 邊界在視覺上模糊（1～2 根短細絲在不同拍攝角度和光線下可能看不清楚）以及單一標注者標注一致性未驗證，這是資料品質問題，而非單純的模型能力問題。針對此弱點，一個初步的改善方向是**降低 B 等級的預測閾值**（即以 softmax P(B) + P(C) + ... + P(F) $>$ 某個低閾值來觸發「非完美品」警示），但此方向需以具人工標籤的獨立測試集重新評估，本研究未能在當前資料條件下實施。C/D 邊界混淆同樣顯著（C→D 有 7/35、D→C 有 2/28）；D→A 出現 2 次跨等級誤判，可能與特定拍攝角度下拉絲特徵被遮蔽有關。E、F 各 8、4 張，統計解讀須謹慎。

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

\par\noindent\small\textit{\textbf{$^{\dagger}$ E（Support=8）與 F（Support=4）兩列數字不具統計意義，不應列入效能比較：F 等級任一張誤判即造成 Recall 變動 25\%，所呈現之 P/R/F1 值完全由少數幾個隨機樣本決定；讀者應忽略此兩列數值，僅參考 Support $\geq 16$ 之等級（A、B、C、D）進行效能解讀。其餘觀察：B 等級召回率（56.3\%）為有效等級中最低，5 張誤判均流向 A 等級；D 等級有 2 張跳至 A（跨等級大跳）。}}

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
\caption{五個 seed 之 Group Split 測試表現（mean $\pm$ std, n=5；MobileNetV3-Large 簡化與 EfficientNet-B0 完整之 accuracy 均為 81.19\%，係兩者精確值相同（均為 81.1905\%），並非四捨五入巧合）}
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
多數類別基準$^{\dagger}$ & $\approx$49.2\% & $\approx$0.11 & — & — & — \\
\hline
\end{tabular}
\end{adjustbox}
\TableNote{精確至小數點後 4 位：MobileNetV3-Large 簡化與 EfficientNet-B0 完整之 mean accuracy 均為 81.1905\%，依實驗紀錄兩者精確值完全相同，並非四捨五入巧合；可區分之指標為 std（MobileNetV3-Large 簡化 3.71\%、EfficientNet-B0 完整 2.25\%）。$^{\dagger}$ 多數類別基準（恆預測 A 等級）：accuracy ≈ 49.2\%，macro-F1 ≈ 0.11；四組模型均較此基準高出約 31 個百分點。}
\end{table}

表 \ref{tab:multiseed-results} 結果中需特別指出 **MobileNetV3-Large 完整設定的不穩定性**：其 accuracy std 為 **5.98\%**，為四組中最大，約為 EfficientNet-B0 完整（2.25\%）與 ResNet18 完整（2.16\%）的 2.6 倍以上；macro-F1 與 QWK 之 std 亦同步偏高（分別為 0.070 與 0.039）。此高方差有其結構性原因：WeightedRandomSampler 在不同 seed 切分下，少數類別（B/E/F）進入訓練集的原圖群組數量差異較大，當訓練集的 E 或 F 原圖群組數量少時，WeightedSampler 對這些類別的過採樣比例大幅增加，可能導致訓練信號不穩定；加以 Focal Loss 對低信心樣本的梯度放大效應，在少數類別分布差異大的不同切分下，訓練動態的 seed 間差異比僅用 Cross Entropy 的設定更為顯著。在 1110 張小樣本資料規模下，此訓練動態不穩定性使完整設定對 Group Split 切分結果（即少數類別進入哪個 split）高度敏感。儘管完整設定在 seed=7 達 89.88\%（為四組中該 seed 之最高），五 seed 平均卻是四組中最低（80.12\%），這代表 seed=7 之高分主要反映「該次切分剛好對完整設定有利」，而非策略本身穩定優越。在工業部署情境下，實際部署只會看到單次訓練結果；完整設定同時落入「平均最低」與「方差最大」兩種劣勢，意味即便偶然抽到 seed=7 級別之高分，其平均期望仍不及其他三組；因此後續對完整設定之解讀，應將高方差視為負面訊號而非優勢。

以 MobileNetV3-Large 簡化設定作為比較基準之 paired t-test 如表 \ref{tab:paired-ttest} 所示。五 seed 結果顯示，其他模型 / 設定相對於簡化設定之 accuracy 與 QWK 差異皆未達統計顯著。需就統計推論的有效性提出兩點根本性警語：（1）**檢定 power 嚴重不足**：n=5 之 paired t-test 對中等效應量（Cohen's d ≈ 0.5）的 power 通常低於 0.3，在此條件下，任何「p 值」的大小均不能可靠地反映真實效應是否存在；「未達顯著」**不可解讀為「兩設定等效」**，「接近顯著」同樣不可解讀為「趨勢存在」，僅能說明在此樣本量下無法區分。（2）**多重比較問題**：本研究進行 3 個模型 × 3 個指標（Accuracy / Macro-F1 / QWK）共 9 個 t-test，即使個別比較觀察到任何 p 值偏小的情形，在 Bonferroni 校正（$\alpha_{\text{corrected}} = 0.05/9 \approx 0.0056$）後均不達顯著門檻。基於上述統計效力根本不足，本研究**不報告具體 p 值以避免誤導**，而改以「五 seed 平均值與 std」作為主要呈現方式，輔以「accuracy 與 QWK 未同步支持、完整設定 std 偏大」兩項觀察。綜上，本文**不宣稱任何單一設定為穩定最佳模型**，並將所有模型 / 策略差異定位為待後續更大樣本研究確認的探索性現象。

**ResNet18 / MobileNet 完整之 macro-F1 較簡化設定略高之可能解釋與骨幹選擇之取捨**：五 seed 結果中 ResNet18 完整之 macro-F1 平均（0.712）與 MobileNetV3-Large 完整（0.713）相當，皆略高於 MobileNetV3-Large 簡化（0.661）。一個可能的結構性解釋是 ResNet18 之參數量（約 11.7M）為 MobileNetV3-Large（約 5.4M）的兩倍以上，在 1110 張資料規模下對 B、E、F 等少數類別可能具有較強的記憶能力，因而提升 macro-F1。然而：（1）如前所述，n=5 之統計效力嚴重不足，此 macro-F1 差異無法透過統計檢定可靠區分，屬探索性觀察而非確立結論；（2）ResNet18 之 FLOPs（約 1.8 GFLOPs）為 MobileNetV3-Large（約 219 MFLOPs）的 8 倍以上，部署成本顯著較高，與本研究納入「未來邊緣部署彈性」之骨幹選擇考量（見第 \ref{sec:method-model-rationale} 節）相衝突。綜合此兩項考量，本研究仍以 MobileNetV3-Large 為主要骨幹；但承認若後續研究以「最大化 macro-F1」為單一目標、且不受部署成本限制，則 ResNet18 之表現值得以更大樣本與多 seed 進一步驗證。

\begin{table}[H]
\centering
\caption{相對 MobileNetV3-Large 簡化之五 seed 指標差異（n=5；因統計效力嚴重不足，本表不報告 $p$ 值，以避免數字誤導；差異方向僅供觀察，不作推論）}
\label{tab:paired-ttest}
\footnotesize
\setlength{\tabcolsep}{3pt}
\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{lccc}
\hline
\textbf{比較模型} & \makecell{\textbf{Accuracy}\\\textbf{差異（pp）}} & \makecell{\textbf{Macro-F1}\\\textbf{差異}} & \makecell{\textbf{QWK}\\\textbf{差異}} \\
\hline
EfficientNet-B0 完整 & 0.00 & +0.038 & $-$0.011 \\
MobileNetV3-Large 完整 & $-$1.07 & +0.052 & $-$0.011 \\
ResNet18 完整 & $-$0.36 & +0.052 & $-$0.006 \\
\hline
\end{tabular}
\end{adjustbox}
\TableNote{n=5 下 paired t-test 對中等效應量之統計效力低於 0.3，任何 p 值均無法可靠推論；9 個比較的 Bonferroni 校正門檻為 0.0056，所有比較均不達顯著。差異方向僅作探索性觀察，不排除機會誤差。}
\end{table}

## seed=7 單變因消融與 100 epoch 檢查 {#sec:results-supplemental-ablation}

表 \ref{tab:ablation-results} 整理 seed=7 下之消融與 100 epoch 檢查。每列「移除 X」代表**僅移除 X，其餘訓練元件（Focal Loss、Label Smoothing、Mixup、Weighted Sampler）均保留**；例如「移除 Focal Loss」仍保有 Label Smoothing、Mixup 與 Weighted Sampler。此表用來診斷完整策略中各訓練元件的影響，但因僅有單一 seed，不能作為穩定性結論。從此單次結果觀察各元件移除後的 accuracy 降幅：Label Smoothing 移除後降 1.78 pp（89.88\% → 88.10\%）、Focal Loss 移除後降 3.57 pp（89.88\% → 86.31\%）、Mixup 移除後降 4.17 pp（89.88\% → 85.71\%）、Weighted Sampler 移除後降 6.55 pp（89.88\% → 83.33\%）。在此 seed=7 單次案例中，Label Smoothing 的邊際貢獻最小，Weighted Sampler 的影響最大（且移除後跨等級誤判從 1.19\% 上升至 4.17\%）；惟此排序僅為 seed=7 診斷觀察，不能推論所有 seed 皆如此。

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

\par\noindent\small\textit{正式五 seed 比較與 seed=7 單變因消融皆依實驗計畫使用 25 epoch、patience=7；僅 MobileNetV3-Large 簡化設定另做 100 epoch、patience=35 檢查，用來觀察較長訓練預算下結果是否改變。}

## 品質分數與全資料回測 {#sec:results-quality-score}

MobileNetV3-Large 簡化設定之品質分輔助頭以 A=100、B=80、C=60、D=40、E=20、F=0 作為監督目標。表 \ref{tab:plain-quality-score} 依實驗紀錄整理 seed=7 Group Split 測試集與全資料回測之各等級平均分。測試集與全資料回測皆呈 A \(>\) B \(>\) C \(>\) D \(>\) E \(>\) F 的單調排序，可作為分類結果之外的輔助排序訊號。

需特別說明的是，B（偏高 9 分）、D（偏高 14.5 分）、F（偏高 12.5 分）等級的品質分偏差，**本質上是分類誤判的副作用而非品質分輔助頭獨立學習的偏誤**：B 等級偏高係因 5 張被誤判為 A 的樣本輸出接近 100 分，拉高 B 的預測均分；D 等級偏高係因部分 D 被誤判為 C 而輸出 60 分附近，使 D 均分上移。品質分輔助頭的輸出幾乎是分類頭 softmax 結果的線性重映射，不具備獨立於分類頭的品質評估能力；其主要應用價值在於提供可用於排序的連續數值，而非作為絕對品質量化指標，此定位與第 \ref{sec:method-model-dualhead} 節的設計說明一致。

\begin{table}[H]
\centering
\caption{MobileNetV3-Large 簡化設定品質分對照（測試集 168 張 vs 全資料回測 1110 張之平均品質分）}
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

\par\noindent\small\textit{測試集平均分來自 seed=7 Group Split 測試紀錄（無原圖洩漏）；\textsuperscript{$\ddagger$} 全資料回測為 1110 張樣本（\textbf{包含 774 張訓練集樣本}）之回測平均分，僅供觀察模型對已標注資料之擬合與品質分排序，不可作為泛化能力指標；原列之「全資料回測 Recall」欄因同樣理由可預期偏高（A 級即達 1.000），資訊價值低且易誤導，已自此表移除。}

此 seed=7 Group Split MobileNetV3-Large 簡化設定模型回測全部 1110 張樣本之整體準確率為 87.30\%（969/1110），macro-F1 為 0.779。**警告：此數字包含 774 張訓練集樣本，對訓練資料的高準確率是過擬合（memorization）的預期行為，不代表任何泛化能力。** 唯一具有泛化意義的數字是 Group Split 測試集（168 張，原圖零重疊）上的結果；全資料回測結果僅用於確認整批推論管線可正常執行，讀者不應將 87.30\% 與測試集的 86.31\% 進行任何比較或引申。

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

**Grad-CAM 視覺解釋**：圖 \ref{fig:gradcam-correct} 與圖 \ref{fig:gradcam-wrong} 分別為預測正確與預測錯誤樣本的 Grad-CAM 熱力圖。本研究以手動掛載 forward/backward hook 的方式，對 MobileNetV3-Large features 模組末段最後一個 InvertedResidual Block 之卷積輸出執行 Grad-CAM；熱力圖以 Jet colormap 生成後依 $0.55 \times \text{原圖} + 0.45 \times \text{熱力圖}$ 疊加顯示。展示樣本以固定亂數種子值（seed=7）從各等級正確或錯誤預測樣本中隨機抽取一張，確保選取過程可重現且排除人工挑選的確認性偏誤（confirmation bias）；由於每等級僅展示一張，不能代表該等級所有正確或錯誤預測的典型行為，讀者應以整體混淆矩陣與召回率數字為主要判斷依據，**Grad-CAM 僅提供個案定性參考，不能作為量化驗證**。

需特別強調，本研究未對熱力圖進行任何量化分析（如計算熱力圖高激活區域與人工標注拉絲區域的重疊 IoU），因此以下描述均為目視觀察，存在嚴重的確認性偏誤（confirmation bias）風險。**Grad-CAM 的根本局限性在於**：（1）人眼在看到「熱力圖高亮於魚骨間隙」時，傾向於詮釋為「模型正確依賴拉絲特徵」，但熱力圖高亮只表示「此區域對最終預測梯度較大」，不能排除同時依賴邊緣輪廓、顏色或背景等特徵；（2）本研究 PLA 顏色未受控，若顏色與等級共現，顏色分布本身也可能在間隙區域產生高梯度；（3）未進行「遮蔽拉絲區域後觀察 accuracy 變化」的受控消融，無法確認模型對拉絲紋理的依賴性。**因此，本節 Grad-CAM 分析不能作為「模型確實學習拉絲特徵」的任何形式的證據**，只能作為「無明顯異常」的最低限度 sanity check。欲驗證模型決策機制，需以人工標注的拉絲分割遮罩計算 IoU 或執行遮蔽實驗，本研究無法提供此層級的驗證。

\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth,height=0.55\textheight,keepaspectratio]{images/gradcam-correct-grid.png}
\caption{預測正確樣本 Grad-CAM 熱力圖（定性觀察：部分樣本高亮區域看似集中於魚骨間隙，未經 IoU 量化驗證）}
\label{fig:gradcam-correct}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth,height=0.55\textheight,keepaspectratio]{images/gradcam-wrong-grid.png}
\caption{預測錯誤樣本 Grad-CAM 熱力圖（定性觀察：熱力相對分散，多為相鄰等級邊界樣本，未經量化驗證）}
\label{fig:gradcam-wrong}
\end{figure}

**t-SNE 特徵可視化**：圖 \ref{fig:tsne} 為 seed=7 測試集（168 張）之 1280 維特徵向量以 t-SNE（perplexity=30，亂數種子值=7，以 PCA 初始化）降維後的散佈圖。A 等級（無拉絲）形成緊密且獨立的聚落；C/D 等級部分樣本邊界相互滲透，與混淆矩陣中 C/D 誤判率較高的現象一致；B 等級聚落與 A 等級部分重疊，解釋了 5 張 B 等級樣本被誤判為 A 的現象。E/F 等級因樣本數過少（各 8/4 張），聚落位置解讀需謹慎。整體而言，特徵空間已形成具意義的等級區隔，但相鄰等級存在相互滲透的邊界區域，符合序數分類任務中等級邊界天然模糊的特性。

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth,height=0.62\textheight,keepaspectratio]{images/tsne-test-features.png}
\caption{seed=7 測試集 1280 維特徵之 t-SNE 視覺化（perplexity=30，168 個樣本，顏色對應 A 至 F 等級）}
\label{fig:tsne}
\end{figure}

## 外部未標注影像診斷 {#sec:results-supplemental-ood}

外部未標注資料共 105 張照片，裁切為 630 支魚骨後進行推論，作為模型輸出是否崩潰的 sanity check。由於此批資料**缺乏人工標籤，本節無法計算任何準確率或召回率**，科學價值極為有限：唯一可確認的事實是「模型輸出未全部集中於單一類別」，此為可部署性的最低必要條件，遠非充分條件。預測分布（A/B/C/D/E/F = 417/14/82/75/30/12）無法區分「外部良品比例確實較高」與「高信心誤判大量非 A 樣本為 A」兩種截然不同的解釋；平均 confidence 0.919 亦不代表預測正確，因高信心誤判在類別不平衡場景下相當常見。本節結果**不能支持任何關於模型泛化能力的推論**，亦不能引用為「模型在外部資料上表現良好」的任何形式的支持。此批資料的唯一正確處置方式是補拍人工標籤後計算定量指標（詳見第 \ref{sec:conclusion-future} 節建議 1）；在此之前，本節僅記錄「模型未崩潰、輸出分布多元」這一單一事實，讀者應忽略此節中的所有具體數字，因其缺乏解釋依據。

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth,height=0.5\textheight,keepaspectratio]{images/external-unlabeled-distribution.png}
\caption{外部未標注 630 支魚骨推論之等級分布（無人工標籤，僅作 sanity check；A 等級佔 66.2\%）}
\label{fig:external-dist}
\end{figure}

## 整批處理流程之推論延遲量測 {#sec:results-batch}

以 seed=7 MobileNetV3-Large 簡化模型於 168 張測試樣本量測，平均單張模型推論時間為 6.90 ms，約 144.9 張/秒；完整 Group Split 模型約 7.05 ms，約 141.8 張/秒（兩者之 0.15 ms 差異屬量測雜訊範圍，且兩設定之比較另受訓練量不對等影響，不應據以判斷哪一設定推論較快）。需特別說明量測條件：推論以 \textbf{batch\_size=1} 逐張送入 GPU，影像張量\textbf{預先載入記憶體}（量測時不含磁碟讀取、裁切、resize/normalize 等前處理耗時），並以 20 張 warm-up 後計時 168 張；所呈現數字為\textbf{純模型前向傳播延遲}，不代表含完整前處理的端到端吞吐量。實際部署場景中，前處理（影像讀取、裁切）與後處理（分級排序、報告生成）的耗時可能與推論本身相當，評估系統吞吐量時應一併納入。此結果僅顯示「單機 GPU 上純模型前向延遲屬毫秒級」此一部署參考事實，**不應引申為「整批照片自動處理流程已具備產線吞吐量」**；實際部署仍需額外評估資料讀取、裁切、人工複核與現場設備整合成本。

# 結論與建議 {#sec:conclusion}

## 結論 {#sec:conclusion-summary}

本研究建立了一套以深度學習影像辨識為核心的 3D 列印件拉絲瑕疵輔助辨識與品質評分原型，以 FDM 列印魚骨件為研究標的，完成六等級（A 至 F）分類與品質評分輸出流程。主要研究成果總結如下：

1. **單一標注者下之可重複品質等級制度**：以目視估計拉絲覆蓋比例為主要判斷依據，建立六個品質等級定義並配合 A 至 F 範例圖。本研究主張的是「模型在嚴格測試集上可部分逼近此套固定標注準則」，可降低批量檢查負擔並提供人工複核輔助；惟全部樣本由單一標注者完成、尚未進行多人一致性測試，故不宣稱已建立多人共識下的品質標準（標注一致性限制詳見第 \ref{sec:method-grading} 節）。
2. **系統性資料蒐集與標注**：透過多批次列印與拍攝，配合 Label Studio 工具完成全部樣本的人工標注，建立含 1110 張有效樣本、185 個原圖群組的六等級分類資料集；以原圖層級 Group Split 確保訓練、驗證與測試集之原圖零重疊，為後續模型效能評估提供無洩漏基準。
3. **深度學習模型效能與不確定性**：正式多 seed 比較包含 4 組模型 / 設定 $\times$ 5 seeds，共 20 筆紀錄。**本研究主要結論以五 seed 統計為準**：四組模型 / 策略之平均 accuracy 落在 80.12\%–81.19\%，比多數類別基準分類器（恆預測 A 等級，accuracy ≈ 49.2%）高出約 **31 個百分點**，顯示模型確實習得超越多數類別猜測的辨識能力；平均 QWK 約 0.91，遠高於多數類別基準之 QWK ≈ 0（隨機猜測）。然而，因 n=5 之統計效力嚴重不足（中等效應量 power 低於 0.3），任何模型間的差異均無法透過統計檢定可靠區分，本研究不報告具體 p 值以避免誤導（詳見第 \ref{sec:results-supplemental-multiseed} 節）。需特別指出，MobileNetV3-Large 完整設定 accuracy 之 std 為 5.98\%，為四組中最大，意味該設定對 seed 較敏感、訓練不穩定；且完整設定因 WeightedRandomSampler 使每 epoch 等效訓練量約為簡化設定六倍，兩者比較本身不對等，故\textbf{完整設定不應被視為穩定優於簡化設定}。seed=7 詳細案例中簡化設定 86.31\%、完整設定 89.88\%，僅作為混淆矩陣、校準與可視化分析之觀察案例（同一單次切分下，包含訓練量不對等之差異），不可外推為穩定效能。各等級分析顯示 B 等級召回率僅 56.3\%（9/16），為六等級中最低，A/B 邊界辨識為本系統最薄弱環節（詳見表 \ref{tab:seed7-perclass} 與第 \ref{sec:results-seed7} 節）。seed=7 單變因消融觀察到移除 Weighted Random Sampler 時跨等級誤判較高，但該消融僅為單次診斷，不作多 seed 穩定結論。模型校準後低 confidence 子集準確率明顯偏低（46.4\%），適合作為人工複核門檻；Grad-CAM 定性觀察顯示部分正確預測樣本之熱力圖高亮區域看似集中於魚骨間隙附近，但此為目視觀察，尚未以 IoU 量化驗證，不能排除模型同時依賴邊緣輪廓或顏色特徵（詳見第 \ref{sec:results-supplemental-calibration} 節）。故系統定位為「品質管控輔助原型」，而非可獨立判定之自動分級系統；**在未取得具人工標籤之 OOD 測試集前，本系統不應部署於與訓練條件不同之拍攝環境或硬體 / 材料條件**。
4. **整批照片自動處理流程**：整合自動裁切、逐張前向推論、分級輸出與 HTML 可視化報告，形成由原始照片到品質等級報告之離線處理流程；於 RTX 3050 Laptop GPU 上量測純模型前向延遲落於 7 ms 量級（簡化與完整設定差異屬量測雜訊範圍，量測條件詳見第 \ref{sec:results-batch} 節）。**此數字僅作為部署參考基準，不代表端到端產線吞吐量**；產線部署前仍需補做含前後處理之完整吞吐量、人工複核成本與現場穩定性評估。
5. **品質評分量化（未經人工校準）**：模型同時輸出 0 至 100 的連續品質分數。各等級平均分在 Group Split 測試集與全資料回測下均呈 A $>$ B $>$ C $>$ D $>$ E $>$ F 之單調遞減（數值詳見表 \ref{tab:plain-quality-score}），具輔助排序價值；惟目標分數採等級編號之線性轉換、未經多人主觀評分校準，B、D、E、F 等級之預測平均偏高，現階段僅作為分類結果之輔助連續指標，不宜作為絕對品質量化依據。

\vspace{0.5em}

**輔助工具實用性的初步評估**：在五 seed 平均 80–81\% accuracy 與 B 等級召回率 56.3\% 的效能水準下，本系統對品質管控流程的實際貢獻可從以下角度初步評估。

**誤判成本框架（部署決策的前提）**：評估本系統是否適合部署前，必須先量化兩種誤判方向的成本比值：（a）**假陰性成本**（瑕疵品被放行，即 B 等級被誤判為 A）：下游損失取決於應用情境，輕則外觀不滿意，重則結構或功能瑕疵，成本可能很高；（b）**假陽性成本**（良品被標為疑問件需複核，即 A 等級被誤判為 B 或更低）：操作員的額外複核時間，通常遠低於假陰性代價。在 B 等級召回率 56.3\%（假陰性率約 44\%）的條件下，本系統適合部署的場景是：假陰性代價相對低（如原型製作、外觀要求低的應用），或可接受高人工複核比例（低 confidence 子集約 16.7\% 加上所有非 A 預測）的場景。對外觀有嚴格要求或結構完整性攸關的生產場景，本系統在 A/B 邊界改善前不適合作為自動放行依據。

（1）**可替代人工的場景**：對於整批以 A 等級（完美品）為主的生產批次，系統可自動篩出高 confidence（$>0.9$）的 A 等級判定（seed=7 單次測試集之準確率約 95.5\%，此數字來自單一 seed，跨 seed 穩定性未驗證），將操作員的複核工作集中於低 confidence 子集（約 16.7\% 的樣本），理論上可減少約 80\% 的逐件目視工作量；但此「80\%」之數字前提是假陰性率可接受，需依上述誤判成本框架個案評估。（2）**不應自動通過的場景**：B 等級召回率僅 56.3\%，意味約 44\% 的輕微瑕疵品可能被誤判為完美品；若生產場景對輕微瑕疵的漏判有零容忍要求，本系統在未改善 A/B 邊界辨識能力前不適合作為自動放行依據。（3）**經濟效益前提**：上述評估以單一標注者標籤為基準，若後續多人一致性驗證顯示標注 Kappa 偏低，上述準確率數字需重新解讀，實際替代效益可能低於估計。

**主要貢獻陳述（Take-home Message）**：

> 在同一份 1110 張資料與原圖層級 Group Split 下，**四組模型 / 策略之五 seed 平均 accuracy 約 80–81\%**，較多數類別基準（恆預測 A 等級 ≈ 49.2\%）高出約 **31 個百分點**、**平均 QWK 約 0.91**（遠高於多數類別基準之 QWK ≈ 0），展現「能複現此固定標注準則」的初步可行性。需特別指出：（i）此準確率以單一標注者標籤為基準，**並非相對於客觀品質標準之表現**；在多人一致性（Cohen's Kappa）驗證完成前，「80–81\% accuracy」代表的是「模型複製一人判斷」的能力，不等同於「正確辨識客觀品質」的能力。（ii）**A/B 邊界召回率（B 等級 56.3\%）為最主要效能瓶頸**，與「單一標注者、未驗證一致性」之資料品質侷限相互糾纏，無法僅靠更換模型解決。（iii）「完整設定 vs 簡化設定」的消融比較存在 6 倍梯度更新量差異的設計缺陷，任何差異均不可歸因於策略本身。應用可信度之提升仍需完成標注一致性驗證、具標籤 OOD 測試集與跨機型 / 跨材料驗證；**在此之前，本系統不應部署於訓練條件外之拍攝環境或硬體 / 材料組合**。

## 建議 {#sec:conclusion-future}

根據本研究執行過程中的觀察與系統評估結果，提出以下建議供後續研究參考。建議分為三類：**【資料基礎】** 指資料收集與標注層面的根本性缺陷，若不修正，後續所有建模工作都在不穩固的基礎上進行；**【前提條件】** 指在本研究條件下尚未完成、若未補足則現有結論的可信度受到根本限制的驗證；**【延伸工作】** 指在資料基礎與可信度前提已滿足後，進一步擴充本研究貢獻的工作。優先序：資料基礎 > 前提條件 > 延伸工作。

0. **【資料基礎，最高優先】重建受控資料收集流程**。本研究現有資料存在三項根本性的資料品質問題，嚴重程度高於所有建模層面的不足：（a）**PLA 顏色未受控**：後續研究應使用統一顏色的 PLA，或確保每種顏色在 A 至 F 各等級均有充足代表樣本，消除顏色-等級共現的混淆；（b）**拍攝條件未固定**：應建立固定燈箱（穩定光源、色溫、方向）、固定架距（毫米級重複性）、鎖定曝光與白平衡的標準化拍攝流程，確保跨批次影像在亮度與色彩上具有可比性；（c）**裁切品質未驗證**：應以自動化輪廓偵測或邊界框確認方式系統驗證全部裁切圖的魚骨完整性，剔除裁切失敗樣本。此三項問題是本研究所有效能數字可信度的根本上限，優先於任何模型或評估方法的改進。**在這三項問題修正之前，即便更換更複雜的模型，結論的可信度仍受到相同的限制。**

1. **【前提條件】補齊應用可信度驗證**。本研究已完成 Group Split、多 seed、單變因消融、100 epoch 檢查、模型校準、PR/ROC、t-SNE、Grad-CAM 與外部未標注 sanity check。以下三項為尚未完成的可信度前提，建議優先補足：

   * **【未完成】具人工標籤的 OOD 測試集**：目前外部 105 張照片僅完成未標注推論分布與 confidence 檢查，不能計算 OOD accuracy。建議補拍並人工標注涵蓋不同光源、背景、角度與相機條件的測試集，先確認各等級皆有代表樣本，再擴充至足以穩定估計各等級召回率與整體退化幅度的規模。
   * **【目前受限，保留為未來工作】標注一致性 Cohen's Kappa**：由於現階段無法取得第二位以上標注者重新標注，本文不計算也不推估 $\kappa$。若未來具備人力，建議重新標注 100 張涵蓋 A 至 F 之樣本並計算 Cohen's $\kappa$ / Fleiss' $\kappa$；若 $\kappa < 0.7$，需重新檢視標注準則並補充邊界判斷規則。
   * **【調整為延伸工作】Ordinal-aware loss 對照**：本研究以 nominal classification + MSE auxiliary regression 近似序數分類任務，CORAL [@caoRankConsistentOrdinal2020]、CORN [@shiDeepNeuralNetworks2023] 等 ordinal-aware loss 方法在理論上更適合本研究的序數分級目標，但受限於研究規模與時程，未能納入主實驗。此項工作已從「前提條件」調整為「重要延伸工作」，原因是現有 nominal classification 結果雖非最佳設計，但仍提供可解釋的基準數字；ordinal-aware loss 的補充將使結論更加完整，而非現有結論完全失效的必要前提。建議後續研究以固定 Group Split 與相同 seed 集合，直接比較 CORAL/CORN 與本研究 nominal 設定之 QWK 與跨等級誤判率差異。

2. **【延伸工作】完善基準模型比較之因子設計**。目前正式多 seed 比較包含 MobileNetV3-Large 簡化 / 完整、ResNet18 完整與 EfficientNet-B0 完整四組，尚缺 ResNet18 簡化與 EfficientNet-B0 簡化之組合；若要分離「架構差異」與「訓練策略差異」的獨立效果，仍需完整 3 架構 $\times$ 2 策略的因子設計，並以五 seed 統計判斷各因素之主效果。
3. **【延伸工作】持續補充少數等級訓練資料**。E 級僅 72 張、F 級僅 32 張、B 級 87 張相較 A 級偏少，建議優先補充 B 級邊界樣本、E/F 嚴重瑕疵樣本，以足以支撐穩定估計與多 seed 分析為目標逐步擴充，降低少數等級邊界誤判率。
4. **【延伸工作】擴充至翹曲與裂痕瑕疵的辨識**。本研究因樣本不足聚焦於拉絲瑕疵。未來可系統性蒐集翹曲及裂痕樣本，建立涵蓋三種瑕疵類型的多標籤分類系統，更全面反映 FDM 列印件品質狀態。
5. **【延伸工作】跨機型 / 跨材料 / 跨幾何泛化能力驗證**。本研究僅於 Bambu Lab A1 + PLA + 魚骨條件下訓練與測試；建議補充其他印表機、材料與幾何形狀之樣本，組成跨域測試集，量化效能退化幅度。
6. **【延伸工作】評估即時列印監控系統**。目前系統為離線整批處理。未來可評估整合內建或外接相機串流，在列印進行中進行即時品質監控；此方向需另行驗證即時影像品質、延遲、誤報成本與設備控制安全性。
7. **【延伸工作】優化品質評分模型的準確性**。目前品質分採等級編號線性轉換為監督目標。未來可邀請有經驗的操作人員對全部樣本進行主觀連續評分，以此作為監督標籤訓練更精確的評分頭，並以 ICC（組內相關係數）作為可信度量化指標。
8. **【延伸工作】模型輕量化與邊緣部署**。MobileNetV3-Large 約 5.4M 參數（FP32 約 21 MB），若未來需部署於邊緣裝置，可評估知識蒸餾、剪枝或 INT8 量化；任何壓縮方案均需在相同資料切分下重新測試混淆矩陣、各等級召回率與推論時間。

9. **【說明】本研究缺乏與現有方法的直接量化比較**。由於 FDM 列印後成品序數品質分級的同域公開資料集與對應文獻目前十分有限（見第 \ref{sec:literature-related} 節說明），本研究無法提供與任何現有方法在相同條件下的直接數字比較；本研究報告的所有效能數字（accuracy、QWK、F1）均為**內部基準**，僅在本研究的特定資料集、切分協定與評估框架下有意義，不能直接與其他方法在不同資料集上報告的數字進行比較。建立公開的 FDM 拉絲嚴重程度標注資料集，以供後續方法間的公平比較，是推動此研究方向成熟的重要一步。

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

本附錄保留列印過程中四張代表性照片，分別對應「正常列印中」、「正常列印完成」、「輕微拉絲」、「列印失敗」四種典型狀態，作為前文等級定義之列印現場佐證。原始完整紀錄（共 16 張）已保存於研究者個人紀錄中，可依請求提供。

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
\multirow{2}{*}{回抽} & 回抽距離（Retraction Distance）& 未紀錄 & \makecell[l]{與拉絲直接相關；\\未截圖留存} \\
                     & 回抽速度（Retraction Speed）& 未紀錄 & 未截圖留存 \\
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
