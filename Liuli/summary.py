import os
dir_name = []
for root, dirs, files in os.walk("."):
    for name in dirs:
        dir_name.append(name)
for i in dir_name:
    yy_mm = i.split('.')
    if(len(yy_mm) == 2):
        yy = yy_mm[0]
        mm = yy_mm[1]
        if (mm[0] == '0'):
            mm = mm[1]
        file_name = '%s年%s月'%(yy, mm)
        first_file = '%s%s01.webp'%(yy_mm[0], yy_mm[1])
        fw = open(file_name+'号.md', 'w', encoding='UTF-8')
        fr = open(os.path.join(i, first_file), 'rb')
        get = fr.read(30)
        fr.close()
        w1 = ((get[27]&0xff)<<8)|(get[26]&0xff)
        h1 = ((get[29]&0xff)<<8)|(get[28]&0xff)
        fw.write('---\n')
        fw.write('title: '+file_name+'\n')
        fw.write('date: '+yy_mm[0]+'-'+yy_mm[1]+'-01 00:00:00\n')
        fw.write('tags: 壁纸包\n')
        fw.write('cover: https://cdn.jsdelivr.net/gh/qdddz/pic@master/Liuli/%s/%s%s01.webp\n'%(i, yy_mm[0], yy_mm[1]))
        fw.write('coverWidth: %d\n'%w1)
        fw.write('coverHeight: %d\n'%h1)
        fw.write('---\n')
        sumn = 0
        for root, dirs, files in os.walk(i):
            for name in files:
                sumn += 1
        fw.write('## 概述  \n')
        fw.write('本合集收录{0}琉璃神社壁纸包，使用[Imagine](https://github.com/meowtec/Imagine)转换为Webp文件格式，并对图片进行80%质量压缩，如果无法显示图片，请更换浏览器。或访问 [图像源站JPG/PNG格式](http://one3.ge2dan.top/Pic/Liuli/Local/{1}) [图像源站WEBP格式](http://one3.ge2dan.top/Pic/Liuli/Online/{1})  \n'.format(file_name, i))
        fw.write('<!--more-->  \n')
        for root, dirs, files in os.walk(i):
            for name in files:
                if (name.find('webp')):
                    fr = open(os.path.join(i,name), "rb")
                    get = fr.read(30)
                    fr.close()
                    w = ((get[27]&0xff)<<8)|(get[26]&0xff)
                    h = ((get[29]&0xff)<<8)|(get[28]&0xff)
                    fw.write('## %s  \n![%s](https://cdn.jsdelivr.net/gh/qdddz/pic@master/Liuli/%s/%s)  \n图片分辨率: %dx%d  \n'%(name[6:8], name[6:8], i, name, w, h))
                else:
                    print(name)
        fw.close()
    else: continue
