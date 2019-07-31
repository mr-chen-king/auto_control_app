# 教你用 Python 群控手机
首先膜拜下开发微信跳一跳自动脚本的大神，本教程基于其启发(脚本放在examples目录下)

## 依赖关系

> adb [Android 和 iOS 操作步骤](https://github.com/wangshub/wechat_jump_game/wiki/Android-%E5%92%8C-iOS-%E6%93%8D%E4%BD%9C%E6%AD%A5%E9%AA%A4)
> ![uiautomator2](https://github.com/openatx/uiautomator2)



## 原理说明

1. 用 ADB 工具获取当前手机截图，并用 ADB 将截图 pull 上来,保存在电脑端，可用作后续的图像识别，模拟坐标点击，可用来作为开发手游脚本使用
```shell
adb shell screencap -p /sdcard/autojump.png
adb pull /sdcard/autojump.png .
```


#### 获取源码

```
- git clone https://github.com/mr-chen-king/auto_control_app
- examples 下有简单的使用例子，可以用于那个app这里为了避免商业纠纷，名字就不说了

```
##### 非常推荐使用Python3，避免编码及import问题
## PR 要求
##### 请选择 merge 进 master 分支，并且标题写上简短描述，例子 
[优化] 使用PEP8优化代码

## 版本说明

- master 分支：稳定版本，已通过测试
- dev 分支：开发版本，包含一些较稳定的新功能，累计多个功能并测试通过后合并至 prod 分支
- 其他分支：功能开发 (feature) 或问题修复 (bugfix)，属于最新尝鲜版本，可能处于开发中的状态，基本完成后合并至 dev 分支



## 更新日志

- 待续

## 开发者列表

- 待续

## 交流

- qq 403063245
- wx chenjq1985

- 微信公众号
 待续



