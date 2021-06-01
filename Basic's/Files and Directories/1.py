from pathlib import Path

path = Path('Emails')
print(path.rmdir())

path = Path("Emails")
print(path.exist())

path = Path('Emails')
print(path.mkdir())

path = Path('Emails')
print(path.rmdir())

path = Path()
for file in path.glob('*'):
    print(file)

path = Path()
for file in path.glob('*.py'):
    print(file)