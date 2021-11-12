# 实验题目
- Nobel prize Data analysis
# 实验内容
- 我们都知道诺贝尔奖一般每年都会颁发给在全球做出突出贡献的科学家们，那么本次实验就来认真研究一下1901年至2020年间诺贝尔奖获得者的信息，选用数据集为有关诺贝尔奖获得者的个人信息，共14个特征，主要包括获奖者

  - 姓名 
  - 出生地、死亡地国家代码  
  - 性别 
  - 获奖年份 
  - 研究领域 
  - 共享人数 
  - 任职大学名称、城市、国家
  - 出生月份
  - 年龄
  - 获奖年龄
# 实验步骤
## 原始数据读取

- 首先从官网下载数据集，数据集为csv文件格式，读取代码如下

```python
# 导入相关库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.mode.chained_assignment = None

nobel = pd.read_csv('nobel_final.csv')
```

- 展示出效果如下，可以看到共有923位诺贝尔奖得主，数据集较为庞大
  ![](F:\Visualization\Exp7-zjh\images\1.png)

## 数据分析
### 1.不同国家诺贝尔奖获得者人数
- 首先看到数据我们肯定想了解这些年来哪些国家获得的诺贝尔奖比较多，于是对获奖总人数超过10的国家进行统计并可视化展示

```python
nobel_bron_country = nobel['born_country_code'].value_counts().to_frame()
nobel_bron_country = nobel_bron_country[nobel_bron_country['born_country_code'] >= 10]
# 绘制
plt.figure(figsize=(15, 5))
sns.barplot(x = nobel_bron_country.index , y = 'born_country_code' ,data = nobel_bron_country)
plt.xlabel('Country Code')
plt.ylabel('Number of Nobel winner')
plt.title("Most Nobel Winner Countries")
plt.show()
```

- 实现效果如下，可以看到美国、英国、德国在这些年中获奖人数最多，中国的我们要努力啊！

![](F:\Visualization\Exp7-zjh\images\2.png)

### 2. 不同国家移民出去的获奖者人数
- 同时我们观察发现有很多的获奖者其出生国籍和死亡国籍并不一样，说明他们是移民，那么到底有多少获奖者为移民呢?下面就让我们一起研究一下

```python
imigrate_nobel_winner = nobel.loc[(nobel['born_country_code'] != nobel['died_country_code'])]
imigrate_nobel_winner.dropna(subset=['died_country_code'] , inplace=True)
print( str(len(imigrate_nobel_winner)) + ' Nobel winners that bron country and died country are diffrent')
```
> 190 Nobel winners that bron country and died country are diffrent

- 可以看到共有190位获奖者为移民，那么这些获奖者到底是从哪些国家移民出去的呢？

```python
imigrate_nobel_winner_born_country = imigrate_nobel_winner['born_country_code'].value_counts().to_frame()
imigrate_nobel_winner_born_country = imigrate_nobel_winner_born_country[imigrate_nobel_winner_born_country['born_country_code'] >= 5]

plt.figure(figsize=(15, 5))
sns.barplot(x = imigrate_nobel_winner_born_country.index , y = 'born_country_code' ,data = imigrate_nobel_winner_born_country)
plt.title("Most Immigrants Countries")
plt.xlabel('Country Code')
plt.ylabel('Number of Nobel winner')
plt.show()
```

- 实现效果如下，可以看到从波兰、德国和英国移民出去的获奖者人数最多

![](F:\Visualization\Exp7-zjh\images\3.png)

### 3.不同国家移民进来的获奖者人数
- 那么你肯定会想问，这些科学家最终移民到哪个国家了呢？

```python
imigrate_nobel_winner_died_country = imigrate_nobel_winner['died_country_code'].value_counts().to_frame()
imigrate_nobel_winner_died_country = imigrate_nobel_winner_died_country[imigrate_nobel_winner_died_country['died_country_code'] >= 5]

plt.figure(figsize=(15, 5))
sns.barplot(x = imigrate_nobel_winner_died_country.index , y = 'died_country_code' ,data = imigrate_nobel_winner_died_country)
plt.xlabel('Country Code')
plt.ylabel('Number of Nobel winner')
plt.title("Countries with the highest number of immigrant admissions")
plt.show()
```
- 实现效果如下，可以看到去往美国，英国和德国的科学家人数最多

![](F:\Visualization\Exp7-zjh\images\4.png)

### 4.获奖者男女比例
- 我们还很关注的一个点就是这些获奖者中男女比例到底如何呢？

