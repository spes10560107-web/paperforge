"""
重畫 new-model-accuracy-comparison.png（圖 \\ref{fig:new-model-acc}）。

修正原圖數據錯誤：原圖顯示 A 97.4%、整體 94.4% 等，但表 \\ref{tab:new-model}
與 paper.md 摘要寫的 version_21 全資料集回測為 A 98.7%、整體 95.86%。

本腳本以表 \\ref{tab:new-model} 的數據重畫左圖；右圖以表 \\ref{tab:old-model}
與 \\ref{tab:new-model} 的 Recall 數據重畫新舊版對比。

輸出：new-model-accuracy-comparison.png（直接覆寫到 ../images/new-model-accuracy-comparison.png 即可）
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "DFKai-SB", "SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# version_21 全資料集回測（來源：paper.md 表 tab:new-model）
grades = ["A\n完美品", "B\n良好品", "C\n輕微拉絲", "D\n中度拉絲", "E\n嚴重拉絲", "F\n失敗品"]
new_recall = [98.7, 92.0, 96.7, 90.6, 88.9, 93.8]
overall = 95.86  # 整體準確率（1064/1110）

# 舊版 MobileNetV3-Small（214 張）Recall（來源：paper.md 表 tab:old-model）
old_recall = [88.4, 80.0, 75.0, 77.8, 88.9, 66.7]

colors = ["#2ecc71", "#27ae60", "#3498db", "#f39c12", "#e67e22", "#e74c3c"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# 左圖：version_21 各等級辨識準確率
bars = ax1.bar(grades, new_recall, color=colors, edgecolor="white", linewidth=1.2)
ax1.axhline(y=overall, color="#333333", linestyle="--", linewidth=1.4,
            label=f"整體準確率 {overall:.2f}%")
ax1.set_ylim(0, 115)
ax1.set_ylabel("準確率（%）", fontsize=12)
ax1.set_title("各等級辨識準確率（version_21 全資料集回測）", fontsize=13, pad=12)
ax1.legend(loc="lower right", fontsize=10)
ax1.grid(axis="y", alpha=0.3)
for bar, value in zip(bars, new_recall):
    # 避開 95.86% 虛線：若數值落在 94–97 範圍就把標籤往上推
    offset = 4.5 if 94.0 <= value <= 97.0 else 1.5
    ax1.text(bar.get_x() + bar.get_width() / 2, value + offset, f"{value:.1f}%",
             ha="center", va="bottom", fontsize=11)

# 右圖：新舊版 Recall 對比
x = list(range(len(grades)))
width = 0.36
ax2.bar([i - width / 2 for i in x], old_recall, width=width,
        color="#bdc3c7", edgecolor="white", linewidth=1, label="舊版（MobileNetV3-Small，214 張）")
ax2.bar([i + width / 2 for i in x], new_recall, width=width,
        color=colors, edgecolor="white", linewidth=1, label="改良版（MobileNetV3-Large，1110 張）")
ax2.set_xticks(x)
ax2.set_xticklabels(grades)
ax2.set_ylim(0, 115)
ax2.set_ylabel("Recall（%）", fontsize=12)
ax2.set_title("新舊版模型 Recall 比較", fontsize=13, pad=12)
ax2.legend(loc="lower right", fontsize=10)
ax2.grid(axis="y", alpha=0.3)
for i, value in enumerate(old_recall):
    ax2.text(i - width / 2, value + 1.5, f"{value:.1f}", ha="center", va="bottom", fontsize=9, color="#555")
for i, value in enumerate(new_recall):
    ax2.text(i + width / 2, value + 1.5, f"{value:.1f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()

out = Path(__file__).resolve().parent / "new-model-accuracy-comparison.png"
fig.savefig(out, dpi=180, bbox_inches="tight", facecolor="white")
print(f"輸出：{out}")
print("請將此檔覆寫到 ../images/new-model-accuracy-comparison.png")
