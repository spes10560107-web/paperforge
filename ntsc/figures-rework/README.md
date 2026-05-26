# paper.md 圖片修正素材

本資料夾不會被 paper.md 直接引用；所有檔案僅作為**修正圖片時的來源原稿**。
最終產生的 PNG 請覆寫到 `../images/` 對應檔名後即可（paper.md 內的 `\includegraphics{images/...}` 不需動）。

---

## 操作流程總覽

| 來源 | 工具 | 產出 | 覆寫到 |
|---|---|---|---|
| `research-overall-flow.mmd` | mmdc / mermaid.live | `research-overall-flow.png` | `../images/research-overall-flow.png` |
| `method-system-flow.mmd` | mmdc / mermaid.live | `method-system-flow.png` | `../images/method-system-flow.png` |
| `regen_new-model-accuracy-comparison.py` | python + matplotlib | `new-model-accuracy-comparison.png` | `../images/new-model-accuracy-comparison.png` |
| `regen_quality-score-comparison.py` | python + matplotlib | `quality-score-comparison.png` | `../images/quality-score-comparison.png` |
| 其餘 defect-{stringing,warping,cracking}、grade-f-sample、print-process-01-normal、bambu-studio-quality-tab | 重拍或換圖 | --- | 各對應檔名 |

### 安裝 mermaid CLI（一次性）

```powershell
npm install -g @mermaid-js/mermaid-cli
```

### 將 mermaid 程式碼轉成 PNG

```powershell
mmdc -i research-overall-flow.mmd -o research-overall-flow.png -t neutral -b white --width 1200
mmdc -i method-system-flow.mmd    -o method-system-flow.png    -t neutral -b white --width 1400
```

若不想裝 mmdc，可直接把 `.mmd` 內容貼到 <https://mermaid.live>，匯出 PNG。

### 重畫 matplotlib 圖

```powershell
python regen_new-model-accuracy-comparison.py
python regen_quality-score-comparison.py
```

需求：`pip install matplotlib`，需中文字型（程式內已用 Microsoft JhengHei，可改為標楷體 `DFKai-SB`）。

---

## 每張圖修正方案

### A1. `research-overall-flow.png`（圖 1 研究整體流程圖）—— **重做**

**問題**：時間範圍（2025/08/15–2025/12/01、4 批次）、訓練設定（Focal Loss+Mixup+WeightedSampler、95.86%）都與正文最新版本不符。

**修正方法**：用 `research-overall-flow.mmd` 重畫（mermaid）；對應正文 sec:intro-flow 的「三大階段」與 sec:method-system 的「五個元件」。

### A2. `method-system-flow.png`（圖 2 研究流程與資料流關係圖）—— **重做**

**問題**：寫「使用 **3D CNN** 自動檢測」（本研究實際是 2D + MobileNetV3-Large）；起點紅色「軟體」節點意義不明；流程過度抽象，未呈現五個元件。

**修正方法**：用 `method-system-flow.mmd` 重畫（mermaid），對應表 \ref{tab:system-components} 的 5 個元件 + 資料流。

### A3. `new-model-accuracy-comparison.png`（圖 12 version_21 各等級準確率）—— **重畫**

**問題**：圖中 A 97.4%、B 94.4%、C 86.3%、D 75.7%、F 94.1% 與表 \ref{tab:new-model}（A 98.7%、B 92.0%、C 96.7%、D 90.6%、F 93.8%、整體 95.86%）完全不一致。

**修正方法**：執行 `regen_new-model-accuracy-comparison.py`，使用表 \ref{tab:new-model} 的正確數字重畫長條圖。

### A4. `quality-score-comparison.png`（圖 13 品質分對照）—— **重畫**

**問題**：圖中 version_21 數據與正文主要結論（簡化設定）脫鉤。

**修正方法**：執行 `regen_quality-score-comparison.py`，產出**簡化設定 Group Split 測試集**的品質分對照（對應表 \ref{tab:plain-quality-score}）。

### A5. `defect-stringing.png`（拉絲示意）—— **換圖或註記**

