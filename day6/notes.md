# File Handling Notes

## What is file handling?
File handling means reading data from files and writing data into files using Python.

It is useful for:
- saving output
- reading records
- working with logs
- handling reports
- basic automation tasks

## Opening a file

```python
file = open("sample.txt", "r")
content = file.read()
file.close()
```

## Better way: with open()

```python
with open("sample.txt", "r") as file:
    content = file.read()
```

Using `with open()` is better because Python automatically closes the file.

## File Modes

- `r` → read
- `w` → write and overwrite
- `a` → append
- `x` → create new file

## Reading Methods

- `read()` → reads full file
- `readline()` → reads one line
- `readlines()` → reads all lines as a list

## Key Understanding
- file paths matter
- write mode overwrites existing content
- append mode adds new content
- always prefer `with open()`
