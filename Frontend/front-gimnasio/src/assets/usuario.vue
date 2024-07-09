<template>
    <form action="">
        <div class="mx-auto max-w-xs">
                        <input
                            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
                            type="email" placeholder="Correo electrónico" />
                        <input
                            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                            type="password" placeholder="Contraseña" />
                        <a href="/dashboard">
                            <button
                            class="mt-5 tracking-wide font-semibold bg-indigo-500 text-gray-100 w-full py-4 rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none">
                            
                            <span class="ml-3">
                                Iniciar Sesión
                            </span>
                        </button>
                        </a>
                        <a href="/register">
                            <button
                            class="mt-5 tracking-wide font-semibold bg-indigo-500 text-gray-100 w-full py-4 rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none">
                            <svg class="w-6 h-6 -ml-2" fill="none" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round">
                                <path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" />
                                <circle cx="8.5" cy="7" r="4" />
                                <path d="M20 8v6M23 11h-6" />
                            </svg>
                            <span class="ml-3">
                                Registrar usuario
                            </span>
                        </button>
                        </a>
                        <p class="mt-6 text-xs text-gray-600 text-center">
                            Acepto los acuerdos de Bull´sGym
                            <a href="#" class="border-b border-gray-500 border-dotted">
                                Terminos de servicio
                            </a>
                            y sus
                            <a href="#" class="border-b border-gray-500 border-dotted">
                                Políticas de privacidad
                            </a>
                            
                        </p>
                    </div>


    </form>
</template>