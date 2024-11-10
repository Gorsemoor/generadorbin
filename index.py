import { useState } from 'react';
import { CreditCard } from 'lucide-react';

interface Bin {
  bin: string;
  tipo: string;
  categoria: string;
  pais: string;
  banco: string;
}

const tipos = ['Visa', 'Mastercard', 'Amex', 'Diners', 'Discover'];
const categorias = ['Clásica', 'Oro', 'Platino', 'Black'];
const paises = ['Estados Unidos', 'Mexico', 'España', 'Francia', 'Alemania'];
const bancos = ['BBVA', 'Santander', 'HSBC', 'Citi', 'American Express'];

const GeneradorBin = () => {
  const [bin, setBin] = useState<Bin>({
    bin: '',
    tipo: '',
    categoria: '',
    pais: '',
    banco: '',
  });

  const generarBin = () => {
    const tipo = tipos[Math.floor(Math.random() * tipos.length)];
    const categoria = categorias[Math.floor(Math.random() * categorias.length)];
    const pais = paises[Math.floor(Math.random() * paises.length)];
    const banco = bancos[Math.floor(Math.random() * bancos.length)];
    const bin = `${Math.floor(Math.random() * 9000) + 1000} ${Math.floor(Math.random() * 9000) + 1000} ${Math.floor(Math.random() * 9000) + 1000} ${Math.floor(Math.random() * 9000) + 1000}`;

    setBin({ bin, tipo, categoria, pais, banco });
  };

  return (
    <div className="max-w-md mx-auto p-4 bg-white rounded-lg shadow-md">
      <h2 className="text-lg font-bold mb-2">Generador de BIN</h2>
      <div className="flex justify-center mb-4">
        <CreditCard className="w-8 h-8 text-gray-600" />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">BIN:</label>
        <input
          type="text"
          value={bin.bin}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          readOnly
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Tipo:</label>
        <input
          type="text"
          value={bin.tipo}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          readOnly
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Categoría:</label>
        <input
          type="text"
          value={bin.categoria}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          readOnly
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">País:</label>
        <input
          type="text"
          value={bin.pais}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          readOnly
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Banco:</label>
        <input
          type="text"
          value={bin.banco}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          readOnly
        />
      </div>
      <button
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        onClick={generarBin}
      >
        Generar BIN
      </button>
    </div>
  );
};

export default GeneradorBin;