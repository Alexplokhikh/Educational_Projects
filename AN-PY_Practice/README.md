# 🐍 Python Practice

A collection of Python exercises, examples, and reference snippets created while studying **Python fundamentals at Analiza IT Academy** and through continued independent practice.

Unlike the application projects in this repository, this directory is intended as an evolving **practice workspace** for experimenting with Python syntax, data structures, language concepts, and small programming exercises.

---

## 📖 About

The purpose of this directory is to document my Python learning and provide small, runnable examples of fundamental Python concepts.

The exercises range from basic operations to practical examples showing how Python data structures can be applied to scenarios such as configuration data, server information, IP collections, and other development or DevOps-oriented tasks.

The directory will continue to grow as I practice additional Python concepts.

---

## 📚 Current Topics

### 📋 Lists — `lists.py`

Practice and reference examples covering Python lists and common list operations.

Topics include:

* Creating and accessing lists
* Indexing
* Negative indexing
* Slicing
* Adding and removing elements
* Modifying existing values
* List methods
* Sorting and reversing
* Copying lists
* Nested lists
* Iterating over values
* Working with different data types

---

### 🧱 Data Structures — `data_structures.py`

A comparison and practical exploration of Python's core built-in collection types:

| Structure                     | Ordered | Mutable | Duplicates | Typical Use                        |
| ----------------------------- | ------- | ------- | ---------- | ---------------------------------- |
| **List `[]`**                 | ✅       | ✅       | ✅          | Sequential collections             |
| **Tuple `()`**                | ✅       | ❌       | ✅          | Fixed data and configuration       |
| **Set `{}`**                  | ❌*      | ✅       | ❌          | Unique values and membership tests |
| **Dictionary `{key: value}`** | ✅       | ✅       | Keys: ❌    | Structured key-value data          |

* Sets should not be relied upon for positional ordering.

The exercises demonstrate concepts such as:

* List mutation, indexing, and slicing
* Tuple immutability and unpacking
* Set deduplication
* Set intersections and differences
* Dictionary creation and modification
* Safe dictionary access with `.get()`
* Iterating through key-value pairs
* Choosing an appropriate data structure for a particular task

Some examples use development and DevOps-oriented scenarios such as server configuration, IP collections, and structured metadata.

---

## 🧠 Concepts Practiced

The exercises currently cover concepts including:

* Python syntax and variables
* Built-in data types
* Lists
* Tuples
* Sets
* Dictionaries
* Mutable vs. immutable data
* Indexing and slicing
* Collection methods
* Iteration
* Membership testing
* Set operations
* Dictionary key-value access
* Type conversion
* String formatting
* Basic algorithmic thinking

---

## 📁 Project Structure

```text
AN-PY_Practice/
├── data_structures.py
├── lists.py
└── README.md
```

Additional exercises may be added as new Python topics are studied.

---

## ▶️ Running the Exercises

Python must be installed locally.

Check your installation with:

```bash
python --version
```

or, depending on your environment:

```bash
python3 --version
```

Clone the repository:

```bash
git clone https://github.com/Alexplokhikh/Educational_Projects.git
```

Navigate to the Python practice directory:

```bash
cd Educational_Projects/AN-PY_Practice
```

Then run an individual exercise:

```bash
python lists.py
```

or:

```bash
python data_structures.py
```

On systems where Python 3 uses the `python3` command:

```bash
python3 lists.py
```

---

## ⚠️ Learning Examples

Some snippets are intentionally written to demonstrate Python behavior and may produce an error when executed.

For example, an immutability exercise may deliberately attempt to modify a tuple in order to demonstrate why tuples cannot be changed after creation.

These cases are marked with comments in the source code and are part of the learning material rather than application errors.

---

## 🌐 Hosting

This project does **not** have a GitHub Pages demo.

The files contain Python code that requires a Python runtime and cannot be executed directly by GitHub Pages, which is intended for static web content.

The source code can instead be viewed directly here on GitHub.

---

## 🎓 Project Context

This directory began as part of my Python studies at **Analiza IT Academy** and serves as an ongoing collection of Python practice material.

The `AN-PY` naming follows the convention used throughout this repository:

**AN** → Analiza IT Academy
**PY** → Python
**Practice** → Collection of exercises rather than a single application

For the complete collection of educational projects, see the main [Educational Projects repository](https://github.com/Alexplokhikh/Educational_Projects).

---

## 👤 Author

**Alex Plokhikh**

* [GitHub](https://github.com/Alexplokhikh)
* [Portfolio](https://plokhikh.netlify.app/)
