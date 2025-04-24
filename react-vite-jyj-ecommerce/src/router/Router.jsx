import MainLayout from '@/ui/layouts/MainLayout';
import { createBrowserRouter } from 'react-router-dom';
import Products from '../ui/components/fruits/Products';

const routes = [
  {
    path: '/',
    element: <MainLayout />,
    loader: () => '메인 레이아웃',
    Children: [
      {
        path: '',
        element: <Products></Products>,
        loader: () => '상품들',
      },
    ],
  },
];

const router = createBrowserRouter(routes);

export { router, routes };
