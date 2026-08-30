# 🌱 Node Farm

A small server-side product catalog built with **Node.js** as part of a Udemy course.

![2025-03-25 16_02_33-NODE FARM](https://github.com/user-attachments/assets/a8686572-1f5b-42d6-bade-99da1f75b9d0)

The project focuses on understanding the fundamentals of Node.js without relying on frameworks such as Express. It implements an HTTP server, routing, filesystem operations, JSON data parsing, and basic server-side HTML templating using Node's built-in modules.

---

## 📖 About the Project

**Node Farm** is a simple product catalog application that dynamically generates HTML pages using product information stored in a JSON file.

The application provides an overview page containing multiple product cards. Each card links to an individual product page, with the appropriate product selected through a URL query parameter.

Rather than maintaining separate HTML pages for every product, the server reads reusable HTML templates and dynamically replaces placeholders with the corresponding product data.

This project was created to practice how a basic web server works underneath higher-level frameworks such as Express.

---

## ✨ Features

* Node.js HTTP server
* Server-side routing
* Product overview page
* Dynamically generated product pages
* JSON-based product data
* Reusable HTML templates
* URL and query-string parsing
* Server-side placeholder replacement
* Static API endpoint returning product data
* Reusable template rendering function
* No external runtime dependencies or web frameworks

---

## 🛠️ Built With

* **Node.js**
* **HTML5**
* **JSON**
* Node.js built-in modules:

  * `http`
  * `fs`
  * `url`

The application intentionally avoids frameworks such as Express so that the underlying Node.js concepts remain visible.

---

## 🧠 Concepts Practiced

### Creating an HTTP Server

The application uses Node's built-in `http` module to create a server and respond to incoming requests.

```js id="sx74wm"
const server = http.createServer((req, res) => {
  // Handle request
});
```

The server listens locally on:

```text id="f65q89"
http://localhost:8000
```

---

### Routing

Different responses are returned depending on the requested pathname.

The application handles routes including:

```text id="e35jpk"
/overview
/product
/api
```

The root route `/` also displays the product overview.

This provides a basic introduction to routing before using dedicated frameworks such as Express.

---

### Reading Data from the File System

Product information is stored in a JSON file and loaded using Node's built-in `fs` module.

The data is read once when the application starts:

```js id="d33xaq"
const data = fs.readFileSync(
  `${__dirname}/dev-data/data.json`,
  "utf-8"
);

const dataObj = JSON.parse(data);
```

Reading the shared product data during application initialization avoids unnecessarily reading the same file again for every incoming request.

---

### Server-Side HTML Templates

Instead of creating a separate HTML document for every product, the application uses reusable templates.

The project contains templates for:

* Product overview
* Product cards
* Individual product pages

Placeholders inside those templates are replaced with actual product information before the HTML is returned to the browser.

This demonstrates the basic idea behind **server-side rendering and templating**.

---

### Dynamic Product Pages

Products are selected through URL query parameters.

![2025-03-25 16_02_57-Goat and Sheep Cheese 🧀 ___ NODE FARM](https://github.com/user-attachments/assets/2b97c4cb-e797-40af-89be-af2bf64de87a)

For example:

```text id="3u1wp9"
http://localhost:8000/product?id=0
```

The server reads the requested product ID, retrieves the matching object from the product data, inserts its values into the product template, and sends the generated HTML back to the browser.

---

### URL Parsing

The built-in Node.js `url` module is used to separate the requested pathname from its query parameters.

This makes it possible to distinguish between routes while also retrieving information such as the requested product ID.

---

## 🔀 Application Flow

A simplified version of the application's request flow looks like this:

```text id="x99epc"
Browser Request
      │
      ▼
 Node.js Server
      │
      ▼
 Parse URL
      │
      ├───────────────┐
      │               │
      ▼               ▼
  /overview        /product?id=X
      │               │
      ▼               ▼
 Product Data      Find Product
      │               │
      ▼               ▼
 Card Template     Product Template
      │               │
      └───────┬───────┘
              │
              ▼
        Generate HTML
              │
              ▼
        Browser Response
```

---

## 📁 Project Structure

```text id="9jx8ha"
UD-N_Node-Farm/
│
├── dev-data/
│   └── data.json
│
├── templates/
│   ├── template-card.html
│   ├── template-overview.html
│   └── template-product.html
│
├── index.js
└── README.md
```

### `dev-data/`

Contains the JSON dataset used to populate the product catalog.

### `templates/`

Contains reusable HTML templates used to generate the pages returned by the server.

### `index.js`

Contains the application's Node.js server, routing logic, data loading, URL parsing, and template-rendering functionality.

---

## 🚀 Run Locally

### Prerequisites

You need **Node.js** installed on your machine.

Check your installation with:

```bash id="2w1zzm"
node --version
```

### Clone the Repository

```bash id="0b6fbn"
git clone https://github.com/Alexplokhikh/Educational_Projects.git
```

Navigate to the project:

```bash id="k7f2cq"
cd Educational_Projects/UD-N_Node-Farm
```

Start the server:

```bash id="8uoxcg"
node index.js
```

The application should report that it is listening on port `8000`.

Open your browser and visit:

```text id="m1znfk"
http://localhost:8000
```

or:

```text id="p1ybwf"
http://localhost:8000/overview
```

---

## 🛣️ Available Routes

| Route           | Description              |
| --------------- | ------------------------ |
| `/`             | Product overview         |
| `/overview`     | Product catalog overview |
| `/product?id=X` | Individual product page  |
| `/api`          | Raw product data as JSON |

For example:

```text id="yuhnh7"
http://localhost:8000/product?id=0
```

returns the page generated for the first product in the dataset.

---

## 🌐 Hosting

Unlike the static frontend exercises in this repository, **Node Farm cannot be hosted directly through GitHub Pages**.

GitHub Pages serves static files but does not provide a Node.js runtime capable of executing `index.js` and running the HTTP server.

The source code remains available here on GitHub and the project can be run locally using Node.js.

---

## 🎓 Project Context

This is an **educational backend project** created while studying Node.js through Udemy.

The `UD-N` naming follows the convention used throughout this repository:

**UD** → Udemy
**N** → Node.js
**Node-Farm** → Product catalog / routing exercise

The project intentionally uses Node.js's native APIs rather than a web framework. Its purpose is to understand concepts such as HTTP requests and responses, routing, filesystem access, URL parsing, and server-side rendering before abstracting those concepts behind frameworks such as Express.

For the complete collection of exercises and educational projects, see the main [Educational Projects repository](https://github.com/Alexplokhikh/Educational_Projects).

---

## 👤 Author

**Alex Plokhikh**

* [GitHub](https://github.com/Alexplokhikh)
* [Portfolio](https://plokhikh.netlify.app/)
