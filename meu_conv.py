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
        
        pat = re.compile(r'[\w゛〝゜]+([,，、。−‐ー➖~〜～!！?？\t\n\r\s.．・︰‥︙…♡♥❤💓💗💕💖💘💙💚💛💜💞💟😍]+)?',flags=re.U)
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
        #主語を取り出す
        word_conv = self.shugo(word_conv, end)
        #\w+めう+感嘆符で終わる単語
        word_conv = self.gobi(word_conv, end)
        #めうめう→芽兎
        word_conv = self.meishi(word_conv, end)
        #取りこぼしクリーン
        word_conv = self.clean(word_conv, end)
        
        return word_conv
        
    def kantan(self, target_str, end_str):    
        conv_str = target_str
        #print("kantan:"+conv_str)
        
        pat = re.compile(r'^め[うぅ]+[つっ]*$',flags=re.U)
        conv_str = re.sub(pat, 'うん。', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'うん。', conv_str)
        
        pat = re.compile(r'^め[うぅ]+[つっ]*[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'うん!', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'なあに?', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[!！]+[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'あれぇ?', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[?？]+[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'え?!', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[?？!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'え?!', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[♡♥❤💓💗💕💖💘💙💚💛💜💞💟😍]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'えへへっ!', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[-−‐ー➖~～〜―→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'うー', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[-−‐ー➖~～〜―→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'うわぁーッ!', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[-−‐ー➖~～〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'あれー?', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[-−‐ー➖~～〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[!！]+[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'あわわ!??', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[-−‐ー➖~～〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[?？]+[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'なにこれ?!', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[-−‐ー➖~～〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[?？!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'なにこれ?!', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*[wW]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'あはは!', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*(。。|\.\.|．．|・・|︰|‥|︙|…)+[。.．・]?[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, '・・・。', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*(。。|\.\.|．．|・・|︰|‥|︙|…)+[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'これは!', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*(。。|\.\.|．．|・・|︰|‥|︙|…)+[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'あれ?', conv_str)

        pat = re.compile(r'^め[うぅ]+[つっ]*(。。|\.\.|．．|・・|︰|‥|︙|…)+[?？!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'あれ?', conv_str)

        pat = re.compile(r'^め[うぅ]+[。.．・]+[つっ]*[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'うん。', conv_str)

        pat = re.compile(r'^め[うぅ]+[。.．・]+[つっ]*[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'あ!', conv_str)

        pat = re.compile(r'^め[うぅ]+[。.．・]+[つっ]*[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'ん?', conv_str)

        pat = re.compile(r'^め[うぅ]+[。.．・]+[つっ]*[?？!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'あれ?', conv_str)

        #print("kantan_E:"+conv_str)
        return conv_str

    def gobi(self, target_str, end_str):
        conv_str = target_str
        #print("gobi:"+conv_str)
        
        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[\t\n\r\s]+$',flags=re.U)
        conv_str = re.sub(pat, 'よ。', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'よ!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'の?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[?？!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'の?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[♡♥❤💓💗💕💖💘💙💚💛💜💞💟😍]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'よ♥', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[-−‐ー➖~～〜―→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'のだー', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[-−‐ー➖~～〜―→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'のだー!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[-−‐ー➖~～〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'かな?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[-−‐ー➖~～〜――→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+[つっ]*[?？!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'なの?!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[wW]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, '(笑)', conv_str)
        
        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*(。。|\.\.|．．|・・|︰|‥|︙|…)+[。.．・]?[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, '・・・。', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*(。。|\.\.|．．|・・|︰|‥|︙|…)+[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'よっ!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*(。。|\.\.|．．|・・|︰|‥|︙|…)+[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'かな?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*(。。|\.\.|．．|・・|︰|‥|︙|…)+[?？!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'なの!?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[。.．・]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'よ。', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[。.．・]+[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'だ…!', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[。.．・]+[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, '…?', conv_str)

        pat = re.compile(r'(?=[\w゛〝゜]+)(んだ)?め[うぅ]+[つっ]*[。.．・]+[?？!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'なの?', conv_str)
    
        #print("gobi_E:"+conv_str)
        return conv_str
    
    def shugo(self, target_str, end_str):
        conv_str = target_str
        #print("shugo:"+conv_str)
        
        pat = re.compile(r'(め[うぅ]+)+(?=[がをにのとは、,，]+)',flags=re.U)
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

        pat = re.compile(r'^め[うぅ]はめ[うぅ][。.．・︰‥︙…!！?？]*[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, '私は私。', conv_str)
        
        pat = re.compile(r'^め[うぅ]+め[うぅ]([。!！?？\t\n\r\s.．・︰‥︙…♡♥❤💓💗💕💖💘💙💚💛💜💞💟😍]+)?$',flags=re.U)
        conv_str = re.sub(pat, 'そうだね。', conv_str)

        pat = re.compile(r'^め[うぅ]な[。.．・︰‥︙…!！?？]*[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'それな。', conv_str)
        
        pat = re.compile(r'め[うぅ]な[。.．・︰‥︙…]*[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'な。', conv_str) 
        
        pat = re.compile(r'め[うぅ]な[。.．・︰‥︙…]*[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'ね!', conv_str) 

        pat = re.compile(r'め[うぅ]な[。.．・︰‥︙…]*[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'だよね?', conv_str) 
        
        pat = re.compile(r'め[うぅ]な[。.．・︰‥︙…]*[!！?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'かな!?', conv_str) 
        
        pat = re.compile(r'め[うぅ]か[。.．・︰‥︙…]*[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'なの?', conv_str) 
        
        pat = re.compile(r'め[うぅ]か[。.．・︰‥︙…]*[!！]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'か!!', conv_str) 

        pat = re.compile(r'め[うぅ]か[。.．・︰‥︙…]*[?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'なの??', conv_str) 

        pat = re.compile(r'め[うぅ]か[。.．・︰‥︙…]*[!！?？]+[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, '!?', conv_str) 

        #コレーションによる[めﾞ=め]の同一解釈を避けるためにフラグは外す。
        pat = re.compile(r'^(め[゛〝]+|めﾞ)+([つっぅう][゛〝]*|うﾞ|ぅ|づ)+')
        conv_str = re.sub(pat, 'ぐわぁぁぁ・・・', conv_str) 
        
        pat = re.compile(r'(?=[\w゛〝゜]+)(め[゛〝]+|めﾞ)+([つっぅう][゛〝]*|うﾞ|ぅﾞ|づ)+')
        conv_str = re.sub(pat, 'よぉぉぉ・・・', conv_str) 
        
        #ここから修正###################################################
        #むっきゅん:
        pat = re.compile(r'むっきゅん',flags=re.U)
        conv_str = re.sub(pat, 'わぉ', conv_str)       
        
        #こり:これ
        pat = re.compile(r'こり',flags=re.U)
        conv_str = re.sub(pat, 'これ', conv_str)
        
        #めうめうめうめう:私は芽兎です。
        pat = re.compile(r'[る]?[め]+う[う]+[。.．・︰‥︙…!！?？\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'ろぉ〜〜〜ッ!', conv_str)
        
        pat = re.compile(r'^めうめうめうめう[。.．・︰‥︙…!！?？]*[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, '私は芽兎です。', conv_str)
        
        #めめめめうめう！:
        pat = re.compile(r'め[め]+めうめう[!！?？]*',flags=re.U)
        conv_str = re.sub(pat, '♪', conv_str) 
        
        #めうだよ:そうだよ
        pat = re.compile(r'^めうだよ(?=[。.．・︰‥︙…!！?？\t\n\r\s]*)',flags=re.U)
        conv_str = re.sub(pat, 'そうだよ', conv_str) 
        
        #やめるめう…:やめて
        pat = re.compile(r'^やめるめう(?=[。.．・︰‥︙…!！?？\t\n\r\s]*$)')
        conv_str = re.sub(pat, 'やめて', conv_str) 

        #もちゃちゃ:自転車
        pat = re.compile(r'もちゃちゃ|モチャチャ',flags=re.U)
        conv_str = re.sub(pat, '自転車', conv_str) 

        #れべべ:レベル
        pat = re.compile(r'れべべ|レベベ',flags=re.U)
        conv_str = re.sub(pat, 'レベル', conv_str) 

        #あーめう:アーメン
        pat = re.compile(r'あーめう|アーメウ',flags=re.U)
        conv_str = re.sub(pat, 'アーメン', conv_str)
        
        #んちち
        pat = re.compile(r'んちち|ンチチ',flags=re.U)
        conv_str = re.sub(pat, 'うんち', conv_str)
        
        ## ごりり:剛力羅
        pat = re.compile(r'ごりり|ゴリリ',flags=re.U)
        conv_str = re.sub(pat, '剛力羅', conv_str)
        
        ## しんぞぞ:心臓
        pat = re.compile(r'しんぞぞ|シンゾゾ',flags=re.U)
        conv_str = re.sub(pat, '心臓', conv_str)

        #ぼるる:SOUND VOLTEX
        pat = re.compile(r'ぼるる|ボルル',flags=re.U)
        conv_str = re.sub(pat, 'SOUND VOLTEX', conv_str) 

        #ちくぱ:ちくわパフェ
        pat = re.compile(r'ちくパ|ちクパ|ちくぱ|チクパ',flags=re.U)
        conv_str = re.sub(pat, 'ちくわパフェ', conv_str) 
        
        #まりり:まり花
        pat = re.compile(r'まりり|マリリ',flags=re.U)    
        conv_str = re.sub(pat, 'まり花', conv_str) 
        #いぶぶ:イブ
        pat = re.compile(r'いぶぶ|イブブ',flags=re.U)    
        conv_str = re.sub(pat, 'イブ', conv_str) 
        #さきき:咲子
        pat = re.compile(r'さきき|サキキ',flags=re.U)    
        conv_str = re.sub(pat, '咲子', conv_str) 
        #りんりん先生:凛
        pat = re.compile(r'りんりん先生|リンリン先生',flags=re.U)    
        conv_str = re.sub(pat, '凛', conv_str) 
        #ひなひな:日向
        pat = re.compile(r'ひなひな|ヒナヒナ',flags=re.U)    
        conv_str = re.sub(pat, '日向', conv_str) 
        #なつつ:夏陽
        pat = re.compile(r'なつつ|ナツツ',flags=re.U)    
        conv_str = re.sub(pat, '夏陽', conv_str) 
        #こここ:心菜
        pat = re.compile(r'こここ|コココ',flags=re.U)    
        conv_str = re.sub(pat, '心菜', conv_str) 

        #print("special_E:"+conv_str)        
        return conv_str
    
    def clean(self, target_str, end_str):
        conv_str = target_str
        #print("clean:"+conv_str)
        
        pat = re.compile(r'め[うぅ]め[うぅ]',flags=re.U)
        conv_str = re.sub(pat, '芽兎', conv_str) 
        
        pat = re.compile(r'のめ[うぅ]',flags=re.U)
        conv_str = re.sub(pat, 'の芽兎', conv_str) 
        
        #一応漏れていたらキャッチする
        pat = re.compile(r'^め[うぅ]+[つっ]*[-−‐ー➖~~〜～〜―→↓←↑⇔⇒↔↕↖↗↙↘↩↪]+',flags=re.U)
        conv_str = re.sub(pat, 'うー', conv_str)

        pat = re.compile(r'(んだ)?め[うぅ]+[。.．・]?[\t\n\r\s]*$',flags=re.U)
        conv_str = re.sub(pat, 'よ。', conv_str) 
        
        pat = re.compile(r'め[うぅ](?!さー|サー|語)',flags=re.U)
        conv_str = re.sub(pat, '私は', conv_str) 

        #print("clean_E:"+conv_str)
        return conv_str

if __name__ == '__main__':
    main()
    

