import { useState } from "react";
import "./App.css";
import Logo from "./components/Logo.tsx";
import Form from "./components/Form.tsx";
import PackingList from "./components/PackingList.tsx";
import Stats from "./components/Footer.tsx";
import { type ItemType } from "./types.ts/ItemType.tsx";

function App() {
  const [items, setItems] = useState<ItemType[]>(
    localStorage.getItem("items")
      ? JSON.parse(localStorage.getItem("items")!)
      : [],
  );

  function handleAddItem(item: ItemType) {
    setItems((items) => [...items, item]);
    localStorage.setItem("items", JSON.stringify([...items, item]));
  }

  function handleDeleteItem(id: number) {
    setItems((items) => items.filter((item) => item.id !== id));
    localStorage.setItem(
      "items",
      JSON.stringify(items.filter((item) => item.id !== id)),
    );
  }

  function handleToggleItem(id: number) {
    setItems((items) =>
      items.map((item) =>
        item.id === id ? { ...item, packed: !item.packed } : item,
      ),
    );
    localStorage.setItem(
      "items",
      JSON.stringify(
        items.map((item) =>
          item.id === id ? { ...item, packed: !item.packed } : item,
        ),
      ),
    );
  }

  function handleClearList() {
    if (window.confirm("Are you sure you want to clear the list?")) {
      setItems([]);
      localStorage.setItem("items", JSON.stringify([]));
    }
  }

  return (
    <div className="app">
      <Logo />
      <Form handleAddItem={handleAddItem} />
      <PackingList
        items={items}
        handleDeleteItem={handleDeleteItem}
        handleToggleItem={handleToggleItem}
        handleClearList={handleClearList}
      />
      <Stats items={items} />
    </div>
  );
}

export default App;
