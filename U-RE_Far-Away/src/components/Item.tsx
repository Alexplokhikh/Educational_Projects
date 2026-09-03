import { type ItemType } from "../types.ts/ItemType.tsx";

export default function Item({
  quantity,
  description,
  packed,
  handleDeleteItem,
  handleToggleItem,
  id,
}: ItemType & {
  handleDeleteItem: (id: number) => void;
  handleToggleItem: (id: number) => void;
  id: number;
}) {
  return (
    <li>
      <input
        type="checkbox"
        checked={packed}
        onChange={() => handleToggleItem(id)}
      />
      <span style={packed ? { textDecoration: "line-through" } : {}}>
        {quantity} {description}
      </span>
      <button onClick={() => handleDeleteItem(id)}>❌</button>
    </li>
  );
}
