#!/usr/bin/env python
# coding: utf-8

# In[93]:


# 商品
class Food():
    """ 寫下商品的基本行為 """
    
    # 身家資料
    def __init__(self, special="一般"):
        self.special = special

    # 自我介紹
    def describe(self, name="產品"):
        print(f"我是{self.special}{name}")


# In[94]:


# 工廠
class McDonald():
    """ 寫下工廠的基本行為 """

    # 工廠負責產生的食物
    def __init__(self, food=Food):
        self.food = food
    
    def make_food(self, special=None):
        if special:
            return self.food(special).describe()
        else:
            return self.food().describe()


# In[95]:


McDonald().make_food()


# In[96]:


McDonald().make_food("台肥新")


# In[97]:


# 商品: 薯條
class Fries(Food):
    
    # 身家資料     
    def __init__(self, special="加鹽"):
        super(Fries, self).__init__(special)
        
    # 自我介紹
    def describe(self, name="薯條"):
        super(Fries, self).describe(name)


# In[98]:


Fries().describe()


# In[99]:


# 工廠: 炸薯條仔
class FriesMaker(McDonald):
    
     # 炸薯條仔負責產生的食物
    def __init__(self, food=Fries):
        super(FriesMaker, self).__init__(food)

    def make_food(self, special=None):
        super(FriesMaker, self).make_food(special)


# In[100]:


FriesMaker().make_food("健康不加鹽")


# In[101]:


FriesMaker().make_food()


# In[ ]:





# In[ ]:




