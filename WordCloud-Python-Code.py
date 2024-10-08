import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#readtext

text2021=open('../input/2021-speech/2021.txt',mode='r',encoding='utf-8').read()
text2021=text2021.lower()
print(text2021)

stopword= STOPWORDS
print(stopword)
print(len(stopword))

#removing specific words

cleanText2021=""
cleanText2021=text2021.replace('excellencies',"")
words2021=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2021:
    cleanText2021=cleanText2021.replace(word,"")

print(cleanText2021)

#generating wordcloud

WC1=(WordCloud(background_color='white',stopwords=stopword,height=400,width=800,min_word_length=5)).generate(cleanText2021)

#checking freq of highest freq words

cleanText2021_dictionary=WC1.process_text(text2021)
word_freq={k:v for k,v in sorted(cleanText2021_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC1.words_
print(list(word_freq.items())[:5])

def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC1.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC1,interpolation='bilinear')
plt.axis("off")
plt.show()

#readtext
text2020=open('../input/20202012-speech/2020.txt',mode='r',encoding='utf-8').read()
text2020=text2020.lower()

#removing specific words
cleanText2020=""
cleanText2020=text2020.replace('excellencies',"")
words2020=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2020:
    cleanText2020=cleanText2020.replace(word,"")


#generating wordcloud

WC2=(WordCloud(background_color='white',stopwords=stopword,height=400,width=800,min_word_length=5)).generate(cleanText2020)

#checking freq of highest freq words
cleanText2020_dictionary=WC2.process_text(text2020)
word_freq={k:v for k,v in sorted(cleanText2020_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC2.words_


def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC2.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC2,interpolation='bilinear')
plt.axis("off")
plt.show()

#readtext
text2019=open('../input/20202012-speech/2019.txt',mode='r',encoding='utf-8').read()
text2019=text2019.lower()


#removing specific words
cleanText2019=""
cleanText2019=text2019.replace('excellencies',"")
words2019=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2019:
    cleanText2019=cleanText2019.replace(word,"")


#generating wordcloud

WC3=(WordCloud(background_color='white',stopwords=stopword,height=400,width=800,min_word_length=5)).generate(cleanText2019)

#checking freq of highest freq words
cleanText2019_dictionary=WC3.process_text(text2019)
word_freq={k:v for k,v in sorted(cleanText2019_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC3.words_


def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC3.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC3,interpolation='bilinear')
plt.axis("off")
plt.show()

#readtext
text2018=open('../input/20202012-speech/2018.txt',mode='r',encoding='utf-8').read()
text2018=text2018.lower()


#removing specific words
cleanText2018=""
cleanText2018=text2018.replace('excellencies',"")
words2018=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2018:
    cleanText2018=cleanText2018.replace(word,"")


#generating wordcloud

WC4=(WordCloud(background_color='white',stopwords=stopword,height=1500,width=1500,min_word_length=5)).generate(cleanText2018)

#checking freq of highest freq words
cleanText2018_dictionary=WC4.process_text(text2018)
word_freq={k:v for k,v in sorted(cleanText2018_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC4.words_


def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC4.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC4,interpolation='bilinear')
plt.axis("off")
plt.show()

#readtext
text2017=open('../input/20202012-speech/2017.txt',mode='r',encoding='utf-8').read()
text2017=text2017.lower()


#removing specific words
cleanText2017=""
cleanText2017=text2017.replace('excellencies',"")
words2017=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2017:
    cleanText2017=cleanText2017.replace(word,"")


#generating wordcloud

WC5=(WordCloud(background_color='white',stopwords=stopword,height=1500,width=1500,min_word_length=5)).generate(cleanText2017)

#checking freq of highest freq words
cleanText2017_dictionary=WC5.process_text(text2017)
word_freq={k:v for k,v in sorted(cleanText2017_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC5.words_


def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC5.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC5,interpolation='bilinear')
plt.axis("off")
plt.show()

#readtext
text2016=open('../input/20202012-speech/2016.txt',mode='r',encoding='utf-8').read()
text2016=text2016.lower()


#removing specific words
cleanText2016=""
cleanText2016=text2016.replace('excellencies',"")
words2016=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2016:
    cleanText2016=cleanText2016.replace(word,"")


#generating wordcloud

WC6=(WordCloud(background_color='white',stopwords=stopword,height=1500,width=1500,min_word_length=5)).generate(cleanText2016)

#checking freq of highest freq words
cleanText2016_dictionary=WC6.process_text(text2016)
word_freq={k:v for k,v in sorted(cleanText2016_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC6.words_


def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC6.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC6,interpolation='bilinear')
plt.axis("off")
plt.show()

#readtext
text2015=open('../input/20202012-speech/2015.txt',mode='r',encoding='utf-8').read()
text2015=text2015.lower()


#removing specific words
cleanText2015=""
cleanText2015=text2015.replace('excellencies',"")
words2015=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2015:
    cleanText2015=cleanText2015.replace(word,"")


#generating wordcloud

WC7=(WordCloud(background_color='white',stopwords=stopword,height=1500,width=1500,min_word_length=5)).generate(cleanText2015)

#checking freq of highest freq words
cleanText2015_dictionary=WC7.process_text(text2015)
word_freq={k:v for k,v in sorted(cleanText2015_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC7.words_


def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC7.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC7,interpolation='bilinear')
plt.axis("off")
plt.show()

#readtext
text2014=open('../input/20202012-speech/2014.txt',mode='r',encoding='utf-8').read()
text2014=text2014.lower()


#removing specific words
cleanText2014=""
cleanText2014=text2014.replace('excellencies',"")
words2014=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2014:
    cleanText2014=cleanText2014.replace(word,"")


#generating wordcloud

WC8=(WordCloud(background_color='white',stopwords=stopword,height=1500,width=1500,min_word_length=5)).generate(cleanText2014)

#checking freq of highest freq words
cleanText2014_dictionary=WC8.process_text(text2014)
word_freq={k:v for k,v in sorted(cleanText2014_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC8.words_


def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC8.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC8,interpolation='bilinear')
plt.axis("off")
plt.show()

#readtext
text2013=open('../input/20202012-speech/2013.txt',mode='r',encoding='utf-8').read()
text2013=text2013.lower()


#removing specific words
cleanText2013=""
cleanText2013=text2013.replace('excellencies',"")
words2013=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2013:
    cleanText2013=cleanText2013.replace(word,"")


#generating wordcloud

WC9=(WordCloud(background_color='white',stopwords=stopword,height=1500,width=1500,min_word_length=5)).generate(cleanText2013)

#checking freq of highest freq words
cleanText2013_dictionary=WC9.process_text(text2013)
word_freq={k:v for k,v in sorted(cleanText2016_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC9.words_


def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC9.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC9,interpolation='bilinear')
plt.axis("off")
plt.show()

#readtext
text2012=open('../input/20202012-speech/2012.txt',mode='r',encoding='utf-8').read()
text2012=text2012.lower()


#removing specific words
cleanText2012=""
cleanText2012=text2012.replace('excellencies',"")
words2012=['president','general assembly','will','see','every',
           'fully','others','across','around','countries','see','need','means'
           'world','people','world','united nations',
           'international','state','today','states','member','office','enough','thank','ladies','gentlemen']
for word in words2012:
    cleanText2012=cleanText2012.replace(word,"")


#generating wordcloud

WC10=(WordCloud(background_color='white',stopwords=stopword,height=1500,width=1500,min_word_length=5)).generate(cleanText2012)

#checking freq of highest freq words
cleanText2012_dictionary=WC10.process_text(text2012)
word_freq={k:v for k,v in sorted(cleanText2012_dictionary.items(),reverse=True,key=lambda item:item[1])}
rel_freq=WC10.words_


def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
WC10.recolor(color_func = black_color_func)

#displaying wordcloud
plt.figure( figsize=(20,10) )
plt.imshow(WC10,interpolation='bilinear')
plt.axis("off")
plt.show()

