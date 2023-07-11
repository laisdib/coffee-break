import { X } from "lucide-react";
import Modal from "react-modal";
// import { Button } from "../Button";

Modal.setAppElement("#root");

interface IResultClassificationPopUp {
  isOpen: boolean;
  resultImage: string;
  results: string[];
  onCloseModal: (isOpen: boolean) => void;
}

export function ResultClassificationPopUp({
  isOpen,
  resultImage,
  results,
  onCloseModal,
}: IResultClassificationPopUp) {
  function closeModal() {
    onCloseModal(false);
  }
  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={closeModal}
      className="w-screen h-screen bg-black bg-opacity-80 flex items-center justify-center text-white"
    >
      <div className="w-[515px] h-[785px] bg-light-dark rounded-md">
        <header className="flex justify-between items-center p-4">
          <h1 className="font-bold text-2xl">Resultado</h1>
          {/* <Button> */}
          <X onClick={closeModal} className="cursor-pointer" />
          {/* </Button> */}
        </header>
        <main className="flex flex-col p-4">
          <img
            src={resultImage}
            alt="Result of the classification"
            className="aspect-video rounded-md"
          />
          <div className="h-16 w-full bg-light-red mt-6 rounded-md flex items-center justify-center font-bold text-3xl">
            {results[0]}
          </div>
          <table className="bg-white bg-opacity-10 mt-6 rounded-md w-full">
            <tr>
              <th className="p-4">Outros resultados</th>
            </tr>
            <tr className="flex flex-col items-center mb-6">
              {results.map(
                (result, index) =>
                  index != 0 && (
                    <td className="border-t-2 w-[80%] border-[#ffffff3f] text-center p-2" key={index}>
                      {result}
                    </td>
                  )
              )}
            </tr>
          </table>
        </main>
      </div>
    </Modal>
  );
}