```python
nobel_winner_gender = nobel['gender'].value_counts().to_frame()

plt.figure(figsize=(15, 5))
sns.barplot(x = nobel_winner_gender.index , y = 'gender' ,data = nobel_winner_gender)
plt.xlabel('Gender')
plt.ylabel('Number of Nobel winner')
plt.title("Gender ratio of winners")
plt.show()
```

- 实现效果如下，可以看到超过850名男性获奖，不到100名女性获奖

![](F:\Visualization\Exp7-zjh\images\5.png)

### 5.每年获奖人数
- 我们知道诺贝尔奖不是每年都会颁发，那么我们好奇的一个点就是每年到底有多少获奖者，下面将获奖人数超过10的年份展示

```python
nobel_winner_year = nobel['year'].value_counts(ascending = True).to_frame()
nobel_winner_year = nobel_winner_year[nobel_winner_year['year'] >= 10]

plt.figure(figsize=(20, 5))
sns.barplot(x = nobel_winner_year.index , y = 'year' ,data = nobel_winner_year)
plt.xlabel('Year')
plt.ylabel('Number of Prize')
plt.title("Number of winners per year")
plt.xticks(rotation = 90)
plt.show()
```

- 实现效果如下,可以看到2001年和2019年的获奖人数是最多的

![](F:\Visualization\Exp7-zjh\images\6.png)

### 6.不同领域每年获奖人数
- 上面我们一直在研究获奖者的国家、性别以及年份信息，其实我们同样好奇的一个点就是到底在哪些领域获奖的人数较多呢？

```python
winner_category = nobel['category'].value_counts().to_frame()

plt.figure(figsize=(20, 5))
sns.barplot(x = winner_category.index , y = 'category' ,data = winner_category)
plt.xlabel('Category')
plt.ylabel('Number of prize')
plt.title("Number of prize per category")
plt.show()
```

- 实现效果如下，医学、物理和化学是获奖人数最多的领域

![](F:\Visualization\Exp7-zjh\images\7.png)

### 7.获奖领域及性别统计
- 现在我们来分析一下不同性别的科学家们在不同研究领域的人数情况

```python
category_and_gender_winner = nobel.groupby('category')['gender'].value_counts().to_frame()
category_and_gender_winner.columns = ['number of winners']
category_and_gender_winner.reset_index(inplace=True)

plt.figure(figsize=(20, 5))
sns.barplot(x = 'category' , y = 'number of winners' , hue = 'gender' ,data = category_and_gender_winner)
plt.xlabel('Category')
plt.ylabel('Number of winners')
plt.title("Category By Gender")
plt.show()
```

- 显示效果如下，女性在和平、文学和医学领域获得最多奖项，但物理、医学和化学领域是男性最受欢迎的领域

![](F:\Visualization\Exp7-zjh\images\8.png)

### 8.获奖者就读大学统计
- 接下来我们分析一下获奖者们大多来自哪些学校,并将前10的学校展示

```python
nobel_university_winner = nobel['name_of_university'].value_counts().to_frame()
nobel_university_winner = nobel_university_winner[nobel_university_winner['name_of_university'] >= 10]

plt.figure(figsize=(10, 5))
sns.barplot(y = nobel_university_winner.index , x = 'name_of_university' ,data = nobel_university_winner ,palette = sns.color_palette('Set2'))
plt.xlabel('Number of Prize')
plt.ylabel('University')
plt.title("Top Universities that Nobel winners studied there")
plt.show()
```
- 显示效果如下，加州大学、哈佛大学和麻省理工学院 (MIT) 是诺贝尔奖获得者就读的前 3 所大学

![](F:\Visualization\Exp7-zjh\images\10.png)

### 9.获奖者就读大学所在国家统计

- 同样我们也很好奇这些获奖者们就读的学校在哪个国家？下面将拥有获奖者大学并且人数超过5的国家展示

```python
nobel_country_winner = nobel['country_of_university'].value_counts().to_frame()
nobel_country_winner = nobel_country_winner[nobel_country_winner['country_of_university'] >= 5]

plt.figure(figsize=(10, 5))
sns.barplot(y = nobel_country_winner.index , x = 'country_of_university' ,data = nobel_country_winner ,palette = sns.color_palette('Set2'))
plt.xlabel('Number of Prize')
plt.ylabel('Country of University')
plt.title("Top Country of universities that Nobel winners studied there")
plt.show()
```

- 显示效果如下，美国 、英国和德国是拥有诺贝尔奖获得者在那里学习的大学最多的国家

![](F:\Visualization\Exp7-zjh\images\11.png)

### 10.**获奖者大学获奖领域分布**
下面我们研究一下这些顶尖大学中其获奖者主要在哪些领域获奖的人数比较多

