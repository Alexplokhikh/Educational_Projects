import { useState } from "react";
import { type ItemType } from "../types.ts/ItemType.tsx";

export default function Form({
  handleAddItem,
}: {
  handleAddItem: (item: ItemType) => void;
}) {
  const [description, setDescription] = useState<string>("");
  const [quantity, setQuantity] = useState(1);

  function handleSubmit(e: React.SubmitEvent) {
    e.preventDefault();
    if (!description) return;
    const newItem = { description, quantity, packed: false, id: Date.now() };
    console.log(newItem);

    handleAddItem(newItem);
    setQuantity(1);
    setDescription("");
  }

  return (
    <form className="add-form" onSubmit={handleSubmit}>
      <h3>What do you need for your trip? 😎🏖️</h3>
      <select
        value={quantity}
        onChange={(e) => setQuantity(Number(e.target.value))}
      >
        {Array.from({ length: 20 }, (_, i) => i + 1).map((num) => (
          <option value={num} key={num}>
            {num}
          </option>
        ))}
      </select>
      <input
        type="text"
        placeholder="Item..."
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button>Add</button>
    </form>
  );
}
