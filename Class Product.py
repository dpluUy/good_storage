# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:56:08 2023

@author: dacos
"""
class Product:
    
        def __init__(self,inputs):
            self.name=inputs['name']
            self.units=inputs['units']
            self.adq_cost=inputs['adq_cost']
            self.sell_price=inputs['sell_price']
       
        def ad(self,x):
            self.units= self.units +x
            
        def sell(self,x):
            remain= self.units -x
            if remain>=0:
                self.units= self.units-x
                return x
            else:
                print("not sufficient to fitfull sell")                
                return self.units    
                self.units=0
                
        def change_adq_cost(self,x,x_range):
            self.adq_cost[x_range]=x
        
        def change_sell_price(self,x):
            self.sell_price=x
            
           
properties ={
    'name':'sabritas',
    'units':1,
    'adq_cost':{'10':5,
                '100':4,
                '1000':3.5
                },
    'sell_price':20
}            


sabritas=Product(properties)
sabritas.ad(100)
print(sabritas.units)
sabritas.sell(999)
print(sabritas.sell_price)
sabritas.change_sell_price(19)
print(sabritas.sell_price)
sabritas.change_adq_cost(4.2, '100')
print(sabritas.adq_cost)
         