```python
fulprize_university = nobel[(nobel['name_of_university'] == 'University of California')
                          | (nobel['name_of_university'] == 'Harvard University')
                          | (nobel['name_of_university'] == 'Massachusetts Institute of Technology (MIT)')
                          | (nobel['name_of_university'] == 'Stanford University')
                          | (nobel['name_of_university'] == 'University of Chicago')
                          | (nobel['name_of_university'] == 'University of Cambridge')
                          | (nobel['name_of_university'] == 'California Institute of Technology (Caltech)')
                          | (nobel['name_of_university'] == 'Columbia University')
                          | (nobel['name_of_university'] == 'Princeton University')
                          | (nobel['name_of_university'] == 'Rockefeller University')
                          | (nobel['name_of_university'] == 'MRC Laboratory of Molecular Biology')]
university_and_category = fulprize_university.groupby('name_of_university')['category'].value_counts().to_frame()
university_and_category.columns = ['number of prize']
university_and_category.reset_index(inplace= True)

plt.figure(figsize=(10, 5))
sns.barplot(y = 'name_of_university' , x = 'number of prize' , hue = 'category' , dodge = False ,data = university_and_category ,palette = sns.color_palette('Set2'))
plt.xlabel('Number of Prize')
plt.ylabel('Country of University')
plt.title("Top Universities and distribution of category")
plt.show()
```

- 显示效果如下，可以看到加州大学、斯坦福大学获奖领域比较多，而麻省理工学院 (MIT)和芝加哥大学在经济学领域是强势学科

![](F:\Visualization\Exp7-zjh\images\12.png)

### 11.**不同国家获奖领域分布**

- 看了顶尖大学获奖者的研究领域分布，同样我们也想了解不同国家到底在哪些领域获奖人数分布

```python
nobel_country_winner_new = nobel_country_winner[nobel_country_winner['country_of_university'] >= 10]
fulprize_university_country = nobel[(nobel['country_of_university'] == 'USA')
                          | (nobel['country_of_university'] == 'United Kingdom')
                          | (nobel['country_of_university'] == 'Germany')
                          | (nobel['country_of_university'] == 'France') 
                          | (nobel['country_of_university'] == 'Switzerland')
                          | (nobel['country_of_university'] == 'Japan')
                          | (nobel['country_of_university'] == 'Sweden')
                          | (nobel['country_of_university'] == 'the Netherlands')]
country_university_and_category = fulprize_university_country.groupby('country_of_university')['category'].value_counts().to_frame()
country_university_and_category.columns = ['Number of Prize']
country_university_and_category.reset_index(inplace=True)

plt.figure(figsize=(10, 5))
sns.barplot(y = 'country_of_university' , x = 'Number of Prize' , hue = 'category' ,dodge = False ,data = country_university_and_category ,palette = sns.color_palette('Set2'))
plt.xlabel('Number of Prize')
plt.ylabel('Country of University')
plt.title("Top Counties and distribution of category")
plt.show()
```

- 显示效果如下,美国获奖人数最多，获奖者们主要获奖领域为和平、经济以及医药学，英国获奖者们主要获奖领域为经济学和医药学，而德国获奖者们主要研究领域为经济学、化学和医药学

![](F:\Visualization\Exp7-zjh\images\13.png)

### 12.获奖者目前年龄分布

- 接下来我们分析一下现在获奖者们的年龄分布，看看目前在世的获奖者们已经多少岁了？

```python
plt.figure(figsize=(15, 5))
sns.distplot(nobel['age'])
plt.xlabel('Age')
plt.title('Age get prize distribution')
plt.title("Distribution of Age Winners")
plt.show()
```

- 显示效果如下，可以看到目前大多数获奖者的年龄分布为80岁左右，最年轻的已经40多岁，而年长的已经超过百岁

![](F:\Visualization\Exp7-zjh\images\14.png)

### 13.获奖时年龄分布
- 然后我们分析一下获奖者获奖时的年龄，看看大家到底是在哪个年龄段获得诺贝奖的呢？

```python
plt.figure(figsize=(15, 5))
sns.distplot(nobel['age_get_prize'])
plt.xlabel('Age get prize')
plt.title('Age get prize distribution')
plt.show()
```

- 显示效果如下,可以看到最年轻的获奖者为20多岁，最大的为九十多岁，而大多数还是在60岁左右
![](F:\Visualization\Exp7-zjh\images\15.png)

### 13.得奖者目前年龄分布 VS 得奖时年龄分布
- 接下来我们对比一下获奖者现在的年龄和其获奖时的年龄分布

