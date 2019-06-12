from pathlib import Path

#Absolute path - exists,mkdir, remove,glob
path = Path("ecommerce")
print(path.exists())
for file in path.glob('*.py'):
    print(file)
