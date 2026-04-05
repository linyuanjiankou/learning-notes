# 背景
当我在Github上找到一个项目，用于即使更正命令行命令的项目，下载试运行的时候出现了问题，这个项目需要在python旧版本的环境下才能运行。
由于我正处于假期，时间还算比较充裕，于是决定研究一下配置miniconda进行环境隔离。
# 日常工作流
日常配置虚拟环境的流程大体上分为三步：
1. 创建一个新环境（虚拟环境）
假设你想做一个 Python 3.11 的项目，给他起名叫 `myenv` ：
```bash
conda create -n myenv python=3.11
```
接着系统会询问是否继续，输入 y 并回车
2. 激活环境
环境建好后还需要激活：
```bash
conda activate myenv
```
激活成功之后你会看到命令行最前面的`(base)`变为了`(myenv)`，说明已经在这个独立的环境内了
3. 安装所需包
激活环境后既可以安装库了（比如安装numpy）：
```bash
conda install numpy
```
或者使用 pip：
```bash
pip install requests
```
# 其他命令总览
- 查看环境实际安装位置：`conda info --envs`
- 临时指定安装路径：`conda create -p <完整路径/环境名> python=3.9`；同时，激活时也需要完整路径：`conda activate <完整路径/环境名>`
- 从当前环境返回：`conda deactivate`
# 配合PyCharm
由于我之前使用官方Python+PyCharm的组合进行编程，现在多写一点有关miniconda+PyCharm的配置关联：
在PyCharm中，在设置`Settings -> Python Interpreter`中，点击齿轮图标`Add...`，选择`Conda Environment`，然后选择环境即可。