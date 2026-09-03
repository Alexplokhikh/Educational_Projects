import { useState } from "react";
import Item from "./Item.tsx";
import { type ItemType } from "../types.ts/ItemType.tsx";

export default function PackingList({
  items,
  handleDeleteItem,
  handleToggleItem,
  handleClearList,
}: {
  items: ItemType[];
  handleDeleteItem: (id: number) => void;
  handleToggleItem: (id: number) => void;
  handleClearList: () => void;
}) {
  const [sortBy, setSortBy] = useState<string>("input");
  const sortedItems = [...items];
  if (sortBy === "description") {
    sortedItems.sort((a, b) => a.description.localeCompare(b.description));
  } else if (sortBy === "packed") {
    sortedItems.sort((a, b) => Number(a.packed) - Number(b.packed));
  }

  return (
    <div className="list">
      <ul>
        {sortedItems.map((item: ItemType) => (
          <Item
            id={item.id}
            description={item.description}
            quantity={item.quantity}
            packed={item.packed}
            handleDeleteItem={handleDeleteItem}
            handleToggleItem={handleToggleItem}
            key={item.id}
          />
        ))}
      </ul>

      <div className="actions">
        <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
          <option value="input">Input order</option>
          <option value="description">Description</option>
          <option value="packed">Packed status</option>
        </select>
        <button onClick={handleClearList}>Clear List</button>
      </div>
    </div>
  );
}
