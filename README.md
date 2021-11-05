## Swapsub-core
这是一个字幕文件格式转换器  
目前支持LRC，SRT，TXT，ASS四者互转  
## 使用方法

### load()函数 
load函数用于加载并预处理字幕文件  
``load(path)``  
path:文件路径  
load()函数将返回一个列表，里面包含里经预处理后的数据  

### convert()函数 
convert函数用于转换并将转换后的文件储存到指定位置  
``convert(data,path)``  
data:load()函数返回的值  
path:文件路径
 
### 示例
``sub = load("a.lrc")``  
``convert(sub,"/home/cybytess/b.srt")``

**注意，路径须包含文件名及扩展名**  

## 许可证  
GPL 3.0
