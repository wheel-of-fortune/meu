# -*- coding: utf-8 -*-

import re

def main():
    pass
class MeuConv:
    def __init__(self):
        pass

    def go_conv(self, target_str):
        #print("input:"+target_str)
        conv_str = target_str
        
        pat = re.compile(r'めう([「(]+)',flags=re.U)
        conv_str = re.sub(pat, '芽兎\g<1>', conv_str) 
        
        pat = re.compile(r'[\w゛〝゜]+([、。!！?？\t\n\r\s.．・︰‥︙…♡♥❤💓💗💕💖💘💙💚💛💜💞💟😍]+)?',flags=re.U)
        conv_str = re.sub(pat, self.word_conv, conv_str)
        
        #print("-"*10)
        #print("out_put:"+conv_str)
        #print("-"*30)
        
        return conv_str
        
    def word_conv(self, match_obj):
        word = match_obj.group(0)
        if match_obj.group(1):
            end = match_obj.group(1)
        else:
            end = ""
            
        #print('word:'+word)
        #print('end:'+end)
        
        word_conv = word
        #短い単語からマッチさせる
        #特別な言い回し
        word_conv = self.special(word_conv, end)
        #めう+感嘆符だけで終わる単語
        word_conv = self.kantan(word_conv, end)
        #\w+めう+感嘆符で終わる単語
        word_conv = self.gobi(word_conv, end)
        #主語を取り出す
        word_conv = self.shugo(word_conv, end)
        #めうめう→芽兎
        word_conv = self.meishi(word_conv, end)
        #取りこぼしクリーン
        word_conv = self.clean(word_conv, end)
        
        return word_conv
        
    def kantan(self, target_str, end_str):    
        conv_str = target_str
        #print("kantan:"+conv_str)
        
        pat = re.compile(r'^め[うぅ]+$',flags=re.U)
        conv_str = re.sub(pat, 'うん。', conv_str)

        pat = re.compile(r'^め[うぅ]+[\t\n\r\s]+$',flags=re.U)
        conv_str = re.sub(pat, 'うん。', conv_str)
        
        pat = re.compile(r'^め[うぅ]+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'うん!', conv_str)

        pat = re.compile(r'^め[うぅ]+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'なあに?', conv_str)

        pat = re.compile(r'^め[うぅ]+[!！]+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'あれぇ?', conv_str)

        pat = re.compile(r'^め[うぅ]+[?？]+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'え?!', conv_str)

        pat = re.compile(r'^め[うぅ]+[?？!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'え?!', conv_str)

        pat = re.compile(r'^め[うぅ]+[♡♥❤💓💗💕💖💘💙💚💛💜💞💟😍]+$',flags=re.U)
        conv_str = re.sub(pat, 'えへへっ!', conv_str)

        pat = re.compile(r'^め[うぅ]+[-−‐ー➖~〜―→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+$',flags=re.U)
        conv_str = re.sub(pat, 'うー', conv_str)

        pat = re.compile(r'^め[うぅ]+[-−‐ー➖~〜―→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'うわぁーッ!', conv_str)

        pat = re.compile(r'^め[うぅ]+[-−‐ー➖~〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'あれー?', conv_str)

        pat = re.compile(r'^め[うぅ]+[-−‐ー➖~〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[!！]+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'あわわ!??', conv_str)

        pat = re.compile(r'^め[うぅ]+[-−‐ー➖~〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[?？]+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'なにこれ?!', conv_str)

        pat = re.compile(r'^め[うぅ]+[-−‐ー➖~〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[?？!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'なにこれ?!', conv_str)

        pat = re.compile(r'^め[うぅ]+[wW]+$',flags=re.U)
        conv_str = re.sub(pat, 'あはは!', conv_str)

        pat = re.compile(r'^め[うぅ]+(。。|\.\.|．．|・・|︰|‥|︙|…)+[。.．・]?$',flags=re.U)
        conv_str = re.sub(pat, '・・・。', conv_str)

        pat = re.compile(r'^め[うぅ]+(。。|\.\.|．．|・・|︰|‥|︙|…)+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'これは!', conv_str)

        pat = re.compile(r'^め[うぅ]+(。。|\.\.|．．|・・|︰|‥|︙|…)+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'あれ?', conv_str)

        pat = re.compile(r'^め[うぅ]+(。。|\.\.|．．|・・|︰|‥|︙|…)+[?？!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'あれ?', conv_str)

        pat = re.compile(r'^め[うぅ]+[。.．・]+$',flags=re.U)
        conv_str = re.sub(pat, 'うん。', conv_str)

        pat = re.compile(r'^め[うぅ]+[。.．・]+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'あ!', conv_str)

        pat = re.compile(r'^め[うぅ]+[。.．・]+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'ん?', conv_str)

        pat = re.compile(r'^め[うぅ]+[。.．・]+[?？!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'あれ?', conv_str)

        #print("kantan_E:"+conv_str)
        return conv_str

    def gobi(self, target_str, end_str):
        conv_str = target_str
        #print("gobi:"+conv_str)
        
        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[\t\n\r\s]+$',flags=re.U)
        conv_str = re.sub(pat, 'よ。', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'よ!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'の?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[?？!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'の?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[♡♥❤💓💗💕💖💘💙💚💛💜💞💟😍]+$',flags=re.U)
        conv_str = re.sub(pat, 'よ♥', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[-−‐ー➖~〜―→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+$',flags=re.U)
        conv_str = re.sub(pat, 'だー', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[-−‐ー➖~〜―→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'だー!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[-−‐ー➖~〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'かな?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[-−‐ー➖~〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[?？!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'なの?!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[wW]+$',flags=re.U)
        conv_str = re.sub(pat, '(笑)', conv_str)
        
        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+(。。|\.\.|．．|・・|︰|‥|︙|…)+[。.．・]?$',flags=re.U)
        conv_str = re.sub(pat, '・・・。', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+(。。|\.\.|．．|・・|︰|‥|︙|…)+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'よっ!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+(。。|\.\.|．．|・・|︰|‥|︙|…)+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'かな?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+(。。|\.\.|．．|・・|︰|‥|︙|…)+[?？!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'なの!?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[。.．・]+$',flags=re.U)
        conv_str = re.sub(pat, 'よ。', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[。.．・]+[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'だ…!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[。.．・]+[?？]+$',flags=re.U)
        conv_str = re.sub(pat, '…?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[。.．・]+[?？!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'なの?', conv_str)
    
        #print("gobi_E:"+conv_str)
        return conv_str
    
    def shugo(self, target_str, end_str):
        conv_str = target_str
        #print("shugo:"+conv_str)
        
        pat = re.compile(r'^め[うぅ]+(?=[がをにのとは、])',flags=re.U)
        conv_str = re.sub(pat, '私', conv_str)
        
        #print("shugo_E:"+conv_str)
        return conv_str
    
    def meishi(self, target_str, end_str):
        conv_str = target_str
        #print("meishi:"+conv_str)
        
        pat = re.compile(r'め[うぅ]め[うぅ]([^$])',flags=re.U)
        conv_str = re.sub(pat, '芽兎\g<1>', conv_str) 

        pat = re.compile(r'め[うぅ]ちゃん',flags=re.U)
        conv_str = re.sub(pat, '芽兎', conv_str) 


        #print("meishi_E:"+conv_str)
        return conv_str

    def special(self, target_str, end_str):
        conv_str = target_str
        #print("special:"+conv_str)

        pat = re.compile(r'^め[うぅ]はめ[うぅ][。.．・︰‥︙…!！?？]*$',flags=re.U)
        conv_str = re.sub(pat, '私は私。', conv_str)
        
        pat = re.compile(r'^め[うぅ]+め[うぅ]([。!！?？\t\n\r\s.．・︰‥︙…♡♥❤💓💗💕💖💘💙💚💛💜💞💟😍]+)?$',flags=re.U)
        conv_str = re.sub(pat, 'そうだね。', conv_str)

        pat = re.compile(r'^め[うぅ]な[。.．・︰‥︙…!！?？]*$',flags=re.U)
        conv_str = re.sub(pat, 'それな。', conv_str)
        
        pat = re.compile(r'め[うぅ]な[。.．・︰‥︙…]*$',flags=re.U)
        conv_str = re.sub(pat, 'な。', conv_str) 
        
        pat = re.compile(r'め[うぅ]な[。.．・︰‥︙…]*[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'ね!', conv_str) 

        pat = re.compile(r'め[うぅ]な[。.．・︰‥︙…]*[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'だよね?', conv_str) 
        
        pat = re.compile(r'め[うぅ]な[。.．・︰‥︙…]*[!！?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'かな!?', conv_str) 
        
        pat = re.compile(r'め[うぅ]か[。.．・︰‥︙…]*$',flags=re.U)
        conv_str = re.sub(pat, 'なの?', conv_str) 
        
        pat = re.compile(r'め[うぅ]か[。.．・︰‥︙…]*[!！]+$',flags=re.U)
        conv_str = re.sub(pat, 'か!!', conv_str) 

        pat = re.compile(r'め[うぅ]か[。.．・︰‥︙…]*[?？]+$',flags=re.U)
        conv_str = re.sub(pat, 'なの??', conv_str) 

        pat = re.compile(r'め[うぅ]か[。.．・︰‥︙…]*[!！?？]+$',flags=re.U)
        conv_str = re.sub(pat, '!?', conv_str) 

        #コレーションによる[めﾞ=め]の同一解釈を避けるためにフラグは外す。
        pat = re.compile(r'^(め[゛〝]+|めﾞ)+([ぅう][゛〝]+|うﾞ|ぅﾞ)+')
        conv_str = re.sub(pat, 'ぐわぁぁぁ・・・', conv_str) 
        
        pat = re.compile(r'(?=[\w゛〝゜]+)(め[゛〝]+|めﾞ)+([ぅう][゛〝]+|うﾞ|ぅﾞ)+')
        conv_str = re.sub(pat, 'よぉぉぉ・・・', conv_str) 
        
        #print("special_E:"+conv_str)        
        return conv_str
    
    def clean(self, target_str, end_str):
        conv_str = target_str
        #print("clean:"+conv_str)
        
        pat = re.compile(r'め[うぅ]め[うぅ]',flags=re.U)
        conv_str = re.sub(pat, '芽兎', conv_str) 
        
        pat = re.compile(r'のめ[うぅ]',flags=re.U)
        conv_str = re.sub(pat, 'の芽兎', conv_str) 

        pat = re.compile(r'(んだ)?め[うぅ]+[。.．・]?$',flags=re.U)
        conv_str = re.sub(pat, 'よ。', conv_str) 
        
        pat = re.compile(r'め[うぅ](?!さー|サー|語)',flags=re.U)
        conv_str = re.sub(pat, '私は', conv_str) 

        #print("clean_E:"+conv_str)
        return conv_str

if __name__ == '__main__':
    main()
    