```python
plt.figure(figsize=(15, 5))
plot = sns.jointplot(x='age', y='age_get_prize' , kind='hex' ,data=nobel)
plot.set_axis_labels('x', 'y', fontsize=12)
plot.ax_joint.set_xlabel('Age')
plot.ax_joint.set_ylabel('Age of winner when get prize')
plt.title("Distribution of Age Winners VS Age of winners when get prize")
plt.tight_layout()
```

- 显示效果如下，从图可以看到目前大多数获奖者都处于年长的状态

![](F:\Visualization\Exp7-zjh\images\16.png)

### 14.按性别划分的平均年龄
- 同时我们也观察一下目前不同性别获奖者们的年龄分布情况

```python
plt.figure(figsize=(15, 5))
sns.boxplot(x='gender', y='age', data=nobel)
plt.ylabel('Age')
plt.xlabel('Gender')
plt.title('Age average seprated by gender')
plt.show()
```

- 实现效果如下，男性的平均年龄约为 81 岁，女性的平均年龄约为 73

![](F:\Visualization\Exp7-zjh\images\17.png)

### 15.不同领域获奖时的年龄分布
- 然后我们分析一下不同性别、不同研究领域的科学家获得诺贝尔奖是的年龄分布

```pytyhon
plt.figure(figsize=(15, 5))
sns.swarmplot(x='gender', y='age_get_prize',hue = 'category', dodge=True , data=nobel)
plt.ylabel('Age when get prize')
plt.xlabel('Gender')
plt.title('Every winner age seperated by gender and prize category')
plt.show()
```

- 实现效果如下，可以看到男性和女性科学家获奖时的年龄大都在60岁左右，男性科学家在物理学领域可以较早获得诺贝尔奖，而女性科学奖在和平领域获得诺贝尔奖较早

![](F:\Visualization\Exp7-zjh\images\18.png)

###  16.不同领域获奖年龄的核密度估计
- 接下来我们分析一下不同研究领域年龄的核密度估计

```python
plt.figure(figsize=(15, 6))
sns.kdeplot(nobel.age[nobel.category == 'chemistry'], label='chemistry', shade=True)
sns.kdeplot(nobel.age[nobel.category == 'economics'], label='economics', shade=True)
sns.kdeplot(nobel.age[nobel.category == 'peace'], label='peace', shade=True)
sns.kdeplot(nobel.age[nobel.category == 'literature'], label='literature', shade=True)
sns.kdeplot(nobel.age[nobel.category == 'physics'], label='physics', shade=True)
sns.kdeplot(nobel.age[nobel.category == 'medicine'], label='medicine', shade=True)
sns.kdeplot(nobel.age[nobel.category == 'chemistry'], label='chemistry', shade=True)
plt.xlabel('Age')
plt.title('Age distribution on category of winners')
```

- 实现效果如下，可以看到要想获奖，大家还是得努力学习，多等几年哈！

![](F:\Visualization\Exp7-zjh\images\19.png)

### 17.多次获奖者和其性别统计

- 通过数据观察我们发现有一些大佬拿奖咳不止一次，那么他们到期是谁呢？

```python
who_won_more_than_one = nobel[nobel.duplicated(subset=['firstname','surname'], keep= False)]\
[["firstname","surname","year", "age_get_prize", "gender","born_country_code", "died_country_code"]].reset_index()
who_won_more_than_one["difference_between_two_prize"] = who_won_more_than_one.groupby("surname")["year"].diff().abs()
who_won_more_than_one.bfill()
```

- 实现效果如下，可以看到Marie、John、Linus和Frederick这四位科学家总共拿了两次诺贝尔奖

![](F:\Visualization\Exp7-zjh\images\20.png)

- 加下来观察一下他们两次获奖之间的时间差是多少

```python
plt.figure(figsize = (16, 7))
sns.barplot(x= "firstname", y= "difference_between_two_prize", hue= "gender",
            dodge=False, data= who_won_more_than_one, palette="Set1")
plt.xlabel("firstname")
plt.ylabel("Years Betwen two Prizes")
plt.title("Time difference between two awards")
plt.show()
```

- 显示效果如下，可以看到两次获奖的时间差最短也要为7年，不得不说还是很厉害啊！

![](F:\Visualization\Exp7-zjh\images\21.png)

# 实验分析
- 这次实验总体上来说难度较大，首先是数据集的选择，这花费了我挺长的时间。选择好数据集后就开始准备可视化数据集，一方面要学习不同的函数实现不同的绘制功能，同时还要构造数据，

**数据集下载链接如下：**https://www.kaggle.com/







