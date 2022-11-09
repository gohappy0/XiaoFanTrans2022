import ybc_trans as trans
import ybc_box as box


#补充代码，使用while语句令下方程序进行无限循环
while True :
    op = box.buttonbox('请选择翻译的类型',
                        ['英译中','中译英','退出'])
    if op == '退出' or op == None:
        #补充代码，使得满足上述条件时，程序可以跳出循环
        break 
    elif op == '英译中':
        words = box.enterbox('请输入翻译内容')
        if words == None:
            break
        if len(words) > 0:
            res = trans.en2zh(words)
            box.msgbox(res)
    elif op == '中译英':
        words = box.enterbox('请输入翻译内容')
        if words == None:
            break
        if len(words) > 0:
            res = trans.zh2en(words)
            box.msgbox(res)
    
