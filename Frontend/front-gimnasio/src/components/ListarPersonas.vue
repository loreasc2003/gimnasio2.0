<template>
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
     <div class="flex items-center justify-between flex-column flex-wrap md:flex-row space-y-4 md:space-y-0 pb-4 bg-white dark:bg-gray-900">
         <div>
             <!-- Dropdown menu -->
             <div id="dropdownAction" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600">
                 <ul class="py-1 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownActionButton">
                     <li>
                         <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Reward</a>
                     </li>
                     <li>
                         <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Promote</a>
                     </li>
                     <li>
                         <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Activate account</a>
                     </li>
                 </ul>
                 <div class="py-1">
                     <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Delete User</a>
                 </div>
             </div>
         </div>
         <label for="table-search" class="sr-only">Search</label>
     </div>
     <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
         <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
             <tr>
                 <th scope="col" class="p-4">
                     <div class="flex items-center">
                         <input id="checkbox-all-search" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                         <label for="checkbox-all-search" class="sr-only">checkbox</label>
                     </div>
                 </th>
                 <th scope="col" class="px-6 py-3">Foto</th>
                 <th scope="col" class="px-6 py-3">Nombre</th>
                 <th scope="col" class="px-6 py-3">Primer Apellido</th>
                 <th scope="col" class="px-6 py-3">Segundo Apellido</th>
                 <th scope="col" class="px-6 py-3">Titulo de Cortesia</th>
                 <th scope="col" class="px-6 py-3">Fecha de Nacimiento</th>
                 <th scope="col" class="px-6 py-3">Genero</th>
                 <th scope="col" class="px-6 py-3">Tipo de Sangre</th>
                 <th scope="col" class="px-6 py-3">Eliminar</th>
                 <th scope="col" class="px-6 py-3">Editar</th>
             </tr>
         </thead>
         <tbody>
             <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                 <td class="w-4 p-4">
                     <div class="flex items-center">
                         <input id="checkbox-table-search-1" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                         <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
                     </div>
                 </td>
                 <td class="px-6 py-4">
                     <img src="/img/bastman.png" width="50px"/>
                 </td>
                 <td class="px-6 py-4">Ana</td>
                 <td class="px-6 py-4">Martinez</td>
                 <td class="px-6 py-4">Lopez</td>
                 <td class="px-6 py-4">Dra.</td>
                 <td class="px-6 py-4">15/08/1985</td>
                 <td class="px-6 py-4">Mujer</td>
                 <td class="px-6 py-4">A-</td>
                 <td class="px-6 py-4"><a href="#" class="font-medium text-blue-600 dark:text-red-500 hover:underline">Eliminar</a></td>
                 <td class="px-6 py-4"><a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a></td>
             </tr>
             <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                 <td class="w-4 p-4">
                     <div class="flex items-center">
                         <input id="checkbox-table-search-2" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                         <label for="checkbox-table-search-2" class="sr-only">checkbox</label>
                     </div>
                 </td>
                 <td class="px-6 py-4">
                     <img src="/img/bastman.png" width="50px"/>
                 </td>
                 <td class="px-6 py-4">Carlos</td>
                 <td class="px-6 py-4">Fernandez</td>
                 <td class="px-6 py-4">Ruiz</td>
                 <td class="px-6 py-4">Ing.</td>
                 <td class="px-6 py-4">20/11/1992</td>
                 <td class="px-6 py-4">Hombre</td>
                 <td class="px-6 py-4">B-</td>
                 <td class="px-6 py-4"><a href="#" class="font-medium text-blue-600 dark:text-red-500 hover:underline">Eliminar</a></td>
                 <td class="px-6 py-4"><a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a></td>
             </tr>
             <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                 <td class="w-4 p-4">
                     <div class="flex items-center">
                         <input id="checkbox-table-search-3" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                         <label for="checkbox-table-search-3" class="sr-only">checkbox</label>
                     </div>
                 </td>
                 <td class="px-6 py-4">
                     <img src="/img/bastman.png" width="50px"/>
                 </td>
                 <td class="px-6 py-4">Laura</td>
                 <td class="px-6 py-4">Hernandez</td>
                 <td class="px-6 py-4">Vega</td>
                 <td class="px-6 py-4">Lic.</td>
                 <td class="px-6 py-4">12/03/1988</td>
                 <td class="px-6 py-4">Mujer</td>
                 <td class="px-6 py-4">AB+</td>
                 <td class="px-6 py-4"><a href="#" class="font-medium text-blue-600 dark:text-red-500 hover:underline">Eliminar</a></td>
                 <td class="px-6 py-4"><a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a></td>
             </tr>
         </tbody>
     </table>
 </div>
 
 
 
 </template>