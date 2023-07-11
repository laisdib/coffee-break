import { FileUploader } from "react-drag-drop-files";

import upload from "../../assets/upload.svg";

interface IDragAndDropProps {
  file: File | undefined;
  onChangeFile: (file: File) => void;
}

export function DragAndDrop({file, onChangeFile} : IDragAndDropProps) {
  const fileTypes = ["JPG", "PNG"];

  function handleChange(currentFile: File) {
    onChangeFile(currentFile)
  }

  return (
    <div className="mt-6">
      <p className="text-sm mb-2">Foto da folha</p>
      <FileUploader handleChange={handleChange} types={fileTypes}>
        <div className="h-80 w-[489px] flex flex-col items-center justify-center bg-light-red bg-opacity-20 border-dashed border-2 rounded-md border-opacity-50 border-spacing-2">
          {file ? (
            <p>{file.name}</p>
          ) : (
            <>
              <img src={upload} alt="Upload file icon" className="mb-8" />
              <h1 className="font-bold text-base">
                Selecione uma imagem para fazer upload
              </h1>
              <p className="text-xs">ou arraste e solte uma imagem aqui</p>
            </>
          )}
        </div>
      </FileUploader>
    </div>
  );
}
