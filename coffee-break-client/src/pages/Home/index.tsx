import { useState } from "react";
import logo from "../../assets/logo.svg";

import { InputField } from "../../components/InputField";
import { Loader } from "../../components/Loader";
import { ResultClassificationPopUp } from "../../components/ResultClassificationPopUp";
import { Button } from "../../components/Button";
import { DragAndDrop } from "../../components/DragAndDrop";

export function Home() {
  const [isLoading, setIsLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const [plantId, setPlantId] = useState<number>();
  const [file, setFile] = useState<File | undefined>();


  console.log(plantId, file);

  function handleOnSubmit(event: React.FormEvent) {
    event.preventDefault();

    setIsLoading(true);

    setTimeout(() => {
      setIsLoading(false);
      setIsOpen(true);
    }, 2000);
  }

  return (
    <article className="w-screen min-h-screen bg-primary-dark flex flex-col items-center text-white font-sans">
      <header className=" flex flex-col justify-center items-center mt-32">
        <aside className="flex flex-col items-center">
          <img src={logo} alt="Coffee Break Logo" className="mb-4" />
          <h1 className="font-bold text-4xl flex items-center">
            coffee<strong className="text-light-red">break</strong>
          </h1>
        </aside>
        <hgroup className="flex flex-col items-center mt-12">
          <h2 className="font-bold">
            Descubra nosso inovador classificador de doenças de café!
          </h2>
          <p className="text-xs mt-6 text-center">
            Detecte e controle doenças em suas plantas de café com nosso
            inovador classificador baseado em aprendizado de máquina. <br />
            Aumente a produtividade e mantenha suas plantas saudáveis.
            Experimente agora mesmo!
          </p>
        </hgroup>
      </header>
      <main>
        <form onSubmit={handleOnSubmit}>
          <InputField
            label="Identificador da folha"
            onChange={(event: React.ChangeEvent<HTMLInputElement>) =>
              setPlantId(Number(event.target.value))
            }
          />
          <Loader isLoading={isLoading} />
          <DragAndDrop file={file} onChangeFile={setFile}/>
          
          {plantId && file ? (
            <Button name="Classificar" />
          ) : (
            <Button name="Classificar" disabled={true} />
          )}
          <ResultClassificationPopUp
            isOpen={isOpen}
            resultImage="https://random.imagecdn.app/500/150"
            results={["mais provável", "opção 2", "opção 3", "opção 4"]}
            onCloseModal={setIsOpen}
          />
        </form>
      </main>
    </article>
  );
}
