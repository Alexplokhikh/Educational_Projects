# 🪟 Modal Window

A small interactive frontend exercise demonstrating how to build and control a **modal window using vanilla JavaScript**.

The project focuses on DOM manipulation, event handling, CSS classes, and implementing several common ways of opening and closing a modal dialog.

🌐 **[View the Live Demo](https://alexplokhikh.github.io/Educational_Projects/H-WD_Modal-window/)**

---

## 📖 About the Project

This project implements a simple modal-window interface using **HTML, CSS, and vanilla JavaScript**.

The page contains multiple buttons that can open the same modal dialog. When opened, the modal is displayed above a semi-transparent blurred overlay.

The modal can then be closed in several ways:

* Clicking the **×** close button
* Clicking outside the modal on the **overlay**
* Pressing the **Escape (`Esc`) key**

The exercise demonstrates how JavaScript can control the visibility and behavior of UI components by manipulating CSS classes.

---

## ✨ Features

* Multiple buttons connected to the same modal
* Reusable modal opening logic
* Reusable modal closing logic
* Background overlay
* Background blur effect
* Close button interaction
* Close by clicking outside the modal
* Close with the `Escape` key
* CSS class-based visibility control
* No external libraries or frameworks

---

## 🛠️ Built With

* **HTML5** — page and modal structure
* **CSS3** — layout, styling, overlay, and modal presentation
* **JavaScript** — DOM interaction and event handling

The project uses only native browser technologies.

---

## 🧠 Concepts Practiced

The project provides practice with several fundamental frontend and JavaScript concepts:

### DOM Selection

Selecting individual and multiple elements using:

```js
document.querySelector();
document.querySelectorAll();
```

### Event Listeners

Responding to different types of user interaction:

```js
element.addEventListener();
```

including:

* Mouse clicks
* Keyboard input

### CSS Class Manipulation

Changing an element's state by adding and removing CSS classes:

```js
element.classList.add();
element.classList.remove();
element.classList.contains();
```

### Reusable Functions

Separating behavior into reusable functions such as:

```js
openModal();
closeModal();
```

instead of repeating the same DOM operations for every interaction.

### Keyboard Events

Listening for the `keydown` event and checking the pressed key to allow the modal to close when the user presses `Escape`.

---

## 🖱️ How It Works

1. Click any of the **Show modal** buttons.
2. The modal and background overlay become visible.
3. Close the modal using one of three methods:

   * Click the **×** button
   * Click the darkened background
   * Press **Esc**
4. The modal and overlay are hidden again.

---

## 📁 Project Structure

```text
H-WD_Modal-window/
├── index.html
├── style.css
├── script.js
└── README.md
```

---

## 🚀 Run Locally

No dependencies, package manager, or build process are required.

Clone the repository:

```bash
git clone https://github.com/Alexplokhikh/Educational_Projects.git
```

Navigate to the project:

```bash
cd Educational_Projects/H-WD_Modal-window
```

Then open:

```text
index.html
```

directly in your browser.

Alternatively, the project can be served using a local development server such as the **VS Code Live Server** extension.

---

## 🌐 Live Demo

The project is hosted through GitHub Pages:

**[Open Modal Window Demo →](https://alexplokhikh.github.io/Educational_Projects/H-WD_Modal-window/)**

---

## 🎓 Project Context

This is a small **independent / at-home frontend practice project** created while learning fundamental web-development concepts.

The `H-WD` naming follows the convention used throughout this repository:

**H** → Independent / at-home practice
**WD** → Web Design / Web Development
**Modal-window** → The UI component explored in the exercise

Although categorized under `WD`, the exercise also includes basic **JavaScript DOM manipulation and event handling**.

The project is intentionally small and framework-free, with the focus placed on understanding how a common interactive UI component works using native browser APIs.

For the complete collection of exercises and educational projects, see the main [Educational Projects repository](https://github.com/Alexplokhikh/Educational_Projects).

---

## 👤 Author

**Alex Plokhikh**

* [GitHub](https://github.com/Alexplokhikh)
* [Portfolio](https://plokhikh.netlify.app/)
