## subtitles-converter
这是一个字幕文件格式转换器  
目前仅支持LRC歌词，SRT视频字幕，TXT三者互转  
## 使用方法
这个项目包含多个组件  
每个组件实现一种到另一种格式的转换
如lrc_to_srt srt_to_txt等  
  
每个组件内包含一个convert()函数   
convert函数包含两个参数  
``convert(source_file_location,destination_file_location)``  
即source_file_location：源文件路径   
  destination_file_location：目标文件路径    
  
实例：convert("test.lrc","test.srt")  
**注意，路径须包含文件名及扩展名**  
#### 许可证  
MIT License
