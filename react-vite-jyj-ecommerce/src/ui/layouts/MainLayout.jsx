import { Outlet } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';

//dev_2_fruit
const MainLayout = () => {
  return (
    <div className="vh-100 d-flex flex-column justify-content-between">
      <Header></Header>
      <Outlet></Outlet>
      <Footer></Footer>
    </div>
  );
};

export default MainLayout;
