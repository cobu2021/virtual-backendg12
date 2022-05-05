/*
  Warnings:

  - You are about to drop the column `clienteId` on the `pedidos` table. All the data in the column will be lost.
  - Added the required column `cliente_id` to the `pedidos` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "pedidos" DROP CONSTRAINT "pedidos_clienteId_fkey";

-- AlterTable
ALTER TABLE "pedidos" DROP COLUMN "clienteId",
ADD COLUMN     "cliente_id" INTEGER NOT NULL;

-- AddForeignKey
ALTER TABLE "pedidos" ADD CONSTRAINT "pedidos_cliente_id_fkey" FOREIGN KEY ("cliente_id") REFERENCES "usuarios"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
