当我们学习和使用一个编程语言的时候，我们往往需要一个平台用于编写程序并且编译运行，来检验程序的正确性，从而查漏补缺、巩固印象。
同样的，在学习 Numpy 的时候，我们可以使用 Jupyter 来达到相同的目的。

> 我的环境：miniconda + python=3.11 + Jupyter

# 使用步骤
### 启动 Jupyter Notebook
1. 激活配置好的环境，具体怎么创建以及激活，可以看文章[Conda](Conda.md)
2. 启动 `Jupyter Notebook` ：在命令行中输入`jupyter notebook` 并回车，稍等片刻，等待浏览器自动打开 Jupyter Notebook 的主界面。
*注意：不要关闭当前的黑色命令行窗口，否则 Jupyter 服务会终止。*
### 创建一个新的 Notebook
1. 在 Jupyter 主页上，点击右上角的 New 按钮
2. 在下拉菜单中选择 Python 3（或者你当前 Conda 环境的名称）。一个新的笔记本（Notebook）就会在新标签页中打开。
### 页面使用指南
- **Cell**：Notebook 由一个个的 Cell 组成，你可以在每个 Cell 中编写代码或文本。
- **导入 Numpy 库**：`import numpy as np`
- **运行代码**：使用工具栏中的 Run 按钮，或者使用快捷键 `Shift + Enter` 来运行。
# 其他
### 修改 Jupyter 默认工作目录
你可以通过配置文件让 Jupyter 启动时就进入指定文件夹，省去每次手动 `cd` 的麻烦：
1. 生成配置：`jupyter notebook --generate-config`
2. 编辑 `jupyter_notebook_config.py` ：
- 找到并修改或添加这一行： `c.NotebookApp.notebook_dir = 'D:/Jupyter_Notebooks'`
*注意，这里填写路径的时候，需要使用正斜杠 `/` 或者双反斜杠 `\\` 来表示路径*
- 之后直接运行`jupyter notebook` 就会自动以 D 盘目录为根。