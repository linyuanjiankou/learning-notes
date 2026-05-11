>依旧是为了重新学一遍C语言，由于再在Windows中学一遍有点枯燥，于是打算在Linux环境下学习，顺便研究一下Linux命令。

*这篇文章只列举我使用过的Linux指令，有关Linux的其他知识，后续在系统学习时可能会单开一个Notes*

- `sudo apt install 软件名称`: 下载软件。`sudo` 表示以超级用户权限执行命令（所以需要验证密码），`apt` 则是 Ubuntu/Debian 系统下的包管理工具，可下载的常用软件：gedit（文本编辑）、eog（查看图片）、Vim（编辑器）、Apostrophe（读取 Markdown）等。
- `软件名称`: 直接输入软件名称就能打开对应软件。
- `sudo apt update`: 获取最新软件信息
- `sudo apt upgrade`: 升级已安装的软件包
- `sudo apt install build-essential`: 一键安装`build-essential`，包括gcc, g++, make, glibc
- `mkdir 文件夹名称`: 在当前目录下创建文件夹
- `pwd`: 查看当前文件路径
- `ls`: 查看当前文件夹内容

# gcc
1. 编译：`gcc hello.c -o hello`
	- `gcc`: C编译器
	- `hello.c`: 你的源文件
	- `-o hello`: 指定生成的可执行文件名为`hello`（如果不加`-o`，默认生成`a.out`）
2. 运行：`./hello`
	- `./`表示当前目录，因为当前目录通常不在系统的PATH环境变量中。
3. 获取警告：`gcc -Wall hello.c -o hello`