## swapsub
这是一个字幕文件格式转换器  
支持LRC，SRT，TXT三者互转  

## 安装
推荐使用pip包管理器进行安装  
```
pip install swapsub
```  

## 使用方法

### 导入swapsub
```python
import swapsub
```  

### load()函数 
load函数用于加载并预处理字幕文件  
```python
swapsub.load(path)

#path:文件路径 
```  
load()函数将返回一个列表，里面包含里经预处理后的数据  

### convert()函数 
convert函数用于转换并将转换后的文件储存到指定位置  
```python
swapsub.convert(data,path)

#data:load()函数返回的值  
#path:文件路径
```  
 
### 示例
```python
sub = swapsub.load("a.lrc")  
swapsub.convert(sub,"/home/cybytess/b.srt")
```

**注意，路径须包含文件名及扩展名**  

## 许可证  
**GPL-3.0**
