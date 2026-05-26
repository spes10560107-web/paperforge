"""
重畫 quality-score-comparison.png（圖 \\ref{fig:quality-score}）。

修正原圖與正文主要結論脫鉤：原圖是 version_21 全資料回測的品質分（A 79.4、F 28.5）；
但 sec:results-quality-score 正文主軸是「簡化設定 Group Split 測試集」結果（表 tab:plain-quality-score）。

本腳本以表 \\ref{tab:plain-quality-score} 兩組數據（Group Split 測試集 + 全資料回測）
並列重畫，並維持「目標分數」對照，使圖文一致。

輸出：quality-score-comparison.png（直接覆寫到 ../images/quality-score-comparison.png 即可）
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "DFKai-SB", "SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

grades = ["A\n完美品", "B\n良好品", "C\n輕微拉絲", "D\n中度拉絲", "E\n嚴重拉絲", "F\n失敗品"]
target = [100, 80, 60, 40, 20, 0]            # 表 tab:grading-criteria
gs_test = [99.6, 89.0, 58.8, 54.5, 23.5, 12.5]   # 表 tab:plain-quality-score Group Split 測試集平均
full_back = [99.5, 88.3, 60.5, 50.9, 30.8, 16.2] # 表 tab:plain-quality-score 全資料回測平均

x = np.arange(len(grades))
width = 0.27

fig, ax = plt.subplots(figsize=(13, 6))

bars1 = ax.bar(x - width, target, width, color="#3498db", edgecolor="white", linewidth=1.0, label="目標品質分")
bars2 = ax.bar(x,         gs_test, width, color="#e67e22", edgecolor="white", linewidth=1.0, label="Group Split 測試集平均（簡化設定，主要結果）")
bars3 = ax.bar(x + width, full_back, width, color="#95a5a6", edgecolor="white", linewidth=1.0, label="全資料回測平均（簡化設定，僅供擬合度參考）")

for bars, values in [(bars1, target), (bars2, gs_test), (bars3, full_back)]:
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 1.5, f"{v:.1f}",
                ha="center", va="bottom", fontsize=9.5)

ax.set_xticks(x)
ax.set_xticklabels(grades)
ax.set_ylim(0, 115)
ax.set_ylabel("品質分", fontsize=12)
ax.set_title("各等級目標品質分與模型輸出平均分比較（MobileNetV3-Large 簡化設定）", fontsize=13, pad=12)
ax.legend(loc="upper right", fontsize=10)
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()

out = Path(__file__).resolve().parent / "quality-score-comparison.png"
fig.savefig(out, dpi=180, bbox_inches="tight", facecolor="white")
print(f"輸出：{out}")
print("請將此檔覆寫到 ../images/quality-score-comparison.png")
print("注意：paper.md 中圖 caption 也應從『version_21』改為『MobileNetV3-Large 簡化設定』")
