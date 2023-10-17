Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     P=int(input("Deliveries:"))
...     C=int(input("Collisions:"))
...     Gained=P*50
...     Lost=C*10
...     F=Gained-Lost
...     print(F)
... 
...     
>>> main()
Deliveries: 6
Collisions: 5
250
