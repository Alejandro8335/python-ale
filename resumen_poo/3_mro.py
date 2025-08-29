
class A:
    def hablar(self):
        print("hola desde A")
        
class A2:
    def hablar(self):
        print("hola desde A2")
              
class B(A):
    def hablar(self):
        print("hola desde B")       
        
class C(A2):
    def hablar(self):
        print("hola desde C")     
          
class D(B,C):
    def hablar(self):
        print("hola desde D") 
         
d = D()
d.hablar()
print(D.__mro__)
A.hablar(D)
#es lo mismo si llamamos a la funcion o a la variable

#como B esta primera se toma toda la familia de B y despues la de C,pq sus herencias son diferentes
#D-B-A-C-A2
#si las dos heredaran de A primero se tomaria B despues la de C y por ultimo A
#D-B-C-A
