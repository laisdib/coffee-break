import { DOMAttributes } from "react";

interface IButtonProps extends DOMAttributes<HTMLButtonElement> {
  name: string;
  disabled?: boolean;
}

export function Button({ name, disabled, onClick }: IButtonProps) {
  return (
    <button
      disabled={disabled}
      onClick={onClick}
      className="h-12 min-w-[490px] mt-8 bg-light-red rounded-md hover:bg-hover-red transition-colors shadow-lg disabled:cursor-not-allowed disabled:bg-hover-red"
    >
      {name}
    </button>
  );
}
