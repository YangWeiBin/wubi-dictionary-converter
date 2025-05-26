# 配置PyQt5环境



## 1 配置PyQt5

```shell
pip install -i https://mirrors.aliyun.com/pypi/simple PyQt5
pip install -i https://mirrors.aliyun.com/pypi/simple PyQt6

pip install -i https://mirrors.aliyun.com/pypi/simple PyQt5-tools
pip install -i https://mirrors.aliyun.com/pypi/simple PyQt6-tools

pip install -i https://mirrors.aliyun.com/pypi/simple PySide5 # 没有这个
pip install -i https://mirrors.aliyun.com/pypi/simple PySide6
```

```shell
E:\00-YangWeiBin\Wubi\01-wubi-data-convert>pip install -i https://mirrors.aliyun.com/pypi/simple PyQt5
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://mirrors.aliyun.com/pypi/simple
Collecting PyQt5
  Downloading https://mirrors.aliyun.com/pypi/packages/56/d5/68eb9f3d19ce65df01b6c7b7a577ad3bbc9ab3a5dd3491a4756e71838ec9/PyQt5-5.15.11-cp38-abi3-win_amd64.whl (6.9 MB)
     ---------------------------------------- 6.9/6.9 MB 21.2 MB/s eta 0:00:00
Collecting PyQt5-sip<13,>=12.15 (from PyQt5)
  Downloading https://mirrors.aliyun.com/pypi/packages/24/c1/50fc7301aa39a50f451fc1b6b219e778c540a823fe9533a57b4793c859fd/PyQt5_sip-12.17.0-cp311-cp311-win_amd64.whl (59 kB)
Collecting PyQt5-Qt5<5.16.0,>=5.15.2 (from PyQt5)
  Downloading https://mirrors.aliyun.com/pypi/packages/37/97/5d3b222b924fa2ed4c2488925155cd0b03fd5d09ee1cfcf7c553c11c9f66/PyQt5_Qt5-5.15.2-py3-none-win_amd64.whl (50.1 MB)
     ---------------------------------------- 50.1/50.1 MB 13.9 MB/s eta 0:00:00
Installing collected packages: PyQt5-Qt5, PyQt5-sip, PyQt5
  WARNING: The scripts pylupdate5.exe, pyrcc5.exe and pyuic5.exe are installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed PyQt5-5.15.11 PyQt5-Qt5-5.15.2 PyQt5-sip-12.17.0

E:\00-YangWeiBin\Wubi\01-wubi-data-convert>pip install -i https://mirrors.aliyun.com/pypi/simple PyQt6
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://mirrors.aliyun.com/pypi/simple
Collecting PyQt6
  Downloading https://mirrors.aliyun.com/pypi/packages/d1/a8/955cfd880f2725a218ee7b272c005658e857e9224823d49c32c93517f6d9/PyQt6-6.9.0-cp39-abi3-win_amd64.whl (6.7 MB)
     ---------------------------------------- 6.7/6.7 MB 4.4 MB/s eta 0:00:00
Collecting PyQt6-sip<14,>=13.8 (from PyQt6)
  Downloading https://mirrors.aliyun.com/pypi/packages/2f/4d/23e9e23a331d5a608217349c931b1d9b5cf9419640033e73ae9895e7f5bd/PyQt6_sip-13.10.0-cp311-cp311-win_amd64.whl (53 kB)
Collecting PyQt6-Qt6<6.10.0,>=6.9.0 (from PyQt6)
  Downloading https://mirrors.aliyun.com/pypi/packages/6e/24/6b6168a75c7b6a55b9f6b5c897e6164ec15e94594af11a6f358c49845442/PyQt6_Qt6-6.9.0-py3-none-win_amd64.whl (73.7 MB)
     ---------------------------------------- 73.7/73.7 MB 4.8 MB/s eta 0:00:00
Installing collected packages: PyQt6-Qt6, PyQt6-sip, PyQt6
  WARNING: The scripts pylupdate6.exe and pyuic6.exe are installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed PyQt6-6.9.0 PyQt6-Qt6-6.9.0 PyQt6-sip-13.10.0

E:\00-YangWeiBin\Wubi\01-wubi-data-convert>pip install -i https://mirrors.aliyun.com/pypi/simple PyQt5-tools
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://mirrors.aliyun.com/pypi/simple
Collecting PyQt5-tools
  Downloading https://mirrors.aliyun.com/pypi/packages/11/7e/3a5bce0e31650e091a16826d7a588be8bd56c2ac30871286b6c90d68ceeb/pyqt5_tools-5.15.9.3.3-py3-none-any.whl (29 kB)
Collecting click (from PyQt5-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/7e/d4/7ebdbd03970677812aac39c869717059dbb71a4cfc033ca6e5221787892c/click-8.1.8-py3-none-any.whl (98 kB)
Collecting pyqt5==5.15.9 (from PyQt5-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/55/5d/8df8a2aa0de6588965d048fca9306cf15a5801be3078f195e8f8f41fa863/PyQt5-5.15.9-cp37-abi3-win_amd64.whl (6.8 MB)
     ---------------------------------------- 6.8/6.8 MB 7.5 MB/s eta 0:00:00
Collecting pyqt5-plugins<5.15.9.3,>=5.15.9.2.2 (from PyQt5-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/cd/29/b9e0ad2d345b425a111f22eac83e45c68afe8d3475a0adabc2da5dbfa5b3/pyqt5_plugins-5.15.9.2.3-cp311-cp311-win_amd64.whl (66 kB)
Collecting python-dotenv (from PyQt5-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/1e/18/98a99ad95133c6a6e2005fe89faedf294a748bd5dc803008059409ac9b1e/python_dotenv-1.1.0-py3-none-any.whl (20 kB)
Requirement already satisfied: PyQt5-sip<13,>=12.11 in c:\users\qxz32h9\appdata\roaming\python\python311\site-packages (from pyqt5==5.15.9->PyQt5-tools) (12.17.0)
Requirement already satisfied: PyQt5-Qt5>=5.15.2 in c:\users\qxz32h9\appdata\roaming\python\python311\site-packages (from pyqt5==5.15.9->PyQt5-tools) (5.15.2)
Collecting qt5-tools<5.15.2.2,>=5.15.2.1.2 (from pyqt5-plugins<5.15.9.3,>=5.15.9.2.2->PyQt5-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/e2/45/3062d0df2bbc88ee4ea04b1073072b337b9e287c0b4ac12109729b413e2e/qt5_tools-5.15.2.1.3-py3-none-any.whl (13 kB)
Collecting colorama (from click->PyQt5-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting qt5-applications<5.15.2.3,>=5.15.2.2.2 (from qt5-tools<5.15.2.2,>=5.15.2.1.2->pyqt5-plugins<5.15.9.3,>=5.15.9.2.2->PyQt5-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/ae/a9/cd64cda6f58321c4a0021ced80117b225562efc42f1318ff2cea69c23eb7/qt5_applications-5.15.2.2.3-py3-none-win_amd64.whl (64.5 MB)
     ---------------------------------------- 64.5/64.5 MB 7.5 MB/s eta 0:00:00
Installing collected packages: qt5-applications, python-dotenv, pyqt5, colorama, click, qt5-tools, pyqt5-plugins, PyQt5-tools
  WARNING: The script dotenv.exe is installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Attempting uninstall: pyqt5
    Found existing installation: PyQt5 5.15.11
    Uninstalling PyQt5-5.15.11:
      Successfully uninstalled PyQt5-5.15.11
  WARNING: The scripts pylupdate5.exe, pyrcc5.exe and pyuic5.exe are installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script qt5-tools.exe is installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pyqt5-tools.exe is installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed PyQt5-tools-5.15.9.3.3 click-8.1.8 colorama-0.4.6 pyqt5-5.15.9 pyqt5-plugins-5.15.9.2.3 python-dotenv-1.1.0 qt5-applications-5.15.2.2.3 qt5-tools-5.15.2.1.3

E:\00-YangWeiBin\Wubi\01-wubi-data-convert>pip install -i https://mirrors.aliyun.com/pypi/simple PyQt6-tools
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://mirrors.aliyun.com/pypi/simple
Collecting PyQt6-tools
  Downloading https://mirrors.aliyun.com/pypi/packages/82/bc/dcea094a26697ba76ae73dec030dd4070836b1e7e810d304d4917518423b/pyqt6_tools-6.4.2.3.3-py3-none-any.whl (29 kB)
Requirement already satisfied: click in c:\users\qxz32h9\appdata\roaming\python\python311\site-packages (from PyQt6-tools) (8.1.8)
Collecting pyqt6==6.4.2 (from PyQt6-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/7a/4e/4acc0ebe1f3231217bee58ec0f90ef6bdfbd6e0b7d08420c5ddb97780288/PyQt6-6.4.2-cp37-abi3-win_amd64.whl (6.4 MB)
     ---------------------------------------- 6.4/6.4 MB 7.0 MB/s eta 0:00:00
Collecting pyqt6-plugins<6.4.2.3,>=6.4.2.2.2 (from PyQt6-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/ea/9e/153a339bf3c6eb699fabf7ef703e8f165275b255fc4bd7a2583a2a0ecdf8/pyqt6_plugins-6.4.2.2.3-cp311-cp311-win_amd64.whl (72 kB)
Requirement already satisfied: python-dotenv in c:\users\qxz32h9\appdata\roaming\python\python311\site-packages (from PyQt6-tools) (1.1.0)
Requirement already satisfied: PyQt6-sip<14,>=13.4 in c:\users\qxz32h9\appdata\roaming\python\python311\site-packages (from pyqt6==6.4.2->PyQt6-tools) (13.10.0)
Requirement already satisfied: PyQt6-Qt6>=6.4.0 in c:\users\qxz32h9\appdata\roaming\python\python311\site-packages (from pyqt6==6.4.2->PyQt6-tools) (6.9.0)
Collecting PyQt6-Qt6>=6.4.0 (from pyqt6==6.4.2->PyQt6-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/11/cf/9102346c5ea4cc2796d1eb2214593e5b65a500b2abaad258cadfe8cb3dca/PyQt6_Qt6-6.4.3-py3-none-win_amd64.whl (57.5 MB)
     ---------------------------------------- 57.5/57.5 MB 7.1 MB/s eta 0:00:00
Collecting qt6-tools<6.4.3.2,>=6.4.3.1.2 (from pyqt6-plugins<6.4.2.3,>=6.4.2.2.2->PyQt6-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/18/5f/58fd48246779de82bd15a9cb1bface620fb7b6009ee5a5544f1a5ca39cdb/qt6_tools-6.4.3.1.3-py3-none-any.whl (13 kB)
Requirement already satisfied: colorama in c:\users\qxz32h9\appdata\roaming\python\python311\site-packages (from click->PyQt6-tools) (0.4.6)
Collecting qt6-applications<6.4.3.3,>=6.4.3.2.2 (from qt6-tools<6.4.3.2,>=6.4.3.1.2->pyqt6-plugins<6.4.2.3,>=6.4.2.2.2->PyQt6-tools)
  Downloading https://mirrors.aliyun.com/pypi/packages/c9/39/eb4d4c22b7785cd31713a8354ca97eb2ffe95f1a8809ea06e21d762d0bc7/qt6_applications-6.4.3.2.3-py3-none-win_amd64.whl (71.3 MB)
     ---------------------------------------- 71.3/71.3 MB 6.9 MB/s eta 0:00:00
Installing collected packages: PyQt6-Qt6, qt6-applications, pyqt6, qt6-tools, pyqt6-plugins, PyQt6-tools
  Attempting uninstall: PyQt6-Qt6
    Found existing installation: PyQt6-Qt6 6.9.0
    Uninstalling PyQt6-Qt6-6.9.0:
      Successfully uninstalled PyQt6-Qt6-6.9.0
  Attempting uninstall: pyqt6
    Found existing installation: PyQt6 6.9.0
    Uninstalling PyQt6-6.9.0:
      Successfully uninstalled PyQt6-6.9.0
  WARNING: The scripts pylupdate6.exe and pyuic6.exe are installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script qt6-tools.exe is installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pyqt6-tools.exe is installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed PyQt6-Qt6-6.4.3 PyQt6-tools-6.4.2.3.3 pyqt6-6.4.2 pyqt6-plugins-6.4.2.2.3 qt6-applications-6.4.3.2.3 qt6-tools-6.4.3.1.3

E:\00-YangWeiBin\Wubi\01-wubi-data-convert>pip install -i https://mirrors.aliyun.com/pypi/simple PySide6
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://mirrors.aliyun.com/pypi/simple
Collecting PySide6
  Downloading https://mirrors.aliyun.com/pypi/packages/63/03/55a632191beadd6bc59b04055961e2c3224a3475a906a63d1899a5ab493d/PySide6-6.9.0-cp39-abi3-win_amd64.whl (564 kB)
     ---------------------------------------- 564.5/564.5 kB 4.9 MB/s eta 0:00:00
Collecting shiboken6==6.9.0 (from PySide6)
  Downloading https://mirrors.aliyun.com/pypi/packages/e2/6e/cf00d723ab141132fb6d35ba8faf109cbc0ee83412016343600abb423149/shiboken6-6.9.0-cp39-abi3-win_amd64.whl (1.2 MB)
     ---------------------------------------- 1.2/1.2 MB 5.2 MB/s eta 0:00:00
Collecting PySide6-Essentials==6.9.0 (from PySide6)
  Downloading https://mirrors.aliyun.com/pypi/packages/96/8a/bc710350c4cf6894968e39970eaa613b85a82eb1f230052de597e44a00ac/PySide6_Essentials-6.9.0-cp39-abi3-win_amd64.whl (72.3 MB)
     ---------------------------------------- 72.3/72.3 MB 6.0 MB/s eta 0:00:00
Collecting PySide6-Addons==6.9.0 (from PySide6)
  Downloading https://mirrors.aliyun.com/pypi/packages/77/c0/b1718f62d1fcc9bac4c410d4150d7e1214235e73cc18f39dc36ad49f093f/PySide6_Addons-6.9.0-cp39-abi3-win_amd64.whl (143.0 MB)
     ---------------------------------------- 143.0/143.0 MB 5.7 MB/s eta 0:00:00
Installing collected packages: shiboken6, PySide6-Essentials, PySide6-Addons, PySide6
  WARNING: The scripts pyside6-assistant.exe, pyside6-balsam.exe, pyside6-balsamui.exe, pyside6-deploy.exe, pyside6-designer.exe, pyside6-genpyi.exe, pyside6-linguist.exe, pyside6-lrelease.exe, pyside6-lupdate.exe, pyside6-metaobjectdump.exe, pyside6-project.exe, pyside6-qml.exe, pyside6-qmlcachegen.exe, pyside6-qmlformat.exe, pyside6-qmlimportscanner.exe, pyside6-qmllint.exe, pyside6-qmlls.exe, pyside6-qmltyperegistrar.exe, pyside6-qsb.exe, pyside6-qtpy2cpp.exe, pyside6-rcc.exe, pyside6-svgtoqml.exe and pyside6-uic.exe are installed in 'C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed PySide6-6.9.0 PySide6-Addons-6.9.0 PySide6-Essentials-6.9.0 shiboken6-6.9.0

E:\00-YangWeiBin\Wubi\01-wubi-data-convert>pip install -i https://mirrors.aliyun.com/pypi/simple PySide5
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://mirrors.aliyun.com/pypi/simple
ERROR: Could not find a version that satisfies the requirement PySide5 (from versions: none)
ERROR: No matching distribution found for PySide5

E:\00-YangWeiBin\Wubi\01-wubi-data-convert>
```



