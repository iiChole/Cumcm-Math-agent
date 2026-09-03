# LaTeX 与 ZIP 交付规范

## 模板优先级

1. 用户提供的模板与 `.cls`；
2. 当年官方模板；
3. 本 Skill 的 `assets/paper_skeleton.tex`，仅作无模板时的骨架。

不要在已有模板时擅自更换版式系统。

## 推荐工程结构

```text
project/
├── figures/
├── code/
│   ├── q1_*.py
│   ├── q2_*.py
│   ├── plot_*.py
│   ├── requirements.txt
│   └── README.md
├── .gitignore
├── cumcmthesis.cls
├── example.tex
└── example.pdf
```

## 编译与检查

优先 XeLaTeX，至少编译两遍：

```bash
xelatex -interaction=nonstopmode -halt-on-error example.tex
xelatex -interaction=nonstopmode -halt-on-error example.tex
```

检查日志中的 `Overfull`、`Undefined`、`LaTeX Warning`、`Citation` 和 `Reference`；处理正文关键公式、表格和图形的溢出、未定义引用、字体乱码和越界。编译后确认摘要与关键词位于第 1 页，删除完全空白页，并用 PDF 渲染检查图表重叠、可读性和章节层级。

正文页数按用户或当年官方要求；没有特别要求时，默认控制在 20–24 页（不含附录）。
附录放在正文之后；默认只约束正文页数，不以附录后的 PDF 总页数替代正文页数检查，也不通过空白、巨图或重复文字凑页数。

## 代码与 ZIP

代码按问题或功能拆分，固定随机种子，输出正文中的关键数值，不依赖开发机绝对路径，README 说明输入、运行顺序和环境。最终 ZIP 只包含必要工程，删除临时渲染图、缓存、编辑器文件和调试中间产物。