**問題**：實際是「溫度塔」(180–240)，不是魚骨件。

**選項一（推薦）**：從 `data/raw/E/` 或 `data/raw/F/` 中挑一張典型嚴重拉絲魚骨樣本，覆蓋 `defect-stringing.png`。
**選項二**：保留原圖，但 caption 加註「（來源：3D 列印社群公開示意圖，非本研究樣本）」並改用通用 FDM 拉絲示意。
**選項三**：直接刪掉，把後續三張瑕疵示意圖（拉絲、翹曲、裂痕）合併為一張 subfigure。

### A6. `defect-warping.png`（翹曲示意）—— **換圖**

**問題**：圖中是平面良好的列印件底層紋理特寫，根本看不到翹曲特徵。

**修正方法**：從網路找一張典型「邊角上翹」的 FDM 翹曲樣本（注意版權），或實際刻意做一張翹曲樣本拍攝。caption 維持原樣即可。

### A7. `defect-cracking.png`（裂痕示意）—— **改 caption 或換圖**

**問題**：圖中明確標示「列印件**長期運作下**產生的裂痕」（受力裂痕），但 caption 寫「層間結合不足導致的分層」（列印時即發生），成因不同。

**選項一（最小改動）**：修改 caption 為「裂痕（Cracking）瑕疵：層間黏結不足或使用受力後產生的裂縫」涵蓋兩種來源；同時刪除原圖右下角紅色箭頭與「長期運作」字樣。
**選項二**：找一張真正的「層間分離（Layer Separation）」典型照片替換。

### A8. `grade-f-sample.jpg`（F 級代表圖）—— **換成無 overlay 原圖**

**問題**：右上角有 `F 90%` 紅色模型推論 overlay 標籤；用「模型輸出」當「人工等級定義範例」邏輯倒置。

**修正方法**：從 `data/raw/F/` 中挑同一張或類似的 F 級魚骨**原圖**（裁切後但未經模型 overlay 處理），覆寫 `grade-f-sample.jpg`。同時：
- A 級 `grade-a-sample.jpg` 是灰白 PLA、B–F 級是藍色 PLA — 建議統一改用同色 PLA 樣本，避免讀者誤以為「顏色＝等級」。

### A9. `print-process-01-normal.jpg`（附錄列印中代表圖）—— **重新挑圖**

**問題**：對焦失敗、前景模糊，看不出「結構完整」。

**修正方法**：從 `print-process-02.jpg`～`print-process-16.jpg`（已在 `ntsc/images/`）中挑一張對焦清楚、能看到「列印中、結構完整」的照片覆寫 `print-process-01-normal.jpg`。或請使用者重拍一張更清楚的。

### A10. `bambu-studio-quality-tab.png`（Bambu Studio 品質頁籤截圖）—— **重截**

**問題**：是簡體中文介面（「层高/默认」）、覆蓋度不足（只到「線寬」）。

**修正方法**：
1. 把 Bambu Studio UI 語言切換成繁體中文
2. 重新截圖「品質」分頁完整內容（含層高、線寬、接縫等所有區塊）
3. 覆寫 `bambu-studio-quality-tab.png`

同樣建議在重截品質頁籤的同時，把 `bambu-studio-cooling-mode.png` 一併重截。

---

## 不在「圖片修正」範疇內的問題（請另開對話處理）

- B1（裁切圖合併 subfigure）、B3（補 Group Split 混淆矩陣）、B4（補誤判案例圖）需要修改 paper.md
- C1–C7 全部是正文敘述問題，需要修改 paper.md
- 這些都交給你另一個對話窗去做

---

## 修正完成後檢查

執行 `scripts/build.ps1 ntsc/paper.md` 編譯 PDF，檢查：

1. 每張新圖的數值與對應表格一致
2. 所有 `\ref{}` 仍能正確解析
3. PDF > 10 KB、頁數合理
4. mermaid 產生的 PNG 在 PDF 中清晰可讀（必要時調 `--width` 參數）