## 2 Pycharm插件

- **QtDesigner——通过Qt语言进行UI设计（支持拖拽式的UI设计） **
- **PyUIC——主要用来将QtDesigner代码转化成Python代码**
- **Pyrcc—— 将图片、数据文件资源打包成py文件**  

```shell
Name:QtDesigner
Group:External Tools
Program:C:\Users\qxz32h9\AppData\Roaming\Python\Python311\site-packages\PySide6\designer.exe
Arguments:$FileDir$\$FileName$ 
Working directory：$FileDir$


Name:pyuic6
Group:External Tools
Program:C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts\pyuic6.exe
Arguments:$FileName$ -o $FileNameWithoutExtension$.py
Working directory：$FileDir$

Name:pyrcc5
Group:External Tools
Program:C:\Users\qxz32h9\AppData\Roaming\Python\Python311\Scripts\pyrcc5.exe
Arguments:$FileName$ -o $FileNameWithoutExtension$.py
Working directory：$FileDir$
```



## 3 安装成功



```shell
E:\00-YangWeiBin\Wubi\01-wubi-data-convert>pip show PyQt5
Name: PyQt5
Version: 5.15.9
Summary: Python bindings for the Qt cross platform application toolkit
Home-page: https://www.riverbankcomputing.com/software/pyqt/
Author: Riverbank Computing Limited
Author-email: info@riverbankcomputing.com
License: GPL v3
Location: C:\Users\qxz32h9\AppData\Roaming\Python\Python311\site-packages
Requires: PyQt5-Qt5, PyQt5-sip
Required-by: pyqt5-plugins, pyqt5-tools

E:\00-YangWeiBin\Wubi\01-wubi-data-convert>pip show PyQt6
Name: PyQt6
Version: 6.4.2
Summary: Python bindings for the Qt cross platform application toolkit
Home-page: https://www.riverbankcomputing.com/software/pyqt/
Author: Riverbank Computing Limited
Author-email: info@riverbankcomputing.com
License: GPL v3
Location: C:\Users\qxz32h9\AppData\Roaming\Python\Python311\site-packages
Requires: PyQt6-Qt6, PyQt6-sip
Required-by: pyqt6-plugins, pyqt6-tools
```

## 4 打包exe

```shell
pyinstaller --onefile --noconsole --distpath wubi-converter --add-data "resources/*;resources" wubi-dictionary-converter.py
```



