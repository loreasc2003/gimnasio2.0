import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/login.vue'
import registerUserView from '@/components/registerUser.vue'
import dashboardView from '@/components/dashboard.vue'
import ProductosView from '@/components/productos.vue';
import DetallesProductosView from '@/components/deProductos.vue';
import PromocionesView from '@/components/promociones.vue';
import DetallesPromocionesView from '@/components/dePromociones.vue';
import PedidosView from '@/components/pedidos.vue';
import DetallesPedidosView from '@/components/dePedidos.vue';
import TransaccionPagosView from '@/components/transPagos.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: registerUserView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboardView,
      children: [
        {path: "/personas", name: "personas", component: registerUserView},
        { path: "/productos", name: "productos", component: ProductosView },
        { path: "/deProductos", name: "detallesProductos", component: DetallesProductosView },
        { path: "/promociones", name: "promociones", component: PromocionesView },
        { path: "/dePromociones", name: "detallesPromociones", component: DetallesPromocionesView },
        { path: "/pedidos", name: "pedidos", component: PedidosView },
        { path: "/dePedidos", name: "detallesPedidos", component: DetallesPedidosView },
        { path: "/transPagos", name: "transaccionPagos", component: TransaccionPagosView }
      ]
    }
  ]
})

export default router
